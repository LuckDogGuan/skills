# 纠正LEARN模块关于ts_arg_min的举例错误

- **链接**: https://support.worldquantbrain.com[Commented] 纠正LEARN模块关于ts_arg_min的举例错误_29409181834519.md
- **作者**: AK76468
- **发布时间/热度**: 1年前, 得票: 4

## 帖子正文

如下图所示，关于ts_arg_min(x, d)的举例中:

```
“...is present 4 days before today. Hence ts_arg_min(x,d) = 1”
```

这里给出的例子有错误，应更正为:

```
“...is present 1 day before today. Hence ts_arg_min(x,d) = 1”
```


> [!NOTE] [图片 OCR 识别内容]
> ts_arg_max(x, d)
> Returns the relative index ofthe max value in the time series forthe past d days. If the current
> has the max value for the past d days, it returns 0.If previous
> has the max value for the past d days, it returns
> Show less
> It returns the relative index of the max value in the time series for the past d days. If the current
> has the max value for the past d days, it returns 0. If previous day has the max value for the past d
> days, it returns 1.
> Example:
> Ifd = 6 and values for past 6 days are [6,2,8,5/9,4] with first element being todays value then max
> Value is 9and
> is present 4ldays before today. Hencelts_arg_maxfx 9) =4
> ts_arg_minfx, d)
> Returns the relative index of the min value in the time series for the past d
> Ifthe current
> has the min value for the past d
> i returns 0; If previous
> has the min value for the past d
> i returns 1
> Show less
> ts_arg_minfx, d)
> It returns the relative index of the min value in the time series for the past d
> If the current
> has the min value for the past d days, it returns 0. If previous
> has the min value forthe
> 9
> i returns 1.
> 此例应该是前-一天
> Example:
> Ifd = 6 and Values for
> days are [6,2,8,5,9,4] with first element being todays value then min
> Value is 2 andlt is present 4days before today. Hence
> arg_minfx, d) =1
> day
> day
> day
> days;
> day
> days;
> day
> days;
> dayS。
> day
> day
> past
> dayS,
> past
> tS_C


这个举例错误带来了一点困扰，浪费了一些不必要的时间在思考错误的答案上...

希望马上更正过来，帮助其他新用户更好的学习！！！

Love&Peace :D

---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 PN39025 (Rank 87), 时间: 1年前)

是的，我看到这个例子有一个时间问题，但还没有找到解决方案，谢谢您的分享。

---

### 评论 #2 (作者: CC85858, 时间: 9个月前)

已经改过来了，感谢指出让平台发现

---

