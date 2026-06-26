# 【经验分享】一句话改造mcp支持pyhton alpha

- **链接**: https://support.worldquantbrain.com[Commented] 【经验分享】一句话改造mcp支持pyhton alpha_40684608877591.md
- **作者**: JX84394
- **发布时间/热度**: 1个月前, 得票: 48

## 帖子正文

# 一句话改造mcp支持pyhton alpha

修改create_simulation支持PYTHON，注意settings配置少了两个handling参数以及多了一个lookback默认设置256,只有python alpha才有lookback参数哦，并且默认使用fasteexpr    参考 论坛文章 Getting Started with Brain Python Alphas，进行实际python alpha测试，可以尝试将某些设置属性的fastexpr 类型的alpha转化成python alpha进行测
  试

# 一句话让python alpha动起来

参考 mcp文档 Getting Started with Brain Python Alphas, 将工作流和skills改造成 找python alpha 而不是fastexpr类型的alpha

好了，现在可以尽情享受python alpha的乐趣了，当然这只是迈出了第一步。。。

具体怎么让mcp用python alpha找到与fastexpr alpha不一样的alpha还需要进一步研究，加油各位！

---

## 讨论与评论 (4)

### 评论 #1 (作者: CZ39633, 时间: 1个月前)

====================================================================================  感谢大佬关于这个mcp改造分享，刚好可以无缝衔接的从AI工作流到做python alpha的工作                                    ================================自信人生两百年，会当水击三千里==========================

---

### 评论 #2 (作者: FF65210, 时间: 1个月前)

感谢jx佬的分享，又学会了一招。

===============================================================================
守正心，戒浮躁，恒复盘，危中机。“复利是世界第八大奇迹，关键在于找到可长期重复的正确策略，日复一日、不疾不徐地执行。”—— 爱因斯坦 / 查理・芒格
Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
sys.setrecursionlimit(α∞)
PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值# 有志者事竟成，苦心人天不负。千淘万漉虽辛苦，吹尽狂沙始到金。
=================================================================================

---

### 评论 #3 (作者: 顾问 LD22811 (Rank 39), 时间: 1个月前)

感谢大佬的探索经验

---

### 评论 #4 (作者: XW23690, 时间: 28天前)

感谢分享，正在初步探索python alpha

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

