# Simple solution to reduce Subuniverse Sharpe fail

- **链接**: https://support.worldquantbrain.comSimple solution to reduce Subuniverse Sharpe fail_40151877296791.md
- **作者**: 顾问 ME83843 (Rank 53)
- **发布时间/热度**: 1个月前, 得票: 17

## 帖子正文

Hello Quants
Subuniverse Sharpe is one of the biggest problems for many quants, especially in Europe region. A lot of alphas look good in overall results, but fail after subuniverse checks because the signal is weak, concentrated, noisy, or dependent on a few names.
Have been doing research on the same and below are my findings. Please fellow quants try them and give me your feedback as well.

## Simple solution to reduce Subuniverse Sharpe failure

## 1. Always rank your signal

Raw values often create unstable weights.

2. Neutralize by sector or industry

3. Use medium lookback windows

Very long windows become stale. Very short windows become noisy.

Best range:

`60 to 250`

4. Smooth noisy signals

5. Avoid multiplying two weak signals

If both legs are weak, product usually fails. Use rank combination instead.

---

## 讨论与评论 (0)

