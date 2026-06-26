# 【ValueFactor预测器】基于Performance评估alpha表现代码优化

- **链接**: https://support.worldquantbrain.com【ValueFactor预测器】基于Performance评估alpha表现代码优化_33825528566423.md
- **作者**: 顾问 KZ79256 (Rank 21)
- **发布时间/热度**: 11个月前, 得票: 65

## 帖子正文

首先感谢weijie老师提出的idea:

之前的实现都是基于SA实现的, 不过这样有以下几个可能问题

- 无法考虑已提交SA的影响
- 中心化的选择对于结果有一定影响
- 无法综合考虑所有的region

所以我觉得是不是可以根据Performance来评估alpha的表现

关于如何使用已提交alpha来估算Performance, 可参看 [这里](基于已提交alpha估算Performance代码优化_33824958369559.md)

这样的话, 就可以

- 考虑所有的RA和SA
- 综合考虑不同region
- 速度更快

不过, 目前VF和指标的关系还不是很明确

代码如下

已提交因子的数据采集这里不在赘述, 最后形成这样的一个dataframe, 必须包含以下几列, 包含RA和SA


> [!NOTE] [图片 OCR 识别内容]
> data[ [ 'alphald'
> datesubmitted
> pnl
> sharpe
> fitness
> turnover
> returns
> Margin'
> dradorn
> 0Os
> alphald
> dateSubmitted
> sharpe
> ftess
> turover
> Teturls
> margin
> dradown
> XIgQVI
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 2.01
> 1.42
> 0.1154
> 0.0625
> 0.001084
> 0.0389
> OISJGXY
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 1.68
> 1.44
> 0.1305
> 0.0958
> 0.001468
> 0.0594
> RAWewNz
> 2025-04-06
> {2010-04-14:nan '2010-04-15': nan '2010-0
> 223
> 1.44
> 0.2071
> 0.0869
> 0.000839
> 0.0383
> VOnOvqb
> 2025-04-06
> {2010-04-14:nan 2010-04-15': nan '2010-0。
> 1.85
> 1.57
> 0.0395
> 0.0900
> 0.004554
> 0.0665
> abdZp5
> 2025-04-06
> {2010-04-14:nan "2010-04-15': nan '2010-0
> 4.46
> 385
> 0.0776
> 0.0933
> 0.002406
> 0.0183
> 1399
> PATOOpL
> 2025-07-30
> {2013-01-21':00'2013-01-22:8368.0'201.
> 1.80
> 1.16
> 0.1255
> 0.0522
> 0.000832
> 0.0340
> 1400
> INjKaqz
> 2025-07-30
> {2013-01-21':00'2013-01-22:21054.0,"20:
> 1.88
> 1.17
> 0.1103
> 0.0486
> 0.000882
> 0.0387
> 1401
> PATZZnW
> 2025-07-30
> {2013-01-21:0.0,'2013-01-22:853.0,'2013。。
> 1.97
> 1.17
> 0.0631
> 0.0444
> 0.001407
> 0.0245
> 1402
> vojkdk
> 2025-07-30
> {2013-01-21:00,"2013-01-22':-508000'2:
> 1.02
> 1.18
> 0.2476
> 03323
> 0.002684
> 0.4667
> 1403
> 32759U
> 2025-07-30
> {2013-01-21:nan "2013-01-22':00'2013-0
> 409
> 4.16
> 0.1317
> 0.1361
> 0.002068
> 00277
> 1118 rows
> columns
> pnl


首先通过之前的贴子里的estimate_performance_func估算某三个月某个region-delay下已提交的所有alpha的综合性能

接着平等考虑每个region-delay下的结果, 形成这个时间段下所有的已提交的SA和RA的综合Performance

```
def calc_region_delay(data):    local_pnls, local_ret, item_metric = estimate_performance_func(data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"    return pd.DataFrame([item_metric])def calc_all_region_delay(calc_data):    calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)    local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['alphaId'] = f"{data['region'].iloc[0]}-{data['delay'].iloc[0]}"    return pd.DataFrame([item_metric])
```

```
data = data.sort_values('dateSubmitted')data['year_month'] = data['dateSubmitted'].dt.to_period('M')year_month = sorted(data['year_month'].unique())metric = []for i in range(len(year_month)-2):    calc_data = data[data['year_month'].isin([year_month[i], year_month[i+1], year_month[i+2]])]    calc_data = calc_data.groupby(['region', 'delay']).apply(calc_region_delay)    local_pnls, local_ret, item_metric = estimate_performance_func(calc_data)    item_metric['pnl'] = local_ret.cumsum().to_dict()    item_metric['month_end'] = year_month[i+2]    item_metric = pd.DataFrame([item_metric])    metric.append(item_metric)metric = pd.concat(metric, axis=0).reset_index(drop=True)
```

这里需要提供一个vf的数据

```
vf = {'2025-05': 0.75, '2025-04':0.91, '2025-03':0.96, '2025-02': 0.9, '2025-01':0.73, '2024-12':0.77}vf = pd.Series(vf, name='vf')vf.index = pd.to_datetime(vf.index).to_period('M')metric = metric.merge(vf, left_on='month_end', right_index=True, how='left')metric = metric[metric['month_end']>=pd.to_datetime('2024-12').to_period('M')].reset_index(drop=True)
```

绘制pnl图

```
plt.figure(figsize=(10, 6))for item, item_month_end, item_vf in zip(metric.pnl, metric.month_end, metric.vf):    item = pd.Series(item)    item.index = pd.to_datetime(item.index)    plt.plot(item.index, item.values, label=f'{item_month_end}: {item_vf:.2f}')    # item.plot(label=item.name, figsize=(10, 6))plt.legend(loc='upper left', frameon=False, prop=font_prop18, bbox_to_anchor=(0, 1))plt.xlabel('Date', fontproperties=font_prop20)plt.ylabel('Pnl', fontproperties=font_prop20)plt.xticks(rotation=45, fontproperties=font_prop18)plt.yticks(fontproperties=font_prop18)plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))plt.gca().xaxis.set_ticks_position('both')  # 在x轴的上下两边都显示刻度plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度for spine in plt.gca().spines.values():    spine.set_linewidth(2)plt.gca().tick_params(direction='in', length=6, width=2)  # length是刻度的长度，width是刻度的宽度plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')  
```


> [!NOTE] [图片 OCR 识别内容]
> Ie7
> 2024-12:0.77
> 1.2
> 2025-01:0.73
> 2025-02:0.90
> 2025-03:0.96
> 2025-04:0.91
> 2025-05:0.75
> 忌
> 0.6
> 2025-06: nall
> 2025-07: nan
> 0.3
> Date
> 2016-07-17
> 2022-01-07
> 2013-10-21
> 2019-04-13


指标和vf的关系

```
plot_cols = ['sharpe', 'turnover', 'returns', 'fitness', 'drawdown', 'margin',]plt.figure(figsize=(2*5, 3*5))for idx, col in enumerate(plot_cols):    plt.subplot(3, 2, idx+1)    plt.scatter(metric['vf'], metric[col])    # 标记最近两个月的metric值    colors = ['blue', 'red']    for i, item_metric in metric.iloc[-2:].reset_index().iterrows():        plt.axhline(item_metric[col], color=colors[i], linestyle='--', lw=1, label=f'{item_metric.month_end}: {item_metric[col]:3f}')    plt.legend(loc='best', frameon=False, prop=font_prop16)    plt.xlabel('VF', fontproperties=font_prop20)    plt.ylabel(col, fontproperties=font_prop20)    plt.xticks(fontproperties=font_prop18)    plt.yticks(fontproperties=font_prop18)    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_ticks_position('both')  # 在x轴的    plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度    for spine in plt.gca().spines.values():        spine.set_linewidth(2)    plt.gca().tick_params(direction='in', length=6, width=2)    plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')plt.tight_layout()
```


> [!NOTE] [图片 OCR 识别内容]
> 8.8
> 0.165
> 0.150
> 8.0
> 2025-06:0.163371
> 詈
> 
> 0.135
> 2025-07:0.169481
> 7.2
> 0.120
> 2025-06:9.139539
> 2025-07:8.962392
> 0.105
> 0.72
> 0.78
> 0.84
> 0.90
> 0.72
> 0.78
> 0.84
> 90
> 96
> TE
> TE
> 0.13
> 8.0
> 0.12
> 7.2
> 
> 0.11
> 鲁
> 6.4
> 0.10
> 5.6
> 2025-06:0.122011
> 2025-06:7.898325
> 2025-07:0.123720
> 2025-07:7.657435
> 72
> 0.78
> 0.84
> 0.90
> 0.72
> 0.78
> 0.84
> 0.90
> TE
> TE
> 2025-06:0.007365
> 2025-07:0.009269
> 0.014
> 0.0021
> 0.012
> 0.0018
> 
> 0.010
> 
> 0.0015
> 0.008
> 0.0012
> 2025-06:0.001421
> 2025-07:0.001430
> 006.52
> 0.78
> 0.84
> 0.90
> 96
> 0.72
> 0.78
> 0.84
> 0.90
> 0.96
> VF
> T


很奇怪, vf和sharpe还有点负相关=.=!!

可能vf是样本外的数据?, 或者vf只是个排名?, 还需要进一步查看, 或许看一下yearly-stats是不是更好一点

上述的时间都代表所述三个月的最后一个月

---

## 讨论与评论 (1)

### 评论 #1 (作者: HW54322, 时间: 10个月前)

VF预测器，好耶

---

