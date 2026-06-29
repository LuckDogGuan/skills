# 对Python一窍不通的萌新小白-终于搞懂了世坤平台挖掘因子的过程啦！

- **链接**: [Commented] 对Python一窍不通的萌新小白-终于搞懂了世坤平台挖掘因子的过程啦.md
- **作者**: 顾问 NL80893 (Rank 16)
- **发布时间/热度**: 1年前, 得票: 181

## 帖子正文

兴奋兴奋！

我从2.17号正式开启因子挖掘，到今天已经提交了48个因子啦！

从一窍不通到干中学再到明白世坤挖掘因子的过程就是一场大型的消消乐游戏，统共用时17天！

我之前没有编程基础，新人课也没听明白啥意思，好在有鑫鑫老师提供了教学和如何操作的过程可以让我迅速上手。

在提交了28个因子之后，发现已经check不出来可以提交的因子了，提示全都是相关性过高，在unsubmite界面筛选Sharpe>1.25,fitness>1后还有700多个未提交的，我手动提交了4天*8h，给我累惨了，时间完全耗在提交上，消消乐游戏从此正式开始！

当开始思考如何调优策略和自动提交的时候，你对挖掘过程的着迷程度和你的求知探索欲才是玩游戏的根本！

借着这个问题，询问老师后得到两个解决方案：

1、Prume剪枝。要是没剪枝两个字我完全不懂啥意思，我理解就是不要交叉太多，一字段不要跑太多二字段；

2、多换数据集；

第一个方案比较好解决，停掉digging2就可以了，停掉step2之后就生成了一个可以提交的因子，在我以为终于好起来的时候，跑了一晚上，第二天啥啥都没有。所以必须经历换数据集的阶段了。

好在鑫鑫老师有代码讲解，边看视频边暂停去平台上找怎么修改fields名称，最后成功获取了fundamental6数据集，也成功提交了三个因子，弄明白了标红是啥意思。但还是不行啊！我的目标是100个，解锁super alpha！这一半儿还没到呢。

换了好几个数据集后，看到鑫鑫老师在群里发了他自己测试用豆包生成fields的提示词，但一堆代码，啥都不懂。就算豆包给我解释了，还是不明白。


> [!NOTE] [图片 OCR 识别内容]
> 介  首页
> 十 Al 搜索或打开网页
> 豆包
> 数据分析与处理
> 按
> (fn) F
> 即可退出全屏模式
> 十  新对话
> 请依据我提供的操作符列表和数据集。生成一些类似于
> C
> Al 搜索
> "liabilities / assets" 这种有经济学解释的因子
> 不限于除法操
> 作
> 也可以是其他操作符组合而成的表达式,结果要以Python
> T  帮我写作
> 的List[str]形式呈现
> 操作符如下: [{'name': 'add'; 'definition': 'add(x, Y filter =
> 夭  图像生成
> false), X + y'} {'name': 'log', 'definition': 'log(x)'} {'name':
> 叫
> Al 阅读
> 'subtract'; 'definition': 'subtract(x, Y, filterzfalse), X
> y}
> {'name': 'signed_power' 'definition': 'signed_power(x, y)'}
> 〈
> Al 编程
> {'name': 'sign; 'definition': 'signfx)'} {'name': 'reverse'
> 'definition': 'reverse(x)'} {'name': 'power'; 'definition'=
> 语音通话
> 'power(x, y)'} {'name': 'multiply; 'definition': 'multiply(X,y
> Al 看网站
> filterzfalse) X
> y} {'name'
> 'min'; 'definition': 'min(x, Y .)'}
> {'name': 'max; 'definition': 'max(x, Y .)} {'name': 'inverse'
> 'definition': 'inverse(x)'} {'name'
> 'densify; 'definition':
> 最近对话
> 'densify(x)'}, {'name': 'abs'; 'definition': 'abs(x)'}, {'name'=
> 数据分析与处理
> 'divide'; 'definition': 'divide(x, y), X /y'}, {'name': 'equal;
> 'definition'
> 'inputl == input2'} {'name'
> less' 'definition':
> 解释每股账面价值
> 'inputl
> input2' }, {'name': 'and'; 'definition': 'and(inputl,
> 手机版对话0
> input2)' }, {'name': 'or; 'definition': 'or(inputl, input2)'},
> {'name': 'not_equal'; 'definition': 'inputl!= input2'}, {'name'
> 数据指标分析
> 'not'; 'definition': 'notfx)'} {'name':
> greater'; 'definition':
> 介绍南大通用产品
> inputl > input2'}, {'name': 'greater_equal'; 'definition'=
> 查看全部。
> 'inp'
> input2'}, {'name': 'less_equal'; 'definition': 'inputl
> <二
> "} {'name': 'is_nan; 'definition': 'is_nan(input)'},
> Al 云盘
> {'name': 'if_else', 'definition': 'if_else(inputl, input2, input
> < Al 编程
> 图像生成
> C AI 搜索
> T 帮我写作
> l Al 阅读
> 学术搜索
> 1  解题答疑
> 骷  更多
> 我的智能体
> 收藏夹
> 发消息
> '输入@选择技能或|选择文件
> Beta
> & 深度思考
> @屙 & @ @


不劳而获隐隐约约有种挫败感，觉得是不是自己也可以用提示词生成，今天下定决心要搞明白。

回到老师讲解的视频里发现了数据类型，有如下两种：


> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com
> Analyst Estimate Data for Eq..
> Analyst Estimate Data for Eq..
> Price Volume Data for Equity
> New post
> WorldQuant BRAIN
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> 8
> Competitions (1)
> 88 Team
> 三
> Region
> Delay
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
> Alphas
> Users
> Name; description
> to
> 100
> All
> to
> to
> Clear
> All
> Field
> Type
> Coverage
> Users
> Alphas
> Matrix
> anl4_adjusted_netincome_ft
> Adjusted
> (revisionlnewl.. )
> Matrix
> 8796
> 3024
> 6244
> Vector
> anl4_ads1 detailafv1 10_bk
> Broker na
> Vector
> 6996
> 17
> 42
> Group
> anl4_ads1detailafv1 10_estvalue
> Estimatior
> Vector
> 6996
> 26
> 53
> Universe
> anl4_ads1detailafv1 10_person
> Broker Id
> Vector
> 699
> 5
> anl4_ads1detailafv1 10_prevval
> The Previous Estimation of Financial Item
> Vector
> 6996
> 20
> 40
> anl4_ads1detailqfv1 10_bk
> Broker name (int)
> Vector
> 639
> 11
> 19
> anl4_ads1detailqfv1 10_estvalue
> Estimation Value
> Vector
> 6396
> 10
> 70
> anl4_ads1 detailqfv1 10_person
> Broker Id
> Vector
> 639
> 2
> anl4_ads1detailqfv1 10_prewal
> The previous estimation of financial item
> Vector
> 6396
> 13
> 19
> anl4_adxqfv1 10_down
> Number of Iower estimations
> Vector
> 7096
> 18
> 25


但数据类型Matrix和Vector是啥意思呢？那就找长的一样的就行：


> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com
> WorldQuant BRAIN
> Analyst Estimate Data for Equity
> WorldQuant
> Price Volume Data for Equity
> WorldQuant BR。
> New post
> WorldQuant BRAIN
> Courses
> Documentation
> Documentation
> 痴
> Operators
> Discover BRAIN
> Create Alphas
> Interpret Results
> 7 Articles
> 7 Articles
> 2 Articles
> FAQ
> *Read this First *
> Starter Pack
> Simulate your first Alpha
> Clear these tests before submittingan
> Events
> Alpha
> Introduction to Alphas
> Test Period
> Parameters in the Simulation results
> Introduction to BRAIN Expression
> How to choose the Simulation Settings
> Glossary
> Language
> How BRAIN platform Works
> Intermediate Pack
> Understand Results
> [1/2]
> Alpha Examples for Beginners
> Intermediate Pack
> Improve your Alpha
> Alpha Examples for Bronze Users
> [2/2]
> Alpha Examples for Silver Users
> 10 Steps to Start on BRAIN platform
> WorldQuant Challenge
> Understanding Data
> Advanced Topics
> 4 Articles
> 2 Articles
> Understanding Data in BRAIN:
> Concepts
> Must-read posts: How to improve your
> and
> Alphas
> How to use the Data Explorer
> Neutralization
> Vector Data Fields
> Group Data Fields
> Key
> Tips



> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com
> Vector Data Fields
> WorldQuant BRAIN
> Analyst Estimate Data for Equity
> WorldQuant
> Price Volume Data for Equity
> WorldQuant BR。
> New post
> WorldQuant BRAIN
> Apply vector
> Submit alpha
> Facebook
> Courses
> operators
> on BRAIN
> Documentation
> Apple
> Needs to be converted
> Can apply regular
> Are used to calculate
> 勿
> Operators
> to matrix field
> matrix operators to
> Pnland other
> Vector operators
> generate final output
> evaluation metrics
> FAQ
> 以下是将向量数据字段转换为矩阵的不同运算符。每个运算符在聚合特定日期和金融工具的向量以形成单个
> Events
> 值时略有不同:
> Glossary
> Operator
> Description
> VeC_aVg(x)
> Taking mean ofthe vector field X
> Vec_choose(xnth=k)
> Choosing kth item(indexed at 0) from each vector field X
> Vec_countfx)
> Number of elements in Vector field X
> Vec_irfx)
> Information Ratio (Mean
> Standard Deviation) of vector field X
> VeC
> kurtosis(x)
> Kurtosis of vector field X
> Vec_max(x)
> Maximum Value form Vector field X
> Vec_minfx)
> Minimum value form Vector field X
> Vec_normfx)
> Sum ofall absolute Values ofvector field X
> Vec_percentage(x;percentage=0.5)
> Percentile ofvector field X
> Vec_powersum(x constant=2)
> Sum of power of vector field X
> Vec_rangefx)
> Difference between maximum and minimum element in vector field X
> Vec_skewnessfx)
> Skewness ofvector field X
> Vec_stddevfx)
> Standard Deviation ofvector field X
> VeC_sum(x)
> Sum ofvector field X
> using


到这一步差不多就明白了世坤因子挖掘就是将他提供的数据字段和运算符计算和遍历后找到符合平台提交要求的因子！

但运算符是什么呢？


> [!NOTE] [图片 OCR 识别内容]
> 首页
> AI 搜索或打开网页
> 豆包
> 数据分析与处理
> 新对话
> 请依据我提供的操作符列表和数据集,
> 生成一些类似于
> C
> Al 搜索
> "liabilities
> assets" 这种有经济学解释的因子,
> 不限于除法操
> 作,
> 也可以是其他操作符组合而成的表达式,结果要以Python
> 3
> 帮我写作
> 的Lst[stn彩戎
> 9巩
> 操作符如下: [{'name': 'add; 'definition': 'add(x, Y filter
> [
> 图像生成
> false) X + y} {'name': 'log'; 'definition': 'log(x)'}, {'name
> 咕
> Al 阅读
> subtract; 'definition': 'subtract(x, Y, filterzfalse), X
> y'}
> {'name': 'signed_power'; 'definition': 'signed_power(x; y)
> }
> 
> Al 编程
> {'name': 'sign; 'definition': 'signfx)'} {'name': 'reverse;
> definition': 'reverse(x)'} {'name': 'power'; 'definition':
> 语音通话
> power(x, y)'}, {'name': 'multiply'; 'definition': 'multiply(x
> Al 看网站
> filter-false), X
> y'} {'name': 'min'; 'definition': 'min(x, Y
> }
> {'name': 'max'; 'definition': 'max(x, Y ..)} {'name': 'inverse';
> 'definition': 'inverse(x)'}, {'name': 'densify; 'definition':
> 最近对话
> 'densify(x)'} {'name': 'abs'; 'definition': 'abs(x)'}, {'name':
> 数据分析与处理
> 'divide'; 'definition': 'dividelx, y), X/y'} {'name': 'equal;
> 'definition':
> inputl == input2'} , {'name': 'less'; 'definition':
> 解释每股账面价值
> 'inputl
> input2'}, {'name': 'and'; 'definition': 'and(inputl,
> 手机版对话0
> {'name': 'or'; 'definition': 'or(inputl, input2)'}
> {'nai
> 'not_equal'; 'definition': 'inputl!= input2'}, {'name':
> 数据指标分析
> Innt
> 'dofinitinn'
> Int/yl'
> ['namo
> 'oroator'
> 'rofinitinn'
> 介绍南大通用产品
> AI 编程
> 图像生成
> AI 搜索
> T 帮我写作
> Q Al 阅读
> 学术搜索
> 1  解题答疑
> 骷  更多
> 查看全部。
> 发消息。输入 @选择技能或 |选择文件
> AI 云盘
> Beta
> 深度思考
> 园 & &
> @
> 我的智能体
> inp'


继续在平台找：


> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com
> WorldQuant BRAIN
> Analyst Estimate Data for Eq..
> Price Volume Data for Equity
> New post
> WorldQuant BRAIN
> WORLDQUANT
> BRAIN
> Simulate
> QAlphas
> Learn
> Data
> Competitions (1)
> 88 Team
> 三
> Courses
> Operators
> Documentation
> bearch operators
> 6加
> Operators
> Unlock more complex operators at Expert; Master and Grandmaster Genius levels。
> FAQ
> Arithmet
> Events
> Operator
> Description
> Glossary
> absfx)
> Absolute Value ofx
> base
> add(x; y, filter = false); X +
> Add all inputs (at least 2 inputs required). If filter
> true; filterallinput NaN to 0 before
> adding
> base
> densify(x)
> Converts a
> grouping field of many buckets into lesser number of only available buckets so as to make
> base
> working With grouping fields computationally efficient
> Show more
> divide(x; y), XIy
> X/y
> base
> inerse(x)
> 1 /X
> Da
> log(x)
> Natural logarithm. For example: Log(high/low) uses natural logarithm of highllow ratio as stock weights_


看出来了吗？是不是跟豆包询问的界面长得一样？

运算符解决了就找数据字段的代码体现在哪了：


> [!NOTE] [图片 OCR 识别内容]
> 首页
> AI 搜索或打开网页
> 豆包
> 数据分析与处理
> 1411IC
> SIVUPCDCUIC
> UCIIIIICIUI |
> SIVUM_LDCVICI^I
> 新对话
> group)'} , {'name': 'group_backfill', 'definition':
> 'group_backfill(X, group, d, std = 4.0)'} {'name':
> C
> Al 搜索
> 'group_mean'; 'definition': 'group_mean(x, Weight, group)'}
> {'name': 'group_rank'i
> definition': 'group_rank(x, group)'}
> 3
> 帮我写作
> {'name': 'group_neutralize' 'definition': 'group_neutralizelx;
> [
> 图像生成
> group)'}]
> 数据集如下: [{'id': 'assets'; 'description': 'Assets
> Total'}
> 咕
> Al 阅读
> {'id': 'assets_curr'; 'description': 'Current Assets
> Total'}
> {'id': 'bookvalue_ps', 'description':
> Book Value Per Share'}
> 
> Al 编程
> {'id': 'capex'; 'description': 'Capital Expenditures'}, {'id':
> 语音通话
> 'cash;; 'description': 'Cash'}
> 'cash_st' 'description':
> 'Cash and Short-Term Investments'} , {'id': 'cashflow';
> Al 看网站
> 'description': 'Cashflow (Annual)'} {'id':
> 'Cashflow_dividends';
> description'=
> Cash Dividends (Cash
> Flow)'}, {'id': 'cashflow_fin; 'description': 'Financing
> 最近对话
> Activities
> Net Cash Flow'} {'id': 'cashflow_invst';
> 数据分析与处理
> 'description': 'Investing Activities
> Net Cash Flow'} {'id':
> 'cashflow_Op'; 'description': 'Operating Activities
> Net Cash
> 解释每股账面价值
> Flow'} {'id': 'cogs'; 'description': 'Cost of Goods Sold'}, {'id':
> 手机版对话0
> 'CU
> ratio'; 'description': 'Current Ratio'}, {'id': 'debt';
> 数据指标分析
> 'desu. .vlion': 'Debt'} {'id': 'debt_It'; 'description': 'Long-
> Tvn
> 厂1+
> T+~111
> 门;1。I^匕+
> +1
> II?nrirtizr1。 I^匕+
> 介绍南大通用产品
> AI 编程
> 图像生成
> AI 搜索
> T 帮我写作
> Q Al 阅读
> 学术搜索
> 1  解题答疑
> 骷  更多
> 查看全部。
> 发消息。输入 @选择技能或 |选择文件
> AI 云盘
> Beta
> 深度思考
> 园 & &
> @
> 我的智能体
> {'id':
> ;



> [!NOTE] [图片 OCR 识别内容]
> platform worldquantbrain.com
> Company Fundamental Data_
> Analyst Estimate Data for Eq..
> Price Volume Data for Equity
> New post
> WorldQuant BRAIN
> WORLDQUANT
> BRAIN
> Simulate
> Alphas
> Learn
> Data
> Competitions (1)
> 88 Team
> 三
> Region
> Delay
> Universe
> Data
> Datasets
> Company Fundamental Data for Equity
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
> assets
> Assets
> Total
> Matrix
> 959
> 15169
> 45334
> assets_CUrr
> Current Assets
> Total
> Matrix
> 7796
> 1472
> 9194
> bookvalue_ps
> Book Value Per Share
> Matrix
> 989
> 1430
> 7366
> capex
> Capital Expenditures
> Matrix
> 96%
> 5883
> 16697
> cash
> Cash
> Matrix
> 759
> 1376
> 8994
> cash_st
> Cashand Short-Term Investments
> Matrix
> 959
> 870
> 6711
> cashflow
> Cashflow (Annual)
> Matrix
> 939
> 1172
> 6674
> cashflow_dividends
> Cash Dividends (Cash Flow)
> Matrix
> 96%
> 1840
> 4619
> cashflow_fin
> Financing Activities
> Net Cash
> Matrix
> 979
> 703
> 5560
> cashflow_invst
> lnwestinouctiwities
> Nlot Cash FlOII
> Matrix
> 979
> 620
> 3766
> FIOW


在找到数据集代码就在这一页的时候，才真正理解为啥世坤需要有一定编程基础的同学加入，这样才能快速的进行自动化啊！

完全理解之后，尝试自己生成列表：（我还不知道这些列表叫啥，只能理解为用以上的运算符对数据集进行进行注释）


> [!NOTE] [图片 OCR 识别内容]
> 首页
> AI 搜索或打开网页
> 豆包
> 数据分析与处理
> 可能还需要检查是否有重复或冗余的因子;
> 确保每个因子都有独特的经济学意义。例如;市销率和企业价值与收入比可能类
> 新对话
> 似;
> 但根据定义不同
> 可能需要保留两者。
> 总结一下。我需要从运算符和数据集中挑选出最相关的组合。生成尽可能多的有经济学解释的因子;
> 并以正确的 Python 列表
> C
> Al 搜索
> 形式返回。
> 3
> 帮我写作
> 以下是基于提供的运算符和数据集生成的经济学因子列表:
> [
> 图像生成
> 收起
> 咕
> Al 阅读
> python
> 回 〉 ^
> 
> Al 编程
> "divide(assets_curr,
> liabilities_curr)
> # 流动比率
> 语音通话
> "divide(enterprise_value,
> revenue )
> # 市销率
> "divide (income,
> equity )
> # `净资产收益率
> (ROE)
> Al 看网站
> "divide (debt ,
> equity )'
> #  负债权益比
> "divide (income
> revenue)
> # `净利润率
> Idivide(liabilities ,
> assets )
> # 资产负债率
> 最近对话
> "divide (cashflow_Op,
> liabilities )"
> #  现金流负债比
> "divide(rd_expense,
> revenue )
> #  研发费用占比
> 数据分析与处理
> "divide (revenue, working_capital)"
> #  营运资本周转率
> Idivide (revenue,
> receivable)"
> #  应收账款周转率
> 解释每股账面价值
> "divide (cogs,
> inventory )
> #  存货周转率
> 手机版对话0
> Its_delta(cashflow_Op,
> 0=12 )"
> # 现金流增长率
> "ts_std_dev (revenue,
> 0=12)
> # 收入波动率
> 数据指标分析
> "group_Zscore (divide (income,
> equity) ,
> group)"
> # 行业调整ROE
> 介绍南大通用产品
> AI 编程
> 图像生成
> AI 搜索
> T 帮我写作
> q Al 阅读
> 学术搜索
> 1  解题答疑
> 骷  更多
> 查看全部。
> 发消息。输入 @选择技能或 |选择文件
> AI 云盘
> Beta
> 深度思考
> 园 & &
> @
> 我的智能体


最后就是复制粘贴，放到vscode里去运行啦！

login sucessful的那一刻才是最开心的，啊哈哈哈哈！

所以不懂代码也没事啊，干中学嘛。你自己就会开始优化自己的流程的，下一步就是再此理解代码是怎么自动运行的啦！加油哦💪🏻

---

## 讨论与评论 (25)

### 评论 #1 (作者: LS32866, 时间: 1年前)

您好，请问鑫鑫老师是谁呀

---

### 评论 #2 (作者: LL49894, 时间: 1年前)

thx

---

### 评论 #3 (作者: SS17089, 时间: 1年前)


> [!NOTE] [图片 OCR 识别内容]
> 么F:
> AI 擅^q打开颐页
> 数据分析与处理
> L| |
> 请依据我捉供的揉作符列表和数据朱
> 生成
> 些类似于
> "abilities
> assets
> "这种有经济学解释的因子;
> 下限于除法探
> 也可以是其他操怍符组合而成的表达式,
> 结耒要以Python
> HLi[a
> 深怍符如下
> [{name
> add
> definition'
> addfx  filter
> alsel
> Y} (name'; "log; definition'; 'oglx) } {name
> subtract' 'definition': 'subtractlx y fter-falsel
> name'
> signed
> pOwer; 'definition : ' signed_powerlx
> name
> sign
> definition'; 'signfi'} {name'
> 'reverse
> definition; 'reverselyl} {name'
> DOWCT
> definition'。
> powerlx yI'} {name'
> multiply
> cetinition
> 'multiplylx
> filterzfalsel
> Y} {name
> min
> Jefinition' : minlx,
> (name'
> max
> definition; 'maxlx Y ,1 {name
> 'inyerse
> detinition: 'iverselx)} {name'
> density; 'detiniton;
> densify(x
> {name
> abs; 'definition: abslx}'} {name :
> 'divide;
> definition ;
> dividelx, y) X/y'} {'name
> equal'
> definition; 'inputl == input2} {name
> Te55'
> defnition;
> IpUtl
> inputz'} {name
> and;
> detnition: 'andlinputl
> Inp
> {'name
> definition': 'or(inputt, inputz)'}
> (na
> not_equal; 'definition; 'input!= input2' }, {'name' ;
> otmnn
> nntlii
> TISm
> +
> CA1!
>  AI 编程
> 图像生成
> AI 搜袁
> _消息 _
> 物入 @ 选择技能或 /选释文件
> 匆深度思琴
> nnt
  
> [!NOTE] [图片 OCR 识别内容]
> Ug
> 1FH
> 苜页
> AI 擅夫t打开厥页
> 豆包
> 数据分析与处理
> 711」1 
> WCIIII
> SIWUNC3UUI
> 新对话
> 1+|
> groupl}, {name'
> group_backfill
> definition:
> group_backfIIIX, group,d
> 401'}, [name':
> AI 搜素
> group_mean
> Octiniton';
> group_meanlx, weight  groupl}
> ['name'
> group_rank; 'definition'; 'group_rank(x group)'}
> 么  帮我写怍
> ['name':
> group_neutralize '
> delinition: 'group_neutralizel
> [  图停生成
> groUDI}]
> 数捱集如下: [{'id; 'assets'
> descriptlon': Assets
> Total}
> AI 阅读
> ['id'。 'assets
> gzscription':
> Current Assets
> Total'}
> ['id'
> bookvalue_Ds
> descrption : Book Value Per Share'}
> 4 AI 编程
> ('id'
> Capex
> descriotion'
> Capital Expenditures' }, {'id:
> Q  语音通话
> cash'
> descrption': 'Cash} {'d;
> cash_st; 'description;
> Cashand Short-Term Investments } {'id': 'cashflow
> AI 看冈站
> description': 'Cashflow (Annualj}, {'id:
> Cashtlow_olvidends
> description'
> Cash Dwioenos
> Cash
> FlowJ} {'id'; 'cashflow_fin; 'description: 'Financing
> 最近对话
> Activities
> Net
> Flow'}, ['id'
> Cashtlow_invst
> 鼓据分析与处理
> description; 'Inyesting Actwities
> Net Cash Flow'} (Io:
> cashtlow_Op'
> description; 'Operating Actiyities
> Net Cash
> 解拜每股账面价值
> Flow'}, {'id': 'cogs
> description:
> Cost ol Goods Sold'} {'id'。
> 手机e对话[
> ratio'
> description': 'Current Ratio'}, {id: 'debt;
> 歆据指怀分忻
> dese
> flon"; 'Debt} {id; 'debt_lt'
> description;
> !|
> TaJI
> 介绍南大通用产
> G AI
> 编程
> 图像生成
> AI 搜;
> 么帮我写怍
> Q AI 阕谟
> 学术搜;
> 6  解题笞-
> go 更多
> 苴看全部
> 发消息,
> 勃入
> 选择浅能或 /选泽文件
> AI 云盘
> F深度思孝
> std
> CUIr
> Cash
> ong-
 想请教一下你这个数据集是哪里找到的？是代码生成的还是在网页上找的？

---

### 评论 #4 (作者: LL52271, 时间: 1年前)

我也没有编程基础，可以留个联系方式吗，想请教你下

---

### 评论 #5 (作者: LM97056, 时间: 1年前)

"后还有700多个未提交的，我手动提交了4天*8h，给我累惨了"

----写个自动提交的逻辑，不然真累死

---

### 评论 #6 (作者: ZG11262, 时间: 1年前)

大佬可以分享一下详细操作步骤吗

---

### 评论 #7 (作者: HN11319, 时间: 1年前)

Can you share more? How can you take the data file?

---

### 评论 #8 (作者: XM75236, 时间: 1年前)

干中学!!!!

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

--------------------------热爱生活的老毛---------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

---

### 评论 #9 (作者: XD81759, 时间: 1年前)

加油！

---

### 评论 #10 (作者: YC92090, 时间: 1年前)

太厉害了！从0基础到17天挖出48个因子，还能主动优化流程、理解剪枝与自动提交逻辑，这真的是超快成长的典范👏看到你那句「login successful 的那一刻才是最开心的」真的有共鸣，程式跑通的成就感无与伦比～加油，朝着100个因子迈进，Super Alpha 等你解锁💪🔥

---

### 评论 #11 (作者: LQ14436, 时间: 1年前)

优秀！

---

### 评论 #12 (作者: 顾问 LW67640 (小虎) (Rank 24), 时间: 1年前)

优秀加励志！ai的确是一个好帮手，解决了很多的问题。期待楼主更多的ai实践分享。

---

### 评论 #13 (作者: JB71859, 时间: 1年前)

可以很励志，从什么都不懂到提交40多个因子，成长的速度确实挺不错的，加油，提交到100个以后就可以组sa了。

干中学!!!!

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

---

### 评论 #14 (作者: SJ11007, 时间: 10个月前)

您好！请问这里的因子就是所说的alpha吗，放到vscode运行的时候是放单独的因子去跑还是需要组合呢？（刚刚加入几天的新人）

---

### 评论 #15 (作者: YF55648, 时间: 10个月前)

同为0基础，请问您说的鑫鑫老师在哪里可以看啊

---

### 评论 #16 (作者: KH92677, 时间: 9个月前)

相见恨晚的贴子，狂补基础啊

---

### 评论 #17 (作者: ZL95348, 时间: 9个月前)

请问鑫鑫老师是谁

---

### 评论 #18 (作者: CC85858, 时间: 9个月前)

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

[ZL95348](/hc/en-us/profiles/34408379218583-ZL95348)  课代表呀

---

### 评论 #19 (作者: CC85858, 时间: 9个月前)

SJ11007                                                                                                                                                                         都可以尝试

---

### 评论 #20 (作者: CH92851, 时间: 8个月前)

有志气啊，看到了这么励志的过程，有什么理由不能努力啊！一步步的来，脚踏实地的去做。

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

-----------------------------------------------------------------------------

---

### 评论 #21 (作者: SL99784, 时间: 5个月前)

感谢前辈！新人还在摸索，但是看到这篇帖子真是既学到了又感同身受。我一开始纯手搓因子，前几天刚开始研究代码，登陆成功的那一刻真的太开心！

---

### 评论 #22 (作者: JY55846, 时间: 3个月前)

==============================================================================

这也太牛了吧，同python一窍不通，最近还在加油补课，边学习边进步，加油加油

==============================================================================

---

### 评论 #23 (作者: XY60816, 时间: 2个月前)

很有启发，基础薄弱还在重走来时路。

---

### 评论 #24 (作者: GZ89021, 时间: 2个月前)

我是新生，0代码

上了3节课，2-3节课课程基本没听明白。

今天要交第三次课的作业来到这里

开始有点眉目了。谢谢您的帖子

---

### 评论 #25 (作者: ZZ22049, 时间: 2个月前)

你说的这些，数据字段，操作符，我都明白了，但是还是不知道怎么放进vscode自动回测

---

