# 【PPAC/Super Alpha Submitter】基于coze 生成描述，提交因子

- **链接**: https://support.worldquantbrain.com[L2] 【PPACSuper Alpha Submitter】基于coze 生成描述提交因子_36489114520471.md
- **作者**: ZY25247
- **发布时间/热度**: 7 months ago, 得票: 11

## 帖子正文

基于coze api 生成PPAC Alpha或SuperAlpha 描述信息，通过brain 接口修改目标alpha的描述，再执行提交，代码开箱即用

1. coze 生成描述

coze.py

```
import requestsimport json,timefrom six import print_api_key = "key" #替换成自己的keybotid = "botid" #替换成自己的botidbaseUrl =  'https://api.coze.cn/v3/chat'headers = {    "Authorization": f"Bearer {api_key}",    'Content-Type': 'application/json'}def processQuestionAnswer(response_data):    if response_data['code']:        print("应答异常：",response_data['msg'])    else:        data = response_data['data']        count = 0        for item in data:            if item['type']=='answer':                content_str = item['content']                print("大模型应答：",content_str)                return content_str            elif item['type']=='follow_up':                if count==0:                    print("您可以参考如下方式提问：")                print(f"☆ 问题{count+1}：",item['content'])                count += 1                return Nonedef getQuesyionAnswer(conversationID,chatID):    params = { "bot_id": botid,"task_id": chatID }    getChatStatusUrl = baseUrl+f'/retrieve?conversation_id={conversationID}&chat_id={chatID}&'    while True:        response = requests.get(getChatStatusUrl, headers=headers, params=None)        if response.status_code == 200:            response_data = response.json()            print(f"response_data:\n{json.dumps(response_data,indent=4, ensure_ascii=False)}")            status = response_data['data']['status']            if status == 'completed':                # 从响应中提取实际的应答内容                getChatAnswerUrl = baseUrl+f'/message/list?chat_id={chatID}&conversation_id={conversationID}'                response = requests.get(getChatAnswerUrl, headers=headers, params=params)                if response.status_code == 200:                    response_data = response.json()                    print("模型返回数据:\n", json.dumps(response_data,indent=4, ensure_ascii=False))                    return processQuestionAnswer(response_data)                break            else:                print(f"任务仍在处理中，状态: {status}")                time.sleep(3)  # 等待5秒后再次检查        else:            print(f"请求失败，状态码: {response.status_code}")            break    return Nonedef questionService(questionText):    type = questionText["type"]    if type == "SUPER":        code = questionText["selection"]["code"]        text = f"{code} 简单描述该因子，要求英文，120字符左右"    else:        template_str = '''        Idea:         Rationale for data used:         Rationale for operators used:         '''        code = questionText["regular"]["code"]        # 可以按照自己需要来修改请求文本        text = f"{code} 按照以下模版描述该因子，要求英文，120字符左右，模版:{template_str}"    # 定义API的URL和授权令牌    data = {        "bot_id": botid,        "user_id": "11233",        "stream": False,        "auto_save_history": True,        "additional_messages": [            {                "role": "user",                "content": text,                "content_type": "text"            }        ]    }    # 发送POST请求    print(f"请求信息:{json.dumps(data,indent=4, ensure_ascii=False)}")    response = requests.post(baseUrl, headers=headers, data=json.dumps(data))    # 检查响应状态码    if response.status_code == 200:        # 解析响应内容        response_data = response.json()        print("响应内容:", json.dumps(response_data,indent=4, ensure_ascii=False))        chatid = response_data['data']['id']        answer = response_data.get("answer")        conversation_id = response_data['data']['conversation_id']        print(f"chatid={chatid},智能体应答: {answer}")        return getQuesyionAnswer(conversation_id,chatid)    else:        print("请求失败，状态码:", response.status_code)        print("错误信息:", response.text)
```

coze 免费资源点每日是500，完全能满足我们的需要


> [!NOTE] [图片 OCR 识别内容]
> 扣子资源点
> 个人免费版
> 487/500
> (每日重置)


api_key 获取：


> [!NOTE] [图片 OCR 识别内容]
> 个人空间
> OAuth 应用
> 已授权应用
> 服务身份及凭证
> ~人访问令
> 添加
> 十
> 创建
> 用于其他应用程序和平台的个人访问令牌。详细说明请查看:  鉴权方式概述
> 主页
> 不要与他人共享您的个人访问令牌。也不要在浏览器或其他客户端代码中暴露它。以保护您账户的安全。若在公开场合发现任何泄露的个人访问令牌。该令牌可能会被自动禁用。
> 由
> 项目开发
> 资源库
> 名称
> 创建时间
> 最近使用时间
> 过期时间
> 状态
> 操作
> 任务中心
> 效果评测
> Secret token
> 2024-09-1111:54:36
> 2024-09-1116:35:45
> 永久有效
> 有效
> 空间配置
> Secret token0ol
> 2025-11-2018:37:32
> 2025-11-2111.54:16
> 2025-12-20
> 有效
> 模板商店
> 插件商店
> 作品社区
> API 管理
> 扣子资源点
> 个人免费版
> 487/500
> (每日重置)


botid 获取


> [!NOTE] [图片 OCR 识别内容]
> 扣子
> 项目开发
> 搜索项目
> 十
> 文件夹
> 十  项目
> 个人空间
> 项目
> 十
> 创建
> 全部
> 全*
> 创建
> 主页
> alpha
> |展示
> 邮
> 项目开发 
> alpha因=
> 资源库
> 什么是扣子
> 智能体
> 答案之书
> :体
> 任务中心
> WeWer
> 10;09
> ewenge
> 最近编辑 06-1711:19
> 效果评测
> 答案之书
> 空间配置
> 扣子[月
> 创建助手
> 通过两个 
> 你心底的疑问
> 用户提供具体故事创建相关内容以 
> 手扣子的
> 求输出的智能助手
> 模板商店
> 智能体支持「提示词对比」和「模型对比」调试啦!
> 义
> 应用
> !
> 插件商店
> Wewer
> 创建智能体
> 创建应用
>  Beta
> ewenge
> 最近编辑 05-1411:20
> 作品社区
> 适围干快谏搭建对话式智能体
> 适用于搭建包含用户界面的完整应用
> API 管理
> 坎垂纶
> ~
 在项目开发中，通过添加项目，创建一个新的智能体，这个智能体的id就是botid


> [!NOTE] [图片 OCR 识别内容]
> coze.cnlspace
> 1/bot17574757857284308992


2. alpha提交

防止同一个alpha 重复调用coze，造成额度的浪费，使用了数据库存储要提交的alpha 和该alpha 的描述。

表结构

```
CREATE TABLE `sa_alpha_submit` (  `id` int(11) NOT NULL AUTO_INCREMENT,  `alpha_id` varchar(128) NOT NULL,  `aplha_json` json DEFAULT NULL,  `add_date` datetime DEFAULT NULL,  `up_date` datetime DEFAULT NULL,  `status` varchar(32) DEFAULT NULL,  `type` varchar(32) DEFAULT NULL,  `descr` text,  PRIMARY KEY (`id`),  UNIQUE KEY `alpha_id` (`alpha_id`)) ENGINE=InnoDB AUTO_INCREMENT=1326 DEFAULT CHARSET=utf8mb4
```

提交代码：submit.p

```
# -*- coding: utf-8 -*-import pymysqlfrom pymysql.cursors import DictCursorfrom threading import Lockimport timeimport jsonfrom alpha.coze import questionServicefrom alpha.machine_lib import loginfrom datetime import date, datetime  # 需要 datetime 来处理时间戳或日期# --- 用户配置 ---TOBE_CONSULTANT_DAY = "2025-10-30"# 要操作的目标区域TARGET_REGION = "EUR"# 并发修改的线程数MAX_WORKERS = 10# 线程池配置（根据数据库性能调整）BATCH_SIZE = 500  # 每批次插入条数MAX_WORKERS = 4    # 最大线程数（建议=CPU核心数×2，避免连接过载）THREAD_SAFE_COUNTER = 0  # 线程安全的插入计数器COUNTER_LOCK = Lock()     # 计数器锁# 数据库配置# 改为自己的MYSQL_CONFIG = {    'user': '',    'password': '',    'host': '',    'database': '',    'charset': 'utf8mb4',    'connect_timeout': 10}def up_alpha_properties(s, alpha_id, params: str = None):    """    一个专门用于修改alpha描述的方法。    """    response = s.patch(        f"https://api.worldquantbrain.com/alphas/{alpha_id}", json=params    )    if response.status_code == 200:        print(f"成功将 Alpha 描述修改为 '{params}'。")        return "SUCCESS"    else:        print(f"修改 Alpha 描述失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"def up_alpha_color(s, alpha_id, color):    """    一个专门用于修改alpha颜色的函数。    """    params = {"color": color}    response = s.patch(        f"https://api.worldquantbrain.com/alphas/{alpha_id}", json=params    )    display_color = "无" if color is None else color    if response.status_code == 200:        print(f"成功将 Alpha {alpha_id} 的颜色修改为 '{display_color}'。")        return color  # 返回成功设置的颜色，方便统计    else:        print(f"修改 Alpha {alpha_id} 颜色失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"# --- 数据库交互函数 ---def get_db_connection():    """建立并返回一个新的数据库连接"""    return pymysql.connect(**MYSQL_CONFIG, cursorclass=DictCursor)def fetch_sim_configs_from_db():        conn = get_db_connection()    sim_configs = []    try:        with conn.cursor() as cursor:                        sql = '''            SELECT id, alpha_id,type,aplha_json,descr FROM sa_alpha_submit                    WHERE status ='UNSUBMITTED' and  type ='SUPER' order by                         JSON_EXTRACT(JSON_EXTRACT(aplha_json, '$.test'), '$.fitness') desc,                         JSON_EXTRACT(JSON_EXTRACT(aplha_json, '$.test'), '$.sharpe') desc,                         JSON_EXTRACT(JSON_EXTRACT(aplha_json, '$.test'), '$.margin') desc,                         JSON_EXTRACT(JSON_EXTRACT(aplha_json, '$.test'), '$.returns') desc,                         JSON_EXTRACT(JSON_EXTRACT(aplha_json, '$.test'), '$.profit') desc                        limit 100            '''            cursor.execute(sql)            sim_configs = cursor.fetchall()    except pymysql.Error as e:        print(f"从数据库读取数据失败: {e}")    finally:        if conn:            conn.close()    print(f"从数据库获取到 {len(sim_configs)} 条待处理记录。")    return sim_configsdef submit(s, alpha_id):    def submit_inner(s, alpha_id):        """Inner submit function with rate limiting handling"""        try:            result = s.post(f"https://api.worldquantbrain.com/alphas/{alpha_id}/submit")            print(f"Alpha submit, alpha_id={alpha_id}, status_code={result.status_code}")            print(f"Response headers: {dict(result.headers)}")            # Handle rate limiting            while True:                if "retry-after" in result.headers:                    wait_time = float(result.headers["Retry-After"])                    print(f"Rate limited, waiting {wait_time * 20} seconds...")                    time.sleep(wait_time * 20)                    result = s.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/submit")                    print(f"Retry GET response, status_code={result.status_code}")                    print(f"Retry headers: {dict(result.headers)}")                else:                    break            return result        except Exception as e:            print(f'Connection error: {e}, attempting to re-login...')            new_session = login()            if new_session is None:                return None            return submit_inner(new_session, alpha_id)    attempt_count = 1    result = None    while attempt_count < 3:        print(f"Submit attempt {attempt_count} for alpha {alpha_id}")        result = submit_inner(s, alpha_id)        if result is None:            print(f"Failed to submit {alpha_id} - connection error")            return None        if result.status_code == 200:            print(f"✅ Alpha {alpha_id} submit successful, status_code={result.status_code}")            return result        elif result.status_code == 403:            print(f"❌ Alpha {alpha_id} submit forbidden, status_code={result.status_code}")            return result        else:            print(f"⚠️ Alpha submit fail, status_code={result.status_code}, alpha_id={alpha_id}, attempt= {attempt_count}, result= {result}")            print(f"Waiting 1 minutes before retry...")            time.sleep(60)  # 1 minutes = 60 seconds            attempt_count += 1            continuedef submit_alpha(alpha_id, s, account_choice=None):    # Submit the alpha    res = submit(s, alpha_id)    if res is None:        print(f"Failed to submit {alpha_id} - connection error")        return False    # Parse response    if res.text:        try:            res_json = res.json()            print(f"Submit response parsed successfully,res_json = {res_json}")        except json.JSONDecodeError:            print(f"Submit response is not JSON: {res.text[:200]}...")            return False    else:        print(f"Submit response has no text content")        return False    # Check for various error conditions    if 'detail' in res_json and res_json['detail'] == 'Not found.':        print(f"{alpha_id} - Alpha ID not found")        return False    # Check submission status    submitted = True    if 'is' in res_json and 'checks' in res_json['is']:        for item in res_json['is']['checks']:            if item['name'] == 'ALREADY_SUBMITTED':                submitted = True                print(f"{alpha_id} - Already submitted")                break            if item['result'] == 'FAIL':                submitted = False                print(f"{alpha_id} - {item['name']} check failed, limit = {item['limit']}, value = {item['value']}")                break    if submitted:        print(f'{alpha_id} - Submission successful!')        return True    else:        return Falsedef update_alpha_status_in_db(alphaId, status):    """更新数据库中的alpha_id和up_date"""    conn = get_db_connection()    current_date_str = date.today().isoformat()    success = False    try:        with conn.cursor() as cursor:            sql = "UPDATE sa_alpha_submit SET status = %s, up_date = %s WHERE alpha_id = %s"            cursor.execute(sql, (status, current_date_str, alphaId))            conn.commit()            success = True            print(f"数据库记录 alphaId:{alphaId} 更新成功")    except pymysql.Error as e:        print(f"更新数据库记录 alphaId {alphaId} 更新失败: {e}")        if conn:            conn.rollback()    finally:        if conn:            conn.close()    return successdef update_alpha_descr_in_db(alphaId, description):    """更新数据库中的alpha_id和up_date"""    conn = get_db_connection()    current_date_str = date.today().isoformat()    success = False    try:        with conn.cursor() as cursor:            sql = "UPDATE sa_alpha_submit SET descr = %s WHERE alpha_id = %s"            cursor.execute(sql, (description, alphaId))            conn.commit()            success = True            print(f"数据库记录 alphaId:{alphaId} 更新成功")    except pymysql.Error as e:        print(f"更新数据库记录 alphaId {alphaId} 更新失败: {e}")        if conn:            conn.rollback()    finally:        if conn:            conn.close()    return success# ===================================================================# PART 2: 主逻辑# ===================================================================if __name__ == "__main__":    s = login()    print("-" * 40)    print("开始获取super alpha.....")    print("-" * 40)    # --- 获取数据库alpha ---    alphas_to_save = fetch_sim_configs_from_db()    # --- 修改 Alphas 描述 ---    total_data = len(alphas_to_save)    if not total_data:        print("没有有效数据可操作")        exit(-1)    alpha_count = 0    alphas_super_count = 0    for i, alpha in enumerate(alphas_to_save):        alpha_id = alpha["alpha_id"]        alpha_type = alpha["type"]        aplha_json_str = alpha["aplha_json"]        aplha_json = json.loads(aplha_json_str)        descr = alpha["descr"]        if descr == "" or descr == None:            descr = questionService(aplha_json)            if descr != None:                print(f" 豆包 cozi 描述: {descr}")                update_alpha_descr_in_db(alpha_id, descr)        print(f"正在处理第 {i+1} 条数据，Alpha ID: {alpha_id}")        if alpha_type == "SUPER":            if descr == None:                descr = "This selection expression filters assets based on key conditions: items must be owned ('own'), color config."            params = {"combo": {"description":"A combo expression combines multiple selection criteria or data operations to create a refined dataset. It uses logical operators (AND/OR) to connect conditions, enabling precise filtering for specific analytical needs in quantitative finance or data analysis workflows."},"selection":{"description":f"{descr}"}}        else:            if descr == None:                code = aplha_json["regular"]["code"]                investabilityConstrained = aplha_json["is"]["investabilityConstrained"]                settings = aplha_json["settings"]                descr = f'''                            Idea: {code}                            Rationale for data used: {investabilityConstrained}                            Rationale for operators used: {settings}                            '''            params = {"regular": {"description":f"{descr}"}}        print(params)        # 更新描述        up_alpha_properties(s, alpha_id, params)        # 提交        ret = submit_alpha(alpha_id, s)        if ret:            print("提交成功")            # 更新数据库，退出            update_alpha_status_in_db(alpha_id, "SUBMITTED")            if alpha_type == "SUPER":                alphas_super_count += 1                if alphas_super_count >=1:                    print(f"已处理超级alpha:{alphas_super_count}，跳过处理")                    exit(0)            else:                alpha_count +=1                if alpha_count >=4:                    print(f"已处理普通alpha:{alpha_count}，跳过处理")                    exit(0)        else:            up_alpha_color(s, alpha_id, "RED")            update_alpha_status_in_db(alpha_id, "FAIL")            print("提交失败")
```

---

## 讨论与评论 (2)

### 评论 #1 (作者: JR57542, 时间: 5 months ago)

整挺好，感谢，这下省事多了嘿嘿

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ 引擎状态：在线 [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(稳健性 * 创造力)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

### 评论 #2 (作者: HS67684, 时间: 3 months ago)

太感谢了

---

