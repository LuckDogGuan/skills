# 基于wqb+MongoDB的边回测边储存alpha_info和pnl方案

- **链接**: https://support.worldquantbrain.com基于wqbMongoDB的边回测边储存alpha_info和pnl方案_34447173846423.md
- **作者**: 顾问 MZ45384 (大角羊) (Rank 51)
- **发布时间/热度**: 10个月前, 得票: 12

## 帖子正文

随着回测数量不断增加，提交前的准备工作也在复杂化，例如检查厂型alpha和相关性剪枝等等，而这些工作都需要pnl或alpha details。由于我本人有每提交一个alpha就重新检查可提交alpha的习惯，因此需要大量调用api，而api调用次数每小时限流，因此使用数据库来储存调用出来的信息一边后续直接从数据库中读取是最优解，论坛里不少前辈都用sqlite, mysql或oracle来储存，不过也有用mongoDB的， 综合来看，我认为后者操作更简单也更符合json格式；而wqb的concurrent_simulate刚好提供了可操作的回调函数。于是我采用了wqb+mongoDB的方式，代码如下：

```
import requestsimport timeimport pymongoclient = pymongo.MongoClient('localhost', 27017)alpha_db = client.alpha_dbalphas_cl = alpha_db.alphaspnls_cl = alpha_db.pnlsdef login():     # 登录平台        username = "3323438320@qq.com"    password = "UCkingdom0102"     # Create a session to persistently store the headers    s = requests.Session()     # Save credentials into session    s.auth = (username, password)     # Send a POST request to the /authentication API    response = s.post('https://api.worldquantbrain.com/authentication')    print(response.text)    return s  s = login()def wait_get(sess, url: str, max_retries: int = 10) -> "Response":    retries = 0    while retries < max_retries:        while True:            simulation_progress = sess.get(url)            if simulation_progress.headers.get("Retry-After", 0) == 0:                break            time.sleep(float(simulation_progress.headers["Retry-After"]))        if simulation_progress.status_code < 400:            break        else:            time.sleep(2 ** retries)            retries += 1    return simulation_progressdef save_alpha_from_children(n, resp, wqbs):   # 储存部分    global s        if resp.status_code != 200:        print(f'{n}, {resp}')        return    children = resp.json()['children']    count = 0    for url in children:        while True:              try:                data = wait_get(s, 'https://api.worldquantbrain.com/simulations/'+url).json()                if data['status'] == 'ERROR':                    print(n, 'irregular alpha:', data['message'])                    break                elif data['status'] == "COMPLETE" or data['status'] == "WARNING":                    alpha_id = data["alpha"]                    alpha = wait_get(s, f"https://api.worldquantbrain.com/alphas/{alpha_id}").json()                    if abs(alpha["is"]["sharpe"]) < 1 or abs(alpha["is"]["fitness"]) < 0.7:   # 选择满足一定标准的进行储存，标准因人而异                        break                    count += 1                    alphas_cl.insert_one(alpha)                    pnl = wait_get(s, 'https://api.worldquantbrain.com/alphas/' + alpha_id + '/recordsets/pnl').json()                    pnl['alpha_id'] = alpha_id                    pnls_cl.insert_one(pnl)                    break                else:                    print(n, data['status'])                    break            except Exception as e:                print(f'{n}, Error: {e}')                time.sleep(100)                s = login()                continue                    print(f'{n}, {resp}, {count} alpha and pnl saved successfully')
```

这段代码可以直接放到machine_lib.py里或者单独放一个py文件，然后在回测部分插入：

```
multi_alphas_2 = wqb.to_multi_alphas(sim_data_list_2, 10)concurrency = 8start = 0resps = await wqbs.concurrent_simulate(            multi_alphas_2,             concurrency,            start_point = start,            on_start=lambda vars: print(f'{vars['idx']}, {vars['url']}'),            on_success=lambda vars: save_alpha_from_children(vars['idx'], vars['resp'], wqbs),            on_failure=lambda vars: print(f'{vars['idx']}, {vars['resp']}'),        )
```

效果如下


> [!NOTE] [图片 OCR 识别内容]
> 1,
> https: //api
> Worldquantbrain . com/simulations /InBN24GDE4SPSUWhWAPPpeG
> 2, https : //api
> Worldquantbrain.com/simulations / EolyXSTT4VSbCWSQDJPN37
> 3, https: /Japi
> Idquantbrain. com/simulations
> ZdwVJddzjsgIbCkAUMbIkKT
> 4,
> https: //api
> Worldquantbrain. com/simulations /ukXWh3fgsGcg8ylzH7jxsEh
> 5,
> https: //api
> Worldquantbrain. com/simulations /pfshogIM4ITcfzamgsVcoV
> 6,
> https: //api
> Idquantbrain. com/simulations
> ZhdMChXl4L98UBXD4QWOSI
> 7, https
> //api.worldquantbrain. com/simulations
> bbx7ajtsglbJelsmjoNee
> 8,
> https: //api
> WOr
> Idquantbrain. com/simulations /ICUYWgCM4YmaBJRQyoISaC
> <Response [280]〉,
> O alpha and
> pnl
> saVed  successfully
> 9, https : //api
> Worldquantbrain.com/simulations / 2KPeSygVXSiGCFVONmQZiPo
> 6,
> <Response [280]〉,
> alpha and
> pnl
> saVed successfully
> 10, https 
> /api.worldquantbrain. com/ simulations / 3eyiFMSsSSgTSONSQJYnDgx
> 1, <Response [280]〉,
> 3 alpha and
> saved successfully
> 11, https
> /lapi
> Worldquantbrain. com/simulations
> OnUISItZ4MYCFfZcsYSWDg
> 5,
> <Response [280]〉,
> alpha and pnl saved successfully
> 12,
> https
> /api
> Worldquantbrain . com/simulations /IEIFVFaDL4pVgUSb1S094aq
> 7 ,
> <Response [280]〉,
> alpha and
> pnl
> saVed  successfully
> 13
> https
> Jabi.Worldauantbrain . com / simulations /1im3CbZS4VISHiZdO3W4UI
> WOr
> WOr
> pnl


---

## 讨论与评论 (2)

### 评论 #1 (作者: MY49971, 时间: 9个月前)

大哥，注意你的账户啊~

========================================================================================================================================================================

---

### 评论 #2 (作者: JX14975, 时间: 9个月前)

大佬，有测试过这样是否会影响回测速度吗？我不清楚wqb库的on_success输入是否会与接下来的异步回测抢时间（貌似在回测完后改颜色与名字是会的）？

另外，在跑GLB等地区可能会出现回测仍然在平台上进行但wqb库已经超时了的情况，这又是如何处理的？

---

