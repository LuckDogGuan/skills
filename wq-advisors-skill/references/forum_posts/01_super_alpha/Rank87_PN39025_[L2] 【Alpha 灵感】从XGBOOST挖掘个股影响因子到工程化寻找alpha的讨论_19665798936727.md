# 【Alpha 灵感】从XGBOOST挖掘个股影响因子到工程化寻找alpha的讨论

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha 灵感】从XGBOOST挖掘个股影响因子到工程化寻找alpha的讨论_19665798936727.md
- **作者**: ZC80223
- **发布时间/热度**: 2 years ago, 得票: 8

## 帖子正文

最近有一个设想并做了简单实现，

首先我根据brain里面的时间序列算子，生成个股的特征库，然后用XG boost迭代出前30个具备影响力的因子。XG boost在效率上素来以快著称，不仅让我感觉可以同时运用到大A 5000只上用于取交集。

将这30个潜在因子做排列组合，或许可以形成一个有效的alpha

Step1 选取一些合适的operator（当然我觉得其实可以进一步扩展）


> [!NOTE] [图片 OCR 识别内容]
> from sklearn preprocessine import standardscaler
> import numpy
> import pandas as pd
> 待征工程
> 新:特征转换函数
> GEf MOVINE_aVerage(serIes
> WIIOOW)
> return series rolling(window-Window) .wean()
> def moVing_std(series
> Window):
> TeTRI
> series.rolling(window-window).std()
> def ts
> NeaI
> std_ratio(series
> Window)
> ME
> moVing_average (series
> windor)
> Sto
> moVing_std(series
> UInOOW
> Feturn mean
> std
> def ts_product(series
> Window)
> 替换界或负数值以避免对数计算中的箔误
> series_cIipped
> series.clip(Iower-le-9)
> 标准化数据
> SCaLeI
> Standardscaler()
> scaled_series
> pd.Series(scaler.fit_transform(series_Clipped.Values.reshape(-1
> 1)).flatten(),
> index-series.index )
> 计算标准化数据的滚动窗口乖积
> product
> SCaLed_SeFIEs
> rolling(window-window).apply (np.prod
> FaW-True)
> 对乖积迸行对数转换
> IOg_product
> 叩.IogIp(product )
> 替换任何无穷大或 NaN 值
> Iog_product
> Iog_product.replace([np.inf,
> inf
> np.nan], 0)
> 对滚动窗口乖积的对数迸行还原缩放
> return Scaler:inverse_transform(Iog_product.Values.reshape(-1,
> 1)).flatten()
> def ts_mean(series
> Nindow):
> "过去window天的均值
> return series.rolling(window-window)
> Dean
> def ts_std(series
> Nindow:
> "过去Window天的标准差
> Feturn
> series.rolling(window-Window).std()
> def ts_diff
> mean(series
> WLIUII 
> 'X菽去其过去window天的均值"
> FetUrn SerIes
> ts_mean(series
> windo)
> def
> COkurtosis(series
> series_y, Window):
> "计算过去windowkxy的共棹度"
> deF
> COUII
> tosis (indow_data)
> 嬴保 window_data 是
> '的
> WIndOW_data
> N.aray (WINOOW_data)
> 讧 Window_Jata.ndim
> Windol_data.shape[I]
> Teturn Tpnan
> pd.DataFrame (window_data
> TIUNC
> [series
> name
> Series
> Name])
> tosis_prod
> KUrtosIs() pro)
> return kurtosis_prod
> Combined
> pd.concat ( [series_X renawe(x )
> series
> rename(y)
> axis=I)
> TeTRI
> combined.rolling(window-windo)
> COLUTtOSIS
> FawTrUe)
> def ts
> CODI
> (series
> Series
> WIndow):
> '返回过去window天xy的相
> 采数
> TeTRI
> 5erIe5
> rOlling(window-windo)
> COII
> (series_y)
> def ts
> NeaI
> OVer_std(series
> WInJOW)
> '返回过去window天均值与标准差的比值"+
> TeTRI
> ts_mean(series
> WInOOW)
> ts_std(series, Window)
> def ts_ZsCOre(series
> Window):
> '过去window天gZ分数'
> ME
> ts_mean(series
> Window)
> Sto
> ts_std(series
> WIndOW
> return (series
> mean)
> std
> def ts_range(series
> Window)
> '过去window天的范母
> t大值
> 冕小值)
> return ts_Max(series
> Window)
> ts_min(series, Window)
> def ts_rate_Of_change(series
> Window):
> '过去window天g变化幸"
> return series pct_Change(periods-window)
> def exponential
> moving_average(series
> Nindou):
> '过去window天豹措数稔动平钧
> return Series
> (spanWindow
> adjust-Folse)mean()
> def ts_min(series
> Nindow)
> '过去window天的4小值"
> Feturn
> 5erIe5
> rolling(window-window) min()
> def
> Max(series
> Nindow):
> '过去window天的曩大值"
> Feturn
> 5erIe5
> ToIling(window-window)
> 0
> def ts_diff_from_mean(series
> Window):
> "计算过去wndow天的均值差
> MEaN_SETIes
> Roving_aVerage(series, Window)
> return Series
> Rean_series
> def ts
> NN
> 01
> std(series
> Window)
> "计算过去window天的均值守标准差豹比值"w
> mean_series
> Roving_aVerage(series
> Nindow)
> std_series
> moving_std(series
> windo)
> Feturn mean_series
> std_series
> TTUm
> aply


Step2 此处我只是针对了一只个股

数据集是 ['open', 'high', 'low', 'close', 'avg_price', 'change', 'pct_chg', 'vol', 'amount']，但我觉得这个方法其实不需要关心数据集，只要确定目标即可，比如以avg_price为目标

特征生成是


> [!NOTE] [图片 OCR 识别内容]
> Feturn Jata
> def construct_observed_features(base_features, Window_settings
> pair_features=None):
> 裉据基础待征和窗口设置构遑观测娈鱼列表。
> :param base_features: 初始的待征列表
> :Param WIndOW
> settings: 滚动窗口的设墨
> :param pair_features: 雾要成对时闯序列的特征函数名莉列表。
> :return: 完垄杓观测变豆列表。
> i pair_features is
> NUIC :
> pair_features
> obseryed_features
> base_features. COpy()
> 添加基于滚动窗口的特征
> window in Window_settings:
> feature in base_features:
> OSeRIeJ
> features.extend([
> {feature}_ 
> {window}
> f {feature}_std_{window}
> {feature}
> U
> std_ratio_{indow}
> f {feature}_product_{windoa}
> {feature}_diff_from_mean_{window}
> {feature}_mean_OVer_std
> {indow}
> 对于勇要咸对特征的函数;
> 颧外处垂
> #for pf in pair_features:
> #for featurel i base_features:
> #for featurez i base_features:
> #i featureI
> featurez:
> #observed_features.append(f' {featurel}_{featurez}_{pf}_{window}
> return obseryed_features



> [!NOTE] [图片 OCR 识别内容]
> Window_settings
> 20]
> 例如。伎用这些窗口设逻
> base_features
> Open
> hieh
> Iow
> CIose
> price
> change
> Cng
> VOI
> amount
> 创数据的副本
> Jata
> CLEaII
> data.copy()
> ney_COIUNIs
> problem_Cols
> UITUOUI
> In WIndow
> settings:
> feature in base_features:
> 玑有的特征计身
> moving_aVerage(data_Clean[feature]
> window)
> std_CoI
> Roving_std(data_clean[feature], window)
> mean_std_ratio_CoI
> JeOI
> std_ratio(data_Clean[feature],
> Window)
> product
> aray
> ts_product(data_Clean[feature], windon)
> 转换 NUIPy 数恕为 Pandas Series 并垂命名
> product_CoI
> pd.Series(product_array,
> index-data_Clean.index).rename(f' {feature}_product_{windo}
> *加新的特征计算
> Jiff_from_Dean_COI
> ts_diff_from_mean (data_Clean[feature], window)
> mean_over_std_CoI
> ts_mean_OVer_std(data_Clean[feature], window)
> 将新列添加到列表中
> neW_Columns.extend( [
> COI.rename (F {featurej_ma_{window}
> std_COI.rename(广' {featurej_std_{indow}
> mean_std_ratio_Col.rename(f{feature}
> M1
> std_ratio_{indow}')
> product_CoI,
> diff_froo_mean_COI.rename(f'{feature}_diff_from_wean_{indow}')
> mean_over_std_COI.rename(f' {feature}_mean_OVer_std_{indow}
> 一次性合井斫有莉列
> Jata_CLEan
> Concat ([Jata_clean]
> ney_CoIUmns
> 71517
> 再次清理无效值
> data_Cleanreplace ([np.inf
> 叩;inf] I
> TOI
> inplace=True)
> Jata_CLean dropnatlnplace=TrUe )
> Pct_


Step3

喂入XGboost训练


> [!NOTE] [图片 OCR 识别内容]
> def integrate_xghoost_feature_selection(data,
> obseryed_features
> target_Column;
> top_n_features=30)
> 使用XGBoost祺型选拜录垂雾的特征。
> :param data: 数据集
> (pandas DataFrame
> :param Obseryed_features
> 观测特征列表
> target_column: 目标列名订
>  DGRI
> LOP_
> features: 选译的项部待征数鱼
> :return: 处霪后的数据和选定的特征列表
> 清理无效值
> data
> handle
> invalid_Values (data)
> 分离待征和目标娈鱼
> X y
> data[observed_features] data[target_Column]
> 训药XGBoost襻翌
> Yb_NOUeI
> XGBRegressor()
> print("开始训练 XGBoost 棱型:.
> XEb_model:fit(x
> feature
> Importances
> XEb_model.feature_importances
> print(" 持征垂享性
> feature_importances)
> 选译晨垂要的待征
> top_features_indices
> np.argsort(feature_importances) [-top
> features: ]
> Selected_features
> Columns[top_features_indices]
> print (f"选的前 {to_
> features} 个特征
> selected_features)
> return data
> selected_features.tolist()
> :Daran



> [!NOTE] [图片 OCR 识别内容]
> UHOT=EU] UTWT 士Ht Tala
> CUSEIIEU
> features
> Construct_obseryed_feature
> (base_Teatures
> wndow_settings, pair_features=Mone)
> 硇保无无效值
> 清理无效值
> data_Cleanreplace ([np.inf
> -Iif] 叩
> inplace=True)
> data_CIeandropna(inplace=True)
> 选择数值类型的列进行进一步处理
> numeric_data
> Jata_Clean.select_dtypes (include=[mp.number] )
> nueric_data
> handle_invalid_Values(nuweric_Jata )
> 再次检查是否有无穷大值
> 在训崭XGBoost之前再次裣查
> i np.isinf(numeric_Jata.to_numpy().any()
> numeric_data.isnull()
> ay()
> ay()
> print("warning: Data still contains invalid Values
> else:
> 如果数捂清清;
> 则跹-训练栏型
> 裣查每个特征是否包合无效值
> for Column
> i observed_features:
> 讧 numeric_data[column] isnul()
> isinf(nuweric_data[column]).any():
> print(fnvalid Values found
> {column}
> 如果没有n出
> 麦示所有列都没有无效值
> problem_coIs
> CheCK_COLUMNs
> Xgboost (numeric_data)
> 对于每
> 个有问蟊的列。 辎出其值的计数
> for COI in problem_cols:
> print(f"value Counts for Colum
> {c0]}
> print(find_abnormal
> Jata_in_CoIumn (numeric_data
> COIJ)
> updated_data
> updated_features
> integrate_YEboOst_feature_selection(
> data-numeric_data
> Obseryed_features-observed_features
> target_column= 'aVE_price
> top
> features-38
> nan


得到的结果是一组特征的排列


> [!NOTE] [图片 OCR 识别内容]
> 800000002+08
> 61198212e-06
> 00883883e+88
> 000009002+88
> 646303292-85
> 488156702-85
> 008888232+88
> 150729052-85
> 800000002+08
> 888888808+00
> 544207368-85
> 833772542-85
> 880000002+03
> 588732538-05
> 000333888+88
> 154578502-05
> 474801972-05
> 349682868-05
> 351149338-85
> 331469782-05
> 888000002+80
> 587368788-85
> 759465988-85
> 219947422-05
> 102649822-05
> 874879448-06
> 008000882+80
> 433517262-05
> 835858532-05
> 683788282-05
> 907730278-86
> +146345502-05
> 888000002+00
> 583432928-05
> 856339268-86
> 509700432-05
> 742650032-05
> 649959632-05
> 000333888+88]
> 选择的前  30
> 待征
> Index( [ 'aount_product_20
> CIose_diff_from_mean_Ig
> hieh_mean
> std_ratio_IO
> open_std_28
> Iow_std_18
> Iow_mean_std_ratio_Io
> price_std_2O
> VoI_mean_std_ratio_2O
> Vol_product
> VOI_diff_from_wean_2O
> hieh_diff_from_mean_Z0
> Change
> hieh_std_28
> CIose_mean_std_ratio_Ie
> open_product
> Change_std_18
> Close_ m_I0'
> CIose_std_IO'
> std_20
> hieh_ma_20
> Open
> IOW_ma_S'
> IOw_wa_I8
> Close_product
> hieh
> Iow
> aVB_price_ma_5'
> Close_ma_S'
> CIose
> avg_price']
> dtype= 'object
> LO


有趣的是选了几只股票都有些区别，所以排名前30是波动的。数据资源有限也没全部大A5000只股一起试

不知道有没有前人已经有研究过这部分了，以及是否值得继续挖掘下去。提供个idea，供讨论。

---

## 讨论与评论 (5)

### 评论 #1 (作者: WL13229, 时间: 2 years ago)

这个想法挺新颖的。可以谈谈输入输出，目标函数和损失函数分别是什么吗？BRAIN的返回值并不直接返回close等信息，而是返回PnL.因此很想学习一下这个是怎么结合BRAIN API实现的

---

### 评论 #2 (作者: ZC80223, 时间: 2 years ago)

先来快速回答一下输入输出、目标函数和损失函数：

1、原始输入['open', 'high', 'low', 'close', 'avg_price', 'change', 'pct_chg', 'vol', 'amount'];经过特征工程后，应该派生出172个子特征，作为模型输入；

2、输出是：子特征相较于avg_price的重要性，本质就是对特征排序

3、因为是回归问题，我用了XGboost系统默认的目标函数和损失函数，针对avg_price求MSE，目标函数和损失函数一致。

关于如何结合BRAIN API实现，我目前有一个设想，但比较长，我晚点单独在写个comments

当前面临的困难是

1、首先这得从个股数据入手，当前brain的数据是封装后的，特征工程其实需要封装前的。因此暂时用了外部数据；

2、目前没有开放operator的api，我是手撸了部分简单的operator。

3、XGboost的个股特征筛选效率虽然高，但后续实验需要大量的个股数据，个体难以形成可用与否的判断，需要集体智慧。

一个明确可实操的点：

筛出来后的特征其实是一定可以通过brain平台的operator实现的，因为特征工程的函数是brain上现有的，原始数据是brain上已经封装后的。

比如针对一只个股筛出来的影响因子，排名第一和排名第二的关于PNL均具有很强的负相关性


> [!NOTE] [图片 OCR 识别内容]
> Settings
> CHN/DI/TOP3000
> amount
> VWap
> VoIume
> N Chart
> Pnl
> alphal
> aV_diff(amount, 5);
> alpha2
> product (volume, 5);
> 00
> alpha2
> DOOK
> 1OM
> 15M
> ZOM
> 1111712017
> PnL: -22.01N1
> -25N
> 301
> Clonethis Alphain a newtab
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021



> [!NOTE] [图片 OCR 识别内容]
> Simulation 1A
> Simulation 18
> Settings
> CHN/D1/TOP3000
> amount
> Vwap*volume
> N Chart
> Pnl
> alphal
> aV_diff(amount, 5);
> alpha2
> product (volume, 5);
> 00
> 04/28/2011
> alphal
> WAIS PnL -72.521
> 5,0OOK
> 1OM
> ~15M
> Z0M
> 25M
> 30M
> 35M
> Clonethis Alphain a newtab
> 2012
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021


---

### 评论 #3 (作者: WL13229, 时间: 2 years ago)

感谢您详尽的回答。有几个需要深入思考和讨论的点。

1.因为平台里有neutralization和decay等操作，目前的负PNL或许不能直接支持“排名第一和排名第二的关于PNL均具有很强的负相关性”这一论点。

2. 如何把PNL变正，是个值得思考的课题。

关于operator和数据层面更加的开放，也是我们平台在努力的方向，相信在不久的未来，可以给到大家更多的自由度。

另外值得注意的是，在用机器学习做类似预测的时候，小心未来数据的引用。否则你很容易看到比较高的准确率，但其实是因为有了未来函数。

---

### 评论 #4 (作者: ZC80223, 时间: 2 years ago)

# **算法设计**

#### 一、 **背景**

通过XGboost对于个股的因子挖掘，按照每一个细分行业做分类，形成一个基于每个行业的因子排序列表。再比较不同行业的排序，根据分类，找到市场级别出现次数最多的因子集合。最终根据这些因子的排列组合及运算，找到合适的交易信号。

#### 二、 **问题定义**

**个股**

**输入：** 原始输入['open', 'high', 'low', 'close', 'avg_price', 'change', 'pct_chg', 'vol', 'amount'];经过特征工程后，应该派生出172个子特征

**输出：** 子特征相较于avg_price的重要性，本质就是对特征排序。一个特征列表+相关性

**行业**

**输入：** 行业id，个股-（特征列表+相关性）

**输出：** 行业（特征列表+相关性）

**市场：**

**输入** ：行业id，行业（特征列表+相关性）

**输出：** 全市场的alpha

**Alpha生成及brain平台交互**

#### 三、 **整体架构**

**
> [!NOTE] [图片 OCR 识别内容]
> 行业分-
> `征工
> boost排i
> 行业排序
> 韦tA1
> alplg生成及回珂
> JOAh
> 0lp13扌}
> 个f
> 个盟孑持正
> ~BJElist
> TTLSLll
> alpha回岗
> 4了特正
> 个股=工
> 市场扫Tlist
> alpae交
> 个殿痔正
> 行业痔正
> 个
> 个u孑持正
**

#### 四、 **设计思路**

- 原始数据的依赖解除，本设计的输入输出并不局限于特定的数据集，理论上是基础特征到派生特征的生成的方法+对派生特征相关性的评价方法
- 在数据处理部分，高度需要原始数据，原因是特征处理是基于时间序列的原始数据，如果是封装后的，缺乏挖掘基础
- 重要性排序部分，先采用XGboost排序，在行业排序中采用枚举所有行业内个股的前30个特征的出现次数作为统计分，暂时不引入基于市值或任一变量的加权统计
- 市场排序同行业排序类似，暂时不引入基于市值或任一变量的加权统计
- 和brain的交互：假定挖掘出来的特征都和avgprice具有强相关，首先对确认并使用正相关因子，对于负相关因子暂时没有新的想法。

#### 五、 **Q&A**

- 选择avg_price作为观测变量是否是不合适的，目前我已经发现了因为avg_price天然会和'open', 'high', 'low', 'close'的关系更紧密些，所以大概率这几个特征占比会很大
- XGboost挖掘出来的因子其实存在正相关性和负相关性，如何进一步对其标记
- XGboost 目前目标函数和损失函数都是MSE，这块是否是合适的，如何去判断其合适
- 如何评价XGboost的模型训练性能，这块的测试集和测试方案应该怎么构建。

#### 六、 **工程设计**

暂无

整体这个设计的实现工作量是很大的，会有很多欠考虑的地方以及大量的具体的问题，需要大家一起研究探讨。希望众人拾薪柴火高！！

---

### 评论 #5 (作者: WL13229, 时间: 2 years ago)

"

- 和brain的交互：假定挖掘出来的特征都和avgprice具有强相关，首先对确认并使用正相关因子，对于负相关因子暂时没有新的想法。"

这句话可能是亟待讨论的，BRAIN上输入的Alpha表达式，会经过neutralization等操作，输出的是股票的权重。这里并非正相关或者负相关可以简单概括。具备负return的Alpha也不一定就是负相关。关于相关性的衡量，是需要进一步定义的。

---

