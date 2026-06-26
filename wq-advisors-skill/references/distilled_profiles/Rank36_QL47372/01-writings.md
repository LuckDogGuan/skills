# 顾问 QL47372 (Rank 36) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 QL47372 (Rank 36) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: BRAIN API及日常回测时常见的报错代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md
- **讨论数**: 5

以下是一些可能的错误消息，它们的可能原因以及解决方案：

- **1. **Attempted to use unknown variable**尝试使用未知变量**

- 数据不可用
   - 表达式中包含了一个不可用的变量。检查你的变量是否有拼写错误，或者你是否在设置中使用了正确的区域。提示：如果在表达式中正确使用，数据字段和操作符的字体颜色会显示为蓝色。

- **2. **Unexpected end of input**意外的输入结束**

- 语法错误，Alpha没有结尾
   - 一个常见的语法错误通常来自于最后一行的Alpha缺少括号或缺少分号。
   - 例如："rank(sales/assets" 会引发此错误

- **3. **Expression cannot be empty**表达式不能为空**

- 在最后一行加分号
   - 该错误通常在用户将他们的alpha分配给一个变量，但实际上没有在之后调用它时引发。
   - 例如： "alpha = -ts_delta(close,5);" 会引发错误，但 "alpha = -ts_delta(close,5); alpha" 就不会。

- **4. **Illegal group index value, cannot exceed number of elements****

- Group operator没有加densify
   - 为确保平台的高性能，在模拟过程中对组索引的值进行检查。索引值不应超过所有索引组所属的元素数量。如果引发错误消息，那么可能是组的索引在某个操作符中使用的不是密集的（非密集索引看起来像[0, 5, 8, 26, 107]）。在这种情况下，使用"densify(group)"会有所帮助。

- **5. **Illegal group index value, cannot be negative**非法的组索引值，不能为负**

- 非法的grouping值
   - 我们不允许组索引的值为负，要解决这个问题，试试使用densify操作符。且自定义分组的时候不能有负值

- **6. **Got invalid value for attribute "lookback", must be constant or string****

- "lookback" 得到无效值，必须为常量或字符串
   - 当你试图在操作符的 "lookback" 字段中使用非常量或字符串，或者当你错误地排列参数时，会引发此错误。
   - 例如："ts_rank(sales/assets, days_from_last_change(sales))" 会引发错误

- **7. **Grouping data used outside of group operator**在group operator外部使用grouping数据**

- 分组数据只能在组操作符中使用。如果你试图在其他地方使用组数据，就会引发此错误。
   - 例如："ts_delta(industry, 5)" 会引发错误

- **8. **Cumulative lookback of expression exceeds available history**表达式的累积回看超过了可用的历史**

- lookback区间非法
   - 由于数据历史的限制，如果你试图回看超过我们可以提供的范围，就会引发此错误。注意，考虑的累积回看是表达式中使用的最高回看。
   - 例如：ts_rank(ts_mean(close,20),20) 会有40的累积回看。

- **9. **You have reached the limit of concurrent simulations. Please wait for previous simulations to finish****

- 一个用户只能同时simulate10个；你已经达到了并行回测的限制。请等待之前的回测完成
   - 你一次只能模拟有限数量的alpha，所以如果你试图模拟超过这个数量，就会引发此错误。你必须等待你之前的一个模拟完成才能继续。

- **10. **Invalid number of inputs: X, should be exactly Y input(s)****

- 有参数未输入
    - 当你提供的输入数量多于或少于所需数量时，会引发此错误。
    - 例如：无论是 "group_mean(sales/assets, market)" 还是 "group_mean(sales/assets, 1, market, 1)" 都会引发此错误。正确的表达式应该是："group_mean(sales/assets, 1, market)"

- **11. **超时登出：Http Error****

- 所有用户每4个小时or提交过多错误simulation会被强制登出。需要书写代码捕捉错误并随时重登，同时需要保证任务的断点续传。

- ***12.* “回测应该回测了3000多个实例，但由于某种原因，丢失了1700个实例。已经设置了一个sleep函数，以防止访问次数过多，并一直在监视status_code以查找错误。但依然出现此问题，如何解决？”**

- simulation_response.status_code为201并不代表你的Alpha运行没有问题，运行有问题的Alpha就是会被丢失的。您可以运行一下下列代码，体会一下错误的来源：

```
simulation_data = {    'type': 'REGULAR',    'settings': {        'instrumentType': 'EQUITY',        'region': 'USA',        'universe': 'TOP3000',        'delay': 1,        'decay': 15,        'neutralization': 'SUBINDUSTRY',        'truncation': 0.08,        'pasteurization': 'ON',        'unitHandling': 'VERIFY',        'nanHandling': 'OFF',        'language': 'FASTEXPR',        'visualization': False,    },    'regular': 'high-close+dfd'}simulation_response = s.post('[链接已屏蔽] json=simulation_data)print(simulation_response.status_code)print(s.get(simulation_response.headers['Location']).json())print(f'status: {s.get(simulation_response.headers["Location"]).json()["status"]}')
```

- ***13.***  **“不确定SLOW+FAST参数的代码”/“不确定Neutralize选项country/region参数的代码”**

*- "* SLOW_AND_FAST"

*- "* COUNTRY"

- ***14.***  **”当使用模板进行模拟时，结果不好，有些时间点显示出平坦的曲线，表明该模型在那些时间没有股票选择能力。“**

- 请手动找到这个Alpha进行查看。在网页浏览器入“ [[链接已屏蔽]) 即可以看到它的表现。一般这种Alpha的出现是因为使用Alpha前的数据处理工作还不够好。

- ***15.***  **"目前我的代码在运行1000次成功回测的时间大概是2个小时到2个半小时之间，这是一个正常的速度吗？"**

-速度是正常的。看到您也获得了一个新可提交的Alpha,从效率上看，大约1000次simulation获得一个Alpha也是正常的效率，这个说明您的模板选择和数据选择都比较合适。另外一个检测自己速度是否合适的方法就是，回到网页界面，尝试手动simulate一下Alpha,如果会报错“too many simulation at a time”，这就说明代码正在全力工作，占用完了十个线程，算是高效了。

- **16. Correlation获取超时**

-用户只能在60分钟内发送150 correlation requests。不要对每个simulated的Alpha都request

- 17. 如何在JupyterNotebook实现多线程和随时插队？

下面这个代码可能可以提供一些思路：

在JupyterNote Book 的第一个cell

```
import timeimport threadingimport requestsclass RequestThread(threading.Thread):    def __init__(self, urls):        threading.Thread.__init__(self)        self.urls = urls    def send_request(self, url):        print(f'Sending request to {url}')        response = requests.get(url)        # handle your response here        time.sleep(5)    def run(self):        i = 0        while i < len(self.urls):            self.send_request(self.urls[i])            i += 1           urls = ['[链接已屏蔽] '[链接已屏蔽] '[链接已屏蔽] = RequestThread(urls)request_thread.start()
```

接着可以随时跑其他cell

```
urls.append('[链接已屏蔽])
```

或者，可以把所有待simulate的Alpha全部先放到一个csv文件，然后用另外一个notebook去读这个csv文件，不断发出Alpha到服务器中。简而言之，将csv文件作为不同notebook的交互点（中转站）

---

### 帖子 #2: Brain API技巧：如何挖掘API代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] Brain API技巧如何挖掘API代码优化_20309362198679.md
- **讨论数**: 9

Brain平台其实开发的非常规矩，很多功能页面都是通过api实现的。API文档只是其中一部分接口。很多同学在尝试使用API文档的时候，会遇到很多问题，例如不知道api的参数如何设定，返回值长什么样子等。希望下面这些信息能够帮助大家。

## 工具介绍

介绍2个好用的工具：

- 浏览器的开发者工具：developer tools：挖掘api，直接看到api链接和返回值
- Postman：测试api，python代码生成

### 浏览器的开发者工具developer tools

这个可以在Chrome，Edge，Firefox的菜单中找到。网上可是搜到详细使用方法。结合Brain平台，它可以帮助我们知道Brain平台使用了哪些API，可以获得什么返回值。

简单概括：打开浏览器 > 开发者工具 > Network(网络)，然后，进行Brain平台的操作（登录，查Data，进入不同菜单，simulation，修改settings，查看自己的alpha，对自己的alpha进行filter等）。这些操作，都会触发不同的api行为，这些api操作都会被记录下来。

下图，domain在api.worldquantbrain.com的就都是可能对我们有用的api


> [!NOTE] [图片 OCR 识别内容]
> Welcome
> Elements
> Console
> 毖 Sources
> NstNoi
> Pelommance
> Memon
> Application
> Presere log
> Disable cache
> No throttling
> Filter
> Inel
> Hide cata URLS
> Hde extenslon URLs
> Doc
> FctchxHR
> CSS
> Font
> Img
> Mcdla
> Manitcst
> Wasm
> Othor
> Blocked response cookies
> Blocked requests
> 3rd-pary requests
> Big recuest rOWS
> GroUp by frame
> Oyeriew
> Screenshots
> Name
> Status
> Domaln
> Type
> authenticaton
> 200
> api. worldquantbraincom
> fetch
> configuration
> 200
> api.Norldquantbraincom
> fetch
> 200
> api. worldquantbraincom
> fetch
> agreements
> 200
> api.Norldquantbraincom
> fetch
> ader?USer
> 200
> api. worldquantbraincom
> fetch
> messages?order--dateCreatedalimit-5
> 200
> api.worldquantbraincom
> fetch
> simulation
> 200
> api. worldquantbraincom
> fetch
> alphas
> 200
> api.Norldquantbraincom
> fetch
> summary
> 200
> api. worldquantbraincom
> fetch
> 117 requests 393 kB transferred
> 12.8 MB resources Finish: 7.4min DOMContentloaded: 2.35
> Load: 4.91


点击想看的api记录，（在Name列），就可以看到如下的信息。其中，“Headers”里有这个API的URL，Request Method(GET, POST, OPTIONS等)，状态code。“Response” tab是返回值，一般都是json格式。


> [!NOTE] [图片 OCR 识别内容]
> C
> https:Ilplatform worldquantbrain.comldata?delay-lginstrumentType=EQUITY&region=CHN&universe-TOP3000
> 鬯"
> Simulate
> Alphas
> Data
> 舀 Competitions (3)
> Events
> Learn
> Reter
> friend
> Region
> Delay
> Universe
> CHN
> TOP3000
> What data do yoU want to find?
> Search bydatasethame heldname Ordescripton
> SGarch
> Browse All Datasets
> Browse All Fields
> Browse by Category
> Welcome
> 〈少Elements
> Console
> 毖 Sources
> Nstwork
> 4 Perommance
> Memon
> Application
> Preserve log
> Disable Cache
> No throttling
> Filter
> Inver
> Hide data URLS
> Hde extension URLs
> Doc
> FctchxHR
> CSS
> Font
> Img
> Mcda
> Manifest
> WS
> Wasm
> Othor
> Blocked response COokes
> Blocked requests
> 3rd-par requests
> Blg request rOWS
> Grouo by frame
> Include pendlng reouests in HAR tile
> Oyeriew
> Screenshots
> Name
> Headers
> Preview
> Response
> Initiator
> Timing
> Cookies
> data:apolicationfo.
> General
> Collzc
> Request URL:
> https.ilapi worldquantbrain comdata-categores
> { data-Categories
> HeqUESt NEtnOC:
> ehyelOPe
> Status Code:
> 200OK
> enyelope
> Remote Address:
> 10.33.130.232.8080
> envelope
> Referrer Policy:
> strict-origin-when-cross-orign
> { authentic
> T?
> Response Headers
> CCESS-ContolAloW-Credentials


对于POST的请求，是需要有Payload的，例如跑alpha的时候，这个时候，也是可以在开发者工具中查看到的，这个过程，你可以查看到整个数据交互的过程，可以了解到从技术流程（跑一个alpha，会生成一个id，跑完后，会生成一个alpha id）。

下面就是simulate alpha的API的信息


> [!NOTE] [图片 OCR 识别内容]
> Headers
> Payload
> Preview
> Response
> Initiator
> Timing
> Cookles
> Genera
> Request URL
> httpsilapi Worldquantbrain comslmulations
> Request Method:
> POST
> Status Code:
> 201 Created
> Remote Adcress
> 10.33.130.232:8080
> Referrer Policy:
> strict-origin-when-Cross-origin
> Response Headers
> ACCeSS-Control-AlloW-Credentials:
> tuE
> AccesS-Control-Allow-Origin:
> https Iplatform worldquantbrain com
> ACCeSS-Contol-Epose-Headers
> Locatlon Retn-Afel
> AIow:
> POST OPTIONS
> Content-Language:
> Content-Length:
> Content-Type:
> texthtml; charset-UTF-8
> Date
> ThU, 04 Jan 2024 05:58:57 GMT


Payload中，是alpha公式和settings信息


> [!NOTE] [图片 OCR 识别内容]
> Headers
> Payload
> Preview
> Response
> Initiator
> Tming
> Cookles
> Request Payload
> View parsed
> TyDE
> REGULAR"
> 5ettings'
> {"nanHandling
> OFF"
> instrumenTyDe'
> EQUITY"
> delajy":1
> Universe"
> 
> TTuncation
> uniHandling
> VERIFYI
> pasteurization
> ON"
> region'
> U54
> a55et
> Tir
> Value but
> Corparatively
> 1TIe !
> EBIT are
> likely
> Comoanies
> that have invesTeJ
> TOI
> Towth
> TIe |
> the past years
> and
> hayve More
> TUI
> Tor
> 9rowth
> the fuzureInnIMPLENENITATION:
> Ween
> domestic and foreign
> EBIT
> Set
> LONe|
> lpha signa
> for
> Comoanies
> WiTh
> lOwET 355eT fair
> Value
> InIHINT
> TO IMPROVE THE ALPHA:
> Can
> Zhe
> lpha
> WOrK Well 讦
> Comparing
> aong
> Companies
> that
> lower
> Cashflows. Iny/nnalpha
> 9rOUp
> rank(fnd2_
> ebitdm;
> industryl
> 9roup
> rank(Tnd2_
> ebitfr
> industry) ; Iningroup_rank ( fn_assets_
> val_ay
> indusTryI
> 0.5
> alpha
> alpha"}
> hioh
> Tair_


“Allow”中显示的是这个API URL支持的请求method。例如上上图支持OPTIONS（虽然当前请求是POST）。既然支持OPTIONS，那你就可以在Postman工具中，尝试一下，看看会有什么返回值，是否有用。

通过developer tools可以监控的很多api urls，可以让你不单单局限在官方的Brain API文档中。

### Postman

这个工具可以让我们不断尝试API，找到我们想要的返回结果。更重要的是，Postman可以给我们展示python代码（支持很多编程语言），特别适合我们编写不同API的函数 - copy代码，简单修改一下，就是我们需要的特定函数。

**注：**  *Postman限制需要注册（免费），登录，才能够开启Collection（理解为，将很多Brain API放到一起）。有很多类似工具，但是只有Postman有代码生成功能（代码生成，特别适合编程不熟的同学。如果很熟悉编程，可以选择任意类似工具，例如Insomnia）*

#### 针对Brain API的使用

使用Postman发送Brain API请求，是需要获得authorization的。所以

1. 首先 **POST**   [[链接已屏蔽]按照下面这个设置就可以。用户名，密码就是Brain平台的email和密码。]([链接已屏蔽])

注意：生成的token有效期是4小时。所以，4个小时后（目前状态，不确定未来Brain是否会改），就需要重新获得token。在编写自己的代码的时候，你需要考虑一下过期之前，重新刷新token，或者如果运行API返回结果是token过期的消息，重新刷一下token。


> [!NOTE] [图片 OCR 识别内容]
> My Workspace
> New
> Import
> Overview
> POST authe
> GET
> Exam
> GET reference
> OPT alpha
> GET ALL Data
> GET TES
> POST simulati
> No Environment
> 000
> WQ-TEST
> authentication
> SaVe
> Collections
> POST
> https:/lapi.worldquantbrain.comlauthentication
> Send
> APIs
> WQ-TEST
> Params
> Authorization
> Headers (10)
> Body
> Pre-request Script
> Tests
> Settings
> Cookies
> 〈
> POST authentication
> Environments
> POST simulation
> Type
> Basic Auth
> Heads up! These parameters hold sensitive data. To keep this data secure While working in a collaborative
> POST simulation multiple
> environment; we recommend using variables. Learn more about yariables
> Mock servers
> The authorization header will be
> GET my Info
> automatically generated when you send
> GET get Example
> the request. Learn more about Basic Auth
> Username
> 用户名
> History
> authorization
> Password
> 密码
> 0十
> Body
> Cookies (1)
> Headers (13)
> Test Results
> Status: 201 Created
> Time: 940 ms
> Size: 839B
> Save as example
> 000
> Pretty
> Raw
> Preview
> Visualize
> JSON
> 2
> USeI"
> 2
> 3
> Iid
> 4
> 5
> token
> 2
> 6
> expiry
> 14400.0
> 7
> 8
> permissions
> [
> CONSULTANT
> 10
> MULTI_SIMULATION
> 11
> "PROD ALPHAS"
> 12
> REFERRAL
> get


2. 在第一步之后，未来的4小时之内，我们就可以不断尝试各种API了。注意一下，其他各种API的Authorization选择继承。例如。


> [!NOTE] [图片 OCR 识别内容]
> WQ-TEST
> TEST
> SaVe
> GET
> https:/lapi.worldquantbrain.comlsuggestlexamples?limit= 500
> Send
> Params
> Authorization
> Headers (9)
> Body
> Pre-request Script
> Tests
> Settings
> Cookies
> Type
> Inherit aut
> The authorization head
> Inherit auth from parent
> automatically generater
> the request. Learn morr
> No Auth
> aythorizatign
> Basic Auth
> This request is using Basic Auth from collection WQ-TESI:
> Bearer Token
> JWT Bearer


#### Postman代码功能

右侧，又一个 </> 图标，点开，选择Python-Requests，就可以看到基于requests 的python 代码。


> [!NOTE] [图片 OCR 识别内容]
> HP
> WQ-TEST
> TEST
> SaVe
> Code snippet
> GET
> https:/lapi.worldquantbrain.com/suggestlexamples?limit= 500
> Send
> Python
> Requests
> 1
> import
> requests
> Params
> Auth
> Headers (9)
> Body
> Pre-req.
> Tests
> Settings
> Cookies
> 2
> UII
> "https: //api.worldquantbrain. com /
> Query Params
> suggest/examples?Limit=500'
> Value
> Description
> Bulk Edit
> payload
> {3
> headers
> {
> limit
> 500
> Authorization
> Basic  0g=
> Key
> Value
> Description
> '
> 10
> 11
> response
> requests . request (
> GET"
> UII
> headerszheaders
> data=payload )
> 12
> 13 print (response
> text )
> 14
> Body
> 200 OK
> 276 ms
> 2.76 KB
> Save as example
> 000
> Pretty
> Raw
> Preview
> Visualize
> JSON
> 2
> Count
> 10_
> 3
> Inext"
> null
> previous
> null
> 5
> results
> [
> 6
> 7
> "settings":
> {
> 8
> "instrumentType
> EQUITY'
> Key


详细的Postman使用，大家可以网上搜搜。

## 一些额外的API

#### 查看自己的messages：GET

[[链接已屏蔽])

#### 查看fastexpression：GET

[[链接已屏蔽])

#### 符合某一个settings的所有datafields：GET

网页端有10000条上限，通过下面API格式，没有上限。如果是几万条数据，大概几百k大小的，需耐心多等几秒）
 [[链接已屏蔽])

[[链接已屏蔽])

网页开发者工具看到的链接是这样的（有10000条上限）
 [[链接已屏蔽])

#### 符合某一个settings的所有datasets：GET

[[链接已屏蔽])

#### 查看某一个dataset的所有datafields：GET

例子dataset.id=fundamental6。dataset ID是可以通过看浏览器的url和查看dataset API的返回值得到。
 [[链接已屏蔽])

#### 个人所有的alpha：GET

[[链接已屏蔽])

可以添加更多条件进行filter。例如` [[链接已屏蔽]) 
具体filter条件，可以去Alphas菜单，自行设置Filter条件，然后通过developer tool查看

#### Simulations：OPTIONS

[[链接已屏蔽]) 
返回值中有所有settings中的值。如果Brain系统加入新的region或者universe等，这里都会实时体现。可以用来批量生产settings组合。

#### 获得alpha examples：GET

返回的是10个examples。Brain也只给出了10个，不超过50个，limit=50是没太大用处的。
 [[链接已屏蔽])

---

### 帖子 #3: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #4: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #5: Save credentials into session
- **主帖链接**: https://support.worldquantbrain.com[L2] Python的安装学习和API文档的下载代码优化_19024058049431.md
- **讨论数**: 15

1. **完成VScode+python+jupyter环境搭建**
   我们需要完成VScode+python+jupyter环境的搭建，核心目的是让计算机能够成功运行jupyter notebook。可以参考这个视频教程（ **请注意播放音量** ）： [vscode+python+jupyter环境搭建_哔哩哔哩_bilibili]([链接已屏蔽]) 。完成后，请用jupyter notebook运行以下代码并截图：
   ```
   print("my user id is: xxxxx")
   ```

2. **安装必要的python package**

参考上述视频，我们将使用“pip install XXXX”方法安装以下插件：

pandas
              requests
              seaborn
              matplotlib
              tqdm
              plotly

请截图显示插件安装成功的提示。

3.  **用户成功使用API连接到BRAIN**

我们需要成功地使用API连接到BRAIN。可以参考这个网页： [API Web:BRAIN API | WorldQuant BRAIN]([链接已屏蔽]) 。请运行以下代码以连接BRAIN后台：

```
def sign_in():
    import requests
    username = "yourBRAINemail@aaaaa.com"
    password = "yourBRAINpassword"

    # Create a session to persistently store the headers
    s = requests.Session()

    # Save credentials into session
    s.auth = (username, password)

    while True:
        try:
            # Send a POST request to the /authentication API
            response = s.post('[链接已屏蔽])
            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
            break
        except:
            print("connection down, trying to login again")
            sleep(10)

    print(response)
    return s
sign_in()
```

只有当返回值为下列显示时，才算跑通

```
 <Response 201>
```

通过上述任务，你已经完成了Python环境的搭建和接通了BRAIN后台，接下来可以开启自动化Alpha开发之旅了！🎇

---

### 帖子 #6: [MCP]找灵感功能上手详解经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]找灵感功能上手详解经验分享_37113649831831.md
- **讨论数**: 20

最近mcp又出新功能了，马上尝试了一下。如下图选好你想要研究的地区和数据集就可以开始了，配置好key点击生成模板就能一键生成好用的模板
 
> [!NOTE] [图片 OCR 识别内容]
> NSA
> 细问比轱
> IOTTIII
> TOHIIILI
> 顾+5
> Alpha Inspiration Master (找灵感)
> model138
> ACcountlng-based
> MoCel
> LLM Settings
> Results
> 生成 Alpha 模板
> Factors
> 8a52 URL
> Sensitivity to the
> hps Ilapi moonshotcn1
> model140
> Model
> 正在生成模板这可能需要几分钟。
> Inflation Change
> Model
> Name
> Stock Selection DL
> model144
> Model
> kimi-kz-turbo-preview
> model
> APIKey
> model16
> Fundamental Scores
> Model
> 测试连接
> Return prediction
> model1 62
> Model
> from conference call
> ML/AI-Estimates for
> Simulation Settings
> model163
> Analysts' Factor
> Model
> Region
> Model
> USA
> Time-series
> model165
> prediction ofalpha
> Model
> Universe
> models
> TOP3000
> Research Analyst
> model17
> Model
> Delay
> Estimate Factors
> Fundamental &
> modelzo
> Model
> Technical Rank Model
> 开始新任务
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable
> No classes, objects
> pointers
> OTfunctions
> 使用说明
> allowed
 生成之后我们直接下载到本地
 
> [!NOTE] [图片 OCR 识别内容]
> Resuits
> 生成 Alpha 模板
> 下载椟板到本地 d
> 以下给出 6 组可直接在平台"填空"的 a-Template。
> 每个模板均保留"插槽"一一用 <>括起
> -方便日后系统扫描。替换或贝叶斯调参。
> 所有模板已用现有 operator 拼装。可直接粘贴到研究环境缩译。
> 模板1:
> ML 模型残差动量 (分析师来源)
> 经济逻辑:  剥离行业共性后。取模型打分短期娈化。赌"模型新信息"尚末被价格充分反映。
> alpha
> [S_ZSCOre(
> group_neutralizel
> deltal
> backfill(<mdl165_analyst_layerl_or_layerz>;
> 63)
> industry
> 20
 
然后就可以结合mcp去使用了我的用法是直接让ai帮我去找合适的字段去填充模板 
> [!NOTE] [图片 OCR 识别内容]
> TCUC
> TU
> @1md 根据椟板内容的描述去获取合适的数据字段。你觉得合适的字段就放进
> ModellGs 数据字段列表
> 适用于模板AIpha生成
> 来;多一点没关系
> Thought for 2s
> [
> Analyst (分析师)  类特征
> 基于 IBES 数据]
> Read 1md
> Thought for Zs
> Layer 1 特征 (快速信号):
> mdl165_dlgibesnuggetschiwumodell_OIv
> 根据模板内容。需要获取以下几类数据字段:
> mdl165_dlgibesnuggetschiwumodelI_OzV
> modell65 ML/AI特征
> analystlquantlfundamental 三类;
> layer-I/layer-
> mdl165_dlgibesnuggetschiwumodell_IIv
> mdl165_dlgibesnuggetschiwumodelI_ZIV
> 2。基本面宇段
> leverage; market_cap; ROE 等
> mdl165_dlgibesnuggetschiwumodell_3Iv
> 3。成交量宇段
> dollar_Volume; advz0 等
> mdl165_dlgibesnuggetschiwumodell
> 4IV
> 让我先认证BRAIN平台。然后搜索这些字段:
> mdl165_dlgibesnuggetschiwumodelz_SIV
> mdl165_dlgibesnuggetschiwumodell
> GIV
> MCP Tool: worldquant-brain-platfomm
> authenticate
> mdl165_dlgibesnuggetschiwumodell
> 71V
> Thought for Zs
> mdl165_dlgibesnuggetschiwumodell
> BIV
> mdl165_dlgibesnuggetschiwumodell_gIv
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_zV
> mdl165_
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> dlgibesnuggetschiwumodell
> mdl165_dlgibesnuggetschiwumodell
> MCP Tool: worldquant-brain-platform
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz
> OIV
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodelz_12v
> Thought for 35
> mdl165_dlgibesnuggetschiwumodelz
> mdl165_dlgibesnuggetschiwumodelz_ZIV
> 让我继续搜索更多模板需要的字段:
> mdl165_dlgibesnuggetschiwumodel2_32V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> ## Layer
> 特征 (愎速信号):
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell_O3v
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 13V
> Thought for 35
> mdl165_dlgibesnuggetschiwumodell_I4v
> mdl165_dlgibesnuggetschiwumodell_Z3V
> 让我再搜索fundamental类的model165字段:
> mdl165_dlgibesnuggetschiwumodell_33V
> MCP Tool: wordquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 43V
> MCP Tool: worldquant-brain-platfomm
> get_datafields
> mdl165_dlgibesnuggetschiwumodell
> 44V
> 07]C
> 4105 CITOT +suT7 !
> ThOINht fom
 
然后根据选出来的字段往wqb里面的模板里面去选，选好之后就像下面这样
 
> [!NOTE] [图片 OCR 识别内容]
> 示例
> 双重中性化:以Analyst15为例
> 组间比较_GLB_topdiv
> 组间比较_9lb_topdiv_anl15
> 顾问分析示例
> Expression Editor
> Decode 
> Templates
> Expression Editor 
> Clear
> Configure Template: <modelA_layerl/>
> Detected Templates
> Operator
> 〈modelA_layerIl> (20)
> ZSCore(ts
> delta
> grOUP_
> ZsCOre
> 〈modeln
> Enter
> COIIa
> -separated list Of operators forthe modelA_layerl
> DalaField
> Other
> template:
> mdl165_dlgibesnuggetschiwumodelz_OlV
> 〈dayIl〉 
> mdl16s_dlgibesnuggetschiwumodelz_
> 121
> mdl165_dlgibesnuggetschiwumodelz
> DalaField
> Other
> mdl165_dlgibesnuggetschiwumodel2
> 2IV
> mdl165_dlgibesnuggetschiwumodelz_32 
> 〈day2/〉 
> Choose Operators Trom BRAIN
> DataField
> OtheT
> 11
> Grammar Rules
> 12
> CanCel
> Apply
> 13
> Block comments for multiple lines
> 14
> 15
> Statement separator (not needed for
> last line)
> 17
> Last statement is the Alpha expression for
> 18
> BRAIN simulator 
> Alpha expression cannot be assigned to
> Template configured as operator with 20 variables
> Variable 
> No classes; objects; pointers
> functions
> 使用说明
> allowed
 
然后一键开始回测就好啦

---

### 帖子 #7: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！
- **主帖链接**: https://support.worldquantbrain.com[L2] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **讨论数**: 73

一句话总结该活动：直接在评论区评论，分享你的模板。

> ```
> 被审核通过者将获得BRAIN纪念品一份（下图背包）优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至8.31日23：59（以服务器时间为准） 
> [!NOTE] [图片 OCR 识别内容]
> WorldQuant
> aRNIN
> BRAIN Backpack


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

### 帖子 #8: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md
- **讨论数**: 23

1. 模板内容及效果

基本模板：

```
ts_covariance(<datafield1>,<datafield2>,<days>)
```

其中datafield1/datafield2均选自Sentiment21 dataset。

这个idea的出现其实是因为我用了Genius rank插件发现自己没用过ts_covariance。在论坛里直接搜索了ts_covariance试图省事想直接找个模板套用，跳出来的是Weijie老师之前发过的一系列" **推荐使用的数据 USA D1 TOP3000 NEWS12__partXXX（未检查数据类型）** "的帖子。News数据集和Sentiment数据集有一定相似性，所以为了降低Corr我就又找了个还没什么人用的Sentiment21数据集跑了跑，效果还是可以的。

这个基础模板只算是个一阶模板，大家外面可以自行再套signed_power/hump/trade_when等等进行进一步优化。除此之外我为了优化六维没有进一步再加operator优化效果了。下图是我在EUR/TOP2500提交的其中两个Alpha示例


> [!NOTE] [图片 OCR 识别内容]
> 431I
> 4OOJK
> SO
> UIT
> LCJK
> MOCK
> 15水
> LI[IK
> IS Summary
> eTodl
> 昵 Single Dara Set Alpha
> ReglrAph
> Fam !theme; EURIDIISENTIMENT .1 +
> APTCUaUC Dald
> TCTNNo
> TC
> 11.0296
> 1.01
> 5.1395
> 3.5896
> 9.319o



> [!NOTE] [图片 OCR 识别内容]
> 4SUOK
> 403ok
> 35OOK
> ZSUOK
> 203oK
> 1.SUK
> 1,03Ok
> I5 Summary
> Penod
> @SIngle Oata Set Mlpha
> B Power Pool Apha
> eBVlaTAInha
> Pram !theme; EURIOIISENTIUENT . 4
> AUITCIaLC
> 1,76
> 10,549
> 1,10
> 4,919
> 2,459
> 9,24900
> J UUI


虽然模板简单，跑出来效果还是不错的，交出来的alpha还能当RA，说明新数据集跑的人应该不多。

2.模板内容分析

```
ts_covariance(y, x, d) 
```

协方差(covariance)是衡量两个变量如何一起变动的统计量。如果两个变量倾向于同时高于或低于它们的平均值，则协方差为正。如果一个变量倾向于高于其平均值而另一个变量倾向于低于其平均值，则协方差为负。 
> [!NOTE] [图片 OCR 识别内容]
> 其数学公式如下:
> Cov(r, X)t
> C
> (yi - Ya)(i - X)
> 4
> it-4+1
> 其中:
> yi 和 ?i 分别是时间序列Y和X 在时间点  i 的值。
> Ya 是时间序列Y在过去
> 个周期 (从
> t-0+1
> 到 t
> 的平均值。
> Xd 是时间序列 X在过去
> 个周期 (从
> t-4+1
> 到
> 的平均值。
> 是计算协方差的时间窗口或回顾期 (lookback period)
> 简单来说。计算步骤如下:
> 确定时间窗口:  获取 y 和
> 在最近
> 天的数据。
> 计算各自的平均值:  分别计算这
> 天内
> 的平均值
> 和
> 的平均值 (Xd)。
> 计算每曰偏差:  对于这
> 天中的每一天。计算当天的
> 值与 Ya 的差值。以及当天
> 值与
> Ld 的差值。
> 计算偏差乘积之和:  将每天计算出的两个差值相乘。然后将这
> 天的乘积全部加起来。
> 求平均:  将上一步得到的总和除以
> 得到最终的协方差值。


比如说我们的alpha是

```
-ts_covariance(负面情绪，正面情绪，d)
```

那么，当d天内负面情绪得分明显降低，正面情绪得分明显升高时，这个表达式的值就会明显增大提示做多；反之则提示做空。

3.个人对该模板的想法

其实一开始我在脑补跑这个模板的结果的时候，还以为这个模板跑出来alpha的会是turnover非常高的alpha(捕捉短期情绪的剧烈波动从而做多/做空)。但最后根据结果来看，单就这个模板而言days较短时跑出的alpha结果都比较一般。我最后交的几个alpha 的days 都是设定在63/252/504等等中长期时间。

我简单查了一篇文献来寻找原因(还没仔细读)

**Investor Sentiment in Asset Pricing Models: A Review of Empirical Evidence**

文献中提到

> The prevalence of the reversal effect of the sentiment, which means that the impact of sentiment on returns usually was reversed  **with the same magnitude after 4 or 5 days** .

所以我猜，我设想的那种短期的这种剧烈情绪波动可以用来设计一些均值回归的alpha来获利？

4.总结

可以看到这个模板最初的idea其实只是来源于论坛的老帖子，只是换了个新dataset就跑出了不错的结果，这对大家来说都是一个比较简单易行的方法，可以多多尝试。

同时，我这个模板其实只是一个非常原始的想法，肯定还有很大的提升空间，也欢迎大家一起发表意见！

---

### 帖子 #9: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md
- **讨论数**: 26

最近大趋势下，想必大家都在使用 72变之类的功能，而72变中，作者提供了一套模板，出货率还不错，不过在此基础上，我通过论坛，让大模型又总结了一份Alpha模板，如标题所言，这份模板均来自社区，所以是来自社区的馈赠

我自己用下来，出货率还不错，和内置模板相当，甚至还能更好一点，不过大家还是要自行评估一下，部分来自社区的论坛也存在过拟合的风险，如有帮助，欢迎点赞，如有错漏，请帮忙指出

```
    ## 模板格式说明

    每个模板使用以下占位符格式：
    - `<ts_op/>` - 时间序列操作符，如 `ts_rank`, `ts_mean`, `ts_delta`, `ts_ir`, `ts_stddev`, `ts_zscore`
    - `<group_op/>` - 分组操作符，如 `group_rank`, `group_neutralize`, `group_zscore`
    - `<vec_op/>` - 向量操作符，如 `vec_avg`, `vec_sum`, `vec_max`, `vec_min`, `vec_stddev`
    - `<field/>` - 数据字段占位符
    - `<d/>` - 时间窗口参数，常用值: `{5, 22, 66, 126, 252, 504}`
    - `<group/>` - 分组字段，如 `industry`, `sector`, `subindustry`, `market`

---

### 帖子 #10: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Lucky】为七十二变加上WQB回测配置--进行批量回测经验分享_36864734537879.md
- **讨论数**: 6

72 变是一个十分好用的工具，但是生成的 json 是没有回测配置的

> e.g.

> 
> [!NOTE] [图片 OCR 识别内容]
> 人9OOJIV
>  ]
> ATa_geVe4teU0133101131301
> "group_neutralize (rank(ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry)"'
> "group_neutralize( rank (ts_backfill (workforce_pillar_composite_score,
> 30) ) ,
> industry )
> "group_neutralize (rank(ts_backfill(anl8l_confidence_level_percent , 30)), industry)
> "group_neutralize ( rank (ts_std_dev (mdl177_liqcoeff,
> 21)
> /
> ts_mean (mdl177_liqcoeff
> 126) ),
> industry)",
> "group_neutralize ( rank
> ts_backfill(sustainability_sector_percentile,
> 30) ) ,
> industry)


为了提升回测效率，设计了一个脚本，将七十二变生成的 json转换成成 WQB 能直接回测的带回测配置的json

> e.g.
> 
> [!NOTE] [图片 OCR 识别内容]
> "type"
> 
> IREGULAR"
> settings":
> {
> "instrumentType":
> IEQUITYI
> 11
> "region":
> IND"
> Iuniverse":
> ITOP5OO"
> "delay":
> 1,
> "decay":
> 5 
> Ineutralization":
> IFASTI
> Itruncation": 0.08,
> 'pasteurization":
> ION"'
> ItestPeriod":
> IIPOYOMII
> "unitHandling":
> IVERIFYI
> "nanHandling
> IOFFI
> 11
> "language"
> 
> FASTEXPR"
> IVisualization":
> false
> }
> regular":
> "group_neutralize ( rank (ts_backfill(backfill_mid_term_momentum_score,
> 30) ) ,
> industry )
> Ivariant":
> "FASTI


设置好回测配置 & 文件输入输出的路径之后，即可生成可直接在 WQB 回测的 JSON。即可批量回测七十二变输出的变体了。

以下是实现代码

```
import jsondef convert_expressions(input_file, output_file, custom_settings):try:withopen(input_file, 'r') asf:expressions=json.load(f)output_data= []forexprinexpressions:alpha_object= {"type": "REGULAR","settings": custom_settings,"regular": expr}output_data.append(alpha_object)withopen(output_file, 'w') asf:json.dump(output_data, f, indent=2)print(f"Successfully converted {len(expressions)} expressions.")print(f"Output saved to '{output_file}'")exceptFileNotFoundError:print(f"Error: Input file not found at '{input_file}'")exceptjson.JSONDecodeError:print(f"Error: Could not decode JSON from '{input_file}'")exceptExceptionase:print(f"An unexpected error occurred: {e}")if __name__ == "__main__":# --- 请在这里自定义参数 ---# --- 以下为示例参数 ---default_settings= {"instrumentType": "EQUITY","region": "IND","universe": "TOP500","delay": 1,"decay": 5,"neutralization": "FAST","truncation": 0.08,"pasteurization": "ON","testPeriod": "P0Y0M","unitHandling": "VERIFY","nanHandling": "OFF","language": "FASTEXPR","visualization": False}INPUT_JSON_PATH='七十二变/输出/文件.json'OUTPUT_JSON_PATH='加上回测配置/文件/的输出路径.json'convert_expressions(INPUT_JSON_PATH, OUTPUT_JSON_PATH, default_settings)
```

---

### 帖子 #11: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [[链接已屏蔽])
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

### 帖子 #12: 【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md
- **讨论数**: 84

今天听说mcp里的APP发布了更新，有了新功能


> [!NOTE] [图片 OCR 识别内容]
> Open Submtter
> Open Simulator_M
> 七十娈


当然，为了更好使用新功能，你需要一个APIkey:  [[链接已屏蔽])

试用之后，我马上获得很多很好的模板！我直接开交！感觉我甚至不用做模板了，这是不是一种错觉？


> [!NOTE] [图片 OCR 识别内容]
> ts_rank(cIiability_gap_field/>,
> 252)"
> Broup_Zscore(ts_mean(ts_delay (cresidual_returns/>
> 21) ,
> 252),
> Sector)


唉，开始感觉自己以前交的Alpha类别有点太单一了，都是一个模板做出来的，现在好了，有了这种工具，反而我用了几次就发现，AI都被我太单一的idea限制住了，出新模板的能力都没那么好了。

还是赶紧多做不一样的吧！再次感谢作者，这个社区分我先”不要脸“地拿了，如果作者要claim这个著作权，请随时留言，我会撤回这个帖子。再次感谢！

**跟大家补充请教：生成的表达式太多咋办？以后限流遭不住。**

**补充点赞:  [【check王】验证表达式是否正确的脚本——七十二变黄金搭档]([链接已屏蔽])**

**虽然我自己用首页的import来检查就够，但这个朋友写得不错**

---

### 帖子 #13: 【新人指南】到底要交什么样的Alpha？置顶的
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人指南】到底要交什么样的Alpha置顶的_32226888249239.md
- **讨论数**: 29

## **到底要交什么样的Alpha？——新人指南**

在Alpha开发与提交的过程中，许多新人常常会问：“到底什么样的Alpha才值得提交？”这是一个复杂的问题，因为Alpha的质量并没有一个单一的“金标准”可以作为绝对的判断依据。新人常见的错误是过度依赖某一两个单一指标，比如  **Sharpe** 、 **Fitness**  或  **Margin** ，认为只要这些指标表现良好，Alpha就一定值得提交。

然而，判断一个Alpha是否值得提交更像是诊断病情——不能仅仅依靠一个指标或单一的维度来做出决定。单一指标可能会提供片面的信息，而忽略了Alpha整体表现的复杂性和多样性。这种过度依赖单一指标的思维方式，往往会导致新人在Alpha提交过程中出现偏差。

### **数量与质量的平衡：螺旋上升的原则**

在Alpha的开发与提交过程中， **数量** 和 **质量** 是两个不可分割的重要维度。许多新人在实践中常常犯两个极端的错误：要么过度关注质量而忽视数量，要么完全不管质量，只追求数量。这两种错误都会对Alpha的整体表现产生负面影响。

#### **数量不足的问题**

如果过度追求质量而导致提交的Alpha数量不足，可能会出现以下问题：

1. **Portfolio不稳定** ：
   Alpha的数量不足会导致整体Portfolio的表现缺乏多样性，从而增加OS（Out-of-Sample）结果的不稳定性。
2. **缺乏真实水平的验证** ：
   单个Alpha的表现可能具有偶然性，只有通过足够的数量才能更接近整体的真实水平，避免因个别Alpha的异常表现而影响整体判断。

#### **质量不足的问题**

另一方面，如果完全忽视质量，只追求数量，也会带来风险：

1. **Portfolio表现受损** ：
   大量低质量的Alpha会拉低整体Portfolio的表现，导致Margin、Sharpe等关键指标下降。
2. **资源浪费** ：
   提交大量低质量Alpha不仅浪费了开发时间，也可能对平台的审核资源造成压力。

#### **螺旋上升的原则**

数量和质量并非对立，而是一个螺旋上升的过程。新人在初期阶段可以优先解决数量的问题，通过提交足够数量的Alpha来建立基础，然后逐步提高质量要求，最终实现数量与质量的平衡。

- **新人建议** ：
  每个月提交的Alpha数量不要少于  **40个** 。这一数量可以帮助新人更接近整体的真实水平，同时避免因单月表现异常而影响长期结果。
  - **数量的意义** ：足够的数量可以为Portfolio提供多样性，降低单个Alpha表现异常对整体的影响。
  - **质量的提升** ：在数量达到一定基础后，可以逐步提高Alpha的质量要求，例如优化Turnover、Margin等关键指标。

### **平台的“最低标准”与其意义**

在Alpha提交过程中，平台设定了一些“最低标准”，这是每位新人必须满足的基本要求。这些标准的存在并非是为了限制，而是为了确保Alpha在实际应用中具有一定的可行性和质量。然而，许多新人在实践中往往只关注如何通过这些指标，而忽略了这些要求背后的逻辑和意义。

#### **Turnover的要求**

**Turnover**  是一个重要的指标，它衡量了Alpha的换手率。平台要求Turnover不能高于  **70%** ，这是为了避免交易频率过高导致交易成本过高，从而影响  **Margin**  的表现。换手率过高会显著增加手续费，最终削弱Alpha的盈利能力。

- **进阶建议** ：
  - 当你的水平到达一定程度，建议将Turnover控制在  **30%**  以下。
  - 当你已经不再断粮，建议将这一指标进一步降低至  **15%**  以下。
- **特殊情况** ：
  - 如果Turnover较高，但  **Margin**  同时表现非常优秀（例如Margin超过  **10** ），这种情况下高换手率是可以接受的。

#### **Turnover的下限**

平台同时要求Turnover不能低于  **1%** ，这一点常常让新人感到困惑。事实上，这一要求的意义在于避免Alpha的持仓过于稳定。换手率过低会导致Position长期不变，而这与对冲基金的核心理念相悖。对冲基金的本质是通过动态调整持仓来捕捉市场机会，而过低的换手率可能意味着Alpha缺乏足够的市场反应能力。

### **Sub Universe与Robust Test的重要性**

在Alpha的评估过程中， **Sub Universe**  是一个关键的测试维度。平台要求Alpha在较小的股票范围（Sub Universe）中仍然保持一定的表现，这一要求的最低标准是  **50%**  的Sharpe。这意味着，如果Alpha在当前的Universe（例如Top3000股票）中表现良好，那么在更小的Universe（例如Top1000股票）中，它的Sharpe也必须达到至少50%的水平。

#### **Sub Universe的原理**

这一要求的核心逻辑是为了避免Alpha的信号仅来源于流动性较低的小市值股票。如果一个Alpha在Top3000股票中表现良好，但在Top1000股票中完全失效，这通常表明其收益主要依赖于流动性较低的那2000只股票。这种情况可能会导致Alpha在实际应用中面临较大的风险，例如流动性不足或交易成本过高。

#### **Robust Test的概念**

**Robust Test**  是一个更广泛的概念，旨在通过调整各种参数来测试Alpha的稳定性和敏感性。具体来说，Robust Test可以包括以下两种方式：

1. **调整Settings中的指标** ：
   - 例如修改交易成本、滑点、或其他市场环境参数，观察Alpha的表现是否稳定。
2. **调整Expression中的参数** ：
   - 修改Alpha表达式中的关键参数，测试结果的敏感性。
   - 如果结果收敛性较好，说明Alpha具有较强的鲁棒性；如果结果发散性较强，则表明Alpha可能过于依赖某些特定条件。

#### **实践建议**

- **前期阶段** ：
  在Alpha开发的初期，可以暂时不需要过多关注Robust Test，重点放在满足平台的最低要求（如Sub Universe的表现）。
- **后期阶段** ：
  随着经验的积累，可以逐步加强Robust Test的强度，通过调整参数和环境来验证Alpha的稳定性。

### **IS测试与长期稳定性：Alpha的“望诊”**

在Alpha的评估过程中， **IS Ladder Testing** （针对Regular Alpha）和 **2-Year Testing** （针对Atom Alpha）是平台用于检测Alpha稳定性的重要工具。这些测试的核心目标是通过观察Alpha的PNL表现，评估其长期稳定性。这一过程类似于“望诊”，通过观察PNL的形状来判断Alpha的健康状况。

#### **PNL的理想形状**

最理想的PNL表现是一条从左下角到右上角的稳定直线。这种形状表明Alpha在长期内具有持续的盈利能力和较低的波动性，是稳定性和可靠性的最佳体现。

- **新人阶段的目标** ：
  对于新人来说，能够通过平台的IS Ladder Testing或2-Year Testing已经是一个不错的开始。这表明Alpha在基本稳定性方面达到了平台的最低要求。

#### **进阶要求**

在进阶阶段，可以通过以下标准来进一步评估Alpha的长期稳定性：

1. **过去10年的表现** ：
   - 在过去10年中，Alpha的Sharpe超过  **1**  的年份不少于  **X年** （具体标准可根据个人目标设定）。
2. **最近两年的表现** ：
   - 特别关注最近两年的PNL表现，尤其是  **2022年**  的表现。

### **为什么要有PPAC？低相关性与Portfolio的多样性**

在Alpha开发与提交的过程中，平台引入了  **PPAC**  的机制，这不仅是为了给新人提供一个更宽松的探索环境，更重要的是为了强调  **低相关性**  和  **Portfolio的多样性**  对整体表现的重要性。

#### **Portfolio的概念：你的军队**

为了更直观地理解Portfolio的意义，可以将它比喻为一支军队。以往的Alpha评估标准过度追求  **Sharpe**  和  **Fitness**  等单一指标，这就像你的军队里清一色都是身高体壮的步兵。虽然这些步兵看起来很强壮，但缺乏多样性会让你的军队在面对复杂战场时显得单薄。

要让你的军队更有战斗力，就需要补充更多的兵种，例如：

- **斥候** ：负责侦查，提供灵活性。
- **炮兵** ：提供远程打击能力。
- **后勤兵** ：确保资源供应，维持军队的稳定性。

同样的道理，Alpha的Portfolio也需要多样性。一个多样化的Portfolio可以更好地应对不同的市场环境（OS），从而提升整体的稳定性和表现。

Self Correlation是一个很直观指标，新人的时候0.7是平台的要求。PPAC的要求是Pool内0.5的要求。值得一提的是这里的SC会随着提交数量的变多而更难有低的表现

- 0.5-0.7 之间的sc是可以通过的标准
- 0.3-0.5 之间的sc已经是很不错的了，通常对portfolio有一些提升
- 0.3以下的sc通常是很低的了

### **经济学意义与OS表现：从Alpha描述开始**

在Alpha开发与提交过程中， **经济学意义**  是决定OS（Out-of-Sample）表现的关键因素之一。许多老师常常强调这一点，因为具有经济学意义的Alpha往往能够更好地适应不同的市场环境，展现出更强的稳定性和可靠性。

#### **写Description的重要性**

对于新人来说，写好Alpha的  **Description** （描述）是一个非常重要的环节。这不仅是对Alpha逻辑的总结，也是开发者学习和思考的过程。可以将Description视为自己的学习日记，通过记录Alpha的核心逻辑和设计思路，帮助自己更好地理解经济学意义。

### **总结**

Alpha的开发与提交是一项复杂的任务，既需要满足平台的最低要求，也需要从长期稳定性、Portfolio优化和经济学意义的角度进行深入思考。新人在实践中应避免过度依赖单一指标，重视数量与质量的平衡，关注整体Portfolio的表现，并通过写Description来梳理自己的思路和逻辑。希望这篇指南能够帮助新人更好地理解Alpha开发的核心原则，并逐步提升自己的能力。

---

### 帖子 #14: 【新人科普】BRAIN 平台上的四类Alpha（RA, ATOM, PPAC, SA）
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普】BRAIN 平台上的四类AlphaRA ATOM PPAC SA_32032672214807.md
- **讨论数**: 74

在 WorldQuant BRAIN 平台上，根据表达式复杂度、字段来源以及检测机制的不同，BRAIN 平台将 Alpha 分为四类： **Regular Alpha（RA）** 、 **ATOM Alpha** 、 **PPAC Alpha**  和  **Super Alpha（SA）** 。本文将为新人系统性介绍这四类 Alpha 的核心特征、检测规则及策略建议。

## 1. Regular Alpha（RA）——最基础也最严谨的 Alpha 类型

对于 Regular Consultant（非 IQC）来说， **Regular Alpha（RA）**  是最早接触、也是最常使用的一类 Alpha。

### ✅ 特点：

- 表达式内的操作符和数据字段数量只要不超过  **64 个** ，就可以提交；
- 几乎 **没有其他限制** ，是最自由的表达方式；
- 需要通过  **所有的 Alpha 检测标准** 。

### 🧪 关键检测机制：

1. **IS Ladder Testing** ：查看 Alpha 在过去 10 年是否每年都有稳定 Sharpe，防止因子过拟合于局部时期。
2. **Sub-Universe Testing** ：验证 Alpha 在不同Universe子集下的表现一致性。
3. **Weight Concentration Testing** ：防止 Alpha 只在极少数股票上集中信号，影响实盘效果。
4. **Product Correlation Testing** ：检测 Alpha 是否和已有产品的表现高度重合，避免“重复造轮子”。

## 2. ATOM Alpha —— 来自单一数据集的“纯净信号”

**ATOM Alpha**  是自 2024 年开始引入的新类型，最初用于特定 Alpha 比赛, 后推广持续沿用。更多信息请见：

[[链接已屏蔽])

### ✅ 判定标准：

- **所有使用的数据字段必须来自同一个数据集** ；
- 常见的  `group`  字段如  `industry` 、 `country`  等是豁免字段，不计入数据集数量限制；
- 提交后页面上会出现“ **Single Dataset Alpha** ”标签。

### 🧪 特别检测机制：

- **放松了 IS Ladder Testing 要求** ；
- **仅要求通过最近两年的 2-Year Sharpe 检测** 。

> 💡 设计逻辑：同一数据集下的数据字段类型更统一， **降低混信号风险** ，更利于 OS 稳定性提升，从而提升 VF（Value Factor）得分。

## ⚡ 3. PPAC Alpha ——轻量但高效的入门路径

**PPAC（PowerPoolAlpha）Alpha**  是更简单直接的信号，比RA少了“修饰的”sub expression。源自于2025年的PPAC比赛，寻求pool内alpha的低自相关。

### ✅ 提交条件（非常宽松）：

- **最多使用 3 个数据字段** ；
- **最多使用 8 个操作符** （包含加减乘除等基础运算符）；
- 同样，常见的  `group`  字段如  `industry` 、 `country`  不计入字段/操作符数量。
- 25年11月更新，PPA alpha 需要是风险中性化中的一种（RAM, STATISTICAL, CROWDING, FAST, SLOW,SLOW_AND_FAST） 才可以提交
- 数量限制

1. 新顾问前三个月对于PPA没有限制
2. 三个月后，如果一个Alpha 符合 PPA + ATOM 或 PPA + REGULAR 或  PPA + ATOM + REGULAR 无限制
3. 三个月后，如果一个alpha 仅有PPA，则一天只能提交1个，且一个月在一个region只能由10个quota

提交后会显示标签：“ **PowerPoolAlpha** ”。

### 🧪 简化检测机制：

- 只要求  **Sharpe > 1** ；
- 通过  **Sub-Universe 检测** ；
- 所在地区的 PPAC Pool（不含非PPAC）需满足：
  - 自相关性低于 50%，或
  - 表现领先于 10% 以上。

> ⚠️ 尽管检测标准大幅降低，但这对提交者的 **自我克制能力** 提出了更高要求。
> 提交数量上升后，要特别注意  **分散性与质量平衡** ，建议早期尽量使用不同模板和数据源， **避免高自相关性** 。

## 🚀 4. Super Alpha（SA）——属于进阶顾问的 Alpha 策略组合

**Super Alpha（SA）**  是平台为有一定alpha积累的顾问推出的进阶功能。更多内容请见：

[[链接已屏蔽])

### ✅ 启用条件：

- 顾问提交的 Alpha 总数达到  **100 个** ；
- 可以从自己已提交的 Alpha 中组合构建；
- 高级顾问（Genius 等级）还可选择  **其他人的 Alpha**  作为基础组件。

### 💰 权益优势：

- 每天可单独提交  **1 个 Super Alpha** ；
- 不计入每日 4 个常规 Alpha 限额；
- 可获得每日额外  **$1~$60**  的收益（与表现挂钩）；

> Super Alpha 是  **Alpha 组合优化领域，对自己本身的regular alpha如果很好，SA也会很好** 。建议VF高了以后提交，会有更高的收益加成，更容易拿到60USD

## 🎓 新手建议：优先提交 PPAC + ATOM Alpha

对于刚加入 BRAIN 的新顾问，推荐策略如下：

- 多做  **PPAC Alpha** ：结构简单，利于练习表达式思维；
- **符合 ATOM 条件的 PPAC Alpha**  优先提交（双标签）；
- 前期应 **着重积累高质量且分散的信号** ，为后期组合打下基础；
- 有经济学意义的模版永远是重要的，不要混信号！

希望这篇文章能帮助你在 BRAIN Alpha 的旅程中更快起步，逐步掌握从表达到组合的核心技能。🎯

也希望可以点赞评论!

---

### 帖子 #15: 【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的_35928620962839.md
- **讨论数**: 30

今天我们来聊聊顾问的名片指标也是GENIUS最重要的指标： **Combined Alpha Performance** 。无论你是刚入门的新人，还是已经提交了几百个 alpha 的“老手”，这个话题都值得你花点时间认真琢磨。因为理解它，不仅能帮你提升 alpha 的表现，还能让你少走很多弯路。

## **什么是 Combined Alpha Performance？**

先说说这个“Combined Alpha Performance”到底是什么。简单来说，它是一个用来衡量所有提交过的 alpha 和 super alpha 的整体表现的指标。它的计算方式很直接：把所有地区已经提交的 alpha 和 super alpha  **等权组合** ，然后看它们在 2023-2025 年（semi-OS）的表现，具体是 **费后表现。**

这就像是一个大锅饭——你提交的每一个 alpha 都是这锅饭里的一粒米，表现好的米会让这锅饭更香，而表现差的米则可能毁掉整锅饭的味道。所以， **Combined Alpha Performance**  不仅仅是一个数字，它实际上反映了你提交的 alpha 是否在整体上“靠谱”。

## **计算原理：从公式看本质**

Combined Alpha Performance 的计算公式其实很简单：
 **等权组合 + 手续费调整 + 2023-2025 年的费后表现** 。

换句话说，平台会把你提交的所有 alpha 和 super alpha 按等权组合起来，然后在 2023-2025 年的市场环境下模拟它们的表现，最后扣除手续费，得出一个费后的 Sharpe 值。

从这个公式里，我们可以提炼出三个提升表现的关键词：

```
分散、质量、手续费。
```

接下来，我们就从这三个关键词出发，聊聊如何一步步提升你的 Combined Alpha Performance。

## **关键词一：分散（Diversity)**

### **为什么分散很重要？**

分散的核心在于降低风险。就像投资一样，如果你把所有的钱都投在一个篮子里（比如一个地区、一个模板），一旦这个篮子表现不好，你的整体表现就会被拖累。而分散可以让你的 alpha 表现更加稳定，减少单一因素的影响。

### **如何做到分散？**

1. **地区分散** ：
   最容易做到的分散就是  **region 的分散** 。不同地区的市场环境、手续费、波动性都不一样，把 alpha 分散到多个地区，可以有效降低单一区域表现不佳的风险。
2. **降低同一地区的 SC（Self Correlation）** ：
   在同一个 region 下，尽量降低 alpha 之间的相关性（SC）。最直接的方法就是多用不同类型的模板和数据类别（category）。也就是多点塔（Pyramid）这里要注意一点：我们说的“点塔”是指  **主信号**  的多样性，而不是通过科技（技术优化）或者附带信号来实现的点塔。换句话说，真正的分散是从信号本身出发，而不是靠“修修补补”来实现。

### **总结**

分散是提升 Combined Alpha Performance 的第一步，也是最容易做到的一步。记住： **多地区、多模板、多数据类别** ，多中性化，尤其是风险中性化，让你的 alpha 表现更加稳健。

## **关键词二：质量**

### **质量比数量更重要**

不管是 Combined Alpha Performance 还是 VF(Value Factor），在不能兼顾的情况下， **质量永远比数量重要得多** 。一个质量差的 alpha 不仅不会给你的组合加分，反而会拖累整体表现。而且，质量差的 alpha 需要很多个高质量的 alpha 来弥补。

### **举个例子：一个负的 OS Sharpe 如何拖累组合表现？**

#### **假设场景**

我们有一个组合，资金规模为  **100 万美元** ，包含以下几个 alpha：

- **Alpha A** ：OS Sharpe = -1
- **Alpha B** ：OS Sharpe = +1
- **Alpha C** ：OS Sharpe = +1

这些 alpha 是等权分配资金的，也就是说每个 alpha 分配的资金为：
 **100 万 ÷ 3 = 33.33 万美元** 。

#### **计算组合表现**

1. **Alpha A 的影响** ：
   - Alpha A 的 OS Sharpe = -1，相当于这 33.33 万美元的资金在拖累组合表现。
2. **Alpha B 和 Alpha C 的贡献** ：
   - Alpha B 和 Alpha C 的 OS Sharpe = +1，它们的表现为组合提供了正收益。
3. **组合表现** ：
   - 由于等权组合的 Sharpe 是所有 alpha 的加权平均值，Alpha A 的负表现会显著拉低整体表现。
   - 结果是：即使有两个 OS Sharpe = +1 的 alpha，组合的 Sharpe 也只有  **0.33** ，远低于 +1。一个负的alpha 让原本+1的组合表现降低了-66%

#### **需要多少好的 alpha 来弥补？**

如果我们想让组合的 Sharpe ≥ +1，那么至少需要  **2 个 OS Sharpe = +1 的 alpha 来弥补 1 个 OS Sharpe = -1 的 alpha** 。
如果有 2 个 OS Sharpe = -1 的 alpha，则需要至少  **4 个 OS Sharpe = +1 的 alpha**  来弥补。

### **如何提升质量？**

1. **关注 alpha 的核心逻辑** ：
   一个 alpha 的质量，核心在于它的逻辑是否有意义。不要为了提交而提交，确保你的 alpha 有清晰的经济学或统计学依据。论坛内有很多其它顾问的内容，就不在此赘述
2. 巧用AI和MCP来帮助我们验证一个alpha是否有意义。在MCP样例中就有如何写出alpha description （验证是否合理）和 alpha performance improvement会让你受益匪浅

[使用MCP成功地将alpha优化成可提交状态的案例 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 使用MCP成功地将alpha优化成可提交状态的案例经验分享_35587548741015.md)

### **总结**

质量是 Combined Alpha Performance 的基石。在不能兼顾的情况下，不要盲目追求数量，专注于打磨高质量的 alpha。

## **关键词三：手续费**

### **手续费的影响**

我们在提交 alpha 时看到的 Sharpe，都是  **不计手续费**  的。但在 Combined Alpha Performance 和真实的市场交易中，手续费是必须考虑的。

如果一个 alpha 的 margin（利润空间）过低，那么在扣除手续费后，原本的正 Sharpe 可能会变成负的，或者大幅降低。

### **如何控制手续费？**

1. **关注 ASI** ：
   不同市场的手续费标准不同。通常来说：
   - **亚洲市场（ASI）** ：尽量保持在 15 以上，20以上为佳。
   - **其他地区** ：建议保持在 10 以上。
2. **优化交易频率** ：
   如果一个 alpha 的交易频率过高，手续费会显著增加。通过调整 decay 或者优化信号，可以有效降低交易频率，从而减少手续费。论坛内有其它帖子自行搜索
3. **避免低 margin 的 alpha** ：
   提交前，检查 alpha 的 margin。如果 margin 太低，即使 Sharpe 看起来不错，也可能在扣除手续费后变得毫无价值。

## **关于 Super Alpha（SA）：双刃剑的误区与正确使用**

### **误区：IS Sharpe 高的 SA 一定能提升表现**

很多人会觉得， **SA 的 IS Sharpe 高** ，所以它一定能在 OS 中表现得很好。但事实是， **IS 的表现和 OS 的表现没有直接关系** 。一个 IS Sharpe 高达 10 的 SA，在 OS 中可能会是负的表现。

### **风险：质量差的 RA 会让 SA 成为“双倍伤害”**

SA 是通过组合多个原始 alpha（RA）生成的。如果这些 RA 的质量本身就很差，那么 SA 的表现也不会好。正所谓  **“Garbage In, Garbage Out”** ，如果你用的是“垃圾”原材料，SA 只会把这些问题放大。

### **如何正确使用 SA？**

- **过滤掉 IQC 表现差的 RA** ：如果IQC的OS表现不好，组SA时候学会剔除 product_correlation > 0 的 RA，确保组合的分散性。
- **确保 RA 的质量** ：优先选择 OS 表现稳定且为正的 RA。
- **优化组合逻辑** ：降低相关性，分散风险，提升 SA 的稳定性。

## **结语：提升 Combined Alpha Performance 的核心思路**

总结一下，提升 Combined Alpha Performance 的核心在于三个关键词： **分散、质量、手续费** 。

- **分散** ：多地区、多模板、多数据类别，多风险中性化，降低风险。
- **质量** ：专注于高质量的 alpha，避免被低质量的 alpha 拖累。
- **手续费** ：优化交易频率，确保 ASI 达标，避免低 margin 的 alpha。

最后送给大家一句话： **“少即是多，精益求精。”**  希望这篇文章能对你有所启发，祝大家的 Combined Alpha Performance 节节高升！

---

### 帖子 #16: 根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的_35129651186967.md
- **讨论数**: 30

## 引言：为什么我们要关心 PC？

 **降低 PC 是提升收益和保证账号健康的最重要因素之一** 。

1. PC的高低直接影响个人短期（base payment)和长期收入 (quarterly payment),
2. PC的高低间接影响Value Factor，从而再次影响收入
3. 高PC alpha 无法入库，无法参与比赛，长期提交大量高pc alpha，可能会导致账户封禁

## 一、理解Product Correlation

### 什么是 Product Correlation（PC）？

PC 衡量一个 alpha 与平台中其他 顾问提交的alpha 的相关性，其计算公式和自相关类似，为最近四年PNL 每日变化（diff）的皮尔逊相关性系数。

### PC高低与收入的关系

顾问提交的alpha被平台接收后，会进行多次筛选以决定是否对平台有用，其中最重要的筛选就是PC。当PC大于0.7，则被认为是相同/及其相近的alpha，则该alpha不会被平台采用，因此也不会有机会获得任何weight。在顾问协议中披露的每日base payment 计算公式中也明确提到与base payment与PC的负相关性。通常来说，当pc< 0.5 会被认为是比较独特的因子，从而会获得更高的base payment，也更有机会被基金经理采纳而获得weight，进而获得更高的quarterly payment。

而更低的PC也意味着更低的SC，组合的correlation 越低，也会进一步提升组合的整体多样性表现，从而获得更好的value factor。从个人经验看，在点塔的时候偶尔提交了更高的pc alpha，相应的该月份的vf就会受到影响。不知道平台在计算vf的时候是否对高pc有额外的惩罚系数。

### 举例说明PC高低与收入的实证

Alpha 1： PC 0.49的SA，获得了58.97的 base payment


> [!NOTE] [图片 OCR 识别内容]
> anonymoUs
> Super
> ACTIVE
> 08/30/2025 EDT
> JPN
> TOP1600
> 0.31
> 0.49



> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 08/30/2025
> Super:
> 58.97
> Regular:
> 7.94
> Total:
> 66.91
> 40
> 20
> 28.
> 29.
> 30.
> 31 _
> 1.Sep
> 2.Sep
> Aug
> Aug
> Aug
> Aug


Alpha 2：SAC 期间的一个表现更好的alpha，PC 0.68，只获得了9.69 USD的收入。而7月14日一个0.73的pc 只获得了5.4USD的收入。对不起当时0.9+的VF


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/19/2025
> Super:
> 9.69
> Regular:
> 8.10
> 15
> Total:
> 17.79
> 10
> 14.Jul
> 15.Jul
> 16.Jul
> 17.JUl
> 18.Jul
> 19.Jul
> 20.Jul


# **二、如何检查PC并降低PC的实操**

**获取PC的代码：论坛有很多，部分同学反馈没有权限，已更新在评论区**

[[链接已屏蔽])

**几个注意事项：**

1. 不建议直接只用check submission的接口，会更慢，因为要检查其他的测试比如自相关，而自相关等检测都可以在本地完成，效率更高
2. 该接口也会限流，甚至影响提交alpha，建议做一些在本地的限流，这样不触发平台限流，从而获得整体的结果最优（代码如下，可以自己调整睡眠时间）
3. 极少数情况会pc通过但是提交失败，这是因为pc是用的缓存数据，在pc检查和提交之间如果别人交了类似的会在提交时候出现pc不过的情况，但这种情况极少极少。

```
s = login()start_time = datetime.now()pass_pc_ids = []last_request_time = datetime.now()max_sleep_time = 60 * 60 # 最大睡眠时间1小时current_sleep_time = 60 # 初始睡眠时间60秒定义重连时间间隔reconnect_interval = timedelta(hours=3.5)for id in batch_ids:# 检查是否需要重新登录current_time = datetime.now()if current_time - start_time >= reconnect_interval:s = login()start_time = current_time# 记录请求开始时间request_start_time = datetime.now()# 调用 get_prod_corrpc = get_prod_corr(s, id)# 记录请求结束时间request_end_time = datetime.now()request_duration = (request_end_time - request_start_time).total_seconds()# 检查相关性if pc > 0.7:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['PROD Correlation'])elif pc >0.5:set_alpha_properties(s,id,name_value,selection_desc=name_value,combo_desc=name_value,tags = ['ace_tag'])else:result = get_simulation_result_json(s,id)selection = result['selection']['code']tag_value = ['PC 0.5','Ready to Submit']name_value = result['name']if "own" in selection:color = 'GREEN'count = count+1else:color = 'None'combo = result['combo']['code']while len(selection)<100:selection = selection + selectionwhile len(combo)<100:combo = combo + combo set_alpha_properties(s,id,name_value,selection_desc=selection,combo_desc=combo,tags=tag_value,color=color)pass_pc_ids.append(id)print(id,pc)# 计算上次请求到本次请求的时间间隔time_since_last_request = (request_start_time - last_request_time).total_seconds()# 如果请求时间明显增加，调整睡眠时间if request_duration > current_sleep_time * 1.5:current_sleep_time = min(max_sleep_time, current_sleep_time * 2)else:current_sleep_time = 60 # 如果请求时间正常，恢复默认睡眠时间# 更新上次请求时间last_request_time = request_start_time# 等待当前睡眠时间time.sleep(current_sleep_time)print(len(pass_pc_ids))
```

## 三、如何降低 PC？

Global 论坛有一篇外区的帖子，有些内容是很有可取之处的

- [Reduce Production Correlations. – WorldQuant BRAIN](../顾问 CC40930 (Rank 95)/[Commented] Reduce Production Correlations_29301199149463.md)

### 避免使用过于常见的 signal

- 如单纯的暴力一二三阶，没有任何自己的迭代

### 增加创新表达方式

- 多尝试非线性组合、二阶交叉项、相对排名等。使用sigmoid，sign power，ts linear window等做一些数学变换
- 尝试使用target tvr的几个operator来降低tvr的同时也会变化pnl从而降低pc （但有时会反而提高，因为别人也使用了该方法提交过）

### 尝试多种region，unvierse和netralization 方式

- 一些高pc的因子，在变换了中性化，unvierse和regioin后会有意想不到的收获，而这个可以代码工程化完成

### 多尝试新的数据集

- 当有新的数据集，新的unvnierse和新的region的时候是pc最低的时候，如TOPDIV3000，最近新上的数据集等

### 使用独特的分组方式

- 最常见的是group datafield （如other455），bucket分组

### 当然王牌还是有自己的模版和自制数据

### 如何快速总结已经提交alpha的PC：

在alphas菜单中点击submitted，选中select column 勾选product correlation，已经提交alpha的PC一目了然


> [!NOTE] [图片 OCR 识别内容]
> 鬯2
> Simulate
> Alphas
> Leamn
> Data
> Labs
> Genius
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> 《
> Refer a friend
> Select Columns
> Summany
> Properties
> Settings
> Perommance
> Alphas
> Nams
> SzazUs
> Resion
> Instrument TypE
> Sharpe
> Rezurns
> Competi-ion
> Catesory
> Universe
> Delay
> Pnl
> Turnoer
> Page size
> Typ=
> Color
> Decay
> Neutralization
> Drawdown
> Marsin
> Fllter
> LansuaEs
> TaE
> Truncation
> Unit Handlins
> Fitnsss
> Book Sizs
> Date Submit-ed (EST]
> Hidgzn
> NaN Handlins
> Pasteurization
> ~oun
> Shor Count
> Select Columns
> Turnover
> Tag
> Favorite
> Sharo 50
> Sharpe 125
> S-ar Date (EST
> Sharpe 250
> Sharpe 500
> 22
> See
> OSIIS Razio
> Pre Close Sharpe
> 4.974
> Pre-Close Razio
> Self-Correlation
> Prod-Correlation
> Reset
> Apply
> Lns


最后祝大家新的赛季VF和Genius双高！如果对你有用还请点赞评论！

---

### 帖子 #17: assuming final_example_alpha_list is your listfunction to divide the list into chunksdef divide_chunks(alpha_list_with_settings, n):    looping till length l    for i in range(0, len(alpha_list_with_settings), n):        yield alpha_list_with_settings[i:i + n]divide the list into chunks of size 10n = 10chunks = list(divide_chunks(final_example_alpha_list, n))print each chunkfor i, chunk in enumerate(chunks):    print(f"Chunk {i+1}:")    print(chunk)    print("\n")
- **主帖链接**: https://support.worldquantbrain.com[L2] 【新顾问必读】BRAIN API可以实现的功能代码优化_19831456877463.md
- **讨论数**: 15

**【重要】使用API请关闭VPN！使用API请关闭VPN！使用API请关闭VPN！**

目前API已经基本可以实现平台上所有的靠鼠标点击的功能了吧，这些是我的总结。有些功能可能没有总结到，欢迎大家配合这篇文章一起使用👉 [Brain API技巧：如何挖掘API]([L2] Brain API技巧如何挖掘API代码优化_20309362198679.md)


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Consultant program
> Events
> Refer a friend
> SignIn
> Sign In
> Email
> Email field empty
> Password
> Forgot password
> Sigm
> Don't have an account? Sign Up here
> Having trouble signing in? Contact support


**STEP 1:Authentication 登录账号** 

- 描述: Authenticates the user using the /authentication endpoint 使用/authentication端点进行身份验证
- **每个登录Session有效期为4小时，请检查你的代码切勿频繁登录，24小时内登录超过25次将会冻结账户**
- Input: A POST request to the /authentication endpoint with a basic authorization header (username and password) 向/authentication端点发送带有用户名和密码的POST请求
- Output: On success, it returns a JSON Web Token (JWT). If biometrics sign-in is enabled, it returns a 401 status code and a header location。成功后，返回一个JSON Web Token (JWT)。 **如果系统启用了生物识别登录（针对非中国大陆用户），它将返回401状态代码和一个header位置。这个header位置是一个链接（or QR code)，需要扫码完成。**
- Code:

```
import requests
#建议将用户名密码放到另外的文件内存储
# Define the path to the text file that store your username and password, the first line should be your username and second line to be your password.
file_path = "credentials.txt"

# Initialize variables to hold the username and password
username = ""
password = ""

# Open the file and read the lines
with open(file_path, "r") as file:
    username = file.readline().strip()  # Read the first line for the username and strip newline characters
    password = file.readline().strip()  # Read the second line for the password and strip newline characters# Create a session to persistently store the headers s = requests.Session() # Save credentials into session s.auth = (username, password) # Send a POST request to the /authentication API response = s.post('[链接已屏蔽])
```

**一种解决超时登出的解决方案（超过4小时会登录session会过期）**

```
def sign_in(credentials_path):    import requests    from time import sleep    # Initialize variables to hold the username and password    username = ""    password = ""    # Open the credentials file and read the username and password    try:        with open(credentials_path, "r") as file:            username = file.readline().strip()  # Read the first line for the username and strip newline characters            password = file.readline().strip()  # Read the second line for the password and strip newline characters    except FileNotFoundError:        print(f"Error: The file '{credentials_path}' was not found.")        return None    except Exception as e:        print(f"An error occurred while reading the credentials file: {e}")        return None    # Create a session to persistently store the headers    s = requests.Session()    # Save credentials into the session    s.auth = (username, password)    while True:        try:            # Send a POST request to the /authentication API            response = s.post('[链接已屏蔽])            response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx            print("Authentication successful.")            break  # Exit the loop on success        except requests.HTTPError as e:            print(f"HTTP error occurred: {e}. Retrying...")  # Provide more specific error message            sleep(10)        except Exception as e:            print(f"Error during authentication: {e}. Trying to login again.")            sleep(10)    return ssession = sign_in("path/to/your/credentials.txt")
```

```
while True:    s = sign_in("path/to/your/credentials.txt")    try:        #Run Alpha code        print("running")    except:        print('connection down')        s = sign_in()
```

```

```

**STEP 1.1 Get Dataset like Data Explorer**  查找数据集


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> 舀
> Competitions (0)
> 8 Team
> Community
> Consultant program
> Region
> Delay
> Universe
> Data
> Datasets
> USA
> TOP3000
> Search
> Category
> Coverage; %
> Value score
> Alphas
> Users
> Name; description
> AlLcategories
> to
> 100
> to
> to
> t0
> Clear
> Dataset
> Fields
> Coverage
> Value Score
> Users
> Alphas
> Research Papers
> Analyst Estimate Data for Equity
> 350
> 609
> 3727
> 55502
> Report Footnotes
> 318
> 41%
> 3832
> 31093
> Company Fundamental Data for Equity
> 886
> 749
> 23292
> 674330
> [1],[2],[3], [4]
> Fundamental Scores
> 31%
> 151
> 674
> [1]
> Systematic Risk Metrics
> 16
> 779
> 1681
> 5455
> US News Data
> 322
> 80%
> 5373
> 43803
> Ravenpack News Data
> 75
> 689
> 645
> 8842
> [1],[2],[3],[4]
> Volatility Data
> 64
> 699
> 2437
> 30093
> Options Analytics
> 74
> 709
> 2204
> 10859
> [1],[2],[3]
> Price Volume Data for Equity
> 18
> 1009
> 26455
> 828156
> [1],[2],[3],[4],[5],[6],
> [7],[8],[9],[10], [11],
> [12]


- Description: 返回DataFrame文件
- **要注意数据集的Universe、REGION的DELAY的设定，不同的设定的数据集是不同的**
- **可以通过对返回的df内的category、name、description等字段进行筛选，找到所有相关的数据集**
- Input: session, settings (which includes region, delay, universe, instrumentType)
- Output: DataFrame
- Code:

```
#Example setting
settings = {'region': 'ASI', 'delay': '1', 'universe': 'ILLIQUID_MINVOL1M', 'instrumentType': 'EQUITY'}

def get_datasets(session, settings):
    url = "[链接已屏蔽] +\
        f"instrumentType={settings['instrumentType']}®ion={settings['region']}&delay={settings['delay']}&universe={settings['universe']}"
    result = session.get(url)
    datasets_df = pd.DataFrame(result.json()['results'])
    datasets_df['instrumentType'] = settings['instrumentType']
    datasets_df['region'] = settings['region']
    datasets_df['delay'] = settings['delay']
    datasets_df['universe'] = settings['universe']
    return datasets_df
```

**Get Datafield like Data Explorer**  获取所有满足条件的数据字段及其ID

 
> [!NOTE] [图片 OCR 识别内容]
> !C匕骘_
> BRNf
> Simulate
> CAlphas
> Learn
> Data
> 罟
> Competitions (0)
> {8 Team
> Community
> Consultant program
> Region
> Universe
> Data
> Datasets
> Analyst Estimate Data for Equity
> USA
> TOP3000
> Fields
> Description
> Search
> Coverage; %
> Type
> Alphas
> Users
> Name; description
> to
> 100
> All
> to
> to
> Clear 
> Field
> Description
> Type
> Coverage
> Users
> Alphas
> adjysted_Detincome 止
> Adjusted net income
> forecast type (revisionlnewl.)
> Matrix
> 879
> 390
> 1186
> anl4_ads1detailafv1 10_bk
> Broker name (int)
> Vector
> 699
> 30
> anl4_ads1detailafv1 10_estvalue
> Estimation Value
> Vector
> 699
> 17
> 38
> anl4_ads1detailafv1 10_person
> Broker Id
> Vector
> 699
> anl4_ads1detailafv1 10_prevval
> The previous estimation of finanicial item
> Vector
> 699
> 15
> 32
> anl4_ads1detailqfv1 10_bk
> Broker name (int)
> Vector
> 6396
> 19
> anl4_ads1detailqfv1 10_estvalue
> Estimation Value
> Vector
> 639
> 10
> anl4_ads1detailqfv1 10_person
> Broker Id
> Vector
> 639
> 2
> anl4_ads1detailqfv1 10_prewal
> The previous estimation of finanicial item
> Vector
> 639
> 10
> anl4_adxqfv110_down
> Number of lower estimations
> Vector
> 709
> 12
> anl4_adxqfv1 10_high
> The highest estimation
> Vector
> 709
> 11
> https:/ /platform worldquantbrain.com /data/data-setslanalyst4idata-fieldsyanl4_adjusted_netincome_ft
> Delay
> anl4
 

- Description: 根据Dataset id来获取数据字段
- **Dataset ID可以通过前步的df内获取，或者在平台网页上，鼠标放到相应的dataset上，在左下角即可看到data set id和datafield id**
- **要多注意data field的category和operator的匹配，尤其MATRIX和VECTOR的比较**
- Input: s, instrument_type, region, delay, universe, dataset_id, search
- Output: 返回DataFrame
- Code:

```
def get_datafields(
    s,
    instrument_type: str = 'EQUITY',
    region: str = 'USA',
    delay: int = 1,
    universe: str = 'TOP3000',
    dataset_id: str = '',
    search: str = ''
):
    if len(search) == 0:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&dataset.id={dataset_id}&limit=50" +\
            "&offset={x}"
        count = s.get(url_template.format(x=0)).json()['count'] 
    else:
        url_template = "[链接已屏蔽] +\
            f"&instrumentType={instrument_type}" +\
            f"&region={region}&delay={str(delay)}&universe={universe}&limit=50" +\
            f"&search={search}" +\
            "&offset={x}"
        count = 100

    datafields_list = []
    for x in range(0, count, 50):
        datafields = s.get(url_template.format(x=x))
        datafields_list.append(datafields.json()['results'])
    datafields_list_flat = [item for sublist in datafields_list for item in sublist]

    datafields_df = pd.DataFrame(datafields_list_flat)
    return datafields_df
```

 **STEP 2: Simulating an Alpha**  回测Alpha


> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitio
> Simulation 1
> Settings
> USA/D1/TOP3000
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.08
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> Off
> YEARS
> MONTHS
> Save as Default
> Apply
> 20
> 21
> 22
> regular
> expression
> Clone this Alphaina new tab
> Example
> Simulate


- **描述: 用于回测Alphas, 一个完整的alpha（JSON）包括Settings （JSON）和 表达式（regular字段）组成，通过API 将这个alpha POST到服务器，成功的POST将获得一个在服务器的url （‘Location’）并获得回测进度条。**
- Input: A POST request to the /simulations endpoint with a JSON object that includes the settings of the simulation and the expression 向/simulations端点发送包含回测设置和表达式的JSON对象的POST请求
- Output: On success, it returns a URL in the HTTP response header Location. This URL can be used to check the progress of the simulation 成功后，它在HTTP响应头Location中返回一个URL。此URL可用于检查回测的进度；如果没有检查到Location ，则说明你的Alpha发送产生了错误。请检查常见错误👉 [BRAIN API及日常回测时常见的错误 – WorldQuant BRAIN]([L2] BRAIN API及日常回测时常见的报错代码优化_19446834004503.md)
- **在大规模回测中，建议您将回测的Alphas List，回测时间和是否成功回测（lcoation url）存储在一个文件中（csv，json或其他格式），以方便debug和管理**
- Code:

```
simulation_data = {
    'type': 'REGULAR',
    'settings': {
        'instrumentType': 'EQUITY',
        'region': 'USA',
        'universe': 'TOP3000',
        'delay': 1,
        'decay': 15,
        'neutralization': 'SUBINDUSTRY',
        'truncation': 0.08,
        'pasteurization': 'ON',
        'unitHandling': 'VERIFY',
        'nanHandling': 'OFF',
        'language': 'FASTEXPR',
        'visualization': False,
    },
    'regular': 'close'
}
simulation_response = s.post('[链接已屏蔽] json=simulation_data)
```

 **STEP3: Alpha Simulation Status and Results Retrieval**  Alpha回测状态和结果检索


> [!NOTE] [图片 OCR 识别内容]
> CODE
> RESULTS
> LEARN
> DATA
> 159
> Simulations usually take a few minutes Ormore:
> Click here to cancel the simulation.
> TIP
> Submit Alphas with Iow Correlation to your other Alphas。
> Properties
> Simulate to saVe
> Name
> Category
> Currently 'anonymous'
> None
> Color
> Selectladd tags
> None
> Description
> Description
> Tags


- **描述：检查alpha回测的进度并检索结果, 一个成功的回测会获得一个服务器内的URL，在response里的‘Location'字段可以获得该URL，复制到浏览器内也可以访问。**
- **如果alpha 表达式有误或已经存在历史的回测中，将不会得到此URL，则回测失败。同时回测的最大上限为10个，所以在POST的任务中，如果FAIL则可以设置sleep一段时间后重试。**
- Input: A GET request to the URL returned when sending an alpha for simulation 向发送alpha模拟时返回的URL发送GET请求
- Output: If the alpha is still simulating, a Retry-After header is returned. Once the simulation finishes, the response includes a JSON object from which you can retrieve the alpha id 如果alpha仍在模拟中，返回Retry-After头。回测完成后，响应包含一个JSON对象，您可以从中检索alpha id （注意alpha id为7位，如：m8qlQZ1）
- Code:

```
from time import sleep

simulation_progress_url = simulation_response.headers['Location']
finished = False
while True:
    simulation_progress = s.get(simulation_progress_url)
    if simulation_progress.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + simulation_progress.headers["Retry-After"] + " seconds")
    sleep(float(simulation_progress.headers["Retry-After"]))
print("Alpha done simulating, getting alpha details")
alpha_id = simulation_progress.json()["alpha"]
alpha = s.get("[链接已屏蔽] + alpha_id)
print(alpha.json())
```

 **STEP 4: Record Sets of Alpha Simulations**  Alpha PnL绩效历史


> [!NOTE] [图片 OCR 识别内容]
> -SOOK
> Jul '17
> Jan '18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Needs
>  IS
> Period
> TRAIN
> TEST
> IS
> O
> Improvement
> Summary
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.20
> 1.149
> -0.08
> -1.909
> 28.549
> -33.389600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Count
> Short Count
> 2017
> 1.77
> 1.229
> 1.71
> 11.709
> 4.159
> 191.279000
> 1096
> 1936
> 2018
> 0.20
> 1.199
> 0.08
> 1.7896
> 10.019
> 29.789000
> 1093
> 1955
> 2019
> 0.04
> 0.899
> 0.01
> 0.289
> 6.0596
> 6.389600
> 1057
> 1979
> 2020
> -1.23
> 1.229
> -1.43
> -16.989
> 25.269
> -277.490000
> 1014
> 2020
> 2021
> 6.29
> 1.559
> 16.28
> -83.709
> 4.509
> -1,081.04900
> 1048
> 2035
> Long


- Description: Retrieves record sets containing the information about simulations 获取PnL图表的信息
- Input: A GET request to the /alphas/<alpha_id>/recordsets/<record set name> endpoint 向/alphas/<alpha_id>/recordsets/<record set name>端点发送GET请求
- Output: Returns a record set containing the information about your simulations for each trading day 返回日度级别的PnL信息
- Code:

```
from time import sleep

finished = False
while True:
    pnl = s.get("[链接已屏蔽] + alpha_id + "/recordsets/pnl")
    if pnl.headers.get("Retry-After", 0) == 0:
        break
    print("Sleeping for " + pnl.headers["Retry-After"] + " seconds")
    sleep(float(pnl.headers["Retry-After"]))
print("PnL retrieved")
```

 **Alpha Management**  获取特定alpha的表现

- Description: Manages alphas
- Input: A GET request to the /alphas/<alpha id> endpoint 向/alphas/<alpha id>端点发送GET请求
- Output: Returns a JSON object representing the alpha 返回Json文件，包含Alpha的所有信息，以下很多的功能都由此延申。
- ```
  alpha = s.get("[链接已屏蔽] + alpha_id)
  ```

 **STEP 5 Alpha List 批量获取已经完成回测的结果**

**
> [!NOTE] [图片 OCR 识别内容]
> WORLDQUANT
> BRAIN
> Simulate
> CAlphas
> Learn
> Data
> :
> Competitions (0)
> {8 Team
> Community
> Consultant program
> 三
> 0 Alphas
> Unsubmitted
> Submitted
> Alpha Distribution
> Alpha Lists
> Size
> 10
> out of 51
> Filter
> Select Columns
> Name
> Competition
> Type
> Status
> Date Created (EST)
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Search
> Select
> Selec
> Selec
> Search
> Selec
> Select
> e〉 1
> e8〉 1
> e8〉 1
> Select
> anonymous
> Regular
> UNSUBMITTED
> 07/30/2024 EDT
> USA
> TOP3000
> 0.32
> 3.189
> 1.159
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.39
> 7.299
> 1.579
> anonymous
> Regular
> UNSUBMITTED
> 07/10/2024 EDT
> USA
> TOP3000
> 1.34
> 7.0996
> 1.769
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> T0P3000
> 1.53
> 5.229
> 3.479
> anonymous
> Regular
> UNSUBMITTED
> 05/20/2024 EDT
> USA
> TOP3000
> 1.31
> 4.449
> 3.489
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 0.96
> 2.859
> 20.009
> anonymous
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.17
> 3.189
> 17.199
> anonymoUs
> Regular
> UNSUBMITTED
> 05/11/2024 EDT
> USA
> TOP3000
> 1.06
> 3.749
> 15.639
>  | | |
> 0oOI I3
> UNSIBNITTED
> OC /1 1 /00/
> C
> TO03O
> C 1O0
> CC0
> Page
> Tag
**

- ```
  Description: Retrieves records in the IS and OS Alpha list 获取所有在IS和OS列表的Alpha信息。这可以帮助你批量筛选出STEP2-3中，哪些回测是有信号的。建议将回测结果和之前的alpha list进行交叉比较（setting和regular （表达式）相同即为同一个alpha）
  ```
- ```
  未提交的alpha stage value是IS，已提交的stage 字段value是OS
  ```
- ```
  Input: session, total_alphas, limit
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to fetch a specific number of IS alphas (`total_alphas`) using pagination.
def get_n_is_alphas(session, total_alphas, limit=100):
    fetched_alphas = []
    offset = 0

    # Keep fetching alphas until the required number of alphas is reached or no more alphas are available.
    while len(fetched_alphas) < total_alphas:
        response = session.get(
            f"[链接已屏蔽]
        )
        alphas = response.json()["results"]
        fetched_alphas.extend(alphas)
        if len(alphas) < limit:
            break
        offset += limit
    return fetched_alphas[:total_alphas]
```

```

```

```
Check result of Checks 获得Checks的结果
```

- ```
  Description: 向/alphas/<alpha id>/check端点发送GET请求
  ```
- ```
  Input: alpha id
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  is_checks_response = session.get(f"[链接已屏蔽])
  ```

```

```

```
Check Self Correlation 自相关性检查
```

- ```
  Description: Retrieves self-correlation result by alpha_id 根据Alpha_id检查自相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve self correlation for the given alpha ID.
def get_self_corr(session, alpha_id):
    response = session.get(f"[链接已屏蔽])
    if response.status_code == 200 and "records" in response.json():
        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]
        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)
        return self_corr_df
    else:
        return pd.DataFrame(columns=["correlation"])

# Function that retries fetching self correlation for the given alpha ID up to `max_retries` times.
def get_self_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            self_corr_df = get_self_corr(session, alpha_id)
            if not self_corr_df.empty:
                return self_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["correlation"])
```

```

```

```
Check Prod Correlation 全局相关性检查
```

- ```
  Description: Retrieves prod-correlation result by alpha_id 根据Alpha_id检查全局相关性
  ```
- ```
  Input: session, alpha_id, max_retries
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to retrieve prod correlation for the given alpha ID.
def get_prod_corr(session, alpha_id):
    try:
        response = session.get(f"[链接已屏蔽])
        response.raise_for_status()
        try:
            response_data = response.json()
        except json.JSONDecodeError:
            print(f"Error while decoding prod_corr JSON for alpha {alpha_id}: Invalid or empty JSON")
            return pd.DataFrame(columns=["alphas", "max"])

        if "records" in response_data:
            columns = [dct["name"] for dct in response_data["schema"]["properties"]]
            prod_corr_df = pd.DataFrame(response_data["records"], columns=columns)
            return prod_corr_df
    except requests.HTTPError as e:
        print(f"Error while fetching prod_corr for alpha {alpha_id}: {e}")
    return pd.DataFrame(columns=["alphas", "max"])

# Function that retries fetching prod correlation for the given alpha ID up to `max_retries` times.
def get_prod_corr_with_retries(session, alpha_id, max_retries=3):
    retry_count = 0
    while retry_count < max_retries:
        try:
            prod_corr_df = get_prod_corr(session, alpha_id)
            if not prod_corr_df.empty:
                return prod_corr_df
        except json.JSONDecodeError:
            pass
        retry_count += 1
        time.sleep(1)  # Wait for 1 second before the next retry
    return pd.DataFrame(columns=["alphas", "max"])
```

```

```

```
Change Alpha properties 给Alpha更改设置，例如改名字，改颜色等
```

- ```
  Description: Change the Alpha's Property 向/alphas/<alpha id>端点发送patch请求
  ```
- ```
  Input: session, alpha_id, color or new_name
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
# Function to update the color of an alpha with the given color.
def update_alpha_color(session, alpha_id, color):
    update_data = {"color": color}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200

# Function to update the name of an alpha with the given name.
def update_alpha_name(session, alpha_id, new_name):
    update_data = {"name": new_name}
    response = session.patch(f"[链接已屏蔽] json=update_data)
    return response.status_code == 200
```

```

```

```
Get Performance Comparison 获取Performance Comparison的结果
```

- ```
  Description: Returns performance comparison for merged performance check 向/alphas/alpha_id/before-and-after-performance端点发送GET请求
  ```
- ```
  Input: s, alpha_id, team_id (optional), competition (optional)
  ```
- ```
  Output: 返回Json文件
  ```
- ```
  Code:
  ```

```
def performance_comparison(s, alpha_id, team_id:Optional[str] = None, competition:Optional[str] = 'ACE2023'):
    """
    Returns performance comparison for merged performance check
    """
    if competition is not None:
        part_url = f'competitions/{competition}'
    elif team_id is not None:
        part_url = f'teams/{team_id}'
    else:
        part_url = 'users/self'
    while True:
        result = s.get(
            f"[链接已屏蔽] + alpha_id + "/before-and-after-performance"
        )
        if "retry-after" in result.headers:
            time.sleep(float(result.headers["Retry-After"]))
        else:
            break
    if result.json().get("stats", 0) == 0:
        return {}
    if result.status_code != 200:
        return {}

    return result.json()
```

```

```

```
补充：Multi-Simulation对应UI中的
```

```
    multisimulation_data = [        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'close'        },        {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': 'USA',                'universe': 'TOP3000',                'delay': 1,                'decay': 15,                'neutralization': 'SUBINDUSTRY',                'truncation': 0.08,                'pasteurization': 'ON',                'unitHandling': 'VERIFY',                'nanHandling': 'OFF',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': 'open'        },        # Add more simulation data as needed    ]    # Send multisimulation request    multisimulation_response = s.post('[链接已屏蔽] json=multisimulation_data)    # Check response    if multisimulation_response.status_code == 201:        print("Multisimulation request sent successfully.")    else:        print("Error in sending multisimulation request.")
```

```
使用get方法获取multi Alpha的结果，其children的结果即为单个Alpha的Location,再对每个使用get方法，即可获得单个Alpha的id
```

```

```

```

```

```
设置Log来记录操作
```

```
import logging# Create a loggerlogger = logging.getLogger('my_logger')# Set the level of the logger. This can be DEBUG, INFO, WARNING, ERROR, or CRITICALlogger.setLevel(logging.INFO)# Create a file handler that logs even debug messageshandler = logging.FileHandler('my_log.log')handler.setLevel(logging.INFO)# Create a formatter and add it to the handlerformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')handler.setFormatter(formatter)# Add the handler to the loggerlogger.addHandler(handler)# Log some messageslogger.info('This is an info message')logger.warning('This is a warning message')logger.error('This is an error message')logger.critical('This is a critical message')
```

```
获取所有本人可用的operator
```

```
# 获取个人所使用的operatordef get_user_operator(session):    import pandas as pd    result = session.get("[链接已屏蔽])    df = pd.DataFrame(result.json())    return df
```

```

```

---

### 帖子 #18: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 959

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #19: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 742

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #20: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #21: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 930

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #22: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 660

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #23: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第八季.md
- **讨论数**: 599

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季](../顾问 LZ63377 (Rank 33)/[Commented] 【日常生活贴】我的量化日记第七季.md) ）因评论到达上限，已无法评论，特此展开第八季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #24: 【日常生活贴】我的量化日记第六季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 30

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #25: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1018

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #26: 【顾问好文，限时置顶】关于新Consultant提升每日paid的一些建议经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【顾问好文限时置顶】关于新Consultant提升每日paid的一些建议经验分享_27599176068503.md
- **讨论数**: 26

许多新Consultant可能会遇到一个问题：我每天的paid就几美元，别人却有十几、二十几美元甚至更多，这该怎么办呢？

首先，新Consultant的每日paid较低是正常现象，我们需要通过“养号”来提升每日的paid。坚持一段时间，会有较大的改善。

[图片 (图片已丢失)]

在此之前，我们需要知道每日paid由regular alpha和super alpha组成，二者分别进行独立计算，互不影响。Super alpha较为容易获得较高的paid，不过需要regular alpha数量达到100以上才可解锁该功能。因此，我们的主线任务就是提交更多alpha使得满足100个的数量要求，尽快解锁Super alpha功能。

对此，推荐大家前期以ASI为主要研究方向。为什么呢？ASI为大region，可挖掘的alpha数量多，且会相对容易拿到weight，前期积累的这些regular，在解锁Super alpha后可进行组合，制造出较多的Super alpha。而GLB无法用于组合Super alpha；USA已被较深层次挖掘，挖掘出的alpha可能很多过不了相关性测试。在解锁Super alpha后就可用之前提交的ASI进行组合制造Super alpha，这将会增加不少的收入。

回到开头提出的paid差异问题，造成这个差异的主要原因是每个Consultant的value factor的差异会极大程度地影响每日paid。value factor每个月更新一次，更新依据是以统计期内三个月的alpha表现（截止日期为上上个月的月底）。例如当前为11月，本月更新的value factor统计的是789这三个月。新Cousultant的value factor为初始值0.5，提交表现好的alpha将value factor提升至0.7，0.8甚至更高，paid就会翻1倍，2倍，3倍乃至更高。

优先考虑尽量交更多的alpha（alpha质量极差的除外）。其余影响因素的提升可参照： [[链接已屏蔽])

补充一点，当出现theme时，可进行评估，如能找到满足theme的alpha，则以此优先，毕竟这个加成不少且限时，错过了就没有了。

以上就是我关于新Consultant提升每日paid的一些建议，如有什么疑问可在下面评论，有觉得错误之处也可指出。祝大家value factor向1靠拢！

---

### 帖子 #27: 【顾问进阶】一文读懂风险中心化，掌握使用方法
- **主帖链接**: https://support.worldquantbrain.com[L2] 【顾问进阶】一文读懂风险中心化掌握使用方法_35954596858903.md
- **讨论数**: 22

今天早上收到公告通知11月起， **PowerPool将仅接受风险中性化的因子，顾问仍然可以使用其他的非风险中性化（MARKET, SECTOR, INDUSTRY, SUBINDUSTRY, COUNTRY) 回测，但只有符合RA标准的才可以提交** 。很多新顾问可能还不太熟悉风险中性化这个概念，希望这篇文章对你有帮助

### **1. 什么是风险中性化？**

- **定义** ：“风口来了猪都可以飞上天”，风险中性化就是在去除已知的“风”。 风险中性化是一种通过消除特定风险因子对Alpha影响的技术，使Alpha的表现更加纯粹，专注于捕捉市场异常。通过风险中性化，可以剔除市场、行业或风格因子等已知风险对Alpha收益的干扰，从而更准确地评估Alpha的独立性和有效性。

- **理论背景** ：风险因子是影响资产收益的主要驱动因素，例如市场风险、行业风险、动量因子等。经典理论：Fama-French三因子模型（市场、规模、价值）和套利定价理论（APT）为风险因子模型奠定了基础。

### **2. 为什么要做风险中性化？**

- **消除已知风险因子的干扰** ：如果Alpha的收益完全由已知风险因子解释，则其价值有限，因为这些因子可以通过简单的模型复制。风险中性化可以帮助研究者专注于Alpha捕捉的独特市场异常。

- **降低风险** ：减少因风险因子回撤或波动性导致的潜在损失。提高Alpha在不同市场条件下的稳健性。

- **提升Alpha性能** ：通过剔除不必要的风险因子，提高Alpha的Sharpe比率，减少回撤，并优化换手率与交易成本之间的平衡。

### **3. 风险中性化的好处**

- **更高的Alpha独立性** ：通过剔除风险因子，Alpha表现更独立，能够更好地反映其捕捉市场异常的能力。

- **降低拥挤交易风险** ：减少因市场中大量投资者持有相似头寸而导致的价格剧烈波动。

- **增强多样性** ：通过不同的风险中性化方法，生成多样化的信号，丰富Alpha池。

- **优化长期表现** ：在保留Alpha收益的同时显著降低风险，提供更稳定、可靠的长期表现。

### **4. 如何使用风险中性化？**

- **界面操作** ：在BRAIN平台的回测界面中，进入模拟设置（Simulation Settings），在 `Neutralization` 选项中选择对应的风险中性化方法，BRAIN平台内置了六种风险中性：FAST, SLOW, SLOW_AND_FAST, CROWDING, STATISTICAL, REVERSION_AND_MOMENTUM (RAM)

- **API操作** ：在API中，通过调整代码中的 `neutralization` 参数实现。例如

```
{    "instrumentType": "EQUITY",    "region": "USA",    "universe": "TOP3000",    "delay": 1,    "decay": 0,    "neutralization": "FAST",  // 替换为上述对应的风险中性化方法    "truncation": 0.1,    "pasteurization": "ON",    "unitHandling": "VERIFY",    "nanHandling": "ON",    "language": "FASTEXPR",    "visualization": false}
```

### **5. 不同的风险中性化方法及其使用场景**

以下是平台支持的六种风险中性化方法的详细介绍：

#### **5.1 FAST**

- **定义** ：快速因子（Fast Factors）包括市场和行业风格因子，和高换手率的风格因子，例如反转因子。
- **适用场景** ：
  - 高换手率信号。
  - 需要捕捉短期市场趋势的Alpha。
- **注意事项** ：
  - 使用FAST中性化可能会增加Alpha的换手率。

#### **5.2 SLOW**

- **定义** ：慢速因子（Slow Factors）包括低换手率的风格因子，例如价值因子。
- **适用场景** ：
  - 低换手率信号。
  - 更关注长期趋势的Alpha。
- **注意事项** ：
  - SLOW因子适合稳健型投资策略。

#### **5.3 SLOW_AND_FAST**

- **定义** ：结合了慢速因子和快速因子的综合模型。
- **适用场景** ：
  - 需要同时考虑短期和长期趋势的Alpha。
  - 适合多样化的投资策略。
- **注意事项** ：
  - 可能会增加换手率，但能更全面地中性化风险。

#### **5.4 RAM（Reversion and Momentum）**

- **反转因子（REVERSION）** ：捕捉短期均值回归现象（如5天内的价格回调）。
- **定义** ：市场通常会对短期事件过度反应，导致暂时性错误定价。随着这些市场效率的修正，超卖的股票价格恢复，超买的股票价格回落。短期反转因子捕捉股票价格的均值回归现象，即近期表现不佳的股票往往在未来获得更高的回报，而近期表现较好的股票可能会出现回调。

- **动量因子（MOMENTUM）** ：捕捉长期价格趋势（如12个月内的价格趋势）。动量因子识别股票价格的持续趋势，即近期表现较好的股票往往继续上涨，而表现较差的股票则可能继续下跌。基于趋势跟随原则，已建立的价格趋势更可能延续而非逆转
- **适用场景** ：
  - 需要对冲短期均值回归和长期动量趋势的Alpha。
- **注意事项** ：
  - RAM中性化适用于多空平衡的Alpha。
  - 建议结合Alpha的特性，评估其是否容易受到反转或动量因子的影响。

#### **5.5 CROWDING**

- **定义** ：拥挤风险中性化，控制因市场中大量投资者持有相似头寸而导致的风险。随着更多投资者进入相同的头寸，交易的盈利能力可能下降。虽然价格在初期可能上涨，但随后可能变得脆弱，容易出现大幅下跌。
- **适用场景** ：需要减少拥挤交易风险的Alpha。当过多投资者同时试图卖出相同的头寸时，价格可能迅速下跌，导致更大的损失。适合在动量趋势强烈的市场中使用。

- **注意事项** ：拥挤风险中性化适用于多空平衡的Alpha。需要结合Alpha的特性，评估其是否容易受到拥挤交易的影响。

#### **5.6 STATISTICAL**

- **定义** ：因子模型的两大类别：基本面因子模型（Fundamental Factor Models）和基于统计因子模型（Statistical Factor Models），其中第二种使用统计技术（如主成分分析PCA或聚类分析）分析证券收益，识别市场数据中的模式和关系。依赖历史收益数据，通过统计方法预测未来表现或优化投资组合风险。经典案例比如：Roll和Ross的《套利定价理论的实证研究》（APT），强调使用统计方法提取影响资产收益的多个因子。
- **适用场景** ：捕捉复杂非线性关系的Alpha，生成在特定收益空间中表现良好的信号。

- **注意事项** ：
  - 统计风险中性化依赖于历史数据，可能对数据质量较为敏感。
  - 建议结合Alpha的特性，评估其是否适合统计模型的应用。

### **6. 总结**

- **风险中性化的核心价值** ：
  - 通过剔除已知风险因子，优化Alpha表现，降低风险。
- **选择合适的方法** ：
  - 根据Alpha的特点（如换手率、风险敞口）选择合适的风险中性化方法。
- **个人建议** ：
  - 在Simulation中先抽样一部分，尝试不同的风险中性化设置，评估其对Alpha表现的影响，选择最合适的再进行全量的回测

**英文原版文档阅读：**

[Getting Started: Risk Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Risk Neutralized Metrics | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Crowding Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with Statistical Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

[Getting Started with RAM Risk-Neutralized Alphas | WorldQuant BRAIN]([链接已屏蔽])

---

### 帖子 #28: 💻代码分享：拉取某个category下的全部dataset，并实现批量生产数据预处理，备战Pyramid
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

### 帖子 #29: 使用大语言模型创建一个BRAIN代码助手代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用大语言模型创建一个BRAIN代码助手代码优化_20098778380439.md
- **讨论数**: 5

最近发现ChatGPT已经提供了可以自创定制化大语言模型的功能（仅限Plus用户）。


> [!NOTE] [图片 OCR 识别内容]
> Nlew GPT
> Draft
> Create
> Configure
> GPT Builder
> Hil IIlhelp you build
> new GPT. You can say something like; "make
> Creative Who
> helps generate Visuals for new products"or "make
> software engineer Who helps
> format my Code。
> What would YoU like to make?
> @
> Message GPT Builder


该功能可以添加至多9个文档给大语言模型作为先验知识，使得它的回答更加精准与贴合。实测发现，文档内容不宜太长。我找到了BRAIN平台上我觉得最有用的几个文档。

1. [*Read this First * - Starter Pack]([链接已屏蔽])
2. [Introduction to Alphas]([链接已屏蔽])
3. [Introduction to BRAIN Expression Language]([链接已屏蔽])
4. [⭐ How BRAIN platform works]([链接已屏蔽])
5. [⭐ Alpha Examples for Silver Users🥈]([链接已屏蔽])
6. [Must-read posts: How to improve your Alphas🥉]([链接已屏蔽])
7. [Operators]([链接已屏蔽])
8. [BRAIN API]([链接已屏蔽])

把这些内容复制变成word后提交给大语言模型作为先验知识。它会变得很聪明噢。亲测好用👍我直接复制粘贴一篇Research Paper for Consultant: **[Research paper 45: Online reviews can predict long-term returns of individual stocks](/hc/en-us/community/posts/15770057302807-Research-paper-45-Online-reviews-can-predict-long-term-returns-of-individual-stocks)**


> [!NOTE] [图片 OCR 识别内容]
> You
> 思考什么是BRAIN Fast Expression并运用你对BRAIN 平台钓所有知识。闶读并分析下
> 列研究摘要
> 写WFast Expression。
> Research paper 45: Online reviews can predict long-term returns ofindividual stocks
> Followed by one person
> KA64574
> 4 months ago
> Abstract:
> Online reviews are Teedback voluntarily posted by consumers abouttheir consumption
> experiences. This feedbackindicates Clstomer attitudles such as affection; awareness
> ancl faith towarcs
> brandOr
> firm ancl dlemonstrates inherent connections Wih a
> companys future sales; Cash Tlow anc stock pricing. However; the predicting
> DOWerOf
  
> [!NOTE] [图片 OCR 识别内容]
> BRAIN Navigator
> Based onthe research summary YoU provided,the key conceptis that online reviews
> significantly impact long-term returns of individual stocks. Inthe context ofthe
> WorldQuant BRAIN platform and its Fast Expression language;
> Ne Canformulate 3n
> expression that incorporates social media data fields relevant to online reviews and
> sentiments. These data fields can be utilized to develop an alpha that reflects the
> influence of customer attitudes and feedback on stock performance。
> Given the data fields YOU Ve mentioned ( ` sc14
> posts
> total
> from the
> Socialmedia4
> cataset representing the total number of posts; and
> SC13
> aVeragesentiment
> fromthe
> Socialmedia3
> dataset representing average
> sentiment):
> potential Fast Expression could be formulated to capture the relationship
> betweenthe Volume of social media posts and the sentiment expressed in these posts
> towards
> company's stock price movement
> Here'san example of how 3 Fast Expression might Iook:
> fastexpr
> Copy code
> Fast Expression
> predict Iong
> temm Leturns based
> online reviews
> aVerage_sentiment
> 5C13
> aVeragesentiment;
> 1Average sentiment
> AOm
> total
> posts
> 5C14_posts_
> total
> t;
> Total
> number
> Of posts
> 1 Combining sentiment and
> Volume
> to predict stock Ieturns
> alpha
> rank(average
> Sentiment
> total_posts)
> post


---

### 帖子 #30: 每个字符之间的时间间隔, 单位秒
- **主帖链接**: https://support.worldquantbrain.com[L2] 向BRAIN Labs里粘贴代码的一个方法代码优化_32440962426007.md
- **讨论数**: 13

brain labs逐步开放了, 但是没法复制粘贴代码进去, 网络也不通, 只能手动敲字进去

这里提供一种方法, 能快速『敲』字进去

核心思路是用模拟键盘按键, 发送文本, 借助python的keyboard包实现

**注意: 模拟按键有风险, 谨慎尝试**

**## 使用示例**

1.在本机安装keyboard包: 
pip install keyboard

2.保存代码到py文件, 比如: send_key.py
其中的text是要复制的内容
```
import keyboard
import time

print('start')
# 等待2秒, 把鼠标光标切换到labs的输入框
time.sleep(2)

# 要输入的文本
text = '''
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
The quick brown fox jumps over the lazy dog
'''.strip()

# 每个字符之间的时间间隔, 单位秒
delay = 0.01

keyboard.write(text=text,delay= delay, exact= False)

```

3.执行脚本
python sned_key.py

4.把鼠标光标定位到labs里, 把浏览器里的输入法改为英文, 等待自动输入完成

**## 效果**


> [!NOTE] [图片 OCR 识别内容]
> Untitledipiynb
> testlmd
> 中又
> Ch=
> qizk
> Dr-i
> 5
> JupS
> TTTC!
> -h=
> 1a21
> clog
> Ch=
> qiek
> IT 
> 5
> JupS
> TTTC!
> -h=
> 1a21
> clog
> the quick
> brown
> TCK Jumps
> STTer
> Che Iazy
> 069


**## 改进思路**

可以指定一个快捷键, 执行快捷键后调用python脚本, 脚本读取剪贴板、发送文字, 实现更丝滑的复制粘贴体验

---

### 帖子 #31: 💻如何使用天翼云主机进行云端程序挂载
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何使用天翼云主机进行云端程序挂载_25891396254231.md
- **讨论数**: 4

本文不构成任何推荐，仅是经验分享，不涉及付费内容。

**Step1:进入免费试用中心👉点击链接 [免费试用中心 - 天翼云 (ctyun.cn)]([链接已屏蔽])**

**Step2:选择“个人认证”，并选择1核4G电脑**


> [!NOTE] [图片 OCR 识别内容]
> 免费试用
> 情遘云产品免J试用
> 豉豆方展。贫完为止
> 舌动拗则>
> 在此镝入趄要搜索豹内客
> 搜窝
> 筛选条件
> 清裤选条仵
> 53通用型云主机1核16
> 53通用型云主机1核26
> 镜像服务
> 用户认证类型
> 拓』音+RnDgR53e
> 环dt3与!
> OqRSC
> TnMNDOCz-NL7们 
> 菁墙昃立用
> 955O片
> 气/(丘L
> 企业认证
> 个人认证
> 观袼
> 1716
> 观掐
> 1526
> 慎逆7
> 5#
> 40G
> s坑基
> 40G
> 公共镇瘭奂梨哿憔
> 产品_别
> 带宽
> 1005
> 带竟
> Tbps
> 计
> 个人认证
> 个 人认l
> 介(U2
> 仔
> 欤揠库
> 免费试用2个月
> 免费试用1个月
> 长期免费试用
> 己-10,004
> 己:10,001
> 网培
> 安全及笞理
> 试用辕识
> 立剧试用
> 试用簌T
> 立8试用
> 试用狨
> 丽{订购


**Step3：选择Windows2019主机。**  
> [!NOTE] [图片 OCR 识别内容]
> 53通用型云主机1核26
> 贵州1-可用区1
> 规格选择
> 1核26
> Windows 2019 DataCente
> Centos7.5 64位(406)
> Das_AHcloud_V3.0.3.2.1_ASTACK_X8G_VRAS_VS.OROI COOSPCI02_tyy_230531(406)
> .00元
> Centos7.9 64位(406)
> Debian8.6 32位(406)
> Windows 2016 DataCenter 64位中文版(406)
> 翼视捷智云版-免费20方(406)
> Centos6.8 64位(406)
> Windows 2019 DataCenter 64位中文版2022(406)


**Step4:等待开通完毕**


> [!NOTE] [图片 OCR 识别内容]
> 岙
> 空利台
> 皿用中0
> 』订革'汀讲佾
> 玎革号:20250825142034021007
> 汀荤=; ;J
> i)  2025-0825142037
> 产新o  202492514.20:3
> T+19
> GTTo
> 开遁
> HEI
> 己下4
> 拜遁中
> 已尧氐
> he
> ITT{
> J
> &1
> JUI
> 1!T-
> 产8
> 玎蜚
> [
> CIo
> 52
> JLUILASSUITLOIA|
> TLCO 兀
> 己苎


**Step5:等待开通完毕后，进入控制台更改密码，并按照指示进行登陆。**


> [!NOTE] [图片 OCR 识别内容]
> 弹性云主机
> 可以21935云主玑。
> 也HTGAFUIDI Sg3GBRT
> 7rNT
> Ut性云士u
> 如塞云主
> L亚5 +丘;
> ]6
> 1竹-
> 0u
> 斥有坛行垃$
> NI
> OH
> LRN憧
> IPbf
> HqIt
> CCUEIhIAYeIUIU
> TCPUs|2G
> 4131256731
> 0459
> 可眍1
> 失
> UN
> 45493231-42224197
> TJo
> 192661IT7
> 54301引胡
> 刨柜?
> 亓玑
> [苎
> 蛮-1膏
> 讽汀
> [*切
> 呙f@


**Step6:进入远程电脑（主机）后，下载Microsoft Edge浏览器，并下载VS Code.  [vscode+python+jupyter环境搭建_哔哩哔哩_bilibili]([链接已屏蔽])**

提示：也可以在本地电脑下载好vs code后把安装包复制到云电脑上

---

### 帖子 #32: 💻如何免费领取阿里无影云电脑使用
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何免费领取阿里无影云电脑使用_25889938244375.md
- **讨论数**: 3

为了让大家在大数据时代顺利上云，提供如下教程供大家参考，不构成任何商业推荐。

1，下载 [阿里无影云电脑客户端]([链接已屏蔽])

2，打开下载好的无影云电脑客户端选择 **个人版云电脑** 使用支付宝二维码扫码登陆得到以下页面


> [!NOTE] [图片 OCR 识别内容]
> 中国电信 14:10
> N%k矧
> 83
> 首页
> @
> 建议您尽快完成实名认证
> 完成后有机会免费领取800小时云电脑时长包(有效期三个月)*;
> 可后续加购个人云电脑。
> 免费领取参与资格:  您的手机号绑定的所有阿里云账号此前均末参与过无影云电脑
> (专业版)  和无影云电脑〈标准版) 的免费试用活动。也未购买过云电脑。
> 用户EA50
> 贝订购1兑换
> 0 >
> 个人云电脑
> 管理镜像
> 为获得最佳使用体验
> 推荐丕载丞影客巳端连接云电脑
> Joo
> 暂无云电脑
> 去开通
> 家庭群组分配的云电脑
> 云电脑
> 家庭
> 我的账号


3，手机上完成上图顶部实名认证免费领取800小时云电脑试用

4，配置选择2核4G,机房选择离所在地最近的地区，系统镜像选择Windows

- 注意：选择云电脑而 **不是ECS云服务器**

5，完成免费试用云电脑领取后，使用支付宝重新扫码登陆阿里无影云电脑客户端

6，通过客户端连接云电脑开始使用


> [!NOTE] [图片 OCR 识别内容]
> 无影云电脑
> [
> 00
> 个人云电脑
> 运行中
> 云电脑基础款
> 订购云电脑
> 电源
> 更新
> 管理
> 团队分配的云电脑
> 暂无团队为您分配电脑。可主动申请加入


---

### 帖子 #33: 如何利用tvr操作符与alpha起舞论坛精选
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md
- **讨论数**: 30

##### ts_target_tvr_decay(x, lambda_min=0, lambda_max=1, target_tvr=0.1)

需要输入的参数为以上4个。

通过lambda_min值（不衰减），和lamdba_max值（衰减）的搜索空间中，去搜索lambda（λ)值，来得到target_tvr值。

也就是说，足够大的搜索空间，通过能得到一个λ，使得alpha的tvr为target_tvr值。

而目前多数顾问采用的是

##### lambda_min=0, lambda_max=1, target_tvr=[0.1,0.15,0.2,0.25] 这样的用法。

但按照我个人理解，设置成

##### lambda_min=0, lambda_max=5, target_tvr=[0.01，0.15，1]   （其中1是tvr参数的是上限值）

在扩大搜索空间后，使得alpha tvr的变化呈现缩小值、理想值、强化值。 这样的用法会更有意义。

**因为与其在固定的搜索空间去趋近target_tvr ，不如扩大搜索空间，跳出局部求解更为实际。如果将**

##### **lambda_min=0, lambda_max=5, target_tvr=0.15作为模板，那么搜索对于tvr弱的alpha，λ值会趋向于5，旧信号衰减更快，增强tvr,趋近0.15。对于tvr强的alpha，λ值会趋向于0，旧信号衰减更慢，降低tvr趋近0.15。是一个自适应的模板。类似decay的用法。**

若如果不存在相应的λ值，0.01和1也使得tvr的变化朝减弱和增强进行了延伸。综上所述，tvr 操作符总是能将tvr值按照自己理想的方向进行变化，是一个很实用的操作符。

比如这个alpha，看到tvr为2.58%， 通常是认为是一个beta而放弃提交。


> [!NOTE] [图片 OCR 识别内容]
> Settings
> GLB/D1/MINVOLTM
> IS Summary
> Period
> Streak: 107 day
> A single Data Set Alpha
> quantile(signed_power(Broup_neutralize( -
> Count_nans
> Winsorize
> ts_backfill(ern3_
> next_reptime,5),std=4),22)),
> Country)1.8)
> Aggregate Data
> Sharoe
> TUTNIUE
> FNss
> REUTR
> LTaOCI
> Narai
> 1.35
> 2.5896
> 0.86
> 5.02%
> 4.3096
> 38.959600
> Year
> Sharpe
> Turover
> Ftess
> Returns
> Drawdown
> Margln
> Long Count
> Short Count
> 2013
> 0.73
> 4.25
> 533
> 2.32
> 11.338:
> 367
> 355
> 2014
> 1.2-
> 3.25
> 3.2E3
> 2.159
> 20.03:
> 41|
> 3370
> 2015
>  5
> 3.33
> E73
> 2.77
> 038:
> 4316
> 1050
> TIC
> 1.46
> 03:
> TJ
> .39
> 4.6:
> 4133
> 33T1
> 2017
> 0.86
> 2.35
> ES%
> 1.759
> 11.575
> 4279
> -120
> 711?
> 1.73
> 2-
> 一273
> 1.379
> 3.32:
> 4621
> -52
> 2015
> 0.25
> _一=
> U6;
> 3.55
> 77304
> 4513
> 3335
> 2020
> 1.13
> 1.73
> 3
> 71 :
> 4333
> 333
> 2021
> 1.
> 88%
> 2.179
> 42.139
> 575-
> -332
> 2022
> 2.76
> 1_ 
> 13.253
> +3
> 201.329
> 573-
> 一37
> 2023
> 0
> 7.7%
> SS
> 155.84903
> 573
> 3375
> AMER
> Aggregate Data
> Snaroe
> TITIT
> Cc
> ReTylrns
> Drawdow
> Marsn
> 0.79
> 1.01%
> 0.28
> 1.59%
> 6.99%
> 31.469600
> APAC
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> CTOI
> MarEn
> 0.60
> 0.9196
> 0.23
> 1.7996
> 7.36%
> 39.479600
> EMEA
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Cratda'
> MarEn
> 96
> 0.659
> 0.35
> 1.629
> 3.149
> 49.709600
> Clone this Alphain
> newtab
> Risk neutralized


但通过增强，可能会使得tvr落到理想的区间内，可以不用担心因为tvr<5%or<10% 降低可用性。


> [!NOTE] [图片 OCR 识别内容]
> Simulation 14A
> Simulation 148
> Settings
> GLB/D1/MINVOLTM
> IS Summary
> Period
> Streak: 107 day
> Single Data Sez AIpha
> A Power Pool Alpha
> Pyramid theme: GLB/DTIEARNINGS %1
> ts_target
> tvr_decay(quantile(signed_power(growp_neutralize((
> count_nans
> winsorize(
> backfill
> (ern3
> next_reptime,5),std-4),22)),
> country ),1.8) ) 
> Iambda_min=o,
> lambda_max=3,
> target_tVrzl)
> Aggregate Data
> 33TO
> LJTC=
> TITE
> RCUTTS
> UTWIOOYT
> Harein
> 1.57
> 10.759
> 1.21
> 7.46%
> 4.9296
> 13.879600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margln
> Long Count
> Short Count
> 2013
> 12.31
> 7.73
> 一7
> 263沾
> 119
> 3715
> 351
> 2014
> 10.335
> 0.75
> 3.319
> SE
> 一SO
> 412E
> 3355
> 215
> 0.53
> 1.21
> 7.27
> 0
> 2.30沾
> 9
> 4343
> 4134
> TIC
> 2.37
> 181
> 5
> Ss
> 13.3_5:
> 4193
> 3331
> 2017
> 0.74
> 0.7
> 529:
> 2.17沾
> 339
> Jy
> J1IE
> 711?
> 0.67
> 5.13
> 4E
> 匕
> JFU
> 一
> 2015
> 5;
> 0.42
> 3.75
> 3.51沾
> 1.229
> 432
> 3555
> 1
> 10.76:
> 13.159
> 一 C
> 1 65:
> 21
> 3355
> 2021
> 10.75
> 15.329
> 2.50沾
> 29.46*o:
> 527
> -373
> 2022
> 3.35
> 0.35
> 27.37
> 355
> 3.554:
> 557
> -235
> 2023
> 0.5
> 6:
> 7.23
> 3310
> CI:;
> 4
> 5717
> 3570
> AMER
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Cryda
> Marsn
> 1.24
> 3.73%
> 0.63
> 3.22%
> 5.92%
> 17.279600
> APAC
> Aggregate Data
> Snaroe
> TITTT=
> Cc
> ReTylrns
> Cratda'
> MarEn
> 0.69
> 2.65%
> 0.25
> 1.70%
> 5.559
> 12.869600
> EMEA
> Aggregate Data
> Snaroe
> TITTT
> Cc
> ReTylCn
> Drawdowir
> Marsn
> 0.97
> 2.12%
> 0.40
> 2.17%
> 4.60%
> 20.509600
> Clone this Alphaina newtab
> Risk neutralized
> 41013
> OpnLOA


降低tvr的方式参考游戏王的降tvr帖子即可。

其他微调tvr的方式如调整decay trucation ts_op的day 亦可尝试。

---

### 帖子 #34: 一、从数据出发，依靠简单模版遍历搜索
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何找到更多alpha的思考新手进阶篇系列 - 第一篇单数据字段_27319802497687.md
- **讨论数**: 21

> **记得老师在上课时候讲过alpha research的两个主要脉络，从Idea出发和从Data出发，两种方式都可以找到alpha，而两种能力都具备一定是不断学习的方向。本文就从这两方面来分享一些如何提高alpha产量的思考和心得，也欢迎大家留言讨论！**

---

### 帖子 #35: 提取字段名（cut_index之前的部分）
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md
- **讨论数**: 23

顾名思义，在回测中常常能遇到高turn高sharpe高fit但低margin的因子。这类因子会直接影响我们的combined performance score，降低被PM采纳获得weight的机会，下面给大家分享如何降低换手率的常见方法

## ***如何理解turn，margin和return的关系？***

粗线条地说，return=turnover*margin，所以在给定收益的情况下，换手率越高，margin越低。margin跟手续费相关联，所以为了较高的margin，需要压低turnover。形象来说，我今天交易10次股票，挣了100块，那么我单笔交易平均收益10元，扣除5元手续费还有净利润。倘若我用1000次交易挣得100元，那么单笔交易收益降低至0.1元，远远不够手续费。

## ***降低turn的方式有哪些？***

常见的降turn方式有：增加decay，使用tradewhen，使用降turn运算符。


> [!NOTE] [图片 OCR 识别内容]
> 衰减Decay
> 通过将今天的值与前n夭的衰减值相结合;执行线性衰减函数。
> 它执行以下函数:
> [Jatel
> * T 十 T[date
> 1 (n
> 1)十. +Tlaate
> Decay_linear(I;n) =
> n十 (几一1)+1
> 允许输入的衰;减值:  整数"n" =
> 其中n >=0。
> 注意:  使用负数或非整数值进行衰减将破坏回测。
> 提示:  衰减可用于减少周转,但衰减值过大会削弱信号。


增加decay的方式可以提升信号的“一致性”，让信号不是那么频繁的变化（后文我们也会看到，一些降turn的op采取的也是类似的思想）

***使用tradewhen：*** tradewhen相当于增加开平仓条件，减少信号频繁变化的次数。直观的理解：市场并非天天大涨大跌，针对市场整体涨跌幅波动率小于1%（仅为举例）的时间窗口，不进行交易，这样可以减少一段时间内的整体换手率（但是会以表现为代价）

推荐阅读： [我可以使用 Trade_when 来降低流水率吗？– WorldQuant 大脑](../顾问 AM60509 (Rank 61)/[Commented] Can I use Trade_when to decease the Turnover_27675353441431.md)

***使用降turn运算符***


> [!NOTE] [图片 OCR 识别内容]
> ts_tarset_Tr_Jecaylx。
> ~ombo; RESUIaT
> Tune "-s_decay
> tO have
> turnoiierEqUalto
> Certain target wirh optimization Weight range berween lambda
> min |ambda_
> Iax
> lambda_min=0,
> ambda_max=1
> taraet_Wr=0.1]
> S
> ts_tarset_Tir_Jelts_limitfxy
> ~ombo; RESUIaT
> Tune  -s_Jelta_limi-'
> tO havs
> turnoiierequalto
> Certain taraet with optimization Weish: ranae between lambda_min;lambda_Max。
> lambda_min=0r
> ambda_mat-l
> AIsC
> please bE aware Ofhe
> forKandy Besides seting
> adV20 Orolune related data, yOU Can alsO SETyas
> COnsan。
> target_tvr=0.1]
> Bemus
> tS_tarset_TT_hUMDIK
> Combo
> Regular
> Tune "huMP
> tO have
> turnoverequa
> Certain target with oprimization Weignt range between lambda
> min, Iambda_Max
> lambda_min=n;
> SMbJa_Max=1
> target_TVr=0.1]
> S
> scaling



> [!NOTE] [图片 OCR 识别内容]
> hump
> Hump
> 0.01]
> Combo  Resular
> Limizs amount and ma
> anitude Of chanses in input (thus reducine urnoverj
> base
> SID
> TOTe
> hurp_decaylx p=0j
> Combo, Regular
> This aperator helps to ignore the values that Changed too litle corresponding
> DreioUs OnEs
> SMU
> ShOW More


降低turn运算符的核心思路在于限制变化幅度，从而减少仓位变化。可以指定turnover具体数值（实际结果会略微高于这个数值），但注意：较低的数值可能会完全破坏信号逻辑，使得因子无效。

## ***实操方式：***

本帖给出相关代码，使得可以按照turn区间筛选因子并利用降turn运算符进行处理回测。此外，本帖也提供了一个可以抓取并统计字段（向量类型数据按照vec运算符计算）的方法（来自本人另一篇文章： [如何统计得到的字段数？如何抓取多地区因子一起检验？ – WorldQuant BRAIN](../worldquant brain赛博游戏王/如何统计得到的字段数如何抓取多地区因子一起检验代码优化_28754183939351.md) ）

## **抓取因子：**

def get_alphas(start_date, end_date, sharpe_th, fitness_th,turnover_th_up,turnover_th_down, region, alpha_num, usage):

s = login()

output = []

# 3E large 3C less

count = 0

for i in range(0, alpha_num, 100):

print(i)

url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C" + end_date \

+ "T00:00:00-04:00&is.fitness%3E" + str(fitness_th) + "&is.sharpe%3E" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=-is.sharpe&hidden=false&type!=SUPER"

url_c = " [[链接已屏蔽])]([链接已屏蔽]))  \

+ "&status=UNSUBMITTED%1FIS_FAIL&dateCreated%3E=" + start_date  \

+ "T00:00:00-04:00&dateCreated%3C" + end_date \

+ "T00:00:00-04:00&is.fitness%3C-" + str(fitness_th) + "&is.sharpe%3C-" \

+ str(sharpe_th) + "&settings.region=" + region + "&order=is.sharpe&hidden=false&type!=SUPER"

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

#if (sharpe > 1.2 and sharpe < 1.6) or (sharpe < -1.2 and sharpe > -1.6):

if (longCount + shortCount) > 100 and (turnover>turnover_th_up) and (turnover<turnover_th_down):

if sharpe < -sharpe_th:

exp = "-%s"%exp

rec = [alpha_id, exp, sharpe, turnover, fitness, margin, dateCreated, decay]

print(rec)

if turnover > 0.7:

rec.append(decay*4)

elif turnover > 0.6:

rec.append(decay*3+3)

elif turnover > 0.5:

rec.append(decay*3)

elif turnover > 0.4:

rec.append(decay*2)

elif turnover > 0.35:

rec.append(decay+4)

elif turnover > 0.3:

rec.append(decay+2)

output.append(rec)

except:

print("%d finished re-login"%i)

s = login()

print("count: %d"%count)

return output

def transform(next_alpha_recs, region):

output = []

for rec in next_alpha_recs:

decay = rec[-1]

exp = rec[1]

output.append([exp,decay])

output_dict = {region : output}

return output_dict

def prune(next_alpha_recs, prefix, keep_num):

# prefix is the datafield prefix, fnd6, mdl175 ...

# keep_num is the num of top sharpe same-datafield alpha

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

decay = rec[-1]

exp = rec[1]

output.append([exp,decay])

return output

## get promising alphas to improve in the next order

fo_tracker = get_alphas("2025-03-01", "2025-03-24", 1.6,1,0.3,0.7, "ASI", 9000, "track")

print(len(fo_tracker))

get_alphas函数参数：开始日期，结束日期，最低sharpe，最低fit，turn下限，turn上限，地区，数量，抓取类型 。

## 减枝函数：

def prune_modified(next_alpha_recs,prefix,keep_num):

output = []

num_dict = defaultdict(int)

for rec in next_alpha_recs:

exp = rec[1]

sharpe = rec[2]

field = exp.split(prefix)[-1].split(",")[0]

if sharpe < 0:

field = "-%s"%field

if num_dict[field] < keep_num:

num_dict[field] += 1

output.append(rec)

return output

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

cut_index = min(backfill_index, end_index)

elif backfill_index != -1:

cut_index = backfill_index

elif end_index != -1:

cut_index = end_index

else:

# 如果没有找到这两个关键词，跳过此记录

continue

# 提取字段名（cut_index之前的部分）

field_name = full_field[cut_index+12:end_index].strip()

field_counts[field_name] += 1

return dict(field_counts)

def prune_second_order(inputdata,all_dict):

th_tracker1=inputdata.copy()

outpur=th_tracker1

for i in all_dict.keys():

if all_dict[i]>100:

outpur=prune_modified(outpur,i,2)

if all_dict[i]<=100 and all_dict[i]>20:

outpur=prune_modified(outpur,i,3)

if all_dict[i]>10 and all_dict[i]<=50:

outpur=prune_modified(outpur,i,4)

if all_dict[i]>3 and all_dict[i]<=10:

outpur=prune_modified(outpur,i,5)

return outpur

fo_tracker_new=[]

for i in fo_tracker:

if ';' not in i[1]:

fo_tracker_new.append(i)

print(len(fo_tracker_new))

all_dict=extract_fields(fo_tracker_new)

print(all_dict)

fo_tracker_tailed=prune_second_order(fo_tracker_new,all_dict)

fo_tracker_new=[]

for i in range(len(fo_tracker_tailed)):

index=0

for j in [';']:

if j in fo_tracker_tailed[i][1]:

index=1

if index==0:

fo_tracker_new.append(fo_tracker_tailed[i][1])

print(len(fo_tracker_tailed))

#all_dict=extract_fields(fo_tracker_new)

print(len(fo_tracker_new))

print(fo_tracker_new[0:3])

## **加入运算符：**

so_alpha_list = []

for expr in fo_tracker_new:

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_decay('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_hump('+expr+', lambda_min=0, lambda_max=1, target_tvr=0.3)')

so_alpha_list.append('hump_decay('+expr+', p=0)')

so_alpha_list.append('hump_decay('+expr+', p=0.01)')

so_alpha_list.append('hump_decay('+expr+', p=0.1)')

so_alpha_list.append('hump_decay('+expr+', p=1)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 240, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 120, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 20, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 60, factor =0.5)')

so_alpha_list.append('ts_decay_exp_window('+expr+', 40, factor =0.5)')

so_alpha_list.append('ts_decay_linear('+expr+', 240, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 120, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 60, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 40, dense = false)')

so_alpha_list.append('ts_decay_linear('+expr+', 20, dense = false)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+', 1, lambda_min=0, lambda_max=1,target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',close, lambda_min=0, lambda_max=1,target_tvr=0.3)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.05)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.1)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.15)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.2)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.25)')

so_alpha_list.append('ts_target_tvr_delta_limit('+expr+',adv20, lambda_min=0, lambda_max=1,target_tvr=0.3)')

print(len(so_alpha_list))

print(so_alpha_list[:3])

后续操作与一二三阶段模版相同，划分pool并进行回测即可。

注意：剪枝函数只能针对123阶因子进行减枝，如果使用模版可能需要进一步处理

推荐：将降turn操作作为“新2阶”使用，即：同时跑使用group的二阶与本文提到的操作，亦可作为“新3阶”使用，经近4个月的验证，有可实现性。

祝好运。

---

### 帖子 #36: ⭐如何自动化创建Alpha（Machine Alpha）合集内容Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何自动化创建AlphaMachine Alpha合集内容Alpha Template_25329126761879.md
- **讨论数**: 8

[Machine Alpha 基础知识1：什么是Alpha模板]([L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md)

[Machine Alpha 基础知识2：理解时间序列利润与规模比较模板]([L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md)

[Machine Alpha 基础知识3：继续理解时间序列模板，以情绪类数据为例]([L2] Machine Alpha 基础知识3继续理解时间序列模板以情绪类数据为例_25066287753367.md)

[Machine Alpha 基础知识4：如何利用对特定数据集的专业领域知识创造Alpha 模板——以期权数据为例](/hc/en-us/community/posts/25329053049495-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%864-%E5%A6%82%E4%BD%95%E5%88%A9%E7%94%A8%E5%AF%B9%E7%89%B9%E5%AE%9A%E6%95%B0%E6%8D%AE%E9%9B%86%E7%9A%84%E4%B8%93%E4%B8%9A%E9%A2%86%E5%9F%9F%E7%9F%A5%E8%AF%86%E5%88%9B%E9%80%A0Alpha-%E6%A8%A1%E6%9D%BF-%E4%BB%A5%E6%9C%9F%E6%9D%83%E6%95%B0%E6%8D%AE%E4%B8%BA%E4%BE%8B)

[Machine Alpha 基础知识5：模板的拓展——以CAPM模型的思路为例](../worldquant brain赛博游戏王/[L2] Machine Alpha 基础知识5模板的拓展以CAPM模型的思路为例_25329078901911.md)

[Machine Alpha 基础知识6：模板的拓展——数据处理的重要性，继续以CAPM模型的思路为例](/hc/en-us/community/posts/25526497127959-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%866-%E6%A8%A1%E6%9D%BF%E7%9A%84%E6%8B%93%E5%B1%95-%E6%95%B0%E6%8D%AE%E5%A4%84%E7%90%86%E7%9A%84%E9%87%8D%E8%A6%81%E6%80%A7-%E7%BB%A7%E7%BB%AD%E4%BB%A5CAPM%E6%A8%A1%E5%9E%8B%E7%9A%84%E6%80%9D%E8%B7%AF%E4%B8%BA%E4%BE%8B)

[Machine Alpha 基础知识7：数据标准化的重要性-以earning idea为例](/hc/en-us/community/posts/26015751078167-Machine-Alpha-%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%867-%E6%95%B0%E6%8D%AE%E6%A0%87%E5%87%86%E5%8C%96%E7%9A%84%E9%87%8D%E8%A6%81%E6%80%A7-%E4%BB%A5earning-idea%E4%B8%BA%E4%BE%8B)

[Machine Alpha 进阶知识1：如何优化Alpha模板中的参数案例一](../顾问 JR23144 (Rank 6)/[Commented] Machine Alpha 进阶知识1如何优化Alpha模板中的参数案例一_27789509613335.md)

[Machine Alpha 进阶知识2：如何优化Alpha模板中的参数案例（续）](../顾问 AY17279 (Rank 14)/[L2] Machine Alpha 进阶知识2如何优化Alpha模板中的参数案例续_28133464556311.md)

[Machine Alpha 进阶知识3：如何使用分析师数据中的期限结构](/hc/en-us/community/posts/32092606398999-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%863-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E5%88%86%E6%9E%90%E5%B8%88%E6%95%B0%E6%8D%AE%E4%B8%AD%E7%9A%84%E6%9C%9F%E9%99%90%E7%BB%93%E6%9E%84)

[Machine Alpha 进阶知识4：如何使用杜邦比率的思想来创造模板](/hc/en-us/community/posts/32198029389207-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%864-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%9D%9C%E9%82%A6%E6%AF%94%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

[Machine Alpha 进阶知识5：如何使用戈登增长率的思想来创造模板](/hc/en-us/community/posts/32227432164887-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%865-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%88%88%E7%99%BB%E5%A2%9E%E9%95%BF%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

[Machine Alpha 进阶知识6：如何使用PEG比率的思想来创造模板](/hc/en-us/community/posts/32495294399895-Machine-Alpha-%E8%BF%9B%E9%98%B6%E7%9F%A5%E8%AF%866-%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%88%88%E7%99%BB%E5%A2%9E%E9%95%BF%E7%8E%87%E7%9A%84%E6%80%9D%E6%83%B3%E6%9D%A5%E5%88%9B%E9%80%A0%E6%A8%A1%E6%9D%BF)

---

### 帖子 #37: 💻如何设置云电脑之京东云？
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何设置云电脑之京东云_25880682394263.md
- **讨论数**: 4

本文旨在帮助大家顺畅设置云电脑，不构成任何商业推荐，请自行选择合适的方案。

**免费试用7天： [官网试用中心-京东云 (jdcloud.com)]([链接已屏蔽])**

**
> [!NOTE] [图片 OCR 识别内容]
> 云产品体验库
> 丰富。安全
> 稳定的试用产品库,
> 满足您的需求。试用后仍可参与新人秒杀活动。
> 查看试用规则
> 热门推荐
> 弹性计算
> 存储
> 安全
> 人工智能
> 开发与运维
> 企业碰用
> 数据库
> 网络
> 容器和中间件
> 云主机 2核4G5M
> 云主机 2核4G5M
> 云电脑 4核86
> 轻量云主机2核2G3M
> 爆款机型。极致性价比。轻量建站
> 爆款机型
> 极致性价比,轻量建站
> 即开即用的"云上电脑"
> 不受时间
> 地
> 预装建站
> 电商
> 办公
> CRM等精选
> 应用部署。开发必选
> 应用部署
> 开发必选
> 点。设备限制,随时随地使用
> 软件。即开即用
> 配置 2核4G5M
> 配置 2核4G5M
> 10M基础带宽
> 2核26 _
> 406硬盘
> 存储 40G HDD
> 存储 60G HDD
> 无界高2办公
> 3/带宽。2006流量/月
> 续费低至4折
> 续费享优惠
> 即开即用
> 续费享优惠
> 免费试用30天
> 免费试用7天
> 免费试用7天
> 免费试用7天
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 了解产品
> 立即试用
> 鼍
**

**付费版本：** 丰俭由人，实测最低版本 2C2G1M （38/年）或3M（58/年）都可以顺畅运行并调试代码。传送门链接: [[链接已屏蔽])


> [!NOTE] [图片 OCR 识别内容]
> 爆品秒杀。下单领1000京豆
> 下单金额大于100元。 可抽奖领1000京豆_
> 瓜分200万京豆
> 活动规则
> 轻量 2核26 低至36元
> 轻量云主机 2核46 SM 1年
> 轻量云主机 2核46 SM 3年
> 轻量4核166 1年13年
> 超值!中午12点
> 晚上12点加库存
> 热销机型。
> 即开即用
> 超值推荐!
> 热销机型,
> 即开即用;
> 超值推荐!
> 热门游戏,
> 一键部署!
> 规格
> 2C26-406 SSD系统盘-3M
> 规格
> 2C46-606 SSD系统盘-5M
> 规格
> 2C46-606 SSD系统盘-5Mi
> 规格
> 4C166-1006 SSD系统盘-5 ~
> 时长 1年
> 时长 1年
> 时长
> 3年
> 时长 1年
> 56元1年
> 限购1台
> 新人专享
> 158元1年
> 限购1台
> 新人专享
> 618元/3年
> 限购1台
> 新人专享
> 518元/1年
> 限购1台
> 新人专享
> 原价522.72元/年
> 原价849.72元年
> 原e2459.+6元年
> 原价19944元+年
> 已抢:
> 609
> 已抢:
> 22%
> 已抢:
> 12%
> 已抢:
> 12%
> 立即秒杀
> 立即秒杀 
> 立即秒杀 
> 立即秒杀


选择所在城市最近的节点，选择windows server镜像，完成购买后，登录控制台，


> [!NOTE] [图片 OCR 识别内容]
> 京东云
> 品 云服务 `
> 佥概览
> 全站搜索
> 费用
> 工单
> 产品与服务
> 运维管理
> 安全管理
> 十新建
> 常用服务
> 云主机 CVM
> 原生容器
> 私有网络
> 云硬盘
> 对象存储
> 云搜索 Elasticsearch
> 云缓存 Redis
> 添加常用服务
> 请输入关键词
> 如云主机
> 最近访问:  轻量云主机
> 已开通服务
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 私有网络
> 1110
> 轻量云主机
> 1/100
> 云主机
> 华北-北京
> 华东-宿迁
> 华东-上海
> 华南-广州
> 总数量 (个)
> 运行中
> 即将过期
> 己过期
> 报警实例
> 0
> 0
> 0
> 0
> https:/Ilavm-console jdcloud.com/lavm/list


进入轻量云主机，重置主机密码, 充值密码后请先通过网页登录，选择VNC方式登录后。会弹出是否允许发现网络，选择是。设置完成后建议重启云电脑


> [!NOTE] [图片 OCR 识别内容]
> C乐云
> W  飞服劣 `
> 仙t笕
> 全站搜察
> (
> 贵用
> L单
> 笛条
> 渠迫官埋
> 灼物牛
> ()
> blngshul115
> 轻量云主机
> 网站搭建
> 搭建开发环境
> 搭建常用办公软件
> 主机列表
> 网站搭建
> 最佳实践
> 常见问题
> 镜像列表
> 使用镜像可以快速搭建您的个人博客 企业网站。电子商务平合
> 论坛等网站;  如果您需要手
> 使用WordPress镜像搭建网站
> 如何更换主机的镜像
> SSH密钥
> 动部署网站。可以参考最佳实践部署静态网站和部署Nodejs SSR应用。
> 使用Ghost镜像搭建博客系统
> 使用WebTerminal登录主机
> 推荐镜像
> 使用PrestaShop搭建跨境电商平台
> 修改防火墙端口号
> Ghost博客系
> Prestashop
> 部署静态网站
> 网站备案操作说明
> WordPress
> =Bhost
> 统
> 电商平台
> 手动搭建WordPress应用
> 轻量云主机如何备份
> 部署Nodejs SSR应用
> 轻量云主机超过流量包后如何计费
> 轻量云主机支持的镜像说明
> 视频演示专区 
> 关机
> 
> 重启
> 重置密码
> 华北-北京
> 华南-广州
> 华东-宿迁
> 创建
> 实例名称
> 请输入实例名称。
> I0
> 重装系统
> 实例0
> 实例名称
> 镜像名称
> 配置
> 状态
> 地址
> 计费
> 续费
> 升级套餐
> Windows Server
> CPU: 2核
> 运行中
> 104.
> 到期时间:  2025-08-1023:59:59
> 登录
> 2019数据中心版
> 内存:  268
> 更多
> 1/
> 64位中文版
> 带宽: 1Mbps
> 共1条
> 10条顷


远程登录云主机： [登录Windows实例--云主机 CVM-帮助文档-京东云 (jdcloud.com)]([链接已屏蔽])

建议使用（Windows）远程登录或（Mac）Remost Desktop 进行登录，输入上图中你的公网IP，用户名（默认Administrator）和密码，即可连接登录。至此完成云电脑的设置，在云电脑上搭建所需python环境即可

---

### 帖子 #38: 1. 下载/增量更新download_data(session, flag_increment=True)Self-correlation 0.7691 is above cutoff of 0.7 and Sharpe not better by 10.0% or more.这是代码计算结果：alpha_id:  XgQqkZda self_corr:  0.7691116930719178alpha_id = "XgQqkZda"Self-correlation is 0.4589, which is above cutoff of 0.7, or Sharpe is better by 10.0% or more.这是代码计算结果：alpha_id:  zq6wpknV self_corr:  0.48371278563080605alpha_id = "zq6wpknV"加载数据os_alpha_ids, os_alpha_rets = load_data(tag='SelfCorr')self_corr = calc_self_corr(    session,    alpha_id=alpha_id,    os_alpha_rets=os_alpha_rets,    os_alpha_ids=os_alpha_ids,)print("alpha_id: ", alpha_id, "self_corr: ", self_corr)
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

### 帖子 #39: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 理解模板与数据集 我将搜索空间缩小10万倍Alpha Template_34478018977687.md
- **讨论数**: 25

***发现模板***

在  *【有奖】Alpha*  *模板征文*   的帖子中发现一篇关于model的模板分享，我正好在跑model，所以研究了一下。 传送门 [../顾问 JR23144 (Rank 6)/[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md/comments/34226901158807](../顾问 JR23144 (Rank 6)/[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md/comments/34226901158807)


> [!NOTE] [图片 OCR 识别内容]
> 4k76468
> Uaysago
> EUeC
> 针对 model264 的 ATOM 模版
> 511TI
> op/> (〈ndl264_predictl/>, <mdl264_predict_2/>, 〈ndl264_predict_3/)
> 娈显; ssum_op/: 可以add和multiply等计箅`计得分的]运算符
> multiply 会放大股票之间得分差
> 异。可能会有更好的表现
> 变量2: <mdl264_predictlxI/: 可以是md264中孤」趋势方向的字段
> 如:
> mdl264_emp_Class
> 述为:
> Predictedtrend
> Numberofemployees
> [:fall, 2: neutral, 3: move UpI
> 员工数显"
> 的预则趋势。数据离敞,
> 只有1。2,3三种取值。可以通过带有 class '的后缀选到。即:
> mdl264_XXK_class
> 搜索空间大小: Imodel264为例。筛选userCountm大的前20个字段。为2*20*19*18=13680
> 考虑add
> 和multipy 怍用类似。回则任务可以只使用其中
> 在捉交时遍历运筲符选挥表现好的捉3呵可
> 所以搜
> 索空间可进
> 步压缩为20*19*18=6840
> 模Hidea: modelz64是时序上的顶则数据
> 通过访问1a6得知。该类数据离散且没有缺失值和0值
> 故不
> 需要回坑
> 截断
> 变换等预处理
> mdl264_X
> class这类字段是针对多维度经济。财务。市场及技术指标
> 等的末来趋势预测结果
> 可犄该字段理舞为得分
> 上张得分越高,
> 下跌得分越低。所以逦过将股剽多度
> 预则数据的得分累计。比如正向指标得分高意味者企业进步
> 儆多。但是得分高低不愆味者殿票表 的好
> 比0负向指标肯定是下踯好。|以衡分低才儆多
> 产出效果;  回刘75812次
> 技#abslsharpel>1, 2筛选
> 1出590个alpha
> 建议其他顾问末来芸试的探索方向: mdl264该类数据有400+个
> 搜秦空间巨大。有些是正向指标
> 有些
> 是负向指标。有些字段指际类似。直接:加可能没意义。所以可以逦过让 MCP 区分指标的正向与负向展
> 性。再筛选出关联度低的预测字段。再将方问一致且相关性低的字段迸行组合
> 可以大大降低溲索空问,
> 能得到重全面的预剡并提升预测的准确性。
> 后续可以继续将该alpha当作鼓据字段使用到
> 阶的流程
> @@


***研究模板***

mdl264数据集的字段都是对于未来趋势的预测，模板的思路是 **将多个预测信号累加，得到一个更强，更稳定的信号。** 但是跑这个模板会遇到几个问题：

1. mdl264有2036个字段，如果直接33组合，搜索空间C(2036,3)大概有14亿，我们需要降低搜索空间
2. 观察lab可知mdl264大部分field的value分布在0~1之间。如果使用multiply，三数相乘，得到的结果差距最高可达千倍，这可能导致权重集中的问题。所以我只使用了add，如果使用multiply可能得搭配rank，zscore等函数。
3. 数据集内的字段都是趋势预测指标，但有上涨、下跌、中性等类型，同类型的字段相加才有意义。

***实践过程***

为避免有缺少年份数据的field，我先将所有裸字段回测一遍，并执行筛查


> [!NOTE] [图片 OCR 识别内容]
> 7030003
> 01264_
> 10_11
> 1.9
> +4815_
> 8.91
> 8.830463
> 2025-88-25T89:45:06-04.08
> XZQuJja
> MOL264_open_I1
> 1.82,
> 0.5905
> 8.8。0.000384
> 2025-08-25189:45:17-04:88
> Iwopvqe
> Nd1264_rdip_11
> 1.46
> 8,8431,1.87,
> 883892,
> 2025-98-25189;4;07-04:88
> Ja213-
> Nd1264_rdipa_11
> 1.27
> 841,
> 8.82,
> 80268
> 2825
> 88-25111;22;26-04;88
> 276XGVd
> 0d1264rdipo_11
> 1,26
> 042,0.8,
> 932523
> 2825-38-25189;5;45-94:88
> I3brLwk
> 001264_OeDs
> SUr_11'
> 1.25
> 9.8345
> .881536
> 2925
> 88-25719;10;27-84:88
> 13b3V-1
> 0d1264_11_^6_1'
> 1.2
> 8.0853
> 8.92,
> 8.331519
> 2925
> 88-25789;55;39
> 8:88
> ZV3VEGx
> 041264_11_pi
> 1.19
> 8.1852
> 0.77
> 8.333332
> 2825.88-25189:46:85.84:88
> RxOxpVe
> N1264_rdipeps_-1
> 1.18,
> 0.8417,
> 0.882+76 _
> 2825
> 88.25T89:51:14.84:88
> q2rRq90
> 01264_h10m10_11
> 1.17,
> 0.2323
> 0.72,
> 0.888761
> 2025
> 83-25T10.02:39
> 8:8O
> BWgepGl
> 0d1264_hieh_11'
> 1.15,
> 506,
> 48。0.000343,
> 2025
> 08-25189:58:33-04:88
> IrQ2lED
> Md1264_11Bhc_qetdti
> 1.1
> 8.8918,8.77,
> 881234
> 2825
> 88-25193;45:45-0;03
> 823Jvb0
> md1264_11m3aBtl_se
> 1.13,
> 8.1397
> 888632
> 2825-88-25110;02:39-84;83
> OOPLnGI
> mdl264price
> day_IVa_I1
> 1.12,
> 8,4679
> 8.51
> 983421
> 2825-88-25189:5;35-84;99
> TPbPbG5
> 001264
> Dstk Class
> 1.1
> 0.3335
> O.6,
> 0.3322-1
> 2025
> 88-25789
> 43;53
> 84:88
> RXnRQZO
> 0d1264_11_spe_rtnze_rB' 
> 1.83,
> 8.1436
> 53,
> 888733,
> 2825
> 83-25710;22:3-84;33
> GGVbOPS
> 041264_31_rta
> 1.87,
> 8.2227,
> #52
> 8.033455
> 2025
> 83-25T11:12;19
> 34:88
> RxOxbNO
> 01264
> 11 Ist
> 1.87,
> 2155,
> 56,
> 888557
> 2825
> 88.25789:52:88
> 84:88
> ATZTXE2
> 01264_11_M3r-yf_spTC_Se
> 8955
> O.51,
> 883367
> 2025-03
> 25189:49:37.84:88
> 9SLOXEe
> md1264_debt_ChR 11
> 1.05
> 0.8691,
> 8.74
> 881816
> 2025-88-25109:44:55-84:88
> nGRjRj
> 0d1264_pstk_13
> 1.83,
> 8.8295,
> 8.53,
> 9,992229
> 2025-98-25189;5;45-04:88
> UXZSNI
> 001264_11_2ktsc
> 1.83,
> 0,0367,
> 8.56
> 902885
> 2825
> 88-25789;45;87-84:88
> jbzxnj
> 0d126411mrIyt_Spe_Se
> 1.82,
> 8.1888, 0.1,
> 8.881872,
> 2825-88-25719:23;-6-84;93'
> 2388
> 2420
> #蒹######{
> 筛除厂子形a12ha
> 革#####茸##
> aIphd量
> 2015,
> 开始执行筛除
> Oupu
> truncoted;Iz: Os
> SollhleelemenL Or open in
> Lee Adjust cell output Selings。
> 筛除迸度
> 193
> 2315/2815 [1:39:25<88:83,
> 2.955/1]
> 筛除完成
> 筛除 apha_
> ids:
> #####苹###  筛除厂子形a1pha
> ########=
> COuI:
> 2815


筛查后发现此数据集 **没有缺少年份的数据，** 且一些字段呈现较强信号。信号弱侧面说明该字段预测趋势不准确，所以我将信号较弱的字段筛除(sharp < 0.5)，得到707个field

> field及下文涉及代码见link   [[链接已屏蔽])    密码:  wq123

观察数据集字段的描述可知，预测类型有4种：


> [!NOTE] [图片 OCR 识别内容]
> #售1S!
> 4
> Ie
> [法
> MOTC_I_rb_dls_dl_Iqhe
> 死_~丰字正T
> mdIt_I_b_dls_dt_IIqilgu
> 二』(6蓦民芥《人] ~寺=yM下r[5
> 下行酱势
> TTTIF!
> _TBb_JI_d
> !U_Le
> 中性趋势
> 值分布为0~1
> TTTIF!
> _dl3_dt_ZI_qIgu
> O
> (0#『+55-「:王
> TTCIZE'1_+sb_dls_dI _
> 巩:+4L s之
> 上行趱势
> TTTIF!
> dl3_dt_3I_qIgu
> 『9》 (扫#0『』]
> 末蕈95上-三
> DCLE
> xgb_dle
> CmCn
> TC
> Fs
> 幸0;
> 上
> 枚举值: 1-下行  2-中性  3-上行
> TCDE 1
> xgbdlo
> UOg
> 9 (扣#@节635+9琴 ( TF;? =_;
> h
> UIOhC


通过description关键词，可以将四种类型数据分类


> [!NOTE] [图片 OCR 识别内容]
> dataset list
> [ 'model264' ]
> data_type
> MATRIX
> combined fnds
> get_combined_datafields(sess, searchscope, dataset_list,
> data_type)
> [7]
> 49.15
> 正在处理数据集: model264
> 上行趋势 &十性趋势字段
> UP_fields
> Combined
> combined_fnds[ ' description' ].str. contains ( 'up
> Case=False,
> na=False
> combined_fnds [ ' description' ]
> str. contains ( 'neutral
> Case=False,
> nasFalse)
> ~Combined_fnds [ ' description' ].str. contains ( ' Predicted
> casesFalse, nasFalse) ]
> len(up_fields)
> [11]
> 0,0s
> 1064
> 下行趋势字段
> fall field
> combined_fnds [ combined_fnds [ ' description' ].str. contains ( 'fall' 二
> case=False, nasFalse _
> & ~combined_fnds [ ' description' ].str. contains ( ' Predicted
> case=False, nasFalse) ]
> len (fall_field )
> [8]
> 00s
> 554
> 放牮字剧
> oth field
> combined_fnds [ combined_fnds [ ' description
> ].str. contains
> Predicted'
> casezFalse, nasFalse) ]
> len(oth_field)
> [12]
> 00s
> 41
> fnds[


以下行趋势为例，我们得到了219个字段。此时如果33组合，搜索空间C(219,3)约170万，需要继续减小搜索空间。

观察这些字段的描述，可以发现其中有明显的分类行为。


> [!NOTE] [图片 OCR 识别内容]
> 46  mdl?64_11_Idav
> The Drobabili: tnat the Future trend Of
> Deferred Rerenle
> Long Term  rill be Sall
> md1264_11_mlm21_tr
> The Drobabilir; that the Tuture Trend Ot
> Price Womentug; I2y-UV'
> Til1 fall
> 480dl264_11_mlr_If_spb_se
> The probabili that the TutUre Trend
> Fvl BPs Pevision
> Till fall
> 『d1264_I1mlr_Iyi_sDd_Se
> IIe probabili Ihat the TuUIC Trend Or
> Fl DPS Revision
> UI will fall
> 50  ud1264_11nlr1_SDe_S
> Ihe probabili; that the Luture trend OI
> Fil EPS Rewis_On
> 『1l1 be
> 0d1264_11mlr_Is_spfC_se
> Ine probabili tnat the Future rend
> Fil CFPS Reiision
> WI11 fal
> mdl264_11_0lr_15_ran_se
> The probabilir that the future trend
> Fyl
> XY serision
> 111 +al!
> 0d1264_11Mlr_cer_Se
> The probabilirr that the future
> Trend
> Recomendation Rerision;
> II sill be Cal1
> 4d1264_11mlr_Btl_se
> The probabilit that the Tuture
> Trend OT
> LoIT
> TPNNI
> Groath Revision,
> 5111 be -311
> Nd1264_11_nlr_Itn_SDC_SC
> Tne Drobabilit tnat the Tuture
> [end
> V EPS Revision
> I111 Ja_
> 56  nd126411mlr_men_SDIC_Se
> Ine Drobabili
> tnat the urure
> irend
> MI CFPS Reision
> I nil1
> fa
> 57  mdl?64_11_mlr_mtn_van_se
> Tne probabi
> tnat the Huture
> CTC
> TIM Terision
> J ri fa
> 5S ndl26'_11_nlr_Dr_se
> The Drobabi
> that
> Tuture trend
> Tarer Price Rersion
> 山~b211
> Ud1264_11n3d_IyT_SDh_Se
> Drobabilir
> that
> Tuture Trend
> Frl BPs irtusion
> (up dom ratiol
> 3l will be fall
> 0d1264_11_"30_12_sDd_Se
> Ihe probabilir
> Ihat the TUTUI Irend O
> Frl DPs dirfusion
> (uD domn ratiol
> 3V 『ill fall
> 44126+114301-sDCSE
> IIe Drobabili
> tat the IutUIe end
> "Fl
> EPS Dirfuson
> (UD Down Ratiol。
> 3V will be 1al1
> 0d1264_11036_15_van_5e
> Ine probabili tnat the Luture rend
> "Fil
> XIV Diifusion
> {Up  Dowi Rato,
> 3I" *111 be fai
> mdl264_11_03a_cer_se
> The probabilit that the future trend Of
> Lecomendatron Dittusior
> 〈O doan ratiol, S
> r」! be +a11
> 54|001264_11n3d_8TI_Se
> The probabilit that the future
> trend ot
> TSTN
> groath ditzusion
> (up/down rariol,
> 111 +311
> 55|"d1264_11m3r_Iyi_Spb_se
> The probabilit that the future
> Trend OT
> Fil
> BPS revision
> 3l" will be fall
> 『d1264_11m3r_Ii_SDd_Se
> Ihe probabili that the Huture
> [end Ot
> Fil
> DPS revision
> 3I' will fall
> #d1264_11m3r_15_Spe_Se
> Ihe probabili" tnat the Future
> trend Or
> Fil
> EPS -eision
> 3V'  will Iall
> md1264_11_m3r_15_spfC_se
> Ihe probabili that the future
> trend Of
> Fii
> CFPS -eision
> wil1 fall
> md1264_11_Nr_I5_van_Se
> The Probabilit; that the Tuture
> trend Ot
> Fil
> XY rerision
> 31 *111 fal
> 70_Md1264_11_n3r_mtn_spb_se
> The Drobabili that the tuture trend of  TI BPS rerision 3 ril1 tall
> Long


通过AI分析，将219个字段根据经济学维度分成了13类


> [!NOTE] [图片 OCR 识别内容]
> 分类
> 英文分类名
> 描述
> 债务与杠杆
> Debt & Leverage
> 与公司债务结构。到期时间。杠杆水平相郑
> 盈利能力与利润率
> Profitability & Margins
> 衡量公司盈利能力和各种利润率的指标
> 收益与每股指标
> Earnings & Per-Share Metrics
> 与公司收益。每股收益 (EPS) 及其变体:}
> 现金流
> Cash Flow
> 反映公司现金流入流出情况的指标
> 分析师预期与修订
> Analyst Expectations & Revisions
> 基于分析师对财务指标 (如EPS
> 技术指标与价格动量
> Technical Indicators & Price Momentum
> 基于价格。成交量等市场数据计算的技
> 期权与市场情绪
> Options & Market Sentiment
> 反映期权市场活动。做空兴趣和市场情绪呦
> 新闻与情绪指标
> News & Sentiment Indicators
> 基于新闻情感。异常关注度等文本或情绪分
> 季节性与时序指标
> Seasonality &
> 反映股票季节性周期。特定时间窗口表现呦扌
> 税收与特殊项目
> Taxes & Special Items
> 与公司税务负担
> 递延税项及-次性牡
> TTTCL |7TT5
> T
> 1TT4 川I  t9n+
> +04wotoynhtutr
> DeepSeek
> Timing


> 分类字段见link   [[链接已屏蔽])    密码: wq123

我抽查了一些相同分类中裸字段的相关性，发现相关性基本>0.7，所以每个分类可以只选出代表性的几个字段(我通过裸字段回测的sharp排序筛选)。

最终，每个分类我保留了3个代表性字段，共39个字段，可组合出C(39,3)=9139个表达式，相较于直接暴力组合，大大缩小了搜索空间。相较于使用userCount、alphaCount倒序取前n条数据，此方法得到的表达式信号更强，跑出的alpha相互的相关性更低。

***扩展思路***

此模板我跑了1w次回测，得到500+能交的ppa(未相关性剪枝)，还交了两个RA


> [!NOTE] [图片 OCR 识别内容]
> AUNTCNaLC Dol
> SIUL Uer StIII
> 1.76
> 7.159
> 1.07
> 4.64%
> 2.919
> 12994
> uo
> 1
> I
> rs
> s
> Teoo
> T
> To
> ToIE'tton
> Lu
> n
> Toe
> L go
> e(
> e od
> Cone AUa
> Chart
> Rist neutralzed
> ACTCRLCC
> 7.1595
> 2.149
> 2,299
> 5,985


模板是三个字段相加，可否是2个，4个?

模板过于粗糙，可以在其基础上继续增强，套入一二三阶或其他模板

---

### 帖子 #40: 理解顾问最重要的指标Value Factor! 分享不同数值对应的预计每日收入
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

### 帖子 #41: 香港地区的同学如何登陆？
- **主帖链接**: https://support.worldquantbrain.com[L2] 香港地区的同学如何登陆_31134702342167.md
- **讨论数**: 9

```
import requestsimport jsonfrom os.path import expanduserfrom urllib.parse import urljoindef authenticate():    # Create a session to persistently store the headers    s = requests.Session()    try:        # Load credentials from JSON file in home directory        with open(expanduser('~/.brain_credentials'), 'r') as f:            credentials = json.load(f)            if len(credentials) != 2:                raise ValueError("Credentials file should contain exactly two elements: [email, password]")            s.auth = tuple(credentials)    except FileNotFoundError:        print("Error: Could not find credentials file at ~/.brain_credentials")        print("Please create a JSON file with your credentials in the format: [\"<email>\", \"<password>\"]")        return None    except json.JSONDecodeError:        print("Error: Could not parse credentials file. Please ensure it's valid JSON.")        return None    except Exception as e:        print(f"Error loading credentials: {str(e)}")        return None    # Send authentication request    auth_url = '[链接已屏蔽]    response = s.post(auth_url)    # Check response status    if response.status_code == requests.codes.ok:        print("Successfully authenticated!")        return s    elif response.status_code == requests.codes.unauthorized:        if "WWW-Authenticate" in response.headers and response.headers["WWW-Authenticate"] == "persona":            print("Biometric authentication required.")            biometric_url = urljoin(response.url, response.headers["Location"])            print(f"Please visit this URL in your browser to complete biometric authentication:\n{biometric_url}")                        # Wait for user to complete biometric authentication            input("After completing biometric authentication in your browser, press Enter to continue...")                        # Try to authenticate again after biometric verification            biometric_response = s.post(biometric_url)            if biometric_response.status_code == requests.codes.ok:                print("Successfully authenticated with biometrics!")                return s            else:                print(f"Biometric authentication failed with status code: {biometric_response.status_code}")                return None        else:            print("Authentication failed: Incorrect email or password")            return None    else:        print(f"Authentication failed with status code: {response.status_code}")        return Noneif __name__ == "__main__":    session = authenticate()    if session:        # You can now use the authenticated session for subsequent API calls        print("Authentication successful. Session is ready for API calls.")        # Example: response = session.get('[链接已屏蔽])    else:        print("Authentication failed. Please check your credentials and try again.")
```

运行上述代码后，你会被要求点击一个链接进行人脸活体认证，认证完毕后，就会登陆成功，返回session

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《Getting started with India Alphas置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Getting started with India Alphas置顶的_36059391387415.md
- **评论时间**: 2个月前

Thanks for sharing. I've been focusing on alpha development for the India region recently, and the biggest hurdle is still the robust universe Sharpe test.

---

### 探讨 #2: 关于《[BRAIN TIPS] How can you improve Alpha coverage with ts_backfill and group_backfill?置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] How can you improve Alpha coverage with ts_backfill and group_backfill置顶的_40576075554327.md
- **评论时间**: 22天前

Thanks for sharing. The point that backfill lookback can affect Alpha performance, and that one lookback should not be applied everywhere, is very useful for parameter tuning and optimization.

---

### 探讨 #3: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Community Leader - 因子构造】提升挖矿产率深度分析数据集经验分享.md
- **评论时间**: 5个月前

感谢大佬的无私分享，也感谢华子哥的插件，精准导航太强了。限5000回测的当下，缩小搜索空间太有必要了。

**==================================================================================
路漫漫其修远兮，吾将上下而求索。
==================================================================================**

---

### 探讨 #4: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader - 因子构造】提升挖矿产率深度分析数据集经验分享_36744363518999.md
- **评论时间**: 5个月前

感谢大佬的无私分享，也感谢华子哥的插件，精准导航太强了。限5000回测的当下，缩小搜索空间太有必要了。

**==================================================================================
路漫漫其修远兮，吾将上下而求索。
==================================================================================**

---

### 探讨 #5: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template.md
- **评论时间**: 4 months ago

感谢大佬分享的模板。最近EUR地区开了新宇宙TOPCS1600，试试这个模板好使不。祝大佬一马当先，马到成功。

---

### 探讨 #6: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子构造 】AI严选条件动量模版点塔SentimentAlpha Template_37083826431895.md
- **评论时间**: 4个月前

感谢大佬分享的模板。最近EUR地区开了新宇宙TOPCS1600，试试这个模板好使不。祝大佬一马当先，马到成功。

---

### 探讨 #7: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **评论时间**: 6个月前

感谢大佬分享。在因子指标合格的情况下，更注重is performance的情况，特别是fitness，简单直接，学习了

---

### 探讨 #8: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md
- **评论时间**: 6个月前

感谢大佬分享。在因子指标合格的情况下，更注重is performance的情况，特别是fitness，简单直接，学习了

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Eligibility Criteria篇】一文告诉你如何GOLD直通Grandmaster上篇置顶的论坛精选_39922788056343.md
- **评论时间**: 1个月前

感谢大佬干货满满的分享，太强了。这塔点的，赏心悦目。国区大佬有东西是真分享，感谢。

---

### 探讨 #10: 关于《【Template by Tiger】 关于news21中的fast_d1的一个思路》的评论回复
- **帖子链接**: [Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路.md
- **评论时间**: 5个月前

模板、数字字段全都有，虎哥真是威武霸气！感谢分享

=============================================================================

路漫漫其修远兮，吾将上下而求索。

=============================================================================

---

### 探讨 #11: 关于《【Template by Tiger】 关于news21中的fast_d1的一个思路》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Template by Tiger】 关于news21中的fast_d1的一个思路_37256491735959.md
- **评论时间**: 5个月前

模板、数字字段全都有，虎哥真是威武霸气！感谢分享

=============================================================================

路漫漫其修远兮，吾将上下而求索。

=============================================================================

---

### 探讨 #12: 关于《【效率王】七十二变的大升级_跨区点塔？指定Category?完全不是问题！》的评论回复
- **帖子链接**: [Commented] 【效率王】七十二变的大升级_跨区点塔指定Category完全不是问题.md
- **评论时间**: 5个月前

工具是个好工具，用什么大模型很重要，免费的大模型出货率实在有点感人……

---

### 探讨 #13: 关于《【效率王】七十二变的大升级_跨区点塔？指定Category?完全不是问题！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变的大升级_跨区点塔指定Category完全不是问题_36974265471511.md
- **评论时间**: 5个月前

工具是个好工具，用什么大模型很重要，免费的大模型出货率实在有点感人……

---

### 探讨 #14: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【效率王】你说你没有模板这里你多得用不完.md
- **评论时间**: 5个月前

AI时代，工具是越来越多，看似简化了很多流程，效率提升了很多。但如果自身没有理解，很容易被AI给糊弄住，自己的思考至关重要。

---

### 探讨 #15: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **评论时间**: 5个月前

AI时代，工具是越来越多，看似简化了很多流程，效率提升了很多。但如果自身没有理解，很容易被AI给糊弄住，自己的思考至关重要。

---

### 探讨 #16: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞.md
- **评论时间**: 5个月前

搞出这个cnhkmcp_app的大佬真是天才，太佩服了，现在首页还有使用说明，简单明了。感谢大佬。

---

### 探讨 #17: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **评论时间**: 5个月前

搞出这个cnhkmcp_app的大佬真是天才，太佩服了，现在首页还有使用说明，简单明了。感谢大佬。

---

### 探讨 #18: 关于《【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的.md
- **评论时间**: 5个月前

今天更新了Combined Alpha Performance，惨不忍睹。再来复习下基础知识，依然有收获，感谢大佬的分享。

---

### 探讨 #19: 关于《根据alpha ID 获取 prod correlationdef get_prod_corr(session, alpha_id):    response = session.get(f"https://api.worldquantbrain.com/alphas/{alpha_id}/correlations/prod")    if response.status_code == 200 and "records" in response.json():        columns = [dct["name"] for dct in response.json()["schema"]["properties"]]        self_corr_df = pd.DataFrame(response.json()["records"], columns=columns)        if not self_corr_df.empty:            print(f'{alpha_id} max: {response.json()["max"]} min: {response.json()["min"]}')            set_alpha_desc(session, alpha_id, f' max: {response.json()["max"]} min: {response.json()["min"]}')        return self_corr_df    else:        return pd.DataFrame(columns=["correlation"])因为经常第一次获取不到内容，可以调用这个函数来多次获取def get_prod_corr_waiting(session, alpha_id, max_times=3):    retry_count = 0    while retry_count < max_times:        try:            self_corr_df = get_prod_corr(session, alpha_id)            if not self_corr_df.empty:                return self_corr_df        except json.JSONDecodeError:            pass        retry_count += 1        time.sleep(60)  Wait for 60 second before the next retry        print(retry_count)    return pd.DataFrame(columns=["correlation"])》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】最全Product Correlation攻略理解PC与顾问收入的密切关系置顶的.md
- **评论时间**: 5个月前

感谢大佬的分享，不仅解读了PC跟收入的关系，还给出了降低PC的实操方案，很受用。

现在还只能把PC艰难的控制在0.7以下，希望能早日把它再降一档。

---

### 探讨 #20: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月7日，我的量化日记第七季打卡第一天

IND区有主题，真是太卷了，好多看着很漂亮的因子，都是高PC

---

### 探讨 #21: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月8日，我的量化日记第七季打卡第二天

继续IND区。马上限回测数了，工作流优化中，加油！

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月9日，我的量化日记第七季打卡第三天

IND区卷不动了，转战GLB，加油！

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月10日，我的量化日记第七季打卡第四天

GLB的回测是真慢啊，一天跑不满1万

---

### 探讨 #24: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月11日，我的量化日记第七季打卡第五天

GLB这个回测真是一言难尽。今天竟然搞出个PC1.0的，哭笑不得

---

### 探讨 #25: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月11日，我的量化日记第七季打卡第六天

暴力回测的路不好走了，得泡论坛学习大佬们分享的AI经验

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月13日，我的量化日记第七季打卡第七天

翻垃圾桶的一天，差点断粮

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月14日，我的量化日记第七季打卡第八天

数据集吃不透真是要走很多弯路！

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月15日，我的量化日记第七季打卡第九天

回测数是又降了吗？降到7500了？

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025年12月15日，我的量化日记第七季打卡第九天

试了试用AI优化因子，结果不太理想，还要好好研究

---

### 探讨 #30: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月20日 我的量化日记第九季 第一天久违的日记终于回来了。最近AI相关又开始井喷了，试了试Skill，AI好像比之前聪明了一点。

---

### 探讨 #31: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月21日 我的量化日记第九季 第二天平台更新了IS，想翻垃圾桶得再重新跑一遍了，炸裂……

---

### 探讨 #32: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月22日 我的量化日记第九季 第三天现在的PPA主题，给的GLB的几个数据集是真难搞……

---

### 探讨 #33: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月23日 我的量化日记第九季 第四天GLB这个回测速度，5000回测跑不完，火力全开也跑不完

---

### 探讨 #34: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月24日 我的量化日记第九季 第五天GLB的Returns好低啊，每天交1个吃低保

---

### 探讨 #35: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 5个月前

2026年1月25日 我的量化日记第九季 第六天是免费的大模型不给力，还是我使用的方法不对？AI总是编的头头是道，但结果并不好。

---

### 探讨 #36: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月26日 我的量化日记第九季 第七天GLB地区news20这个数据集真难跑，想趁着PPA主题点塔都费劲

---

### 探讨 #37: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月27日 我的量化日记第九季 第八天GLB地区的PPA主题实在跑不动了，不知道下次PPA会是哪个区

---

### 探讨 #38: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月28日 我的量化日记第九季 第九天AI比赛还没有参加，不知道从哪下手，希望晚上的会议能有所启发

---

### 探讨 #39: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月29日 我的量化日记第九季 第十天参加了AI比赛的培训会，有了点头绪，感恩老师的讲解

---

### 探讨 #40: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月30日 我的量化日记第九季 第十一天GLB地区的PPA主题活动马上结束，才点了3个塔，难受。不知道下一期的主题会是哪个地区。

---

### 探讨 #41: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年1月31日 我的量化日记第九季 第十二天新的PPA主题竟然又是GLB地区的，好消息是这次不限某几个数据集了？坏消息是universe限定为TOPDIV3000了。

---

### 探讨 #42: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年2月1日 我的量化日记第九季 第十三天workday账单出来了，马上要见钱了，蚊子腿再细也是肉，不容易

---

### 探讨 #43: 关于《【日常生活贴】我的量化日记第九季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXJr4tYCI6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzc3OTY0Nzk2NDExMTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTQlQjklOUQlRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQo6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--21fe46df9c3e1d7cbc3ae937add8b9d59d109ca8
- **评论时间**: 4个月前

2026年2月2日 我的量化日记第九季 第十四天这次的PPA主题限定GLB地区的universe为TOPDIV3000，好像比之前限定数据集稍微简单点，希望能多点几个塔

---

### 探讨 #44: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月20日 我的量化日记第九季 第一天

久违的日记终于回来了。最近AI相关又开始井喷了，试了试Skill，AI好像比之前聪明了一点。

---

### 探讨 #45: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月21日 我的量化日记第九季 第二天

平台更新了IS，想翻垃圾桶得再重新跑一遍了，炸裂……

---

### 探讨 #46: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月22日 我的量化日记第九季 第三天

现在的PPA主题，给的GLB的几个数据集是真难搞……

---

### 探讨 #47: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月23日 我的量化日记第九季 第四天

GLB这个回测速度，5000回测跑不完，火力全开也跑不完

---

### 探讨 #48: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月24日 我的量化日记第九季 第五天

GLB的Returns好低啊，每天交1个吃低保

---

### 探讨 #49: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月25日 我的量化日记第九季 第六天

是免费的大模型不给力，还是我使用的方法不对？AI总是编的头头是道，但结果并不好。

---

### 探讨 #50: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

2026年1月26日 我的量化日记第九季 第七天

GLB地区news20这个数据集真难跑，想趁着PPA主题点塔都费劲

---

### 探讨 #51: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年1月27日 我的量化日记第九季 第八天

GLB地区的PPA主题实在跑不动了，不知道下次PPA会是哪个区

---

### 探讨 #52: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年1月28日 我的量化日记第九季 第九天

AI比赛还没有参加，不知道从哪下手，希望晚上的会议能有所启发

---

### 探讨 #53: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年1月29日 我的量化日记第九季 第十天

参加了AI比赛的培训会，有了点头绪，感恩老师的讲解

---

### 探讨 #54: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年1月30日 我的量化日记第九季 第十一天

GLB地区的PPA主题活动马上结束，才点了3个塔，难受。不知道下一期的主题会是哪个地区。

---

### 探讨 #55: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年1月31日 我的量化日记第九季 第十二天

新的PPA主题竟然又是GLB地区的，好消息是这次不限某几个数据集了？坏消息是universe限定为TOPDIV3000了。

---

### 探讨 #56: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年2月1日 我的量化日记第九季 第十三天

workday账单出来了，马上要见钱了，蚊子腿再细也是肉，不容易

---

### 探讨 #57: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 4个月前

2026年2月2日 我的量化日记第九季 第十四天

这次的PPA主题限定GLB地区的universe为TOPDIV3000，好像比之前限定数据集稍微简单点，希望能多点几个塔

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月122日，我的量化日记第八季打卡第1天

终于又有日记可写了，论坛是真热闹，学不过来，完全学不过来。

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月23日，我的量化日记第八季打卡第2天

AI相关井喷式的爆发了，5000回测不会AI真可能被淘汰

---

### 探讨 #60: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月24日，我的量化日记第八季打卡第3天

今天开始EUR。5000回测不耐用啊。。。

---

### 探讨 #61: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月25日，我的量化日记第八季打卡第4天

参加了主题会，感谢老师的付出与分享

---

### 探讨 #62: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月26日，我的量化日记第八季打卡第5天

各种AI工具只是提高研究效率，不能无中生有。加油！

---

### 探讨 #63: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025年12月27日，我的量化日记第八季打卡第6天

让心流用MCP读取指定数据集的数据字段，它竟然只能读50个……

---

### 探讨 #64: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

我的量化日记第十一季 3月19日第一天

终于又开日记了，前两季都满的好快。。。最近渗透分频繁谷底，难受

---

### 探讨 #65: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

我的量化日记第十一季 3月20日第二天

最近在点JPN地区的塔，想着用FAST中性化，多少能出点PPA，出是出了，指标有点难看……

---

### 探讨 #66: 关于《Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100% sys.setrecursionlimit(α∞) PnL = ∑(Robustness * Creativity) #无限探索、鲁棒性优先，创新性增值 #Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

我的量化日记第十一季 3月21日第三天

渗透分连续三次更新在0.3左右徘徊，得调整调整了，不然这日base没眼看

---

### 探讨 #67: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月3日 第一天久违的日记终于又来了。没出正月还是年，给大家拜个晚年，祝大家VF高高，收入多多。

---

### 探讨 #68: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月4日 第二天最近一直在跟着PPA主题走，EUR-D1-TOPCS1600点了几个塔，现在有个很闹心的问题，这个宇宙的提交太慢了，半小时起步

---

### 探讨 #69: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月5日 第三天继续死磕EUR主题，现在的base受渗透分的影响挺大的。还没摸索出稳定打分的思路，继续努力。

---

### 探讨 #70: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月6日 第四天最近在用TRAE进行一些优化工作，水平忽高忽低，有时候真会让人血压飙升

---

### 探讨 #71: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月7日 第五天参加了AI工具助您研究顺利的培训，cnhkmcp竟然又又又更新了，要进入一键生成可提交的Alpha的时代了？

---

### 探讨 #72: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月8日 第六天试用了下最新版的cnhkmcp中的Alpha自动流水线功能，随变调了个数据集，结果并不很理想，得再琢磨琢磨

---

### 探讨 #73: 关于《【日常生活贴】我的量化日记第十季》的评论回复
- **帖子链接**: https://support.worldquantbrain.com/hc/zh-cn/search/click?data=BAh7DjoHaWRsKwgXe%2B6IQiM6D2FjY291bnRfaWRpA9GrqjoJdHlwZUkiE2NvbW11bml0eV9wb3N0BjoGRVQ6CHVybEkiAcxodHRwczovL3N1cHBvcnQud29ybGRxdWFudGJyYWluLmNvbS9oYy96aC1jbi9jb21tdW5pdHkvcG9zdHMvMzg3Njg2NzIxNDQxNTEtLSVFNiU5NyVBNSVFNSVCOCVCOCVFNyU5NCU5RiVFNiVCNCVCQiVFOCVCNCVCNC0lRTYlODglOTElRTclOUElODQlRTklODclOEYlRTUlOEMlOTYlRTYlOTclQTUlRTglQUUlQjAlRTclQUMlQUMlRTUlOEQlODElRTUlQUQlQTMGOwhUOg5zZWFyY2hfaWRJIilhNjJiNGY5Mi1mYTVmLTQyNGYtOTExOS1mOTYxOTY2YWMzZDEGOwhGOglyYW5raQw6C2xvY2FsZUkiCnpoLWNuBjsIVDoKcXVlcnlJIgxRTDQ3MzcyBjsIVDoScmVzdWx0c19jb3VudGkO--d47142f2e4b4119fddb358d602a4c087c6c98fc7
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月9日 第七天这次Osmosis刷新总算是往上走了点，周一的刷一次管三天，太重要了。Combined Performance也快刷了吧，希望能有个好结果。

---

### 探讨 #74: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月3日 第一天

久违的日记终于又来了。没出正月还是年，给大家拜个晚年，祝大家VF高高，收入多多。

---

### 探讨 #75: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月4日 第二天

最近一直在跟着PPA主题走，EUR-D1-TOPCS1600点了几个塔，现在有个很闹心的问题，这个宇宙的提交太慢了，半小时起步

---

### 探讨 #76: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

我的量化日记第十季 2026年3月5日 第三天

继续死磕EUR主题，现在的base受渗透分的影响挺大的。还没摸索出稳定打分的思路，继续努力。

---

### 探讨 #77: 关于《利用Gemini从0到1手搓IND区alpha尝试经验分享》的评论回复
- **帖子链接**: [Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享.md
- **评论时间**: 6个月前

感谢分享。IND区开活动了，学习下

---

### 探讨 #78: 关于《利用Gemini从0到1手搓IND区alpha尝试经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 利用Gemini从0到1手搓IND区alpha尝试经验分享_36444272754711.md
- **评论时间**: 6个月前

感谢分享。IND区开活动了，学习下

---
