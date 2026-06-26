# [BRAIN TIPS] Using trade_when for Event Alphas and Low Turnover Alphas

- **链接**: https://support.worldquantbrain.com[L2] [BRAIN TIPS] Using trade_when for Event Alphas and Low Turnover Alphas_8360363631127.md
- **作者**: KA64574
- **发布时间/热度**: 3 years ago, 得票: 46

## 帖子正文

You can use the following targeting to create event-driven alphas and low turnover alphas.

 **Concept:** 
If (event) {
Assign alpha values;
} else {
Hold alpha values;
}
Expression:

```
trade_when(Event_condition, Alpha_expression, -1)
```

**Pros:**

- Good alpha coverage
- Flexible in determining events
- Can be used to enhance signals by trading at the right time
- Low turnover and low cost alpha

**Cons:**

- Not easy to get high Sharpe alpha
- Not easy to get high return alpha

**Approach:** 
Define events: Any spike in returns, data values and technical indicators can be used to define events.
Alpha assignment: Look for signals that are aligned with the abnormality of an event — that is, alphas that need to be executed when such events happen.

 **Note:** 
Hold alpha can be replaced by decaying alpha linearly or exponentially.
Check alpha coverage to make sure events are not so rare.

---

## 讨论与评论 (11)

### 评论 #1 (作者: Permanently deleted user, 时间: 3 years ago)

[KA64574](/hc/en-us/profiles/7052057119511-KA64574) , what does -1 do in the expression

```
trade_when(Event_condition, Alpha_expression, -1) 
```

---

### 评论 #2 (作者: KA64574, 时间: 3 years ago)

Hi ,

The general format of trade_when operator is the following :

Trade_When (x=triggerTradeExp, y=AlphaExp, z=triggerExitExp)

z / triggerExitExp is basically the exit condition for the alpha . triggerExitExp = -1 means that the positions taken will not be exited .

Please do refer to the following page where you would find a more detailed explanation of the trade_when operator :

[https://platform.worldquantbrain.com/learn/data-and-operators/detailed-operator-descriptions#10-trade_when](https://platform.worldquantbrain.com/learn/data-and-operators/detailed-operator-descriptions#10-trade_when)

---

### 评论 #3 (作者: JC10962, 时间: 3 years ago)

Such great content. Thanks for sharing.

---

### 评论 #4 (作者: KY46056, 时间: 3 years ago)

What does "Hold alpha values" means?

---

### 评论 #5 (作者: SH71033, 时间: 3 years ago)

As event driven alphas have relevant values in case of rare events, such as company specific event, hold alpha value means holding position in the stock according to the expression in else parentheses {logic for Hold alpha values} instead of a NaN value.

---

### 评论 #6 (作者: PP55193, 时间: 2 years ago)

Thanks

---

### 评论 #7 (作者: EW29497, 时间: 2 years ago)

Could you please give an example of how to "Hold alpha can be replaced by decaying alpha linearly or exponentially"? thank you

---

### 评论 #8 (作者: SM57809, 时间: 2 years ago)

What is event_condition , please explain with an alpha as example.

---

### 评论 #9 (作者: AG20578, 时间: 2 years ago)

Hi!

> Could you please give an example of how to "Hold alpha can be replaced by decaying alpha linearly or exponentially"? thank you

Let's say event_condition is a particular condition you're interested in, and alpha_expression is the alpha you want to decay.

Now, your expression could look like this:

```
event_condition? alpha_expression : (alpha_expression + trade_when(event_condition, alpha_expression, -1))/2
```

In this configuration, if 'event_condition' is true, we take the 'alpha_expression' value. If it's false, we average the current 'alpha_expression' value and the 'alpha_expression' value at the time of the last event. This gradually decays the alpha.

You can also use 'days_from_last_change(event_condition)' to assign more or less weight to the 'old' alpha expression, controlling the rate of decay.

> What is event_condition , please explain with an alpha as example.

An example of event_condition could be something like (rank(volume/adv20) > 0.5). So the alpha will be executed when the rank of the ratio of  `volume`  to  `adv20`  exceeds 0.5.

So, an example alpha expression with event_condition might look like:

```
trade_when(rank(volume/adv20) > 0.5, pcr_oi_all, -1)
```

---

### 评论 #10 (作者: VK91272, 时间: 1 year ago)

thanks for providing these expression.

---

### 评论 #11 (作者: AC63290, 时间: 1 year ago)

Event-driven Alphas use targeted triggers to assign Alpha values during defined events while holding or decaying values otherwise. They offer good coverage, low turnover, and flexibility in timing trades. However, achieving high Sharpe or returns can be challenging. Ensure events are frequent enough to maintain meaningful Alpha coverage and signal relevance.

---

