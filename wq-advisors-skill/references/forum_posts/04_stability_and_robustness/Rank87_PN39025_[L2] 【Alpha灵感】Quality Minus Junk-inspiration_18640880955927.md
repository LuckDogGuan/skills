# 【Alpha灵感】Quality Minus Junk-inspiration

- **链接**: https://support.worldquantbrain.com[L2] 【Alpha灵感】Quality Minus Junk-inspiration_18640880955927.md
- **作者**: BC52452
- **发布时间/热度**: 2 years ago, 得票: 10

## 帖子正文

1. 文章标题及作者：Quality Minus Junk

Asness, C. S., Frazzini, A., & Pedersen, L. H. (2019).

Review of Accounting Studies, 24(1),

DOI：10.1007/s11142-018-9470-2

2. 投资者倾向于为“质量”更高的股票支付更高的购买价，该文章从quality角度出发，用profitability, growth, safety三方面来描述股票的质量

3. 相关数据集：mdf_gpr,assets, mdf_rec, mdf_rac, mdf_coa, mdf_grm, systematic_risk_last_30_days, star_sr_leverage, mdf_roe, oth434_model_ohlson_oscore

4.策略PnL 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 4,0OOK
> 3,50OK
> 3,00OK
> 2,5OOK
> MNw
> 2,0OOK
> 1,5OOK
> 1,00OK
> 500
> Jan '12
> Jan '13
> Jan '14
> Jan '15
> Jan '16
> Jan '17
> Jan '18
> Jan '19
> Jan '20
> Jan '21


5. 改进思路：对quality指标使用不同的数据集进行描述，在不同的国家与不同的中性化条件下也许能取得更好的表现

6. alpha表达式：

pfb=zscore(zscore(mdf_gpr/assets)+zscore(mdf_rec)+zscore(mdf_rac)+zscore(mdf_coa/assets)+zscore(mdf_grm));

t=20;

grow=zscore(zscore(ts_delta(mdf_gpr/assets,t)/ts_delay(mdf_gpr/assets,t))+zscore(ts_delta(mdf_rec,t)/ts_delay(mdf_rec,t))+zscore(ts_delta(mdf_coa/assets,t)/ts_delay(mdf_coa/assets,t))+zscore(ts_delta(mdf_grm,t)/ts_delay(mdf_grm/assets,t)));

safe=zscore(zscore(systematic_risk_last_30_days)+zscore(star_sr_leverage)+zscore(oth434_model_ohlson_oscore)+zscore(ts_std_dev(mdf_roe, t)));

a=zscore(pfb+grow+safe);

a

---

## 讨论与评论 (2)

### 评论 #1 (作者: YT65687, 时间: 2 years ago)


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Stage
> IS 
> O
> Aggregate
> Sharpe Turnover
> Fitness Returns
> Drawdown Margin
> Data
> 1.3512.48960.905.52966.01%8.859600


---

### 评论 #2 (作者: WL13229, 时间: 2 years ago)

这个如果在最后

a=zscore(pfb+grow+safe)

的部分用乘号而非加号，可能有其他的表现

---

