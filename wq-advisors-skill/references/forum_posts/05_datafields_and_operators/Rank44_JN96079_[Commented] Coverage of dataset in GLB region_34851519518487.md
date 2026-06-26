# Coverage of dataset in GLB region

- **链接**: https://support.worldquantbrain.com[Commented] Coverage of dataset in GLB region_34851519518487.md
- **作者**: LR13671
- **发布时间/热度**: 9个月前, 得票: 18

## 帖子正文

I noticed that the dataset description says  **86% coverage**  for the field  `mdl26_peg_smartestimate_fy1` , but when I calculated the NaN percentage, it was  **76%** . This leaves only  **24% non-null values** . So, what does "86% coverage" actually mean?

---

## 讨论与评论 (10)

### 评论 #1 (作者: 顾问 JN96079 (Rank 44), 时间: 9个月前)

How are you able to determine the number/percentage of NaNs in a data field?

However, I saw somewhere in the community that a data field can work better with NaNs than with zero values, and that is why some operators like to_nan exclusively aid in enhancing a data field's smoothness by converting zeros to NaNs. So, the NaNs could be in the whole 86% coverage in your case above.

Also, those who have a better idea from the platform can share more insights, and if I'm wrong, please don't hesitate to correct me.

Thanks, all!

---

### 评论 #2 (作者: TP85668, 时间: 9个月前)

Great observation! The difference comes from how “coverage” is defined. In many datasets, “coverage” usually refers to the proportion of instruments or tickers that  *have at least some values reported*  for the field over a given period, not the proportion of non-missing values at each timestamp. That’s why you may see 86% coverage overall, but when you check missing values at the daily level, the usable data can be much lower (e.g., 24%). In short, coverage ≠ completeness at every point in time, but rather availability across the universe.

---

### 评论 #3 (作者: DS54387, 时间: 9个月前)

If you have 100 stocks over 100 days, but only 86 days have at least one stock with a non-NULL value, the coverage is 86%. However, within those 86 days, many stocks could still be NULL (leading to your observed 76% NaN)

---

### 评论 #4 (作者: RC80429, 时间: 9个月前)

Whatever i understand is that it’s more about how broadly the field exists across the universe over time, not how many daily entries are non-NaN. So your 24% non-null daily values don’t contradict the 86% coverage—it just means the field is available for most instruments at some point, but sparsely populated day-to-day. This nuance is good to keep in mind when choosing fields for alpha design.

---

### 评论 #5 (作者: AG14039, 时间: 9个月前)

Here’s a clear explanation: if you track 100 stocks over 100 days, and only 86 of those days have at least one stock with a non-NULL value, your  **coverage**  is 86%. However, even on those 86 days, individual stocks may still have NULL values. This means that when you count all stock-day entries, the proportion of missing values could be much higher—explaining why you observe 76% NaNs across the dataset.

---

### 评论 #6 (作者: AG14039, 时间: 9个月前)

Exactly! Coverage measures breadth across instruments over time, not density of daily values. So even if only 24% of daily entries are non-NULL, an 86% coverage means most instruments have at least some data over the period. This distinction is important in alpha design—fields with high coverage but sparse daily data can still be valuable if leveraged correctly with smoothing, decay, or cross-sectional operations.

---

### 评论 #7 (作者: RP41479, 时间: 9个月前)

If you track 100 stocks for 100 days and 86 days have at least one non-NULL value, coverage is 86%. But individual stock-days can still be NULL, leading to a higher overall missing rate, like 76% NaNs.

---

### 评论 #8 (作者: HT71201, 时间: 9个月前)

Coverage is defined at the ticker level, not per timestamp. For example, if 86% of days have at least one non-NULL value across 100 stocks, coverage is 86%. But many stock-days may still be missing, so the actual usable data can be much lower—like 76% NaNs.

---

### 评论 #9 (作者: AF65023, 时间: 8个月前)

Coverage is defined at the ticker level, not per timestamp. For example, 86% coverage means 86% of days have at least one non-NULL across 100 stocks—but many stock-days may still be missing, so actual usable data could be much lower (e.g., 76% NaNs).

---

### 评论 #10 (作者: JC84638, 时间: 8个月前)

Thanks to DS5438 for the concise remark. This post highlights how serious the plagiarism issue has become: AG14039, RP41479, HT71201, and AF65023 copied and re-output DS54387’s comment using tools. We might also want to check which countries these users belong to. (jzc) 
⚠️ [Reminder: Respect original IP on the platform — complete AI re-outputs and plagiarism are not allowed]


> [!NOTE] [图片 OCR 识别内容]
> 0554337
> 1903y5330
> IFyoU have 100 stocks over 100 days; bu only 86 days hawe at least one stock with
> Hon-NULL
> Value; the Cowerage Is 8696_
> However。 within those 86 cays; many stocks coulc still be NULL (leacing
> -0 yOUTODserved 763 NaNI
  
> [!NOTE] [图片 OCR 识别内容]
> 4614033
> Hsre's
> Eplanaen:
> track 100 stecks Oer 100
> anyonly 85clthose
> 73'=
> least one stock Mth
> Ton NULL elue; OUTcoyerage
> 86q  Hower, een on theee 86
> Jays
> individual stocks may still have NULLvalues This means that whenyOU
> SOUT
> stoCk Jayentries;
> the Progorin
> ITssingalues Could
> 匕 much
> higher
> explaining tN JOU obsere 763 NaNs
> 32r  Ts 03al
> 44614033
> UCa
> Eactloerage rTieasJrss
> breadthacress instruments Ower time No density ofdaily
> JJE
> 「
> Orly 243oldeilyenriesars non-NJLL
> 869 Coverage reans mest instrurTents have
> leastsome Ja-a Ower the
> period This Clisunc-ion
> important
> aloha Jesgntelcs 'witn hign
> weraee but sparSE
> Jaily daz
> still bs
> II
> lewsraged correztly withsmoothirg
> COSC-SPCtIOs
> OFsrations
> 2341479
> 匕 Uol JgU
> IySU
> LCk 1 St-l
> Jaysard 85 J3,5 haye
> P38107三
> NnNULL 'elue
> TOERaCE
> 85q。
> Butincwiyya
> CTOCL-dac Can 5HII
> NULL,leading
> hgher
> 妹烂7
> rTlssine rats lie 763 Nals
> TTTIZOI
> 5 JJroy
> Cosrage
> detimedat  he IC-Er
> Tl C
> irestarp
> For exarols,i 863
> day haeat lsast
> nrNUL_alus
> 320r
> 1305.OCrs
> CCIETAC
> 850.2Utrany stezk-Jays
> stillDE tissing
> sothe atua
> Usable Jaa Can be muzh Ioer
> aII
> A650Z3
> TCy'JCO
> Cosrage
> detimedat  he IC-Er
> Tl Cr
> irestarp
> FrearTal
> 85qCoeraee
> T3
> 859
> OfJays raye
> eastone non MULLa-ross 13C stoc -
> Dutrarysock-days rTaysll be miss ng 5
> 32-03
> usable data could be rruch lower [2匀。,768 NaNsl
> Tvy
> TSFU
> a
>  =
> dacy
> Ie


---

