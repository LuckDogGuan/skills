# 【这个alpha可以交吗？】从平台sharpe的计算规则角度来看尾部翘头（低头）的alpha可以交吗

- **链接**: https://support.worldquantbrain.com【这个alpha可以交吗】从平台sharpe的计算规则角度来看尾部翘头低头的alpha可以交吗_36465055883287.md
- **作者**: 顾问 JG15244 (Rank 67)
- **发布时间/热度**: 7个月前, 得票: 32

## 帖子正文

在日常寻找alpha的时候，经常会见到前面几年平平无奇，而最后一年却猛然拉升的alpha，又或者最后一年突然拉低的alpha，那么这种alpha还可以交吗？

其实我也不知道能不能交...但是这样的alpha平台上的submit按钮确实是亮的，有时候我会想，是不是因为最后一年的数据太好了，所以将综合指标拉高了，才达到了可以提交的门槛呢？

然后我去仔细看了一下平台关于sharpe的计算规则，自己复现了一下，发现好像影响并不会很大。

**平台的计算规则：**

**
> [!NOTE] [图片 OCR 识别内容]
> 夏普比率和信息比率
> 信息比率 (IR) 衡量模型的预测能力。在BRAIN平台中,定义为组合每日平均收益与这些收益的波动率之比:
> TeQT2
> PnL)
> IR =
> stdev(PnL)
> 其中Pnl 是每日盈亏。以美元计算
> Sharpe是1R统计量的年化版本,即Sharpe=sqrt(252)IR ~ 15.8IR。 其中252是一年中美国交易日 (市场开放
> 日)  的平均数量。
> Sharpe或IR衡量Alpha的回报。同时尝试识别其一致性。 |R越高。 Alpha的回报就越一致,一致性是理想的特
> 征。高Sharpe (或IR)  比仅仅高回报更为理想。
> 注意: Sharpe和IR在BRAIN平台以外的其他地方可能会被定义得略有不同。
**

**借助gemini3.0实现的代码：**

```
import jsonimport pandas as pdimport numpy as npfrom math import sqrt# =================配置区域=================FILE_NAME = 'pnl_amr.json'STOP_YEAR = 2023  # 设置截止年份# =========================================def calc_sharpe(series):    """    计算 WorldQuant 标准的 Sharpe Ratio    """    if len(series) < 2: return 0.0    mean = series.mean()    std = series.std(ddof=1) # 样本标准差    if std == 0: return 0.0    return (mean / std) * sqrt(252)def main():    # 1. 读取数据    with open(FILE_NAME, 'r', encoding='utf-8') as f:        data = json.load(f)    df = pd.DataFrame(data['records'], columns=['date', 'pnl'])    df['date'] = pd.to_datetime(df['date'])    df = df.sort_values('date')    # 2. 数据清洗与 Daily PnL 计算    # 确保数值类型并填充缺失    df['pnl'] = pd.to_numeric(df['pnl'], errors='coerce').ffill()       # 计算每日差分    df['daily_pnl'] = df['pnl'].diff()    # 补回第一天的数据 (第一天的日收益 = 第一天的累计收益)    df.loc[df.index[0], 'daily_pnl'] = df.iloc[0]['pnl']       # 3. 打印分年度 Sharpe (Yearly)    print("\n" + "=" * 60)    print(f"{'Year':<6} | {'Days':<6} | {'Mean PnL':<12} | {'Sharpe':<8}")    print("-" * 60)    for year, sub_df in df.groupby(df['date'].dt.year):        sharpe = calc_sharpe(sub_df['daily_pnl'])        mean_val = sub_df['daily_pnl'].mean()        print(f"{year:<6} | {len(sub_df):<6} | {mean_val:<12.2f} | {sharpe:.4f}")    print("-" * 60)    # 4. 计算【智能全时段】Sharpe (自动剔除首尾的0)    # ---------------------------------------------------    non_zero_indices = df.index[df['daily_pnl'] != 0].tolist()    if non_zero_indices:        first_idx = non_zero_indices[0]        last_idx = non_zero_indices[-1]        df_active = df.loc[first_idx : last_idx]               total_sharpe = calc_sharpe(df_active['daily_pnl'])        print(f"{'Total':<6} | {len(df_active):<6} | {df_active['daily_pnl'].mean():<12.2f} | {total_sharpe:.4f}")        print(f"       (自动截取活跃期: {df_active['date'].dt.date.iloc[0]} 到 {df_active['date'].dt.date.iloc[-1]})")    else:        print("Total  | 0      | 0.00         | 0.0000")    print("-" * 60)    # 5. 计算【剔除特定年份后】的 Sharpe (按你的要求)    # ---------------------------------------------------    # 这里的逻辑是：保留年份 < STOP_YEAR 的数据    # 如果你想保留2023年，请将下面的 `<` 改为 `<=`       df_cutoff = df[df['date'].dt.year < STOP_YEAR].copy()       # 同样应用“剔除首尾0”的逻辑，防止早期数据也有0    cutoff_indices = df_cutoff.index[df_cutoff['daily_pnl'] != 0].tolist()       print(f"\n>>> 特别计算：剔除 {STOP_YEAR} 年及之后的数据")       if cutoff_indices:        c_first = cutoff_indices[0]        c_last = cutoff_indices[-1]        df_cutoff_active = df_cutoff.loc[c_first : c_last]               cutoff_sharpe = calc_sharpe(df_cutoff_active['daily_pnl'])               print(f"Sharpe (Before {STOP_YEAR}): {cutoff_sharpe:.4f}")        print(f"数据范围: {df_cutoff_active['date'].dt.date.iloc[0]} 到 {df_cutoff_active['date'].dt.date.iloc[-1]} (共 {len(df_cutoff_active)} 天)")    else:        print(f"Sharpe (Before {STOP_YEAR}): 0.0000 (无有效数据)")           print("=" * 60)if __name__ == "__main__":    main()
```

这里，我随便找了一个最后一年2023年翘头（指标很高）的alpha来测试


> [!NOTE] [图片 OCR 识别内容]
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.66
> 9.25%
> 1.03
> 30.409
> 74.91%
> 65.729600
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> 2013
> 0.11
> 13.2596
> 0.06
> 3.33%
> 33.04%
> 5.039600
> 24
> 15
> 2014
> 0.57
> 8.6796
> 66
> 16.80%
> 22.05%
> 38.739600
> 24
> 2015
> 0.77
> 5.01%6
> ,09
> 25.22%
> 19.68%
> 100.739600
> 36
> 29
> 2016
> 0.31
> 4.20%6
> 0.22
> 6.33%
> 23.65%
> -30.159600
> 15
> 34
> 2017
> 0.37
> 6696
> 47
> -20.50%6
> 52.24%
> 61.569600
> 24
> 20
> 2018
> 1.95
> 3.0696
> 4.81
> 76.07%6
> 16.47%
> 168.019600
> 18
> 46
> 2019
> 0.27
> 10.5196
> 0.26
> -11.66%
> 49.45%6
> -22
> 9960o
> 12
> 32
> 2020
> 2.01
> 12.2596
> 5.81
> 143.45%
> 50.45%
> 234
> 2960o
> 33
> 23
> 2021
> 0.25
> 12.2596
> 0.27
> 14.75%
> 58.0096
> 24.099600
> 47
> 47
> 2022
> ,06
> 9.3296
> 2.28
> 57.84%
> 32.8396
> 124.089600
> 25
> 30
> 2023
> 3.85
> 23.3796
> 11.24
> 199.15%
> 4.4796
> 170.409600
> 18
 代码计算结果如下：


> [!NOTE] [图片 OCR 识别内容]
> Year
> Days
> Mean Pnl
> Sharpe
> 2013
> 245
> 1332.30
> 0.1123
> 2014
> 258
> 6718.57
> 0.5741
> 2015
> 258
> 10087.19
> 0.7719
> 2016
> 259
> 2530.88
> -0.3144
> 2017
> 258
> -8200.89
> -0.3733
> 2018
> 258
> 30428.13
> 1.9604
> 2019
> 258
> -4665.51
> -0.2718
> 2020
> 237
> 57381.42
> 2.0131
> 2021
> 259
> 5901.18
> 0.2526
> 2022
> 259
> 23136.46
> 1.0641
> 2023
> 15
> 79660.13
> 3.8635
> Total
> 2536
> 12165.92
> 0.6620
> (自动截取活跃期:
> 2013-02-28  到
> 2023-01-20)
> 〉>
> 特别计算:  剔除  2023  年及之后的数据
> Sharpe (Before 2023):
> 0.6420
> 数据范围:
> 2013-02-28  到
> 2822-12-15 (共
> 2510 天)


可以看出来，代码计算得到的sharpe值和平台的sharpe一致，可以说明代码计算的没有问题。

然后我将最后一年（2023年）的数据去除不参与计算，得到的sharpe为0.64，与没去除之前的0.66相比，仅差了0.02。

所以，我个人认为，最后一年的异常指标其实并不会影响最后的Aggregate Data指标，也就是说，你的Aggregate Data达到了标准后，其实没有必要过分关注最后一年的指标数据。

> > 我是用最后一年翘头的来计算的，低头的同理。
> > 我只计算了sharpe的值，对应fitness的值没有进行计算，计算方式在平台文档里也有写，但是好像获取不到每天的return，所以计算不了。

最后，这里仅是从sharpe计算的角度来说明，最后一年的异常指标不会对Aggregate Data的指标产生较大比重的影响，但是不能排除2023年1月份走势向下了，2023年2月份->至今走势就不向下了。

---

## 讨论与评论 (1)

### 评论 #1 (作者: WL13229, 时间: 7个月前)

不如直接抓取pnl来计算sharpe of last 200 trading days

---

