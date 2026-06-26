# Use of operator ts_step

- **链接**: https://support.worldquantbrain.com[L2] Use of operator ts_step_13580036296087.md
- **作者**: LN14840
- **发布时间/热度**: 3 years ago, 得票: 3

## 帖子正文

Can you give me an example of how ts_step working? I have implemented some alphas with it, but I don't see any difference.

---

## 讨论与评论 (7)

### 评论 #1 (作者: SH71033, 时间: 3 years ago)

ts_step is like a day counter, which, with today's value provided as an argument, back counts the number of days in the simulation.
for ts_step(1), for the simulation day, it would count 1 as today, 0 as yesterday, -1 as day before yesterday etc.
Thus, ts_regression(close, ts_step(1), 5) would mean you are regressing close over the 5 days with the array [1,0,-1,-2,-3,] for the 5 day regression window.
Thus, you see ts_step being used as a day counter to regress over time.

You can refer to the learn section for more examples on ts_step.

---

### 评论 #2 (作者: deleted user, 时间: 1 year ago)

Hello, I want to ask for example using ts_step(1), is 1 considered as 1 datafield? Or is it a number. Hope to get an answer. Thank you very much.

---

### 评论 #3 (作者: AV23565, 时间: 1 year ago)

In my experience with the  `ts_step(1)`  operator, I’ve noticed that the "1" is considered a number, not a datafield. It represents the step or interval in time, not a specific datafield.

---

### 评论 #4 (作者: XL31477, 时间: 1 year ago)

**Hey guys! Regarding ts_step, as  [SH71033](/hc/en-us/profiles/10135105894423-SH71033)  said, it's like a day counter. For example, ts_step(1) counts days in the simulation. And as**  **[AV23565](/hc/en-us/profiles/22221929197463-AV23565) pointed out, the "1" in ts_step(1) is indeed a number representing the time interval.  [TK95999](/hc/en-us/profiles/18243496991767-TK95999) , it's not a datafield. You can use it in functions like ts_regression to analyze data over time intervals. Hope this clears things up!**

---

### 评论 #5 (作者: NH84459, 时间: 1 year ago)

Hi, I would like to ask for example multivariate function like ts_regression, if I let variable x be ts_step(day) and y be 1 data like return, will it be effective?

---

### 评论 #6 (作者: BA51127, 时间: 1 year ago)

**Understanding  `ts_step`** : The  `ts_step`  operator functions as a day counter in simulations. For instance,  `ts_step(1)`  would count the current day as 1, the previous day as 0, and so on, providing a sequential count of days.
 **Application in  `ts_regression`** : When used within  `ts_regression(close, ts_step(1), 5)` , it indicates a regression of the  `close`  price over the past 5 days, with the array  `[1, 0, -1, -2, -3]`  representing the days in the regression window.
 **Clarification on "1" in  `ts_step(1)`** : The "1" is a number representing the time interval and is not considered a datafield. It signifies the step size in the time series analysis.
 **Effectiveness in Multivariate Functions** : For multivariate functions like  `ts_regression` , using  `ts_step(day)`  for one variable and a single datafield like  `return`  for another can be effective, as it allows for the analysis of how returns change over time intervals.

---

### 评论 #7 (作者: NH84459, 时间: 1 year ago)

- `ts_step(1)`  counts today as 1, yesterday as 0, the day before yesterday as -1, and so on.
- When used with a regression function like  `ts_regression(close, ts_step(1), 5)` , you're essentially performing a regression on the  `close`  price over a window of 5 days. In this case, the window would look like  `[1, 0, -1, -2, -3]` , where 1 corresponds to today's data, 0 to yesterday, -1 to the day before yesterday, and so forth.

---

