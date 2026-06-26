# MAX TRADE Asia Region

- **链接**: https://support.worldquantbrain.com[Commented] MAX TRADE Asia Region_34488691312279.md
- **作者**: DS54387
- **发布时间/热度**: 10个月前, 得票: 5

## 帖子正文

Does anyone know how to enable the Max Trade setting via the API? I'm looking for the correct parameter or function call.

alpha_list = [ace.generate_alpha(x, region=REGION, universe=UNIVERSE, neutralization="COUNTRY", decay=0, delay=DELAY, max_trade="ON") for x in expression_list].                Not working for me.

---

## 讨论与评论 (13)

### 评论 #1 (作者: TP85668, 时间: 10个月前)

I think  `max_trade`  is not a valid parameter in the API call. The Max Trade setting can only be configured through the platform interface (not via API). You may want to check the API docs — currently, it doesn’t support enabling Max Trade directly.

---

### 评论 #2 (作者: TD40899, 时间: 10个月前)

You can check the announcement from when the Brain platform enabled the ON/OFF max trade feature, I remember there were some instructions provided.

---

### 评论 #3 (作者: RC80429, 时间: 10个月前)

I also tried enabling the Max Trade setting via the API, but didn’t have any success. If anyone has managed to get this working, please share the correct approach with the community.

---

### 评论 #4 (作者: JC84638, 时间: 10个月前)

I didn’t pass  `maxTrade`  as a keyword argument to  `generate_alpha()` , but rather included it inside the  `settings`  dict in the payload (jzc

> payload = {
> 'type': 'REGULAR',
> 'regular': None,
> 'settings': {
> 'decay': 0,
> 'delay': 1,
> 'instrumentType': 'EQUITY',
> 'language': 'FASTEXPR',
> 'nanHandling': 'OFF',
> 'neutralization': "SECTOR",
> 'pasteurization': 'ON',
> # 'testPeriod': 'P2Y',
> 'region': 'USA',
> 'truncation': 0.01,
> 'unitHandling': 'VERIFY',
> 'universe': 'TOP3000',
> 'visualization': False,
> 'maxTrade': 'ON'
> }
> }

---

### 评论 #5 (作者: AK98027, 时间: 10个月前)

I ran into the same issue recently! From what I've found,  **Max Trade isn't exposed in the current API parameters**  - it's only controllable through the web interface. The  `max_trade="ON"`  parameter you're using isn't recognized by  `ace.generate_alpha()` .

Have you tried submitting your alphas through the API first, then manually enabling Max Trade in the platform UI? It's not ideal for batch processing, but seems to be the current workaround. Would love to see this added to the API in future updates - it's definitely needed for automated alpha generation workflows!

Anyone from the platform team have insights on when this might be available via API?

---

### 评论 #6 (作者: TP18957, 时间: 10个月前)

This is a very relevant question since Max Trade is mandatory for ASI-region alphas and directly impacts after-cost performance at the combo level. From what I’ve seen,  `max_trade`  isn’t currently recognized as a direct parameter in  `ace.generate_alpha()` , which explains why passing it there fails. The correct approach, as noted, is to include it within the  `settings`  dictionary of the payload when using the API. For example:
payload = {
   "type": "REGULAR",
   "settings": {
       "region": "ASI",
       "universe": "TOP600",
       "neutralization": "COUNTRY",
       "decay": 0,
       "delay": 1,
       "maxTrade": "ON"
   }
}
This matches the JSON structure the platform expects. That said, it’s worth double-checking whether the API version you’re using fully supports this flag—some reports suggest the UI setting is more reliable. A best practice is to confirm via the simulation output whether Max Trade was applied (e.g., reduced excessive position sizing). If automation is critical, it may be safest to submit via API but toggle Max Trade in the UI until official documentation confirms stable support.

---

### 评论 #7 (作者: NT84064, 时间: 10个月前)

Thanks for asking this—super practical. A lot of us hit the same wall because it’s easy to assume “Max Trade” belongs in  `generate_alpha` , when in many ACE setups it’s actually a  **simulation control**  (and booleans beat  `"ON"` / `"OFF"` ). Your snippet is helpful because it highlights exactly where people try to switch it on, and it prompted me to re-check my own pipelines for silent no-ops when a flag isn’t recognized. The reminder to verify the applied controls in the simulation metadata is great practice, and even if someone’s ACE flavor differs, your question nudges everyone to standardize: define the signal first, enforce trading constraints at execution, and confirm units/limits. Really appreciate you bringing this up—it’s one of those small configuration details that can have an outsized impact on realized turnover, costs, and ultimately Pyramid progress.

---

### 评论 #8 (作者: AY28568, 时间: 9个月前)

That’s an interesting question , From your code, it looks like you are trying to set the  **Max Trade**  parameter directly in the  `generate_alpha`  function. Usually, some settings like max trade are controlled through specific API parameters or configuration options rather than a simple “ON/OFF” flag. It might be worth checking the latest API documentation or examples, as the exact keyword can differ (sometimes it’s written as  `max_trade` ,  `max_trades` , or a numerical value instead of “ON”). If nothing works, reaching out to support or testing with different parameter formats could help confirm the right one.

---

### 评论 #9 (作者: 顾问 HY90970 (Rank 54), 时间: 9个月前)

Hi,
you need to download the latest version of ACE API then only it will work. I also faced lot of difficulty in using max_trade parameter initially, you have raised a critical problem.

I use the following now, which works:

ace.generate_alpha(x, region= region,delay=delay, universe = universe, test_period = 'P2Y', decay= 4, max_trade="ON", neutralization= 'COUNTRY')

---

### 评论 #10 (作者: TP18957, 时间: 9个月前)

This is a really useful question because  **Max Trade**  is not just a convenience toggle—it materially affects turnover, after-cost performance, and compliance with ASI region requirements. Based on the comments here and my own experience, the confusion comes from how the API parses parameters. In most ACE workflows,  `max_trade`  isn’t recognized as a top-level keyword argument in  `generate_alpha()` . Instead, it has to be placed inside the  `settings`  dictionary of the payload with the correct key ( `"maxTrade": "ON"` ), as shown in some of the working snippets. One additional nuance: different API versions handle this flag inconsistently—older builds sometimes ignore it silently, so it’s always worth checking the simulation metadata to confirm it actually applied. Another best practice is to test both  `"ON"` / `"OFF"`  and boolean values ( `True` / `False` ) since implementations can differ. If you’re batch-submitting alphas, you might want to build a wrapper that enforces Max Trade post-submission by calling a confirmation function against the returned sim object. This ensures you’re not unknowingly running unconstrained simulations, which could skew your Pyramid or Power Pool contributions.

---

### 评论 #11 (作者: TP18957, 时间: 9个月前)

Thanks a lot for raising this point about enabling  **Max Trade**  via the API. It’s easy to overlook small configuration details like this, but as your post and the responses highlight, they can make a huge difference in practical workflows. I especially appreciate that you shared your exact code snippet—seeing where you placed  `max_trade`  makes it much easier for others to recognize why their own attempts might be failing. I also found the replies here super valuable, especially the clarification that Max Trade often belongs inside the payload  `settings`  rather than in the  `generate_alpha`  call directly. This kind of community troubleshooting is what makes the platform discussions so useful: one person’s sticking point quickly becomes a shared learning for everyone. I’ll definitely be rechecking my own API scripts to make sure I’m not missing silent no-ops when toggling Max Trade. Thanks again for surfacing such a practical and timely issue.

---

### 评论 #12 (作者: WH74165, 时间: 9个月前)

thx a lot

---

### 评论 #13 (作者: RP41479, 时间: 9个月前)

Max Trade often confuses users because it’s a simulation control, not generate_alpha. Always define the signal first, enforce trading limits at execution, and verify metadata to avoid silent no-ops and manage turnover effectively.

---

