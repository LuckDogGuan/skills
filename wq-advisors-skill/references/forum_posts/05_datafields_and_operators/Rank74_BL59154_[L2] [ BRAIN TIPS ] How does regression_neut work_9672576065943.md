# [ BRAIN TIPS ] How does regression_neut work ?

- **链接**: https://support.worldquantbrain.com[L2] [ BRAIN TIPS ] How does regression_neut work_9672576065943.md
- **作者**: KA64574
- **发布时间/热度**: 3 years ago, 得票: 9

## 帖子正文

The regression_neut (Y,X) operator conducts a cross-sectional regression on all the stocks in a given universe for the variables Y and X, using the parameters ‘a’ and ‘b’ — creating the final neutralized output of Y-(a+b*X) for each of the stocks in the universe.

Say, you have a dataset with sales and assets for 3,000 USA-listed companies and you want to answer the question: On a particular day, if my company’s assets equal 10, what sales would it have? You look into all the other companies with assets equaling ‘any value’ and their sales happen to be ‘any other value.’ You want to find the dependency between sales and assets and come up with a line provided by regression.

This line is defined as: sales_estimation = a+b*assets, where a and b come from regression by 3,000 points (companies’ sales–assets pairs) on a particular day, and assets are the assets for your company on that day. The regression_neut is sales (actual sales for your company) - sales_estimation (cross-sectional).

Here are a couple of examples of how this idea can be used in your workflow:

- As cross-sectional mean reversion (or momentum) of some value (ratio, returns, etc.) by something related to this value (otherwise b would be 0).
- For orthogonalization to some factors defined by X (similar to vector_neut operator). One popular factor is long price momentum/reversion.

---

## 讨论与评论 (1)

### 评论 #1 (作者: PH82915, 时间: 1 year ago)

Really appreciate this, it's a valuable topic!

---

