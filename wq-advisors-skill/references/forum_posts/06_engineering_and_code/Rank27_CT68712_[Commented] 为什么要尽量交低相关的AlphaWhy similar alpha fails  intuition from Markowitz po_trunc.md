# 为什么要尽量交低相关的Alpha?Why similar alpha fails:  intuition from Markowitz portfolio management theory

- **链接**: https://support.worldquantbrain.com[Commented] 为什么要尽量交低相关的AlphaWhy similar alpha fails  intuition from Markowitz portfolio management theory_27986550038423.md
- **作者**: ZL29184
- **发布时间/热度**: 1年前, 得票: 12

## 帖子正文

**前言**

我们在比赛（如最近的atom）中，经常会遇到machine出来的一批能提交的alpha，在交完一个之后，其他的就立刻变成扣分的alpha。同时也有遇到一个特别好的alpha，在提交完后，相似的alpha依然能够加分。本篇文章就包含笔者对上述原因的思考，以及基于此现象的比赛加分策略。

**简化模型构建**


> [!NOTE] [图片 OCR 识别内容]
> 考虑一一
> Portfolio, 其中配置钓
> 秘资立等权组合。其中每种资产的权重为 I/n, 我们设权
> 重向量为 W。其每种资产钓收益为Ki。 总平均收益为p = E(Mj)j= 1,2,...,1。风险 (波动性)
> 佼用收益的方差来衡量。可以有矩阵 C 为两两资产收益钓协方差矩阵。矩阵中的僮为Oij =
> COV(KiNi).
> 总收益很显然为 p = KTW
> 其中八为收益向量。
> 模型的目标可以是最小化风险为目标
> 此时总收益条件可以看作是对于权重的一个约束。
> 我们有:
> Tin WTCWC
> 8.七
> Zwi=i
> KTw 2 pe
> WI' W2'
> Wn 2 0e
> 当然我们可以直接利用拉格朗日乘值法解出这个式子。得到 W, 其牛 W 是总收益和(协〉方
> 差的函数。虽然我们这里的己经是给定的了。当 W 给定。总收益和方差自然也就是一一
> trade
> Off 的关系了。


通常来说，风险和收益的关系是二次的。具体含义是想要增加一点收益就要二次方的风险承担。可以看到如下图的有效边界所示。（满足优化条件的组合 w 会根据期望或者目标组合收益产生变化, 从而给出不同的风险值. 如果把所有组合按照期望收益和风险画图出来, 就是资产优化里常见的有效边界）

我们也可以在这个边界上找到一个最优资本配置线来比较不同的portfolio


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier
> 5.5
> 5.0
> 4.5
> 4.0
> 薹
> 罡
> 
> 3.5
> 訾
> 3.0
> 2.5
> 2.0
> 1.5
> 14
> 1.6
> 1.8
> 2.0
> 2.2
> 2.4
> Portfolio Risk (Standard Deviation)


**相似alpha失效的原因**

处于简化模型的考虑，我们一开始仅仅考虑三个风险资产，也就是考虑三个不同的alpha。收益向量为[8.41, 7.92, 5.21]。


> [!NOTE] [图片 OCR 识别内容]
> 其协方差的矩阵为 
> 0.6
> 0.6
> 0341
> 0.3
> 0.4
> 其有效边界如下



> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> Efficient Frontier
> Max Sharpe Ratio
> Capital Market Line
> 7.5
> 7.0
> 薹
> 罡
> 
> 6.5
> 詈
> 6,0
> 5.5
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 10
> 1.2
> 14
> Portfolio Risk (Standard Deviation)


然后我们加入另外一个alpha，其相关系数和每一个alpha都是0.9。然后考虑三种情况：

其收益等于5.21：

可以看到此时不加入新alpha的有效边界比加入后的要大，也就是加入一样的收益率，但是相关系数高的alpha，对portfolio的效果是负面的。


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> 8.0
> Original Efficient Frontier
> Original Max Sharpe Ratio
> New Efficient Frontier
> New Max Sharpe Ratio
> 7.5
> Capital Market Line
> 7.0
> 薹
> 罡
> 
> 6,5
> 詈
> 6,0
> 5.5
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> 1.4
> Portfolio Risk (Standard Deviation)


其收益等于7.92

虽然这个的边界比原来的大，但是最优资本配置线依旧是不如或者和之前的一样，也没有优化组合，或者是仅仅很少地优化了组合。


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> 8.00
> Original Efficient Frontier
> Original Max Sharpe Ratio
> New Efficient Frontier
> 7.75
> New Max Sharpe Ratio
> Capital Market Line
> 7.50
> 7.25
> 
> 7.00
> 罡
> 
> 6.75
> 訾
> 6.50
> 6.25
> 6.00
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> 1.4
> Portfolio Risk (Standard Deviation)


其收益等于8.41

可以看到此时加入后的有效边界要比之前大，最优资本配置线也在新的位置。这里有更高的return，但是同时其方差也增大了。体现出来的应该是能较多的加分，但是处于return和std的trade off，这样子的优化似乎是不健康的。


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> Original Efficient Frontier
> Original Max Sharpe Ratio
> 8.0
> New Efficient Frontier
> New Max Sharpe Ratio
> Capital Market Line
> 7.5
> 薹
> 罡
> 7.0
> 
> 詈
> 6.5
> 6.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 10
> 1.2
> 1.4
> Portfolio Risk (Standard Deviation)


**基于此的策略**

我们加入另外一个alpha，其相关系数和每一个alpha都是0.3。然后也考虑三种情况：

其收益等于5.21：可以看到有效边界基本一致，没有什么提升


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> Original Efficient Frontier
> Original Max Sharpe Ratio
> New Efficient Frontier
> 8.0
> New Max Sharpe Ratio
> Capital Market Line
> 7.5
> 薹
> 罡
> 
> 7.0
> 詈
> 6.5
> 6.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 10
> 12
> 1.4
> Portfolio Risk (Standard Deviation)


其收益等于7.92，可以看到此时有效边界更大了，同时在return提高了的情况下，std也减少了，这是我们想要的优化。


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> Original Efficient Frontier
> 9.5
> Original Max Sharpe Ratio
> New Efficient Frontier
> New Max Sharpe Ratio
> Capital Market Line
> 8.5
> 薹
> 8.0
> 罡
> 
> 7.5
> 詈
> 7.0
> 6.5
> 6.0
> 0.0
> 0.2
> 0.4
> 0,6
> 0.8
> 1.0
> 1.2
> 1.4
> Portfolio Risk (Standard Deviation)
> 9.0


其收益等于8.41，同样的，我们看到了收益等于7.92一致的情况。


> [!NOTE] [图片 OCR 识别内容]
> Efficient Frontier with Capital Market Line
> Original Efficient Frontier
> Original Max Sharpe Ratio
> New Efficient Frontier
> New Max Sharpe Ratio
> Capital Market Line
> 8.5
> 薹
> 罡
> 8.0
> 
> 訾
> 7.5
> 7.0
> 6.5
> 6.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> 1.4
> Portfolio Risk (Standard Deviation)
> 9.5
> 9.0


**总结**

我们可以看到在相同的return的情况下，不同的corr带来的增益效果是有很大区别的。IS的加分是一个方面，对于组合的优化也是一个方面，可以看到低corr的策略在如上的情况中是最优的。这也是我在比赛中采取的策略，希望这篇文章对各位有帮助。

出于时间和精力的原因，本文写作仓促，许多细节未来得及检查，仅仅提供一个基础的idea，希望各位多多批评指正，共同进步。

---

## 讨论与评论 (8)

### 评论 #1 (作者: TN48752, 时间: 1年前)

我同意你的观点，提交低相关性的阿尔法将有助于增加投资组合的价值，从而增加价值因子。然而，提交 alpha 并在很长一段时间内减少确实很困难，部分原因是池很大，也可能是因为前几个月的 corr 太低。

---

### 评论 #2 (作者: PH82915, 时间: 1年前)

实际上，我看不出低相关性和价值因子之间的明确关系。我只同意提交低相关性将为投资组合增加价值，但价值因子意味着更高的 OS。提交低相关性意味着发现信号的方式与 WQBrain 的池不同，后者已经通过了 OS 测试并且没有被淘汰，我认为 80% 的低相关性 alpha 将具有较低的 OS，而 20% 的 OS 良好。

---

### 评论 #3 (作者: 顾问 PN39025 (Rank 87), 时间: 1年前)

I also agree with you that sending low correlation can increase weight quickly because it can create more diverse portfolios. But I think the corr between IS and prod will be different. So I think the corr in IS just needs to be below 0.6 to be suitable.

---

### 评论 #4 (作者: 顾问 CT68712 (Rank 27), 时间: 1年前)

感谢您的精彩分享！文章对低相关性 Alpha 的重要性以及其对投资组合优化的影响阐释得非常清晰，特别是通过有效边界的分析，生动地说明了不同相关性对收益和风险的权衡。

不过我有一个疑问，在实际操作中，您是如何筛选出相关性较低且收益较稳定的 Alpha？是否会采用特定的方法来量化 Alpha 的相关性，比如动态调整相关系数的阈值或使用特定的数据工具？期待您能分享更多具体的实践经验！

---

### 评论 #5 (作者: JB71859, 时间: 1年前)

这篇文章深入分析了相似alpha失效的原因，并提供了非常有价值的思考和策略，尤其是关于低相关性alpha的优化方案。你提到的“相同收益情况下，低相关性alpha的增益效果远大于高相关性alpha”的观点特别有启发性，凸显了如何通过精确的组合优化来避免不健康的风险收益权衡。尤其是你在比赛中采取低相关alpha的策略，既能提高收益，又能控制波动，确实是一种非常聪明且高效的做法。

文章的思路清晰，理论与实践相结合，尤其对于那些深度参与竞赛的同学来说，具有很大的参考价值。虽然写作上还有些地方可以进一步打磨，但基本的框架已经很完整，期待你能进一步展开细节部分，帮助更多人理解如何在实际比赛中实施这些策略。感谢分享，期待更多的深入讨论和思考！

---

### 评论 #6 (作者: CL50482, 时间: 11个月前)

感谢分享，只能记住结论：低corr的策略是最优的

---

### 评论 #7 (作者: CC85858, 时间: 9个月前)

虽然不能完全理解，但是挖出低相关的alpha有一种成就感，仿佛挖到了宝藏的感觉

---

### 评论 #8 (作者: 顾问 ML47973 (Rank 100), 时间: 9个月前)

感谢大佬分享精彩的帖子，图文并茂看起来非常舒服 . 我认为提交低相关的阿尔法

[图片 (图片已丢失)] 
        一、长远发展来看 可以保证阿尔法组群具有阿尔法多样性，同时提交低相关性的阿尔法将有助于增加投资组合的价值，保持多样性可以降低投资风险，正如量化对冲的理念 ； 
        二、自身近处来看 从 base payment 到 weight 都是非常明确的跟 Product Correlation (PC) 指标挂钩，保持低 pc 都是非常有必要的 .

[图片 (图片已丢失)]

---

