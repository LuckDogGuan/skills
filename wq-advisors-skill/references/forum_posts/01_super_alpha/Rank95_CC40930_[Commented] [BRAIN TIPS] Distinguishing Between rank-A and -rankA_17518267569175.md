# [BRAIN TIPS] Distinguishing Between rank(-A) and -rank(A)

- **链接**: https://support.worldquantbrain.com[Commented] [BRAIN TIPS] Distinguishing Between rank-A and -rankA_17518267569175.md
- **作者**: NL41370
- **发布时间/热度**: 2年前, 得票: 9

## 帖子正文

Although simulating  **rank(-A)**  and  **-rank(A)**  yield identical performance metrics, they don't behave the same way in all scenarios.

**Background Process**

When these expressions are simulated, rank(-returns) would result in Alpha values in the range of [0, 1], while -rank(returns) would result in Alpha values in the range of [-1, 0], as seen in the green boxes below.

This difference in ranges between the two expressions would be neutralized away during the  [background process](https://platform.worldquantbrain.com/learn/documentation/create-alphas/how-brain-platform-works) , when we subtract the average of the Alpha values from each Alpha value in the group, as shown in the red boxes below. Thereafter, the resultant weights for capital allocation would be the same for both expressions.


> [!NOTE] [图片 OCR 识别内容]
> Stocks
> Returns
> Rankl-returns/
> Minus AVB
> Neutralization
> 0115OIMPMAIP
> Normalize welbhts
> 015OIMIe IAIIP
> AIlocate capital
> StOCR 1
> 3.05
> 0.UU
> U.30
> U,50
> U.SUI
> U.2_
> -4.38
> Stock 2
> 2.550
> 0 5O
> 0.36
> 0.16
> [ T
> -3.13
> Soch3
> 1.85
> 0.09
> 1.88
> Stock
> 0.55
> 0
> StoC
> .29
> Siock
> 0,99
> Stock7
> 0,36
> Siock 3
> 2,8%
> 1,00
> 1
> 44
> StOCKS
> Returns
> Ranklreturns)
> Mus AVB
> Neutralization
> 405OIUte VAIUC
> Normalize weiBhts
> K05OIUtC
> VA1UC
> Allocate capital
> Stock1
> 3.05
> 1.00
> DS
> CSU
> 0.22
> Stock2
> 2.59
> 0.85
> U.3U
> 0.36
> U3b
> 0.16
> ULo
> 3.13
> Siock3
> 1.89
> Stock
> 0.596
> 0,07
> 0.63
> Sioc 5
> 0.296
> 7 
> 11
> 17
> Siock
> 0,93
> 0,29
> 0,21
> 009
> 17
> SoC 7
> 1.7
> -0.4
> 07
> 016
> UO
> ULo
> 3.13
> Srock 8
> 2.8%
> 0.00
> @
> 0S0
> 0 SN
> 0.22
> 4.33
> 007
> 0.50


Although these two Alphas would produce the same results when simulated on their own, the same cannot be said when they are used with other expressions or operations.

**Interactions with other Expressions**

For example, when these two Alphas are each multiplied with another Alpha expression, the resultant Alpha values would differ in ranges and intervals, as seen in the red boxes below. Consequently, the neutralized values and ultimately the weights allocated would also differ.


> [!NOTE] [图片 OCR 识别内容]
> UTALTIUITII/
> TIf
> UFTINI
> Rankl return)
> IOUNOI
> IIOIII
> AUCL JNT
> LIIC A
> N IIJIN
> 4LUIIITJIIIL
> Normallze welpht
> UAUOILIT'MAILI
> UNOGtC GDIL
> SUOCR !
> T
> StnCl
> 2.5沾
> 0.0
> 0.03
> 9
> Sock 9
> 1.8沾
> 00g
> Stoc+
> 0,65
> 0,43
> 0,30
> Stocr 5
> Stock6
> -0.9o
> OTI
> 0.05
> Om
> SCOCK/
> 1
> SCOCk{
> ~26
>  U
> Rankl-retrnsl
> SInC
> RPIIIII,
> RnkITMITII'
> athOI
> olpha
> TTOIICT
> alph
> Minws AYR
> Ntaliaion
> AIsnlulo VAIUP
> Nnmalip
> weights
> HhNIIIP SIIII
> NlInlr
> qpital
> Stoc!
> 3.0
> 1,00
> IN
> 1,00
> 0.61
> 0.25
> 501
> Stocr2
> 2.55
> stock }
> 1.8o
> 0.22
> 0.09
> 178
> StOCk』
> 
> Stoc 5
> Vc
> Slock 6
> 095
> SLOCK/
> SnC {
> 8
> 0O0


**Interactions with other Operators**

The two expressions can also interact differently with operators. To illustrate this, we have Alpha 1 and 2 below using the if_else() operator.

Expression 1:

returns > 0? rank(-returns) : 1

Expression 2:

returns > 0? -rank(returns) : 1

Given the if-else condition, Stocks 6 to 8 would have Alpha value of 1, as shown in the yellow cells below. Again, the resultant expression values would lead to differing weights allocated.


> [!NOTE] [图片 OCR 识别内容]
> Stocks
> Returns
> Rankl-returns/
> AU
> Neutralization
> 015OIMPMAIP
> NOIAI 
> Welbhts
> 0750III
> AIILP
> AIlocate capital
> StOCR 1
> 3.05
> 0.UU
> 0.33
> 0,53
> 0.20
> U2U
> -4.08
> Stock 2
> 2.50
> 1 5S
> 0+1
> 0.15
> 0.15
> 3.03
> Stock
> 1.35
> 0.10
> 1.97
> Stock4
> 0.55
> 09
> Stock
> Siocr
> TU
> Srock 7
> 1.00
> StoC 3
> 2.8%
> 1.00
> 0.16
> U10
> 3.29
> StOCKS
> Returns
> Rank(returns)
> WsMR
> Neutralization
> 405OIUtC
> VAlUe
> Normalize weiBhts
> L0SOIUtC
> VA1Ue
> Allocate capital
> Stock1
> 3.05
> 1.00
> 0.93
> 0.1'
> [ 11
> 2.89
> Stock
> 2.59
> 0.86
> 0.07
> 079
> 0.12
> 0.12
> 2.4
> Siock3
> 1.35
> 0.71
> 2,00
> Stock
> Siocr
> 0,43
> 1,11
> Srock
> 0.93
> 1.00
> 3.33
> StoC7
> 1.7
> 1.00
> 1.07
> 3.33
> Stock 3
> 2.8%
> 1.00
> 0.07
> 1.07
> 017
> 0.17
> 3.33


**Interactions with if_else() operator – as a condition**

Alternatively, we can also include the two sub-expressions as the condition in the if_else() operator.

Expression 1:

rank(-returns) > 0? 0 : 1

Expression 2:

-rank(returns) > 0? 0 : 1

In Expression 1, all stocks would be allocated weight = 1, while in Expression 2, all stocks would be allocated weight = 0.


> [!NOTE] [图片 OCR 识别内容]
> Stocks
> Returns
> Rankl-returns)
> StOCI
> ,0%
> StOCL 2
> 2.59
> 0.14
> STOCL 3
> 1.89
> StOC4
> 0.63
> Stock 5
> 0.57
> StOC 5
> 0,9%
> 0.71
> Stoc7
> 1.7%6
> StOCL 3
> 2.3%
> 1.00
> StOCKS
> Returns
> Rank(returns}
> StOCE 1
> 3.0%
> 1.00
> StOc 2
> 2.59
> 0.36
> StOC 3
> 1.3%
> 0.71
> StOCL4
> STOCL 5
> 0.29
> 0.43
> StOC
> 0.9%
> 0.29
> StOCE 7
> 1.73
> 0.11
> StOC 8
> 2,8%
> 0,00


---

## 讨论与评论 (7)

### 评论 #1 (作者: PK42917, 时间: 2年前)

can we see the selections of our alpha at the stock levels?

---

### 评论 #2 (作者: AG20578, 时间: 2年前)

Hi! No you can't see weights on stock levels, tables above - is just an illustrations.

---

### 评论 #3 (作者: AC63290, 时间: 1年前)

Though  `rank(-A)`  and  `-rank(A)`  yield identical metrics in isolation, they differ in interactions with other expressions and operators. Variances in value ranges impact neutralization, weight allocation, and results when combined or used in conditions. These distinctions highlight the importance of understanding subtle expression behaviors when designing Alphas for robust performance.

---

### 评论 #4 (作者: TT55495, 时间: 1年前)

In addition to the differences in range and weight allocation between rank(-returns) and -rank(returns), how might these variations affect the overall stability and robustness of an Alpha model when backtested over longer periods or in different market conditions? Could the interaction between these expressions and other factors, such as volatility or liquidity, lead to unexpected results?

---

### 评论 #5 (作者: 顾问 CC40930 (Rank 95), 时间: 1年前)

In conclusion, while both expressions may produce identical performance metrics in simulations, their interaction with other expressions or operators can lead to differing results due to their distinct ranges and behavior.

---

### 评论 #6 (作者: ND68030, 时间: 1年前)

**Adjust the Look Back Period:**

- Locate the parameter that defines the look back period (e.g., "Period," "Length," "Look Back").
- Enter the desired number of periods (e.g., changing from 14 to 20 days).

---

### 评论 #7 (作者: 顾问 CT68712 (Rank 27), 时间: 1年前)

It's really interesting to see how rank(-A) and -rank(A) can yield identical performance metrics but behave differently when combined with other expressions. As a high-frequency trader, I totally get how crucial it is to understand these nuances. For instance, the difference in range can significantly affect the resultant weights for capital allocation, which is something we have to consider in our models. Additionally, the interactions with operators like if_else() can lead to vastly different outcomes in terms of weight allocations, which could impact our strategy's performance. This highlights how important it is to deeply analyze expression behaviors when developing alpha models for consistent performance across varying market conditions.

---

