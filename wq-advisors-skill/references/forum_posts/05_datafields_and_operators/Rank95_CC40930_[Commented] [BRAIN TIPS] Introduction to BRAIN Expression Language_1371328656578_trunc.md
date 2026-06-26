# [BRAIN TIPS] Introduction to BRAIN Expression Language

- **链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] Introduction to BRAIN Expression Language_13713286565783.md
- **作者**: AS34454
- **发布时间/热度**: 3年前, 得票: 10

## 帖子正文

## 1. What is Fast Expression?

“Fast expression” is a proprietary programming language used by WorldQuant BRAIN that is designed to make it easier to write and test financial models. The language can be thought as a form of pseudo code, which uses natural language and simple programming constructs to convey the logic of the algorithm.

The goal of using “Fast expression” on BRAIN is to provide a clear and concise way to express complex ideas and algorithms that can be easily understood by other developers and researchers. By abstracting away the details of the underlying implementation, it can allow BRAIN users to focus on the high-level logic of their algorithms, rather than getting bogged down in the implementation details.

## 2. Characteristics of Fast Expression

Just like how an English sentence consists of a subject, verb and object; Fast expression can include data fields, operators and numerical values.

### Data fields

Data fields refer to a named collection of data, for example 'open price' or 'close price'.


> [!NOTE] [图片 OCR 识别内容]
> Dataset
> Field
> Company Fundamental Data for Equity
> 1,575
> US News Data
> 644
> Relationship Data
> 82
> Options Analytics
> 74
> Price Volume Data for Equity
> 72
> Field
> Description
> Type
> adv20
> Average daily volume in past 20 days
> Matrix
> Close
> Daily close price
> Matrix
> returns
> Daily returns
> Matrix
> Volume
> Daily volume
> Matrix


### Operators

[Operators](https://platform.worldquantbrain.com/learn/data-and-operators/operators)  refer to a set of mathematical techniques required to implement your Alpha ideas.


> [!NOTE] [图片 OCR 识别内容]
> Arithmetic Operator
> Description
> Arithmetic operators: add, subtract; multiply; divide;
> DOWeF
> log(x)
> Natural logarithm
> Cross Series Operator
> Description
> rank(x; n)
> Ranks the input among all the instruments and returns
> an
> equally distributed number between 0.0 and 1.0
> Time Series Operator
> Description
> tsS_rank(x; n)
> Rank the values of x for each instrument over the past
> days
> then return the rank of the current value
> The
> rank Value is between 0.0and 1.0


## 3. Further Knowledge of Fast Expression


> [!NOTE] [图片 OCR 识别内容]
> 鬯 
> Simulate
> Alphas
> Competitions (1)
> @ Team
> Events
> Learn
> Refer
> friend
> Simulation
> Settings
> USA/D1/TOP30O0
> HYPOTHESIS; If
> Stock Closes below its
> open
> price more often in the Iast month
> Compared to the Iast year
> there could be
> reversal in the stock
> price and 让
> may increase in the short term。
> IIPLENENTATIOINI; Buy
> Tore
> Of stocks for Which such days OCCUr
> more often (ts_SUm) in last month (20 days), Compared
> to the last year (250 days)
> HIIIT
> Can introducing the intensity of daily stock fluctuations Or price instability improve the alpha?
> SUI(Open〉
> 20/1t5
> SUN(open
> CIose,
> SUM(open
> 250)
> ts_SU(apencclose, 25
> rank(a/b)
> Close
> CIose


- ***/****  helps to create block comments that span multiple lines of text, while ****/***  denotes the end of the comment. Comments consist of explanatory text to help understand what the code does. [1]
- ***;*** (semicolon) acts as a semicolon in a sentence, separating the end of one sentence from the beginning of another sentence. For the last line of the code (line 13) ; is not needed. [2]
- The last sentence of the entire expression is the alpha expression that the BRAIN simulator use to calculate the positions to take in each stock. [3]
- Lastly, Fast expression does not have classes, objects, pointers, or functions.

In summary, Fast expression provides a clear and concise way for users to express complex ideas and algorithms. Don’t worry if you’re not familiar with Fast expression yet. With a bit of practice, we believe you’ll pick it up in no time!

---

## 讨论与评论 (5)

### 评论 #1 (作者: deleted user, 时间: 1年前)

I hope that Brain will allow options to code in python or c++ to make it easier for experienced coders to custom alpha.

---

### 评论 #2 (作者: HV77283, 时间: 1年前)

Thank you so much for sharing such a great n wonderful information  . Your points and explanations help us to improve our work quality.Great tips.

---

### 评论 #3 (作者: TT55495, 时间: 1年前)

Thank you so much for your valuable insights! I really appreciate the detailed explanation of Fast Expression and its characteristics. Your information about the impact of group coalescing on backtest results is incredibly helpful and will definitely assist me in developing better alpha strategies.

---

### 评论 #4 (作者: TD17989, 时间: 1年前)

I hope Brain will provide more debugging features and ai bot to support more effective alpha in the future

---

### 评论 #5 (作者: 顾问 CC40930 (Rank 95), 时间: 1年前)

Fast Expression is a proprietary programming language developed by WorldQuant BRAIN to simplify the creation and testing of financial models. It functions like pseudo-code, using natural language and straightforward programming constructs to express algorithmic logic clearly and concisely.

---

