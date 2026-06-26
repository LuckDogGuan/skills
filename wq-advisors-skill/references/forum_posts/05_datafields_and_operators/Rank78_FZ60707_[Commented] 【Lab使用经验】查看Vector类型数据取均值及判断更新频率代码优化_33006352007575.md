# 【Lab使用经验】查看Vector类型数据：取均值及判断更新频率代码优化

- **链接**: https://support.worldquantbrain.com[Commented] 【Lab使用经验】查看Vector类型数据取均值及判断更新频率代码优化_33006352007575.md
- **作者**: LL87164
- **发布时间/热度**: 0年前, 得票: 10

## 帖子正文

**Vector** 类型数据字段在Lab里显示如下： 
> [!NOTE] [图片 OCR 识别内容]
> 『42]
> EPSr
> T2la
> Drain
> Jata
> fie141 { IaJ144
> 2
> SP3r
> T31Ue!
> fela_a
> brain. Jet_data_Irame [ePSI_Held
> datee二 [ (〉"
> 2021-01-01U ] )
> Hela_r
> 『42]
> 1000050308
> En0000000000050428
> En000000000005056O
> En000000000005094B
> EQ0000000000055155
> EQ0000000000055851
> EQDT5
> [12.7198,12.7
> [0.06296,0.05296,
> Ilone
> 13.2782,13.3,15.9,
> Mone
> Mlone
> Mone
> 0.09434,0.09434]
> 15.9,13.
> [12.7198,12.7
> [0.05296,0.05296,
> Mone
> 13.2782.13.3,15.9
> Mone
> Mlone
> Mone
> 0.09434,0.09434]
> 15.9,13.
> [12.7198,12.7
> [0.05296,0.05296,
> Mone
> 13.2782,13.3,15.9,
> Mone
> Mlone
> Mone
> 0.09434,0.09434]
> 15.9,13.
> [15.9,15.9,13.58
> [0.06296,0.05296,
> Mone
> Mone
> Mlone
> Mone
> 13.58]
> 0.09434,0.09434]
> [15.9,15.9,13.58
> [.05296,0.05296,
> Icne
> Mone
> Mlone
> Mone
> 13.58]
> 0.09434,0.09434]
> get


取一个样本判断其类型： **numpy.ndarray**


> [!NOTE] [图片 OCR 识别内容]
> EPSI_Iield
> brain .yet_Jata
> f214
> "anl44_2_ePSI_ialue
> Hela_e
> brain.Jet_Clata_ILale (SPSI_Iieldl;
> datee二 [ {]〉"
> "2021-01-01) ] )
> SaIPIE_
> 2211=f219
> J. LoC [
> 2021-01-0
> 卫60000004000047099
> Print {5TTPe :
> ICTPe !2aPIE_
> C21111
> IzPE
> 21435
> RUIP} .ndarzay


判断类型是为了下一步取均值的操作

采用类似平台的Vector操作符来取 **均值** ：


> [!NOTE] [图片 OCR 识别内容]
> [5]
> mean_df
> field_df.map (
> lambda
> aTr:
> np
> nanmean(arr)
> i isinstance(arr;
> np.ndarray)
> and
> arr.5iZe
> else np.nan
> mean
> df.head()
> [5]
> EQ0086122700001000
> EQ0010001900001000
> EQ0096897500001000
> EQ0031307000001000
> EQ0018787700001000
> EQ0000000000165488
> EQ0018663100001000
> EQ0010103500001000
> EQ001001000OC
> 2021-
> 01
> NaN
> NaN
> NaN
> NaN
> NaN
> NaN
> 1.744500
> NaN
> 04
> 2021-
> 01
> NaN
> NaN
> NaN
> NaN
> NaN
> NaN
> NaN
> NaN
> 05
> 2021
> 01
> NaN
> NaN
> NaN
> NaN
> -1.09
> NaN
> NaN
> NaN
> 06
> 2021
> 01
> NaN
> NaN
> NaN
> NaN
> -1.09
> NaN
> 1.744500
> NaN
> 07
> 2021-
> 01-
> NaN
> NaN
> NaN
> NaN
> NaN
> NaN
> 2.010055
> NaN
> 08
> 5rows ^ 23380 columns


注：应该使用  **np.nanmean**  函数来对 Vector 字段取均值，避免列表中有一个 NaN 时返回值是 NaN。

更新频率图示及代码参见另一个帖子里的评论： [[L2] Data Idea系列1Research Sentiment Data_Sentiment1Alpha Template_33247252289943.md/comments/33263818275607]([L2] Data Idea系列1Research Sentiment Data_Sentiment1Alpha Template_33247252289943.md/comments/33263818275607)

备注：

1. 图中使用的字段  `anl44_2_epsr_value`  代表 "reported earnings per share"（报告每股收益）。

---

## 讨论与评论 (5)

### 评论 #1 (作者: YQ51506, 时间: 1年前)

因为 vector字段元素这里是个列表，因此我是以这个列表为基础，取出其最大值，最小值，均值等，进行处理，构建为matrix的dataframe格式，实现了vector_operator的效果，不知道准不准确

---

### 评论 #2 (作者: LL87164, 时间: 0年前)

[YQ51506](/hc/en-us/profiles/27706511330455-YQ51506)

**Vector** 数据字段是数组： **numpy.ndarray。** 用python函数 np.nanmean(arr) 取均值，避免列表中有一个 NaN 时返回值是 NaN。

---

### 评论 #3 (作者: 顾问 FZ60707 (Rank 78), 时间: 1年前)

感谢大佬分享，正愁着vector数据看不了呢，一直报错

---

### 评论 #4 (作者: YW93864, 时间: 1年前)

我记得可以使用dataframe的.map操作，比如取均值df.map(np.nanmean)

=======================================================================================================================================================================

---

### 评论 #5 (作者: LL87164, 时间: 0年前)

[YW93864](/hc/en-us/profiles/14096946892439-YW93864)

不好意思，没及时回复。多谢提醒！您说的对，应该是用这个 np.nanmean。也是最近才发现： Vector 字段的列表里如果有一个是 NaN，用标准函数的话返回的也是 NaN。已更新正文中截屏内容。

补充两组函数的对比：

标准函数
功能
nan-Safe 版本

np.max()
最大值
np.nanmax()

np.min()
最小值
np.nanmin()

np.quantile()
分位数
np.nanquantile()

np.percentile()
百分位数
np.nanpercentile()

np.sum()
求和
np.nansum()

np.std()
标准差
np.nanstd()

---

