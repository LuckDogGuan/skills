# Please Share Your Thought! Rules and Updates Regarding the competition置顶的

- **链接**: https://support.worldquantbrain.com[Commented] Please Share Your Thought Rules and Updates Regarding the competition置顶的_38689147544343.md
- **作者**: WL13229
- **发布时间/热度**: 3个月前, 得票: 21

## 帖子正文

Dear Consultants,

Greeings again for your participation in this competition. Please use this forum to exchange your ideas and thoughts, or any questions you may have. Do not use pure AI to generate content (which may be deleted). Good posts or comment will be featured by our team to help you get more Genius Community points.

Best

Weijie

------------------

For the recent webinar's recording, please refer to 👇

[Introduction to Data Creation Challenge 2026 Webinar Recording (16th Feb)]([Commented] Introduction to Data Creation Challenge 2026 Webinar Recording 16th Feb置顶的被推荐的_38681830954135.md)

---

## 讨论与评论 (24)

### 评论 #1 (作者: WL13229, 时间: 3个月前)

please note that the baseurl is in the following

```
API_BASE_URL = "https://api.worldquantbrain.com"
```

```
INCORRECT Example 👉 API_BASE_URL = "https://api.dev.worldquantbrain.com"
```

---

### 评论 #2 (作者: 顾问 JN96079 (Rank 44), 时间: 3个月前)

Is it possible to create a dataframe that, when used to create an alpha, can be submitted?

---

### 评论 #3 (作者: 顾问 JN96079 (Rank 44), 时间: 3个月前)

I have only 2 years of IS, but they are good; it still shows the following. How can I solve that?
 
> [!NOTE] [图片 OCR 识别内容]
> 囱 IS Testing Status
> 7PASS
> 2 FAIL
> The simulation doesn't match the current IS period . Please clone this alpha and re-simulate。
> Alphas containing user defined fields and can't be submitted。
> 2WARNING
> 5 PENDING


---

### 评论 #4 (作者: VG88979, 时间: 3个月前)

Remember you have 'create_dataframe' function in your code, which will help WorldQuant to study and explore your dataframe later.

---

### 评论 #5 (作者: 顾问 JN96079 (Rank 44), 时间: 3个月前)

And the issue;

#The simulation doesn't match the current IS period.

How to fix that?

---

### 评论 #6 (作者: AV90680, 时间: 3个月前)

429 Client Error: Too Many Requests for url:  [https://api.worldquantbrain.com/authentication](https://api.worldquantbrain.com/authentication)   getting this error

---

### 评论 #7 (作者: WL13229, 时间: 3个月前)

[顾问 JN96079 (Rank 44)](/hc/en-us/profiles/25468856195607-顾问 JN96079 (Rank 44))

please make a dataframe between 2021-01-01-2022-12-31

---

### 评论 #8 (作者: WL13229, 时间: 3个月前)

@AV90680 please use a sleep method to control your speed. you can refer to the sample demo code

---

### 评论 #9 (作者: ER89729, 时间: 3个月前)

Thanks for the tips! I found that aligning my dataframe with the IS period helps avoid simulation errors. Also, using sleep() between API calls prevents the 429 error

---

### 评论 #10 (作者: AR98193, 时间: 3个月前)

Error creating data field: 400 ["Unable to validate data field"] Upload failed: 400 Client Error: Bad Request for url:  [https://api.worldquantbrain.com/users/self/data-fields](https://api.worldquantbrain.com/users/self/data-fields)

Please explain this error

---

### 评论 #11 (作者: WW15616, 时间: 3个月前)

When I try to tag alpha,I got error:

```
Cannot update DCC2026 tag for this alpha.
```

Why I got this.operator too much or I use fields witch platform alright have (such as `cap`) with the field I made togather?

---

### 评论 #12 (作者: MO60428, 时间: 3个月前)

hi, on upload to brain,im getting this  "field (....ID_XXX_xx...) already exist",, how do i go about this?also does number of aunthetications on DCC also count for the 25times in brain?

---

### 评论 #13 (作者: WL13229, 时间: 3个月前)

[MO60428](/hc/en-us/profiles/32247871110551-MO60428)

you can scroll down to the end of the notebook to change the name of the field

---

### 评论 #14 (作者: WL13229, 时间: 3个月前)

[WW15616](/hc/en-us/profiles/34445801835927-WW15616)

you can only tag the alphas that use the fields you created and supporting fields only. please double check whether you have used other datafield

---

### 评论 #15 (作者: NO99584, 时间: 3个月前)

Hi, can we check,delete test data fields that already uploaded to our account? (please suggest by API or directly from platform)

---

### 评论 #16 (作者: AK58648, 时间: 3个月前)

Can you combine the created datafield with any other brain datafield to simulate the alpha, or does it have to be pure without any other legacy datafields?

---

### 评论 #17 (作者: 顾问 JN96079 (Rank 44), 时间: 3个月前)

Hi  [AK58648](/hc/en-us/profiles/26584508472471-AK58648) , from the admins, you need to  ***use only the created datafields*** in the alphas you will be tagging. Otherwise, support datafields are the only ones from Brain you are allowed to utilize, including country, subindustry, exchange, market, and currency.

^^JN

---

### 评论 #18 (作者: XX81632, 时间: 3个月前)

What are some good ways to obtain the comprehensive before-and-after-performance value?

---

### 评论 #19 (作者: CW89092, 时间: 3个月前)

can you use one datafield to create several alphas and tag them ?

---

### 评论 #20 (作者: JK32424, 时间: 3个月前)


> [!NOTE] [图片 OCR 识别内容]
> When |
> totagalphal got error:
> Cannot update DCC2026 tag for
> this
> alpha _
> Why
> got this operator too much or
> Use fields witch platform alright have (such as
> cap `) with
> the field
> made togather?
> try
 This error occurs when you use outdated datasets make sure you use created  *datafields*  with a  *dataframe*  between 2021-01-01-2022-12-31 which has gone through a **backtest**  and you can only tag the alphas that use the fields you created.

---

### 评论 #21 (作者: NO99584, 时间: 3个月前)

How many data fields can I upload,100 data fields? If I exceed the maximum limit, will the oldest ones be overwritten by newer ones, and will those older data fields no longer be usable or taggable for the competition?

---

### 评论 #22 (作者: 顾问 JN96079 (Rank 44), 时间: 3个月前)

Hey  [NO99584](/hc/en-us/profiles/34889104281495-NO99584) , I think the datafields stay there until further notice, so you should focus on uploading more if you like. I believe there is no maximum, and it isn't mentioned either!

^^JN

---

### 评论 #23 (作者: YX50005, 时间: 3个月前)

It seems like generating the Pair Network takes a very long time. Is that correct?

Additionally, I have a second question: Is the focus of this competition primarily on brainstorming many different themes, while the actual engineering implementation of the workflow is relatively less important?

---------------------If you come to the forum to study hard every day, you will get a GM---------------------------------

---------------------------------------------------------------------------------------------------------------------------

---

### 评论 #24 (作者: AR98193, 时间: 3个月前)

will UploadMatrix() be acceptable as an alternative to CreateDataframe() as this function was not used in one of the workflow python notebooks in a webinar but still was shown to us....

---

