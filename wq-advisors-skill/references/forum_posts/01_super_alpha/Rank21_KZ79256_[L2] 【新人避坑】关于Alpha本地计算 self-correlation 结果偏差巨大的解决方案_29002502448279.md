# 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案

- **链接**: https://support.worldquantbrain.com[L2] 【新人避坑】关于Alpha本地计算 self-correlation 结果偏差巨大的解决方案_29002502448279.md
- **作者**: 顾问 WX84677 (Rank 69)
- **发布时间/热度**: 1 year ago, 得票: 14

## 帖子正文

首先感谢 XZ23611 分享的帖子：
“ [【提升Check Submission效率】一些可以提升Check Submission的Tips，效率提高10倍以上]([L2] 【提升Check Submission效率】本地计算自相关和提高check的tips效率提高10倍以上代码优化_28524742174359.md?page=1#community_comment_28755853659031) ”其中分享的代码非常实用。一般情况下，使用这套代码本地计算self-correlation值与Brain 平台计算的结果值，一般只会有 0.02~0.05 的差异，对于实战完全够用。

但有个场景下，计算结果与平台结果天差地别：

看以下案例：


> [!NOTE] [图片 OCR 识别内容]
> ids
> ['alphal
> alphaz' ]
> Checkable_ids
> check_remove_self_correlation(5,
> example_ids,
> Os_ret_df)
> example


Alpha_id1 的pnl曲线：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 3JCJ
> 7JCJ
> TU


Alpha_id2 的pnl曲线：


> [!NOTE] [图片 OCR 识别内容]
> N Chart
> 4,00J
> 1[


关键点就是alpha 的pnl **数据日期不一致，** 且批量获取 pnl 时先获取了数据日期较少的alpha.

这种情况下，get_pnl_panel( ) 函数中，对多个alpha的pnl_df 进行合并时，由于行数不一致，合并后的 pnl_df 会出现 Date 索引乱序。

而后续计算自相关性时，pnl 数据的时序性是非常关键的，如果非时序结果自然完全不同。


> [!NOTE] [图片 OCR 识别内容]
> 转Ipnl
> 主契用干处理super alphat含有ris
> NPRNe
> HJpnl
> 转 Hdatatrae
> pnl panel(session
> alpha Iist)
> 40NA
> pr5
> fetch_pnls (session,
> Jlpha_list)
> pd, DataFral()
> alpha
> LOUN
> (alpha_pnls)
> 检苴p1对桌是杏有j50n方达
> 如臾夯。则涸用该方法获耶数晷
> hasattr(pnl
> J5OI
> collable(pnl.Json)
> Nat?
> json()
> 8158.
> 惧设p1己经昱宁典桕式
> Ta
> 尬 records的列战
> 1 len(data [
> records' ][]
> PdUatatrane(datal
> 「PCOFO
> COLUII
> Uale
> alpha_Id]
> df.set
> Tne
> inplace
> True)
> Plif len(data
> TeCORO
> proertins
> Hta[ 'schema
> J[ properties
> 处果合有' risk-neutralized-pol
> 0罔}
> 井{除且怕彘6列
> ay(prop
> Ial
> 「isk-neutralized-Pnl
> OPO[
> DTOIerTIes:
> TLOTUS
> [record[:7] for pecord
> in data[ records
> DtFTmPCOPO
> TILIIII
> Date
> alpha_id])
> ut.set
> Ide( Uate
> Inplace-True
> 01
> tererordslg列」9
> @不包含' risk pevtralized pnl
> NHi这 Talpha
> COTILLTIUL
> 捋~芦alpha jdgyoatafrae SgAoataframe台并
> pnl_df. empty
> merge df 后
> 作为 index 的 Dale 会乱序
> 8
> pl_Tf
> p.merBe(pnl_#f,
> Dte '
> T
> MUt
> PTI[
> pnl_df
> Rot
> Dnl
> 0]
> Onl
> Dl
> 0302
> Dl


pnl_df 只包含 alpha1 时，print(pnl_df.index):


> [!NOTE] [图片 OCR 识别内容]
> Index( ['2012-07-16'
> 2012-07-17' '
> 2012-07-18
> 2012-07-19
> 2012-07-20
> 2012-07-23
> 2012-07-24
> 2012-07-25
> 2012-07-26
> 2012-07-27
> 2022-07-01 `
> 2022-07-05
> 2022-07-06
> 2022-07-07
> 2022-07-08
> 2022-07-11
> 2022-07-12'
> 2022-07-13
> 2022-07-14
> 2022-07-15
> dtype
> object
> TAINI
> Date
> LenBth-2495 )


pnl_df 合并 alpha2 后，print(pnl_df.index):


> [!NOTE] [图片 OCR 识别内容]
> Index( [ '2012
> 07-16'
> 2012-07-17 ,
> 2012-07-18'
> 2012-07-19
> 2012-07-20
> 2012-07-23
> 2012-07-24
> 2012-07-25
> 2012-07-26
> 2012-07-27
> 2021-07-05'
> 2021-09
> 2021-11-25
> 2021-12-24'
> 2022-01-17
> 2022-02-21
> 2822-04-15
> 2022
> 05-30
> 2022-06-20
> 2022-07-04' ]
> dtype= 'object
> name=
> Date
> length=2588 )


解决方案：

修改get_pnl_panel() 函数即可：


> [!NOTE] [图片 OCR 识别内容]
> Jet get_pr_panel(sesslon,
> alpha_Iist):
> pnl
> alpha id in tqdm(alpha DnIs)
> 检芦pnl对t是否有jso方法
> 如卑有
> 则调用该方法荻取数据
> i hasattr(pnl
> Json
> Callable(pnl .Json ) :
> Jata
> json()
> 0u ;
> n设p1己经足字典概式
> Jata
> 检苴records的列数
> i len(data[ 'records ' ][0])
> pd.DataFrame (datal 'records'
> OILIIIIIC
> Date
> alpha _id1)
> df, set_inde( 'Date
> iplace=True)
> elif len(data[ records '][0])
> properties
> Jata 
> SChela
> 1[ 'properties
> 如果含有 'risk nevtralized DnI
> 则保留这
> 井掰除其他颗外伪列
> i any(prop [ name
> Tisk-neutralized
> tor prop in properties)
> TOMTO'
> [record[:2] for record
> in Jata
> FeCurus
> pd.DataFrame(records
> COLUIIIS
> Date
> alpha_id])
> df. set_index( 'Date
> inplace=True)
> 675e +
> 如果records{9}列数为3
> 但下包含'risk neutralized pnl
> 则跳过这 Falpha id
> Continwe
> 将当Halpha_idfDataFraaeSRIDataFrame合井
> pnLdf,empty:
> pnl_df
> C」Se ;
> Dd
> pd.NerRe(pnl df
> Date
> TO
> outer
> pnl_df
> pnl_df. sort_indexgJ
> peturn pnl df
> FO
> Onl
> Oml
> pnl


希望遇到相同场景的伙伴，能节省调试时间，少走弯路。

最后祝愿所有顾问伙伴，2025年都能收获满满~

---

## 讨论与评论 (1)

### 评论 #1 (作者: HQ17963, 时间: 1 year ago)

感谢分享！

注意到截图中Date列的类型为object，即str储存的，可以转换为datetime64类型，再merge就没问题了。

附转换代码：

> pnl_df=pnl_df.assign(Date=lambda x:pd.to_datetime(x.Date,format='%Y-%m-%d')).set_index('Date')

改：我是用concat实现合并的，不知道是否影响

> final_df = pd.concat(pnl_dfs, axis=1)

---

