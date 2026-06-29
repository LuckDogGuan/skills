# WQB回测的同时用MongoDB保存Alpha信息和PNL

- **链接**: https://support.worldquantbrain.comWQB回测的同时用MongoDB保存Alpha信息和PNL_34094244284567.md
- **作者**: 顾问 MZ45384 (大角羊) (Rank 51)
- **发布时间/热度**: 10个月前, 得票: 13

## 帖子正文

最近拜读了社区里好几位大佬保存alpha信息和pnl的帖子，于是自己也写了一个，代码能力薄弱，还望批评指正。代码如下：

import requests

import time

import pymongo

client = pymongo.MongoClient('localhost', 27017)
alpha_db = client.alpha_db
alphas_cl = alpha_db.alphas
pnls_cl = alpha_db.pnls

def login():

    username = "your email"
    password = "your password"

    # Create a session to persistently store the headers
    s = requests.Session()

    # Save credentials into session
    s.auth = (username, password)

    # Send a POST request to the /authentication API
    response = s.post(' [https://api.worldquantbrain.com/authentication](https://api.worldquantbrain.com/authentication) ')
    print(response.text)
    return s

s = login()

def wait_get(sess, url: str, max_retries: int = 10) -> "Response":
    retries = 0
    while retries < max_retries:
        while True:
            simulation_progress = sess.get(url)
            if simulation_progress.headers.get("Retry-After", 0) == 0:
                break
            time.sleep(float(simulation_progress.headers["Retry-After"]))
        if simulation_progress.status_code < 400:
            break
        else:
            time.sleep(2 ** retries)
            retries += 1
    return simulation_progress

def save_alpha_from_children(n, resp, wqbs):
    global s

    if resp.status_code != 200:
        print(f'{n}, {resp}')
        return
    children = resp.json()['children']
    count = 0
    for url in children:
        while True:  
            try:
                data = wait_get(s, ' [https://api.worldquantbrain.com/simulations/'+url).json(](https://api.worldquantbrain.com/simulations/'+url).json() )
                if data['status'] == 'ERROR':
                    print(n, 'irregular alpha:', data['message'])
                    break
                elif data['status'] == "COMPLETE" or data['status'] == "WARNING":
                    alpha_id = data["alpha"]
                    alpha = wait_get(s, f" [https://api.worldquantbrain.com/alphas/{alpha_id}").json(](https://api.worldquantbrain.com/alphas/{alpha_id}%22).json() )
                    if abs(alpha["is"]["sharpe"]) < 1 or abs(alpha["is"]["fitness"]) < 0.7:   # 挑选满足一定条件的alpha保存
                        break
                    count += 1
                    alphas_cl.insert_one(alpha)
                    pnl = wait_get(s, ' [https://api.worldquantbrain.com/alphas/](https://api.worldquantbrain.com/alphas/) ' + alpha_id + '/recordsets/pnl').json()
                    pnl['alpha_id'] = alpha_id
                    pnls_cl.insert_one(pnl)
                    break
                else:
                    print(n, data['status'])
                    break
            except Exception as e:
                print(f'{n}, Error: {e}')
                time.sleep(100)
                s = login()
                continue

    print(f'{n}, {resp}, {count} alpha and pnl saved successfully')

这个函数放到wqb的回调函数里就可以在回测的同时储存alpha和pnl:

multi_alphas_1 = wqb.to_multi_alphas(sim_data_list_1[::-1], 10)
concurrency = 8
start = 0
resps = await wqbs.concurrent_simulate(
            multi_alphas_1,  
            concurrency,
            start_point = start,
            on_start=lambda vars: print(f'{vars['idx']}, {vars['url']}'),
             ***on_success=lambda vars: save_alpha_from_children(vars['idx'], vars['resp'], wqbs),*** 
            on_failure=lambda vars: print(f'{vars['idx']}, {vars['resp']}'),
        )

效果如图：


> [!NOTE] [图片 OCR 识别内容]
> 1,
> https : //api
> Worldquantbrain.com/ simulations _
> 15VMB37c15crcyXPTHJSMAR
> 2,
> https : //api
> Worldquantbrain. com/simulations _
> 2W7WYWeni4PobGxVZ4EUVX2
> 3, https
> /Japi
> Worldquantbrain. com/simulations
> IMSWLtIDE4XSbnnGkSdRLIf
> https
> /Japi
> Worldquantbrain.com/simulations _
> 4b21
> LV4OPaR4yCIGKIP3
> 5,
> https
> /lapi
> Worldquantbrain. com/simulations _
> 13YCiOSfNScbcBDIh3WjgGco
> 6,
> https
> /api
> Worldquantbrain. com/simulations
> 3YSIWjbFOS4ObGBWybLVODH
> 7 ,
> https
> /Japi
> Worldquantbrain. com/
> imulations /I8QKimbIH4iqbUNiqcxheox
> 8, https
> Japi
> Worldquantbrain. com/simulations
> bMAIOGVfSSFcwgnUgurVyj
> 7,
> <Response [280]〉,
> 3 alpha and
> pnl
> saVed sUCCessfully
> 9,
> https : //api
> Worldquantbrain.com/simulations /2Sjy4179f4QBbUsDUPffXMZ
> 8,
> <Response [280]〉
> 5 alpha and
> pnl
> saVed successfully
> 2,
> <Response [280]〉
> 2 alpha and
> pnl
> saved sUccessfully
> 〈Response
> [280]>,
> alpha and
> pnl
> saVed sUCCessfully
> 4,
> 〈Response [280]〉,
> 4 alpha and
> pnl
> SaVed
> sUCCessfuIIy
> 5,
> <Response [280]〉
> 3 alpha and
> pnl
> saved sUccessfully
> 10, https : //api
> dquantbrain. com/simulations / 2045p023k4Z68VpGXZSUPTA
> 11
> https : / /api
> Worldquantbrain . com/simulations / 3LVVWE8JG4VyaTrlgllsaMs
> Pm7L
> Worlc


---

## 讨论与评论 (0)

