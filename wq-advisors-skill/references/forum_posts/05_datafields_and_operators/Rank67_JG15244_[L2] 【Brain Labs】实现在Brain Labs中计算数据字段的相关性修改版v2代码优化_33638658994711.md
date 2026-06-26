# 【Brain Labs】实现在Brain Labs中计算数据字段的相关性(修改版v2)代码优化

- **链接**: https://support.worldquantbrain.com[L2] 【Brain Labs】实现在Brain Labs中计算数据字段的相关性修改版v2代码优化_33638658994711.md
- **作者**: FS29418
- **发布时间/热度**: 11个月前, 得票: 8

## 帖子正文

通过在Brain Labs中计算数据字段之间的相关性，可找到与我们已经提交过的数据字段类似的数据字段，进行替换来找到新的Alpha。

以下是实现在Brain Labs中计算字段相似性的代码，希望对大佬们有所帮助。

```
from brain import Brainfrom brain.errors import UnexpectedStatusfrom typing import Optionalimport numpy as npimport pandas as pdimport timeimport osdef calc_mean_corr(df1, df2) -> float:    timeS = time.time()    # 行对齐和列对齐（按 index 和 columns）    df1, df2 = df1.align(df2, join='inner', axis=0)    df1, df2 = df1.align(df2, join='inner', axis=1)    corrs = []    for col in df1.columns:        s1 = df1[col]        s2 = df2[col]        # 对齐非 NaN 的值        valid = s1.notna() & s2.notna()        s1_valid = s1[valid]        s2_valid = s2[valid]        if len(s1_valid) < 2 or s1_valid.std() == 0 or s2_valid.std() == 0:            continue        corr = s1_valid.corr(s2_valid)        if not np.isnan(corr):            corrs.append(corr)    print(f"calc self corr cost {time.time() - timeS} seconds")    if corrs:        return float(np.mean(corrs))    else:        return np.nandef save_df(region: str, delay: int, universe: str, data_field: str, df: pd.DataFrame):    dir_path = os.path.abspath('.')    file_path = os.path.join(dir_path, "dataframe", region, str(delay), universe, f"{data_field}.csv")    os.makedirs(os.path.dirname(file_path), exist_ok=True)    df.to_csv(file_path)    print(f"saved to {file_path}")def get_df(region: str, delay: int, universe: str, data_field: str) -> Optional[pd.DataFrame]:    dir_path = os.path.abspath('.')    file_path = os.path.join(dir_path, "dataframe", region, str(delay), universe, f"{data_field}.csv")    if os.path.exists(file_path):        return pd.read_csv(file_path, index_col=0, parse_dates=True)    return Nonedef filter_by_dates(df: pd.DataFrame, dates: list):    mask = pd.Series(True, index=df.index)    for op, date_str in dates:        date = pd.to_datetime(date_str)        if op == '>':            mask &= df.index > date        elif op == '>=':            mask &= df.index >= date        elif op == '<':            mask &= df.index < date        elif op == '<=':            mask &= df.index <= date        elif op == '==':            mask &= df.index == date        elif op == '!=':            mask &= df.index != date        else:            raise ValueError(f"Unsupported operator: {op}")    return df[mask]def get_df_if_exist(brain: Brain, data_field, dates: Optional[list] = None):    df = get_df(str(brain.region), brain.delay, str(brain.universe), data_field.id)    if df is not None:        if dates:            return filter_by_dates(df, dates)        return df    while True:        try:            df = brain.get_data_frame(data_field)        except UnexpectedStatus:            continue        except Exception as e:            print(e)            continue        else:            break    save_df(str(brain.region), brain.delay, str(brain.universe), data_field.id, df)    if dates:        return filter_by_dates(df, dates)    return dfdef calc_data_field_mean_corr(brain: Brain, data_field1: str, data_field2: str):    data_field1 = brain.get_data_field(data_field1)    data_field2 = brain.get_data_field(data_field2)    df1 = get_df_if_exist(brain, data_field1)    df2 = get_df_if_exist(brain, data_field2)    return calc_mean_corr(df1, df2)def get_data_field_similar(datafield: str, region: str, delay: int, universe: str, same_data_set: bool = True, dates: Optional[list] = None, target_type: list = ["MATRIX"]):    brain = Brain(region=region, delay=delay, universe=universe)    datafield = brain.get_data_field(datafield)    dataframe = get_df_if_exist(brain, datafield, dates=dates)    now_dataset = datafield.dataset.id    datasets = brain.get_data_sets()    datasets = datasets.results    datasetsId = [dataset.id for dataset in datasets]    if same_data_set:        datasetsId = [now_dataset]    dataCorr = []    for dataset in datasetsId:        datafields = brain.get_data_fields(data_set=dataset)        datafieldsId = [datafield.id for datafield in datafields.results if datafield.type in target_type]        for datafield in datafieldsId:            datafield = brain.get_data_field(datafield)            dataframeN = get_df_if_exist(brain, datafield, dates=dates)            selfcorr = calc_mean_corr(dataframe, dataframeN)            dataCorr.append({                'id': datafield,                'sc': selfcorr,            })    return pd.DataFrame(dataCorr).sort_values(by='sc', ascending=False)
```

使用方法如下:

```
# 计算与给定字段相同数据集的使用数据字段的相似度scs = get_data_field_similar('anll1_2_2pme', 'USA', 1, 'T0P3000', same_data_set=True)print(scs)# 计算两个字段之间的相似度brain=Brain(region='USA', delay=1, universe='T0P3000')print(calc_data_field_mean_corr(brain,'anl11_2_1pme', 'anl11_2_2pme'))
```

由于计算时发现不设置时间范围计算全量数据一次需要接近30s, 设置为大于2021年的数据后，时间为13秒左右，可以根据需要自行修改，默认只计算同数据集字段，same_data_set设置为False，将计算当前region-delay-universe的所有数据字段与给的数据字段的相似度。

相似度计算函数使用DataFrame自带的corr函数，可以根据需要自行修改calc_mean_corr函数来满足自己的要求。

使用代码时可以单独开启一个jupyter文件然后运行，实测就算关掉Brain Labs界面计算还会继续，也就是可以在晚上开始计算几个想计算的数据字段相似度，第二天就基本能看到结果了。

以下为计算结果:

由于计算时间太长，所有只选取了当前数据集的10个数据字段。可以发现使用全量数据计算anl11_2_1pme与anl11_2_pme的相似度为0.57，而大于2021年数据计算出为0.49还是有一定的误差。


> [!NOTE] [图片 OCR 识别内容]
> SCS
> data
> field_similar("anlll
> 2_2pme
> USA
> 1,
> T0P3000
> print (sCs
> brain
> Brain (region= 'USA
> delay=l;
> universe=' T0P3000
> print (calc_data_field_mean_corr(brain;
> anlll
> 2_Ipme
> anll1
> 2_Zpme' ) )
> anlll
> 2_Zpme
> analystll
> Calc
> Self
> COTI
> COSt
> 12.6117556095123295
> Calc Self
> COrr
> COSt
> 12.6700372695922855
> calc self
> COTF
> COst
> 12.815838336944585
> Calc self
> COTI
> COst
> 12.7351031303405765
> calc self
> COTI
> COSt
> 14.0531449317932135
> Calc Self
> COrr
> COSt
> 14.2117724418640145
> calc self
> COTF
> COst
> 13.9583809375762945
> Calc Self
> COTI
> COst
> 14.2266893386840825
> calc self
> COTI
> COSt
> 14.2195904254913335
> Calc Self
> COTI
> COSt
> 13.9569535255432135
> id
> SC
> anll1
> 2_2pme
> 1.000000
> anlll
> 2_Ipme
> 0.491526
> anlll
> 2 2tic
> 0.463154
> anllI
> 22
> 0.330435
> anlll
> 2_39
> 0.277872
> anlIl
> 2_29
> 0.263194
> anlll 2_19
> 0.187412
> anllI
> 2_3e
> 0.130620
> anlll
> 2 le
> 0.114858
> anlll 2 Itic
> 0.109822
> Calc Self
> COrr
> COSt
> 15.1421022415161135
> 0.5706013982446931
> get


可以发现anl11_2_2pme与anl11_2_pme有0.82的相似度，还是很高了，但是这是我随便选的，没有使用过。


> [!NOTE] [图片 OCR 识别内容]
> 日
> +
> &
> 口
> 凹
> Code
> Notebook C
> Cluster
> Python 3 (ipykernel)
> 11/T0P3000
> A/I/T0P3000/an111
> Company
> name
> CSV
> Name
> Modified
> Calc
> Self
> COTI
> COSt
> 9.3469376564025885
> anl11_2_le.csV
> 9hago
> SaVe
> to
> /mnt/custom-file-systems /efs /fs -0a9c53e05417598fa_fsap-Oeb4elef5d316f1b8 /dataframe /US
> anlll_Z_19.csV
> 9ha90
> A/I/TOP3OOO/anlIlcreptcesgerle .CsV
> Calc Self corr
> COSt
> 10.2125208377838135
> anl11_2_Ipme.csV
> 9hago
> Save
> t0
> /mnt/custom-file-systems /efs /fs - 0a9C53e05417598fa
> Oeb4elef5d316f1b8 /dataframe /US
> 田 anlll_2_IticcsV
> 9ha90
> A/I/TOP3OOO/anlll_creptcesgerlg
> CSV
> calc
> Self Corr
> COSt
> 10.2548635005950935
> anl11_22e.CsV
> 9hago
> Save
> to
> /mnt/custom-file-systems /efs /fs - 0a9C53205417598fa
> Oeb4elef5d316f1b8 /dataframe/US
> anlll_2_2g.CSV
> 9ha90
> A/I/TOP3OOO/anlll_creptcesgerlpme
> CSV
> Calc
> Self
> COTI
> COSt
> 10.6469922065734865
> anlll_22pme csV
> 9hago
> Save
> to
> /mnt/custom-file-systems /efs /fs - 0a9c53205417598fa_fsap-Oeb4elefsd316f1b8 /dataframe /Us
> 田 anlll_2_Ztic CsV
> 9ha90
> A/I/TOP3OOO/anlII_creptcesgerltic .csV
> a0l11_2_3e.CSV
> 9hago
> Calc
> Self
> COTI
> COSt
> 10.2657704353332525
> SaVe
> to /mnt/custom-file-systems /efs /fs- 0a9C53e05417598fa_fsap-Oeb4elefsd316f1b8 /dataframe
> anl11_2_39.CsV
> 9ha90
> A/I/TOP3OOO/anlIlcreptcesgerze .CsV
> anlll_23pme.csV
> 8ha90
> CalC Self corr
> COSt
> 10.3563883304595955
> id
> SC
> 田 anlll_2_3ticcsV
> 8ha90
> anlll_2_2pme
> 1.000000
> anl11_2_e.CsV
> 8ha90
> 15
> anlll
> 2_pme
> 0.827962
> anl11_2_9.CsV
> 10
> anlll 2 3pme
> 0.618368
> anlll 2
> Ipme
> 0.491526
> anlll_2gse.CSV
> 8ha90
> anlIl 2 2tic
> 0.463154
> 田 anlll_2_pme.csv
> 8ha90
> anlll
> 2_95e
> 0.439470
> anlll_2_region.csv
> 8ha90
> :
> anlll
> 22e
> 0 .330435
> anlll_2_tic
> 0.302962
> anlll_2_ticcsV
> 8ha90
> anlll
> 0.294157
> anlll_cit_totalcor。
> 8hag0
> anlll 2_39
> 0.277872
> 47
> anlll_Creptcesgerlpme
> 0.274874
> anlll_cit_totalcor。。
> anlll 2_29
> 0.263194
> 0 )10155
> fsap-
> fsap-
> /US
> Sha9o
> Sha9o


修正:

根据weijie老师建议增加了数据的缓存，只保留了MATRIX数据，可以根据需要修改。

经过测试修改为缓存数据后，数据的计算时间变成了2s，不知道是不是因为晚上的时候服务器快一点，所以直接将dates默认参数改为None，可以根据需要修改。

改进建议:

1. 获取的数据字段一次的最大数目为10000，不知道是否存在超过10000个数据字段的数据集，如果存在可能返回的数据字段不全。

2. 获取数据字段时可以根据用户alpha数目或者用户数排序，或者根据covrage过滤等，以获得更优的数据字段。

3. 可以保存已经计算过的相似度到一个文件中，避免重复计算。

---

## 讨论与评论 (8)

### 评论 #1 (作者: WL13229, 时间: 11个月前)

[FS29418](/hc/en-us/profiles/28884318315799-FS29418)

挺好挺好，差不多了。

1. 建议增加将df保存至你文件夹的操作，这样就不用每次请求网站去下载文件。同时做好命名。

2.另外，找相似的数据字段，建议都去model data找找。可以减少你使用到意义不明的model data的情况。

3. 请补充代码，让它跳过vector数据，因为目前可以暂时不用探索vector数据，后续再让其他同学补充。

请进行进一步尝试。

最后当你找到一个高相关的时候，请回测试试看。

---

### 评论 #2 (作者: WL13229, 时间: 11个月前)

这个改进很明显。

再加一两个实例，看看有没有帮助到你找到新的alpha. 不一定需要在同数据集搜索，也可以去model data搜

[FS29418](/hc/en-us/profiles/28884318315799-FS29418)

---

### 评论 #3 (作者: LL87164, 时间: 11个月前)

提醒：for循环中的 print 会造成 I/O 频繁超限的问题，建议注释掉。另外，是否可以考虑增加一个输出：有效数据点。结合字段更新频率，统一分析。

def calc_mean_corr(df1, df2) -> tuple:

---

### 评论 #4 (作者: LH50827, 时间: 11个月前)

from brain import Brain

from brain.errors import UnexpectedStatus   这两个引用没哦，麻烦分享一下。

---

### 评论 #5 (作者: FS29418, 时间: 11个月前)

LL87164

感谢提醒，print输出是当时测试用的，没有注释掉，有效数据点数量和其他相关信息可以根据需要添加，感谢补充

---

### 评论 #6 (作者: FS29418, 时间: 11个月前)

LH50827

brain库是lab中自带的，好像目前没有提供对应的库的定义，需要自行在lab中探索函数的使用。

---

### 评论 #7 (作者: FS29418, 时间: 11个月前)

WL13229

好的weijie老师明白了，目前还在继续探索

---

### 评论 #8 (作者: CW99271, 时间: 10个月前)

我已经连续好几天打不开lab网页555

---

