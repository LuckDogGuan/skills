# 顾问 worldquant brain赛博游戏王 技术答疑与对话录 (Technical Conversations)

> 本文档为顾问 worldquant brain赛博游戏王 参与论坛技术讨论的对话上下文，以 Q&A 问答形式展现其指导思路。已进行脱敏与图片 OCR 解析。

### 技术对话片段 1 (原帖: Selection Expression 部分)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 2024 super alpha比赛心得经验分享_32341036686231.md
- **时间**: 1年前

**提问/主帖背景 (QH29412)**:
### surperAlpha比赛在2024年的可使用范围是USA，ASI，EUR


> [!NOTE] [图片 OCR 识别内容]
> REGION
> DELAY
> SELECTION HANDLING
> REGION
> DELAY
> REGION
> DELAY
> USA
> Non Zero
> EUR
> ASI
> Combo settings
> Combo settings
> Combo settings
> UNIVERSE
> NEUTRALIZATION
> UNIVERSE
> TOP3000
> SIOw Factors
> TOP1200
> UNIVERSE
> TOP3000
> PASTEURIZATION
> TOP1OOO
> TOP1200
> MINVOLIM
> On
> TOPSOO
> TOP8OO
> MINVOLIM
> TOP200
> TOP4O0
> ILLIQUID_MINVOLIM
> ILLIQUID_MINVOLIM
> ILLIQUID_MINVOLTM


对同一个数据集，可以选择在各个universe上面创建super alpha。

个人经历：这篇是去年参加比赛的心得，略微修改。去年成为正式顾问后一个多月就参加这个SA的比赛，比赛结束后权限就收回了。我靠自己的努力终于在去年圣诞节获得了属于自己的SA权限，总来的说经验还要靠比赛来提升吧。

# Selection Expression 部分

**Alpha Properties**  **选择**

1. 一般选择turnover < 0.30，对ASI区域，建议使用更小的turnover，在使用 [Risk Neutralized Alphas]([链接已屏蔽]) 时会拉高整体的turnover。

a,  筛选alpha 观察整体turnover < 0.10时，建议使用“Slow Factors”设置，效果更佳。

b,  筛选alpha 观察整体turnover > 0.20时,  建议使用“Fast Factors”设置，效果更佳。

1. 一般选择prod_correlation< 0.6，可以选出idea比较新的alpha，最后的prod-corr 也会较好。

3.  平时跑过的数据集，多留意它的特点。有的DS可能sharp优秀，margin一般；有的DS是margin 很好，但turnover很高。可以把他们放在一起做一个增强，可以通过 category 或者DS in(datasets, "fundamental6") 来选取你的alpha 组合。

**SuperAlpha selection features**  **选择-Auther information**

1. 一般设置 author_returns_to_drawdown>2,官方建议是author_returns_to_drawdown > 1 && author_returns_to_drawdown < 4。可以根据不是数据集的alpha情况调整，这个参数有时可有可无，但有时至关重要。
2. Author Fitness or Author Sharpe 效果类似，一般设置author_fitness >= 2 or author_sharpe >= 2 ,个人比价倾向于fitness，具有很强的综合性且一般不容易通过算法调整，能够体现author的综合素质。但是，不同的数据集下面的alpha的特性不同，为了满足能select 出足够多的alpha，具体参数适当调整。
3. 我大部分是基于 Selection Handling = "Non-Zero"创建的super alpha。

## 🌰例子： 
> [!NOTE] [图片 OCR 识别内容]
> Code
> Selection Expression
> 1
> (0.30-turnover)*
> (in(tags,
> "PowerPoolSelected" )
> && universe
> 
> IT0P1000" )
> Combo Expression
> 1
> combo_a(alpha, nlength
> 250
> mode
> 'a1902')


## Combo Expression 部分

USA建议时间窗口选择：250，500；ASI建议时间窗口选择：60，120，250.

stats = generate_stats(alpha); ts_mean(stats.returns, 500)；

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的分享，点赞！！！

这边有一个小小的问题需要讨论：prodcor小于0.6，或者小于0.5，是可以选到cor低的因子的，但如果大家都放了这个设置，意味着大家都在相同的因子上做组合，这个是不是又背离初衷了呢？

==============================================

“我的回合，抽卡！“——《游戏王》

==============================================


---

### 技术对话片段 2 (原帖: 2024Q4关于genius项目结果分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 2024Q4关于genius项目结果分享_30031129438871.md
- **时间**: 1年前

**提问/主帖背景 (JL16510)**:

> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2024-04, October 1st 2024 - December 31st, 2024
> Gold
> Expert
> Master
> Grandmaster
> Signals
> 193
> 27 more to Grandmaster
> 120
> 220
> Pyramids Completed
> 33
> 27 more to Grandmaster
> Combined Alpha Performance
> 3.15
> Reached Grandmaster
> 0.5



> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2024-04, October 1st, 2024 -
> December 31st 2024
> Operators per Alpha
> Operators used
> Fields per Alpha
> Fields used
> Community activity
> 11.2
> 68
> 4.04
> 170
> Completed referrals
> Simulation activity
> Submission activity
> Oct
> NOV
> Dec
> Oct
> NoV
> Dec
> Max simulation streak
> 99



> [!NOTE] [图片 OCR 识别内容]
> Shanghai new consultant training and meet ups
> 10/09/2024
> USS145.00
> 202404 Payment
> 02/14/2025
> US5170.85
> 09/10/2024
> Total
> 055315.85
> 02/15/2025


目前等级还是gold，虽然因子最看重的应该是其质量，但genius项目算综合指标，其他指标也同样重要。如果想获得更高等级，其他指标也要同时提升。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
per op稍微有点高，如果把activity刷一下估计能到expert，很厉害


---

### 技术对话片段 3 (原帖: 计算置信度)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Alpha PNL 合法性检测【自动剔除 厂 Alpha等无效Alpha实现高效率剪枝】代码优化_32761924007703.md
- **时间**: 1年前

**提问/主帖背景 (JR23144)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的代码，点赞！！！

解决了 厂一直筛不掉的问题，可惜我的服务器太垃圾，跑点大的代码就报错。

这里也提供一个优化思路：检测到厂，把它隐藏，这样就不会再出现，再筛选了


---

### 技术对话片段 4 (原帖: 市值中性化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] ATOM模板分享_32988918972183.md
- **时间**: 1年前

**提问/主帖背景 (MY49971)**:
模板如下:

```
"ts_mean({DATA},d1)/ts_mean({DATA},d2)"
```

其中d1,d2可以取值是(5,60)或者(20,120),这是一个基于长短期均值比例的交易策略，目前在USA、EUR区域内测试发现了一些信号,然后结合ts和group等操作符就可以跑出可以提交的alpha了。量化小白，抛砖引玉，还请大佬们多多指教！！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享，已经用上了。感觉可以再套一层group优化，后续会试一试，如果效果好的话会分享！！！

========================================================================================================================================================================


---

### 技术对话片段 5 (原帖: Congratulations to our Global ATOM winners!)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Congratulations to our Global ATOM winners_28386256322967.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:

> [!NOTE] [图片 OCR 识别内容]
> NTOM
> 2024
> TOP 10 WINNERS
> 1st
> 器
> Yuqi Liu
> 2nd
> Thanh Nguyen
> Sra
> Ritesh Palawat
> 4th
> Dat Nguyen
> Sth
> Wenqian Dai
> Lingyu Zhang
> Ajay Bagul
> SaadKhan
> Leich Mugoh
> 1Oth
> Kuan Hung Kuo
> CONGRATULATIONS!
> ERAN


**顾问 worldquant brain赛博游戏王 的解答与建议**:
Congratulation to all winners! and thanks brain workers for their hard work, as well as all consultants engaged!


---

### 技术对话片段 6 (原帖: Dataset Deepdives - News87 (Smart Conference call transcript data)被推荐的Research)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Dataset Deepdives - News87 Smart Conference call transcript data被推荐的Research_28234460258327.md
- **时间**: 1年前

**提问/主帖背景 (AC28031)**:
Conference calls, also known as analyst/earnings calls, are significant events for public companies and investors to discuss in detail the firm’s fiscal quarter, as well as projected financial performance and future business insights. Thus, these events may contain impactful information related to the firm’s stock price such as new information, sentiment, surprise, reaction, etc.

This article will discuss potentially unique Alphas using "News87" dataset named “Smart Conference Call Transcript Data” for Global region.

**Dataset Highlight**

- The "News87" dataset is classified under the Analyst category > Analyst Estimate subcategory.
- Data Type: VECTOR type only
- Regions: USA D-1 & D-0. GLB D-1
- At the time of writing, "News87" is quite under-explored by the consultant community in GLB region compared to Analyst category in general (table below). This makes "News87" potential source for creating low-correlation Alphas. Info on GLB Alphas in the dataset at the time of publishing:


> [!NOTE] [图片 OCR 识别内容]
> Dataset
> Users
> Alphas
> Fields
> Alphaluser
> Alphalfield
> GLB
> 39% coverage
> Value Score 5
> Neis87
> 44
> 138
> 201
> Analyst category (Average)
> 430
> 157


- The ideas discussed below can be used to create Alphas in both USA and GLB Regions. It is encouraged for consultants to submit Alphas especially in GLB Region for this dataset.

**Dataset Feature**

1. **Low frequency, low coverage.**  Conference calls aren't mandatory, but most public companies hold them, usually within one month after the completion of the quarter, following the quarterly earnings announcement. Thus, a quarterly frequency is typically observed, and at least a 63-day backfill is recommended.
2. **Participants and Sections concepts.** Given the conference calls' nature in business presentations & discussions, there are various objects regarding the call participants and presentation sections that are seen across the "News87" dataset.
3. **Structured into three statistical groups: Basic Stats, Readability Score, and Sentiment Score.**  These metrics are extracted from calls that are recorded and broadcasted live on the internet. Vendors transcribe the calls into written text for investors to consume, and advanced measurement such as NLP algorithm are applied to derive various statistics.

1. Basic Stats:General basic count and its derived values of information including:

*Ex: "mws87_numvswordsratioceoqa" is the Number of numerical words divided by number of all words spoken by CEO in Q&A*

1. Readability Score:There are many numeric test indices, calculated from the number of characters, words, sentences, etc... from textual transcript, indicating linguistic complexity across Participants and Sections. The values of these data ranging from 0 to 100 and specific test indices provided by "News87 dataset are listed below:

*Ex: "mws87_oper_fre_qa" is The Flesch Reading Ease score of the operator in Q&A*

1. Sentiment Score:for various Participants under different Sections.

*Ex: "mws87_corppart_sent_score_qa: is The sentiment score of corporate participants in Q&A*

**Usage Advice**

1. Check coverage, as different fields within the dataset may vary given their economic implications. For example, analysts may seldom talk, or the CEO not attending the meeting may lead to lower coverage for certain fields.
2. It is always advisable to use ts_backfill() operator for all datafields in this dataset. Backfilling at least one or two quarters and removing outliers by winsorize, truncating, etc.., especially for sentiment data, are recommended.
3. Time series operators may be useful given the different base value of sentiment of different markets, companies and individuals.
4. Earnings conference data can serve as a long-term signal, similar to fundamental data as its contain sentiment, reaction, etc.. factors derived from latest business and financial discussion information.
5. Try applying this to different universes in the GLB region to achieve low correlation and maximize value scores.

- **Sample Alpha Ideas**

1. Tone and Sentiment: Conference call linguistic tone of the dialogue between management and analysts may predict abnormal returns. The below can be starting points:

See Papers:  [Earnings conference calls and stock returns: The incremental informativeness of textual tone]([链接已屏蔽])

1. Financial reporting readability: Consistent and low financial report readability impeding the efficient and accurate assimilation of information into stock prices, less understandable reporting are associated with greater equity mispricing and momentum effect.

See Papers:  [Annual report readability and equity mispricing]([链接已屏蔽])

**Alpha Performance and Correlation** Below is the performance of a Single Dataset Alpha idea implemented on this dataset in the GLB Region. 
High Margin with Low production correlation is easily achievable if one creates Alphas using this dataset.
 
> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> Awerage
> Single Data Set Alpha
> Dyramid theme: GLBIDIIAnalyst *1.5
> Aggregate Data
> 31aroE
> UPICNe|
> FiznEss
> ECUTI
> UTaWOUF
> Warain
> 1.89
> 3.27%
> 1.07
> 4.0196
> 2.8296
> 24.549000
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Frness
> REIICn
> Oraroin
> Warain
> 1.58
> 3.2796
> 0.58
> 1.699
> 1.649
> 10.359600
>  Correlation
> Self Correlation
> Natirum
> Ninimum
> Last Run:
> Prod
> [sTIIT
> [inimUT
> Lt RMn:
> 12/03120245-09
> Correlation
> 0.3881
> -0.2380
> TU


**Call for Action**

*Comment below if you found this post helpful and were able to submit at least one Alpha using this dataset* .

Feel free to ask any questions in case of any doubts! We also look forward to hearing if you would like similar notes on other datasets.

**顾问 worldquant brain赛博游戏王 的解答与建议**:
excellent work, which makes me understand a new datacategory, upvoted!


---

### 技术对话片段 7 (原帖: Genius Rank Analysis by 20250625)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Genius Rank Analysis by 20250625_33040481988375.md
- **时间**: 1年前

**提问/主帖背景 (YX23928)**:
2025-06-25T11:48:10.663Z
总人数: 6028 人
可能的基准人数: 2102 人（交够40个）
各个Level 满足的人数 / 最终的人数:
• For Expert: 1034 / 420
• For Master: 442 / 168
• For Grandmaster: 60 / 42

========================================================================

**顾问 worldquant brain赛博游戏王 的解答与建议**:
紧张

2025-06-25T11:48:10.663Z
总人数: 6028 人
可能的基准人数: 2102 人（交够40个）
各个Level 满足的人数 / 最终的人数:
• For Expert: 1034 / 420
• For Master: 442 / 168
• For Grandmaster: 60 / 42

========================================================================


---

### 技术对话片段 8 (原帖: GLB的SA讨论)
- **原帖链接**: https://support.worldquantbrain.com[Commented] GLB的SA讨论_32984760419351.md
- **时间**: 1年前

**提问/主帖背景 (XX42289)**:
救命！做GLB的SA研究卡壳了😫 翻遍数据都找不到靠谱的global super alpha因子，感觉陷入死胡同！有没有比较好的combo code？或者有超牛的select筛选思路？在线等超实用经验分享，一起打破僵局💪！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
蹲，glb的sa感觉质量组合出来普遍不如ra，感觉应该是大universe不适合刻意去压低turn的原因 也很苦恼

生活就像海洋，只有意志坚强的人才能到达彼岸


---

### 技术对话片段 9 (原帖: IQC 研究小组双周分享-高分策略经验)
- **原帖链接**: https://support.worldquantbrain.com[Commented] IQC 研究小组双周分享-高分策略经验_32123298592663.md
- **时间**: 1年前

**提问/主帖背景 (OL33779)**:
## 1.增加数量--将手动微调框架化

### 1.1 分析过程

IQC的几个test：

1. sharpe >=1.25
2. fitness >= 1
3. Sub-sharpe >= 0.75 * sqrt(subuniverse_size / alpha_universe_size) *sharpe
4. Weight <= 0.1
5. turnover ~(0.01,0.7)
6. 自相关

对已经simulate的alpha，可以去看上面几个错误的分布，再综合发生频率与难度，来设计自动化的通用的框架。从全部的回测来看，大部分的FAIL会发生在sharpe、fitness，那么对于满足一定sharpe、fitness的alpha，剩余的几种test发生频率如何？我将用一个小样本说明：


> [!NOTE] [图片 OCR 识别内容]
> LOI_SHARPE
> LOII_FITNESS
> LOI_TURNOVER
> HIGH_TURNOVER
> CONCENTRATED
> IEIGHT
> LOI_SUB_UNIVERSE_SHARPE
> HATCHES_COHPETITION
> PASS
> 144
> 144
> 141
> 111
> 144
> FAIL


FAIL频率：concentrated-weight>sub-sharpe>turnover 。在⼿动微调的时候是如何解决这些难点的？将不能提交的alpha转换为满⾜要求的alpha.

1.2 框架与部分设计
a. 解决concentrated-weight
weight的本质是某个节点的股票权重过⾼不够分散，也就是有最终信号的样本不⾜（信号data不⾜ or 股票数值过⼤），导致股票的权重过⾼。我的解决⽅案如下（三步法）：
i. 将 settings.truncation 调⼩为0.01。（抑制极端权重，拉平信号分布，没有股票能“独
吃”过⾼权重）
ii. 对 regular 字符串中的 winsorize 调⽤做处理：根据基础变量的 coverage 值，移除
winsorize包装或修改其 std 参数，可能⽣成多个变体。
分析：⼤家通⽤的模版都是对数据加上ts_backfill和winsorize追求稳健性，对于winsorize，哪些数据在加了缩尾后容易出现数据不⾜？我认为是coverage（dataset表单的⼀个特征）不⾜的data。因此对coverage<0.6的基础变量data直接移除 winsorize ，对于coverage⼤于0.6的，提⾼std的参数值以包括更多的样本。当然这是我思考的标准，也可以采⽤其他标准，像上节课⽼师提到的close可能本⾝不适合⽤winsorize。
iii. 对整个 regular 字符串中未被 ts_backfill 包裹的基础变量做包装。（直接解决数据不⾜的问题）
▪ 衍⽣问题（"⼚"字形的alpha怎么排除）：1.最好的⽅法是PnL每年的longcount和
shortcount都不为零 2.我的近似处理是longcount和shortcount⼤于100，因为is的区间为
201801~202301，⽽alpha⻚⾯的longcount和shortcount的值是18~22年（前五年）的平
均值，每年平均⼤于100对于我常设定的truncation=0.01来说是可以接受的。
b. 解决sub-sharpe
待分享
c. 解决turnover&提⾼sharpe、fitness、margin
⽅案：摇摆decay*neut
分享⼀个decay*neut能提⾼sharpe、fitness的案例：对于最难解决的sharpe和fitness，我们
可以⽤double sorting来分别看解决⽅案.⽐如说图中的案例part，对于sharpe>1.4（⽐1.25的标准更⼤，容错⾜够）但fitness~（0.9，1）的alpha，我们可以通过调整decay来降频从⽽使得fitness满⾜要求，因为Fitness = Sharpe * Sqrt( Abs( Returns ) / Max( Turnover, 0.125 ) ) ，要么提⾼夏普要么降低turnover，⽽夏普不好提⾼，就只能降频了，decay不⼤时是有可能提⾼sharpe的（过滤低频波动），⽽对于sharpe>1.4的alpha，我们也可以接受牺牲部分的sharpe来提⾼fitness。 
> [!NOTE] [图片 OCR 识别内容]
> fitness Isharpe
> 1.15
> 1.25
> 14
> 0.9
> 案例part
> 01标准
> 1.3
> 00标谁
 
在经过数个模块的分析后，我抛弃了分区解决的思路，⽽是化繁为简，只要sharpe>=1.15&fitness>=0.9&上述其他条件，就统⼀摇摆去寻找最优解（正如第⼆次会议中grand master提到了对可以提交的alpha，也可以加decay*neut来提⾼margin）

**每一次筛选都是为了解决一个特定的test，所以三个阶段的条件越来越严格** ，阈值的设置就是经验--什么程度的alpha值得微调？好调和不好调的点在哪里？


> [!NOTE] [图片 OCR 识别内容]
> 三筛
> 筛
> (weight~[0.1,0.1
> 初筛
> 批量产出所有
> simulate
> sub-sharpe-
> 5]+pass) & sub-
> weight~[0.1,0.4]
> 可能的alpha
> diff~(0.01,0.1)
> sharpe-
> diff<-0.05


追求的效果是每一步都能解决一个问题，比如通过优化1.2之后就能增加参与优化3的样本数，然后再进行统一的处理。

较强的拓展性：成为正式顾问后，只需要在优化3之前添加几个新的test调整手段；当然也可以在三之后加上一些自动检验鲁棒性的方法。

## 2.提高质量与效率--从阻力最小的路径出发

### 2.1 阻力最小--低自相关&高分散性

截止写稿，alpha单个均分1480。从第十个alpha后有意控制单个alpha的加分幅度为1300~2500。（下图展示所有控分的alpha，从上到下-->提交从先到后）

**这些alpha最重要的几个特征**

**（1）自相关低于0.3**

**（2）数据集分散且平均** （基本面和量价较多是因为数据本来维度就更多，且有些操作符例如group也会增加这两个种类的分布；整体产出比例也符合dataset的alpha产出比）

**（3）longcount和shortcount都偏小，可能都是对小样本的特殊行情进行了**  **拟合**  **，因此也保证了低相关**

**（4）更稳健的表现，比如说每年的正收益&夏普，更高的sub-sharpe，decay*neut效果也不会大幅下降**

**Q：（3）+（4）的衍生问题：偏小的count+较高的sub表现等价于更换universe吗？**

**A：不是，count更多由低coverage决定**

（5）alpha的加分会随着submit的增加⽽改变（⾃相关和对Pnl分布的影响也发⽣变化）， **但加分多的alpha往往会出⾃本⾝底⼦就不错的pool** 。因此在遍历分数时，也可以优先测试这些本来分数就⾼的alpha，⽐如我现在有10000个PASS的alpha需要测试，我就只会选择⼤于-1000的来跑（通常来说也就⼏百个）。这部分的⾃动化框架是检索是否有submit，如果没有就只计算新增的，如果有就把⼤于0&⾃相关低的全部过⼀遍，设置定时任务每六个⼩时跑⼀次。【有时间的话可以全部遍历score】

### 2.2 阻力最小路径的几个案例（operator+data+框架）

1. （operator）在提供的三阶段模版中，可以概括为以下几个步骤：
   1. 预处理：用winsorize+ts_backfill包装数据，matrix+用vec运算符包装的vector
   2. 第一阶：套上ts运算符，参数取不同的days，shuffle后simulate
   3. 第二阶：获取满足一定标准的alpha，剪枝，套上group_ops，参数选不同的group
   4. 第三阶：获取满足一定标准的alpha，剪枝，套上trade_when，参数选不同的entry_event和exit_event

那么，为什么ts后要进行第二阶group？我的理解是第一阶体现时序上的变化规律，即股票自身的强度；而第二阶就是截面（也是计量经济学中资产定价的核心），最核心的是套上group的经济学含义是体现 **组间差距** ，这和一阶的值本身相比， **能够产出差别较大的值** ，这就是逻辑上的朝着低自相关的路径前进。（这也是在第二次会议中分享的相关性剪枝是会比其他剪枝更有效的原因）

**经济含义是可以赋予的，但朝着低相关发散是客观的** 。

1. (data) 在price volume dataset中的relationship Data for Equity中的grouping fields, 三阶段代码中会罗列出某些地区或universe好用的现成的分类标准，其实也可以用LLMs结合description和命名规则来给这些field分类， **把相似的分到一组** ，那么每次使用时只需要每组选一个来simulate，如果效果好再替换为该组其他的field来选最优，也就产生了一个优化效率&高阶提高质量的思路。

1. (框架) 以负向的alpha为例，在几个test中会产生负号的有sharpe、fitness、subsharpe，那么对于负的alpha群，统一的转换思路就是加负号（根据有无分号区分两种情况）。但是并不是所有的alpha在转换后都值得simulate， **比如对weight而言，转换方向后并不会改变weight的情况，FAIL的不会PASS** 。因此在1的框架中，我们对于负alpha也是分test来解决，最后只对筛选后的alpha做simulate来加快效率
2. tips1:在二次开发时筛选条件就不要写死，比如说嵌套一个abs去包括正负两种情况，减少代码的重复
   tips2:对于负向的alpha，判断相关性时也要加个负号：max_corr = corrs.max()-->(-corrs).max()。分析逻辑是根据sharpe的计算公式和markowitz的结论， **负相关因子几乎总能提升夏普** ，只要 μ₂>0。所以对于正向alpha，计算最大的正相关系数即可；而对于负向alpha，regular变向后等同于对pnl变向，所以对corr矩阵加个负号再取最大。

## 3.感悟与os警示

1.所有的决策都有数据支撑，解决特定的问题

2.只要设计到筛选，都可以用自相关和高阶拓展来大幅提高效率。一开始是枚举法，但无效枚举远大于有效产出，所以后期一定是结合先验经验做减法先小样本试错，再筛选、拓展为一二三阶去处理（比如一开始就decay*neut*days，和用1.2的框架，效率差十倍都有可能；然后对每一批simulate也要不断观察反馈，比如相对加分多的都没有sector中性化，那就直接放弃，效率提高25%）

3.爬虫思维--可见即所得，从最原始的数据出发，官网提供的每个字段都是有意义的，而不是只使用加工好的代码，一开始就使用完整的代码会约束思考和迭代的过程，自动化也应该是逐步实现的。比如一开始数据不多时用get_alphas就足够，当api筛选完超过1W且查询速度太慢时，再考虑把历史筛选过的alpha本地保存&入库

4.上面的分析都是基于is分数推导出的高分alpha的特征，os表现确实要更注意（结合base payment，kunqi老师说的经济学含义等等）；赛段二做更多的尝试，即使is扣分、风格不一致，也可能是好的提升

5.上面实现的低相关，在理论上是追求不同行情下可以叠加的CTA策略

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的一篇文章，读一读还是会有所收获，点赞。

低自相关的因子可以产生高鲁棒性的投资组合，这也是中国区众多研究顾问正在努力的目标。三阶模版与genius计划，与powerpool相违背，同时会产生一定程度的过拟合，许多顾问已经不再跑这一part了，这个可以进行修改（例如，针对确实值得二次优化的因子进行三阶操作，而不是123跑到底）。针对subsharpe的解决，个人理解为 ：如果一个因子是靠着大universe来获得收益，fail subsharpe的话，说明其是靠着低流动性标的挣钱。顾问有一根maxtrade线，可以根据maxtrade线与pnl的差异，判断是否有fail的风险，甚至可以在回测的时候打开maxtrade线，进行检测。

期待下一位国区GM的诞生。


---

### 技术对话片段 10 (原帖: Machine Learning for Stock Selection)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Machine Learning for Stock Selection_25238140293143.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Talks about general machine structures, and proposed solutions to overfitting.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Excellent paper,thank you for your post. I can find how is it related to the way I choose Alpha for submission.


---

### 技术对话片段 11 (原帖: Momentum in Prices and Volume of Trades)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Momentum in Prices and Volume of Trades_29301176116759.md
- **时间**: 1年前

**提问/主帖背景 (KS69567)**:
This study reveals a key relationship between  **past trading volume**  and both  **momentum**  and  **value**  strategies, highlighting its predictive power for future stock performance. Specifically, firms with high  **past turnover ratios**  (indicative of higher trading volume) tend to exhibit  **glamour**  characteristics, earn lower future returns, and experience more  **negative earnings surprises** . Conversely, firms with low turnover ratios align with  **value**  characteristics, earn higher future returns, and show more  **positive earnings surprises**  over the next eight quarters.

Furthermore, past trading volume is a strong predictor of both the  **magnitude**  and  **persistence**  of  **price momentum** . The study finds that  **momentum effects**  tend to reverse over a five-year horizon, with high-volume winners and low-volume losers experiencing  **faster reversals** .

The study’s findings provide several deeper insights into the relationship between  **past trading volume** ,  **momentum** , and  **value**  strategies, with implications for both asset pricing and investment strategies:

1. **Momentum and Value Strategies** : The study shows that  **high past trading volume**  correlates with stocks exhibiting  **glamour characteristics** , which tend to earn  **lower future returns** . On the other hand,  **low past trading volume**  is associated with stocks that have  **value characteristics** , which historically generate  **higher future returns** . This suggests that investors who focus on high-volume stocks may be chasing recent price gains (glamour), while those focusing on low-volume stocks may be buying underappreciated or undervalued assets.
2. **Earnings Surprises** : The study also highlights that firms with  **high past trading volume**  tend to have  **more negative earnings surprises**  in the following quarters, while firms with  **low past trading volume**  tend to experience  **more positive earnings surprises** . This is important for forecasting earnings results, as  **momentum stocks**  are often priced with overly optimistic expectations, leading to negative earnings surprises, while  **value stocks**  may be underappreciated, leading to positive surprises.
3. **Price Momentum and Reversals** : The study shows that  **price momentum**  effects (where stocks continue to move in the same direction) tend to reverse over time, particularly within a  **five-year horizon** . Stocks with  **high volume**  that have been  **winners**  (rising prices) are likely to experience  **faster reversals** , while  **low-volume losers**  (declining stocks) also experience reversals. This insight challenges traditional momentum strategies and emphasizes that the persistence of price momentum is temporary, especially for stocks with extreme trading volumes.
4. **Intermediate-Horizon Underreaction and Long-Horizon Overreaction** : The findings effectively reconcile the  **underreaction**  and  **overreaction**  effects observed in asset pricing. At shorter horizons (e.g., intermediate-term), stocks with high trading volume may be subject to underreaction, where market prices fail to fully adjust to new information, creating opportunities for momentum. However, over longer horizons, the  **overreaction**  effect takes hold, where stocks that have experienced momentum begin to experience reversals as the market corrects itself, indicating  **market inefficiency** .

### Implications for Investment Strategies:

- **Trading Volume as a Signal** : Traders and investors can use past trading volume as a signal to gauge potential future returns and adjust their portfolios accordingly. High-volume stocks may indicate a  **momentum**  strategy, while low-volume stocks could align with a  **value**  strategy.
- **Timing of Momentum Strategies** : The study suggests that momentum strategies should be adjusted over time, with caution for longer-term holding periods.  **Faster reversals**  in high-volume winners and low-volume losers suggest that  **momentum strategies**  may need to be shortened in duration to avoid losses from price corrections.
- **Predictive Power for Earnings** : Past trading volume could be integrated into  **earnings prediction models** . High-volume stocks may have a higher probability of negative earnings surprises, while low-volume stocks may signal potential positive earnings surprises.
- **Enhancing Risk-Adjusted Returns** : By incorporating insights from past volume trends, investors can better manage risk and improve the risk-adjusted returns of their momentum and value strategies. Recognizing when momentum is likely to reverse or when value opportunities are undervalued based on volume trends can lead to more informed decision-making.

These findings underscore the importance of  **trading volume**  as a significant factor in understanding and predicting stock performance, and offer actionable insights for adjusting both  **momentum**  and  **value**  strategies to align with market dynamics and time horizons.

Overall, the findings suggest that  **past trading volume**  plays a critical role in explaining the dynamics between  **intermediate-horizon underreaction**  (where market prices fail to fully adjust to new information) and  **long-horizon overreaction**  (where prices correct due to overreaction to past trends). These insights help to reconcile and better understand the behavior of stocks over different time horizons, offering valuable implications for developing  **momentum and value-based strategies** .

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Excelllent post, upvoted

what's more, could you recommend some datafields(or some topic data) that can be used to momentum trading?

Due to limited data access, I can not find some useful data to try this idea, thanks.


---

### 技术对话片段 12 (原帖: NEWS 数据集如何做ATOM的alpha)
- **原帖链接**: https://support.worldquantbrain.com[Commented] NEWS 数据集如何做ATOM的alpha_33020085052823.md
- **时间**: 1年前

**提问/主帖背景 (MY49971)**:
最近再跑news相关数据集的一二阶模板，信号都很一般。请教各位大佬，对于此类数据集如何构建atom类alpha？ 之前看过一篇帖子中提到可以利用 “没有新闻就是好消息”这一思路来构建alpha，不知道具体如何实现

**顾问 worldquant brain赛博游戏王 的解答与建议**:
news按照一阶二阶是可以跑出因子的，这个我实践过

没有新闻就是好消息？可以按照vecsum取-rank，或者vecavg取最靠近0的（而不是最小），都可以尝试，供参考。=========================================================================================


---

### 技术对话片段 13 (原帖: ［PPAC］使用程序提交alpha之前，必需做的一件事经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPAC使用程序提交alpha之前必需做的一件事经验分享_30987517001495.md
- **时间**: 1年前

**提问/主帖背景 (LG37773)**:
## 一、背景：

近期开始了Power Pool Alphas Competition 2025的比赛，受到新老顾问的欢迎。特别是不进行Prod correlation的测试，很多以前不能提交的alpha也可以提交了。参加比赛还有其他的一些福利就不一一表述。

参加比赛时，提交alpha会有一个特别的动作需要完成，就是填写Alpha的description，而且需要按照指定的template进行填写。


> [!NOTE] [图片 OCR 识别内容]
> Description
> 113/100 character minimum
> Power Pool Alphas Competition 2025
> Use the template
> In order to submit this alpha, you have to add an alpha description
> following the given template。


具体template如下：
Idea: 
Rationale for data used: 
Rationale for operators used:

## 二、解决方案：

手动填写是个重复劳动的工作，既然在使用Python就让程序来完成吧。

在machine lib中，修改set_alpha_properties函数。添加参数regular_desc，不能使用自带的参数selection_desc。

将alpha的description通过这个参数，传进函数内进行更新。

为了看贴子的同学也有收获，直接分享代码。欢迎点赞留言。

```
def set_alpha_properties(    s,    alpha_id,    name: str = None,    color: str = None,    selection_desc: str = "None",    regular_desc: str = None,   #changed by new version    combo_desc: str = "None",    tags: str = ["ace_tag"],):    """    Function changes alpha's description parameters    """     params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": regular_desc},  # changed by new version        # "regular": {"description": None},        "combo": {"description": combo_desc},        "selection": {"description": selection_desc},    }    response = s.patch(        "[链接已屏蔽] + alpha_id, json=params    )
```

调用set_alpha_properties函数时，指定Description：

```
from machine_lib import *sess =login()alpha_id = 'XXXXX'  #<==== 替换成自己的alpha idPPAC_desc = '''Idea: This alpha for Power Pool Alphas Competition 2025Rationale for data used: The data utilized in this alpha is highly reliable.Rationale for operators used: The chosen operators are specifically selected for their suitability and effectiveness in executing the required operations.'''set_alpha_properties(sess, alpha_id=alpha_id,regular_desc=PPAC_desc)status_code = submit_alpha(sess, alpha_id)  #submit_alpha function has been defined. if status_code == 200:    print('alpha was successfully submitted')
```

这样就实现了自动提交alpha, 然后可以进一步优化，定时提交等等。

我们不断地扩展alpha machine的功能，更高效地完成工作。希望能够帮助到大家，欢迎大家在评论区留言。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢你的分享 和帖子，十分有用，点赞！


---

### 技术对话片段 14 (原帖: PPAC量化经历分享经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] PPAC量化经历分享经验分享_31708782472727.md
- **时间**: 1年前

**提问/主帖背景 (IM49242)**:
1.得益于ppac比赛，alpha的提交不再需要Production correlation的检测。三阶模板可以在usa delay1中回测获取大量alpha。在一个数据集中太多的回测结果在提交3个alpha左右后过多的alpha的自相关性不再满足比赛的条件。巧合下，我在平台上看到了顾问 KZ79256 (Rank 21)分享的本地0误差计算自相关性的帖子，阅读完帖子就可以轻松使用。再通过剪枝函数可以减少check的数量，更快找到可以提交的alpha。

2.除三阶模板之外的alpha模板的提交：在模板大师论坛中寻找一些自己运算符权限之内的模板。为了满足ppac比赛，通过chatgpt去掉了一些运算符，然后自己回测一下，确认有主信号之后就可以使用该模板了。

这里我找到一个alpha是关于期权数据的

trade_when(prc_ui_1080<1,implied_volatility_call_1080-implied_volatility_put_1080,-1)

implied_volatility_call_1080-implied_volatility_put_1080回测已经有明显信号了，但是自宇宙sharpe不满足条件。在prc_ui_1080<1之后就可以通过自宇宙测试了。

通过对期权数据的学习，prc_ui_1080<1应该反映了市场是乐观的。但是不清楚为什么

implied_volatility_call_1080-implied_volatility_put_1080信号明显。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
提供一个gpt回答：

实质上是 **同一执行价和到期日下，看涨期权与看跌期权隐含波动率的差值** ，它有一个明确的金融含义：

### ✅  **这个差值的意义：**

#### **衡量市场对未来价格变动方向的偏好或风险不对称（volatility skew / smile）**

1. **理论上（BS模型假设下）** ，在完美市场中，同一执行价和到期日的看涨和看跌期权的隐含波动率应该相等（因为它们的价格可以通过看跌-看涨平价互推）。
2. **实际上（尤其在股市中）** ，投资者对市场下跌更为担忧，因此 **看跌期权通常比看涨期权更贵**  → 隐含波动率更高 →
   所以这个差值往往是  **负的** 。

### 📈  **如果  `IV_call - IV_put > 0` ：**

- 市场对 **上涨风险或机会** 更敏感；
- 投资者可能愿意支付更高价格来对冲上涨；
- 有时意味着市场整体偏乐观或存在“ **泡沫溢价** ”。

### 📉  **如果  `IV_call - IV_put < 0` （更常见）：**

- 市场更担心 **下跌风险** ；
- 看跌期权对冲需求大，IV 被推高；
- 显示出对尾部风险（如系统性风险、黑天鹅事件）的担忧。


---

### 技术对话片段 15 (原帖: Python调用DeepSeek官方API实现数据集内字段智能组合代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Python调用DeepSeek官方API实现数据集内字段智能组合代码优化_31448235831319.md
- **时间**: 1年前

**提问/主帖背景 (YX50005)**:
在3月第二节顾问课上，老师展示了使用网页版大模型来进行字段组合生成具有经济学含义的新字段的流程，如果能把这个流程放在python中自动执行，可以提高一些效率。

- 大语言模型选择DeepSeek-R1
- 输入给大语言模型的信息遵循老师课上给的例子，包括数据集描述和字段名，字段描述

流程如下：

1.输入数据集描述/字段信息形成prompt

```
def _build_prompt(
        self, dataset_desc: str, fields_info: List[Tuple[str, str]]
    ) -> str:
        """
        构建 prompt
        """
        # 如果字段数量超过100，随机选择100个
        if len(fields_info) > 100:
            fields_info = random.sample(fields_info, 100)

        fields_text = "\\n".join(
            [
                f"{field_name}: {field_desc}; "
                for field_name, field_desc in fields_info
            ]
        )

        prompt_system = f"""
你是一位专业的量化金融分析师。现在有一个数据集提供给你：

1. 数据集描述：  
   {dataset_desc}

2. 现有字段信息：  
   {fields_text}
"""

        prompt_user = f"""
请根据以下要求，生成新的字段表达式列表：
(1) 请尽量多样化地生成新的字段表达式，且每个字段都需具有明确的经济学含义。  
(2) 可使用加减乘除等基本运算符。  
(3) 每个字段的经济学含义需有注释说明
(4) 输出格式：仅返回 JSON 数组，数组中每个元素包含 "description" 和 "expression" 两个字段：  
    • description（描述字段含义）  
    • expression（字段的实际表达式）  

请勿输出除 JSON 数组外的任何额外文字或说明。请直接返回最终的 JSON 数组结果。
"""

        return prompt_system, prompt_user

```

2.调用deepseek API

```
def _call_api(self, system_prompt: str, user_prompt: str) -> dict:
        """
        调用 DeepSeek API
        """
        data = {
            "model": "deepseek-reasoner",
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
            "temperature": 0.7,
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        response.raise_for_status()

        return response.json()

```

输出的结果类似于


> [!NOTE] [图片 OCR 识别内容]
> "description": "Adjusted
> ROE volatility factor, measuring stability
> of profitability by adjusting
> ROE
> With
> its standard deviation
> OVer
> past
> 60
> months"
> Iexpression":
> 'fnd65_totalcap_cusip_roe
> /
> fnd65_totalcap_cusip_sigma"
> }
> "description":
> ICash
> flow momentum adjusted by price momentum
> combining 18-month alpha change With
> Cash
> flow growth"
> 'expression":
> (fnd65_us5000_cusip_chgGmalphalgm
> fnd65_us5aa0_cusip_pctchgcf)
> /
> 21
> }
> "description": "Composite quality
> SCore
> combining
> debt coverage,
> profitability
> and efficiency
> ratios"
> 'expression":
> fnd65_totalcap_cusip_divcov
> fnd65_us5oao_cusip_mpg
> fnd65_allcap_sedol_ocfroi)
> /
> 3"
> }
> "description":
> "Enterprise value-adjusted operating efficiency
> ratio"
> 'expression":
> 'fnd65_totalcap_cusip_vefcomtt
> 米
> fnd6s_totalcap_cusip_saleicap"
> }
> "description":
> "Leverage-adjusted momentum
> factor
> Comb
> ining relative strength
> With
> debt
> ratio"
> 'expression":
> fnd65_us5000
> CUS
> j_d4lisr
> /
> fnd65_totalcap_Cusip_ed"
> }
> "description":
> "Earnings quality composite
> incorporating surprise persistence
> and
> forecast dispersion
> 'expression":
> (fnd65_totalcap_cusip_Surp
> 十
> fnd65_totalcap_cusip_fc_fqsurstd)
> /
> fnd65_totalcap_cusip_fc_numest"
> }
> "description": "Liquidity-risk adjusted value
> factor combining working capital with bid-ask spread"
> 'expression":
> 'fnd6s_totalcap_cusip_wcast
> fnd65_totalcap_cusip_bapzod"
> }
> "description":
> IGrowth sustainability
> SCore
> combining sales growth consistency
> With
> RSD efficiency"
> 'expression":
> (fnd65_totalcap_cusip_cg3ysales
> fnd65_totalcap_cusip_adverint)
> 米
> fnd65_us5oao_cusip_cv4qsales3y"
> }
> "description": "Composite financial
> health
> indicator combining
> debt
> Coverage
> ratios"
> 'expression":
> (fnd65_totalcap_cusip_totalcov
> 十
> fnd65_totalcap_cusip_voctni)
> /
> fnd65_Us5000
> cusip_debtcf"
> }
> "description":
> IEarnings
> revision
> momentum adjusted by market reaction sensitivity"
> 'expression":
> fnd65_Us5000
> cusip_rev3mylstd
> * fnd65_US5000
> cusip_Cre_cf"
> }
> "description":
> IFree
> cash
> flow yield adjusted
> for capital expenditure efficiency"
> 'expression":
> fnd65_allcap_sedol_pfcomtt
> /
> fnd65_allcap_sedol_capacq"
> }
> "description":
> IRelative
> Value composite comparing multiple
> Valuation
> metrics
> to industry peers"
> "expression":
> fnd65_totalcap_cusip_curindbp_
> fnd65_totalcap_cusip_curindcfp_
> 十
> fnd65_totalcap_cusip_curinddivp_)
> 3"


3.解析输出的json，获取生成的字段

```
def _parse_response(self, response: dict) -> List[str]:
        """
        解析 API 响应
        """
        try:
            content = response["choices"][0]["message"]["content"]
            if content.startswith("```json"):
                content = content[len("```json") :]
            if content.endswith("```"):
                content = content[: -len("```")]
            print(content)
            fields = json.loads(content)
            return [field["expression"] for field in fields]
        except Exception as e:
            print(f"解析响应时出错: {e}")
            return []

```

这样在通过API获取数据集的表述、字段的信息后，就可以自动地为各个数据集生成一批具有经济学含义的新的组合字段了。

更进一步

- Deepseek的官方API需要收费，可以探索其他更经济的调用大模型的方式
- 目前取了一个数据集中的随机100个字段，如果大模型本身支持，并且价格不贵，可以取更多的字段进行输入

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的实践，潜在的优化方向是把一些基础的运算符，比如sqrt，tsmean这些也同时扔给ai，供参考。


---

### 技术对话片段 16 (原帖: SA 扫盲贴之Selection是如何选到alpha的)
- **原帖链接**: https://support.worldquantbrain.com[Commented] SA 扫盲贴之Selection是如何选到alpha的_33119885224727.md
- **时间**: 1年前

**提问/主帖背景 (QZ67721)**:
简单来说,Selection就是你通过你的表达式,从你个人(own)拥有的或者你顾问等级所能触达的所有active alpha做一个筛选, 选择你需要的alpha.

选择表达式通过根据 SuperAlpha 设置对所有 Alpha 进行排名，并选择排名最高的 Alpha 来组建SA。这里是关键.你必须要非常清楚你的Selection里面为什么出现的是这样的alpha,而非那样的alpha.同时,如果你的Selection设置限制很小,那么很有可能挑到的alpha非常同质化,因为他们的权重是一致的.尤其是你设置几十个alpha的limit,但是又有几千个alpha符合条件的时候.

具体权重如何确定?

其实这里把你的Selection表达式类比成alpha即可,同时,alpha里面的每一个股票就对应你的Selection里面的每一个alpha. 从我们普通组建alpha的角度来说,经过alpha运算以后,每一个股票都有一个alpha权重,这表示这个alpha占用你的多空投资额的比例.比如今天满足你alpha表达式的有100个股票, 50做多,50做空, 权重是-1到+1之间,两者算数相加和为0.代表多空投资总额相等.

而Selection里面的alpha也会经过Selection表达式的计算,获得这个alpha的权重,在选中的alpha数量大于你settings里面设置的alpha数量时,就按照权重从高到低取出你设置数量的alpha作为你最终选中的alpha.

举例如下: in(competitions, "HCAC2025")&&not(own) &&(self_correlation <= 0.5) *  (prod_correlation < 0.5) * (long_count + short_count) *(operator_count < 8)

可以看到上一行是选择的alpha的范围,主要是判断符组成,在设置Positive的情况下,不在范围内的alpha直接赋值为0,就无法选中了.后面*号开始计算权重.这里有个关键点需要注意.后续的部分权重条件,比如乘以(longcount+shortcount)-universe_size（universe）/2,或者作者活跃天数等,都会极大增加原先alpha的权重,使用的时候可能导致选到的因子几乎来自一个作者,这些权重的量级跟prod_corr差了几个量级.

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享

学到了很多，对于sa都是比较迷茫的状态，这篇帖子教会了我很多

。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。


---

### 技术对话片段 17 (原帖: SAC 比赛第十经验分享 回馈社区经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] SAC 比赛第十经验分享 回馈社区经验分享_33745762241175.md
- **时间**: 11个月前

**提问/主帖背景 (JJ47083)**:
大家好，首先很幸运能够在SAC的比赛里获得第十名，这出乎了我的预料，因为整个比赛我只交了19个SA，当然这一切的归功于论坛和各位大佬的无私奉献，由于我清楚自己本身实力并不是很充足，能获奖运气占比很大，所以在这里我会分享我的经验希望能够帮助大家。

这是我在整个比赛期间，所用到的combo表达式，主要来源于论坛

1. stats = generate_stats(alpha); innerCorr = self_corr(stats.returns, 500); ic = if_else(innerCorr == 1.0, nan, innerCorr);maxCorr = reduce_max(ic); 1 - maxCorr
2.combo_a(alpha)

3.stats = generate_stats(alpha);mom = ts_ir(stats.returns,60);ts_rank(mom,500)
4.w1 = combo_a(alpha,nlength = 40 , mode ='algo1');w2 = combo_a(alpha,nlength = 160 , mode ='algo1');w3 = combo_a(alpha,nlength = 252, mode ='algo1');scale (w1)+scale (w2)+scale (w3)
5.1
这里会选择1的原因是因为在我针对1个select对所有combo进行回测时，我会用1的结果去对比其他表达式，如果其他表达式效果不好或者表现下降特别大的情况下，即使能加分，我都会选择提交等权的SA。

接下来是Selection的分享，对于Selection我的理解是，从原有的alpha池子选出你设置的池子，然后在你的专属池子中对alpha进行打分排序，通过limt你就能选出自己想要的alpha了，这时候就有一个问题，在比赛中我们有GM的权限，即使分配了相应的主题，依旧能选择很多的alpha，即使你limt设置了500，他都能选满，那么这时候你在进行打分就是很困难的，所以我在想能不能设置严格的条件，在专属的池子里alpha的数量可观，于是我就去论坛里找灵感了

在这里非常感谢JB71859的无私分享，也是靠着这位大佬的表达式帮我在ATOM那周获得了第一


> [!NOTE] [图片 OCR 识别内容]
> 871859
> 1个月前
> Idea
> 高质量低相关策略
> Selection Expression:
> (self_correlation
> <二
> 0.5)
> (prod_correlation
> 0.4)
> (turnover >= 0.1)
> (turnover <= 0.3)
> (long_count
> Short_count)
 
当时我在翻论坛的时候，一眼就注意到了这个表达式，这不是正好是一个非常严格的布尔表达式吗，于是我立马去尝试，limit设置为500，这时候我就发现他选不到500了，没记错的话只选出了300多，那这完全达到了我的目的，然后我们就可以针对性打分了，在你选出的alpha中我们可以看到View all，点击他你就可以看到所有选择的alpha，这时候我会首先看不同Universe的alpha占比，比如在EUR，如果选出来的alpha里TOP1200占比极少，那么这时候我多加一个universe == 'TOP2500'的条件，其次我会看turnover，如果有些turnover很高，但他的其他指标很奇怪，这样的alpha我也会通过控制turnover去除掉，最后我会按照turnover打分排序和控制limt（我limt选择200到300）优先选出较好的alpha出来

接下来就是回测，对于任何一个区域，我都会遍历所有的中心化和区域，最后在选择加分较高，表现提升的更好的SA交，然后每周比赛我我都会刻意交不同Regin的SA，想要is分高，如果同一个区域相似的表达式交了2个以上，在多交的话，他的is加分就会很少，甚至扣分，所有一定要多区域的交，其次就是要有独特的selcetion,is分才会高

由于我当时比赛vf较低，所以我不会去考虑要把pro降低到0.5以下，更注重的是数值，以下是我在ATOM各区域中表现较好的SA

EUR TOP2500 Crowding Factors
 
> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximun
> Minimum
> Last Run; SUn; 07/27/2025,5:06 PM
> l
> 0.5970
> -0.5005
> 1OOM
> N
> TM
> Q
> 寰
> 1Ok
> 区
> 昱
> 100
> 皂
> 0.01
> 09
> 02
> 03
> 0^
> 0?
> 0@
> 0^
> 09
> 09-
> 0?2
> 6
> 0?
> 5l
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> TUrnOVeT
> Fitness
> Returns
> Drawdown
> Marein
> 11.43
> 12.379
> 16.80
> 27.029
> 0.609
> 43.689600
> 0.8
> 0.2
>  
> 0.7..
> 0.7.
> ~0.5。
> -1,0
> ~0.3,



> [!NOTE] [图片 OCR 识别内容]
> 戌
> Chart
> Pnl
> 叫
> N
> Q
> 25M
> 区
> ZOM
> 6
> 15M
> 6/22/2018
> Equal Weight Pnl: 15.93M
> IS Combo Pnl
> 14.18M
> 10M
> 5,0OOK
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


USA TOP3000 SUNINDUSTRY
 
> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> Maximun
> Minimum
> Last Run; SUn; 07/27/2025,5:05 PM
> 0.6347
> -0.6243
> o
> N
> IS Summary
> Period
> IS
> 05
> Q
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 区
> 8.43
> 13.969
> 9.26
> 16.849
> 0.879
> 24.139600



> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 25M
> ZOM
> 15M
> 10M
> 5,OOOK
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


ASI FAST


> [!NOTE] [图片 OCR 识别内容]
> Prod Correlation
> MaxinUI
> UinimUn
> Last Run:
> 07/27/2025,5:13 PM
> 0.6984
> -0.2190
> TOON
> IN
> 寰
> 1Ok
> 昱
> 皂
> 100
> 0@
> 05
> 0
> 09
> 0^
> 09
> 0?
> 0^ 
> 05
> 0
> 03
> IS Summary
> Period
> IS
> 05
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> RetUrns
> Drawdown
> Margin
> 9.20
> 9.53%
> 13.74
> 27.879
> 1.25%
> 58.479600
> SUR
> 0.5
> 0.7
> 1.0
> 0.4
> 0.7..
> 0.1.
> 0.2.
> @
> 0.7.



> [!NOTE] [图片 OCR 识别内容]
> N
> Chart
> Pnl
> 2SN
> 05/26/2020
> ZOM
> Equal Weight Pnl: 19.94M
> I5 Combo PnL
> 19.94M
> 15M
> 1OM
> 5OOOK
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


尽量选择近似一条直线的交，如果尾部区域区域水平，那么他的os基本上就是不行的，然后在根据加分多少来提交就好了。

目前，权限回归之后，能选择到的alpha不像比赛那么多，动态分层去选择alpha或许比较好，比如游戏王的turover分层，和橘子姐的datacategories 分层，我在实践中取得了不错的效果。

以上就是我整个比赛以来的经验，由于当时正值期末，有些比较难的主题就没有去提交，当然更多的是我没实力，没想到居然可以排这么高的名次，在这里再次感谢论坛里的各位大佬以及JB71859，感谢WQ这么好的学习氛围，让我这个对量化0基础的，代码也不懂的小白可以慢慢接触学习量化。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
wow

恭喜获奖，期待共同进步！

===========================================================================================================================


---

### 技术对话片段 18 (原帖: SA分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] SA分享_33119868350615.md
- **时间**: 1年前

**提问/主帖背景 (QZ67721)**:
Selection：
in(competitions, "HCAC2025")&&not(own) &&(self_correlation <= 0.5) * (prod_correlation < 0.5) * (long_count + short_count) *(operator_count < 8)
Combo：
combo_a(alpha, nlength = 250, mode = 'algo3')

region ： usa
universe：TOP3000
delay：1
decay：50
neutralization：subindustry
++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++
像能给大家一点启发

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享

但还是想问一下，decay拉到50有什么小巧思吗？

Selection：
in(competitions, "HCAC2025")&&not(own) &&(self_correlation <= 0.5) * (prod_correlation < 0.5) * (long_count + short_count) *(operator_count < 8)
Combo：
combo_a(alpha, nlength = 250, mode = 'algo3')


---

### 技术对话片段 19 (原帖: SA日入50刀，如何把握好SuperAlphaCompetition经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] SA日入50刀如何把握好SuperAlphaCompetition经验分享_32630124449559.md
- **时间**: 1年前

**提问/主帖背景 (MG88592)**:
大家好，我是顾问 MG88592 (Rank 38)，目前Genius等级为Gold，Value Factor（VF）为0.95，分组G4。今天想和大家分享一下最近SuperAlpha比赛的Base Payment情况，并总结一些实用经验。

**收益表现** 
得益于SAC策略，近四天的SuperAlpha Base日均收益达到50美元，相比之前提升了两到三倍！研究小组已经公开了SuperAlpha的收益公式，这里结合我的实际数据验证一下：

**关键发现**

1. **Value Factor决定上限** ：VF 0.99或1.0的选手，提交Fitness>5且Prod Corr<0.5的sa时，基本能拿到顶格Base。
2. **我的收益天花板** ：由于VF仅0.95，我的单日Base上限约为50美元。
   
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 75
> 06/03/2025
> Super:
> 47.15
> 50
> Regular:
> 7.80
> Total:
> 54.949999999999996
> 25
> 31. May
> Jun
> 2.Jun
> 3.Jun
> Jun
> 5.jun
  
> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
>  Status
> Created (EST)
> Region
> Universe
> Delay
> Submission Date
> Self-
> Prod-
> (EST)
> Correlation
> Correlation
> SearCh
> Super Alpha
> Selec
> Selec
> SearCh
> Selec
> Selec
> Selec
> Selec
> Search
> e.吕>1
> e.吕>1
> 0.63
> Super
> ACTIVE
> 06/06/2025 EDT
> ASl
> MINVOLIM
> 06/06/2025 EDT
> 0.32
> 0.63
> Super
> ACTIVE
> 6/05/2025 EDT
> USA
> T0P3000
> 6/05/2025 EDT
> 0.1 /
> 0.41
> 0.48
> Super
> ACTIVE
> 6/04/2025 EDT
> EUR
> TOP2500
> 6/04/2025 EDT
> 0.49
> 0.49
> 0.5002
> Super
> ACTIVE
> 06/03/2025 EDT
> EUR
> TOP2500
> 06/03/2025 EDT
> 0.36
> 0.49
> 0.48
> Super
> ACTIVE
> 06/02/2025 EDT
> EUR
> TOP2500
> 06/02/2025 EDT 
> 0.35
> 0.49
> Date
> Tag

   **数据实证**
   以下是近期的具体指标（Prod Corr均<0.5）：
   - Fitness 8.48 | PC 0.49 → Base 46.76
   - Fitness 7.92 | PC 0.49 → Base 50.99
   - Fitness 5.46 | PC 0.49 → Base 47.15
   - Fitness 6.80 | PC 0.47 → Base 50.15
   今天提交的pc有点拉垮，可以预见base打对折。
   **核心结论**
   - **PC的优先级高于Fitness** ：当Fitness>5后，进一步升高对Base影响极小，而降低PC能显著提升收益（例如PC从0.49降至0.47时Base增加）。
   - **策略建议** ：不必盲目追求高Fitness或加分，优先控制PC<0.5才是收益最大化的关键。
   希望对大家有所启发，欢迎交流优化思路！
   **希望您顺手点个小赞，祝您base多多！**
   更新昨日sa pc0.6+。base仅有15刀

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的帖子，感谢分享。

mg大佬一直在探索sa的select与combo，值得学习！！！！


---

### 技术对话片段 20 (原帖: ② POST 失败时打印错误并直接 return，避免后续引用未定义变量simulation_response = s.post(url, json=sim_data)if simulation_response.status_code != 201:    print("POST failed:", simulation_response.status_code, simulation_response.text)    return                        ← 退出本次任务simulation_progress_url = simulation_response.headers['Location'])
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的代码，感谢分享 ！！！


---

### 技术对话片段 21 (原帖: super alpha的学习成果经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] super alpha的学习成果经验分享_33255038555031.md
- **时间**: 1年前

**提问/主帖背景 (YL21428)**:
我是去年就加入Brain的“萌新”，经历过vf暴跌，所以一直都没有什么兴趣去研究super alpha，这一次按照论坛里大佬们的经验，终于做出来了看起来还不错的super alpha.

我看的就是下面这些

[【进阶学习】Super Alpha 每日获得额外1-60USD，来此学习 – WorldQuant BRAIN]([L2] 03-【进阶学习】Super Alpha 每日获得额外1-60USD来此学习Pinned_32759852398487.md)


> [!NOTE] [图片 OCR 识别内容]
> 2.5A经验分享
> [有奖] SuperAlpha征文:  分享你独到的selection和combination方法!
> SAB入50刀, 如何把握好SuperAlphacompetition from MC88592
> 2024 super alphal赛心得
> 0H29412
> [SuperAlpha灵感]  因子择时模型 fromYw93864
> 组sa时如何选取高质量因子?
> from 2559763
> [5A完全搜索最大独立集]  提交尽可能多的Super Alpha from L479055
> [SuperAlpha灵感] ChatCPT Portfolio Selection
> [SuperAlpha灵感]
> Risk Parity
> [SuperAlpha灵感] Modern Portfolio Theory
> [SuperAlpha灵感]
> Post-Modern Portfolio Theory
> (SuperAlpha灵感]  从面试题到RegularAlpha和SuperAlpha的思考
> from


接下来我就讲一下我做super alpha用了什么selection和combo

我喜欢使用的Selection Expression是if_else(turnover >= 0.15 && turnover <= 0.20, 1.5, 1) * if_else(turnover >= 0.30 && turnover <= 0.35, 1.5, 1) / operator_count * (1 - self_correlation) * if_else(in(competitions, "ACE2023"), 1, 0)

我的Combo Expression是combo_a(alpha, nlength = 500, mode = 'algo1')

我首先用两个换手率条件对股票进行筛选：

if_else(turnover >= 0.15 && turnover <= 0.20, 1.5, 1) - 当换手率在15%-20%区间时给予1.5倍增强

if_else(turnover >= 0.30 && turnover <= 0.35, 1.5, 1) - 当换手率在30%-35%区间时也给予1.5倍增强

除以operator_count - 操作者越多，信号强度会被稀释

(1 - self_correlation) - 降低自相关性高的股票权重，追求更独立的信号

if_else(in(competitions, "ACE2023"), 1, 0) - 只选择参与ACE2023比赛的股票，因为我是G2，这个周为了特定比赛，一定要设置的过滤条件

combo是借鉴论坛里的做法，我自己不太明白其中的具体思想

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有意义的实践，通过权重进行相关性筛选，而不是强制限制cor小于30or50，值得学习。

此外，针对combo，combo_a是个智能算法，1是等权，其他的一些组合方式就把整个因子 池的不同属性，例如turn，pnl，看做字段来跑的，ra。


---

### 技术对话片段 22 (原帖: Super Alpha选择及防过拟合技巧_豆包总结)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Super Alpha选择及防过拟合技巧_豆包总结_33043004374039.md
- **时间**: 1年前

**提问/主帖背景 (YX23928)**:
一、防过拟合技巧

1. 过拟合定义 ◦ 当模型（Alpha）过度拟合样本内数据（in sample），而非捕捉样本外（out of sample）的通用模式时，即发生过拟合。

2. 防过拟合方法 ◦ 经济可解释性：Alpha 需具备经济意义，避免单纯基于统计指标筛选。 ◦ 多维度测试：通过子宇宙（sub-universe）和超宇宙（super-universe）测试验证 Alpha 的稳定性，例如延迟排名、参数变化分析等。 ◦ 简洁性原则：Alpha 应避免使用过多数据字段，可通过操作符数量（operator count）和数据字段数（data field count）进行筛选。    二、OS 起始日期（Out Sample Start Date）的应用

1. 筛选逻辑 ◦ 通过 OS 起始日期过滤新提交的 Alpha，例如排除 2025 年 2 月后提交的 Alpha，避免纳入未经过样本外验证的模型。

2. 性能评估 ◦ 对比 OS 起始日期前后的夏普比率（Sharpe Ratio），若前 / 后比率大于 1，表明 Alpha 在样本外表现更稳健。 ◦ 示例：2022 年 7 月 16 日前的性能反映拟合效果，之后反映非拟合效果，需重点关注后者。

三、Super Alpha的多样性构建

1. 数据来源多样化 ◦ 避免集中使用回报率（returns）、市值（cap）等常见数据字段，可通过排除特定数据类别（如价格、成交量）实现。

2. 交易频率与中性化 ◦ 利用不同换手率（turnover）区间筛选 Alpha，或采用多种中性化方法（如行业、风格中性化）降低相关性。

3. 区域分散策略 ◦ 建议在全球、亚洲、欧洲等不同区域提交超 Alpha，避免单一市场风险（如美国市场竞争激烈，易出现过拟合）。

四、筛选与优化建议

1. 关键指标 ◦ OAScore：高权重指标，需减少噪声信号（如非稳健 Alpha）对排名的影响。 ◦ 测试周期设置：通过 OS 起始日期和测试周期（test period）筛选未过度拟合的 Alpha。   2. 实操技巧 ◦ 使用组合表达式（combo expression）降低相关性，例如结合长短期收益率移动覆盖比率。 ◦ 控制入选 Alpha 数量（建议 100-250 个），平衡模拟效率与多样性。

五、问答环节摘要

1. 样本外周期（Samoyeds Period） ◦ 指 Alpha 提交时的样本外阶段，模拟时不可见，需通过长期表现验证其有效性。

2. 降低交易成本 ◦ 调整中性化方法，避免复杂表达式的负权重，可借助 Carmelator 工具优化。

3. 区域选择优先级 ◦ 依每周主题而定，全球区域（涵盖欧美亚）通常更优，但亚洲市场需开启 Mac trace 设置，欧美市场需注意相关性风险。

4. 产品相关性降低 ◦ 通过组合不同表达式（如长短周期指标比率）、调整中性化因子（如慢因子）实现。

六、总结 会议强调防过拟合需结合经济解释性、多维度测试与简洁性原则，超 Alpha 构建需注重数据、区域及策略的多样性。建议通过 OS 起始日期、夏普比率对比等工具筛选稳健 Alpha，并定期调整策略以适应市场变化

**顾问 worldquant brain赛博游戏王 的解答与建议**:
================================ZS59765=============================================

感谢分享，参加了会议但是英语不好，听不太懂，这下明白了，再次谢谢大佬的分享

====================================================================================


---

### 技术对话片段 23 (原帖: Thanks BRAIN Community for everything in 2024!)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Thanks BRAIN Community for everything in 2024_28885704754711.md
- **时间**: 1年前

**提问/主帖背景 (NG20776)**:
Happy new year and take a look back at our achievements! We are looking forward to seeing what you achieve next in 2025!  [Quant on!]([链接已屏蔽])

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Happy new year and thanks for conducting a lot of competitions throughout the year it was a great learning experience and would like to continue the same in the upcoming years . I would love to perform even better starting this new year


---

### 技术对话片段 24 (原帖: The 101 ways to measure portfolio performance.)
- **原帖链接**: https://support.worldquantbrain.com[Commented] The 101 ways to measure portfolio performance_25238156125207.md
- **时间**: 1年前

**提问/主帖背景 (NL41370)**:
**Comment from Brain Researchers:**

Proposes multiple approaches to evaluate portfolio performance, can be used as machine-driven research's fitness function.

**Research Paper Link :**

[[链接已屏蔽])

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Thank you for sharing this research paper.It helped me a lot to understand the things better


---

### 技术对话片段 25 (原帖: velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享_32340009231127.md
- **时间**: 1年前

**提问/主帖背景 (JB71859)**:
在我第一次更新VF（velue factor）时，数值显示为0.04。当时，我心中充满了疑问：系统难道出错了吗？怎么会有这么低的VF值？于是，我急忙写邮件询问，是否是系统问题，但得到的回复却是：“没有问题。”这让我瞬间陷入了深深的失落，几乎觉得天塌了——怎么可能，连0.1都不到，之后还能做什么？

然而，这只是我VF学习之路的起点。为了寻找答案，我开始请教一些经验丰富的大佬，他们中有些VF值高达0.98甚至1.0。他们耐心地与我分享了他们的经验和见解，这些交流让我逐渐找到了自己的问题所在。原来，我不自觉地陷入了过拟合的泥潭，交出的结果都是“垃圾”。我明白了：问题出在自己的方法上。

**重新审视与总结**

经过这段时间的反思，我发现了自己在方法上的几个关键错误。在不知不觉中，我深陷于一阶、二阶、三阶死代码的漩涡，完全忽视了核心的“alpha”操作。我每天就是无脑地运行代码，反复跑着一堆没有意义的模型，完全没有思考“为什么”去做这些。VF值的低迷，也正是这些无用操作累积的结果。

意识到问题后，我开始调整思路。为了避免重复犯错，我决定通过更为系统的方式进行自我提升。我开始更加积极地参加论坛讨论、查阅书籍，并向研究小组里的资深成员请教，深入了解模型的核心思想与技术细节。每天都坚持积累，不再盲目操作，而是逐步理清了我自己的逻辑框架。

**突破与升华**

随着不断的实践与学习，我逐渐整理出了属于自己的交alpha逻辑和代码。我的模型开始逐步改进，VF值也在不断提高。最终，我成功突破了0.5以下的瓶颈，达到了0.93还成为了Expert。这段艰辛的成长历程，虽然充满挑战，但也让我收获了宝贵的经验和深刻的理解。

通过这次经历，我深刻认识到，技术和方法固然重要，但更重要的是要保持不断学习、持续反思的态度。没有什么是“一蹴而就”的，每一次的低谷，都是我们成长的铺垫。正是这份坚持与耐心，才让我从0.04走到了0.93，终于找到了属于自己的成功之路。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很宝贵的经验，感谢大佬分享。向大佬学习

===生活就像海洋，只有意志坚强的人才能到达彼岸===

===This is an apple, I like apples, apples are good for our health===


---

### 技术对话片段 26 (原帖: vf更新了，大佬们是如何那么高vf的？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] vf更新了大佬们是如何那么高vf的_33127609798167.md
- **时间**: 1年前

**提问/主帖背景 (AH18340)**:
vf更新了，大佬们是如何那么高vf的？

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================

**顾问 worldquant brain赛博游戏王 的解答与建议**:
d多交sa，sa可以巩固组合表现（notown）

=============================================================================

The best time to plant a tree is 20 years ago. The second-best time is now.

=============================================================================


---

### 技术对话片段 27 (原帖: Vscode自动提示operator代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] Vscode自动提示operator代码优化_33274404140439.md
- **时间**: 1年前

**提问/主帖背景 (WL27618)**:
有时候一边写代码一边查opeartor网页会非常打断思路, 我们可以基于自己的 JSON 文档开发一个轻量级的 VSCode 插件，提供 **悬停文档** 和 **自动补全** 功能，用于自定义的 **数据字段** 和 **运算符** ，。

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> Welcome
> 1U
> test py
> t
> ts_arg
> Iax
> ts_arg_max(x,
> ts_arg_min
> ts_av_diff
> Time Series
> ts_backfill
> ts
> Returns the relative index of the max Value in the tme
> ts
> Count_nans
> series for the past d days
> If the current day has the max
> ts
> covariance
> Value for the past d days, i returns 0.If previous day
> ts_decay
> linear
> has the max Value for the past d days; j returns
> ts_delay
> ts_delta
> ts_ir
> ts
> kurtosis
> test py
> LCOFr
 

大家可以在vscode搜我编译好的插件试一下.

 
> [!NOTE] [图片 OCR 识别内容]
> EXTENSIONS: MARKETPLACE
> brain_s
> brain_snippet
> 2ms
> Worldquant brain platform datafiel..
> Roshameow
> Restart Extensions
> {
> 氐
 
加载自己的opeartors. 像这样, 在这里添加自己的json路径.

 
> [!NOTE] [图片 OCR 识别内容]
> field-operator-hints
> EXTENSIONS: MARKETPLACE
> Welcome
> package.json
> 田 Extension: brain_snippet
> test:py
> Settings
> 义
> brain_
> Jext:Roshameow field-operator-hints
> Setting Found
> brain_snippet
> 2ms
> User
> Workspace
> Backup and Sync Settings
> Worldquant brain platform datafiel..
> Roshameow
> Extensions (1)
> 品
> Field Operator Hints: Custom Operator JSON Path
> Path to a custom operator JSON file (absolute or workspace-relative path)
> 唱
> 囚


**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的插件，已经用上了

省去了一边写 模版一边翻learn的烦恼，点赞！！！

========================================================================================================================================================================


---

### 技术对话片段 28 (原帖: [代码踩坑]回测偶然卡住不动的解决方法经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [代码踩坑]回测偶然卡住不动的解决方法经验分享_30988224144151.md
- **时间**: 1年前

**提问/主帖背景 (HQ17963)**:
许多新人会遇到回测卡住不动的情况，有两个可能的原因：

1. 有的回测就是一直不结束

解决方法：保存回测开始时间，如果回测超过半小时，就跳过该回测。

2. 网络或服务器原因

默认情况下， `requests的get()或者post()`  不会设置超时时间。如果目标服务器没有响应或响应非常慢，程序会一直等待，直到服务器返回数据或连接中断。

解决方法：加timeout参数

在每次get和post时，添加参数：

response = session.get(url, timeout=30)

response = session.post(url, timeout=30)

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢你的分享，很有用的方法，点赞！


---

### 技术对话片段 29 (原帖: - HTTP 400 错误表示客户端发送的请求存在错误，无法被服务器理解和接受。常见原因包括请求参数错误、请求头设置不当、Cookie问题、客户端软件错误等。解决方案：1. 首先检查函数调用那里传参的填写内容格式是否正确（如调用 multi_simulate 函数那里的第二个参数应该是`SECTOR`而非`Sector`）2. 还有报错 400 ，post 的代码尝试改造如下（理论上应该是参数错误，你看看是不是有个批量槽只送了一个 alpha ）if len(sim_data_list)== 1:    simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=sim_data_list[0])else:    simulation_response = s.post('https://api.worldquantbrain.com/simulations', json=sim_data_list))
- **原帖链接**: https://support.worldquantbrain.com[Commented] [工程优化]增强版mult_simulation分享_30359217149847.md
- **时间**: 1年前

**提问/主帖背景 (ZL35633)**:
* 支持断点续跑

* 支持卡槽分配

* 支持完成时间预估

* 优化提交效率 [速度+15%]

* 基础语法+单线程实现

* 兼容旧版本接口

```
import osimport jsonimport timeimport hashlibimport datetimeimport wqbAPI_SIMULATION_URL = "[链接已屏蔽] = "[链接已屏蔽] _generate_payload(task):    payload = []    for code, decay in task['alpha_list']:        item = {            'type': 'REGULAR',            'settings': {                'instrumentType': 'EQUITY',                'region': task['region'],                'universe': task['universe'],                'delay': 1,                'decay': decay,                'neutralization': task['neutralization'],                'truncation': 0.08,                'pasteurization': 'ON',                'testPeriod': 'P2Y',                'unitHandling': 'VERIFY',                'nanHandling': 'ON',                'language': 'FASTEXPR',                'visualization': False,            },            'regular': code        }        payload.append(item)    return payloaddef _is_slot_available(session, slot):    if not slot:        return True    try:        now = time.time()        if slot.get('check_time', 0) > now:            return False        response = session.get(slot['progress_url'], timeout=60)        retry_after = response.headers.get("Retry-After", 0)                if retry_after != 0:            slot['check_time'] = now + float(retry_after)        else:            slot['cost'] = float(now - slot['start_time'])            data = response.json()                        if data.get("status") == "COMPLETE":                slot['complete'] = True                print(f"Task {slot['task_id']} complete, Cost: {int(slot['cost'])} s")            else:                print(f"Task {slot['task_id']} fail, Cost: {int(slot['cost'])} s")                print(slot['task'])                for task_id in data.get('children', []):                    msg = session.get(API_SIMULATION_MSG_URL.format(task_id=task_id), timeout=60).json()                    print(json.dumps(msg, indent=2))            return True    except Exception as e:        import traceback        traceback.print_exc()    return Falsedef _submit_task(session, slot, task):    if not task:        return False    slot['task'] = task    slot['task_id'] = task['task_id']    slot['alpha_list'] = task['alpha_list']    slot['start_time'] = time.time()    slot['complete'] = False    slot['check_time'] = 0        try:        payload = _generate_payload(task)        response = session.post(API_SIMULATION_URL, json=payload)        slot['progress_url'] = response.headers['Location']        return True    except Exception as e:        print(f"Error submitting task: {e}, http_code: {response.status_code}")        print(payload)        time.sleep(600)    return Falsedef _gen_signature(alpha, region, universe, neutralization):    code, decay = alpha    plaintext = f"{region}{universe}{neutralization}{decay}{code}"    sign = hashlib.md5(plaintext.encode()).hexdigest()    return sign        def _make_task(neutralization, region, universe, task_id, alpha_list, signature_list):    task = {        'task_id': task_id,        'alpha_list': alpha_list,        'region': region,        'universe': universe,        'neutralization': neutralization,        'signature_list': signature_list    }        return taskdef _initialize_tasks(alphas, signature_set, neutralization, region, universe):    tasks = list()        alpha_list = list()    signature_list = list()        cnt = 0        for alpha in alphas:        sign = _gen_signature(alpha, region, universe, neutralization)        if sign in signature_set:            print(f'Skip alpha, {alpha}')            continue                alpha_list.append(alpha)        signature_list.append(sign)                if len(alpha_list) >= 10:            task = _make_task(neutralization, region, universe, cnt, alpha_list, signature_list)            tasks.append(task)            cnt += 1            alpha_list = list()            signature_list = list()                if len(alpha_list) > 1:        task = _make_task(neutralization, region, universe, cnt, alpha_list, signature_list)        tasks.append(task)    elif len(alpha_list) == 1:        print(f"Invalid Task: {alpha_list}")                            print(f"Total Tasks: {len(tasks)}")        return tasksdef _estimate_completion(n_task, n_slot, avg_cost):    estimated_time = datetime.datetime.fromtimestamp(time.time() + (avg_cost * n_task / n_slot))    return estimated_time.strftime("%Y-%m-%d %H:%M:%S")def _save_checkpoint(file_path, task):    with open(file_path, 'a') as fp:        for sign in task['signature_list']:            fp.write(f'{sign}\n')            fp.flush()def _load_checkpoint(checkpoint_file):    signature_set = set()    if not os.path.exists(checkpoint_file):        with open(checkpoint_file, 'w') as _:            pass    with open(checkpoint_file) as fp:        for sign in fp:            signature_set.add(sign.strip())     return signature_setdef _cost_avg():    cost_list = list()    def add_cost(cost):        nonlocal cost_list        cost_list.append(float(cost))        return sum(cost_list)/len(cost_list)    return add_costdef run_simulations(session, alphas, neutralization, region, universe, slot_num=9, checkpoint_file='./simulation.ckpt'):    slots = [dict() for _ in range(slot_num)]    signature_set = _load_checkpoint(checkpoint_file)    tasks = _initialize_tasks(alphas, signature_set, neutralization, region, universe)        cost_avg = _cost_avg()    while tasks:        for slot in slots:            time.sleep(0.1)            if _is_slot_available(session, slot):                                task = tasks.pop(0)                                if slot.get('complete', False):                    _save_checkpoint(checkpoint_file, slot['task'])                    print(f"Estimated completion: {_estimate_completion(len(tasks), len(slots), cost_avg(slot['cost']))}")                                if _submit_task(session, slot, task):                    print(f"Task {slot['task_id']} submitted")                print("Simulation complete")def multi_simulate(alpha_pools, neut, region, universe, start):    wqs = wqb.WQBSession(('<email>', '<password>'))    alphas = list()    for pool in alpha_pools:        for batch in pool:            for alpha in batch:                alphas.append(alpha)    run_simulations(        wqs, alphas, neut, region, universe,         slot_num=10, checkpoint_file='./simulation.ckpt'    )
```

**顾问 worldquant brain赛博游戏王 的解答与建议**:
location一般是：你槽已经跑满了，或者入参有问题（建议检查alpha的表达式是否正确）


---

### 技术对话片段 30 (原帖: [经验分享]手搓因子理论支持，从此交满不是梦！【系列一】经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] [经验分享]手搓因子理论支持从此交满不是梦【系列一】经验分享_33675647454999.md
- **时间**: 11个月前

**提问/主帖背景 (TL32287)**:
引言：

大家好，最近有些新的研究，给大家一阅。

首先，在日常中machine_lib大家使用占居多，但是效率还是颇慢，主要的原因来至对数据的敏感不高，也就是没有很多时间熟悉操作符带来的影响。

首先，致谢：XZ81923提供一定的手搓理论支持，SY90356、AL13375、ZZ44620提供一定的改进建议。

正文：

首先，在日常的挖掘中，我们会选择一阶达到sharp>=1.0或者更好标准，或者fitness大于0.5-0.8。

那么为什么要选择这些标准？那么是不是这份工作就是在数据的筛选？

有没有理解数据的本质是什么？我也困惑？

方法一：

就是去观察每次剥离后的层级关系对应：

比如：
原始的表达式是：

ts_delta(winsorize(ts_backfill(vec_sum(nwsxx),120), std=4), 7)

那么第一层剥离后是：

winsorize(ts_backfill(vec_sum(nwsxx),120), sstd=4)

第二层剥离后是：

ts_backfill(vec_sum(nwsxx),120)

第三层剥离之后是：

vec_sum(nwsxx)

最后的剥离回归到原始的数据：

Nwsxx

将这样的剥离的数据每一个和原来的数据进行对比在一个图上，那么就能实现观察逆向还原数据的本身带来的变化。

示例：


> [!NOTE] [图片 OCR 识别内容]
> 表达式层级PNL对比 (黑色为原始基准)
> 1e6
> 层级 1: ts_delta(winsorize(ts_backfill.
> 1e6
> 层级 2: winsorize(ts_backfill(Vec_suml.
> 层级因子:
> 原始因子: m
> 原始@子
> _
> _
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
> 2023
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
> 2023
> 曰期
> 曰期
> 1e6
> 层级 3: ts_backfill(vec_sum(nws
> 1e6
> 层级 4: Vec_sum(nws.
> 原始@子:
> 原始@子:
> 2
> _
> _
> MAIA
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
> 2023
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
> 2023
> 日期
> 日期


原始的数据(层级4）vec_sum(nwsxx)经过ts_backfill（层级3）之后能够有效减少波动，由于数据缺失带来的极端波动。

winsorize操作符（层级2）在原本的基础上实现了减少由极端数据，也就是标准差之外的收益，也就是在数据中可以把原本的std=4换成std=3观察波动，最后原表达式，经过ts_delta之后就意外找到一个可以进阶的alpha.

1、这一点可以学到什么？

当数据波动幅度很大可以尝试winsorize，ts_backfill操作符降低，没有用的时候，说明数据完整，不需要优化。

- ts_op带来的变化是什么？还有没有必要其他操作符？

说明在时序上进行因子挖掘，本事上是改变数据的分布形态，在近似正态分布上的数据更可以被线性利用做线性回归。；

还有没有必要要使用其他操作符请看方法二。

说明

方法二：

将进入二阶的表达式回测，观察每一个操作符带来的影响；

直观的看到数据在操作符的直观变化，


> [!NOTE] [图片 OCR 识别内容]
> 分组操作对比 (黑色曲线为原始因子)
> group_neutralize 组表 邓比
> 40M
> 35p(1.25]
> 3.0M
> Z.OM
> 1.0M
> 匾
> 云
> QOM
> -1.0M
> 
> ZOM
> 3.0M
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
> 日期
> group_rank 组表现邓比
> 40M
> 3.0M
> Z.OM
> 1.0M
> 俭
> 云
> QOM
> -1.0M
> 2.M
> 3.0M
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
> 日期
> group_zscore 组表 邓比
> 40N
> (1.25]
> 3.OM
> 2.OM
> 1.0M
> 岛
> 日
> QOM
> -1.0M
> 2.M
> 3.0M
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
> 日期


图表中原始因子的持续超额收益强烈暗示：该因子的核心预测能力来源于对 **宏观趋势或跨组别特征** 的捕捉。分组操作在消除行业风险的同时，也剔除了核心alpha来源，导致“倒洗澡水连孩子一起倒掉”的现象。

解决办法，尝试ts_op进入二阶查看效果：

效果图：


> [!NOTE] [图片 OCR 识别内容]
> 时旬序列操作符分组对比 (黑色曲线为原始因子)
> ts_delta 组表珈邓比
> ts_rank 组表现邓比
> ts_sum 组表 邓比
> 6OM
> 6OM
> GOM
> 原始医子: mTdx35p (1.25)
> 原始医子: mTdx35p (1.25)
> 原始医子: mTdx35p (1.25)
> M7dx35p (1.25)
> AESTW
> 50)
> YYOgXZw (089]
> M7dx35p (1.25)
> AESTW
> SOJ
> YYOgXZw (089]
> I7dx35p (1.25)
> AESTWW
> 50)
> YYOgXZw (089)
> m7dX3Sp [1.25)
> AESTM
> 50)
> YYOgXZw (089]
> 47N
> 47M
> 47M
> m7dx3Sp (1.25)
> AESTM
> 50)
> YYOgXZw (089]
> m7dx35p (1.25)
> AESTW
> 50)
> YYOgXZw (089)
> M7dx35p (1.25)
> AEST {0.50)
> YYOgXZw (089]
> I7dx35p (1.25)
> AESTWW
> 50)
> YYOgXZw (089]
> I7dx35p (1.25)
> AESTWW
> 50)
> YYOgXZw
> 891
> 3.4M
> 3.4M
> 34M
> 21M
> 21M
> 21M
> 匾
> 屉
> 云
> 云
> 云
> 0gM
> 0gM
> OgM
> D4NI
> -D4N
> -D4NI
> -1.7M
> -1.7M
> -1.7M
> 3OM
> -30M
> -30M
> 2013
> 2014
> 2015
> 2016  2017
> 2018
> 2019  2020
> 2021  2022
> 2023
> 2013
> 2014  2015 2016  2017
> 2018  2019  2020 2021  2022 2023
> 2013  2014
> 2015 2016  2017  2018  2019  2020 2021
> 2022 2023
> 日期
> 日期
> 日期
> ts_delay 组表现邓比
> ts_std_deV 组表 邓比
> ts_arg_min 组表现邓比
> GOM
> GOM
> GOM
> 原始困子 m7dx3Sp (1.25)
> 原始匝子: m7dx3Sp (1.25)
> 原始医子: mTdx3Sp (1.25]
> MVnQGJL (0.35)
> GgNGnzQ (-0.52]
> 05LP7d6 (0891
> VPbvyod (0.351
> G9NGnzQ (-0.52)
> 051p7d6 (0.89)
> MVnQGJL (0.35)
> G9NGnZQ (-0521
> 05Lp7d6 (089]
> VPbvyoA (0.351
> GSNGnZQ (-052]
> 05LP7d6 (089]
> 47M
> 47M
> 47M
> NVnoGJl (0.35)
> G9NGnzQ (-0.52)
> 05LP7d6 (0.89)
> VPbvyoA (0.351
> GgNGnzQ (-0.52]
> 05Lp7d6 (0.89)
> NVnoGJl (0.35)
> G9NGnzQ (-0.52)
> 05LP7d6 (0.89)
> VPbvyoA (0.351
> G9NGnZQ (-0521
> 05Lp7d6 (089]
> MVnQGJL (0.35)
> GSNGnZQ (-052]
> 05LP7d6 (089]
> 3.4M
> 3.4M
> 34M
> Z1M
> 21M
> 21M
> 蜃
> 俭
> 盏
> 盏
> 云
> 09M
> 0gM
> O9M
> 0.4M
> -0.4M
> -04M
> 1.7M
> -1.7M
> -1.7N
> 30M
> -3.0M
> -3.0M
> 2013
> 2014
> 2015
> 2016  2017
> 2018  2019  2020  2021
> 2022
> 2023
> 2013
> 2014 2015
> 2017  2018
> 2019  2020
> 2021
> 2022
> 2023
> 2013  2014 2015 2016
> 2017  2018  2019   2020 2021
> 2022
> 2023
> 日期
> 日期
> 日期
> ts_arg_max 组表珈邓比
> ts_scale 组表 邓比
> ts_quantile 组表现邓比
> 6OM
> 6OM
> GOM
> 原始匝孑: m7dx3Sp (1.25)
> 原始匝孑: m7dx3Sp (1.25)
> 原始匝孑: m7dx3Sp (1.25)
> VeL3gPM (0.40]
> qVp6gIZ (045]
> bAgQ5kl (0.58)
> Vel3gPM (0.40]
> qVp6gIZ (0.45)
> bAgQskl (0.58)
> VeL3gPM (0.40)
> qVp6glZ (045)
> bAgQ5kl (0.58)
> VeL3gPM (0.40)
> qVp6glZ (045)
> bAgQ5kl
> 58]
> 47M
> 47M
> 47M
> Vel3gPM (0.40]
> 9Vp6gI2 (045]
> bAgQ5kl (0.58]
> Vel3gPM
> .40]
> qVp6gIZ (0.45)
> bAgQskl
> 58]
> Vel3gPM
> qVp6gIZ (0.45)
> bAgQskl (0.58)
> VeL3gPM
> .40]
> qVp6glZ (045)
> bAgQ5kl
> 58]
> VeL3gPM (0.40)
> qVp6glZ (045)
> bAgQ5kl (0.58)
> 34N
> 34N
> 34M
> 21M
> 21M
> 21M
> 匾
> 榀
> 云
> 云
> 云
> OgM
> OgM
> OgM
> D4NI
> -D4NI
> -D4NI
> -1.7M
> -1.7M
> -1.7M
> 3.0M
> 3.0M
> -3.0M
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
> 2023
> 2013
> 2014  2015 2016  2017
> 2018
> 2019  2020 2021  2022 2023
> 2013  2014
> 2015  2016
> 2017
> 2018  2019 2020
> 2021
> 2022 2023
> 日期
> 日期
> 曰期
> {
> 2016


可以看到随机100个的结果也是并不理想，那么思考原因出现在什么地方？

对手搓有什么帮助？

可以看到大多数的手搓ts_op都是有相同的共性的，那么简短的手搓只需要测试几个操作符就可以进行，比如直接测试ts_rank(expr,day)day = 10 或60 就可以直观看出可以大致的变化趋势，如果含义有效，那么可以继续优化，在大致的方向做优化，原理是时序因子的权重更高吧？

我的理解是，这个可能原本是111（三时序）因子，但是你没有数据，也不知道他原本就是时序因子，也就是说从高维度去观察低维因子他不是完全形态但是你想要找到高纬度的因子是很麻烦的，很无序的；

如何最简单便捷的办法找到因子这是最佳的方法，machine_lib挖的方法，展示的是结果和筛选的过程，没有品味怎么制作出来。

最后，这种形态的数据应该怎么解决？

查看数据特性，进行针对性修改，在手搓的时候进行“重要的操作符快速手搓拿到结果，缩短时间”；

最后进行模板化操作，下一步代码优化方向，根据模板课第二课进行优化处理；

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有意思的帖子，点赞

手搓确实是一个成熟顾问应该掌握的技能

期待后续推出降cor手搓，提fit手搓等教学！

===================================================================================


---

### 技术对话片段 31 (原帖: 【2025SAC比赛G4组ACE第二分享】（新人向自动回测SA指南+获奖因子揭晓）)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【2025SAC比赛G4组ACE第二分享】新人向自动回测SA指南获奖因子揭晓_33223079226391.md
- **时间**: 1年前

**提问/主帖背景 (FZ60707)**:
大家好，这一次运气使然获得了ACE组的第二，来和大家分享是怎么做的SA和获奖的因子是长什么样子的。(其实哥们也刚来不久哈，3月底才来的，也算刚来一个季度，我也还在不断摸索，说错了请见谅呀(*´∀`)~♥)

首先昨天看到了有很多新顾问进来，我想着应该有一些同学还没有SA的权限或者还在手动回测SA，手动回测确实有些累人。论坛里是有一些宝藏的，比如自动回测SA的代码，我来给大家指条路（其实就是我走的路线），按照这条路走，你一定可以挂着代码该吃吃该喝喝，不用盯着屏幕去回测SA了。

我是用的 [顾问 JL16510 (Rank 18)](/hc/en-us/profiles/25889743296151-顾问 JL16510 (Rank 18)) 大佬提供的回测代码，链接如下： [多线程遍历回测super alpha – WorldQuant BRAIN]([Commented] 多线程遍历回测super alpha代码优化_31527668843671.md) 。你把里面的代码复制出来保存成.py文件，就可以运行了，里面需要改的地方其实就几处，首先有个regi = ['usa']，这里你可以改成你想跑的地区，比如'eur','usa','asi','glb'。然后还有一个参数叫'selectionLimit': 1000,这个是选择的ra的个数，你要选择几个ra来组，老师说过大于30个是比较好的，他原代码这里是1000，我选择改成50，（1000个也太多了喂）然后关键的是select表达式和combo表达式这里，即selection_exp和combo_exp，这里是需要去做文章的，也是大家水平的体现了。但是......显然哥们是水平有限，还是得从论坛里找资源，最后找到了这篇由顾问 KZ79256 (Rank 21)大佬提供的文章： [【SA自动化】像RA一样跑SA – WorldQuantBrain-CN]([L2] 【SA自动化】像RA一样跑SA代码优化_30682024469527.md) 。里面其实也是一种自动回测SA的方式，不过更吸引我的是他的代码自带了超多的表达式，我就直接用了，就是把代码复制给selection_exp和combo_exp，我还没有太多太深刻的对SA表达式的理解，这也是我后面需要去学习的。

有人会问：如果大家都用一样的表达式，那岂不是大家都跑一样的，相关性咋过？

答：其实我也有这个担心，不过因为这个比赛每个人的组别不同，而且每个人每天只能交一个SA，而且有的组别还能跑多个地区，比赛结束了的话，每个人交的ra也不一样的，交SA撞车几率还是小的。这个方法只是前期更丝滑的提交SA，不至于SA交不上。

以上就是我这段时间做SA的流程，希望对大家有用，当然论坛还有很多其他大佬写的文章，不过自己还没有实现过，也就不推荐了。

#---------------------------------分割线-------------------------------------------------------------------

然后是获奖因子的样子，这次ACE的比赛我只交了4个SA，很坦白的讲，其中前两个是厂SA，所以我想获得名次应该是后面两个SA的OS表现比较好（为啥后面两个不是厂绝对不是因为已经交了厂导致相关性过不去了(#`Д´)ﾉ）

第一个厂：


> [!NOTE] [图片 OCR 识别内容]
> ACNV
> Created 06/17/2025 EDT
> anonymoUs
> Add Alpha
> List
> Code
> IS Summary
> Period
> Selection Expression
> Aggregate Data
> Sharpe
> Fitnes
> C-c
> CST
> Mare
> (in(competitions
> ACE2023
> & not(Own) )*
> (1-prod_correlation)* (1
> turnoVer ]
> 5.74
> 4.11%
> 6.99
> 18.5596
> 2.659
> 90.309600
> Combo Expression
> Year
> TTTOVOT
> Htness
> Returns
> DawUOWn
> Marqin
> Count
> Short Count
> 2013
> 532
> 4.511
> 5.85
> 12.5190
> 0.429
> 54.71553o
> 1524
> 1CSC
> simulation Settings
> 2014
> 5.93
> 3.63
> 550
> 15.0255
> 0.5895
> 81.635600
> 541
> 1253
> Instrument Type
> Reqion
> UnNerse
> Lanquage
> Delay
> Truncation
> Neutralization
> Pasteuriation
> NaN Handling
> Unit Handling
> MaxTrade
> 2015
> 553
> 684
> 15.0755
> 0.3795
> 87.325600
> 552
> 537
> US。
> TOP3OOO
> Fast Expression
> 0.08
> SEC-OF
> WErfy
> 2015
> 5.95
> 3.754
> 817
> 17.2935
> 0.569
> 355
> 547
> 1534
> 2017
> 7.62
> 3.314
> 8.83
> 15.3350
> 0.549
> TTC
> 1571
> 2013
> 13
> 1201
> 37
> 17.8996
> 0.5891
> OSFCoo
> 551
> 1570
> 2013
> 9.59
> 425北
> 13.03
> 23.0990
> 0.509
> 108.
> 541
> 155-
> Clone Alpha 
> 2020
> 0 6
> 1.274:
> 2022
> 44.3833
> 0.8395
> 210.375600
> 519
> 701
> 303
> 4454
> 3 C
> 95
> 55o
> 76.115600
> 1
> Chart
> PIL
> 2022
> 220
> 4374
> 1.66
> 7.1235
> 3995
> 32.556600
> 1551
> 595
> 2023
> 71
> 341
> 5.3050
> 0.2795
> 1552
> 1507
> Risk neutralized
> 1OI
> Aesresate
> Data
> ShaTm
> TUCN
> ITSS
> CamO
> 1areir
> 6.1
> 4.119
> 6.24
> 13.0596
> 2.0996
> 63.549600
> 5,0OOK
> 医 Correlation
> Jul'13
> 1an'14
> Jul"
> Jan ' 15
> Jul '15
>  Jan
> "16
> Jul '16
> Jan
> Jul'7
>  Jan '13
> Jul' 18
> Jan ' 19
> Jul '19
>  Jan '20
> Jul 20
> Jan '21
> Jul '21
> Jan 22
> Jul '22
> Jan '23
> Self Correlation
> T3irIIT
> Winimuq
> Last Run; ThU
> 07/03/2025
> 3 C
> 0.4801
> -0.1283
> Combo Pnl
> Equal Weight Pnl
> Drod
> Correlation
> WaxinTuT
> Winimuq
> Last Run
> ThU
> 07/03/2025
> 3.35 Pu
> 0.7437
> -0.6093
> OS Testing Status
> Period
> 05
> Properties
> NC- - SSTo
> 0512552025
> 5-09
> Name
> Category
> 11PENDING
> CurrentlyanonymOUS
> None
> Color
> Selected Alphas
> Alphas have been
> -二
> Neal
> Selectladd tags
> None
> Sharpo
> LO
> Decay
> Eq
> 42560
> 035-00
> Tags


第二个厂:


> [!NOTE] [图片 OCR 识别内容]
> ACN
> Created 06/18/2025 EDT
> anonymous
> Add Apha
> 3 List
> Code
> IS Summary
> Period
> 05
> Selection Expression
> Aggregate Data
> Sharps
> TTO
> Fins =
> ETIICm
> ra
> (i(competitions
> ACE2023
> not
>  OWn
> )(1-prod_correlation )
> 4.62
> 7.879
> 4.20
> 10.3596
> 1.939
> 26.299600
> Comhc
> Expression
> Year
> Sharpe
> TIONOT
> Ftness
> Returs
> DrawJOWn
> Marqin
>  Count
> Short Count
> 5tats
> generate_stats(alpha); innercorr
> self_corr(stats.returns, 500);
> if_else(innerCorr
> 1.0
> nan; innercorr );maxCopp
> reduce
> max(ic);
> MaxCorr
> 2013
> 3.37
> 7.4350
> 2.29
> 5.795
> 2903
> 15485600
> 1S-7
> 1531
> Simulation Settings
> 2014
> 2.54
> 5.7450
> 1.72
> 5.235
> 1.2701
> 15.675600
> 1571
> 1530
> Instrument
> Type
> Reqjon
> UnNerse
> Language
> Delay
> TUCation
>  Neutraliation
> Pasteuriation
> NaN Handling
> Unit Handling
> MaxTrade
> 2015
> 5.9350
> 4.25
> 937*
> 0.795
> 27.045630
> 1561
> 1575
> Equizi
> US
> TOPTJ
> Fast Expression
> 0.03
> SIOW - FEs? Facrors
> Verf
> 2015
> 1.35
> 7.3150
> 3.39
> 7.56沁
> 0.5495
> 20.635603
> 1557
> 1574
> 2017
> 3.93
> 7.5455
> 3.10
> 7.53光
> 0.5295
> 20.12560
> 1537
> 1SGs
> 2013
> 5.44
> 3.335
> 5.2-
> 53*
> 0.3395
> 27.625603
> 156-
> 1535
> Clone Alpha 
> 2019
> 7.95
> 8.1630
> 3.5-
> 15.3
> 0.7395
> 4_935
> 1565
> ISs
> 2020
> 1071
> 8.5255
> 171
> 28.0-沁
> 0.3795
> 55.306630
> 1550
> 1554
> 2021
> 2.79
> 9.2250
> 2.30
> &.49沉
> 1.395
> 13-153
> 1535
> 1557
> Chart
> Pnl
> 2022
> 1.39
> 8.4530
> 0.57
> 2.83汇
> 1.4195
> 6.325433
> 1537
> 1C5
> 2023
> 2.15
> 7.7950
> 1.5
> 535
> 0.3495
> 11.3360
> 7,5OOK
> 医 Correlation
> 5OOOK
> Self Correlation
> TTTT1IT
>  Minimum
> Cm
> 25OOK
> 07103120_
> 
> 680.521
> 一
> Prod Correlation
> T3irIIT
> IT
> + Pm
> Jul '13
> Jan"
> Jul'
> Jan '15
> Jul' 15
> Jan '16
> Jul '16
> Jan '17
> Jul 17
> Jan '"18
> Jul '18
> Jan
> 19
> Jul'19
> Man
> Jul '20
> Jan '21
> Jul 21
> Jan '22
> Jul'22
> Jan '23
> Combo Pnl
> Equal Weight Pnl
> Properties
> +
> TTe= Fn
> 5C
> Name
> Category
> Currently anonymous'
> NOne
> OS Testing Status
> Period
> 05
> Color
> Selectladdtags
> None
> 11PENDING
> Short descriptions OfyoUr Selection Expressionand Combo Expression are required
> submit this SUperAIpha
> Selected Alphas
> Alohas have been selecred
> Wewall
> Description of Selection Expression*
> 908
> 100 character minimum
> Long 
> Decay
> Tags


第三个SA：


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/19/2025 EDT
> anOnyMOUS
> Add Alpha t0 3 List
> Code
> IS Summary
> Period
> 05
> Selection Expression
> Aggregate
> Sharp
> TUITn
> Fines
> CCaIC
> 113r3ir
> (in(competitions,
> ACE2023
> NOTLOT
> COIIN+
> sqrt(universe_size (universe)
> 11101001761
> !
> 4.01
> 12.2596
> 3.72
> 10.779
> 2.349
> 17.599600
> Comho
> Expression
> VOar
> TITOVOT
> Ftness
> Roturs
> Drawdown
> Marqin
> Long Count
> Short Count
> stata
> Benerate_stats(alpha);
> stata.pnl;
> 2013
> 3.73
> 3550
> 2.76
> 6.66沁
> 1.0195
> 11.745603
> 1595
> 1355
> ts_mean(a, 250 )/ts_std_dev (a,258)
> 1_T
> 2014
> 3.33
> 12.0050
> 3.0-
> 7.485
> 0.3195
> 1535
> 1410
> i5
> 4.21
> 11.7390
> 7.95沁
> 0.55N
> 1353
> 593
> 14-2
> Simulation Settings
> 2015
> 1.30
> 9255
> 03
> 1141
> 15.245600
> 143
> Instrument Type
> Reqion
> Umerse
> Language
> Decay
> Delay
> Truncation
> Neutraliatijon
> Pasteurizatijon
> NaN Handling
> Unit Handling
> MaxTrade
> 2017
> 0955
> 3.5-
> 8.31沁
> 0.5095
> 14.985603
> 1707
> 1395
> Equi?i
> US。
> TOP3OO0
> Fast Expresslon
> 7.03
> SIOW - FEs? Facrors
> Verfi
> 13 _T
> 2013
> 3.53
> 11.9635
> 2.33
> 8.05沁
> 1.0093
> 1113
> 141
> 2113
> 5.92
> 11.1790
> 5.23
> 13.84光
> 0.509
> 247850
> 153
> 1425
> 702
> 5.3+
> 035
> C
> 16.29沁
> 0.5291
> 25.00R6oo
> 147
> Clone Alpha
> 202
> 2.74
> 14.9550
> 2.30
> 10.49北
> 2.3495
> 11.035600
> 1693
> 1455
> 2022
> -0
> 13.1990
> 5.30
> 19.12沁
> 1.3793
> 2900F8oo
> 153
> 1518
> 2023
> 3.15
> 11.1795
> 1-
> 21.37*
> 0.2391
> Sooo
> 503
> 1574
> N Chart
> Pnl
> [
> Correlation
> Self Correlation
> T3irIIT
> LnimIn
> Last Run:
> OOOK
> Correlation
> Naximun
> Minimun
> Last Run:
> Jul '13
> Jan 
> Jul'
> Jan '15
> Jul"15
> Jan '16
> Jul '16
> Jan '17
> Jul' 17
> Jan '"18
> Jul '18
> Jan '19
> Jul '19
> Jan '20
> Jul '20
> Jan '21
> Jul 21
> Jan '22
> Jul'22
> Jan '23
> Properties
> Wed
> 06/25/2025。5.05 Pw
> ComboPnl
> Equal Weight Pnl
> Name
> Category
> CurrentlanonymOUsi
> NOne
> Color
> 叫 OS
> Testing Status
> Period
> 05
> Selectladdtags
> NonE
> Short descriptions ofyour Selection Expressionand Combo Expression are required
> SUbmit this
> SuperAlpha
> PENDING
> Description of Selection Expression*
> 1011
> 100 character minimum
> The Selection Expression
> desisned to filter stocks based
> participation in the "ACE20Z3" competition (in(competitions
> ACE2023") while excluding those already owned (not(ownj). The result is then scaled by the ratio ofthe
> Selected Alphas
> 50 AIphas have beEnselected
> Viewall
> numberof
> positions
> Count) tothe square rootofthe universe size (sqrtluniverse_size(universe)j)。 which norma
> the selection based on portfolio breadth. This adjustment ensures that the strategy remains balanced
> reeardless ofthe total number of stocks available
> Data
> IonB
> Sharpo
> 7
> Prod
> Tags
> Ione
> (ongC
> IiZes


第四个SA：


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 06/19/2025 EDT
> anOnyMOUS
> Add Alpha
> 3 LISt
> Code
> IS Summary
> Period
> 05
> Selection Expression
> Aggregate Data
> ShaT
> Fi-nes
> ETIICMS
> Opac
> Marair
> (i(competitions,
> ACE2023
> & not(own) )8gturnover>8.15
> 龊 (O5_start_date
> '2812-06-01'
> && color
> 'PURPLE" )
> turnover
> 5.41
> 10.469
> 5.72
> 13.959
> 1.7296
> 26.679600
> Combo Expression
> Year
>  Sharpe
> Turover
> Ftness
> Retums
> Drawdown
> Marqin
> Long Count
> Short Count
> Combo_
> (alpha)
> 2013
> 1.77
> 0.0090
> 0.71
> 0.00沁
> 0.009
> 0.0OFCoo
> Simulation Settings
> 2014
> 3.32
> 13.5140
> 3.29
> 15.3
> 0.509
> 29.375600
> 1430
> 14-5
> Instnument Type
> Reqjon
> Unmerse
> Lanquaqe
> Decav
> Delay
> Truncation
> Neutralization
> Pasteurizatjon
> NaN Handling
> Unit Handling
> Max Trade
> 2015
> 9.71
> 3.4590
> 12.76
> 21.59沁
> 0.339
> 45.57530
> 1553
> EqU
> USA
> TOP3JOD
> Fast Expression
> 0.03
> Ststisti-sl
> Verf
> 2016
> 13.3
> 10.0035
> 1
> 0.21
> 50.235633
> 1C-
> 127
> 20
> 3.54
> 8.7555
> 3.70
> 16.12沁
> 0.341
> 36.34520
> 15-7
> 1535
> 2018
> 3.57
> 10.7050
> 2.36
> 800*
> 0.3995
> 1-.945603
> 155-
> 1535
> Clone Alpha 
> 2013
> 2.17
> 11.3150
> 1.35
> 5.13*
> 0.3195
> 90ss
> 533
> 1557
> 2020
> 1.24
> 10.553
> 4.52
> 14.35沁
> 3695
> 27.335630
> 1563
> 15-1
> 2021
> 2.50
> 12.4855
> 2.06
> 852*
> 1.7295
> 13.655633
> 153
> 567
> Chart
> PIL
> 2022
> 355
> 5935
> 31_
> 10.445
> 1.1745
> 21.785630
> 1553
> 533
> 2023
> 1.18
> 10.0390
> D.5
> 2.57*
> 0.254
> 51152
> 1532
> 153s
> 医 Correlation
> OOOK
> Self
> Correlation
> Maximum
> WinimuT
> Last Run:
> 0711612013
> Equal
> Weight Pnl: 536.55K
> Combo DnL
> DO0
> Correlation
> Maximum
> Minimum
> Last Run:
> Jul '13
> Jan
> Jan '15
> Jul' 15
> Jan '16
> Jul '15
> Jan '17
> Jul
> Jan '18
> Jul'18
> Jan '19
> Jul'19
> Jan '20
> Jul '20
> Jul 21
> Jan '22
>  Ju1'22
> Jn '23
> Combo Pnl
> Equal Weight Pnl
> Properties
> Las: saved Ied。 06/2512025。5:05 PM
> Name
> Category
> CurrentlyanonymOUS
> NOne
> 4 OS
> Testing Status
> Period
> 05
> Tags
> Color
> Selectladdtags
> NOnE
> 11 PENDING
> Short descriptions OfoUr Selection Expression and Combo Expression are required to submit this SuperAlpha
> Selected Alphas
> Alohas have been selecred
> Viewall
> Description of Selection Expressionx
> 930
> 100 character minimum
> Prod
> Jul'


以上就是交的四个因子，你问我为啥获奖，我也不造......大概是后面两个因子的OS表现比较好把。

我交SA的时候会尽量交2022和2023的sharpe为正值的SA，当然我也看到过有人说过2023就1个月，不能代表什么，但是我还是比较在意负值的，负值给人一种不信任的感觉：你连这一个月都表现不好，我还期望你以后表现好？？（类似这种心理ಠ_ಠ）更深层次的分析就留给大佬们把。

希望这篇文章能对萌新有用，也希望各位能在接下来的两周嘎嘎获奖，获得好名次！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享。因子质量确实不错

这边也要补充一句，针对撞车这个事情，没有必要担心。可以用prodcor进行限制（后台因子的cor tag是不断更新的，所以代码里面prodcor<0.5总是能选到0.5以下的因子，这也是为啥前期已选选一千个，后期就几十个，一百来个的原因），不用太担心撞车这个事情。


---

### 技术对话片段 32 (原帖: 【9月有奖活动】Alpha模板征文：分享你独到的Idea和Implementation！)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【9月有奖活动】Alpha模板征文分享你独到的Idea和Implementation_33603438929047.md
- **时间**: 11个月前

**提问/主帖背景 (WL13229)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
波动率分歧因子（适用于rsk数据 类型）

模版：

```
<group_op>(power(<ts_op>(abs(<data>),<day1>),2)-power(<ts_op>(<data>,<day1>),2),<group>)
```

**具体变量：**

<group_op>：'group_neutralize','group_zscore','group_rank','group_normalize'

<ts_op>：'ts_std_dev','ts_rank','ts_sum','ts_zscore'

<data>：与风险有关的数据集 字段 ，例如rsk70

<day1>：常见的时间窗口 ，5,20,120,252均可，模版中默认是5

<group>：中性化组，模版中默认使用四个基础的中性化组

**搜索空间大小：** 按照默认参数，单个字段搜索空间为4*4*4*1=64个因子=7个槽

**产出效果：** 实验在usa地区按照使用人数倒序选取前100个rsk类型数据，目前跑了2234个因子，按照sharpe1和fit0.6进行筛选，得到114个因子，产出率为5%

**模版的idea：** 衡量过去 `<day1>` 天内数据的波动幅度与趋势的偏离程度，可以用来衡量风险的稳定性或者风险的突变。

**探索方向：**

- 在其他类型数据中实验模版
- abs(data)=data的问题，weijie老师给出的建议是把abs的处理方式换成在数轴上的分布，从而按照分布进行处理，初步的想法是按照ts_mean作为分布中心点，以if_else的方式代替abs处理，可以基于此进一步优化模版


---

### 技术对话片段 33 (原帖: save your alphas as txt)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【AI-agent】How to build your own quant AI-agent with ollama structure_30039527427991.md
- **时间**: 1年前

**提问/主帖背景 (SH97251)**:
Hello there, AI assistants helps us a lot in our work, but AI with very specific knowledge is not that common. So I will introduce how to build your own AI assistant by a simple study case.

Here I will use ollama to deploy my local LLM model, and choose deepseek-r1:8b to run （because the limit of my machine, larger model, better result, so choose the biggest model that your machine could handle）.

1. Load the model locally.

First, search "ollama" and download it on web.


> [!NOTE] [图片 OCR 识别内容]
> Discord
> GitHub
> Models
> Search models
> Signin
> Download
> Get upand running with large
> language models.
> Run Lama33, DeepSeek-R1 Phi-4. Mistral
> Gemma 2. and other models, locally。
> Download
> Available for macOS,
> Linux, and Windows
> 2025 Ollama
> Blog
> Docs
> GitHub
> Discord
> (Twitter)
> Meetups
> Download


2. When ollama is downloaded, install it. Then, open your terminal to run "ollama pull deepseek-r1:8b" (change the model name if you use different model).

3. When the model loading is completed, you could send messages in your terminal cell and get answers, but that is what we want. What I want is, send very long csv or json data, and a few lines of prompts to let the model work for me. So I need to build a local agent. Here comes the tutorial:

4. Create a python file (end with ".py"). Assume that I have a case to combine operators with certain fields. And now I have the operators in csv file and I have the fields with csv file, too. Then follows the code (I'm Chinese so I use Chinese as annotation, but I also added some English annotation, please use chargpt or other AI tools to translate the annotations that without English version (Actually those not translated annotation are not important : D)):

import csv
import subprocess
import os

# 函数：读取CSV文件，返回字典形式的内容

# Function: read the csv file, return the contents in dictionary.
def read_csv(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# 函数：构建运算符描述字符串

# Function: find the description of the operators
def build_operator_description(operator_data):
    description = ""
    for row in operator_data:
        operator = row[0].strip()
        rule = row[1].strip()
        description += f"运算符: {operator}，规则: {rule}\n"
    return description

# 函数：构建字段描述字符串

# Function: find the descriptions of the fields
def build_field_description(field_data):
    description = ""
    for row in field_data:
        field = row[0].strip()
        text = row[1].strip()
        description += f"字段: {field}，描述: {text}\n"
    return description

# 函数：生成alpha因子的请求并调用LLM模型

# Funtion: call LLM model to produce alphas.
def generate_alpha_factor(operators_description, fields_description, prompt, output_file):
    # 构造完整的 prompt

# organize full prompt
    full_prompt = f"运算符和规则描述:\n{operators_description}\n字段和描述:\n{fields_description}\n生成alpha因子的要求:\n{prompt}"

    # 调用模型生成结果

# call model to produce results
    result = subprocess.run(
        ["ollama", "run", "deepseek-r1:8b"],
        input=full_prompt,  # 通过标准输入传递 prompt
        capture_output=True, text=True
    )

# 处理返回的结果
    if result.returncode == 0:
        # 将生成的结果保存到指定的文本文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result.stdout)
        print(f"Alpha因子已保存到: {output_file}")
    else:
        print("Error occurred:", result.stderr)

# 主函数
def main():
    # 输入文件路径
    operator_file = 'your own file path with operators'  # 运算符与运算规则描述文件
    field_file = 'your own file path with fields'  # 字段与描述文件
    prompt = """Your own reqires. You could use double quota if you don't need multi-line prompt.
    """

    # 输出文件路径

# output file path
    output_file = 'generated_alpha_factor.txt'  # 生成的Alpha因子保存为txt文件

    # 读取CSV数据

# read csv data
    operator_data = read_csv(operator_file)
    field_data = read_csv(field_file)

# 构建描述

# run the function about description extraction

operators_description = build_operator_description(operator_data)
    fields_description = build_field_description(field_data)

# 生成Alpha因子并保存为txt文件

# save your alphas as txt
    generate_alpha_factor(operators_description, fields_description, prompt, output_file)

if __name__ == "__main__":
    main()

**顾问 worldquant brain赛博游戏王 的解答与建议**:
excellent post, upvoted!

and here i would like to provide a simple guidence about ollama and chatbox in chinese version:

[[链接已屏蔽])

what's more, i think its pretty difficult for people without powerful computrer to have powerful local ai

helper.

(please upvote this comment if you find something useful, thx!)


---

### 技术对话片段 34 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha模板】情绪数据中用ts_covariance构建alpha模板Alpha Template_35294898626711.md
- **时间**: 8个月前

**提问/主帖背景 (RM49262)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
高端的因子只需要简单的表达式

所以是不是可以这样，把covariance换成其他支持二元，多元的运算符呢？

此外，数据的量纲是不是最好也要处理下

=========================================================================================哈哈，你还不知道吧，其实我是游戏王==================================================================================


---

### 技术对话片段 35 (原帖: 【alpha模板】有关速度加速度模板的处理)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【alpha模板】有关速度加速度模板的处理_33046186122903.md
- **时间**: 1年前

**提问/主帖背景 (YZ70114)**:
在前几期的双周会中，kunqi 老师分享了一个模板，但回测下来并未获得好的结果

我当前是以这样进行处理的

```
def process_time_derivative(datafields):    tb_fields = []    days = [5, 22, 66, 240]    for field in datafields:        for day in days:            # 速度            tb_fields.append(f"ts_delta({field}, {day})")            # 加速度            tb_fields.append(f"ts_delta(ts_delta({field}, {day}), {day})")    return tb_fields
```

生成为基础字段，后续套用其他操作符去回测alpha，这套模板是否是处理正确？或者是应该适用于哪个类型的数据集？

**顾问 worldquant brain赛博游戏王 的解答与建议**:
个人感觉可以嵌入一阶模版中，一起跑。供参考

========================================================================================================================================================================


---

### 技术对话片段 36 (原帖: 【Alpha灵感】Stock Market's reaction to liquidity shocksAlpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】Stock Markets reaction to liquidity shocksAlpha Template_32546137590039.md
- **时间**: 1年前

**提问/主帖背景 (TK60163)**:
**这篇论文在撰写过程中出现了一个随机的错误，结果意外地产生了一个表现良好的 alpha。（如果你能找出这个 alpha 为什么有效，将不胜感激）**

研究论文： [[链接已屏蔽]) 
讲义资料： [[链接已屏蔽])

**摘要：**

This paper investigates how the stock market reacts to firm level liquidity shocks. We find that negative and persistent liquidity shocks not only lead to lower contemporaneous returns, but also predict negative returns for up to six months in the future. Long-short portfolios sorted on past liquidity shocks generate a raw and risk-adjusted return of more than 1% per month. This economically and statistically significant relation is robust across alternative measures of liquidity shocks, different sample periods, and after controlling for various risk factors and firm characteristics. Furthermore, the documented effect is stronger for small stocks, stocks with low analyst coverage and institutional holdings, and for less liquid stocks. Our evidence suggests that the stock market underreacts
to firm level liquidity shocks, and that this underreaction can be driven by investor inattention as well as illiquidity.

**我们的灵感来自 PDF 第13页第1段：**

> *The significantly positive correlation between liquidity shocks and future stock returns suggests that negative liquidity shocks (reductions in liquidity) are related to lower cross-sectional stock returns. In this section, we perform formal analysis, and show that the pricing effect documented in this paper cannot be explained by other risk factors and firm characteristics that are known to predict future stock returns in the cross-section.*

**现在让我们使用流动性冲击与股票回报之间的相关性来构建 alpha。**

**但是等等，我们该如何衡量流动性冲击？**

**让我们看看第4页第1段：**

> The main liquidity shock variable we employ is constructed as the standardized innovation of the negative Amihud’s (Amihud (2002)) illiquidity measure, demeaned (using the past 12-month illiquidity as the mean) and divided by its past 12-month standard deviation.

由于它使用了 **Amihud illiquidity measure** ，我们尝试再找一篇有关该公式的论文：


> [!NOTE] [图片 OCR 识别内容]
> Let Diy be the number of days with available data for stock
> I Jear !;
> be the stock return for
> stock
> 边 day dof year g; and
> VOLDiwyd be the daily volume (证 lnits Of currency).
> Amihud (2002)8
> meastre is calcllated
> 38
> ILLIQy
> 106
> Diy
> ToLDiuyd
> This calculation is typically done for a Jear_
> but one
> Can
> take averages at different frequencies, such
> 95
> quarterly Or monthly.
> Riyd
> Rigl


在拥有所有所需条件后，我们开始构建 alpha：

```
amihud = (10^6)*(1/252)*ts_sum(abs(returns)/volume,252);illiquidity = ts_mean(amihud,252)/ts_std_dev(amihud,252);-ts_corr(illiquidity,returns,63)
```

这个 alpha 确实表现出了一些信号，但依旧较弱。


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 05
> Needs Improvement
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.69
> 30.709
> 0.17
> 1.969
> 7.129
> 1.289600
> Year
> Sharpe
> Trnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 2.11
> 30.8996
> 0.76
> 3.9896
> 0.88%
> 2.57930
> 1528
> 1521
> 2019
> 1.55
> 29.7490
> 0.52
> 3.39%
> 1.0995
> 2.289330
> 1523
> 1514
> 2020
> -1.78
> 31.4396
> 0.71
> 5.0196
> 8995
> 9930
> 1534
> 1499
> 2021
> 1.97
> 31.3496
> 0.90
> 6.4996
> 1.97%
> 49300
> 1562
> 1526
> 2022
> 0.23
> 30.1096
> 0.04
> 0.8496
> 4.1295
> 0.569330
> 1548
> 1538
> 2023
> -1.57
> 31.79%6
> 0.54
> -5.22%6
> 0.639
> 3.299330
> 1554
> ctiate IindOMC
> 1549


经过对数值和操作符的一些调整，我偶然发现了一个表现相当不错的 alpha：


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP30O0
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Subindustry
> 0.01
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


Expression:

```
amihud = (10^6)*(1/252)*ts_sum(abs(returns)/volume,252);illiquidity = normalize(amihud,useStd=false);-ts_corr(illiquidity,amihud,42)
```


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> 1S
> 05
> G000
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.14
> 6.88%
> 1.98
> 10.68%
> 6.999
> 31.069600
> Year
> Sharpe
> Turnover
> Ftness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2018
> 0.56
> 5.1496
> 0.18
> 1.369
> 1.459
> 4.43930
> 1391
> 1655
> 2019
> .96
> 7.6490
> 1.37
> 6.10%
> 1.96%
> 15.999300
> 1498
> 1535
> 2020
> 2.37
> 7.7496
> 2.45
> 13.4195
> 2.5395
> 34.649300
> 1542
> 1488
> 2021
> 3.15
> 5.6396
> 4.32
> 23.52%
> 6.9995
> 70.919300
> 1519
> 1565
> 2022
> 1.50
> 5.3896
> 1.11
> .88%
> 2.5995
> 21.57900
> 1423
> 1663
> 2023
> 12.45
> 4.6990
> 23.89
> 46.02%
> 0.23%
> 196.099330
> 1390
> 1718


使用标准化 amihud 与 amihud 本身在两个月内的时间序列相关性，这样就能创建一个可以独立提交的 alpha。

在此发现后，我尝试进一步优化表达式以获得最佳性能用于提交。以下是最终版本：

```
amihud = (10^6)*(1/252)*ts_sum(abs(returns)/volume,252);illiquidity = normalize(amihud,useStd=false);-hump(group_neutralize(ts_corr(illiquidity,amihud,42),bucket(rank(mdl77_valuemomemtummodel_reportedearningsmomentummodule),range="0,1,0.2")),hump=0.0005)
```

New data introduced: mdl77_valuemomemtummodel_reportedearningsmomentummodule

新增数据： `mdl77_valuemomemtummodel_reportedearningsmomentummodule` 
定义：已公布收益动量模块（Reported Earnings Momentum module）

我选择这个因子用于中性化的原因是，我认为高收益公告的股票已经吸引了许多投资者/分析师的注意，因此投资者/分析师不会对流动性冲击反应不足，因为他们已投入该股票。

**结果：**


> [!NOTE] [图片 OCR 识别内容]
> IS Summary
> Period
> IS
> 0S
> Excellent
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> MarEin
> 2.31
> 4.829
> 2.23
> 11.62%
> 5.359
> 48.199600
> Year
> Sharpe
> Turnover
> Hitness
> Returns
> Drawdown
> Margin
>  Long Count
> Short Count
> 2018
> 0.67
> 4.5196
> 0.25
> 1.6995
> 1.5895
> 7.49900
> 1406
> 1575
> 2019
> 2.31
> 5.4796
> 1.83
> 7.8295
> 1.8495
> 28.609300
> 1489
> 1479
> 2020
> 2.55
> 5.7696
> 2.70
> 14.05%6
> 2.99%
> 48.76930
> 1534
> 1417
> 2021
> 3.01
> 4.6490
> 3.88
> 20.81%
> 5.35%
> 89.78900
> 1480
> 1531
> 2022
> 2.18
> 3.8796
> 2.12
> 11.839
> 2.52%
> 61.22930
> 1478
> 1572
> 2023
> 8.82
> 3.2996
> 16.07
> 41.4995
> 0.4495
> 251.88900
> 1418
> 1648


**我想请教以下几个问题：**

1）这个 alpha 是基于我使用论文中提到的变量构建的新想法，但我整个表达式都和原文不同。这样的 alpha 是否值得推荐？

2）这个 alpha 的回报略有下降。我给你看一下在哪个地方：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> Pnl
> 5OOOK
> 40OOK
> 300OK
> Z,0OOK
> OOOK
> Jul'18
> Jan '19
> Jul '19
> Jan '20
> Jul'20
> Jan '21
> Jul'21
> Jan '22
> Jul '22
> Jan '23


虽然最后一年交易期回报下降，我仍然相信它在 OS 表现会很好，因为在5年回测期间没有出现大幅亏损。这种情况下是否还推荐提交这个 alpha？

3）对于观看我帖子的顾问们，你们可以尝试将这个 alpha 应用于不同地区/中性化方法/股票池吗？我目前还是一名 conditional consultant，但我非常好奇这个 alpha 在其他国家以及不同慢因子中性化和股票池中是否表现更好。

感谢你阅读我的帖子！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
推荐提交的

平台数据跟论文使用数据不一定完全相同，计算方式，逻辑等底层架构也未必相同。基于相同思路进行衍生是一个很好的方法！

至于因子为什么有效，这个需要进行额外研究了，粗略看下来是关注了amihud和2月前的amihud变化，推测是买入一些流动性相比之前更好的标的？毕竟amihud是个 反向指标，指标越大流动性越差。

另：表达式里面的数值参数可以删除，大家都乘等于大家都不乘。

（个人拙见，欢迎讨论）


---

### 技术对话片段 37 (原帖: 【Alpha灵感】从一个简单的概念（组平均差）开始理解到底什么是模版，进而尝试做出自己的模板Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】从一个简单的概念组平均差开始理解到底什么是模版进而尝试做出自己的模板Alpha Template_32394129497239.md
- **时间**: 1年前

**提问/主帖背景 (LL87164)**:
**概述：** 从一个非常容易理解的概念，一步步摸索到底什么是模版、它该长什么样，进而尝试着做出一个属于自己的模版。

**来源：** 双周例会上Kunqi老师的一个分享，组平均差，这是一个一看就懂很容易理解的概念。 
> [!NOTE] [图片 OCR 识别内容]
> Template Ideas
> Idea 1: 组平均差
> Base
> 二
> datafield
> 
> group_mean(datafield, group)
> Idea 2: 时间的导数
> 时间零阶导是位移(Distance)
> datafield
> 时间一阶导是速度(Velocity)
> ts_delta( datafield, days
> 时间二阶导是加速度(Acceleration)
> +
> ts_delta(ts_delta( datafield, days ), days)
> Example:
> 原始时间序列t: [1,2,4,7,9,10]
> td
> 二
> ts_delta(t;,1):
> [1,2,3,2,1]
> tdd = ts_delta(td, 1):
> [1,1,-1,-1


**最初想法：** 开始只是想尝试一下看看这么简单的一个想法能有什么效果，最初的思路是：

```
## 组平均差模版# 组平均差先跑一阶# 然后再跑标准二阶（或标准一阶）alpha = f"""({datafield} - group_mean({datafield}, log(ts_mean(cap, 21)), {groupfild}))"""
```

在 group_mean 上 **冒出个想法** ，是因为正好在看  [模板的拓展——以CAPM模型的思路为例]([L2] Machine Alpha 基础知识5模板的拓展以CAPM模型的思路为例_25329078901911.md)  ，其中提到了“选择log(ts_mean(cap, 21))进行加权，以防止大公司扭曲组平均值，同时也平滑了cap”，于是借鉴了过来。

**回测过程：** 在目前正在做的region上挑了一个数据集，基于以上想法先把“组平均差”当一阶去跑，看到有信号，于是跑标准二阶（group_op）。最后从中挑出一个，希望对组合在 margin 上能有贡献。

**
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS
> Summary
> Period
> IS
> 0S
> Theme: Power Pool Alphas Theme X2.5
> 自
> Power Pool Alpha
> Pyramid theme: EURIDIIPV X1
> Pyramid theme: EURIDIIANALYST X1.5
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.27
> 1.269
> 0.99
> 7.579
> 8.499
> 119.7290。
**

整个过程总结下来，有以下 **几点体会：**

1. 可以把“ *最初的简单想法”* 当成一个 0 阶模版，或者假设成新组了个数据集，在此基础上去套用自己熟悉的标准的一二三阶模板。

2. 标准的一二三阶顺序上可以灵活处理，我是跳过了一阶直接套二阶后就交了。主要是想降一下当前平均操作符的数量。目前还没有尝试这一步去跑 ts_op 或 trade_when 等其他操作，但值得继续尝试。

3. 在不断尝试和回测的基础上，直接抽象成一个新的模版：

```
alpha = f"""sinal = ({datafield} - group_mean({datafield}, log(ts_mean(cap, 21)), {groupfild_1}));group_neutralize(signal, densify({groupfild_2}))"""
```

或者在此基础上继续做进一步的 **拓展：** 把 group_neutralize 抽象成 {group_op} ，或者换成 {ts_op} ，再或加调仓判断 trade_when 或横截面回归 vector_neut，或先做 {ts_op} 再做 {group_op} 等等。

但最终提交用的是 group_neutralize ，按 subindustry 做的行业中性化。想一下这也是有背后的意义的。

**关于具体应用：** 建议是根据具体情况做调整，比如到底是一次性跑完遍历好还是拆分开分阶段跑。个人经验是分开跑好一点，做相关性剪枝后再跑下一轮，这样效率更高一点。如果前一轮性能指标不理想，直接换数据集。

总之，把它当成是一个探索生成新模版的过程。希望再看论坛模版大师里前辈的作品时，能够找到点感觉。也希望对像我这样的新手能有所启示和帮助。

最后，再次感谢Kunqi老师的分享和一对一的指导。写帖子的过程中，感觉有些点对自己也是一个新的认知和提升。祝大家 VF 步步高，Genius 早日 GM！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
点赞！！！很好的实践思路。


---

### 技术对话片段 38 (原帖: REGRESSION VARIABLES)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【Alpha灵感】短期现金回报率对股票价格的影响_29092280236567.md
- **时间**: 1年前

**提问/主帖背景 (YZ92137)**:
灵感来源： [《PRODUCTIVITY OF SHORT TERM ASSETS AS A SIGNAL OF FUTURE STOCK]([链接已屏蔽])  [PERFORMANCE 》]([链接已屏蔽])

- Alpha 核心思路

短期的现金回报率有超额收益

- Alpha关键公式


> [!NOTE] [图片 OCR 识别内容]
> Tit
> 一
> R = Q + Y1ACashit + Y2AEarningsit + ?3AAssetsit +
> 十 Eit
> 其中,
> Nit 是公司'在时间 t 的股票回报,
> Rt 是无风险利率, ACashit: AEarningsit 及其他项捕
> 捉贝务指标的娈化。



> [!NOTE] [图片 OCR 识别内容]
> ACashit
> Eamingsit
> Y2
> (Assetsit
> Cashit)
> Ag&DFpenseit
> Y3
> Y4
> Interest Expenseit
> ADividends
> Y5
> YG
> NIt-I
> NIt-1
> Mt-1
> MIt-I
> Paidit
> MIt-1
> Nt-1


- Alpha实现思路

1 因为文中多次提到以月为单位（点题短期），所以Alpha的时间周期基本就是d=20

2 从公式看到实际是要回归短期的股票回报率和现金之间的关系，股票回报率通过20天跨度的close进行计算得到

3 因为里面提到了是选择了的标的，排除了金融行业的股票，简单来说就是进行了分组，尝试了sector，industry和subindustry，industry效果相对较好，可能是里面有金融大类的划分？

4 因为是短期的数据，但是很多cash等财报类的数据的从逻辑上考虑就是季度更新，所以要进行填值操作，有没有对nan的处理，效果差别相当大

5 因为原文写了要用现金回报率进行排序，那我就选了group_rank，另外在S&P500上效果最好，我就选了用cap分组

- Alpha setting


> [!NOTE] [图片 OCR 识别内容]
> LANGUAGE
> INSTRUMENT TYPE
> Fast Expression
> Equity
> REGION
> UNIVERSE
> DELAY
> USA
> TOP3000
> 1
> NEUTRALIZATION
> DECAY
> TRUNCATION
> Industry
> 0
> 0.05
> PASTEURIZATION
> UNIT HANDLING
> NAN HANDLING
> TEST PERIOD
> On
> Verify
> On
> 1
> YEARS
> MONTHS
> Save as Default
> Apply


- Alpha performance, Sharpe>1.3, turnover<50%, return>8%, fitness>0.7, pro-corr<0.65
- 增强Alpha的信号，以及其他不同的探索与尝试
- 可提交的版本

d = 20;

M = ts_delay(cap,d);

r = ts_delta(close,d);

y1 = power(ts_delta(cashflow, d),2)/ts_delay(M, d);

alpha = ts_regression(r,y1,600);

group_rank(-alpha, bucket(rank(cap),range="0,1,0.1"))


> [!NOTE] [图片 OCR 识别内容]
> 医 Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run:
> C V
> Prod Correlation
> Maximum
> Minimum
> Last Run: Sun, 01/05/2025,9:43 AM
> ?
> 0.6373
> -0.4249
> 1M
> 訾
> 1OK
> IT
> 晷
> 8
> 100
> 0'
> 6
> 0
> 0*
> 0
> 0:
> -0.9
> -0.8
> 8
> -0.5
> -0.4
> 0.2
> 0.4
> 0.5
> 0.6
> 0.7
> 0.8
> 0.9
> 1.0
> 令
> -0.3
> -0.2
> 0.0
> 0.3
> -0.1
> 0.1
> 0.4..
> 0.7..
> 0.9..
> 0.0..
> 0.2.
> -0.4...
> 3
> 0.5.
> 0.8
> -0.1 _
> 5
> -0.2..
> -1.0.
> -0.9.
> -0.7 
> -0.5.
> -0.3



> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> IS
> 0S
> Pyramid theme: USAIDI/Price Volume X1
> Pyramid theme: USAIDIIFundamental X1.1
> Pyramid theme: USA/DI/Earnings X1.2
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.73
> 23.939
> 2.48
> 19.809
> 3.069
> 16.5496o0
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2012
> 7.68
> 22.4696
> 6.68
> 17.009
> 0.379
> 15.149600
> 1481
> 1583
> 2013
> -1.09
> 21.729
> -0.38
> -2.60%
> 3.2396
> -2.399600
> 1498
> 1592
> 2014
> 3.87
> 21.0696
> 2.85
> 11.4696
> 1.72%
> 10.889600
> 1505
> 1592
> 2015
> 0.78
> 22.159
> 0.26
> 2.529
> 2.4796
> 2.289600
> 1524
> 1612
> 2016
> 2.85
> 21.80%
> 1.79
> 8.609
> 3.0296
> 7.899600
> 1538
> 1590
> 2017
> 0.81
> 22.409
> 0.25
> 2.0596
> 1.559
> 1.839600
> 1517
> 1583
> 2018
> 1.94
> 22.209
> 1.00
> 5.909
> 2.349
> 5.329600
> 1519
> 1599
> 2019
> 0.89
> 23.279
> 0.32
> 3.0596
> 3.429
> 2.639600
> 1524
> 1578
> 2020
> 0.71
> 26.459
> 0.32
> 5.469
> 5.029
> 4.139600
> 1526
> 1574
> 2021
> 3.29
> 25.949
> 3.21
> 24.69%
> 3.379
> 19.049600
> 1525
> 1626
> 2021
> 2.59
> 22.319
> 2.19
> 15.959
> 2.8396
> 14.309600
> 1538
> 1606
> 2022
> 2.86
> 25.379
> 2.74
> 23.219
> 3.069
> 18.309600
> 1566
> 1566
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2.06
> 23.939
> 0.92
> 4.749
> 1.189
> 3.96900
> Year


- Alpha的模板

```
    for d in days:        for group_ops in group_ops_list:            for group in groups:                alpha = f"""d = {d};M = ts_delay(cap,d);r = ts_delta(close,d);y1 = power(ts_delta(cashflow, d),2)/ts_delay(M, d);alpha = ts_regression(r,y1,750);{group_ops}(-alpha, densify({group}))"""
```

- **Alpha模板的产能**

**搜索了2万个大概，产生了2个alpha，后面想再改个模板试试，已经没权限了。。。。**

- **Alpha的稳健性检查**

**d=10,20,30均有尝试，都有信号，随着时间增加递减，为了在其他region中方便尝试，都尽量用了比较通用的字段，发现其他region很多也有信号。**

- Alpha在其他region的表现

在ASI，GLB，EUR，CHN都有信号，但是普遍比USA的弱，没有简单找到alpha，现在没权限了，可能要换个路试试。

- 探索该Alpha遇到的困难

实际上这篇论文还有一部分公式和内容如下，逻辑上讲这篇文章主要说把股票的回报分为现金汇报和非现金汇报，上面我理解只是找到了现金回报的部分，还要再去掉非现金汇报的部分，才完美，不过我根据下面的公式做了一些尝试，效果没有很好，可能是我哪里搞错了。希望大家能完善。


> [!NOTE] [图片 OCR 识别内容]
> Cash
> Holdingstzl
> Y8
> Leverageit
> (Total Debtit + Mt-I )
> Mt -I ` ACashit
> Yg
> Lagged Total
> + MIt-I
> Y10
> M_
> Leverggeit_
> ACashit
> Y11
> IIt-1
> Debtit
> Mt
  
> [!NOTE] [图片 OCR 识别内容]
> 回归使用普通最小二乘法 (OLS) 进行估计,
> 系数用于计算现金的边际价值。
> 具体地, 现金的边际价
> 值为:
> Cash Holdt-I
> Marginal Cash Value =
> Q 十 Y7
> Y8
> Leverageit
> 平均现金值通过将边际现金值乘以当前的现金持有量来获得。最后。每月的现金回报 bit 通过以下公
> 式计算:
> Average Cash Valuet
> Average Cash
> bit
> Average Cash Valuet-I
> 这种方法使我们能够量化现金持有及其他贝务指标对公司超额回报的贡献。同时考虑公司规模和杠杆
> 效应。为了减少极端值的影响,
> 我们对现金回报分布进行了 winsorization , 设定了在第1和第 99
> 百分位的阈值。
> Winsorization 能够减少异常值的影响,
> 同时保留数据的结构,
> 确保信号计算的稳健
> 性
> Mt-I
> Valuetzl


附原文代码参考：

def calculate_b_it(company):
    data = company.copy()
    data['market_cap_t_minus_1'] = data['market_cap'].shift() # paper uses M_{t-1} for the denoms
    data['leverage'] = data['total_debt'] / (data['total_debt'] + data['market_cap'])

    # Y VALUES
    data['r_minus_R'] = data['stock_return'] - data['rf_rate']

# REGRESSION VARIABLES
    data['gamma_1'] = (data['cash_holdings'].diff()) / data['market_cap_t_minus_1']
    data['gamma_2'] = (data['earnings'].diff()) / data['market_cap_t_minus_1']
    data['gamma_3'] = ((data['total_assets'] - data['cash_holdings']).diff()) / data['market_cap_t_minus_1']
    data['gamma_4'] = (data['rd_expense'].diff()) / data['market_cap_t_minus_1']
    data['gamma_5'] = (data['interest_expense'].diff()) / data['market_cap_t_minus_1']
    data['gamma_6'] = (data['dividends_paid'].diff()) / data['market_cap_t_minus_1']
    data['gamma_7']= data['cash_holdings_t_minus_1'] / data['market_cap_t_minus_1']
    data['gamma_8'] = data['leverage']
    data['gamma_9'] = (data['total_debt'].diff() + data['market_cap_t_minus_1'].diff()) / (data['total_debt'].shift() + data['market_cap_t_minus_1'].shift())
    data['gamma_10'] = (data['market_cap_t_minus_1'] * (data['cash_holdings'].diff())) / (data['market_cap'] ** 2)
    data['gamma_11'] = (data['leverage'] * (data['cash_holdings'].diff())) / data['market_cap']

    data = data.dropna()

    y = data['r_minus_R']
    X = data[['gamma_1', 'gamma_2', 'gamma_3', 'gamma_4', 'gamma_5', 'gamma_6', 'gamma_7', 'gamma_8', 'gamma_9', 'gamma_10', 'gamma_11']]

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    data['marginal_cash_value'] = (
        model.params.iloc[0] +
        (model.params.iloc[10] * (data['cash_holdings_t_minus_1'] / data['market_cap_t_minus_1'])) +
        (model.params.iloc[11] * data['leverage'])
    )

    data['average_cash_value'] = data['marginal_cash_value'] * data['cash_holdings']

    company['b_it'] = data['average_cash_value'].pct_change()  # monthly cash return

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的帖子，点赞！

此外，想问一下，你有没有尝试过用其他描述财务状况或者基本面状况的字段代替cashflow？我看你的模版核心就是不同的operator轮换，换cashflow字段或许是个办法？我不太确定


---

### 技术对话片段 39 (原帖: 【genius】如何在 Genius 级别范围内获得更高的季度付款)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【genius】如何在 Genius 级别范围内获得更高的季度付款_33037373635223.md
- **时间**: 1年前

**提问/主帖背景 (ZX58901)**:
### 如何在 Genius 级别范围内获得更高的季度付款

在 Genius 级别范围内，季度付款金额由 **weight（权重） **和** value factor（价值因子）** 共同决定，二者影响付款金额在该级别最大与最小范围之间的具体数值。其中，value factor 每 4 至 6 周更新一次，用于计算季度付款的 value factor 会在季度结束后 4 至 56 周内显示。

关于不同时间段提交的 Alphas（咨询顾问的相关成果或指标）及其对应的付款计算规则如下：

1. **2024 年第四季度（Q4 2024）提交的 Alphas**
   - 决定咨询顾问在 2025 年第一季度（Q1 2025）所处的 Genius 级别。
   - 该季度的季度付款将基于 ** 旧计算方法（不含 Genius 级别因素）** 计算。
   - value factor 将按常规周期在 Q1 2025 更新。
2. **2025 年第一季度（Q1 2025）提交的 Alphas**
   - 咨询顾问的季度付款将根据其 Q1 2025 的 Genius 级别计算。
   - 对应的 value factor 将于 2025 年第二季度（Q2 2025）更新。

简而言之，Genius 级别的季度付款金额受权重和价值因子动态影响，不同季度提交的 Alphas 将关联不同计算周期的规则，需关注 value factor 更新时间及级别对应的计算方式。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的帖子，感谢分享，点赞！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！11


---

### 技术对话片段 40 (原帖: 【op深度研究系列】signed_power)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【op深度研究系列】signed_power_31919170562839.md
- **时间**: 1年前

**提问/主帖背景 (DZ31817)**:
受到上次论坛GM大佬帖子中根据不同op的非线性程度进行剪枝的启发，感觉有必要对不同的op进行更深入的研究。这次研究一下比较常用的signed_power。此文的图表在AI协助下完成。

首先，从signed_power函数的定义和图像看，我们的第一印象就是这个op可以用来放大（指数p>1）或抑制（指数p<1）信号。在p逼近1时，op操作后的结果近似原信号。以下是指数为2、0.5、1.01时的图像，比较直观。


> [!NOTE] [图片 OCR 识别内容]
> Graph ofy = signed_power(x, 2)
> y = signed_powerlx, 2)
> 1
> -3
> 一2.0
> -1.5
> 一1,0
> -0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0



> [!NOTE] [图片 OCR 识别内容]
> Graph ofy = signed_power(x, 0.5)
> 1.5
> y = signed_power(x, 0.5)
> 1.0
> 0.5
> 0.0
> 一0.5
> 一1.0
> 一1.5
> 一2.0
> 一1.5
> 一1.0
> 
> 0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> X



> [!NOTE] [图片 OCR 识别内容]
> Graph ofy
> 二
> signed_power(x; 1.01)
> 2.0
> y = signed_power(x, 1.01)
> 1.5
> 1.0
> 0.5
> 0.0
> -0.5
> 一1.0
> 一1.5
> 一2.0
> ~2.0
> 一1.5
> 一1.0
> 一0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> X


接下来，我让AI在对p在0-10之间取值，画出图像，直观感受不同指数值的放大或抑制效果。这里我们又可以获得一个新信息，当原信号在-1到1的范围时，p>1和p<1的放大和抑制效果是相反的。

更具体地说：

- **当 p>1** 时，
  大数被放得更大，小数被压得更小，
  —— **放大强信号、削弱弱信号** ，增加分化。
- **当 0<p<1**  时，
  小的数变得更大，大的数变得更小，
  —— **抑制强信号、提升弱信号** ，让信号变得更均匀。


> [!NOTE] [图片 OCR 识别内容]
> Graph ofy = signed_power(x, p) for pin [0,10]
> p=0.1
> p=0.3
> p=0.5
> p=0.7
> p=l.5
> p=2
> 2
> p=l0
> 0
> 一2
> 一4
> 2.0
> 一1.5
> 1.0
> -0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> p=1
> p=3
> =5


到这里，我想看看这个op对原信号分布会产生什么影响，于是让AI生成了两组原始信号数据，分别为均匀分布和正态分布，对两组数据应用p分别为0.5、1、2的signed_power操作后，分布变化如下：

均匀分布观察：

- p=0.5（平方根）时，弱信号（接近0）被放大，极端值（接近±2）被压缩，中间区域的密度高了；
- p=1 是原始信号，不变；
- p=2（平方）时，强信号被进一步拉远，弱信号更集中在0附近，极端分化明显。


> [!NOTE] [图片 OCR 识别内容]
> Signal after signed_power(x, 0.5)
> Signal after signed_power(x, 1)
> 30
> p=0.5
> 40
> 25
> 30
> 20
> 
> 20
> 
> 15
> U
> 10
> 10
> 5
> 0
> 一1.5
> 一1.0
> -0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 一2.0
> 一1.5
> 一1.0
> -0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> Transformed Value
> Transformed Value
> Signal after signed_power(x, 2)
> Original Signal
> 30
> Original
> 70
> 25
> 60
> 50
> 20
> 
> 40
> 
> 15
> 9
> 30
> 10
> 20
> 5
> 10
> 一4
> -3
> 一2
> 一1
> 0
> 1
> 2
> 3
> 一2.0
> 一1.5
> 一1.0
> 一0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> Transformed Value
> Value
> p=l
> p=2


正态分布观察：

- **原始正态分布** ：标准的钟形曲线，高峰、厚尾；
- **p=0.5** ：
  - 平均数值被“拉近0”，
  - 两边尾部（极大、极小值）被大幅压缩，
  - 分布在靠近0的位置被分开变宽。
- **p=1** ：
  - 保持原样，仍是标准正态分布。
- **p=2** ：
  - 尾部信号被放大（极大极小值更大了），
  - 中间信号（靠近0）被进一步压缩，
  - 分布变得更加尖锐陡峭。


> [!NOTE] [图片 OCR 识别内容]
> Normal Signal after signed_power(x, 0.5)
> Normal Signal after signed_power(x, 1)
> 40
> P=0.5
> 50
> p=l
> 35
> 40
> 30
> 25
> 30
> 
> 20
> 
> 20
> 15
> 10
> 10
> 5
> -1.5
> 一1.0
> -0.5
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> 一3
> 一2
> 一1
> 0
> 2
> 3
> Transformed value
> Transformed Value
> Normal Signal after signed_power(x, 2)
> Original Normal Signal
> 250
> 50
> Original
> 200
> 40
> 150
> 30
> 
> 100
> 
> 20
> 50
> 10
> 一10
> -5
> 0
> 5
> 10
> 15
> 3
> 一2
> 0
> 3
> Transformed Value
> Value
> p=2


再让AI画一下正态分布信号的均值、方差、偏度、峰度随不同p的变化：


> [!NOTE] [图片 OCR 识别内容]
> Mean Vs p
> Standard Deviation Vs p
> 0.004
> 3.5
> 0.003
> 0.002
> 3.0
> 0.001
> 吾
> 2.5
> 量
> 忌
> 0.000
> 2.0
> -0.001
> 1.5
> 一0.002
> 1.0
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> 2.5
> 3.0
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> 2.5
> 3.0
> p
> p
> Skewness Vs p
> Kurtosis Vs p
> 0.8
> 30
> 25
> 0.6
> 20
> 
> 0.4
> 
> 15
> 簋
> 10
> 0.2
> 5
> 0.0
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> 2.5
> 3.0
> 0.0
> 0.5
> 1.0
> 1.5
> 2.0
> 2.5
> 3.0
> p
> p


- **均值 (Mean)** ：
  - 大致随着 p 增大而略有偏移（因为正负值的非对称拉伸效应）。
- **标准差 (Standard Deviation)** ：
  - 随 p 增大而快速上升，
  - 说明信号的整体波动变大了（尤其极端值被拉远）。
- **偏度 (Skewness)** ：
  - 原始正态分布是近似0偏度，
  - 但经过 signed_power 后，小的 p 稍微负偏，大的 p 稍微正偏。
- **峰度 (Kurtosis)** ：
  - 随 p 增大而明显上升，
  - 高峰度表示：更多极端值、更尖锐的分布（“肥尾”效应加强）。

**最后让AI总结一下规律：**

p 取值范围
变换后效果

0<p<1
压缩极端，提升中间信号，分布更平，尾部更短

p=1
不变

p>1
强化极端，抑制中间信号，分布更尖，尾部拉长

###

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有意思的研究，点赞。我已经把signpower与四个降turn运算符一起列入二阶后的提升方式了。

对于signpower的参数选择，我认为0.5和2尚且是有意义的参数，如果一定要能到提交的程度，我之前跳过1.0469类似的参数，很有过拟合的嫌疑，也没有交。好消息是现在ppa常驻之后，差一点点的因子也能交流。


---

### 技术对话片段 41 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【OSMOSIS新人友好版】真正的一键打分指定区域清空补齐10类标签过滤_39408397746199.md
- **时间**: 2个月前

**提问/主帖背景 (BQ64903)**:
前几天看到  **[XX42289](/hc/en-us/profiles/14187300941847-XX42289)**   [【课代表】【轻松点击即可完成参赛】CA 降维 + 多指标聚类数评判 + KMeans / 层次 / DBSCAN 聚类的 Osmosis 点数分配工具 – WorldQuant BRAIN]([L2] 【课代表】【轻松点击即可完成参赛】CA 降维  多指标聚类数评判  KMeans  层次  DBSCAN 聚类的 Osmosis 点数分配工具经验分享_37023499938327.md) 和 [顾问 JR23144 (贺六浑) (Rank 6)](/hc/en-us/profiles/28844048981143-顾问 JR23144 (贺六浑) (Rank 6))  [【贺六浑】-【工具配置】OC2025 一键清空分数脚本 – WorldQuant BRAIN]([L2] 【贺六浑】-【工具配置】OC2025 一键清空分数脚本经验分享_37090321198359.md) 的文章。发现一些细节不足：

1. 清除分数会将所有区域清除，且不包含super alpha
2. 分配分数时四舍五入的偏差并没有通过API更新
3. 分类结果可能小于10类，不满足打分标准

所以在此做了略微改进，主要在于：

1. 给指定区域打分前先清空该区域所有分数（包括super alpha）
2. 通过API更新四舍五入的偏差
3. 不足十类的，给其他alpha赋值1，强行满足要求
4. 支持通过颜色/tag筛选要打分的alpha（这样可以把AI提交的烂alpha排除出去）

```
# # 清空# In[1]:# -*- coding: utf-8 -*-import urllib.parseimport loggingimport numpy as npimport pandas as pdfrom sklearn.preprocessing import StandardScaler, RobustScalerfrom sklearn.cluster import KMeans, DBSCAN, AgglomerativeClusteringfrom sklearn.metrics import silhouette_score, calinski_harabasz_scorefrom sklearn.decomposition import PCA# 假设该库返回requests.Session对象#from machine_lib import login  from ace_lib import (    start_session )import timefrom datetime import datetime, timedelta#from machine_lib import *  # 假设 login() 在这里from concurrent.futures import ThreadPoolExecutorimport json# In[2]:# ===================================================================# PART 1: 配置与函数定义# ===================================================================#  并发清除操作的线程数MAX_WORKERS = 10def up_alpha_properties_to_clear(s, alpha_id: str, old_osmosisPoints: str):    """    一个专门用于清除 Alpha 分数的函数。    它通过将 'osmosisPoints' 字段设置为 null 来实现。    """    params = {"osmosisPoints": None}  # 在 requests 中, None 会被序列化为 JSON null    response = s.patch(        f"[链接已屏蔽] json=params    )    if response.status_code == 200:        print(f"成功清除 Alpha {alpha_id} 的分数 (原分数: {old_osmosisPoints})。")        return "SUCCESS"    else:        print(f"清除 Alpha {alpha_id} 分数失败，状态码: {response.status_code}, 信息: {response.text}")        return "FAILED"def get_colored_alphas_in_date_range(s, start_date, end_date, region, alpha_num_limit=1000):    """    获取在指定日期范围内，所有设置了分数的Alpha。    """    colored_alphas = []    print(f"开始查找从 {start_date} 到 {end_date} 所有已设置分数的常规 Alpha...")    for i in range(0, alpha_num_limit, 100):        print(f"正在扫描第 {i} 到 {i + 100} 个 alpha...")        # 【重要】在 URL 中加入了 dateSubmitted 过滤器        url_e = (            f"[链接已屏蔽]            f"&status!=UNSUBMITTED&status!=IS_FAIL&hidden=false"            f"&dateSubmitted>={start_date}T00:00:00-04:00"            f"&dateSubmitted<{end_date}T00:00:00-04:00"            f"&settings.region={region}"          )        try:            response = s.get(url_e)            response.raise_for_status()            alpha_list = response.json().get("results", [])            if not alpha_list:                print("已扫描完所有符合条件的 Alpha。")                break            # 在客户端筛选出有分数的 Alpha            for alpha in alpha_list:                if alpha.get("osmosisPoints") is not None:                    record = {                        "id": alpha["id"],                        "osmosisPoints": alpha["osmosisPoints"]                    }                    colored_alphas.append(record)        except Exception as e:            print(f"获取alpha时发生异常: {e}")            resp = s.get('[链接已屏蔽])            if resp.status_code != 200:                print(f"用户会话可能已过期，状态码: {resp.status_code}")            break    print(f"\n查找完毕！共找到 {len(colored_alphas)} 个在指定日期内需要清除分数的 Alpha。")    return colored_alphas# In[3]:def get_history_alpha_ids(s, region, start_date, limit=50, offset=0, exclude_tags=None, exclude_color=None):    """    从接口分页获取指定地区、指定日期后的alpha数据    :param s: requests.Session对象，已完成登录的会话    :param region: 地区大写：USA, EUR ... ...    :param start_date: 过滤日期，获取该日期之后的因子    :param limit: 每页获取的数量    :param offset: 分页偏移量    :return: 包含alpha的id和各类is指标的列表    """    alphas_data = []    # 对日期字符串进行URL编码，避免特殊字符影响请求    start_date_str = urllib.parse.quote(start_date.astimezone().isoformat(timespec='seconds'))    # 分页获取数据    #去掉color为红的    while True:        url = (            f"[链接已屏蔽]            f"limit={limit}&offset={offset}"            f"&dateCreated%3E={start_date_str}"            f"&settings.region={region}"            f"&status!=UNSUBMITTED%1FIS-FAIL"            f"&hidden=false"            f"&order=-dateSubmitted"            f"&color!={exclude_color}"            f"&tag!={exclude_tags}"        )        try:            resp = s.get(url)            if resp.status_code != 200:                print(f"请求出错，状态码：{resp.status_code}")                break            data = resp.json()            results = data.get("results", [])            alphas_data.extend(results)            # 判断是否获取完所有数据，是则退出循环            if offset + len(results) >= data.get("count", 0) or len(results) < limit:                break            offset += limit        except Exception as e:            print(f"数据获取异常，异常信息：{e}")            break    # 提取需要的指标数据    alpha_metrics = []    for item in alphas_data:        # 检查is中的关键指标是否存在，避免键缺失报错        is_data = item.get('is', {})        metrics = {            'id': item['id'],            'fitness': is_data.get('fitness', 0.0),            'longCount': is_data.get('longCount', 0.0),            'shortCount': is_data.get('shortCount', 0.0),            'turnover': is_data.get('turnover', 0.0),            'returns': is_data.get('returns', 0.0),            'drawdown': is_data.get('drawdown', 0.0),            'margin': is_data.get('margin', 0.0),            'sharpe': is_data.get('sharpe', 0.0)        }        alpha_metrics.append(metrics)    if not alpha_metrics:        print("错误：没有获取到有效的alpha数据")        return []    return alpha_metricsdef determine_clusters_multi_criteria(X, min_clusters=5, max_clusters=50):    """    多指标确定聚类数（结合轮廓系数、CH指数，同时限制聚类数范围）    :param X: 标准化后的特征数据    :param min_clusters: 最小聚类数（避免过少）    :param max_clusters: 最大聚类数（避免过多）    :return: 最终聚类数量    """    if len(X) <= min_clusters:        return len(X)  # 样本数少于最小聚类数时，取样本数    # 限制聚类数范围：2 ~ 样本数（但不超过max_clusters，不低于min_clusters）    cluster_range = range(max(2, min_clusters), min(max_clusters + 1, len(X)))    scores = []    for k in cluster_range:        kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')        labels = kmeans.fit_predict(X)        # 轮廓系数：衡量聚类紧密度和分离度，越接近1越好        sil_score = silhouette_score(X, labels)        # CH指数：数值越大表示聚类效果越好（类内紧密，类间分离）        ch_score = calinski_harabasz_score(X, labels)        # 综合得分（归一化后加权，可调整权重）        scores.append({            'k': k,            'sil': sil_score,            'ch': ch_score,            # 权重可调整，平衡轮廓系数和CH指数的影响            'composite': 0.4 * sil_score + 0.6 * (ch_score / 100000)        })    # 转换为DataFrame方便排序    score_df = pd.DataFrame(scores)    # 按综合得分降序排序，取第一个作为最佳聚类数    best_k = score_df.sort_values('composite', ascending=False)['k'].iloc[0]    # 兜底：确保聚类数在合理范围    best_k = max(min_clusters, min(best_k, max_clusters))    return best_kdef cluster_alphas_improved(alpha_metrics, use_pca=True, cluster_algorithm='kmeans'):    """    改进的聚类逻辑：支持PCA降维、多种聚类算法、多指标确定聚类数    :param alpha_metrics: alpha的指标数据    :param use_pca: 是否使用PCA降维（处理特征冗余）    :param cluster_algorithm: 聚类算法（kmeans/agglomerative/dbscan）    :return: 选中的alpha列表（每个聚类fitness最大）    """    # 转换为DataFrame方便处理    df = pd.DataFrame(alpha_metrics)    # 定义用于聚类的特征列    feature_cols = ['longCount', 'shortCount', 'turnover', 'returns', 'drawdown', 'margin', 'sharpe']    # 提取特征数据，处理缺失值（填充0）    X = df[feature_cols].fillna(0).values    # 改进1：使用RobustScaler标准化（抗异常值，比StandardScaler更适合金融数据）    scaler = RobustScaler()  # 替代StandardScaler，对异常值不敏感    X_scaled = scaler.fit_transform(X)    # 改进2：PCA降维（处理特征冗余，减少噪声）    if use_pca and len(feature_cols) > 2:        # 保留95%的方差，自动确定降维后的维度        pca = PCA(n_components=0.95, random_state=42)        X_processed = pca.fit_transform(X_scaled)        print(f"PCA降维后，特征维度从{len(feature_cols)}变为{X_processed.shape[1]}")    else:        X_processed = X_scaled    # 改进3：多指标确定聚类数（避免聚类数过少）    best_k = determine_clusters_multi_criteria(X_processed, min_clusters=5, max_clusters=50)    print(f"改进后确定的最佳聚类数量：{best_k}")    # 改进4：支持多种聚类算法（KMeans/层次聚类/DBSCAN）    if cluster_algorithm == 'kmeans':        # KMeans：适合球形分布，速度快        cluster_model = KMeans(n_clusters=best_k, random_state=42, n_init='auto')        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'agglomerative':        # 层次聚类：不假设球形分布，更灵活        cluster_model = AgglomerativeClustering(n_clusters=best_k)        df['cluster'] = cluster_model.fit_predict(X_processed)    elif cluster_algorithm == 'dbscan':        # DBSCAN：无需指定聚类数，自动识别密度聚类（适合非球形分布）        # eps和min_samples可调整：eps越大，聚类数越少；min_samples越大，聚类数越多        cluster_model = DBSCAN(eps=0.5, min_samples=5)        df['cluster'] = cluster_model.fit_predict(X_processed)        # DBSCAN的-1表示噪声点，单独处理为一个聚类        noise_cluster = df['cluster'].max() + 1        df.loc[df['cluster'] == -1, 'cluster'] = noise_cluster        best_k = len(df['cluster'].unique())        print(f"DBSCAN聚类后实际聚类数量：{best_k}")    # 每个聚类中选择fitness最大的alpha    selected_alphas = []    for cluster in df['cluster'].unique():        cluster_df = df[df['cluster'] == cluster]        # 取fitness最大的行        best_alpha = cluster_df.loc[cluster_df['fitness'].idxmax()]        selected_alphas.append(best_alpha.to_dict())    return selected_alphas# In[4]:# ===================================================================# PART 3: 主逻辑 (先清除该地区，再赋值)# ===================================================================if __name__ == '__main__':    # 1. 基础配置    target_region = "USA"     advisor_date_obj = datetime(2025, 12, 10)    advisor_date_str = advisor_date_obj.strftime("%Y-%m-%d")    page_limit = 100  # 每页获取的alpha数量    page_offset = 0   # 分页起始偏移量    session = start_session()    # --- A. 清除该地区既有分数 ---    # 计算日期范围 (参考你清除脚本的逻辑)    begin_date = advisor_date_str    end_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")    print(f"正在清除地区 {target_region} 在 {begin_date} 之后的既有分数...")    alphas_to_clear = get_colored_alphas_in_date_range(session, begin_date, end_date, target_region)    if alphas_to_clear:        with ThreadPoolExecutor(max_workers=10) as executor:            for alpha_data in alphas_to_clear:                executor.submit(up_alpha_properties_to_clear, session, alpha_data["id"], alpha_data["osmosisPoints"])    else:        print("未找到需要清除分数的 Alpha。")    # 获取alpha的指标数据    alpha_metrics_list = get_history_alpha_ids(        s=session,        region=target_region,        start_date=advisor_date_obj,        limit=page_limit,        offset=page_offset,        #exclude_tags=["TEST"],         exclude_color='RED'    )    # 校验数据是否有效    if not alpha_metrics_list:        print("程序终止：未获取到有效alpha数据")        exit(1)    # 执行聚类并选择每个类别中fitness最大的alpha    selected_alpha_list = cluster_alphas_improved(        alpha_metrics=alpha_metrics_list,        use_pca=True,        cluster_algorithm='kmeans'    )    # 校验聚类结果    if not selected_alpha_list:        print("程序终止：聚类后未选中任何alpha")        exit(1)# In[5]:# --- 1. 获取聚类领头羊 ---# selected_alpha_list 已经是每个聚类里 fitness 最大的一个selected_ids = {a['id'] for a in selected_alpha_list}# --- 2. 补齐逻辑：如果不足 10 类，从备选池里抓取 ---target_count = 10current_count = len(selected_alpha_list)if current_count < target_count:    # 找出那些没被选中的因子    remaining_alphas = [a for a in alpha_metrics_list if a['id'] not in selected_ids]    # 按 Fitness 排序，选出表现较好的作为凑数因子    remaining_alphas.sort(key=lambda x: x['fitness'], reverse=True)    # 计算需要补多少个    needed = target_count - current_count    # 注意：补齐数量不能超过备选池总数    fillers = remaining_alphas[:needed]    for f in fillers:        f['cluster'] = 'filler'  # 标记为凑数        selected_alpha_list.append(f)# 更新当前最终选中的数量final_selected_count = len(selected_alpha_list)print(f"最终入选因子数：{final_selected_count} (其中聚类领头羊：{current_count}，凑数因子：{final_selected_count - current_count})")# --- 3. 分数分配逻辑 ---# 分成两拨处理：核心因子 vs 凑数因子leaders = [a for a in selected_alpha_list if a['cluster'] != 'filler']fillers = [a for a in selected_alpha_list if a['cluster'] == 'filler']# 凑数因子总分 = 数量 * 1分filler_total_points = len(fillers)# 核心因子总分 = 100,000 - 凑数分leader_pool_points = 100000 - filler_total_points# 核心因子基础分（平分池子）leader_base_score = leader_pool_points // len(leaders)leader_remainder = leader_pool_points % len(leaders)# --- 4. 执行 API 更新 ---total_check = 0for i, alpha_info in enumerate(selected_alpha_list):    alpha_id = alpha_info['id']    # 判断分数    if alpha_info['cluster'] == 'filler':        final_score = 1    else:        # 如果是核心因子中的第一个，拿走余数        if alpha_id == leaders[0]['id']:            final_score = leader_base_score + leader_remainder        else:            final_score = leader_base_score    print(f"Alpha {alpha_id} | Fitness值：{alpha_info['fitness']} | 类型: {alpha_info['cluster']} | 分配分数: {final_score}")    # 执行更新    update_url = f"[链接已屏蔽]    session.patch(update_url, json={"osmosisPoints": final_score}) # 确认无误后再取消注释    total_check += final_scoreprint(f"\n分配总计：{total_check} 分 (目标 100,000)")
```

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用，很赞

后续的改进思路：对ra和sa的赋分有个上限，比如设置一下，sa给三万分，或者几万分，就可以自动区分开了

=========================================================================

告诉你个秘密，其实我是游戏王

=========================================================================


---

### 技术对话片段 42 (原帖: 【SuperAlpha灵感】因子择时模型Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】因子择时模型Alpha Template_32553007626007.md
- **时间**: 1年前

**提问/主帖背景 (YW93864)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
用处很大，感谢分享！！！


---

### 技术对话片段 43 (原帖: 【SuperAlpha灵感】连续几天SA60刀的秘诀？经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【SuperAlpha灵感】连续几天SA60刀的秘诀经验分享_33316845356439.md
- **时间**: 1年前

**提问/主帖背景 (SZ83096)**:
今天是第4天了吧，对于为啥连续几天SA 都拿满60刀，我自己也挺困惑的。说说我的SA 怎么做的吧，小伙伴们应该感兴趣吧，我也不确定是不是正确的道路。

这个思路是我ACE主题（上周）最后几天手搓SA的时候，灵光一闪想到的。得益于游戏王的turnover分层思想，我一开始想着turnover分层的，但是ACE主题，turnover分层选择的结果不是很理想。看了learn的文档，尝试了下datacategories 分层，从我最熟悉datacategories开始尝试，试了下，效果挺好的。后面我尝试了不同datacategories的组合，可能是我选的datacategories 表现比较好，组合起来都挺不错的。

昨天 7月7号的SA 选择的思路

```
1、我先看看主题和🔝的这个datacategories 有多少alpha，然后我给datacategories 限制条件，比如op，turnover，prod，设置个大概的范围，看这个datacategories有多少，然后决定要不要再更细致的分层。这样完成了一个datacategories2、然后继续另一个独立的datacategories 设置，和第一个一样。3、最后2个或者2个以上的datacategories 加起来（|| 连接，）这样就相当于你保证选择了不同的datacategories 。
```

最后给大家看看最近4天的SA base吧


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 07/04/2025
> Super:
> 60.00
> Regular:
> 9.59
> Total:
> 69.59
> 40
> 20
> 2.Jul
> 3.Jul
> 4.Jul
> 5.Jul
> 6.Jul
> 7.Jul
> Period
> Regular
> Super
> Total


如果我的分享对你有帮助，记得点赞哦～～

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的分层思路！不过有一个小问题：橘子姐是按照什么思路，选取的category呢？有些数据类型之间可能会 存在共性，或者相关度较高，比如anl，fnd，ern，三者都是侧重于基本面的，可能重合度较大！是要选择较为类似的类型组合，还是要选差异较多的？

bytheway：分层方式还可以用longcount，hcac末尾我是用sqrt（long*short做的）


---

### 技术对话片段 44 (原帖: 【VF 0.9+顾问分享】新人常见误区之Under Fitting （欠拟合）经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的一篇文章，点赞

里面的函数大多可以在machinelib和acelib里面找到，也不乏需要魔改的地方。

我感觉最终形态应该是，输入一个alpha的id，单独留一个槽跑这个id所有可能性遍历（预计不会多，顶多5*10（粗略估计）），在抓取比较，选最号的提交


---

### 技术对话片段 45 (原帖: 【六维】Field Used & Operator Used 是每个季度重新统计吗？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【六维】Field Used  Operator Used 是每个季度重新统计吗_32984674254487.md
- **时间**: 1年前

**提问/主帖背景 (XC66172)**:
如题，因为这是我第一次参加的赛季不是很确定。如果我一季度使用了 ADD operator, DATAFIELD_1; 然后二季度再次使用了ADD operator, DATAFIELD_1, 这个在二季度的时候也会再次统计它们增加了Field Used, Operator Used这两个维度吗？

**顾问 worldquant brain赛博游戏王 的解答与建议**:
是的，但是要注意，alphadistribution那边是累积的所有数据。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。


---

### 技术对话片段 46 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【大角羊】2025SAC比赛ATOM第三分享请国区G2的兄弟们看过来希望我在ATOM中获得高分的经验给你们一些启发经验分享_33294035948311.md
- **时间**: 1年前

**提问/主帖背景 (AL13375)**:
相信很多人和我一样，虽然可以组出来加分的走势良好的super alpha，但是并不完全了解这样select和combo的作用，以及它的os表现会如何。所以大部分情况下，许多人要么是为了交sa而组sa，要么是为了调低prod来获取更高的base，只有少数人会去研究如何让自己组的sa在is表现良好的同时也可能在os表现依然出色。

在SAC比赛之前我并没有组过sa，所有组sa的经验都是这二十几天的经验，这期间我没有使用代码回测，每天都是手搓，也是收获了一些帮助优化sa的技巧。在此，要感谢weijie老师的帖子- [【有奖】SuperAlpha征文：分享你独到的selection和combination方法！]([Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md) 并且特别感谢游戏王 [worldquant brain赛博游戏王](/hc/en-us/profiles/26858512793111-worldquant brain赛博游戏王) 的经验分享：

```
(not(own)&& #选择不是自己的因子((turnover<0.07&&turnover>0.05)||(turnover<0.15&&turnover>0.13)||(turnover<0.12&&turnover>0.09))#按照turnover进行分层，每次选取不同的范围以保证每次选到的因子不同，提升多样性&&(operator_count<8)  &&(dataset_count<=2)  #限制op和pyramid个数，降低过拟合的概率&&(prod_correlation<0.5&&prod_correlation>0.1)  #按照prodcor筛选，0.5可以保证充分的分散化，0.1则是保证不选到奇奇怪怪的东西（一些厂或者极端的pnl）#以上为组合部分，以下为权重分配)/(turnover*s_log_1p(turnover)#按照turnover进行加权*sigmoid(self_correlation)*sigmoid(prod_correlation)#按照prodcor进行加权，为了防止权重变化过大，比如0.5和0.1权重差五倍，容易集中到一个因子上去*abs(long_count-short_count))#按照多空进行加权，对于多空平衡的因子赋予更高权重，可以避免选到偏多或者偏空因子
```

我组的sa的selection就是受这段表达式的启发的，游戏王大佬也是解释的很详细了。这种组sa的思路就是“ **择优而优** ”，因为选择的regular alpha比较优质，所以组的super alpha自然而然就会比较优质。

我就是用这个alpha加以调整在每个主题的多个region上提交了，并且分数都还可以，总分一直保持在百名左右，足以看到这个selection的强大之处！

至于combo，我一般常用的就三种：

1. 等权combo：1
2. 单combo_a表达式：combo_a(alpha,nlength=252,mode='algo1')（实测换成160效果也不错）
3. 多combo_a表达式：
   w1=combo_a(alpha,nlength=40,mode='algo1');
   w2=combo_a(alpha,nlength=160,mode='algo1');
   w3=combo_a(alpha,nlength=252,mode='algo1');
   signed_power(scale(w1)+scale(w2)+scale(w3),2)

这三种combo的作用机制区别很大，还有其他的combo的表达式的写法我试过但是is表现一般，就暂时没用了，但是建议大家多去尝试，找到最合适的。

最后一周了，祝愿大家可以在这一周做出好的alpha，成功逆袭，加油！VF1.0！！！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
nice，向al大佬学习！

生活就像海洋，只有意志坚强的人才能到达彼岸

this is an apple, i like apples,  apples are  good for my health


---

### 技术对话片段 47 (原帖: 3E large 3C less)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【提升Check Submission效率】本地计算自相关和提高check的tips效率提高10倍以上代码优化_28524742174359.md
- **时间**: 1年前

**提问/主帖背景 (XZ23611)**:
```
你的点赞和鼓励是我持续分享的动力！2025.04.08 更新  每日的pnl差值应该是diff而不是pct，感谢研究小组的各位大大们！现在可以做到和平台计算0差值【Check Submission都做什么？】
```

要提升效率首先要理解其背后的逻辑是什么！我粗略的把这个过程依次分为以下三个顺序：

1. **检查回测结果是否有FAIL** ，如果有FAIL这个过程会很快
2. **检查Self Correlation** ，这个速度就慢下来了，不过可以本地完成，后面会分享
3. **检查Prod Coorelation** ，无法本地完成，最耗时的步骤

```
【理解Check Submission的限流机制】
```

通过大量实践发现，我发现以下三个规律

1. 在一批check中，开始会很快，然后就变得异常慢，并开始出现check self/product correlation error 的超时情况
2. **所以我推测这个背后是有限流机制的** ，也就是说前XXX个相关性测试会是MAX Speed，单位时间内相关性的请求次数越多，就会降速。
3. Alpha中含有FAIL的情况，不会触发限流

虽然同时check的最大并发是3个，但由于限流机制的存在，并发并不会提高效率。

```
【如何提升效率？】
```

理解了限流机制后，那提升效率的大原则就出来了

1. **减少单位时间内的总的相关性的请求**
2. **对于需要请求的要进行优先级的排序**

具体的思路有以下几点：

**第一步: 利用prune剪枝函数，对于每个字段的最好的3个进行筛选, 再进行请求。这样做的好处有两个:**

1. 大量的相似alpha，如果最好的可以通过测试，可以先进行提交，这样后面的就可以不用再检查，或者可以在本地计算自相关性后排除（后面介绍方法）。
2. 如果PC相关性很高，则大概率后面的相关性也不容易降下来，那就放低优先级。

**第二步：进一步排除一些含有某些特定字段的alpha。**

1. 当我们做了几轮第一步后发现，有些特定字段的PC都在0.85以上了，那这里可以直接从list中暂且移除掉，连剪枝后的3个也移除掉

**第三步：移除PnL异常的曲线，或覆盖率低的alphas**

1. 经常有一些alpha的PnL是直线等无效的曲线，提前移除list，不要发送请求
2. 有一些alpha只有最近3-4年有数据，从质量优先的角度考虑，放到后面低优先级再check

**第四步：本地计算自相关性，排除自相关高于0.7的alphas**

1. 相关性计算取值是有PnL数据的最近四年，即2018年7月16-2022年7月15日。注意这个窗口会随着平台的数据更新而动态调整
2. 先拉取已经提交过的alpha的pnl到本地，这里注意要处理risk neturalized pnl和super alpha的pnl
3. 再拉取这批待提交的alpha的pnl到本地
4. 对所有的pnl依次计算每日的差值diff，然后计算差值的最大相关性（皮尔逊相关系数），移除最大相关性高于0.7的。注意这里要处理差值是nan的情况

通过以上四个步骤，可以最大化的利用我们相关性检查的MAX Speed的价值，而不是一直几百甚至上千个list去一个个的check submission

**【部分的实现代码】**

**第一步：prune 函数可以直接复用即可**

**第二步：删除关键字，这里可以有tracker和exprission两种使用方式**

```
def filter_alpha(tracker,keys,return_type):        if return_type == 'tracker':        def contains_keyword(sublist, keys):            return any(key in " ".join(map(str, sublist)) for key in keys)        tracker['next'] = [item for item in tracker['next'] if not contains_keyword(item, keys)]        tracker['decay'] = [item for item in tracker['decay'] if not contains_keyword(item, keys)]        return tracker    elif return_type == 'expression':        original_list = tracker['next'] + tracker['decay']        expression_list = [item[1] for item in original_list]        result = [expr for expr in expression_list if not any(key in expr for key in keys)]        return result
```

**第三步：获取pnl的代码可以在Ace Library里面下载（Learn，右下角）**

**3.1 获取 pnl**

```
def get_alpha_pnl(session, alpha_id):    count = 0    while True:        if count>30:            s = login()            count = 0        pnl = session.get("[链接已屏蔽] + alpha_id + "/recordsets/pnl")        retry_after = pnl.headers.get("Retry-After")        if retry_after:            # print(f"Sleeping for {retry_after} seconds")            sleep(float(retry_after))            # sleep(10)        else:            # print(f"{alpha_id} PnL retrieved")            count += 1            return (pnl, alpha_id)
```

**3.2 批量拉取pnl**

```
def fetch_pnls(session, alpha_list):        pnl_ls = []    with concurrent.futures.ThreadPoolExecutor() as executor:        # Create a list of tasks        futures = [executor.submit(get_alpha_pnl, session, alpha_id) for alpha_id in alpha_list]        for future in tqdm(concurrent.futures.as_completed(futures), total=len(futures)):            result = future.result()            pnl_ls.append(result)    return pnl_ls
```

**3.3 转化pnl，主要用于处理super alpha和含有risk netrulized 的pnl，转化为dataframe**

```
def get_pnl_panel(session, alpha_list):    alpha_pnls = fetch_pnls(session, alpha_list)    pnl_df = pd.DataFrame()        for pnl, alpha_id in tqdm(alpha_pnls):        # 检查pnl对象是否有json方法，如果有，则调用该方法获取数据        if hasattr(pnl, 'json') and callable(pnl.json):            data = pnl.json()        else:            # 假设pnl已经是字典格式            data = pnl        # 检查records的列数        if len(data['records'][0]) == 2:            df = pd.DataFrame(data['records'], columns=['Date', alpha_id])            df.set_index('Date', inplace=True)        elif len(data['records'][0]) == 3:            properties = data['schema']['properties']            # 如果含有'risk-neutralized-pnl'，则保留这一列，并删除其他额外的列            if any(prop['name'] == 'risk-neutralized-pnl' for prop in properties):                records = [record[:2] for record in data['records']]                df = pd.DataFrame(records, columns=['Date', alpha_id])                df.set_index('Date', inplace=True)            else:                # 如果records的列数为3，但不包含'risk-neutralized-pnl'，则跳过这个alpha_id                continue        # 将当前alpha_id的DataFrame与总的DataFrame合并        if pnl_df.empty:            pnl_df = df        else:            pnl_df = pd.merge(pnl_df, df, on='Date', how='outer')    return pnl_df
```

**第四步： 选取覆盖率大于0.4（这个值大家自定义即可）**

```
def check_remove_low_pnl(    s,    bar,    ids):    is_pnl_df = get_pnl_panel(s,ids)    df_diff = is_pnl_df.diff(axis=0)    df_processed = df_diff.apply(lambda x: x.apply(lambda y: 1 if abs(y) > 1e-10 else 0))    non_zero_counts = df_processed.sum(axis=0)    total_counts = df_processed.count(axis=0)    percentages = non_zero_counts / total_counts    ids_to_keep = percentages[percentages > bar].index.tolist()    ids_to_remove = [id for id in ids if id not in ids_to_keep]    # 打印结果    print('KEEP:{',len(ids_to_keep),'个} ',ids_to_keep)    print('REMOVE:{',len(ids_to_remove),'个} ',ids_to_remove)    return ids_to_keep,is_pnl_df
```

**第五步：本地计算自相关性，这个和平台结果有一定误差，但不超过2%**

**5.1 获取已经提交alpha的pnl**

```
def get_n_os_alphas(session, total_alphas, limit=100, max_retries=10):    fetched_alphas = []    offset = 0    retries = 0    while len(fetched_alphas) < total_alphas and retries < max_retries:        try:            response = session.get(                f"[链接已屏蔽]            )            response.raise_for_status()            alphas = response.json()["results"]            fetched_alphas.extend(alphas)            if len(alphas) < limit:                break            offset += limit            retries = 0        except requests.HTTPError as http_err:            print(f"HTTP error occurred: {http_err}, retrying in {2 ** retries} seconds...")            time.sleep(2 ** retries)  # 指数退避策略            retries += 1  # 增加重试次数            continue  # 继续下一次循环，不增加offset        except Exception as err:            print(f"An error occurred: {err}")            break    return fetched_alphas[:total_alphas]
```

```
def get_submitted_all(    s,    max: int = 300):    os_alpha_list = get_n_os_alphas(s, max)    os_alpha_ids = [item['id'] for item in os_alpha_list]    os_pnl_df = get_pnl_panel(s,os_alpha_ids)    os_ret_df = os_pnl_df - os_pnl_df.ffill().shift(1)    return os_ret_df
```

**5.2 计算相关性**

```
def gold_mining(s,is_ret_df, os_ret_df):       is_df = is_ret_df[(pd.to_datetime(is_ret_df.index)>pd.to_datetime(is_ret_df.index).max() - pd.DateOffset(years=4)]    os_df = os_ret_df[(pd.to_datetime(os_ret_df.index)>pd.to_datetime(os_ret_df.index).max() - pd.DateOffset(years=4)]        is_df = is_df.replace(0, np.nan)    os_df = os_df.replace(0, np.nan)    gold_ids = []    for col_is in is_df.columns:        ret = is_df[col_is]        ret = pd.concat([ret,os_df],axis=1)        corr_=ret.corr()        cor_max = corr_.iloc[0,1:].max()        if cor_max<0.7:            gold_ids.append(col_is)        else:            if np.isnan(cor_max):                cor_max = 0                set_alpha_properties(s,col_is, name= 'NO_DATA', regular_desc= cor_max, tags=['MOVE'])               else:                set_alpha_properties(s,col_is, name= col_is, regular_desc= cor_max, tags=['Self Correlation'])       print(gold_ids)    return gold_ids
```

```
def check_remove_self_correlation(    s,    ids,    os_ret_df):    is_pnl_df = get_pnl_panel(s,ids)    is_ret_df = is_pnl_df - is_pnl_df.ffill().shift(1)    pass_is_ids = gold_mining(s,is_ret_df, os_ret_df)    return pass_is_ids
```

希望可以提升大家的效率，不再苦等！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
分享一下我的方法，我是把get_alpha进行了魔改（根据函数就可以了），给了sharpe上下限，fitness上下限，同时可以实现多个地区因子一起检验（这不难，写个循环就可以了，但是要注意chn的阈值要放到2,.07），下边是我之前做的一版代码供参考：

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


---

### 技术对话片段 48 (原帖: 【插件】genius operators使用情况分析)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【插件】genius operators使用情况分析_28982066443799.md
- **时间**: 1年前

**提问/主帖背景 (KZ79256)**:
插件地址： [[链接已屏蔽])

在插件中增加了对于operators使用情况的分析

使用说明

- 打开genius页面，可以看到会增加了两个按钮，其中`运算符分析`是抓取此时已提交的alpha进行分析.`显示运算符分析`是调用之前抓取的分析结果. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> 驯Ganlus
> Displaying quarter:
> 2025-01 (Current)
> 运算符分析
> 显示运算符分析

- 无论点击以上哪一个按钮都会在该页面的底部显示一个使用表格, 表格右上角是分析的时间.PS:运算符分析按钮需要等待片刻 
> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 2025-01-05103:36.49.3882
> Category
> Definition
> Count
> Arithmetic
> add(x, Y filter
> false); X+y
> Arithmetic
> eXP(X)
> Arithmetic
> multiplyfx,y
> filterzfalse), X
> Arithmetic
> Signfx)
> Arithmetic
> subtractfx, Y, filterzfalse). X -Y
> Arithmetic
> pasteurizelx)
> Arithmetic
> Jog(X)
> Arithmetic
> purify(x)

- 可以通过点击表头以实现Count排序 
> [!NOTE] [图片 OCR 识别内容]
> Operator Analysis
> 2025-01-05703:36:49.3882
> Category
> Definition
> Count
> Time Series
> _quantilelx,d, driver-"gaussian" )
> Arithmetic
> densifylx)
> Logical
> inputl
> inputz
> Time Series
> tS_corrfx; Y,d)
> Time Series
> [S_ZSCOre(X, d)
> Time Series
> backfill(x lookback = d, k=1, ignore="NAN")
> Cross Sectional
> winsorizelx, std=4)
> Vector
> VeC_minfx)


下一步

- 目前没有做抓取的进度条

情况说明

- 需要在genius页面刷新一下，才能看到按钮，具体原因正在排查
- 由于`-`在表达式里可以用作reverse和subtract两个用处,不太好判断是哪个,所以统一为subtract

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的插件，点赞！

此外，关于“-”的判别，感觉可以检验是否在表达式的首位出现，还是在表达式的中间出现来判断。因为按照一二三阶段来说，一阶跑完后负号会加在表达式之前，再去二阶，所以我感觉可以检测group后，ts_前的负号以判断是reverse还是subtract，供参考。


---

### 技术对话片段 49 (原帖: 【新手顾问看过来】顾问的十大QA经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【新手顾问看过来】顾问的十大QA经验分享_31716442551831.md
- **时间**: 1年前

**提问/主帖背景 (JA75692)**:
## 自我介绍

我是一名SQL boy，一位打工的牛马，对python的了解全是靠AI生成，能读懂。 目前正在消化顾问阶段的一二三阶段的代码，正在思考如何改代码，如何提升回测效率，如何快速的分析回测的alpha，思考如何自动化回测整个流程等等...感觉后面能做的还有很多，偶尔想着想着就睡着了^.^  每当看顾问的帖子，看到大佬每天好几十刀，那叫一个眼馋😋啊（目前我就一天不到2刀😭😭😭） 下面是在这1个多月中遇到的问题，和思考的内容，写成了一个QA的回答，希望对大家有帮助，另外有不对的地方，希望大家能批评指正。

## Q1：如果只跑顾问的1 2 3阶段，调整dataset，能不能跑出啊提交的因子？

能跑出来，但是很少，很多的alpha因子都是pc过不了，都在0.8往上。所以还需要调整模板。

## Q2：一天能回测多少alpha？

我目前一天回测2W左右，不知道达到了平均水平了没有，回测的慢了，希望有大佬给点建议。由于最近再参加PPAC的比赛，这个比赛限制比较低，所以最近只提交了一阶段的因子，一阶段的因子回测的效率可能会快点。


> [!NOTE] [图片 OCR 识别内容]
> Simulated Alphas
> 04/26/2025
> Simulated Alphas: 26.27
> 10K
> 3
> pe
> pe
> ^3"
> 2:
> 9
> ^O.
> ^1.
> 9"
> ^O"
> ^1.
> ?
> A'
> ^
> Displayed Period
> 12/30/2024
> 04/27/2025
> 551711
> Yesterday
> 04/27/2025
> 26270
> Current period
> 03/01/2025
> 04/30/2025
> 558857
> Previous period
> 01/01/2025
> 02/28/2025
> 3573
> Yearto date
> 01/01/2025
> 04/27/2025
> 551710
> Total
> 12/30/2024
> 04/27/2025
> 551711
> Dec
> Mar
> Mar
> Mar
> Mar
> Mar
> Apr
> 6.Jan
> 豆
> "Jan
> Feb
> Feb
> Feb
> Feb
> 20._
> 24.
> 14.
> 31.


## Q3：回测的工具

买了一个最低的阿里云服务，好像是1C2G的配置，一年大概百十块，用于回测alpha够用了。

## Q4：回测代码如何分配

把1 2 3阶段和check阶段的代码进行了拆分，拆分了几个文件，跑哪个阶段，就执行哪个脚本。


> [!NOTE] [图片 OCR 识别内容]
> (base)
> [rooteizzze4voqmrGstfb4olz13Z step] # 1l
> total
> 1108
> drwxr-Xr-X
> root
> root
> 4096
> Apr
> 05:59 alphas
> drwxr-Xr-X
> root
> root
> 4096 Mar
> 31
> 09:20
> bak
> -TT-r-
> root
> root
> 317455
> Apr 27
> 17:50
> check:
> CT-T-r
> root
> root
> 17306
> Apr 27
> 14:28 check_submisstion.Py
> -TT-r-
> root
> root
> 511
> Mar 25 08:59
> check_submit-2025-03.
> -TT-r-
> root
> root
> 513
> Apr 27
> 14:28
> check_submit-2025-04.
> drwxr-Xr-X
> root
> root
> 4096
> Mar
> 13
> 09:26 logs
> -TT-r-
> root
> root
> 31734
> Mar 10
> 21:05 machine_lib.py
> TWXF-XF-X
> root
> root
> 3031
> Mar 13
> 07:28 manage_service.sh
> drwxr-Xr-X
> root
> root
> 4096
> Mar 13
> 11:08 pid
> drwxr-Xr-X
> root
> root
> 4096
> Apr
> 17
> 09:07
> power
> drwxr-Xr-X
> root
> root
> 4096
> Mar
> 11
> 13:41
> pycache
> T-T-r
> root
> root
> 2344 Apr
> 17
> 09:10
> stepl_alpha_power.Py
> T-T-「
> 1
> root
> root
> 1932
> Mar 26 09:47
> stepl_alpha.py
> T-F-厂
> 1
> root
> root
> 177140
> Mar
> 28
> 13:26
> stepl.
> TW-p-p
> 1
> root
> root
> 38489 Apr 15
> 07:39
> stepl_power。
> TW
> root
> root
> 655
> Mar 18
> 10:39
> stepz_alpha.py
> T
> root
> root
> 134338
> Mar 18
> 11:55
> stepz.
> TW厂
> root
> root
> 572
> Mar
> 18
> 18:20
> step3_alpha.py
> T-T-「
> 1
> root
> root
> 274158
> Mar 18
> 19:32
> step3.
> T
> root
> root
> 2090
> Apr 22
> 13:14 step4_alpha.py
> -T-T
> root
> root
> 64865 Apr
> 05:59
> step4.
> (hase)
> [rootoiz27e4v0amrGstfh401 7137
> Stenl#
> 109
> 1o9
> log
> Pool
> 109
> log
> 1og
> 1og
> log


## Q5：曾经尝试过 哪种回测策略？

顾问阶段是用线程池，默认是10*10。但是如果只回测一个阶段，效率就会有点慢。后来把阶段1分了 10*4，阶段2分了10*3，阶段3分了10*3。这样同时跑三个脚本，把资源利用完全，也是可以跑出来alpha的，不过大部分都是3阶段的。

## Q6：新手奖如何拿到？

目前已经拿到100刀的新手奖，这对于我来说还是很大的鼓励。这个过程应该就是成为顾问后提交10天的alpha，就会自动发放的。我当时也没具体看规则，反正就是每天能提交就提交，达到要求就会自动发放，所以，没得到的，不要着急，达到要求，总会有的。


> [!NOTE] [图片 OCR 识别内容]
> Other Payment
> 04/10/2025
> US$100.00
> Total
> 02/27/2025
> 04/27/2025
> US$100.00


## Q7：回测1 2 3阶段到底是个什么？

想要了解整个流程，通读1 2 3阶段的代码是必须的。我读过之后，我对整个流程的理解如下

1、阶段一：选择合适的数据集，通过api得到相对应的字段。 然后把字段放入到一阶段的模板中，生成一个alpha因子的集合。 在把这个集合整理成一个多个线程池，一个线程池有10*10个alpha因子。 最后再对线程池中的因子进行回测。

2、阶段二：通过api获取回测过的alpha因子，当然，要加入限制条件，比如加入sharpe>1,fitness>0.7，这样，就会过滤掉一些因子，得到一些因子之后，在进行剪枝，剪枝的含义是：当有字段相似的因子，就保留前5个（默认情况），因为相似的因子即使提交后，其他的因子再次提交，可能会出现 自相关性太高过不了，所以保留前5个，够用了。剪枝之后，得到一个过滤后的集合，和阶段一样，再次放到线程池中进行回测；

3、阶段三：和阶段二一样，获取因子，过滤，剪枝，然后加入在套入新的操作符，再次进行回测。这样，因子的质量可能会越来越好。

## Q8、如何快速分析回测过的alpha？

想要分析回测过的alpha，当然是把回测过的因子记录下来。记录到文件中也好，数据库也好。当然，作为一个sql boy，是热衷于数据库的。目前我使用的是mysql，见了两张表，一个alphas，一个alpha_check。第一个存储的是get_alphas api得到的results下面的所有字段，第二张表存储的是 is下面的check所有的字段。表结构如下。

```
CREATE TABLE `alphas` (  `id` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `dateCreated` datetime DEFAULT NULL,  `dateModified` datetime DEFAULT NULL,  `hidden` varchar(255) DEFAULT NULL,  `code` varchar(255) DEFAULT NULL,  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,  `operatorCount` varchar(255) DEFAULT NULL,  `settings` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,  `stage` varchar(255) DEFAULT NULL,  `status` varchar(255) DEFAULT NULL,  `category` varchar(255) DEFAULT NULL,  `classifications` varchar(255) DEFAULT NULL,  `color` varchar(255) DEFAULT NULL,  `competitions` varchar(255) DEFAULT NULL,  `dateSubmitted` datetime DEFAULT NULL,  `type` varchar(255) DEFAULT NULL,  `is_check` varchar(255) DEFAULT NULL,  `check_time` datetime DEFAULT NULL,  `is_submit` varchar(255) DEFAULT NULL,  `submit_time` datetime DEFAULT NULL,  `is_pass` varchar(255) DEFAULT NULL,  `pass_time` datetime DEFAULT NULL,  `is_drawdown` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `is_fitness` varchar(255) DEFAULT NULL,  `is_investabilityConstrained` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,  `is_longCount` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `is_margin` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `is_pnl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `is_returns` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `is_riskNeutralized` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,  `is_sharpe` varchar(255) DEFAULT NULL,  `is_shortCount` varchar(255) DEFAULT NULL,  `is_startDate` datetime DEFAULT NULL,  `is_turnover` varchar(255) DEFAULT NULL,  `query_start_date` varchar(255) DEFAULT NULL,  UNIQUE KEY `idx_id` (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

```
CREATE TABLE `alpha_checks` (  `id` varchar(10) DEFAULT NULL,  `name` varchar(255) DEFAULT NULL,  `result` varchar(255) DEFAULT NULL,  `limit_val` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `value_val` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,  `themes` varchar(255) DEFAULT NULL,  `competitions` varchar(255) DEFAULT NULL,  `check_time` varchar(32) DEFAULT NULL,  UNIQUE KEY `id_name_idx` (`id`,`name`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

## Q9：如何插入向两个表插入数据？

表1 alphas：写一个脚本，使用python的pymysql工具。复用之前的get_alphas api，可以得到一天中所有回测的alphas，100个一批，得到的结果转化为json，解析json，然后再写一个 insert函数，把json数据插入到数据库。数据如下。这样就可以通过sql来分析了。


> [!NOTE] [图片 OCR 识别内容]
> id
> dateCreated
> dateModified
> hidden
> code
> description
> Q0Z9VGr
> 2025-04-2622:15:16
> 2025-04-2622:15:16
> False
> ts_quantile(group_rank(oth432_predictivefcf_ttm_predictlcap, market), 240)
> (NULL)
> aakLLn5
> 2025-04-2615:20:00
> 2025-04-2615:20:01
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, densify(pv13_h_f1_sector)), 120)
> (NULL)
> 5J8GoW5
> 2025-04-26 13:25:44
> 2025-04-2703:40:26
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, densify(pv13_h_f_sector)), 240)
> Idea: ts_mean(group_rank(star_eps_surp
> AXTRGEg
> 2025-04-2611:09:22
> 2025-04-26 16:05:38
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, densify(pv13_h_f1_sector) ), 240)
> Idea: ts_mean(group_rank(mdl30_psprise
> maPEpZ2
> 2025-04-2610:54:18
> 2025-04-2610:54:18
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, industry), 240)
> (NULL)
> 912X8OX
> 2025-04-2608:37:52
> 2025-04-2608:37:53
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, densify(pv13_h_f1_sector)), 120)
> (NULL)
> da21A8E
> 2025-04-2608:11:24
> 2025-04-2608:11:25
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, industry), 240)
> (NULL)
> malj829
> 2025-04-26 15:08:39
> 2025-04-26 15:08:39
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, densify(pv13_h_f_sector)), 66)
> (NULL)
> XagGWYm
> 2025-04-26 11:40:50
> 2025-04-26 11:40:50
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, industry), 120)
> (NULL)
> da2P6z9
> 2025-04-2610:00:11
> 2025-04-2610:00:11
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, industry), 120)
> (NULL)
> AXREQIE
> 2025-04-2609:47:40
> 2025-04-2609:47:41
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, densify(pv13_h_f1_sector)), 66)
> (NULL)
> GmrVYRO
> 2025-04-2612:38:25
> 2025-04-2612:38:26
> False
> ts
> mean(group_rank(star_eps_surprise_prediction_fq1/cap, industry), 66)
> (NULL)
> ealPqRJ
> 2025-04-26 10:05:11
> 2025-04-26 10:05:11
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, industry), 66)
> (NULL)
> WIMq8QQ
> 2025-04-2702:34:20
> 2025-04-2702:34:21
> False
> ts_quantile(group_rank(oth432_predictiveebitd_q_predictlcap, sector), 120)
> (NULL)
> 2SrOMI8
> 2025-04-2615:14:55
> 2025-04-2615:14:56
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, sector), 240)
> (NULL)
> paqkomg
> 2025-04-26 10:03:39
> 2025-04-26 10:03:40
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, market), 240)
> (NULL)
> 「I9ONJ
> 2025-04-2609:06:34
> 2025-04-2609:06:35
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1lcap, sector), 240)
> (NULL)
> aaraed2
> 2025-04-2608:47:37
> 2025-04-2608:47:38
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1lcap, market), 240)
> (NULL)
> LKLGXMm
> 2025-04-2613:16:22
> 2025-04-2613:16:22
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, sector), 120)
> (NULL)
> MGjTvrk
> 2025-04-2607:59:06
> 2025-04-2612:26:54
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1/cap, sector), 120)
> Idea: ts_mean(group_rank(star_eps_sUrp
> ReMQbxb
> 2025-04-2702:49:03
> 2025-04-2702:49:04
> False
> ts_quantile(group_rank(oth432_rasvzsplitprofitabilityfcf_
> profitabilitylolcap, market), 240)
> (NULL)
> 5Jn8alk
> 2025-04-2618:39:32
> 2025-04-26 18:39:33
> False
> ts_quantile(group_rank(oth432_rasvzsplitprofitabilityebitd_q_profitability7Icap, densify(pv13_h_f1_sector));
> (NULL)
> glqpGae
> 2025-04-2614:57:18
> 2025-04-2614:57:19
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, subindustry), 240)
> (NULL)
> 0W05851
> 2025-04-2613:40:17
> 2025-04-2613:40:17
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1lcap, sector), 66)
> (NULL)
> 9a5737w
> 2025-04-2613:31:40
> 2025-04-2613:31:41
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fy1/cap, densify(pv13_h_fT_sector)), 240)
> (NULL)
> Yajepew
> 2025-04-2610:48:14
> 2025-04-2610:48:14
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fqllcap, subindustry), 240)
> (NULL)
> Gmqxj5o
> 2025-04-2609:40:23
> 2025-04-2609:40:24
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, sector), 66)
> (NULL)
> LKPMKNL
> 2025-04-2608:34:28
> 2025-04-2608:34:28
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fy1_epslcap, densify(pv13_h_f1_sector)), 240)
> (NULL)
> glqajZk
> 2025-04-26 13:49:56
> 2025-04-2613:49:57
> False
> ts_mean(group_rank(mdl3O_psprise_pct_fql_epslcap, market), 120)
> (NULL)
> 7Y80130
> 2025-04-2613:19:09
> 2025-04-2613:19:09
> False
> ts_mean(group_rank(star_eps_surprise_prediction_fq1lcap, market), 120)
> (NULL)
> ttm_



> [!NOTE] [图片 OCR 识别内容]
> is_longCount
> is_margin
> is
> is_returns
> is_riskNeutralized
> is_sharpe
> is
> shortCount
> is
> startDate
> is_turnover
> query_start_date
> 1504
> 0.000885
> 4080011
> 0.0409
> {"pnl": 2416608, "bookSize": 20000000,
> 1.46
> 1529
> 2013-01-2000:00:00
> 0.0923
> 2025-04-26
> 1610
> 0.004141
> 4637882
> 0.0465
> {"pnl": 1526623, "bookSize": 20000000,
> 1.46
> 1436
> 2013-01-2000:00:00
> 0.0224
> 2025-04-26
> 1652
> 0.005812
> 5342544
> 0.0535
> {"pnl": 1729764, "booksize": 20000000,
> 1.46
> 1395
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1652
> 0.005812
> 5342557
> 0.0535
> {"pnl": 1729809,
> bookSize"=
> 20000000,
> 1.46
> 1395
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1647
> 0.00574
> 5270198
> 0.0528
> {"pnl": 1677718, "bookSize": 20000000, "1 1.46
> 1400
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1610
> 0.004142
> 4637916
> 0.0465
> {"pnl": 1526713, "booksize": 20000000, "1
> 1.46
> 1436
> 2013-01-2000:00:00
> 0.0224
> 2025-04-26
> 1647
> 0.00574
> 5270216
> 0.0528
> {"pnl": 1677766, "bookSize": 20000000,
> 1.46
> 1400
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1566
> 0.002951
> 4174681
> 0.0418
> {"pnl": 1555223,
> bookSize": 20000000,
> 1.45
> 1480
> 2013-01-2000:00:00
> 0.0283
> 2025-04-26
> 1606
> 0.004109
> 4591579
> 0.046
> {"pnl": 1439735, "bookSize": 20000000,
> 1.45
> 1441
> 2013-01-2000:00:00
> 0.0224
> 2025-04-26
> 1606
> 0.004109
> 4591602
> 0.046
> {"pnl": 1439816, "bookSize": 20000000,
> 1.45
> 1441
> 2013-01-2000:00:00
> 0.0224
> 2025-04-26
> 1566
> 0.002951
> 4174705
> 0.0418
> {"pnl": 1555284, "bookSize": 20000000,
> 1.45
> 1480
> 2013-01-2000:00:00
> 0.0283
> 2025-04-26
> 1565
> 0.002918
> 4119629
> 0.0413
> {"pnl": 1373895, "booksize"
> 20000000,
> 1.44
> 1481
> 2013-01-2000:00:00
> 0.0283
> 2025-04-26
> 1565
> 0.002918
> 4119653
> 0.0413
> {"pnl": 1373953, "booksize": 20000000, "
> 1.44
> 1481
> 2013-01-2000:00:00
> 0.0283
> 2025-04-26
> 1501
> 0.000792
> 5212038
> 0.0522
> {"pnl": 1974852, "bookSize": 20000000,
> 1.43
> 1532
> 2013-01-2000:00:00
> 0.1318
> 2025-04-26
> 1660
> 0.005784
> 5303521
> 0.0531
> {"pnl": 1648989, "bookSize": 20000000,
> 1.43
> 1386
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1665
> 0.005798
> 5331633
> 0.0534
> {"pnl": 1684330, "bookSize
> 20000000,
> 1.43
> 1381
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1660
> 0.005784
> 5303485
> 0.0531
> {"pnl": 1648933, "bookSize": 20000000,
> 1.43
> 1386
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1665
> 0.005798
> 5331582
> 0.0534
> {"pnl": 1684254, "booksize": 20000000,
> 1.43
> 1381
> 2013-01-2000:00:00
> 0.0184
> 2025-04-26
> 1620
> 0.004115
> 4585819
> 0.0459
> {"pnl": 1365293, "bookSize": 20000000,
> 1.42
> 1426
> 2013-01-2000:00:00
> 0.0223
> 2025-04-26
> 1620
> 0.004115
> 4585794
> 0.0459
> {"pnl": 1365222,
> bookSize": 20000000,
> 1.42
> 1426
> 2013-01-2000:00:00
> 0.0223
> 2025-04-26
> 1265
> 0.001175
> 5344521
> 0.0535
> {"pnl": 2826830, "booksize": 20000000,
> 1.41
> 1344
> 2013-01-2000:00:00
> 0.0911
> 2025-04-26
> pnl


表2：alpha_checks，在顾问代码中有check的流程，我们对这块代码进入插入功能。因为回测的时候是一个alpha一个alpha进行check的，所以这个地方加入插入的操作，通过更新alphas表，当check过的alpha，更新表中的is_check=1，说明check过了，即使check阶段断了，也可以继续实现断点测试。check的时候只check is_check=0的。数据如下：


> [!NOTE] [图片 OCR 识别内容]
> Message
> Result
> Profile
> Status
> id
> name
> result
> limit_val
> Value_val
> competitions
> themes
> check_time
> VUUnUy
> TCOULAT_DUDIVIIDIVIV
> 厂CIUIIVU
> TULC)
> (WULLI
> (OLCJ
> (WULLI
> (WULLI
> Xvqdkbg
> MATCHES_COMPETITION
> WARNING (NULL)
> (NULL)
> [{'id': 'PPAC2025' 'name'=
> 'Power Po
> (NULL)
> (NULL)
> Xvqdkbg
> IS_LADDER_SHARPE
> FAIL
> 1.58
> -1.27
> (NULL)
> (NULL)
> (NULL)
> Xvqdkbg
> MATCHES_PYRAMID
> PASS
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> Xvqdkbg
> MATCHES
> THEMES
> WARNING (NULL)
> (NULL)
> (NULL)
> [{'id': 'byg8ooy
> 'multiplier': 2.0, 'nam
> (NULL)
> 9IY7ZEr
> LOW_SHARPE
> FAIL
> 1.58
> -0.41
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> LOW_FITNESS
> FAIL
> 1.0
> -0.16
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> LOW_TURNOVER
> PASS
> 0.01
> 0.1294
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> HIGH_TURNOVER
> PASS
> 0.7
> 0.1294
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> CONCENTRATED_WEIGHT
> PASS
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> LOW_SUB_UNIVERSE_SHARPE
> PASS
> -0.18
> -0.17
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> UNITS
> WARNING
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> SELF_CORRELATION
> PENDING
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> DATA_DIVERSITY
> PENDING
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> PROD_CORRELATION
> PENDING
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> REGULAR_SUBMISSION
> PENDING
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> MATCHES_COMPETITION
> WARNING
> (NULL)
> (NULL)
> [{'id': 'PPAC2025' 'name'=
> Power Po
> (NULL)
> (NULL)
> 9IY7ZEr
> IS_LADDER_SHARPE
> FAIL
> 1.58
> -1.18
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> MATCHES_PYRAMID
> PASS
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 9IY7ZEr
> MATCHES_THEMES
> WARNING (NULL)
> (NULL)
> (NULL)
> [{'id': 'byg8ooy
> multiplier': 2.0, 'nam (NULL)
> 3OWeMoX
> LOW_SHARPE
> FAIL
> 1.58
> 0.49
> (NULL)
> (NULL)
> (NULL)
> 3OweMoX
> LOW_FITNESS
> FAIL
> 1.0
> 0.29
> (NULL)
> (NULL)
> (NULL)
> 3OWeMoX
> LOW_TURNOVER
> PASS
> 0.01
> 0.0321
> (NULL)
> (NULL)
> (NULL)
> 3OweMoX
> HIGH_TURNOVER
> PASS
> 0.7
> 0.0321
> (NULL)
> (NULL)
> (NULL)
> 3OWeMoX
> CONCENTRATED_WEIGHT
> PASS
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> (NULL)
> 3OWeMoX
> LOW_SUB_
> UNIVERSE
> SHARPE
> PASS
> 0.21
> 0.43
> (NULL)
> (NULL)
> (NULL)


## Q10：后续还有哪些优化点？

我也是最近刚有的想法，目前准备进行优化代码，思想如下：

当check之后的步骤，可以通过check的结果获取到alpha_id，通过alpha_id得到这个alpha_id的所有信息，sharpe、fitness、longcount等等。然后判断 sharpe、fitness，当达到条件之后，直接可以进行二阶段回测。同样，而阶段回测，也进行判断，满足条件直接进行三阶段回测。这样，就不用等待一阶段跑完，再跑二阶段，二阶段跑完跑三阶段。 实现了比较深层次的搜索过程。  这个思路不知道怎么样，请各位大佬评判一下。

好了，分享到这里结束，但是探索的过程还远远没有结束，我的思路是：最终可以搭建一个coze、n8n类似的工作流，真正的实现自动化全流程，后期只要调整相关的模板就可以了。一键修改，一键回测，一键提交，是终极目标。 所有的quant们，一起加油，希望我这个小菜鸡的思路可以帮助到大家，同时也希望大佬们也给我多点建议！ 谢谢大家！！！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的帖子，点赞！但同时要稍微提示一下，1g2m的跑的不是特别顺畅，卡卡的，我用的是2g4m有时候也会卡，有能力的情况下还是尽可能上高配，这样用着舒服


---

### 技术对话片段 50 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day1

今日主要内容如下

①提交两个glb因子，（有些因子居然微调后的效果还不如原始版本，这不得不说运气十分好了）、

②重构了machinelib里面二阶运算符（下午听老师说会增加，可能还要回滚代码，不过我是mute而不是删除，问题不大）

③把各种代码从本地电脑搬到云服务器上进行运行


---

### 技术对话片段 51 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day3

昨天从垃圾堆里面找了个alpha交，喜提一个因子1.43刀，哎，好在glb的一阶快跑完了，二阶以上就会有新的存货。我统计了一下，没改版之前，我所有能提交的（check没问题，sharpe大于1.6，fit大于1.1，turnover小于50），一共有275个，我自己挑选出40个比较好的，改版之后拉了一下总共就剩75个了，其中还有小十个一阶跑出来的。估计还是要坐2-3天牢


---

### 技术对话片段 52 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day4

今天重新写了一下二阶，正式上线了（不得不把所有一阶的notebook全重启）。同时把之前跑的一阶检查了一下，查出十几个能交的，产出率还可以。同时我也想讨论一个问题：一阶跑出来的因子，感觉pnl曲线和fit等年份数值不是特别稳定，这种是微调一阶因子好，还是放去跑二阶好呢？


---

### 技术对话片段 53 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day5

这几天的因子质量一直不行，basepay总是距离基准差一点，不是1.68就是1.84，看起来一阶还是差点意思。目前打算先交用模版跑的因子（经过我可持续性地涸泽而渔之后，这种因子也没有多少了。。。而且质量还不行），坚持到二阶跑出因子，这样整体水平应该还能拯救一下。

昨天参加了某大学的硕士笔试，给我难坏了(哭


---

### 技术对话片段 54 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day6

从8号开始到16号，eur一阶一个因子都没出来，实在是忍不下去（还占我两个通道，一个一阶一个模板），也不管跑没跑完直接上二阶，终于出了一个看着还行的，

Sharpe2.70

Turnover23.64%

Fitness1.68

Returns9.18%

Drawdown2.80%

Margin7.76‱

还是我第一个eur因子，之前权限都有的时候也没跑过eur


---

### 技术对话片段 55 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day7

↓这个eur因子，居然只有1.42刀，估计还是有点过拟合的味道了。我在提交因子前都会开一个multi去把每一个中性化都跑一遍选最好的交，这个也会过拟合嘛？

Day6

从8号开始到16号，eur一阶一个因子都没出来，实在是忍不下去（还占我两个通道，一个一阶一个模板），也不管跑没跑完直接上二阶，终于出了一个看着还行的，

Sharpe2.70

Turnover23.64%

Fitness1.68

Returns9.18%

Drawdown2.80%

Margin7.76‱

还是我第一个eur因子，之前权限都有的时候也没跑过eur


---

### 技术对话片段 56 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day8

之前交的太猛了，有个比赛能+3的因子卡prod没法交，拼拼凑凑交了个+1的因子。。。

现在二阶基本上已经开始跑，有了一定产出了（虽然减枝，但是同质化现象依旧很严重，还是要在想办法才是）

自从8号之后，basepay急速下滑，估计等到三月更新到1月的时候估计要坐牢。。。不过还好模版和123阶马上就能产出


---

### 技术对话片段 57 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day9

今天是2025年1月22日，是北方小年

提前祝各位朋友新年快乐

昨天交了四个，2.2，终于把base拉回正常水平了。。。

老虎哥发的福利模版还在跑，估计后天吧，后天能出点结果，我觉得老虎哥的模版就跟123阶的模版一样，很通用，就是搜索空间大了点，要自己筛一下。


---

### 技术对话片段 58 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day10

今天是2025年1月23日，是南方小年，提前祝各位朋友新年快乐。

昨天交了三个因子，base给了1.9刀，深刻感觉value的重要性。

有些usa和glb的因子，turnover小于10，但是sharpe不达标，交了吧，影响比赛得分（虽然本来也没多少分。。。），不交吧，等到卡cor就傻眼了，纠结哇。。。


---

### 技术对话片段 59 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day12

马上要过年了，提前祝各位朋友新年快乐

昨天交了2个因子，给了1.89刀，再次感受到vf的重要性。

我手上有一堆因子，但是每次都得 挑挑拣拣，不是turnover高就是近几年sharpe和fit烂

为了更好的参加genius项目，我已经停掉了很多很好用但是op多的模版，回归到123阶段了

我个人感觉，一阶段的因子op少，但是质量和稳定性差一点，二阶因子op多，稳定性会好点


---

### 技术对话片段 60 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day13

马上要过年了，提前祝各位朋友新年快乐

昨天下午cor突然高了起来，交了一下午只成功了一个模版出的因子给了1.58

重新筛了一遍，发现之前跑出来的小三百个因子就剩下五十多能交了，大部分还是模版出的（model虽然现在不限制，但以后要是限制就亏大了，我现在能不交model就不交model）


---

### 技术对话片段 61 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day14

今天是2025年1月27日，马上要过年了，提前祝各位朋友新年快乐

青黄不接的时候，昨天只交了一个模版出的因子，质量一般，居然给了1.83，感觉是vf更新了

现在我的存货99%都是模版跑出来的，效果好但是op多，很纠结交不交，怎么交，今天重新开始跑eur了，因为交sa的时候感觉三个地区主动放弃一个还是太亏，eur的主要问题在于20-22年的fit和sharpe没法拉起来，之前跑的很多因子都有这个感受。

anyway，很快就下班了，过完年再看看跑的怎么样


---

### 技术对话片段 62 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day15

新年快乐！！！！！！！！！！！

今天交了一个模版出的因子，为了降低op我魔改了一下，以0.2fit换掉三个op，现在op还是7.74，太高，得想办法降下去，但是一二三阶一直没有产出，好模版又太长，纠结哇


---

### 技术对话片段 63 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day16

大家新年快乐！！！！

昨天交了两个因子，给了1.71，现在只剩下模版出的因子了，其他的一点都没了，一二阶也没啥产出，已经在考虑每天只交一个直到存货充足的方法。今天把usa的两个槽分给chn了，chn我做的还是蛮多的，sa也能组，静待收获。


---

### 技术对话片段 64 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day17

祝大家新年快乐！！

最近断粮了，昨天只交了一个因子，给了1.53,。

最近在想办法提升天才计划那个排名，感觉还是在op方面 差一点，还是要探索不同op的使用

anyway，静待产出


---

### 技术对话片段 65 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day18

祝大家新年快乐！！

昨天实在是没有产出，交了一个垃圾，只给了1.35，质量真的堪忧，

最近开始停掉glb，跑asi了，glb太慢，导致一二阶产出效率也不行

找到一个还可以的模版，跑了220个差不多有2个微调一下就能交（正在微调），期待一下跑完的效果


---

### 技术对话片段 66 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day19

昨天的因子微调出来，效果还可以，用的是risk和pv数据，特征是收益库库高，换手率也库库高，margin还能拉上10

跑的二阶有了点产出，最近一阶段基本上不会有任何产出了，有点头疼

同时祝大家新年快乐。


---

### 技术对话片段 67 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day20

有点头疼，现在属于，跑出来能交的，要么卡cor，要么op巨多不敢交，今天停掉glb，重新开始跑asi和eur，eur真的难跑，一阶前后跑了好几天一个没有，唯一交上去的一个是二阶+调参才成功的

最近调了一个针对risk的模版，之前跑asi差不多2200个出2个（一个卡cor70.3，再想办法调），特点就是之前提到的，收益高，fit也高

此外还有个小问题，我手头有个22年fit达到9.但是总的fit才2左右的因子，这个能交吗？我担心是不是过拟合这种的


---

### 技术对话片段 68 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day22

今天os更新了，看了下表现，发现还行，越早交的质量越一般（但还是能过得去的）

昨天交了一个news，一阶跑出来的，给了1.58，感觉还可以

combined组合，从1.25跌倒-0.94，个人估计是刚当上顾问的时候 ，asi的高turn因子交了不少（我现在甚至还有一堆turnover50,60的），叠加上算法的更新导致的，不过好在12月，1月交的turnover中位数都控制在20,30左右，最高也就41，感觉还是能做的

更新os后，所有的老因子都要跑一遍，从1月8号开始的因子，sharpe高于1.58抓了一遍，分了三个槽再跑，希望能出点吧，不然真没存货了


---

### 技术对话片段 69 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day23

昨天交了一个老虎哥模版出来的因子，只有20年往后才有数据，但给的出乎意料的多，一个因子1.88

分了三个槽跑之前的老因子（抓的是1月8号后，到2月7号的），阈值选的是1,58和fit1，usa差不多能抓出六七千个，glb五千，chn两千千（一堆chn因子莫名其妙地跌，跌的还很一致，可惜不能加符号），eur更离谱，就六百个，今天跑完在排队check，感觉虽然最近check速度快了，但是我有一堆要检测的，还是得等

下一阶段的任务就是去深入研究一下老虎哥的模版，以及一些用的人少的字段，看看有没有什么意外之喜


---

### 技术对话片段 70 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day26

怀念短暂出现的0.7vf

昨天交了两个同字段op，一个删掉了backfill和windosize，另一个保留，prod分别是66和52，在0.5vf的情况下两个给了2.73，证明低prod的因子真的很加分


---

### 技术对话片段 71 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day27

想念0.7vf的第二天

昨天交了一个mdl数据，两个 op，1.69，感觉有时候backfill和windosize不是必须的，我现在提交前都会网页跑一下，先吧所有中性化试一遍，选定最好的后把这两个op分别删了试一遍

为了genius，天天降op，这几天per op从7.74拉到7.58了，后边看看能不能下到6或者5，这样卷expert希望大一点


---

### 技术对话片段 72 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day28

0.7vf回来辣

昨天交了一个模版出的因子，glb的model（这个数据集之前跑模版交了五十多个，红的不能再红了，现在正在全力跑glb其他数据平均一下），给了1.69，感觉还可以

下一步就是提质增效，找更好的数据和模版，继续跑


---

### 技术对话片段 73 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day29

0.7vf的第二天，开心

今天交了三个因子，分别是mdl，fnd和anl，给了不少

吸引了一个新人来咨询（虽然还没确定报名），推荐奖我来辣


---

### 技术对话片段 74 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day32

sa组不出来，相关性太高

提醒一下各位，asi地区mdl135，按照一二阶来做能出不少，但是turn高，没有什么交的价值，可以不用跑这个数据集了

感觉vf更新后，没有1.5基准来判断，对于交上去的质量有点摸不清。。。


---

### 技术对话片段 75 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day33

昨天组了个sharpe5.6，fit4.4的sa，才给了2刀，感觉还是质量的问题

虎哥的模版还在跑，最近基本上都是靠着虎哥模版撑起来的提交

下一步计划研究一下大规模回测sa的方法


---

### 技术对话片段 76 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day34

昨天交了个sharpe7，fit6的sa，给了2.5，确实感觉没有1.5基准大法之后，对因子质量把握不清了，昨天的ra才1. 69，vf0.5的时候一个1.69也不是没有过，还是要提质增效！最近有点青黄不接了。。。


---

### 技术对话片段 77 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day35

昨天check函数抽风，差点没得交了，翻了翻还有个二阶news数据，交上去了

最近在研究这个superalpha的组合表达式，感觉好有意思，上下两种组合可以保证组出一堆（虽然可能 有些卡prod），针对这个我研究明白了可能会写个帖子分享一下（


---

### 技术对话片段 78 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day36

最近游走在断粮的边缘，每天只能尽力保证1个sa和1个ra

可持续性竭泽而渔的日子啥时候是个头哇，周末要研究一下新的模版和数据了，不然越等越完蛋


---

### 技术对话片段 79 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day37

eur跑出不少高turn因子，

应该是我数据选择的问题，已经在修改一阶数据集了

还有个比较尴尬的事情是，发现自己修改后的check函数，并不能实现按照turnover筛选。。。（原因是wq的turnover按照0.xx的格式，而我写的是xx。。。量纲对不上了）


---

### 技术对话片段 80 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day38

继续开挖EUR，单字段因子能给不少，狠狠挣一笔

现在check 函数，又怕一个 都出不来，又怕个个都能交，一交就报废一大堆，减枝还是不彻底


---

### 技术对话片段 81 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day39

实验了一个新模版，有点信号，但是会卡cor，还是要多交eur的因子才有钱拿（前天交了一个eur atom，普通的，给了6.67，但昨天交的asi，比eur纸面数据要好，只有1.76，老师说是theme扭曲rank的原因，eur至少是未来两周内的重点


---

### 技术对话片段 82 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day40

之前实验的模版初步有了一点产出，但是数量级是字段数目的平方再乘以2（因为正反有时候都有信号，为了防止错过什么都会跑），。在chn上能出一点（1.6+的不少，但是chn是2.07，就没法交），现在再跑eur和glb的（glb太慢），可能会攒一点等下个季度。模版的问题是可能会卡cor（很多高质量的，cor都是0.75左右）


---

### 技术对话片段 83 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day41

今天更新了combined，经过一个月努力整体sharpe从-0.94拉到-0.8，看来这个费后还真是麻烦，还是得交低turn的，新人时期亮了就交真的是个愚蠢的决定。selected倒是有0.29，看看再努力一个月能不能拉一个到0.5


---

### 技术对话片段 84 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day42

今天在教新人，大一小朋友要耐心点教

昨天交了一个asi的，质量很不错，但是没theme，只有1.86刀，真心疼啊，但是没办法，不交就断粮了（只要坚持总会有好因子出现的：））


---

### 技术对话片段 85 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day43

不知不觉已经写了四十三天日记了，最近有点断粮的趋势，一只没check出什么东西

昨天晚上光顾着看美股大跌了。。。希望我的因子们还好


---

### 技术对话片段 86 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day44

最近check函数一直在报catch错误，两天的因子没检查了，还是要耐心点。


---

### 技术对话片段 87 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day45

今天更新了vf，从0.7掉0.57，还是要注重质量。

q1马上就结束了，还是要想办法多刷一点，希望不会被卡combined（现在0.29），一直在交能改善组合表现的影子

最近拉了一个新人，转化率差不多真就10%


---

### 技术对话片段 88 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day46

0.57的日子真难过啊，相比0.7的日子真的煎熬，最近一个月每天都只能交一个了（不是坐牢，产能不足，回测数少了，效率也低。。。），昨天1.67今天1.68，估计就是基准水平。

今明两天iqc开了，要帮带的新人挣点钱，才能有更多新人来投奔。忙啊


---

### 技术对话片段 89 (原帖: 对 next_alpha_recs 进行去重使用字典来存储去重后的结果unique_recs = {}for rec in next_alpha_recs:    exp = rec[1]  获取 exp    sharpe = rec[2]  获取 sharpe    如果 exp 不在字典中，或者当前的 sharpe 更高，则更新    if exp not in unique_recs or sharpe > unique_recs[exp][2]:        unique_recs[exp] = rec将结果转换为列表unique_alpha_recs = list(unique_recs.values()))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Day47

交了个自相关0.66，池相关0.69的因子，给了1.74，感觉0.57的基准就在这。感觉现在一阶段已经很少出货，全靠 模版撑着了 。


---

### 技术对话片段 90 (原帖: 【日常生活贴】我的量化日记第三季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **时间**: 0年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年7月16日

好久没写量化日记了，最近在研究12+降turn的协同效应，combine翻车后，更加要注重因子质量而非数量或者六维，有些py点的确实困难，anyway，keep moving!!!

========================================================================================================================================================================


---

### 技术对话片段 91 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年6月1日

昨天交了四个ra，一个sa，sa是usa的sa，给的比glb的sa少，我估计是glb交的少，cor低双重影响叠加下来，base拉满的

再说 ra，四个ra分别是两个amr，一个usad0，一个eurd0，不想混d1的情况下只能猛交d0凑pyramid了。

=======================================================================

“没有过去的人，未来是不会前来造访他的。累积了过去的往事，才有了现在，然后“现在”才会持续着“过去”继续往“未来”而去，不管是什么样的过去都不会毫无意义的，“过去”是跟“现在”还有“未来”的自己串在一起的。”——《游戏王》

=======================================================================


---

### 技术对话片段 92 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年6月2日

sa比赛开始，交了一个fit5，不衰减的sa，只有一万六千多分，看来还是要多选才行。昨天没下手，今天想要再组的话可能难度就会上去了，cor逐渐升高 ，头疼。

===生活就像海洋，只有意志坚强的人才能到达彼岸===

===This is an apple, I like apples, apples are good for our health===


---

### 技术对话片段 93 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年6月12日

又到了季度末了，要开始冲刺喽

pyramid点到了47个，剩下3个有信心在d0做出来

现在就看 combine了，希望能如愿，但也要给自己 做预期管理

生活就像海洋，只有意志坚强的人才能到达彼岸


---

### 技术对话片段 94 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年6月15日

今天点完了第50个py

可以抽时间优化六维，跑小地区，补强扶弱了

=======================================================================

“没有过去的人，未来是不会前来造访他的。累积了过去的往事，才有了现在，然后“现在”才会持续着“过去”继续往“未来”而去，不管是什么样的过去都不会毫无意义的，“过去”是跟“现在”还有“未来”的自己串在一起的。”——《游戏王》

=======================================================================


---

### 技术对话片段 95 (原帖: 【日常生活贴】我的量化日记第二季)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([Commented] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

**顾问 worldquant brain赛博游戏王 的解答与建议**:
2025年6月16日

今天倒腾了一下自营量化的框架，深刻感受到了什么叫做基础设施的重要性，策略谁来都能跑，有没有对应的算力支持，有没有对应的服务器支持才是最重要的，平台matters

=======================================================================

“没有过去的人，未来是不会前来造访他的。累积了过去的往事，才有了现在，然后“现在”才会持续着“过去”继续往“未来”而去，不管是什么样的过去都不会毫无意义的，“过去”是跟“现在”还有“未来”的自己串在一起的。”——《游戏王》

=======================================================================


---

### 技术对话片段 96 (原帖: 步骤2: 计算残差与X平方的协方差)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【有奖】SuperAlpha征文分享你独到的selection和combination方法_32451124312599.md
- **时间**: 1年前

**提问/主帖背景 (WL13229)**:
一句话总结该活动：直接在评论区评论，分享高质量selection或者combo。

> ```
> 被审核通过者将获得BRAIN纪念品一份优秀分享更有机会将获得50USD的一次性津贴。
> ```

活动时间：即日起至6.14日23：59（以服务器时间为准）

活动要求：参赛同学可发布多个idea参赛，可以是selection idea或者combo idea；必须展示setting。同一人可发布多条评论参赛，一个评论仅能放1个idea。同一人不可领多份奖励，但被发出的评论越多会更容易获得较多点赞。


> [!NOTE] [图片 OCR 识别内容]
> S~A吣I
> BRAINI


> 纪念品图

再次强调🎇

**被审核通过者将获得BRAIN纪念品一份
优秀分享更有机会将获得50USD的一次性津贴。**

**顾问 worldquant brain赛博游戏王 的解答与建议**:
类别：SELECTIONN

表达式：

(

not(own)&&

#选择不是自己的因子

((turnover<0.07&&turnover>0.05)||

(turnover<0.15&&turnover>0.13)||

(turnover<0.12&&turnover>0.09))

#按照turnover进行分层，每次选取不同的范围以保证每次选到的因子不同，提升多样性

&&(operator_count<8)  &&(dataset_count<=2)

#限制op和pyramid个数，降低过拟合的概率

&&(prod_correlation<0.5&&prod_correlation>0.1)

#按照prodcor筛选，0.5可以保证充分的分散化，0.1则是保证不选到奇奇怪怪的东西（一些厂或者极端的pnl）

#以上为组合部分，以下为权重分配

)

/(turnover*s_log_1p(turnover)

#按照turnover进行加权

*sigmoid(self_correlation)

*sigmoid(prod_correlation)

#按照prodcor进行加权，为了防止权重变化过大，比如0.5和0.1权重差五倍，容易集中到一个因子上去

*abs(long_count-short_count))

#按照多空进行加权，对于多空平衡的因子赋予更高权重，可以避免选到偏多或者偏空因子

其他参数： 
> [!NOTE] [图片 OCR 识别内容]
> Combo Expression
> Simulation Settings
> Instrument Type:
> Equity
> Decay:
> Pasteurization:
> 0n
> Reglon:
> A51
> Delajl:
> NaN
> Handling:
> 0n
> Universe:
> MINVOLIM
> Truncation:
> 0.08
> Unit Handling:
> Verify
> Language:
> Fast Expression
> Neutralization:
> Sector
> Max Trade:
> Off


最终结果：


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> TurnoVer
> Fithess
> Returns
> Drawgown
> Margin
> 7.66
> 13.049
> 9.20
> 18.839
> 1.539
> 28.899600
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 8.04
> 13.7695
> 10.34
> 22.759
> 0.76%
> 33.07330
> 1385
> 1331
> 2014
> 6,63
> 13.299
> 14.799
> 829
> 22.26930
> 1598
> 1547
> 2015
> 8,64
> 12.8995
> 11.54
> 23.4196
> 0.519
> 36.33950
> 659
> 538
> 2016
> 4.65
> 12.6995
> 4.56
> 12.739
> 1.5796
> 20.059630
> 590
> 1577
> 2017
> 8.92
> 12.9995
> 10.93
> 19.52%
> 88%
> 30.0530
> 605
> 1638
> 2018
> 8.89
> 13.4095
> 10.75
> 19.589
> .68%
> 29.21930
> 883
> 1851
> 2019
> 6,08
> 13.3796
> 6.14
> 13.649
> 1.139
> 20.41930
> 1675
> 2020
> 8,05
> 12.959
> 10.15
> 20.6096
> 0.939
> 31.80750
> 1811
> 1736
> 2021
> 9.21
> 12.629
> 11.83
> 20.8196
> 0.529
> 33.00750
> 2243
> 2250
> 2022
> 8.60
> 12.5595
> 10.91
> 20.18%
> 639
> 630
> 2104
> 2072
> 2023
> 5.90
> 9.8195
> 8.18
> 24.029
> 0.7196
> 28.3530
> 1760
> 1872
> Risk neutralized
> Aggregate Data
> Sharpe
> TurnoVer
> Fithess
> Returns
> Drawcown
> MarEin
> 7.55
> 13.049
> 7.87
> 14.18%
> 0.7796
> 21.759600
> VYear



---

### 技术对话片段 97 (原帖: 转换为 Pandas DataFrame)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【网页监控】基于Streamlit和数据库的网页监控进程代码优化_30329770583959.md
- **时间**: 1年前

**提问/主帖背景 (KZ79256)**:
由于我是基于数据库跑alpha的，每次想监控跑了多少，还有多少没跑，程序是不是在运行，都要用相应的代码在数据库或者命令行中运行。为了便捷我使用Streamlit做了个网页来查看运行情况（可能需要公共ip）

其中Streamlit是一个非常简单的制作网页的方法，在访问网页时调用后端python代码实时渲染网页，通过st.write可以向网页中写入dataframe，st.markdown向网页写入markdown语法

**一些库的导入和侧边栏制作**

因为我用的时mongo数据库管理alpha，可以适时改写成自己的

```python

import streamlit as st

from streamlit_extras.colored_header import colored_header

from streamlit_option_menu import option_menu

from streamlit_extras.badges import badge

# from streamlit_card import card

import pandas as pd

import numpy as np

from pymongo import MongoClient, UpdateOne

from pymongo import errors

from datetime import datetime

import pytz

import json

#侧边栏制作

with st.sidebar:

select_option = option_menu(

"WQB-监控",

[

"数据库监控",

"收入监控",

],

icons=[

'house',

'arrow-repeat',

],

menu_icon="boxes", default_index=0

)

if select_option == "数据库监控":

这个网页你想做的内容

其余同理

```

**首先是程序监控**

效果如下


> [!NOTE] [图片 OCR 识别内容]
> WQB- 监控
> 程序监控
> 数据库监控
> PID
> action
> UISeI_
> Collection_
> name
> 收入监控
> 193873
> TUIn
> 193874
> get
> 458295
> TUIn
> 458296
> get


通过下述代码，可以获得正在运行的程序，注意第一行的command应该改成你程序运行命令，以显示你正在运行的程序

```python

command = 'ps aux | grep "python main.py --action" | grep -v grep'

result = subprocess.run(command, shell=True, text=True, capture_output=True)

# 解析输出

data = []

for line in result.stdout.strip().split("\n"):

parts = line.split(maxsplit=10)  # 解析 ps aux 的格式

if len(parts) == 11:  # 确保解析正确

data.append(parts)

# 定义列名（ps aux 的标准列）

columns = ["USER", "PID", "CPU%", "MEM%", "VSZ", "RSS", "TTY", "STAT", "START", "TIME", "COMMAND"]

# 转换为 Pandas DataFrame

df = pd.DataFrame(data, columns=columns)

colored_header(label=f"程序监控",description="",color_name="red-70")

st.write(df)

```

**接下来是数据库alpha状态监控**

效果如下


> [!NOTE] [图片 OCR 识别内容]
> WQB-监控
> 数据库: WQBGeniusQl
> 数据库监控
> 收入监控
> alpha state
> Pending
> Running
> Run_Done
> Check_Done
> Dropout_ZYSHARPE
> Dropout_Fitness
> Dropout_Stock
> Run_Error
> 些数字
> bs stage
> 999
> 些数字
> 数据库: WQBSAQI
> alpha state
> Run_Done
> Check_Done
> Run Errol
> bs stage
> Pending
> Running


我把alpha用两个标识，一个是alpha state（用于描述该alpha是什么状态，等待运行，正在运行，运行完毕，正在获取is数据，获取完毕，以及因为各种原因丢弃的alpha和运行失败的），一个是bs stage（目前的alpha属于第几阶段，或者模板是什么）

目前我在自动跑regular alpha和super alpha，所以会有两个数据库要监视

通过mongo查询相应的alpha状态，然后写入网页，这样我就可以通过看pending，running来查看还有多少要运行，正在跑的alpha的状态

由于每个人的思路不太一样，这里就只是抛砖引玉，不放具体的代码了，写入的核心还是st.markdown，st.write

**收入监控**

效果展示


> [!NOTE] [图片 OCR 识别内容]
> WQB-监控
> 收入监控
> 数据库监控
> 刷新收入数据
> 收入监控
> 抓取的美东时间:2025-02-28
> SUPERAlpha
> Tee
> SUDer
> TyDE
> aUtHOI
> dateSubmitted
> themes
> pyramids
> alphald
> regIon
> Unlerse
> Ttness
> delay
> prodCorrelation
> ValueFactor
> 131
> SUPER
> 顾问 KZ79256 (Rank 21)
> 2025-02-28
> 1.0
> OLELnd2
> USA
> T0P3000
> 5.99
> 0.6738
> 0.77
> 5.38
> SUPER
> 顾问 KZ79256 (Rank 21)
> 2025-02-27
> OLIIXaXL
> USA
> T0P3000
> 5.24
> 0.679
> 0.77
> 5.11
> SUPER
> 顾问 KZ79256 (Rank 21)
> 2025-02-26
> 1.0
> ANPmEdE
> USA
> T0P3000
> 5.07
> 0.5992
> 0.77
> 5.09
> SUPER
> 顾问 KZ79256 (Rank 21)
> 2025-02-25
> 1.0
> PRNrKAJ
> USA
> T0P3000
> 5.77
> 0.675
> 0.77
> 5.49
> SUPER
> 顾问 KZ79256 (Rank 21)
> 2025-02-24
> 1.0
> IdWOMENI
> USA
> T0P3000
> 7.02
> 0.6863
> 0.77
> REGULAR Alpha
> Tee_regUlar
> TDe
> JUthOI
> JateSubmitteo
> Themes
> pyramids
> alphald
> reSIOI
> Unwerse
> Titness
> delay
> prodCorrelation
> ValueFactor
> 4.26
> REGULAR
> 顾问 KZ79256 (Rank 21)
> 2025-02-26
> 1.0
> 28b3YW1
> EUR
> T0P2500
> 1.09
> 0.6929
> 0.77
> 3.98
> REGULAR
> 顾问 KZ79256 (Rank 21)
> 2025-02-27
> 1.0
> KONVWOO
> EUR
> T0P2500
> 1.12
> 0.6993
> 0.77
> 1an
> REGULAR
> 顾问 KZ79256 (Rank 21)
> 2025-02-28
> 1.0
> X3V1ZVn
> EUR
> T0P2500
> 1.09
> 0.5627
> 077


这部分的核心主要是把每天的收入实时展示，我也可以不用因为收入专门查看网页了，并且按照base payment的计算方式展示出相应的影响因素，为了后续分析收入提供便利

这部分代码也不展示了，只是说一下思路

按钮可以使用

cols = st.columns(3)

cols[0].button("刷新收入数据", on_click=reload_fee_data, use_container_width=True)

**当然也可以监控更多的东西，但是我现在没有想到还要弄啥监控，慢慢更这个帖子吧**

**顾问 worldquant brain赛博游戏王 的解答与建议**:
大佬太牛了


---

### 技术对话片段 98 (原帖: 【课代表📕】关于2阶段的改进，字段方向Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 【课代表】关于2阶段的改进字段方向Alpha Template_31503981064087.md
- **时间**: 1年前

**提问/主帖背景 (XX42289)**:
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


**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的帖子，点赞。

按照这个思路推下去，感觉能造出更多的分组


---

### 技术对话片段 99 (原帖: 一点新人建议)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一点新人建议_28771138669207.md
- **时间**: 1年前

**提问/主帖背景 (YW13378)**:
本人由于工作党，平时可利用的闲暇时间不多，目前还处于跑模版回测阶段，刚开始跑的数据集可能是大家都跑过，没有什么可提交的alpha了，所以获得顾问权限之后有段时间一直没有提交alpha，直到我尝试了新的数据集，突然一天出现了好几个alpha，才给了我一点信心，然后开始尝试更多新的数据集，每天能出一两个alpha，最近才慢慢总结一点心得。

在数据集的选择上，通过初步的测试，我筛选出了表现优异的数据集，对于那些初期表现不佳的数据集，需要及时调整策略，避免在低效的资源上浪费过多时间。我尝试用模板回测Fundamental、Other和Model的数据集比较多，大多数alpha也是从这几个数据集出来的，而Risk和News比较难用模板回测出alpha。

对于表现良好的数据集，我尝试了不同的Region和参数设置。我发现即使是同一个数据集，在不同的条件下也可能展现出不同的潜力。地区的选择上，我出alpha最多的地区是USA，其次是JPN，TWN比较难回测出alpha。

我深知，量化研究是一个不断学习和进步的过程，在下一个阶段回测中，我也会尽量多理解代码背后的逻辑，为手搓代码、读论文做准备。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
想问一下，不同的region中相同alpha的可比性强吗？我自己实验下来，发现换地区的话，信号可能不会那么强烈了。

此外，很好的帖子和经验分享，点赞。


---

### 技术对话片段 100 (原帖: 示例代码继续使用 df1)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一键检验alpha稳定plus 版本代码优化_32415931097623.md
- **时间**: 1年前

**提问/主帖背景 (YZ70114)**:
原贴：
 [[Commented] 一键检验alpha稳定性代码优化_32008506789655.md?input_string=%E4%B8%80%E9%94%AE%E6%A3%80%E9%AA%8Calpha%E7%A8%B3%E5%AE%9Aplus%20%E7%89%88%E6%9C%AC]([Commented] 一键检验alpha稳定性代码优化_32008506789655.md?input_string=%E4%B8%80%E9%94%AE%E6%A3%80%E9%AA%8Calpha%E7%A8%B3%E5%AE%9Aplus%20%E7%89%88%E6%9C%AC)  
@ [顾问 JL71699 (Rank 64)](/hc/en-us/profiles/23363707892759-顾问 JL71699 (Rank 64))   感谢JL 大佬的初版，以及kitty 哥 [DZ31817](/hc/en-us/profiles/25751669201943-DZ31817)  发的有关decay 的研究图

对于原版一键检验alpha稳定性 做了下优化

1. decay 直接填写固定值遍历

2.  ASI 地区最近需要强制开启maxTrade 做了修改

3. dataframe 打印format 出百分比和万分比数值，显示更直观

4.画图修改使用plotly 画图


> [!NOTE] [图片 OCR 识别内容]
> alpha_id
> sharpe
> ftness
> turnover
> margin
> returns
> drawdown
> neutralization
> decay
> JoL8KGE
> 1.8700
> 1.2400
> 4.21%
> 26.35%0。
> 5.54%
> 5.00%
> 24
> 8VqGP3o
> 1.8800
> 1.2400
> 3.29%
> 33.28%o。
> 5.48%
> 5.28%
> COUNTRY
> OReP3K5
> 1.8300
> 1.2100
> 6.15%
> 17.78%o。
> 5.46%
> 5.04%
> 12
> pXgWKZX
> 1.8900
> 1.2600
> 3.70%
> 29.9790。
> 5.54%
> 5.06%
> 32
> GXVQKJZ
> 1.8700
> 1.2300
> 3.12%
> 34.82%o。
> 5.44%
> 5.40%
> W3VNVmQ
> 1.2000
> 0.7200
> 6.71%
> 13.44%o。
> 4.51%
> 5.77%
> 32
> joQVPJO
> 1.2900
> 0.7900
> 3.36%
> 27.73%0。
> 4.66%
> 5.46%
> CROWDING
> 24
> JoL3N8e
> 1.2800
> 0.7800
> 3.53%
> 26.32%o。
> 4.64%
> 5.76%
> 12
> W3myglk
> 1.2700
> 0.7700
> 3.95%
> 23.5796o。
> 4.65%
> 5.43%
> 32
> GZbGdrJ
> 1.2400
> 0.7300
> 3.23%
> 27.189o。
> 4.39%
> 6.60%
> 24
> nmb6P3a
> 1.2100
> 0.7100
> 3.40%
> 25.35%o0
> 4.31%
> 6.66%
> INDUSTRY
> 12
> ae3RPr9
> 1.1700
> 0.6800
> 3.83%
> 21.95%o0
> 4.21%
> 6.59%
> W3VNVgd
> 1.1000
> 0.6300
> 6.45%
> 12.56%o。
> 4.05%
> 6.81%
> 12
> dYwgneg
> 1.3100
> 0.8500
> 3.59%
> 29.08%o
> 5.22%
> 5.89%
> 32
> XValzzm
> 1.3200
> 0.8500
> 3.01%
> 34.66%o。
> 5.22%
> 5.53%
> MARKET
> 24
> VZVYrbQ
> 1.3100
> 0.8500
> 3.18%
> 32.81%o。
> 5.21%
> 5.96%
> PXEPgVK
> 1.2400
> 0.7900
> 6.17%
> 16.46%o。
> 5.08%
> 6.28%
> 24
> 31WGPGX
> 1.2500
> 0.7700
> 3.24%
> 29.149o。
> 4.73%
> 6.62%
> 12
> XVENkda
> 1.2300
> 0.7500
> 3.66%
> 25.65%o
> 4.69%
> 6.59%
> SECTOR
> 32
> dYWSaRX
> 1.2600
> 0.7800
> 3.08%
> 30.87960。
> 4.75%
> 6.54%
> kv58526
> 1.1600
> 0.7000
> 6.25%
> 14.50%o。
> 4.53%
> 6.92%
> 24
> pxgWjnj
> 1.3700
> 0.6500
> 5.50%
> 10.2796o。
> 2.82%
> 3.31%
  
> [!NOTE] [图片 OCR 识别内容]
> 值: 629861.00
> JOL3NBe
> V
> 日期: Aug 2013
> 类别
> 值:317795.00
> JoLSKGE
> pxgWjnj
> Ygdlnz6
> 日期: Aug 2013
> W3VNVgd
> 值:164238.00
> kv58526
> 8VqGP3o
> PXEPSVK
> 日期:
> 2013
> 值: 669117.00
> W3VNVmQ
> kv5gagp
> PXgWJd6
> 日期: Aug 2013
> OReP3K5
> 值: 242876.00
> PXgW8ZV
> GZbGdr]
> ae3RPrg
> 日期: Aug 2013
> XVENkda
> 值:  362257.00
> dywgneg
> dYWSaRX
> 日期: Aug 2013
> W3mYglk
> 值: 485718.00
> 8VqGLNa
> XValzzm
> PXgWKZX
> 日期: Aug 2013
> ORePqmb
> V
> 值:  624793.00
> nmb6p3a
> joQVPJO
> 3IWGPGX
> 日期: Aug 2013
> 值:319511.00
> VZVYrbQ
> 0
> JoL3N8e
> eNJ1ZJ6
> 日期: Aug 2013
> pxgWjnj
> 值:167190.00
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> GXVQKJZ
> 日期
> 日期: Aug 2013
> 值: 642972.00
> Aug


#一键检验稳定性
import time
import json
import requests
import pandas as pd
import numpy as np
import requests
from requests.auth import HTTPBasicAuth
from urllib.request import urlopen

#这里填alpha
alpha_id_ori='jxRvMmj'
force_truncation = None

def login():
    username = "你的账号"
    password = "你的密码"

# Create a session to persistently store the headers
    s = requests.Session()

    # Save credentials into session
    s.auth = (username, password)

    # Send a POST request to the /authentication API
    response = s.post(' [[链接已屏蔽]) ')
    print(response.content)
    return s

s = login()

#=========================================

def locate_alpha(s, alpha_id):
    while True:
        alpha = s.get(" [[链接已屏蔽]) " + alpha_id)
        if "retry-after" in alpha.headers:
            time.sleep(float(alpha.headers["Retry-After"]))
        else:
            break
    string = alpha.content.decode("utf-8")
    metrics = json.loads(string)
    # print(metrics["regular"]["code"])

dateCreated = metrics["dateCreated"]
    sharpe = metrics["is"]["sharpe"]
    fitness = metrics["is"]["fitness"]
    turnover = metrics["is"]["turnover"]
    margin = metrics["is"]["margin"]
    returns = metrics["is"]["returns"]
    drawdown = metrics["is"]["drawdown"]
    decay = metrics["settings"]["decay"]
    exp = metrics["regular"]["code"]
    universe = metrics["settings"]["universe"]
    truncation = metrics["settings"]["truncation"]
    neutralization = metrics["settings"]["neutralization"]
    region = metrics["settings"]["region"]
    testPeriod = metrics["settings"]["testPeriod"]

# triple =pd.DataFrame([[alpha_id,  sharpe, turnover, fitness, margin]])
    triple = [
        alpha_id,
        sharpe,
        turnover,
        fitness,
        margin,
        exp,
        region,
        universe,
        neutralization,
        decay,
        truncation,
        testPeriod,
        returns,
        drawdown,
    ]
    return triple

sharp_list = []
df = pd.DataFrame(columns=["alpha_id", "sharpe", "turnover", "fitness", "margin","returns","drawdown"])

alpha_line = []
tem = locate_alpha(s, alpha_id_ori)

[
    alpha_id,
    sharpe,
    turnover,
    fitness,
    margin,
    exp,
    region,
    universe,
    neutralization,
    decay,
    truncation,
    testPeriod,
    returns,
    drawdown,
] = tem
use_truncation = truncation
if force_truncation is not None and force_truncation > 0:
    use_truncation = force_truncation

# 根据 decay 的值选择不同的 decay_tem 列表
decay_tem_list = [0, 1, 5, 20, 60]

# 固定的 neutralization_tem 列表
neutralization_tem_list = [
    "SUBINDUSTRY",
    "INDUSTRY",
    "SECTOR",
    "MARKET",
    "CROWDING",
    "STATISTICAL",
    "SLOW_AND_FAST",
    "FAST",
    "SLOW",
    "REVERSION_AND_MOMENTUM"
]
if region == "ASI" or region == "EUR" or region == "GLB":
    neutralization_tem_list.append("COUNTRY")
# neutralization_tem_list = ['SUBINDUSTRY']
# 使用列表推导式生成 simulation_data
max_trade = "OFF"
if region == "ASI":
    max_trade = "ON"
alpha_line.extend(
    {
        "type": "REGULAR",
        "settings": {
            "instrumentType": "EQUITY",
            "region": region,
            "universe": universe,
            "delay": 1,
            "decay": decay_tem,
            "neutralization": neutralization_tem,
            "truncation": use_truncation,
            "pasteurization": "ON",
            "unitHandling": "VERIFY",
            "nanHandling": "ON",
            "language": "FASTEXPR",
            "visualization": True,
            "testPeriod": testPeriod,
            "maxTrade": max_trade,
        },
        "regular": exp,
    }
    for decay_tem in decay_tem_list
    for neutralization_tem in neutralization_tem_list
)
alpha_total = len(alpha_line)
print(f"total simulate {alpha_total} alphas")
wbs = []
for alpha_data in alpha_line:
    while True:
        count = 0
        try:
            # Send multisimulation request
            response = s.post(
                " [[链接已屏蔽]) ", json=alpha_data
            )
            # Check response

if len(response.headers["Location"]) > 0:
                print(
                    f"Alpha location get successfully: {response.headers['Location']}"
                )
                wbs.append(response.headers["Location"])
                break
        except:
            count = count + 1
            # s = sign_in(username, password)
            print("Error in sending simulation request. And retry after 5s")
            time.sleep(5)
            if count > 10:
                s = login()
            if count > 30:
                break
print(len(wbs))

#========================================

df_list = []
df_list = pd.DataFrame(
    columns=[
        "alpha_id",
        "neutralization",
        "decay",
        "sharpe",
        "fitness",
        "turnover",
        "margin",
        "returns",
        "drawdown"
    ]
)
tem = locate_alpha(s, alpha_id_ori)
[
    alpha_id_ori,
    sharpe,
    turnover,
    fitness,
    margin,
    exp,
    region,
    universe,
    neutralization,
    decay,
    truncation,
    testPeriod,
    returns,
    drawdown,
] = tem
new_row = [alpha_id_ori, neutralization, decay, sharpe, fitness, turnover, margin, returns, drawdown]
df_list.loc[len(df_list)] = new_row
print(df_list)

for wb in wbs:
    # 发送请求
    url = wb
    while 1:  # 对1个simulated测试
        data = s.get(url).text
        if "progress" not in data and "error" not in data:
            json_data = json.loads(data)  # 将文本转为字典
            alpha_value = json_data["alpha"]  # 直接获取 alpha 字段
            print(alpha_value)
            tem = locate_alpha(s, alpha_value)
            [
                alpha_id,
                sharpe,
                turnover,
                fitness,
                margin,
                exp,
                region,
                universe,
                neutralization,
                decay,
                truncation,
                testPeriod,
                returns,
                drawdown,
            ] = tem
            new_row = [
                alpha_id,
                neutralization,
                decay,
                sharpe,
                fitness,
                turnover,
                margin,
                returns,
                drawdown,
            ]
            df_list.loc[len(df_list)] = new_row  # 直接赋值（确保 df 已初始化列名）
            break
        else:
            print("progressing")
            time.sleep(60)
            continue
df_list = df_list.drop_duplicates(subset="alpha_id", keep="first")

#=========================================

#显示df 数据
print(alpha_id_ori)

df_sorted = df_list.sort_values("neutralization")
df_multiindex = df_sorted.set_index(["neutralization", "decay"])

#df 数据做处理，returns turnover，drawdown 显示为百分比后面加%，margin 显示万分比后面加‱
df_multiindex['returns'] = df_multiindex['returns'] * 100
df_multiindex['turnover'] = df_multiindex['turnover'] * 100
df_multiindex['drawdown'] = df_multiindex['drawdown'] * 100
df_multiindex['margin'] = df_multiindex['margin'] * 10000

# 使用styler格式化显示，添加百分号和万分号
styled_df = df_multiindex.style.format({
    'returns': '{:.2f}%',
    'turnover': '{:.2f}%', 
    'drawdown': '{:.2f}%',
    'margin': '{:.2f}‱',
    'sharpe': '{:.4f}',
    'fitness': '{:.4f}'
})

styled_df

#=========================================

from time import sleep
def get_pnl(s, alpha_id):
    finished = False
    while True:
        pnl = s.get(' [[链接已屏蔽]) ' + alpha_id + '/recordsets/pnl')
        if pnl.headers.get('Retry-After', 0) == 0:
             break
        print('Sleeping for ' + pnl.headers['Retry-After'] + ' seconds')
        sleep(float(pnl.headers['Retry-After']))
    # print('PNL retrieved')
    return pnl

df1 = pd.DataFrame()

for alpha_id in df_list['alpha_id'].unique():
    print(alpha_id)
    json_data = get_pnl(s, alpha_id).json()['records']
    df = pd.DataFrame(json_data)
    df=df.iloc[:,0:2]
    df.columns = ['date', alpha_id]
    df.set_index('date', inplace=True)
    df1 = pd.merge(df1, df, left_index=True, right_index=True, how='outer')

df1.index = pd.to_datetime(df1.index)
start_time=df1.index[0]-pd.Timedelta(days=1)
start_time

#=========================================

import plotly.graph_objects as go

# 假设 df1 是你的时间序列 DataFrame，行索引是日期，列是不同的曲线
# 示例代码继续使用 df1
fig = go.Figure()

for col in df1.columns:
    fig.add_trace(go.Scatter(
        x=df1.index,
        y=df1[col],
        mode='lines',
        name=col,
        hovertemplate=(
            f"<b>{col}</b><br>"
            "日期: %{x}<br>"
            "值: %{y:.2f}<extra></extra>"
        )
    ))

fig.update_layout(
    title="多时间序列对比",
    xaxis_title="日期",
    yaxis_title="数值",
    legend_title="类别",
    width=1000,
    height=600,
    template="plotly_white",
    hovermode='x unified'
)

fig.show()

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的改善 ，点赞！

同时 也想问一下，我在用的时候会出现，跑完，get到一半就 出错 的情况，这个要怎么解决呢？

========================================================================

“王牌总是在最后出场”——《游戏王》

========================================================================


---

### 技术对话片段 101 (原帖: 一键检验alpha稳定性代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 一键检验alpha稳定性代码优化_32008506789655.md
- **时间**: 1年前

**提问/主帖背景 (JL71699)**:
很多顾问提交的alpha都是machine alpha，就会遇到一个问题，如何检验稳定性，通过常规方法就是改变neutralization和decay观察信号是否有明显的变化，于是我就有下面的思路，原理是我输一个id，get了alpha的信息，修改alpha setting，就自动发送命令，然后抢线发送，然后顺着发送的链接，get到alphaid再爬回来稳定性检验alpha的数据及pnl，之后本地绘制pnl并且绘制表格，给出对比

只需要输入想进行稳定性分析的alphaid，就能得到下面的图像，具体的稳定性测试方法可以在代码中进行修改。

具体代码我已经开源到研究小组，有需要可自取 [[链接已屏蔽])

下图为示例，并且会有跟随的alpha表格（具体未展示）


> [!NOTE] [图片 OCR 识别内容]
> 126
> 多时间序列邓比
> WO7qbpx
> PSLrOZWI
> 7YPqAd1
> VATnqMQ
> MGvlog6
> XTWMOII
> gaNqvlQ
> QORrm7r
> LKobeMe
> LKobq7m
> 日期
> rTa6QPI
> 2014
> 2015
> 2018
> 2019
> 2013
> 2016
> 2017
> 2020
> 2022
> 2023
> 2021


**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢jl大佬的分享，以往的鲁棒性检验都得停掉一个槽，网页单独跑，如今有大佬的代码帮助，属实是轻松了许多。感谢大佬开源！！！


---

### 技术对话片段 102 (原帖: 为什么有些人有那么多alpha可以挖呢？ 我ppa都 1 的相关性了)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 为什么有些人有那么多alpha可以挖呢 我ppa都 1 的相关性了_33039213327255.md
- **时间**: 1年前

**提问/主帖背景 (LM81527)**:
为什么有些人有那么多alpha可以挖呢？ 我ppa都 1 的相关性了，真不知道那些大佬是怎么做的

**顾问 worldquant brain赛博游戏王 的解答与建议**:
不要再小范围内深挖，优先广度，其次深度，一个数据集一个字段一直挖不能长久的，要不断跑起来，wq一直有催人跑的感觉。======================================================================================================================


---

### 技术对话片段 103 (原帖: && author_fitness > 0.2)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 今日SA_33139583623447.md
- **时间**: 1年前

**提问/主帖背景 (QZ67721)**:
bool = (

not (own)

&&in(competitions,"HCAC2025")

&&(neutralization == 'FAST')

&&datacategory_count<=3

&& datafield_count <= 4

&&short_count+long_count> universe_size(universe)/2

&& (( self_correlation <0.2) || (self_correlation <0.4 ||self_correlation >0.2)||(self_correlation >0.45) )

# && author_fitness > 0.2

);

weight = (

1

*((long_count+ short_count)/ universe_size(universe))

*if_else(prod_correlation > 0.7, 2, 1.5)

*(1 - self_correlation)

*(1 / datafield_count)

);

bool * weight

combo：1

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的select，感谢分享

但还是有个小问题，为什么会设置    *if_else(prod_correlation > 0.7, 2, 1.5)，按道理来说，prod越高的应该给越小的权重才对？


---

### 技术对话片段 104 (原帖: 今晚SA顾问培训的一点收获)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 今晚SA顾问培训的一点收获_33042870306967.md
- **时间**: 1年前

**提问/主帖背景 (LW67640)**:
Phd大佬上次分享的combo表达式很多人都在用，这次又来了。

觉得最有收获的就是里面的一句话：

Try limiting number of selected component Alphas by using filters in expression, not selection limit setting.

这个观点有意思，我之前都是通过限制数量达到控制筛选的数量，通过表达式的层层限制来控制数量，对我来说有一种只可意会不可言传的感觉。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
Try limiting number of selected component Alphas by using filters in expression, not selection limit setting.

有意思，层层限制，大浪淘金的感觉，点赞。


---

### 技术对话片段 105 (原帖: 保证os表现和提升vf——多样性和稳健性)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 保证os表现和提升vf多样性和稳健性_33046136707991.md
- **时间**: 1年前

**提问/主帖背景 (MY27687)**:
审查多样性提示（“Review the diversification tips listed under the Quality Factor flow chart”），以确保Alpha在不同主题、数据源和策略中保持多样化。这有助于提升Value Factor的长期稳定性。通过系统化评估Alpha因子的多维分散性，增强价值因子的长期鲁棒性。在样本外（Out-of-Sample, OS）阶段，Alpha的稳健性至关重要，因为这是测试策略是否能够在真实市场环境中保持良好表现的关键时期。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的建议，感谢分享

审查多样性提示（“Review the diversification tips listed under the Quality Factor flow chart”），以确保Alpha在不同主题、数据源和策略中保持多样化。这有助于提升Value Factor的长期稳定性。通过系统化评估Alpha因子的多维分散性，增强价值因子的长期鲁棒性。在样本外（Out-of-Sample, OS）阶段，Alpha的稳健性至关重要，因为这是测试策略是否能够在真实市场环境中保持良好表现的关键时期。


---

### 技术对话片段 106 (原帖: 保证os表现和提升vf——提升Self-Growth Factor（自我成长因子）)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 保证os表现和提升vf提升Self-Growth Factor自我成长因子_33095509286295.md
- **时间**: 1年前

**提问/主帖背景 (MY27687)**:
性能监控：定期计算Alpha的平均性能（“Compute the avg. performance (Sharpe, correlation etc.) of your submitted alphas”），并评估是否在过去几周中提交了更高质量的Alpha（“Are you submitting better quality Alphas over time?”）。
持续创新：如果提交数量和质量未见提升，保持创新（“Keep improving over time and continue innovating”），尝试使用“bucket”和“density”操作符（neutralizing operators）来优化Alpha。
避免过度优化：不要故意恶化Alpha的表现以通过相关性测试（“Do not intentionally worsen your Alphas performance just to pass correlation test”），这可能会损害OS阶段的稳健性。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的帖子，感谢分享。

性能监控：定期计算Alpha的平均性能（“Compute the avg. performance (Sharpe, correlation etc.) of your submitted alphas”），并评估是否在过去几周中提交了更高质量的Alpha（“Are you submitting better quality Alphas over time?”）。
持续创新：如果提交数量和质量未见提升，保持创新（“Keep improving over time and continue innovating”），尝试使用“bucket”和“density”操作符（neutralizing operators）来优化Alpha。
避免过度优化：不要故意恶化Alpha的表现以通过相关性测试（“Do not intentionally worsen your Alphas performance just to pass correlation test”），这可能会损害OS阶段的稳健性。


---

### 技术对话片段 107 (原帖: 兄弟们, 今晚8:00全球会议)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 兄弟们 今晚800全球会议_33037250763287.md
- **时间**: 1年前

**提问/主帖背景 (ZX58901)**:
兄弟们, 今晚8:00全球会议

不要忘记参加

 **Build your skills with SuperAlpha's Research Session** 

Date & Time
Jun 25, 2025 05:30 PM India

Webinar ID
936 8164 5775

Description
Join us on

Jun 05- Introduction to SuperAlpha Competition 2025
Jun 25- Tips for acing in SuperAlpha Competition 2025

**顾问 worldquant brain赛博游戏王 的解答与建议**:
收到，感谢提醒

 **Build your skills with SuperAlpha's Research Session** 

Date & Time
Jun 25, 2025 05:30 PM India

Webinar ID
936 8164 5775

Description
Join us on

Jun 05- Introduction to SuperAlpha Competition 2025
Jun 25- Tips for acing in SuperAlpha Competition 2025


---

### 技术对话片段 108 (原帖: 关于冲Pyramid的一点心得)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 关于冲Pyramid的一点心得_28674188909207.md
- **时间**: 1年前

**提问/主帖背景 (JL11546)**:
大家好。最后半个月计划冲一下Master试试。这周我用了5天时间获得了10个Pyramid，达到了Master级别。分享一些冲Pyramid的思考，希望能对各位有所帮助。

1. 优先选择一些包含多个catergories的模板。有些模板跑出一个alpha可以获得两个甚至三个categories，这会显著提高我们点亮Pyramid的效率。比如@TL87739同学提供的模板效率就很高：

```
regression_neut(group_zscore(group_neutralize(ts_zscore(ts_backfill({data1},120),120),densify(bucket(rank(ts_backfill({market_cap or enterprise_value or revenue or sales},120)),range='0,1,0.1'))),densify(industry)),group_neutralize(ts_zscore(ts_backfill({{market_cap or enterprise_value or revenue or sales}},120),120),densify(industry)))
```

这个模板选择analyst和model字段可以同时获得fundamental的category，并且这个模板在ASI, CHN, KOR, TWN, HKG这几个region的效率都很不错。

2. 一个模板如果跑了5000个simulations以上还没有信号就尽快更换模板，不要在一个模板上浪费时间。我这5天使用了9个模板，其中只有4个模板挖到了alpha。如果在一个模板上纠结可能会浪费大量的时间

3. 使用多线程进行回测，能显著提升效率，代码我参考的这篇文章。

[使用协程方式提高Multi-simulation效率代码框架分享]([L2] 使用协程方式提高Multi-simulation效率代码框架分享_28236334008855.md)

4. 对因子的调整：

（1）可以使用hump，ts_delta_limit降低turnover；

（2）可以使用signed_power和trade_when降低IS_Ladder和Prod_Corr；

（3）CHN的字段如果各项标准差的不多可以尝试降低Decay，使用Crowding的中性化尝试挽救一下；

5. 放弃一些region和categories。我发现我在Delay0的全部,region Delay1的EUR, JPN, AMR这几个region里面挖到的Alpha数量寥寥无几，所以我放弃了上述的region，并且优先跑了analyst, model, fundamental, pv这些categories。另外sentimen比较意外的好出alpha，值得尝试。

以上就是我的在冲Pyramid中的一点心得，祝各位都能获得自己期望的Genius Level！

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的评论，点赞。


---

### 技术对话片段 109 (原帖: 关于回测量与模板alpha的平衡)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 关于回测量与模板alpha的平衡_31042344584855.md
- **时间**: 1年前

**提问/主帖背景 (DP37881)**:
在通过顾问part2的课程后了解了想要更多,质量更好的alpha势必需要不断寻找模板,了解数据集以把算力尽可能多的放在有背景的模板和数据上,但是这部分做法一般得到的alpha总数并不会很多,一般是几千甚至几百,若放到代码回测很可能下次查看时早已跑完,我大约持续了3~4天,日回测量大幅下降,考虑到大家都对日回测量非常重视,我开始思考如何平衡,毕竟我还是没有很快构建出新模板代码的水平。

综合考虑后我决定重拾一二三阶模板,以USA中各字段的人数与alpha为基准,在EUR,ASI等区域找到人数、alpha数较少的数据放到一二三阶模板中,回测时只开7个multi_simulate,剩下的部分留给产量少质量可能好的模板alpha,保证回测数量的同时相对综合了我产出低的情况,希望能给各位一些灵感,也希望能得到大佬们的指点。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
针对你的问题，一种可能的解决方式是打开思路，针对模版中所要求的数据集 进行优化，例如如果需要analyst类型，可以在所有数据中找到与分析师有关的数据，可能在model和sentiment里面有，把所有沾边的放进去，这样就可以增大搜索空间。另一种可能的解决方式是修改模版，最简单的例子就是：一些模版要求matrix数据，但你可以把matrix换成vector，只需要加入对应的运算符就可以了。以上两种思路供参考。


---

### 技术对话片段 110 (原帖: 搜索包含特定操作符的Alpharesults = cache.search_by_expression("rank")搜索特定数据字段results = cache.search_by_expression("close"))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 分享一个alpha_info 和 alpha_pnl 存储到本地的代码模板SQLite版代码优化_32443272850967.md
- **时间**: 1年前

**提问/主帖背景 (LH94963)**:
分享一个基于SQLite的缓存alpha类，专门用于缓存Alpha info、yearly_stats 和 PnL 数据。

主要包含两个 SQLite 库：

1. AlphaInfoCache - Alpha因子信息缓存
- 基础缓存：存储Alpha因子的基本信息（表达式、设置、性能指标等）
- 年度统计缓存：独立存储Alpha的年度统计数据
- 条件筛选：支持基于JSON字段的复杂查询
- 表达式搜索：支持模糊匹配Alpha表达式

2. AlphaPnlCache - PnL数据缓存
- 原始数据存储：缓存Alpha的损益数据
- 快速检索：基于alpha_id的高效查询

一些使用示例：

- JSON查询

```
cache = AlphaInfoCache()# 复杂条件筛选conditions = {    "pfm.fitness": (">", 1.5),      # fitness > 1.5    "pfm.turnover": ("<", 30),       # turnover < 30    "pfm.sharpe": (">", 0.8)         # sharpe > 0.8}# 可选择特定alpha进行筛选alpha_ids = ["123456", "789012"]filtered_alphas = cache.filter(conditions, alpha_ids)
```

- 表达式搜索

```
# 搜索包含特定操作符的Alpharesults = cache.search_by_expression("rank")# 搜索特定数据字段results = cache.search_by_expression("close")
```

完整代码如下

```
import sqlite3import jsonfrom typing import Optional, Dictimport loggingfrom pathlib import Pathimport osclass AlphaInfoCache:    def __init__(self):        root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")        db_path = os.path.join(root_path, "results", "alpha_info.db")        self.db_path = Path(db_path)        self._init_db()    def _init_db(self):        with sqlite3.connect(self.db_path) as conn:            conn.execute('''                CREATE TABLE IF NOT EXISTS alpha_info (                    alpha_id TEXT PRIMARY KEY,                    data TEXT NOT NULL,                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                )            ''')            conn.execute('''                CREATE TABLE IF NOT EXISTS alpha_yearly_stats (                    alpha_id TEXT PRIMARY KEY,                    data TEXT NOT NULL,                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                )            ''')            conn.commit()    def get(self, alpha_id: str) -> Optional[Dict]:        try:            with sqlite3.connect(self.db_path) as conn:                cursor = conn.execute(                    'SELECT data FROM alpha_info WHERE alpha_id = ?',                    (alpha_id,)                )                result = cursor.fetchone()                return json.loads(result[0]) if result else None        except Exception as e:            logging.error(f"Cache get error: {str(e)}")            return None    def set(self, alpha_id: str, data: Dict) -> bool:        try:            with sqlite3.connect(self.db_path) as conn:                conn.execute(                    '''INSERT OR REPLACE INTO alpha_info                     (alpha_id, data) VALUES (?, ?)''',                    (alpha_id, json.dumps(data))                )                conn.commit()                return True        except Exception as e:            logging.error(f"Cache set error: {str(e)}")            return False        def get_yearly_stats(self, alpha_id: str) -> Optional[Dict]:        try:            with sqlite3.connect(self.db_path) as conn:                cursor = conn.execute(                    'SELECT data FROM alpha_yearly_stats WHERE alpha_id = ?',                    (alpha_id,)                )                result = cursor.fetchone()                return json.loads(result[0]) if result else None        except Exception as e:            logging.error(f"Yearly stats cache get error: {str(e)}")            return None    def set_yearly_stats(self, alpha_id: str, data: Dict) -> bool:        try:            with sqlite3.connect(self.db_path) as conn:                conn.execute(                    '''INSERT OR REPLACE INTO alpha_yearly_stats                     (alpha_id, data) VALUES (?, ?)''',                    (alpha_id, json.dumps(data))                )                conn.commit()                return True        except Exception as e:            logging.error(f"Yearly stats cache set error: {str(e)}")            return False        def filter(self, conditions: Dict[str, tuple], alpha_ids: Optional[list] = None) -> list:        """        根据条件筛选数据。        :param conditions: 筛选条件字典，格式为 {"字段路径": (操作符, 值)}。                           例如：{"is.fitness": (">", 1), "is.turnover": ("<", 30)}        :param alpha_ids: 可选参数，指定 alpha_id 数组进行筛选。        :return: 符合条件的数据列表。        """        try:            # 构建查询条件            query_conditions = []            params = []            # 添加 JSON 字段条件            for field_path, (operator, value) in conditions.items():                query_conditions.append(f"json_extract(data, '$.{field_path}') {operator} ?")                params.append(value)            # 添加 alpha_id IN (...) 条件            if alpha_ids:                placeholders = ", ".join(["?"] * len(alpha_ids))  # 动态生成占位符                query_conditions.append(f"alpha_id IN ({placeholders})")                params.extend(alpha_ids)            # 拼接完整的 SQL 查询            where_clause = " AND ".join(query_conditions)            query = f"SELECT data FROM alpha_info WHERE {where_clause}"            # 执行查询            with sqlite3.connect(self.db_path) as conn:                cursor = conn.execute(query, params)                results = cursor.fetchall()            # 解析结果            return [json.loads(row[0]) for row in results]        except Exception as e:            logging.error(f"Filter error: {str(e)}")            return []        def search_by_expression(self, pattern: str) -> list:        """        根据表达式模式在alpha信息中进行模糊搜索                Args:            pattern: 要匹配的表达式模式                Returns:            匹配到的alpha信息列表        """        try:            pattern_with_wildcards = f"%{pattern}%"                        with sqlite3.connect(self.db_path) as conn:                cursor = conn.execute(                    "SELECT data FROM alpha_info WHERE json_extract(data, '$.exp') LIKE ?",                    (pattern_with_wildcards,)                )                # 与filter方法保持一致的返回格式                return [json.loads(row[0]) for row in cursor.fetchall()]        except Exception as e:            logging.error(f"搜索表达式时出错: {e}")            return []class AlphaPnlCache:    def __init__(self):        root_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")        db_path = os.path.join(root_path, "results", "alpha_pnl.db")        self.db_path = Path(db_path)        self._init_db()    def _init_db(self):        with sqlite3.connect(self.db_path) as conn:            conn.execute('''                CREATE TABLE IF NOT EXISTS alpha_pnl (                    alpha_id TEXT PRIMARY KEY,                    raw_data TEXT NOT NULL,                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP                )            ''')            conn.commit()    def get(self, alpha_id: str) -> Optional[dict]:        try:            with sqlite3.connect(self.db_path) as conn:                cursor = conn.execute(                    'SELECT raw_data FROM alpha_pnl WHERE alpha_id = ?',                    (alpha_id,)                )                result = cursor.fetchone()                return json.loads(result[0]) if result else None        except Exception as e:            logging.error(f"Pnl cache get error: {str(e)}")            return None    def set(self, alpha_id: str, raw_data: dict) -> bool:        try:            with sqlite3.connect(self.db_path) as conn:                conn.execute(                    '''INSERT OR REPLACE INTO alpha_pnl                     (alpha_id, raw_data) VALUES (?, ?)''',                    (alpha_id, json.dumps(raw_data))                )                conn.commit()                return True        except Exception as e:            logging.error(f"Pnl cache set error: {str(e)}")            return False
```

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的代码，感谢分享，我的sql水平仅限于select* from，看来要好好练一下了

===生活就像海洋，只有意志坚强的人才能到达彼岸===

===This is an apple, I like apples, apples are good for our health===


---

### 技术对话片段 111 (原帖: 分享一个"反转类"因子)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 分享一个反转类因子_33036857595543.md
- **时间**: 1年前

**提问/主帖背景 (QP72475)**:
```
rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2), 5))
```

经过简化后，可以理解为：

```
当收益率<0时：rank(stddev(returns, 20)^2)
否则：rank(close^2)
然后取过去5天的最大值
```

## 因子逻辑解析

1. **条件判断** ：首先判断股票当日收益率是否为负
   - 如果收益率为负，计算该股票过去20天收益率的标准差
   - 如果收益率为正，直接使用收盘价
2. **平方处理** ：对得到的值进行平方处理，放大差异
3. **排名处理** ：在横截面上对所有股票进行排名
4. **时间序列最大值** ：取过去5天排名值的最大值

## 因子意义

1. **反转效应** ：当股票出现负收益时，因子关注其波动率，波动率大的股票可能面临更大的反转压力
2. **动量延续** ：当股票出现正收益时，因子关注价格本身，可能捕捉动量延续
3. **风险控制** ：通过波动率衡量，间接控制了风险

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享，很有用，感觉后续可以抽象成模版跑machinealpha，点赞！！！！！！！！！！！！！！

```
rank(Ts_ArgMax(SignedPower(((returns < 0) ? stddev(returns, 20) : close), 2), 5))
```


---

### 技术对话片段 112 (原帖: coroutine)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 利用delete simulation api节省重启脚本的时间代码优化_31525106377879.md
- **时间**: 1年前

**提问/主帖背景 (WP88606)**:
使用代码跑回测时，经常（至少本人经常【流汗】）因为写错配置或其他原因需要提前结束脚本，暴力的kill掉进程后，如果直接重启程序，因为之前simulation还在Brain后台跑，占用着卡槽，会导致location error。

然后就只能在心里默默估算后台执行结束的时间，苦苦等待，或者在代码中添加sleep，不断重试。要是有获取正在占用的卡槽数量的API就好了，就可以在发现卡槽被释放时，执行下一个任务，可惜没有。

发现前端的页面上有取消simulation的操作：


> [!NOTE] [图片 OCR 识别内容]
> 159
> Simulatio
> HSaI
> take a few minutes Or
> more
> Clia
> heretc
> cancel the simulation
> TIP
> Explore various Transformational Operators and Cross
> Sectional Operators.
> Drnotioc
> Smllato to 53V6


API是这个DELETE  [[链接已屏蔽])

想到能不能在程序退出时，取消掉正在跑的simulation，这样就可以直接重启程序。实践了一下，确实可行。具体方法就是，在代码中捕获Ctrl-C(kill -2 PID)引发的异常，删除simulation，再退出。

大概是这样：

```
try:    simulation_progress_url_list = multi_simulate()except KeyboardInterrupt as e:    for simulation_progress_url in simulation_progress_url_list:        delete_simulation(simulation_progress_url)
```

使用协程有点不一样，需要在主线程中捕获`KeyboardInterrupt`，在协程中捕获`asyncio.CancelledError`。

```
# main thread
try:
    main()
except KeyboardInterrupt as e:
    pass

# coroutine
async def coroutine():
    try:
        simulation_progress_url = await multi_simulate()
    except asyncio.CancelledError:
        delete_simulation(simulation_progress_url)
        raise
```

需要注意的是，delete_simulation需要使用同步代码调用API，不然还是会被主线程取消掉。

还有这个API是删除的操作，服务器可能出于安全的考虑，对调用频率有很大的限制，不过测试连续删10个还是没问题的。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很有用的方法，解决了我重启代码后一直在网页上点的问题。点赞！


---

### 技术对话片段 113 (原帖: 听完顾问第二次培训后，目前在使用的一个AI构造数据比率或相减新字段的模式。)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 听完顾问第二次培训后目前在使用的一个AI构造数据比率或相减新字段的模式_31070067563031.md
- **时间**: 1年前

**提问/主帖背景 (WY38139)**:
顾问第二课的时候老师演示了如何提问去让AI帮忙生成新的有经济学含义datafield比率或相减的datafield，主要是相同数据集中的datafield组合。这也启发了我，让我想到是否可以让AI也能生成跨dataset的datafield组合。

目前我主要分三步去实现跨dataset的组合，第一步是输入将datafieldid和description，以及dataset的描述作为promt输入，让AI对字段进行分类。结果样例如下：


> [!NOTE] [图片 OCR 识别内容]
> R categorl
> k
> BC categonz
> 5
> BC combination method
> 孓
> AC
> meaning
> p
> AC dat;
> 隐含波可萃
> 历史波动率
> 除
> 隐含波动率与历史波动萃的比萃窝垦末: optiont
> ETF苄联指标
> 诙动率比率指标
> 除
> 个股疲动率SETF波动率的比平反腴个 optiont
> 市场柜关性指标
> 市场网险指标 (Beta]
> 柜关性乘以Beta值o垦系统性风险对狩 optiont
> 诚U率比率指标
> 股息柞关指标
> 波动滓风险溢价与殷息收益的比汨评估[ optiont
> 利?指标 (短期]
> 利率指标 (长期]
> 艋
> 长短期利差反映市场对孥济屑期和通[
> 斯权市场活动指标
> 隐含疲动藜
> 期权交舄昼与隐含波动率的比率哥垦邡 optiont
> optiont


由于一开始目标是做单dataset组合，因此我这一步直接让AI协助组合并给出组合的方法与经济学含义。

第二步是逐批（目前是50条一批）将fieldid和description输入给AI，让AI使用上面的分类对每个field_id进行分类。（分开两步做主要是因为提示词长度受限）


> [!NOTE] [图片 OCR 识别内容]
> RCfeld i
> 萜
> H
> description
> 5
> H
>  categor
> 了
> AC dataset
> 了
> ACuniyerse
> 汩
> RCrE
> fnd14_1_vqe_hsc
> Total Cash and Cash Equivalents frc 总现金及等价钩
> fundamentall4
> TOP30O0
> USA
> fnd14_2_mtt_vqe_
> TTM Change in Cash and Cash Equi 现金流娈化(TTM]
> fundamentall4
> TOP3OO0
> USA
> fnd14_Zpc_krm_: Market capitalization at the end of
> 市场价_
> fundamentall4
> TOP3DO0
> USA
> fnd14_2rtq_vqe_
> Change in Cash and Cash Equivalen 单幸度现金谎弯化
> fundamentall4
> TOP3OO0
> USA
> fnd14 2 sto rhs
> Number of outstanding shares
> 流通殷数垦
> fundamentall4
> TOP3OO0
> USA
> fnd14_2_td_sto_r Date and time When number of out: 流通殷记录时闫
> fundamentall4
> TOP30O0
> USu


抽检过部分结果，感觉分类应该还算靠谱？不知道AI有没有胡诌。

两步结束后，其实已经可以根据这两个表进行单dataset内的字段组合了。

如需进行两个不同dataset的组合，则进行多一步，将第一步中两个不同dataset的分类输入到AI中让AI进行有经济学含义的组合，结果如下


> [!NOTE] [图片 OCR 识别内容]
> AC Jatasetl
> 了
> BC Jataset2
> }
> BC categorl
> 了
> BBC categor2
> p
> ACeconomic_meaning
> ]
> 月
> fundamental31
> option6
> 估值指标
> 隐含波动〉
> 估值与隐含跛动率的比萃可c量风险调
> fundamental31
> option6
> 徒务纭构
> 利率指标 (短期]
> 短期裱务占比与短郫率的差值可评估]
> fundamental31
> option6
> 酃利猷长
> 市场柞关性指标
> 盈利-长狈立于市场疲动的程度。反腴:
> fundamental31
> Option6
> 现金流充定性
> 股息柞关指标
> 亨白现佥流覆盏殷息乏付的能力差直
> fundamental31
> option6
> 资本结构
> 利率指标 (长期]
> 资本结构忧化程度柞对于长期熊资或O /
> fundamental31
> option6
> 收益稳定性
> 历吏诙动率
> 收益稳定性与史返动率杓比值反陂企


看上去说得很有道理的，不过不知道会不会存在幻觉。

最后一步就是根据表二对应字段的分类，将对应datafield进行组装，就得到一批新的datafield了。

目前测试下来，我将这些组合放进一二三阶模板中跑，也是能出货的，不过出货效率好像也没有显著提高，没达到老师说的alpha多到交不完的水平。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
提示一下，需要考虑不同字段的量纲，可以套个算术运算符标准化一下。


---

### 技术对话片段 114 (原帖: 在尝试Human Alpha的时候，如何找到想要的datafields？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 在尝试Human Alpha的时候如何找到想要的datafields_31978925276823.md
- **时间**: 1年前

**提问/主帖背景 (MZ32639)**:


**顾问 worldquant brain赛博游戏王 的解答与建议**:
data那边可以搜索得到相关的数据，但在当前genius计划下，每个人的op，运算符都有所差别，所以未必能够百分百找到，需要在每个地区查询，同时放宽数据集的要求。可以去寻找类似主题的数据，进行尝试。（在抽象成模版做machiinealpha的时候，也是要找类似数据的，所以此种操作类似于提前检验模版的鲁棒性）


---

### 技术对话片段 115 (原帖: print(pools[0]))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 多线程遍历回测super alpha代码优化_31527668843671.md
- **时间**: 1年前

**提问/主帖背景 (JL16510)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好用的方法，点赞。此外要提醒一下，select条件不能太严格，不然select不到10个就等于空跑


---

### 技术对话片段 116 (原帖: PnL = ∑(Robustness * Creativity))
- **原帖链接**: https://support.worldquantbrain.com[Commented] 如何利用tvr操作符与alpha起舞论坛精选_34562640928023.md
- **时间**: 10个月前

**提问/主帖背景 (QX52484)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享，很好的点子

按照相同的思路，lambda min是否可以写成-5？这样±都进行便利搜索，而非只局限于0到5，此外，target最大值是否可以考虑改为0.7，这是提交因子的理论上线（glb high turn主题不在此列）


---

### 技术对话片段 117 (原帖: 如何科学搜索alpha)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 如何科学搜索alpha_31246918695447.md
- **时间**: 1年前

**提问/主帖背景 (WC79277)**:
了解算法的同学都知道，广度优先搜索、深度优先搜索和A*搜索算法，而回测Alpha的过程，本质上也是一个搜索过程。

### 1. 广度优先搜索

广度优先搜索的核心思想是按层次逐步探索。在回测中，如果你先选择一个数据集，然后依次完成1阶、2阶、3阶的回测，具体流程是：先跑完1阶，选择一个表现较好的Alpha，再进行2阶回测，最后将表现最优秀的Alpha用于3阶优化。这种方法属于广度优先搜索。

**优点：**  广度优先搜索可以帮助你更全面地感知数据集是否符合你设定的模板，逐层优化，确保搜索的系统性和全面性。

**缺点：**  广度优先搜索需要等待前一层次完成后才能进入下一层，因此回测的时间较长。尤其是当数据集庞大时，计算成本较高，效率不够理想。

### 2. 深度优先搜索

深度优先搜索则是按深度逐步探索。在回测过程中，当你运行完1阶代码后，如果同时发现一个符合2阶条件的Alpha，就可以立即生成2阶Alpha并开始回测，3阶的优化同理。这样，你无需等待所有的1阶回测完成，即可开始进行后续阶段的回测。

**优点：**  深度优先搜索的主要优点在于它能够减少等待时间，实现更高效的资源利用和更快速的回测。

**缺点：**  深度优先搜索可能导致早期的某些优化深度不够，从而忽略了全局最优解。也就是说，虽然它能够更快进行局部优化，但缺乏全局视野，容易陷入局部最优而错过整体的最优解。

### 3. A* 智能搜索

A *搜索是一种启发式搜索算法，结合了广度优先搜索和深度优先搜索的优点。在回测过程中，A* 智能搜索会根据某个优先级指标，优先选择表现较好的Alpha进行优化。例如，当你得到一个表现优异的1阶Alpha时，在生成2阶Alpha时可以为其分配更多的权重。在检查过程中，A*会优先检查那些表现优秀的Alpha，而不是那些指标平平的Alpha。

**优点：**  A*智能搜索可以在深度优先搜索的基础上增加搜索方向，使得优化过程更加有针对性，从而更快地找到最佳的Alpha。

**缺点：**  A *搜索虽然能够加速优化过程，但它依赖于选择合理的启发式指标。如果选错了指标，可能导致搜索偏离最优解，甚至浪费时间在不合适的搜索方向上。此外，A* 搜索在计算复杂度上可能高于其他方法，尤其是在处理非常庞大的数据集时。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
很好的一种思路，这里我也提供我的一些做法。在一阶层面兼顾深度与广度，从ts运算符开始减枝，同时控制跑的字段数量（usage，coverage这种），如果装好槽数多的话，会跳着回测（偶数回测），这样能够稍微平衡下深和广。


---

### 技术对话片段 118 (原帖: 想请教一下sa中的 Selection Handling nan)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 想请教一下sa中的 Selection Handling nan_32986417280407.md
- **时间**: 1年前

**提问/主帖背景 (QX52484)**:
weight = (   1   *(prod_correlation)   *abs(self_correlation-0.5)   *(1-turnover));bool * weight 各位老师，我想请教一下像这样改变权重是如何影响到选取alpha的？ 是得到一个具体数值，而后在Selection Handling为nan的规则下，数值越高则从因子池中优先选取吗？

**顾问 worldquant brain赛博游戏王 的解答与建议**:
我记得这种情况下，想要选到数值高的，应该选positive才对，供参考。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。


---

### 技术对话片段 119 (原帖: 新人小小小心得)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人小小小心得_31747867191191.md
- **时间**: 1年前

**提问/主帖背景 (LZ84152)**:
作为新人一开始真的使用三阶段代码无脑交，没有太多思考，后来发现无脑提交的alpha质量高的不多，但又不太想为了交而交，索性开始逛起了论坛，就来说说论坛对于新人来说比较重要的一些小tip。
一、alpha 提交基础规则

对于vf0.5的新人，不知道如何评价alpha质量，可以查看这篇文章

[日赚90刀💵作为新人，我是怎么样从value factor 0.5升到0.99的？ – WorldQuant BRAIN]([L2] 日赚90刀作为新人我是怎么样从value factor 05升到099的经验分享_28856000657303.md)

有时候有些alpha的其他内容表现都很好，但就是turnover比较高，margin较低，可以查看

[如何提高流水率？– WorldQuant 大脑](/hc/en-us/articles/20251419309719-How-to-improve-Turnover)

***删除 [对于check，要记住check只有三个槽，同时每天四个alpha提交完后，check无法运行。所以要一直check就不能一次交满4个alpha，可以选择每天更新前提前半小时交最后一个。]***

二、效率提升经验总结

即插即用的多线程提交，把它放在multi_simulate_dynamic中修改一下就好，不会直接两个代码放gpt，要他改为多线程一般也就好了。

```
import concurrent.futureswith concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:    # 当队列未空 或 存在正在运行的任务时，持续循环    while not task_queue.empty() or futures:        # 当活动任务数小于10且队列中还有任务时持续提交        while not task_queue.empty() and len(futures) < 8:            try:                task = task_queue.get(timeout=2)            except Empty:                break            # 提交任务并加入列表            times = datetime.datetime.now()            args.log_id.Info(f"processing task: {now_id}")            future = executor.submit(simulate_and_check, task, args, s, now_id)            futures.append(future)            task_queue.task_done()            now_id += 1        # 等待任意一个任务完成        if futures:            done, not_done = concurrent.futures.wait(futures, return_when=concurrent.futures.FIRST_COMPLETED)            futures = list(not_done)
```

二、模板的选择

对于如何找alpha，可以看下面两个链接，一个英文和一个中文的alpha模板合集：

[【Alpha Template Collections】- Continuously Update – WorldQuant BRAIN]([L2] 【Alpha Template Collections】- Continuously UpdatePinnedAlpha Template_24472586368279.md)

[如何找到更多alpha的思考（新手进阶篇）系列 - 第三篇：论坛内的模版 – WorldQuant BRAIN]([L2] 如何找到更多alpha的思考新手进阶篇系列 - 第三篇论坛内的模版_27758310278295.md)

我自己先择差不多抛弃了三阶段方式，主要是现在更新点亮dines区域的数据集点亮规则变了，现在主要尝试论坛中的模板加套一个二阶段，二阶段可以是分组，也可以是trade_when。之后就是尝试更多的一些模板的可能性。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
论坛中的模版本身的op已经有点多了，再套一个阶段，有过拟合的感觉，这个需要注意啊


---

### 技术对话片段 120 (原帖: 新人构建模板的经验)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人构建模板的经验_33038189937687.md
- **时间**: 1年前

**提问/主帖背景 (FL39657)**:
我是三月份成为顾问的，目前也是到了要自己写模板的阶段，虽然遇到了不少困难，但是总归还是有些收获，因此想分享一些我做模板时的一些经验，因为模板效果并不是很好，仅仅只是能跑出来alpha，就不把模板分享出来了，如果以后出了好的模板，我会分享到论坛里。

首先，作为一个金融零基础的新人，想要构建自己的模板并不是什么容易的事情，重要的要能够理解自己想要做出什么养的alpha，在处理数据之前，一定要了解数据字段的含义，因此，先把数据集丢给AI分析，让AI给出数据字段的经济学意义，并且让AI给出关于这个数据集的量化策略，是我构建模板前的准备工作，在了解该数据集大概含义之后，我会参考AI的策略，如果合适的话，就将其复现，在手动回测看看效果，不合适的话，就会自己对其进行部分修改，修改过程中可以参考论坛的模板，我是把论坛里的模板都丢给了知识库，让知识库帮我总结并给出修改建议。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
能够自己做模版已经超越很多顾问了

Keep moving，Keep quanting！

===============================================================================


---

### 技术对话片段 121 (原帖: 新人经验分享以及近期的一些困惑)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人经验分享以及近期的一些困惑_31070381814295.md
- **时间**: 1年前

**提问/主帖背景 (JJ47083)**:
大家好，我是今年2.17拿到的顾问权限，不过我在3月才开始提交因子，属于进步比较慢的了，目前为止交了35个alpha，在这里谈谈我的经验。

我一开始主要用的一阶和二阶的模板跑asi区域，显然大多数跑出来的alpha相关性都特别高，不过用代码check的话，还是能找到一些alpha可以提交，不过fitness大多还是在1.4左右，想必大家也明白fitness还是尽量交1.5以上的才是一个合格的alpha，迫于一开始无法找出多的alpha，通过此办法混了几天，后来转战用论坛里的模板，得到了比较多的好的alpha，具体模板的使用方法大家可以去看这篇文章，相信大家还是可以找到alpha的

[如何找到更多alpha的思考（新手进阶篇）系列 - 第三篇：论坛内的模版 – WorldQuant BRAIN]([L2] 如何找到更多alpha的思考新手进阶篇系列 - 第三篇论坛内的模版_27758310278295.md)

不过目前阅读论坛里的大佬的帖子，发现大家其实更多的还是用的一二三阶的模板，不过对于一阶模板的改善，我依然存在许多的疑惑很困难，希望有大佬看到能给我指点迷津。

最后，还是非常感谢社区里所有小伙伴的帮助，让我这个基本没有金融基础的，也能交上几个alpha，虽然对于新手的我困难依然很多，不过我相信继续坚持和找到正确的方向努力仍然很重要

**顾问 worldquant brain赛博游戏王 的解答与建议**:
具体是什么方面的困难呢？可以详细说明一下


---

### 技术对话片段 122 (原帖: 新人经验分享以及近期的一些困惑)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新人经验分享以及近期的一些困惑_31070381814295.md
- **时间**: 1年前

**提问/主帖背景 (JJ47083)**:
大家好，我是今年2.17拿到的顾问权限，不过我在3月才开始提交因子，属于进步比较慢的了，目前为止交了35个alpha，在这里谈谈我的经验。

我一开始主要用的一阶和二阶的模板跑asi区域，显然大多数跑出来的alpha相关性都特别高，不过用代码check的话，还是能找到一些alpha可以提交，不过fitness大多还是在1.4左右，想必大家也明白fitness还是尽量交1.5以上的才是一个合格的alpha，迫于一开始无法找出多的alpha，通过此办法混了几天，后来转战用论坛里的模板，得到了比较多的好的alpha，具体模板的使用方法大家可以去看这篇文章，相信大家还是可以找到alpha的

[如何找到更多alpha的思考（新手进阶篇）系列 - 第三篇：论坛内的模版 – WorldQuant BRAIN]([L2] 如何找到更多alpha的思考新手进阶篇系列 - 第三篇论坛内的模版_27758310278295.md)

不过目前阅读论坛里的大佬的帖子，发现大家其实更多的还是用的一二三阶的模板，不过对于一阶模板的改善，我依然存在许多的疑惑很困难，希望有大佬看到能给我指点迷津。

最后，还是非常感谢社区里所有小伙伴的帮助，让我这个基本没有金融基础的，也能交上几个alpha，虽然对于新手的我困难依然很多，不过我相信继续坚持和找到正确的方向努力仍然很重要

**顾问 worldquant brain赛博游戏王 的解答与建议**:
JJ47083

所谓的123阶段只是一种流程，不是必须先1再2后3的，有人会裸跑字段（0阶），筛选好的放入一阶，也有人会213，更有121这种。所以我个人感觉是，选好的字段很重要，而0123阶只是针对字段进行处理，garbage in，garbage out。


---

### 技术对话片段 123 (原帖: 新手一个多月提交147个alpha的经验总结)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 新手一个多月提交147个alpha的经验总结_29878528858135.md
- **时间**: 1年前

**提问/主帖背景 (RP76828)**:
本人python熟练，无金融背景知识，去年12月底拿到顾问权限，12月31日正式提交第一个顾问alpha。由于之前错过了顾问培训课程，刚拿到顾问权限时挺迷茫，不知道怎么入手，只能从自己擅长的工程着手，试着构建一套系统，第一步先确保每天能提交足够的alpha。截至今天提交了147个，但还是没能做到每天能挖出足够可提交的alpha，现在等待参加今年的顾问培训课程，提升技能。我把这一月多一点的操作经验跟大家分享下，错误的地方欢迎前辈指正。

首先是系统搭建：

1、我把所有区的dataset都下载到本地，每个dataset一个文件，比如datasets/USA-1-TOP3000/analyst11

2、构建三个python进程，分别对应一阶，二阶，三阶，一阶提交的alpha全部以step1_开头，二阶以step2_开头，三阶以step3_开头。

一阶代码的实现是随机从任意dataset中取任意几个field，最多10个，最少2个，再随机从+，-，*，/中取operator，构建alpha，比如可以是两个field，一个operator，例子是field1 / field2，也可以是七个field，六个operator，例子是field1 - field2 + field3 +field4 +field5 +field6 +field7。

二阶代码的实现是定时轮询，取当前名字为step1_开头的，sharp大于1.2，fitness大于0.5的alpha，并存储到redis中，以防止下次轮询重复获取。

三阶代码的实现是定时轮询，取当前名字为step2_开头的，sharp大于1.4，fitness大于0.7的alpha，并存储到redis中，以防止下次轮询重复获取。

1月份前七天还比较顺利，这套系统每天能提交4个alpha，当时也还没有super alpha权限，算是满额提交。结果1月8日突然只能用部分field和operator，有些措手不及，因为忙，也没时间改造代码，差不多七八天没法提交一个alpha。

后来代码改造成适配部分field和operator，每天可提交的alpha有时候2个，有时候只有1个，甚至没有，这段时间我就找那些check submission只有一个FAIL的alpha，想手动把它改成可提交的alpha。

重点是处理IS_LADDER_SHARPE这个错误，我第一步是调时间，比如ts_mean(a, 240)，我会试着把240改成120，或者66，20， 10或者5。如果还不行，就参考community里搜到的一篇文章讲到的，把a改成a/(1.7-a)，或者改成a*(1+a)，我记得还改过一个，把a改成a*(1+a)*(2+a)*(3+a)后，变成能提交了，也试过把a改成log(rank(a*(1+a)))后，变成能提交的。还有一两次差一点点，我改了setting里的 **TRUNCATION** ，变成能提交的，也尝试换分组方式，变成能提交的。如果 [IS ladder Sharpe](/hc/en-us/articles/6726865162903?_gl=1*qjnlik*_gcl_au*NzI5ODQ4MzEuMTczODM3MDQyMQ..*_ga*MTczODM3MDQxODMxMWU5YTY1NjczZDEwZA..*_ga_9RN6WVT1K1*MTczOTE5OTE3MS43Mi4xLjE3MzkxOTkyNjMuNjAuMC4w)  等于或者小于零，我就直接放弃，因为之前调过几次，不管怎么调，也过不了。CONCENTRATED_WEIGHT错误，目前我只会调decay，增加decay，通过了几个，CONCENTRATED_WEIGHT超过50，我就放弃调，也是因为之前怎么调，也调不过。

还有一个意外发现是三阶脚本执行后，挑选出一些觉得接近提交的，把step3_改成step1_前缀的名字，重新送给二阶三阶脚本执行，反复嵌套，结果会产生不少可提交的alpha。比如最近提交的一个alpha的模版是group_neutralize(trade_when(ts_corr(close, volume, 20) < 0, -ts_target_tvr_hump(trade_when(group_rank(ts_std_dev(returns,60), sector) > 0.7, a, 22), abs(returns) > 0.1),lambda_min=0, lambda_max=1, target_tvr=0.1), abs(returns) > 0.1),densify(bucket(rank(close*volume),range = '0.1, 1, 0.1’)))，类似这种三阶之后又嵌套二阶的。

目前最大的问题是，虽然提交了147个alpha，30个pyramid，但是combined Alpha Performance是-0.78。我自己可能是犯了如下错误：

1、为了过 [IS ladder Sharpe](/hc/en-us/articles/6726865162903?_gl=1*qjnlik*_gcl_au*NzI5ODQ4MzEuMTczODM3MDQyMQ..*_ga*MTczODM3MDQxODMxMWU5YTY1NjczZDEwZA..*_ga_9RN6WVT1K1*MTczOTE5OTE3MS43Mi4xLjE3MzkxOTkyNjMuNjAuMC4w)  ，我有几个提交的alpha把时间从120改成类似113这种没有意义的数字

2、提交了大量相关性强的alpha，基本上一个alpha通过后，这个alpha再通过二阶，三阶脚本反复执行，能产生五六个可以提交的alpha，我基本都提交了。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
有个小问题需要注意一下， op用的太多了，在genius那边，单个alpha平均op可能不占优势


---

### 技术对话片段 124 (原帖: 根据系统提示构建新的数据字段Alpha Template)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 根据系统提示构建新的数据字段Alpha Template_30783222618007.md
- **时间**: 1年前

**提问/主帖背景 (YJ83444)**:
在Alpha灵感匮竭之时，收到系统发送的提示：

PE ratio can be a good measurement to generate Alphas. Calculate estimated PE ratio using EPS estimates of  [EPS Estimate Model Dataset]([链接已屏蔽])  and price fields of basedata ( [Price Volume Data for Equity]([链接已屏蔽]) )

系统提示可以使用EPS估值和价格字段构建新的PE比率数据字段。

第一步先看看什么是PE比率数据字段。

PE ratio，即 市盈率（Price-to-Earnings Ratio），是股票估值中最常用的指标之一。它反映了投资者愿意为每单位盈利支付的价格，是衡量股票相对价值的重要工具。

计算公式为：PE Ratio = 股票价格（Price）/ 每股收益（Earnings Per Share, EPS）
其中：

- 股票价格（Price）：当前股票的市场价格。
- 每股收益（EPS）：公司每股股票的盈利，通常使用过去12个月的盈利（Trailing EPS）或未来12个月的预测盈利（Forward EPS）。

PE比率可以用来：
1、衡量股票的估值水平：

- 市盈率越高，说明投资者愿意为每单位盈利支付更高的价格，可能意味着股票被高估。
- 市盈率越低，说明股票相对便宜，可能意味着股票被低估。

2、比较较同一行业中不同公司的估值水平。

3、判断市场情绪：

- 高市盈率可能反映市场对公司未来增长的高预期。
- 低市盈率可能反映市场对公司未来增长的悲观预期。

然后，从  **pv1**  数据集中获取价格字段，从  **model30**  数据集中获取EPS估值字段，构成 Price/EPS 组合字段。

为了消除极端值的影响，提高信号的可比性，将组合字段rank后，再放入一二三阶中生成Alpha。

目前跑了EUR TOP2500 D1，可以产生可提交的Alpha。

**思考：**

可以通过类似于PE比率的方式构建其他的数据字段组合，比如：

1、PEG Ratio（市盈率相对盈利增长比率）
PEG Ratio 是市盈率（PE Ratio）与盈利增长率（Earnings Growth Rate）的比值，用于衡量股票的估值是否合理，同时考虑公司的成长性。

公式为：PEG Ratio = PE Ratio / Earnings Growth Rate

其中：

- Earnings Growth Rate：盈利增长率，通常使用未来几年的预期盈利增长率。

意义为：

- PEG Ratio < 1：表示股票可能被低估，因为市盈率低于盈利增长率。
- PEG Ratio = 1：表示股票估值合理。
- PEG Ratio > 1：表示股票可能被高估，因为市盈率高于盈利增长率。

2、PB Ratio（市净率）
PB Ratio 是股票价格与每股净资产（Book Value per Share）的比值，用于衡量股票的市场价值与其账面价值的关系。

公式为：

PB Ratio = 股票价格 / 每股净资产
其中：

- 股票价格：当前股票的市场价格。
- 每股净资产：公司的净资产除以总股本，反映公司每股的账面价值。

意义为：

- PB Ratio < 1：表示股票的市场价格低于其账面价值，可能被低估。
- PB Ratio = 1：表示股票的市场价格等于其账面价值。
- PB Ratio > 1：表示股票的市场价格高于其账面价值，可能被高估。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢你的帖子，很有帮助的内容，点赞！


---

### 技术对话片段 125 (原帖: 求教，这个alpha还能救一下么)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 求教这个alpha还能救一下么_31017228094615.md
- **时间**: 1年前

**提问/主帖背景 (ZP42727)**:
最近跑了一个Spectacular的alpha,  但是 [Sub-universe Sharpe](/hc/en-us/articles/6568644868375?_gl=1*zfgsgt*_gcl_au*MTQzMDQzMDc2OC4xNzQwODkzODM5*_ga*MTczOTA3MDg1MjA5OThjZWVjNTU1NDc3ZGU.*_ga_9RN6WVT1K1*MTc0MzIzOTU3My4xMDMuMS4xNzQzMjQzNDYwLjYwLjAuMA..)   低好多， 尝试找了些方案，但是效果并不是太好。请诸位会诊一下，是否还有挽救的可能。


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> TRAIN
> TEST
> IS
> 09
> Spectacular
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 1.98
> 2.16%
> 3.97
> 50.21%
> 14.46%
> 465.71%o。



> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> PASS
> 1 FAIL
> Sub-universe
> Sharpe Of 0.35 is below cutoff of 0.74.
> 1 PENDING


参数设置如下：


> [!NOTE] [图片 OCR 识别内容]
> Simulation Settings
> Instrument Type
> Region
> Universe
> Language
> Decay
> Truncation
> Neutralization
> Pasteurization
> NaN Handling
> Unit Handling
> Max Trade
> Equity
> USA
> TOP3000
> Fast Expression
> 0.08
> Subindustry
> On
> On
> Verify
> OFF
> Delay


**顾问 worldquant brain赛博游戏王 的解答与建议**:
调整中心化， decay6没有实际经济学含义，换成0,1,3,5试试看，实在不行再套一层运算符


---

### 技术对话片段 126 (原帖: 浅探对robust test结果的观测方法经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 浅探对robust test结果的观测方法经验分享_31920180343703.md
- **时间**: 1年前

**提问/主帖背景 (DZ31817)**:
所谓robust test（稳健性测试），是指为因子设置不同的工作环境，并观测其在不同环境下的表现，如果表现没有出现大幅波动，说明这个因子是比较稳健的。这里设置的不同环境在某种意义上来说也算是一种OS，因此表现稳健的因子更有可能获得更稳定的OS表现。

我们在平台做robust test，主要通过遍历修改因子回测的各种参数，观测因子在不同设置组下的表现来实现。遍历的参数方面，有离散型的region、universe、neut和3个开关参数，以及decay、trun这两个连续型参数。

在遍历跑完后，如何对结果进行观测，这里分享一下我的一些方法，希望可以抛砖引玉。

1.首先观测因子主要指标总体的表现分布，这里通过画分布直方图、KDE图、箱型图并结合定量指标来观测。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 25
> 20
> 詈
> 詈
> Sharpe
> Fitness
> Margin
> Turnover
> 25
> 詈
> `
> 0.0000
> 0.0025
> 0.0050
> 0.0075
> 0.0100
> 0.0125
> 0.0150
> 0.0175
> 0.0200
> 0.00
> 0.25
> 0.50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Margin
> Turnover
  
> [!NOTE] [图片 OCR 识别内容]
> KDE
> Sharpe KDE
> Fitness KDE
> 1.0
> 1.25
> 1.00
> 0.6
> 鲁
> 鲁
> 0.75
> 0.50
> 0.25
> 0.00
> Value
> Value
> Margin KDE
> Turnover KDE
> BO0
> 500
> 400
> 鲁
> 300
> 
> 200
> 100
> 0.0000
> 0.0025
> 0.0050
> 0.0075
> 0.0100
> 0.0125
> 0.0150
> 0.0175
> 0.0200
> 0.00
> 0.25
> 0.50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Valle
> ValUe
  
> [!NOTE] [图片 OCR 识别内容]
> Boxplot
> Sharpe Boxplot
> Fitness Boxplot
> 詈
> 詈
> Margin Boxplot
> Turnover Boxplot
> 0200
> 2.00
> 0.0175
> 1.75
> 0.0150
> 1.50
> 0.0125
> 1.25
> 詈00100
> 詈
> 1.00
> 0075
> 0.75
> 0050
> 0.50
> 0025
> 0.25
> 0000
> 0.00


肉眼看表现不是很稳定，但也没有出现特别差的极端值。

2.接下来进行更细粒度的观测，画出因子指标在不同设置下的具体表现。这种观测除了进行robust test的目的外，还可以帮助你思考现在这个模板、数据集更适合什么设置。

不同universe下的表现：

看出这个因子在更大的universe下表现更好。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.4
> 1.0
> 1.2
> 1.0
> 0.8
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.002
> 0.100
> 0.075
> 0.001
> 0.050
> 0000
> 0.025
> Universe
> Universe
> MINVOLTM
> TOP1200
> TOP4O0
> TOP8O0
> _MINVOLTM
> TOP1200
> TOP4O0
> TOP8OO
> ILLIQUID_
> ILLIQUID
> TOP1200
> TOP1200
> TOP4O0
> TOP8O0
> _MINVOLTM
> TOP4OO
> TOPgOO
> MINVOLTM
> ILLIQUID_
> ILLIQUID_


说到不同universe该如何选择，之前也在研究小组中讨论过，这里把gpt的总结也顺带放这个帖子里。仅供参考，不一定完全适用。


> [!NOTE] [图片 OCR 识别内容]
> Universe 分类与推荐适配关系 (按 Datafield 类型分)
> Datafield 类型
> 推荐 universe 示例
> 说明
> Analyst
> TOP5OO
> TOPZOODU
> 尤其是
> TOPSP5OO
> 覆盖面广的 sell-side 研究。适用于大中
> TOPIOGO
> 盘股。数据密度高
> Earrngs
> TOP1OO0
> TOPSPS吣0
> EPS surprise。 guidance 变化等容易在
> 大票中反应明确
> Fundamental
> TOPIOGO
> 以下。如
> TOP16O0
> TOP3OOO
> 甚至
> 小票和低流动性股信息滞后。误定价多
> LLIQUID_MINVOLIN
> 基本面因子容易出 alpha
> Imbaance
> TOP4OO 以内。如
> TOP5O
> TOPIOO
> TOPSP5B0
> tklevel
> 数据需要高流动性。高频交易
> 特征在大盘蓝筹中更稳定
> Insiders
> TOPBOO
> TOP3OOO
> 小中盘股 insider 交易更有预测力。尤其
> 在信息不对称强的股票上
> Institutions
> TOP5OO
> TOPIGg0
> 机构重仓通常集中在中大盘。低流动性股
> 票机构参与少
> Macro
> 全市场通用。如
> T0P30O0
> TOPZOOgU
> 与个股无强关联性。可作为横截面
> beta。 风格回归项
> Model
> 跟随原始模型设计池子
> 模型因子取决于训练数据设计。不做统
> 分类
> News
> TOPIOGO
> 以内。如
> TOP2O0
> TOPSP5OO
> 上新闻的股票以热点大票为主。小票新闻
> 稀疏无效
> Option
> TOPSO
> TOP5OO
> 尤其 TOPSP5OO
> 有期权交易的股票以大盘蓝筹为主。其余
> 票期权数据缺失
> Other
> 具体字段具体判断
> 例如
> othg4
> Oth95
> 常见于舆情[事件
> 类。适用于中大票
> Price Volume
> TOP3OOO 全部。需做分层测试
> 价格。波动宰。成交量因子广谱适用。尤
> 其 momentum 在大票更稳定
> Risk
> T0P30O0  通用
> Volatility
> beta。
> size 等因子构建风格模
> 型基础组件
> Sentiment
> TOPIOO
> TOPIGg0
> 舆情活跃股通常足热点股票。小票讨论稀
> 疏。舆情滞后
> Short Interest
> TOP4OO
> TOPI6OO
> 做空机制活跃的股票更可能出现在中大
> 票。低流动性票难以借券
> Social Media
> TOPIOO
> TOPIGg0
> 社交媒体热度集中于热门票。小票信息噪
> 声大或缺失


继续观测robust test结果，不同中性化下的表现：

看出这个因子在country中性化下表现更好。这个示例因子我用的是EUR的因子，这个结论也与官方的推荐设置一致，逻辑闭环了。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 1.4
> 1.0
> 1.2
> 1.0
> 0.8
> p9
> G
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.100
> 0.075
> 0.001
> 0.050
> 0.000
> 0.025
> Neut
> Neut
> 惫
> FAST
> COUNTRY
> CROWDING
> MARKET
> SECTOR
> FAST
> INDUSTRY
> SLOW
> SUBINDUSTRY
> COUNTRY
> CROWDING
> MARKET
> SECTOR
> FAST
> INDUSTRY
> SLOW
> SUBINDUSTRY
> STATISTICAL
> STATISTICAL
> AND_
> OW_
> SLOW
> COUNTRY
> MARKET
> |
> FAST
> s
> SUBINDUSTRY
> COUNTRY
> SECTOR
> INDUSTRY
> FAST
> SLOW
> SUBINDUSTRY
> CROWDING
> STATISTICAL
> SECTOR
> WNDUSTRY
> CROWDING
> MARKET
> FAST
> STATISTICAL
> AND
> AND_
> SLOW
> SLOW


不同universe+中性化组合下的表现：

帮助找到当前最适合的搭配。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.4
> 1.0
> 1.2
> 0.8
> 1.0
> 0.8
> Neut
> Neut
> Margin by Group
> Turnover by Group
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 003
> 0.150
> 0.125
> UUU2
> 0.100
> 0.075
> 0.00
> 0.050
> DOO
> 0.025
> Neut
> Neut


不同decay下的表现：

这里decay离散取了几个值，看出对于这个因子，decay越高似乎表现更好。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.4
> 1.0
> 1.2
> 0.8
> 1.0
> 0.4
> 120
> 240
> 120
> 240
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 0.005
> 0.225
> 0.200
> 0.004
> 0.175
> 0.003
> 0.150
> 0.125
> 0.002
> 0.100
> 0.075
> 0.001
> 0.050
> DOO
> 0.025
> 120
> 240
> 22
> 120
> 240
> Decay
> Decay
> DTOUH


由于decay是连续型参数，我干脆固定了其它参数后把decay从0-240都取值跑了一下，结果如下：

看出对于这个因子，decay对性能增强的峰值在70附近。同时，也可以观测到turnover随decay的增大而被削弱，与理论吻合。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> VS Decay
> 1.60
> 1.55
> 1.50
> 詈
> 1.45
> 1.40
> Fitness Vs Decay
> 1.30
> 1.25
> 1.20
> 岛
> 1.15
> 1.10
> 1.05
> Margin Vs Decay
> 0.0050
> 0.0045
> 0.0040
> 
> 0.0035
> 0.0030
> 0.0025
> 0020
> Turnover Vs Decay
> 0.06
> 
> 0.05
> 0.04
> 100
> 150
> 200
> 250
> Decay


既然说到了turnover，虽然它不是一个参数，但大家都对它比较敏感，对高turnover的因子避之不及，因此我也顺便观测了一下turnover对性能的影响：

看出turnover在15以上后性能确实迅速退化。此外，这里margin随turnover的变化图像也验证了return ~ turnover*margin的理论，理论与实践再次闭环。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe Vs Turnover
> 1.25
> 1.00
> 詈
> 0.75
> NIRI
> 0.50
> 0.25
> Fitness Vs Turnover
> 1.0
> 0.8
> 0.6
> 
> 0.4
> 0.2
> "WWlkwt
> 0.0
> Margin Vs Turnover
> 0.005
> 0.004
> 0.003
> 
> 0.002
> 0.001
> 0.000
> TurnoVer VS Turnover
> 0.20
> 0.15
> 
> 0.10
> 0.05
> 0.025
> 0.050
> 0.075
> 0.100
> 0.125
> 0.150
> 0.175
> 0.200
> 0.22
> WM
> IMMAN


以上观测方法仅仅是抛砖引玉，对于robust test的结果还是要人工判断，没有一个能一概而论的判断标准，希望大家能够分享交流是否有更好的观测方法。另外，从这次观测之旅我们也体会到，这种详细的数据分析和深入研究的收获，往往能大大超出你原本的目的。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
WQ科学家！！！很好的帖子，点赞。如果对于不同地区的因子都做一次测试，就可以找出最适合每个地区的中性化方式了。


---

### 技术对话片段 127 (原帖: 过滤掉 Python 内置函数和关键字)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 用python ast提取表达式中operator和datafield的方法代码优化_30870358077463.md
- **时间**: 1年前

**提问/主帖背景 (WL27618)**:
python ast可以自动解析符合python规范的代码表达式. 因此把我们的alpha转换成python可以理解的方式就能解析了, 这样避免了每次字符串的解析(写正则表达式之类). 可以用来在跑模版的时候检测datafield是否符合规范, 也可以用来统计自己使用的各种datafield, operators频率.

代码如下:

import ast

import re

def parse_alpha(alpha_expression):

"""

Parses an alpha expression and extracts operators and data fields.

This function processes a given alpha expression by converting ternary expressions,

fixing indentation errors, and parsing it into an abstract syntax tree (AST). It then

traverses the AST to extract operators and data fields, while filtering out defined

variables, NaN values, and Python built-in functions and keywords.

Args:

alpha_expression (str): The alpha expression to be parsed.

Returns:

dict: A dictionary containing two lists:

- 'operators': A list of unique operators (function and method names) found in the expression.

- 'data_fields': A list of unique data fields (variable names) found in the expression, excluding defined variables and NaN values.

"""

# 处理三元表达式

alpha_expression = alpha_expression.replace('?',' if ').replace(':',' else ')

# 处理和python内置逻辑表达式冲突

alpha_expression = re.sub(r'\band\b', 'and_', alpha_expression) # 替换独立的 'and'

alpha_expression = re.sub(r'\band\(', 'and_(', alpha_expression) # 替换 'and('

alpha_expression = re.sub(r'\bor\b', 'or_', alpha_expression) # 替换独立的 'or'

alpha_expression = re.sub(r'\bor\(', 'or_(', alpha_expression) # 替换 'or('

# 处理逻辑表达式

alpha_expression = alpha_expression.replace('!',' not ').replace('&&',' and ')

# 处理range="0.1,1,0.1" 类似表达式

alpha_expression = re.sub(r'"([^"]*)"', "0", alpha_expression)

# 处理缩进错误，尝试修复

alpha_expression = "\n".join(line.strip() for line in alpha_expression.splitlines())

# 解析表达式为抽象语法树 (AST)

tree = ast.parse(alpha_expression)

# 提取 operators 和 data fields

operators = set()

data_fields = set()

# 提取过程中定义的变量

defined_variables = set()

# 遍历 AST

for node in ast.walk(tree):

# 提取赋值语句中的变量名

ifisinstance(node, ast.Assign):

for target in node.targets:

ifisinstance(target, ast.Name):

defined_variables.add(target.id) # 记录定义的变量名

# 提取函数调用 (operators)

ifisinstance(node, ast.Call):

ifisinstance(node.func, ast.Name):

operators.add(node.func.id) # 函数名

elifisinstance(node.func, ast.Attribute):

operators.add(node.func.attr) # 方法名

# 提取变量名 (data fields)

ifisinstance(node, ast.Name):

data_fields.add(node.id) # 变量名

# 提取三元条件表达式

ifisinstance(node, ast.IfExp):

# 提取条件部分

ifisinstance(node.test, ast.Compare):

for comparator in node.test.comparators:

ifisinstance(comparator, ast.Name):

data_fields.add(comparator.id)

# 提取 if 部分

ifisinstance(node.body, ast.Name):

data_fields.add(node.body.id)

# 提取 else 部分

ifisinstance(node.orelse, ast.Name):

data_fields.add(node.orelse.id)

# 过滤掉过程中定义的变量

data_fields = data_fields - defined_variables

# 过滤掉特殊变量nan

data_fields = data_fields - set(['nan','true','false'])

# 过滤掉 Python 内置函数和关键字

builtin_functions = set(dir(__builtins__)) # Python 内置函数

operators = operators - builtin_functions # 去掉内置函数

data_fields = data_fields - builtin_functions - operators # 去掉内置函数

return {'operators':list(operators),"data_fields":list(data_fields)}

目前这个版本我自己用着是没发现什么解析错误的问题. 欢迎大家指正.

**顾问 worldquant brain赛博游戏王 的解答与建议**:
提供一个新的思路，如果是走一二三阶段的路子，可以试着用backfill来抓取（当然，向量类型每种向量运算符都算一个），详细的可以参考： [如何统计得到的字段数？如何抓取多地区因子一起检验？ – WorldQuant BRAIN](如何统计得到的字段数如何抓取多地区因子一起检验代码优化_28754183939351.md)


---

### 技术对话片段 128 (原帖: 第一赛季Value Factor Improvement 心得与分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 第一赛季Value Factor Improvement 心得与分享_32578030064407.md
- **时间**: 1年前

**提问/主帖背景 (ML42552)**:
也想像大佬们一样贴出自己的value factor 成长史，但现在依旧牢底坐穿，比赛的成果也需要在下一次value factor 更新后才能看到。

那就跟大家分享以下踩过的坑和参加比赛获得的一些结果吧。

首先踩过最大的一个坑：

base payment的计算公式，相信大家都不陌生，rank（每日提交alpha数量，质量，value factor，自我成长）。第一次新人培训完后我灵机一动，欸，那是不是我刚开始交差一些，后面就很容易拿到自我成长的分数。结果就是我现在牢底坐穿......

value factor: 0.32 --> 0.31 --> 0.44

combined: (前面还更新了一次，更糟糕就忘记了) --> -0.33 --> 0.02

combined selected: 0.49 --> 0.75 -->1.33


> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-01,January 1st, 2025
> March 31st, 2025
> Category
> USA
> GlB
> EUR
> ASI
> CHN
> Analyst
> Earnings
> GLBIDIIMoJe
> Fundamen-s
> SUbIissions:
> Insiders
> ACtIVE
> Clic-kto View Jatesets
> Wacro
> Wodel
> NEws
> Opzion
> Other
> Drice Volume
> Risk
> Seniment
> Social Media


从图片不难看出我2025年Q1交了差不多一半的低质量ASI的model，在手续费本就高的亚洲市场，再提交了一大堆不稳定的model因子，最后不好的结果也是可想而知的。

这是20250401 VF Improvement 比赛前的截图：


> [!NOTE] [图片 OCR 识别内容]
> Distribution of Active Alphas
> Click to drill down
> EUR
> GLB
> TN


可见当时交的因子非常的单一，多样性不足。

USA


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> USA
> Delay
> Analyst
> Model 
> Prce Volume
> Fundamental
> Earnings
> Institutions


TWN


> [!NOTE] [图片 OCR 识别内容]
> AIphas
> TN
> Delay
> Model
> 12 alphas
> (100% OfTWN Delay 1 )
> Under the limit of 30%.
> Model
> Price Volume
> Fundamental


202412,交了大量的USA以及12个TWN，没错，就是这12个小地区alpha，并且质量不怎么样，导致2月份更新value factor ，喜提0.32

ASI


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> ASI
> Delay
> Model
> Prleg Volume
> Fundamental


GLB


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> CLB
> Delay
> Price Volume
> 11 alphas
> (85% OfCLB Delay 1)
> Under the limit Of 30%.
> Price Volume
> Model 
> Fundamental


202501交了大量的低质量ASI,GLB是参加新年的HCAC大赛提交的，最后os质量倒也中规中矩。

这个告诉我们紧跟着比赛的节奏是不错的选择。

再到后来202502只交了几个alpha，因为相关性算法的调整，也因为自我的禁锢，导致整个2月几乎没有提交alpha，最后就得到了0.31的惊人”成果“

EUR


> [!NOTE] [图片 OCR 识别内容]
> AIphas
> EUR
> Delay
> Price Volume
> Model
> Fundamental
> Analyst


后来三月份EUR地区新增了Top2500，并且有意识地优先做ananlyst和fundamental这两个数据集，value factor 和 combined 都有了一定地优化

非常感谢这次的Value Factor Improvement 比赛和 PPAC比赛，让我至少目前走回了正轨


> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-02, April 1st, 2025
> June 3oth, 2025
> Category
> USA
> GLB
> EUR
> ASI
> CHN
> Analyst
> Earnings
> Fundamenza
> Insigers
> Macro
> Model
> NEWs
> Option
> Other
> Drics Volume
> Risk
> Sen-iment
> Socia
> MeJia


目前金字塔点了46个，虽然质量也不咋滴，但是多样性得到了保证，再赌一手更多相对好的super alpha被选上，combined selected拿个2+，大主人不是梦哈哈哈哈。

对的，super alpha也是算进我们的combined中，所以如果解锁了super alpha，每天做一个其实是能优化我们的组合的。尽管在我们value factor 不高的情况下 super alpha 几乎拿不到什么base payment

6月份的super alpha 比赛应该也是告诉我们这个道理。跟着比赛的节奏走，准没错

最后再看看现在的已提交alpha分布图：


> [!NOTE] [图片 OCR 识别内容]
> Click to drill down
> ASI
> EUR
> USA
> GUB
> TN


USA


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> USA
> Delay
> Price Volume
> 72 alphas
> (53% Of USA Delay I)
> Over the limit Of 309.
> Model
> Price Volume
> Earnlngs
> Macro
> Fundamental
> Sentiment
> Option
> Othep
> Analyst
> Soclall Medla
> Insti.
> News
> Inslders
> Risk


ASI


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> 451
> Model
> Prlce Volume
> RIsk
> Analyst
> Fundamentall
> Sentiment
> Other
> Delay


EUR


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> EUR
> Delay
> Fundamentall
> Fundamental
> 12 alphas
> Price Volume
> (235 Of EUR Delay 1)
> Under the Iimit of 30%.
> Insiders
> Analyst
> Macro
> RIsk
> News
> Model
> Sentiment
> Other


GLB


> [!NOTE] [图片 OCR 识别内容]
> Alphas
> CLB
> Delay
> Model
> 15 alphas
> (48% Of GLB Delay 1)
> Under the limit of 30%.
> Rrice Volume
> Fundamentall
> Analyst
> Model
> Macro
> RIsk


以前交的大红虽然还在，但肉眼可见的在慢慢优化

总结：

1.多样化，不管是region还是datafields，亦或者是operators

2.跟着比赛的节奏走

3.ananlyst和fundamental的表现相对稳定一些

4.super alpha 尽量每天都交

结语:

希望最后value factor 能有一些提升吧，不然本篇就要成为打脸日记黑历史了......

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢大佬分享，很有用的经验！！！================================================================================================================================


---

### 技术对话片段 129 (原帖: 组super alpha时所有可用的属性经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 组super alpha时所有可用的属性经验分享_34178199290135.md
- **时间**: 10个月前

**提问/主帖背景 (QQ68782)**:
在学习小组里有人在组SA时用了 own_country 表达式, 但是这个表达式在文档里并没有出现: 
 [[链接已屏蔽])

还有哪些表达式文档没有出现呢? 所有可用的表达式有哪些呢?

在网页里发现, 这个地址可以请求到所有可用的字段: 
 [[链接已屏蔽])

```
{
  "selection": [
    "turnover",
    "long_count",
    "short_count",
    "decay",
    "universe",
    "operator_count",
    "datafield_count",
    "dataset_count",
    "datacategory_count",
    "self_correlation",
    "prod_correlation",
    "neutralization",
    "truncation",
    "datacategories",
    "datasets",
    "datafields",
    "classifications",
    "competitions",
    "themes",
    "name",
    "color",
    "category",
    "favorite",
    "own",
    "own_university",
    "own_country",
    "tags",
    "os_start_date",
    "author_tenure",
    "author_activity",
    "author_distinct_count_regions",
    "author_self_correlation",
    "author_prod_correlation",
    "author_sharpe",
    "author_turnover",
    "author_fitness",
    "author_returns_to_drawdown",
    "author_distinct_count_datafield",
    "author_distinct_count_datasetcategory",
    "author_distinct_quarter_count_datafield",
    "author_distinct_quarter_count_dataset",
    "author_distinct_quarter_count_datasetcategory",
    "author_distinct_count_operator",
    "author_distinct_quarter_count_operator",
    "author_distinct_count_dataset",
    "author_yield_rate",
    "author_quarter_yield_rate"
  ],
  "combo": [
    "alpha",
    "long_value",
    "short_value",
    "pnl",
    "returns",
    "drawdown",
    "long_count",
    "short_count",
    "hold_value",
    "trade_value",
    "hold_shares",
    "trade_shares",
    "hold_pnl",
    "trade_pnl",
    "turnover"
  ]
}
```

其中 themes、own_university、own_country 等在文档里没有出现;

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享，作为sa小白学到了很多，点赞


---

### 技术对话片段 130 (原帖: **Alpha主机专业**)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 组装Alpha主机炸毁同事第一代_30219424049943.md
- **时间**: 1年前

**提问/主帖背景 (JB71859)**:
# **Alpha主机专业**

## **配置：**

CPU:

E5400，主频2.7，二级缓存（2MB）

主板:

G41集成显卡

内存:

DDR2 2G*2 == 4G内存

散热：

英特尔原装

总价格: 40米

硬盘：

机械320G == 18米

显卡：

HD5450 512兆缓存 == 18米

电源随机200w  ==  13米

## 搭配下来总金额 ： **89**

当看到这个配置和价格时有没有要搞的，具体能不能点亮我不确定，但肯定不会炸。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
你这个预算放图吧老哥手上能配两台（笑）


---

### 技术对话片段 131 (原帖: 经验分享｜PPAC全球第三名，回馈社区经验分享)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **时间**: 1年前

**提问/主帖背景 (MH33574)**:
引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.3
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 2.94
> Reached Grandmaster
> 0.5


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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
出神入化的经验分享，很有用。点赞！


---

### 技术对话片段 132 (原帖: 给新手跑region和dataset的小建议)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 给新手跑region和dataset的小建议_28467103126679.md
- **时间**: 1年前

**提问/主帖背景 (XX42289)**:
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

**顾问 worldquant brain赛博游戏王 的解答与建议**:
amr确实很难跑，但架不住给的多。analyst感觉需要慎重，因为会做出一堆能提交的，但卡相关性后就一两个。


---

### 技术对话片段 133 (原帖: 解决网页出现"WorldQuant BRAIN is experiencing some difficulties"导致的回测中断代码优化)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 解决网页出现WorldQuant BRAIN is experiencing some difficulties导致的回测中断代码优化_33170238135959.md
- **时间**: 1年前

**提问/主帖背景 (HQ17963)**:
**背景说明：**

在使用 WorldQuant BRAIN 进行网页端回测时，前端会定期通过 GET 请求（ `[链接已屏蔽] ）获取当前回测的进度信息。然而，在网络不稳定或服务端异常（如返回 526 错误等）的情况下，该请求可能会失败，导致页面显示 "WorldQuant BRAIN is experiencing some difficulties" 的错误提示，并中断回测。

需要注意的是，虽然此时页面无法更新进度信息，但实际的回测任务仍在后台正常运行。这种中断仅是前端展示层面的问题，影响了顾问体验和研究效率。

**脚本功能：**

为  `[链接已屏蔽] 下的所有 GET 请求添加自动重试机制，在网络波动或临时性服务异常发生时，尝试重新发起请求，从而避免因短暂故障而导致的回测中断问题。

**使用方法：**

1.  **安装篡改猴插件** (直达链接： [篡改猴 - Microsoft Edge Addons]([链接已屏蔽]) )

- 打开 Microsoft Edge 浏览器；
- 点击右上角  **三个点图标** ；
- 选择  **扩展** ；
- 在 Microsoft Edge Addons 商店中搜索  **Tampermonkey（篡改猴）** ；
- 点击  **获取**  并安装插件。

2.  **安装脚本**

- 点击浏览器右上角三个点图标-扩展-篡改猴-添加新脚本
- 将脚本代码粘贴至编辑器中；
- 按下  **Ctrl + S**  保存脚本；
- 脚本即已安装并生效。

注1：该脚本仅修改网页前端以实现GET请求出错时重试，不会修改WQ服务端的任何数据，不会对WQ服务器造成任何影响。

注2：该脚本已在数周使用中验证了功能。但在未来，脚本可能会由于WQ前端代码更新而失效。若如此，请联系作者更新代码。

注3：有时，回测仍会报 "WorldQuant BRAIN is experiencing some difficulties" 错误。通过访问上述进度信息URL可知，这是WQ后端异常导致的真 · 回测失败。

**顾问 worldquant brain赛博游戏王 的解答与建议**:
感谢分享，很有用的代码与方法

平常 网页卡卡的时候，回测总会丢，很恼火，按照 文章的方法一下子就迎刃而解了，点赞!

============================================================================


---

### 技术对话片段 134 (原帖: 调查下，你的simulate程序能一直运行多久？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 调查下你的simulate程序能一直运行多久_32986452726807.md
- **时间**: 1年前

**提问/主帖背景 (EL94401)**:
simulate程序的效率，很重要。这需要一方面，将槽位用满，再则就需要健壮，长期稳定运行。请问你的程序能一直运行多久？方法是什么？

**顾问 worldquant brain赛博游戏王 的解答与建议**:
如果时常清理输出的话，可以达到八千分钟，最长一次跑了一万两千分钟（很多时候崩溃是输出太多的原因，不是程序和kernel本身的问题，我现在每天都清理一次输出）， 供参考》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》》


---

### 技术对话片段 135 (原帖: 除了turnover还有其他分层方式吗？)
- **原帖链接**: https://support.worldquantbrain.com[Commented] 除了turnover还有其他分层方式吗_33119740000407.md
- **时间**: 1年前

**提问/主帖背景 (QZ67721)**:
如题，非常感谢游戏王大佬在顾问论坛写的SA分成选取因子的思路，
比如选择特定区间内的因子，以降低相关性
((turnover<0.08&&turnover>0.07)||
(turnover<0.05&&turnover>0.04)||
(turnover<0.03&&turnover>0.02))

那么既然turnover可以进行分层，是否有其他适合分层的指标？原本想用Sharpe之类的指标，但是这部分是没有数据的。
++++++++++++++++++++++++++++++++++++++++++++++++
所以有大佬试过其他可用的分成指标吗？

**顾问 worldquant brain赛博游戏王 的解答与建议**:
count也可以，但是不同universe会存在偏颇，不能搞清楚哪些好因子一定在哪个区间里面，所以需要不断尝试！！！！！！！！！！！！！！！！！！！！！！！！！！1


---
