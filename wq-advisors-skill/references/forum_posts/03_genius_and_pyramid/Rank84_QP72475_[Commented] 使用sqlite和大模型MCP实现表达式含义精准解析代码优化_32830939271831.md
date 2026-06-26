# 使用sqlite和大模型MCP实现表达式含义精准解析代码优化

- **链接**: https://support.worldquantbrain.com[Commented] 使用sqlite和大模型MCP实现表达式含义精准解析代码优化_32830939271831.md
- **作者**: LS51569
- **发布时间/热度**: 1年前, 得票: 6

## 帖子正文

**本文使用cherry studio和sqlite mcp，可以从sqlite数据库准确获得数据字段的信息，相比于将datasets导入知识库检索更加准确，因为sqlite mcp会直接执行sql语句从数据库检索到对应数据行，效果如下：**


> [!NOTE] [图片 OCR 识别内容]
> 用户
> 9
> 06/1004.55
> @Qwen: Qwen3 2358 A228 (Free)
> asi数据表里用了anl14_all_mean_eps_Fy1 这个数据,解释一下他的含义
> Tokens: 44
> Qwen: Qwen3 2358 AZZB (Free) | OpenRouter
> 06/1004.55
> 已深度思考
> (用时0.1秒)
> 我可以为你查询包含 anl14_all_mean_eps_Fy1 的 asi_datafields 表中相关信息
> 让我先查找这一数据项的描述
> read_query
> 已完成
> params
> {
> query"
> SELECT description
> FROM asidatafields
> WHERE datafield_id
> anl14_all_mean_eps_fyl
> },
> response":
> {
> content"
> [
> {
> 'type"
> text"
> text"
> " [{'description':
> Mean
> 0f
> estimations
> of earnings per
> Share
> upcoming
> year' }]'
> ]
> iSError
> false
> 已深度思考 (用时0.1秒)
> 根据查询结果,
> anl14_all_mean_eps_fyl 的描述是:
> "Mean OF estimations OF earnings per share - upcoming year"
> (意为:  每股收益的预测均值 -下一年度)
> 这表示该数据字段提供的是分析师对未来一年内公司每股收益 (EPS) 的预测值的平均值。
> 它通常用于财务分析和投
> 资决策,以便了解市场的预期情况。具体来说, 这个字段可以帮助评估公司未来盈利能力,是投资者预测公司股票价
> 值的重要指标之一。
> 如果需要。我可以进一步查询其他相关字段的值 (如数据集
> 分类。覆盖率等) ,或者解释它在实际场景中的作用!
> 是否需要继续查询其他信息?
> Tokens: 2069 ^1648 v421
> 用户
> 左田去
>  e


具体步骤：

1. 将所有数据字段存入sqlite。可以参考之前的帖子，将datasets所有字段信息存入表中


> [!NOTE] [图片 OCR 识别内容]
> description
> 丫
> dataset
> 丫
> category
> 孓
> Worldquant_datasets.db
> The highest estimation
> of earnings"
> {'id
> analystlg
> 'name
> Estim
> {'id'
> analyst
> name
> Analyst。
> 6 main
> 2
> The highest estimation of earnings"
> {'id
> 'analystlg
> 'name
> Estim
> {'id
> 'analyst
> name
> Analyst。
> O 表7
> asi_datafields
> 3
> The lowest estimation
> of earnings
> {'id'
> 'analystlg
> 'name
> Estim
> {'id'
> 'analyst
> name
> Analyst。
> datasets
> The
> Lowest Estimation of Earnings
> {'id
> analystlg
> name
> Estim
> {'id'
> analyst
> name
> Analyst。
> eur_datafields
> 5
> Mean
> 0f
> estimations
> 0f earnings
> pe
> {'id
> analystlg
> 'name'
> Estim
> {'id'=
> analyst
> name
> Analyst。
> opt_alpha
> Mean
> 0f
> Estimations
> 0f Earnings
> Pei
> {'id
> 'analystlg
> 'name
> Estim
> {'id
> analyst
> name
> Analyst
> sqlite_master
> sqlite_sequence
> Median
> 0f
> Estimations
> 0f
> Earnings
> {'id'
> 'analystlg
> 'name
> Estim
> {'id'
> 'analyst
> name
> Analyst:
> submit_alpha_check
> Median
> of estimations of Earnings
> {'id
> 'analystlg
> 'name
> Estim
> {'id'
> analyst
> name
> Analyst。
> 服务器对象
> Num Of Estimations of Earnings
> Per:
> {'id
> analystlg
> 'name'
> Estim
> {'id'=
> analyst
> name
> Analyst。
> 10
> Num
> 0f
> estimations
> of earnings per
> {'id
> analystlg
> 'name
> Estim
> {'id
> analyst
> name
> Analyst。
> 11
> Standard
> Deviation
> of Estimations
> {'id'
> 'analystlg
> 'name
> Estim
> {'id'
> 'analyst
> name
> Analyst。
> 12
> Standard
> Deviation
> 0f
> Estimations
> {'id
> analystlg
> name
> Estim
> {'id'
> analyst
> name
> Analyst。
> 13
> Number
> Of period
> {'id
> analystlg
> 'name'
> Estim
> {'id'=
> analyst
> name
> Analyst。
> 14
> Type
> 0f
> Period
> {'id
> 'analystlg
> 'name
> Estim
> {'id
> analyst
> name
> Analyst
> 15
> Current Share Outstanding
> {'id'
> 'analystlg
> 'name
> Estim
> {'id'
> 'analyst
> name
> Analyst:
> 16
> Broker
> name
> {'id
> 'analystlg
> 'name
> Estim
> {'id'
> analyst
> name
> Analyst。
> 17
> Estimation
> Value
> {'id
> analystlg
> 'name'
> Estim
> {'id'=
> analyst
> name
> Analyst。
> 18
> Estimation Value
> upcoming
> 3
> quar
> {'id
> analystlg
> 'name
> Estim
> {'id
> analyst
> name
> Analyst。
> 19
> The highest estimation
> 0f
> Book
> Val:
> {'id
> 'analystlg
> 'name'
> Estim
> {'id'
> 'analyst
> name
> Analyst。
> 20
> The highest estimation
> 0f
> Book
> Val:
> {'id
> analystlg
> name
> Estim
> {'id'
> analyst
> name
> Analyst。
> N
> TL
> :+
> +'+'
> [
> 几。+7
> 「! |
> 7+1 |
>  |
> C+
> 「|。
> 17|
> 
> [7|


2. 在cherry studio中配置mcp。参数最下面一行事db文件所在位置


> [!NOTE] [图片 OCR 识别内容]
> 模型服务
> 名称
> 默认模型
> sqlite
> 网络搜索
> 描述
> MCP 服务器
> 描述
> %常规设置
> Ce 显示设置
> *类型
> 品  小程序设置
> 标准输入/输出 (stdio)
> 兕  快捷方式
> 命令
> 8  快捷助手
> UVX
> q  划词助手
> 包管理源
> g  快捷短语
> 默认
> 清华大学
> 阿里云
> 中国科学技术大学
> 华为云
> 腾讯云
> 数据设置
> 参数0
> 关于我们
> mcp-server-sqlite
> --db-path
> /Users
> S/consultant /data/
> worldquant_datasets. db


3. 在窗口对话，勾选上mcp

Mcp调用通常比较耗费token，所以这里用了openrouter上免费的qwen3 api


> [!NOTE] [图片 OCR 识别内容]
> 用户可以相关项月中杳看苴改讲
> 厉馈和衬仄讨论
> 例如
> 关闭
> sqlite
> 高德地图
> 高德地图是
> 个支持任何MCP协议客户端的服务器。允许用户转
> 添加服务器.
> MCP 服务器
> ESC 关闭
> MCP 服务器
> 在这里输入消息
> 田 @ ?
> 夕  孕 {?


也可以扩展到mysql，有对应的mcp。

---

## 讨论与评论 (6)

### 评论 #1 (作者: YQ51506, 时间: 1年前)

想法不错，但是有点大材小用了，可以想想是不是有更有潜力的应用

---

### 评论 #2 (作者: HW93328, 时间: 1年前)

感谢大佬的分享，最近我也关注到了mcp可能在alpha因子挖掘中起到的一些作用，楼主的这个思路非常好，将brain平台上的字段描述存储到本地中让模型可以精准获取并解析。在此基础上我觉得是否可以再接入docx或者md方面的mcp理解brain平台上的一些规则以及alpha方面的知识，进而可以帮助我们构建具有经济学意义的alpha模板之类的事情，又或者是将回测完的alpha数据落到数据库中让ai帮我们自动分析选择。mcp有很大的想象空间，也期待楼主分享更多实用的mcp工具！

==================================

---

### 评论 #3 (作者: 顾问 QP72475 (Rank 84), 时间: 1年前)

不错的方法，有空我也尝试一下。

---

### 评论 #4 (作者: FL39657, 时间: 1年前)

很有用，节省了很多写模板时，查询信息花的时间

---

### 评论 #5 (作者: AH18340, 时间: 1年前)

感谢大佬的深度分享！这篇关于[使用sqlite和大模型MCP实现表达式含义精准解析] 的帖子干货满满，，让我深受启发。这种无私的经验传递真的太难得了，必须点赞收藏反复学习！期待您后续更多精彩内容！

===============================================================================

---

### 评论 #6 (作者: YP44571, 时间: 1年前)

感谢大佬，让我深受启发，随着学习的深入，发现脑子不大够用了，正迫切需要各种工具的辅助。

---

