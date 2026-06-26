# 新人经验分享

- **链接**: [Commented] 新人经验分享.md
- **作者**: CG48008
- **发布时间/热度**: 1年前, 得票: 9

## 帖子正文

## 异步回测，提高效率

顾问课程提供的是将10个tasks封装到一个池子，进行回测，但是这10个tasks回测的速度是不一样的，因此使用多线程或者异步等方法可以提高回测效率，下面是代码分享

原理为控制并发数为 max_tasks_num，当有一个 task 先测完，则立马回测一个新的 task，使同一时刻正在回测的数量永远保持 max_tasks_num 个，最大限度利用服务器资源

```
import asyncioimport timeimport requestsfrom tqdm.asyncio import tqdm as tqdm_asynciofrom lib import apifrom lib.user import login### my testdef gen_tasks(alpha_list, limit_of_children_simulations):    tasks = [        alpha_list[i : i + limit_of_children_simulations]        for i in range(0, len(alpha_list), limit_of_children_simulations)    ]    return tasksdef generate_sim_data(alpha_list, region, uni, neut):    sim_data_list = []    for alpha, decay in alpha_list:        simulation_data = {            "type": "REGULAR",            "settings": {                "instrumentType": "EQUITY",                "region": region,                "universe": uni,                "delay": 1,                "decay": decay,                "neutralization": neut,                "truncation": 0.08,                "pasteurization": "ON",                "unitHandling": "VERIFY",                "nanHandling": "ON",                "language": "FASTEXPR",                "visualization": False,            },            "regular": alpha,        }        sim_data_list.append(simulation_data)    return sim_data_listasync def simulate_a_task(task, index):    s: requests.Session = login()    # send post    try:        simulation_response = s.post(api.simulation, json=task)        progress = simulation_response.headers["Location"]    except:        # 重大报错        print("loc key error: %s" % simulation_response.content)        time.sleep(60 * 3)        s = login()    # wait progress    try:        while True:            simulation_progress = s.get(progress)            retry_after = float(simulation_progress.headers.get("Retry-After", 0))            if retry_after == 0:                break            await asyncio.sleep(retry_after)        status = simulation_progress.json().get("status", 0)        if status != "COMPLETE":            print(f"Task {index} not complete: {progress}")    except KeyError:        print(f"KeyError for task {index}: {progress}")    except Exception as e:        print(f"Error for task {index}: {e}")import lib.util.config_reader as cfgasync def my_multi_simulate(tasks, start):    """    @param tasks: 待回测的任务列表    @param neut: neutralization 参数    @param region: region 参数    @param universe: universe 参数    @param start: 从第几个任务开始    @param max_tasks_num: 最大并发数量    """    max_tasks_num = cfg.max_tasks_num    neut = cfg.neutralization    region = cfg.region    universe = cfg.universe    # s: requests.Session = login()    sem = asyncio.Semaphore(max_tasks_num)  # 定义全局的 Semaphore    async def wrapped_task(task, index, progress_bar):        async with sem:  # 使用共享的 Semaphore            await simulate_a_task(task, index)        progress_bar.update(1)  # 更新进度条    # 过滤起始任务    filtered_tasks = [        (index, generate_sim_data(task, region, universe, neut))        for index, task in enumerate(tasks)        if index >= start    ]    # 创建异步进度条    with tqdm_asyncio(        total=len(filtered_tasks), desc="Simulating Tasks"    ) as progress_bar:        await asyncio.gather(            *[wrapped_task(task, index, progress_bar) for index, task in filtered_tasks]        )    print("Simulations all done")
```

实测24小时能回测5w+代码


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 12/16/2024
> Simulated Alphas: 63.016
> 4OK
> 2OK


## 获取目前能使用的 group fields

比如我这里获取USA D1 ILLIQUID_MINVOL1M 下的 group fields

```
def get_group_datafields_test():    url = "https://api.worldquantbrain.com/data-fields?delay=1&instrumentType=EQUITY&limit=20&offset={x}&region=USA&type=GROUP&universe=ILLIQUID_MINVOL1M"    s: requests.Session = login()    count = s.get(url.format(x=0)).json()["count"]    datafields_list = []    for x in range(0, count, 50):        datafields = s.get(url.format(x=x))        datafields_list.append(datafields.json()["results"])    datafields_list_flat = [item for sublist in datafields_list for item in sublist]    datafields_df = pd.DataFrame(datafields_list_flat)    output_csv = "./data/group_datafields.csv"    datafields_df.to_csv(output_csv, index=False)  # Write DataFrame to CSV file
```

## 
> [!NOTE] [图片 OCR 识别内容]
> escriptiol dataset
> category
> subcategc region
> UnIerse
> type
> COVeraCI
> Jsercounl
> Iha
> OUIpyramidM themes
> anl52_200 CIO split
> {id:
> anal} {id: 'anal {id': 'anal USA
> ILLIQUID_
> GROUP
> 8795
> 1.2
> anl52_200 C20 split
> {id': 'anal {id: 'anal} {id': 'anal} USA
> ILLIQUID
> GROUP
> 12
> anl52_200 C5O split
> {id:
> anal {id: 'anal} {id': 'anal} USA
> ILLIQUID_IGROUP
> anl52_200
> split th {id: 'anal} {id': 'anal} {id: 'anal} USA
> ILLIQUID_IGROUP
> 0.75
> anl52_200 C5 split th {id:
> anal {id: 'anal {ic: 'anal} USA
> ILLIQUID_
> GROUP
> 8508
> anl52_300 CI0 split
> {id': 'anal}
> ic: 'ana
> {id': 'anal} USA
> ILLIQUID_IGROUP
> anl52_300 C20 split
> {id:
> 3nal}
> id
> 3na
> id: 'anal USA
> ILLIQUID_IGROUP
> anl52_300 C50 split
> {id': 'anal {id:
> 3na
> "id: 'anal} USA
> ILLIQUID_
> GROUP
> 10|an152_300 C2 split th {id: 'anal {id:
> anal {id: 'anal} USA
> ILLIQUID_
> GROUP
> 95
> anl52_300 C5 split th {id': 'anal} {id: 'ana
> {id': 'anal} USA
> ILLIQUID
> GROUP
> 
> 12|anl52_300 CIO split
> {id: 'anal
> id: 'ana
> id: 'anal USA
> ILLIQUID_IGROUP
> 13|anl52_300 C20 split
> {id': 'anal {id:
> 3na
> "id': 'anal} USA
> ILLIQUID_IGROUP
> 14|anl52_300 C50 split
> {id: 'anal {id:
> anal {id: 'anal USA
> ILLIQUID_
> GROUP
> 15|anl52_300 C2 split th { id': 'anal} {id: 'ana
> {id': 'anal} USA
> ILLIQUID_IGROUP
> 16|anl52_300 C5 split th {id': 'anal {id:
> 3na
> id: 'anal USA
> ILLIQUID_IGROUP
> 17
> countny
> Country g {id: 'pvl  {id: 'Dv
> {ic:
> DV-DUSA
> ILLIQUID_
> GROUP
> 100
> 03
> 18
> CUrrency
> Currency |{id': 'pvl', {id': 'pV,
> {id:
> DV-pUSA
> ILLIQUID_
> GROUP
> 19
> exchange Exchange {id: 'pvl'  {id:'pv,
> {id: 'Dv-DUSA
> ILLIQUID
> GROUP
> 1523
> 20 |industry
> Industry g {id': 'pvl , {id:'pv ,
> {id: 'DV-DUSA
> ILLIQUID_IGROUP
> 21
> market
> Market gr {id: 'pvl , {id:'Dv ,
> {id': 'DV-DUSA
> ILLIQUID_IGROUP
> 8905
> 22 |sta2_top3( statistical{id': 'pV3O {id:'pv
> {id: 'DV-DUSA
> ILLIQUID_
> GROUP
> 23 |sta2_tOp3( statistical { id: 'pv30 {id: 'pv ,
> {id': 'DV-DUSA
> ILLIQUID_IGROUP
> 16
> 24 |sta2_top3( statistical { id: 'pv30 {id: 'pv
> {ic:
> DV-pUSA
> ILLIQUID_IGROUP
> 25
> Sta2_top3( statistical_{id': 'pv30 {id:'pv,
> {id:
> DV-DUSA
> ILLIQUID_
> GROUP
> 盈
> 26 |sta2_tOp3( statistical {'id': 'pV30 {'id: 'pv
> {ic:
> DV-pUSA
> ILLIQUID_
> GROUP
> 27
> sta2_tOp3( statistica
> {id: 'Dv30 {id: 'pv,
> {id: 'Dv-DUSA
> ILLIQUID_
> GROUP
> 28 |5ta2_top3( statistical {id': 'pv30 {id: 'pv,
> {id: 'DV-DUSA
> ILLIQUID_IGROUP
> 32
> 「 -1
> 「 -1
> 「 -1
> 1 !
> ULUICLIIC
> LCDCLID
> grOUP
> dataflelds


## check submission 技巧

我的思路是把能点check按钮的alpha全部check，能过就打上标记，后续再考虑筛选

check 前，可以筛出没有fail的alpha，用于 check，更有效率

```
def is_check_no_fail(alpha):    """    @desc: 筛出没有 fail 的 alphas    """    checks = alpha["is"]["checks"]    for check in checks:        if check["result"] == "FAIL":            return False    return True
```

```
def get_can_submit_alphas(start_date: str, end_date: str):    """    @desc:    """    s = login()    result = []    template = (        api.self_alphas        + "?status=UNSUBMITTED%1FIS_FAIL&is.sharpe%3E1.58&is.fitness%3E1&order=-is.sharpe&hidden=false"        + "&limit=100"        + "&offset={offset}"        + "&color!=RED"        + "&dateCreated>="        + start_date        + "T00:00:00-05:00&dateCreated<"        + end_date        + "T00:00:00-05:00"    )    url = template.format(offset=0)    # print(url)    response = s.get(url)    try:        count = response.json()["count"]        alpha_list = response.json()["results"]        for alpha in alpha_list:            if is_check_no_fail(alpha) == True:                result.append([alpha["id"], alpha["regular"]["code"]])    except:        print("request to check alphas error" + response.content)    # print(count)    for x in tqdm(range(100, count, 100)):        # print(x)        url = template.format(offset=x)        # print(url)        response = s.get(url)        try:            alpha_list = response.json()["results"]            for alpha in alpha_list:                if is_check_no_fail(alpha) == True:                    result.append([alpha["id"], alpha["regular"]["code"]])        except:            print("request to check alphas error" + response.content)    return result
```

## 推荐一些小工具

### 论文阅读软件推荐 ReadPaper

[https://readpaper.com/download](https://readpaper.com/download)

免费版就完全够用，支持笔记、翻译选中文本


> [!NOTE] [图片 OCR 识别内容]
> Readpaper
> 一 ^& X
> 文献列表
> textual sentiment Opti。。
> SSrn_id3506781_cod23..
> Do Option-Based Mea..
> Dividend capture retur。。
> 翻译
> 资料
> 笔
> 学91
> : X
> Dividend captlre retirns: anomaly OI
> 有道
> 百
> IDEA
> Al翻译
> 廿  勿
> 咨
> Iisk premill? Evidence fron the eqlity
> 园
> 回
> options markets
> 鼠标选中对应的句子。即可自动翻译
> 按住Ctrl选取多段文字迸行翻译
> Brian Healy
> Conall 0 Sullivan
> Finance and Risk Engineering
> Smurfit Business School
> New York University
> University College Dublin
> bhgg@nyl.edu
> Colall.osullivan@ucd.ie
> +1347463 2267
> +353
> 716 8836
> 1102
> 1309
> ONOOantBR


集成了论文搜索功能，也能自己添加论文网站，将论文下载直接导入阅读


> [!NOTE] [图片 OCR 识别内容]
> Readpaper
> & X
> SSF
> i3506781_code3。
> ReadPaper
> 百庹学术
> ssrn_id3506781_c0de352464.pdf
> 49
> 90%
> 十 |
> 囚
> 0
>   邱 :
> AFI
> 知网
> SCI
> HUB
> Sci-hub
> WOs
> SSRN
> Do Option-Based Measures 0f Stock Mispricing Find Investment
> Opportunities or Market Frictions?
> Google
> 添加学术网站
> Martijn Cremers"
> Rusln
> Goyenkot
> Paul Schult 
> und
> Stcphen Szaurab
> Ahstriol
> This paper considers
> plethoraof
> based mcasures ofstock mist
> 检测到PDF,
> 是否导入?
> literature. Thesc mcasurcs arc bascd on differenccs betwccn implicd 9
> i implied volatilities across options, and on option
> Volume。
> mncasures indicatc are mispriced arc small andlor hard to borrow。
> 导入到 末分类文献
> aC omitteg, returns to short
> selling are insignificant for some ofthe me
> Others
> Threc of the ninc mcasures, however, predict positive abnortal
> portfolios without obvious market frictions, suggcsting that 
> 键导入
> Oplion 
> trading
> Wher
> consli
> they


### 代码格式化：black

也就是将格式杂乱的代码整理，让代码美观易读

安装：

```
pip install blackpip install black[jupyter]
```

使用方法：

```
black .  # 格式化该文件夹下所有代码black file_name  # 格式化该文件的代码
```

欢迎大家留言讨论

---

## 讨论与评论 (7)

### 评论 #1 (作者: YZ92137, 时间: 1年前)

这个好，这两天就换上试试，感谢分享

---

### 评论 #2 (作者: 顾问 SD17531 (Rank 15), 时间: 1年前)

getd atafield使用时,服务器最多返回10000条数据,如果数据超过了一万条,后续的数据就获取不到了,该怎么处理?

---

### 评论 #3 (作者: XX42289, 时间: 1年前)

太有实力了，终于有人把异步async发上来了，就是作者 [CG48008](/hc/en-us/profiles/27705934439703-CG48008) ，您的代码格式好像分叉的很厉害，格式太长了，不方便阅读，不知道这怎么样可以改的紧凑一点。

It's so powerful. Finally, someone sent asynchronous asynchronous up. It's the author CG48008. Your code format seems to be forked very badly. The format is too long and inconvenient to read. I don't know how to make it more compact.

---

### 评论 #4 (作者: GL61467, 时间: 1年前)

[顾问 SD17531 (Rank 15)](/hc/en-us/profiles/27215746752791-顾问 SD17531 (Rank 15))  时间跨度缩短点，从天缩短到小时级别就可以了

---

### 评论 #5 (作者: GL61467, 时间: 1年前)

[顾问 SD17531 (Rank 15)](/hc/en-us/profiles/27215746752791-顾问 SD17531 (Rank 15))  看这篇文章

# [【工程技术分享】如何将自己的回测过的alpha全部下载到本地]([L2] 【工程技术分享】如何将自己的回测过的alpha全部下载到本地_28883893064599.md)

---

### 评论 #6 (作者: CG48008, 时间: 1年前)

[XX42289](/hc/en-us/profiles/14187300941847-XX42289)

你可以考虑使用模块和包，将代码解耦

---

### 评论 #7 (作者: MF59400, 时间: 11个月前)

大佬,我根据你的异步代码回测, 我回测下来大概是同步的0.9倍左右, 我平时同步回测在2.5-3W, 这几天测试了异步,不增反降了.大佬能给点找bug的思路吗

---

