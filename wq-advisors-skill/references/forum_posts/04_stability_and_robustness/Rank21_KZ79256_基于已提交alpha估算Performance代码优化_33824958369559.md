# 基于已提交alpha估算Performance代码优化

- **链接**: https://support.worldquantbrain.com基于已提交alpha估算Performance代码优化_33824958369559.md
- **作者**: 顾问 KZ79256 (Rank 21)
- **发布时间/热度**: 11个月前, 得票: 73

## 帖子正文

在alpha界面有一个Performance Comparison, 一个自然而然的问题就是这个Performance是怎么计算的. 这里通过已提交的alpha计算before Performance.

结果展示

首先是本地计算(local)和云端计算(cloud)的每日盈亏, 整体来看本地估算和云端计算的结果比较相近


> [!NOTE] [图片 OCR 识别内容]
> USA-DO
> USA-DI
> 80000
> Num=30
> 60000
> Num=502
> p=0.97
> p=0.95
> 40000
> 30000
> 菡
> 
> 
> -30000
> -40000
> IOT
> bgh
> IOT
> lgh
> Density
> Densit
> -40000
> 40000 SOd00
> -4000620000
> 2000040000
> Local Ret
> Local Ret
> AMR-DI
> 40000
> ASI-DI
> 100000
> Num=l6
> Num=l68
> p=1.00
> 0.99
> 20000
> 50000
> 蓝
> 蓖
> 
> 晷
> -20000
> -50000
> IOW
> ligh
> IOW
> Density
> -40000
> -50000
> 50000 100000
> -20000
> 20000
> 40000
> Local Ret
> Local Ret
> 160000
> CINNDI
> EUJR-DI
> Nul=l5s
> 40000
> Num=l90
> 80000
> p=0.94
> p=0.98
> 蓖
> 惑
> 20000
> 
> 
> -80000
> -20000
> IOT
> bieh
> IOT
> bgh
> Density
> Density
> 一160000
> -12000860000
> 60000120000
> -20000
> 20000 40000
> Local Ret
> Local Ret
> 80000
> 100000
> GLB-DI
> HGDl
> Num=S0
> Num=27
> p=1.00
> 40000
> p=l.00
> 茁
> 茁
> 詈
> 100000
> 詈
> -40000
> -200000
> IOT
> bgh
> IOT
> lgh
> Density
> -80000
> Density
> -2400606000080000
> 80000
> -80000-40000
> 40000 80000
> Local Ret
> Local Ret
> 80000
> 100000
> JND1
> KOR-DI
> Num=s
> Num=S0
> p=1.00
> p=1.00
> 40000
> 50000
> 蔹
> 蓖
> 
> 晷
> -50000
> -40000
> IOT
> IOT
> 'Densityel
> -40000
> 40000
> 80000
> -50000
> SO000 IOOO00
> Local Ret
> Local Ret
> 100000
> TWNDI
> Nul=4
> 1.00
> 50000
> 惑
> 
> 50000
> IOT
> Densitligh
> -50000
> S0000 I00000
> Local Ret
> 蓖
> 0二
> Densitigh
> Densityfieh
> p二


接下来是估算的各个指标和线上指标的对比


> [!NOTE] [图片 OCR 识别内容]
> PnI
> drawdown
> UUIIONBI
> TCUUIIIS
> margin
> shampe
> ftess
> Tegion_delay
> Idex
> US4-0
> true
> 9.1468438+06
> 0.009400
> 0.194500
> 0.091600
> 0.000942
> 5.130000
> 3.520000
> 7.7876182+06
> 0.009410
> 0.203300
> 0.095180
> 0.000931
> 4820702
> 3.298485
> US4-1
> true
> 1.608381e+07
> 0011100
> 0138200
> 0.136500
> 0.001976
> 6910000
> 6.870000
> 1.4005202+07
> 0.009288
> 0.141468
> 0.143071
> 0.002132
> 8485042
> 8532991
> AAR-1
> tue
> 1.1981002+07
> 0.029600
> 0.168000
> 0.116900
> 0.001392
> 3.880000
> 3240000
> pred
> 1.1476752+07
> 0027718
> 0,165938
> 0.116712
> 0.001401
> 3.656892
> 3.066892
> 4S1-1
> true
> 1.0840882+07
> 0.005800
> 0.172700
> 0.095200
> 0.001102
> 8370000
> 6210000
> 1.018014e+07
> 0.005419
> 0.164132
> 0.096548
> 0.001208
> 8423970
> 6.460886
> CHN-I
> true
> 1.5425632+07
> 0074100
> 0175200
> 0.152800
> 0.001744
> 40000O0
> 3.740000
> 1.5767292+07
> 0.064552
> 0.181900
> 0.149400
> 0.001663
> 4.434734
> 4019079
> EUR-I
> tue
> 1.185887e+07
> 0.007100
> 0.129100
> 0.104400
> 0.001617
> 9.080000
> 8170000
> pred
> 1.2557902+07
> 0021566
> 0131339
> 0.106275
> 0.001973
> 6368670
> 5.728832
> GLB-1
> true
> 1.2991402+07
> 0.038800
> 0.243500
> 0.114000
> 0.000937
> 3.690000
> 2520000
> 1.2668262+07
> 0.038815
> 0.240434
> 0.116800
> 0.001022
> 3.686740
> 2569603
> HG 1
> true
> 9.5816902+06
> 0032400
> 0065700
> 0,092600
> 0.002819
> 3.720000
> 3200000
> pred
> 9.537564e+06
> 0032403
> 0065659
> 0.092559
> 0.002841
> 3.721863
> 3202693
> JPN1
> tue
> 6.1226252+06
> 0.016300
> 0.075000
> 0.059200
> 0.001577
> 3.020000
> 2080000
> pred
> 61147602+06
> 0016334
> 0075040
> 0.059180
> 0.001573
> 2886310
> 1.985982
> KOR-I
> true
> 1.4870882+07
> 0063300
> 0,159800
> 0.137100
> 0.001717
> 3.870000
> 3580000
> 1.4809662+07
> 0.063388
> 0.151244
> 0.132242
> 0.001789
> 3.891873
> 3.639186
> TNI
> true
> 1.0209202+07
> 0025300
> 0064800
> 0,098600
> 0.003046
> 3420000
> 3.040000
> pred
> 1.0280252+07
> 0025346
> 0064750
> 0.098600
> 0.003086
> 3280877
> 2913891
> Pred
> Pred
> Pred
> Pred
> Pred
> Pred


以及相对误差


> [!NOTE] [图片 OCR 识别内容]
> pnl
> drawdown
> tUIOVeT
> TeturI
> margin
> sharpe
> fess
> Tegion_delay
> US4-0
> 0.148600
> 0.001053
> 0.045244
> 0.039083
> 0.011904
> 0.060292
> 0062931
> US4-1
> 0.129236
> 0.163244
> 0.023646
> 0.048141
> 0.078961
> 0.227937
> 0.242066
> M侃R-1
> 0.042087
> 0.063577
> 0.012277
> 0.001604
> 0.006658
> 0.057502
> 0053428
> ASIT
> 0.060949
> 0.065733
> 0.049611
> 0.014162
> 0.096529
> 0.006448
> 0040400
> CHN-1
> 0.022149
> 0.128851
> 0.038242
> 0.022251
> 0.046380
> 0.108684
> 0.074620
> EUR-I
> 0.058946
> 2037507
> 0.017347
> 0.017957
> 0.220341
> 0.298605
> 0,298797
> GLB-1
> 0.024873
> 0.000394
> 0.012591
> 0.024561
> 0.091025
> 0.000883
> 0019684
> HKG-1
> 0.004605
> 0.000086
> 0.000620
> 0.000440
> 0.007929
> 0.000501
> 0.000842
> JPN1
> 0.001285
> 0.002114
> 0.000533
> 0.000338
> 0.002814
> 0.044268
> 0045201
> KOR-I
> 0.004117
> 0.001396
> 0.053542
> 0.035434
> 0.042047
> 0.005652
> 0016532
> TNN1
> 0.006959
> 0.001826
> 0.000772
> 00OOOOO
> 0.013222
> 0.040679
> 0.041483


整体来看除了个别区域以外, 大部分地区都比较符合

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


核心估算函数如下

- pnl是每个pnl的均值
- sharpe和drawdown是基于pnl计算的
- turnover, returns, margin都是近似所有alpha的相应值的均值
- fitness 是基于公式计算的

```
def estimate_performance_func(tmp_data, max_date=None):    local_pnls = pd.json_normalize(tmp_data['pnl']).T    local_pnls.columns = tmp_data['alphaId'].values    local_pnls.index = pd.to_datetime(local_pnls.index)    local_pnls = local_pnls.sort_index()    local_rets = local_pnls - local_pnls.ffill().shift(1)    local_ret = local_rets.mean(1).dropna()    ret = local_ret    if max_date is not None:        ret = ret[ret.index <= max_date]    ret.dropna(inplace=True)    pnl = ret.cumsum()    metric_pnl = pnl[-1]    metric_sharpe = np.mean(ret) / np.std(ret) * np.sqrt(252)    metric_drawdown = ((pnl.cummax() - pnl) / 10000000).max()    metric_turnover = tmp_data['turnover'].mean()    metric_returns = tmp_data['returns'].mean()    metric_fitness = metric_sharpe * np.sqrt(np.abs(metric_returns) / max(metric_turnover,0.125))    metric_margin = metric_pnl/(local_pnls.apply(lambda col: col.loc[col.last_valid_index()])/pd.Series(tmp_data['margin'].values,index=tmp_data['alphaId'])).mean()    metric = {        'turnover': metric_turnover,        'pnl': metric_pnl,        'sharpe': metric_sharpe,        'returns': metric_returns,        'margin': metric_margin,        'drawdown': metric_drawdown,        'fitness': metric_fitness,    }    return local_pnls, local_ret, metric
```

绘图函数如下

```
from scipy.stats import gaussian_kdefrom mpl_toolkits.axes_grid1.inset_locator import inset_axesdef plot_ret(compare_ret):    xy = np.vstack([compare_ret['local'], compare_ret['cloud']])    z = gaussian_kde(xy)(xy)    sc = plt.scatter(compare_ret['local'], compare_ret['cloud'], c=z, s=10, cmap='viridis')    plt.axline((0, 0), slope=1, color='red', linestyle='--', lw=2)    plt.xlabel('Alpha')    plt.ylabel('PingTai')    plt.xlabel(r'Local Ret', fontproperties=font_prop20)    plt.ylabel(r'Cloud Ret', fontproperties=font_prop20)    # plt.legend(loc='lower right', frameon=False, prop=font_prop20, bbox_to_anchor=(1.05, 0))    plt.legend(loc='upper left', frameon=False, prop=font_prop20, bbox_to_anchor=(0, 1), title=f'{region}-D{delay}\nNum={local_pnls.shape[1]}\n'+rf'$\rho={compare_ret.corr().iloc[0,1]:.2f}$', title_fontproperties=font_prop20)    plt.xticks(fontproperties=font_prop18);    plt.yticks(fontproperties=font_prop18);    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))    plt.gca().xaxis.set_ticks_position('both')  # 在x轴的上下两边都显示刻度    plt.gca().yaxis.set_ticks_position('both')  # 在y轴的左右两边都显示刻度    for spine in plt.gca().spines.values():        spine.set_linewidth(2)    plt.gca().tick_params(direction='in', length=6, width=2)  # length是刻度的长度，width是刻度的宽度    plt.gca().tick_params(direction='in', length=4, width=1.4, which='minor')      # 在主图内部空白处添加水平colorbar    axins = inset_axes(        plt.gca(),        width="50%",   # colorbar宽度        height="5%",   # colorbar高度        loc='lower right',        bbox_to_anchor=(-0.05, 0.15, 1, 1),        bbox_transform=plt.gca().transAxes,        borderpad=0    )    cbar = plt.colorbar(sc, cax=axins, orientation='horizontal')    # 1. 统一刻度样式（与主图保持一致）    cbar.ax.tick_params(        direction='in',  # 刻度向内        length=6,        # 主刻度长度        width=2,         # 主刻度宽度        which='major'    )    cbar.ax.tick_params(        direction='in',        length=4,        # 次刻度长度        width=1.4,       # 次刻度宽度        which='minor'    )    # 2. 去除colorbar所有ticklabel    cbar.ax.set_xticklabels([])    # 3. 在最左和最右分别标记low和high    vmin, vmax = cbar.ax.get_xlim()    cbar.ax.text(vmin, -0.8, 'low', va='center', ha='left', fontproperties=font_prop18, transform=cbar.ax.transData)    cbar.ax.text(vmax, -0.8, 'high', va='center', ha='right', fontproperties=font_prop18, transform=cbar.ax.transData)    # 4. 美化colorbar边框    for spine in cbar.ax.spines.values():        spine.set_linewidth(2)  # 边框线宽与主图一致    # 5. 优化colorbar标签    cbar.set_label(        'Density',        fontproperties=font_prop20,  # 标签字体与坐标轴标题统一        labelpad=10  # 标签与colorbar的间距    )
```

需要一个可以获得performence的alpha_id

```
alpha_id_maps = {    'USA':{0:'K28bJV1', 1:'VRaOVKY'},    'AMR':{1:'l5ROaLn'},    'ASI':{1:'J2pl86W'},    'CHN':{1:'kYoQoxz'},    'EUR':{1:'G7vve1O'},    'GLB':{1:'OzzENXb'},    'HKG':{1:'xjvwmZp'},    'JPN':{1:'PPdpArW'},    'KOR':{1:'K7v9XQz'},    'TWN':{1:'zL8X50X'},}
```

绘图函数如下

```
region_delay = [(region, delay) for region, delays in alpha_id_maps.items() for delay in delays]plt.figure(figsize=(5*2,5*math.ceil(len(region_delay) / 2)))estimate_data = {}for idx, (region, delay) in enumerate(tqdm(region_delay)):    item_estimate_data = {}    tmp_res = wait_get(f'https://api.worldquantbrain.com/users/self/alphas/{alpha_id_maps[region][delay]}/before-and-after-performance').json()    cloud_pnl = tmp_res['pnl']       cloud_pnl = pd.DataFrame(cloud_pnl['records'], columns=[item['name'] for item in cloud_pnl['schema']['properties']])    cloud_pnl.set_index('date', inplace=True)    cloud_pnl = cloud_pnl['beforePnL']    tmp_data = data.query(f'region=="{region}" and delay=={delay} and dateSubmitted >= "{date_beg}"')    local_pnls, local_ret, item_metric = estimate_performance_func(tmp_data, max_date=cloud_pnl.index.max())    cloud_pnl.index = pd.to_datetime(cloud_pnl.index)    cloud_pnl = cloud_pnl.sort_index()    cloud_ret = cloud_pnl - cloud_pnl.ffill().shift(1)    compare_ret = pd.merge(        local_ret.rename("local"),        cloud_ret.rename("cloud"),        left_index=True,        right_index=True    )    compare_ret.sort_index(inplace=True)    compare_ret.dropna(inplace=True)    plt.subplot(math.ceil(len(region_delay) / 2), 2, idx+1)    plot_ret(compare_ret)       item_estimate_data['true'] = tmp_res['stats']['before']    item_estimate_data['pred'] = item_metric    estimate_data[region + '-' + str(delay)] = item_estimate_data        # break   plt.tight_layout()
```

---

## 讨论与评论 (4)

### 评论 #1 (作者: LZ63459, 时间: 10个月前)

thanks, 如果能够根据历史提交的alpha去总结fields特征,是不是可以更进一步了解到数据集的字段有效性

---

### 评论 #2 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

经过别人提醒，正文的误差大概率来源于 PPA和RA在performence里是分开的。

---

### 评论 #3 (作者: 顾问 KZ79256 (Rank 21), 时间: 9个月前)

[LZ63459](/hc/en-us/profiles/30029792452759-LZ63459)

> 如果能够根据历史提交的alpha去总结fields特征,是不是可以更进一步了解到数据集的字段有效性

这是一个庞大的工程，而且可能不具有通用性

---

### 评论 #4 (作者: MM38095, 时间: 3个月前)

厉害了，试试看

---

