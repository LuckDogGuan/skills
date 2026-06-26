# Data Idea系列1：Research Sentiment Data_Sentiment1Alpha Template

- **链接**: https://support.worldquantbrain.com[L2] Data Idea系列1Research Sentiment Data_Sentiment1Alpha Template_33247252289943.md
- **作者**: WL13229
- **发布时间/热度**: 1 year ago, 得票: 39

## 帖子正文

开一个新系列，对少人用的数据字段进行一些提示并增强LAB的使用。请注意，这并非官方提示，但是希望能给你一些idea的启发。请大家一定要在评论区进行评论，对提及的数据字段 **使用LAB进行探索并发出insight。仅有所有的datafield被探索后，我们才会发下一期，欢迎大家共建评论。**

今天我们聊的数据字段是： [Research Sentiment Data](https://platform.worldquantbrain.com/data/data-sets/sentiment1/fields)

Dataset_id: Sentiment1

Region/Delay/Universe: USA/Delay1/TOP3000

本文探索的数据字段：该数据集17个字段。

# Analysis Results

## Selected Fields

- **snt1_d1_uptargetpercent** : Ratio of (Number ofup target) over (Number ofall analysts)

## Analysis Output

***Step 1: 基础理解** 
-  **snt1_cored1_score** ：该分数用于衡量市场情绪，分数小于5为看跌，大于5为看涨，在[-5, 5]区间为中性。常用于判断市场对公司的整体情绪倾向，帮助投资者了解市场预期。
-  **snt1_d1_analystcoverage** ：指提供盈利预测的分析师数量。反映了市场对该公司的关注度，较多的分析师覆盖通常意味着公司受到市场更多关注，其信息透明度可能较高。
-  **snt1_d1_buyrecpercent** ：分析师给出买入建议的比例，即（分析师给出买入建议的数量 / 所有分析师数量）。用于评估分析师对公司股票的买入倾向，比例越高，表明分析师整体越看好该公司股票。
-  **snt1_d1_downtargetpercent** ：分析师给出下调目标价建议的比例，即（分析师给出下调目标价建议的数量 / 所有分析师数量）。体现了分析师对公司股价向下调整的预期程度，比例高可能暗示公司股价面临下行压力。
-  **snt1_d1_dtstsespe** ：分析师盈利预测的离散程度。反映了分析师之间对公司盈利预期的分歧大小，离散程度高意味着分析师们的看法差异较大，公司未来盈利的不确定性较高。
-  **snt1_d1_dynamicfocusrank** ：范围为0 - 100，数值高为买入信号，数值低为卖出信号。综合多种因素给出的一个动态的投资信号排名，帮助投资者快速判断当前市场动态下的买卖倾向。
-  **snt1_d1_earningsrevision** ：（1个月盈利预测均值的变化 / 股价）。衡量了近期盈利预测的变动情况与股价的关系，可用于观察市场对公司盈利预期的短期调整，变化幅度大可能预示着公司基本面或市场预期的改变。
-  **snt1_d1_earningssurprise** ：（实际盈利 - 预期盈利） / 股价。表示实际盈利与预期盈利的差异相对于股价的比例，反映了公司盈利是否超出或低于市场预期，盈利惊喜可能对股价产生重要影响。
-  **snt1_d1_earningstorpedo** ：（预期盈利 - 上一期实际盈利） / 股价。通过比较预期盈利与上一期实际盈利，评估公司盈利的增长或下降趋势，帮助投资者判断公司盈利的持续性。
-  **snt1_d1_fundamentalfocusrank** ：范围为0 - 100，数值高为买入信号，数值低为卖出信号。基于公司基本面因素给出的投资信号排名，侧重于从基本面角度评估公司股票的投资价值。
-  **snt1_d1_longtermepsgrowthest** ：分析师预期的经营盈利增长的中位数。反映了分析师对公司长期盈利增长的预期，是评估公司长期发展潜力的重要指标。
-  **snt1_d1_netearningsrevision** ：（分析师上调盈利预测的数量 - 分析师下调盈利预测的数量） / 所有分析师数量。体现了分析师对公司盈利预测调整的净方向和程度，正数表示上调的分析师多于下调的，可能暗示公司盈利前景改善。
-  **snt1_d1_netrecpercent** ：（分析师给出买入建议的数量 - 分析师给出卖出建议的数量） / 所有分析师数量。衡量分析师对公司股票买卖建议的净差值比例，反映了分析师整体的买卖倾向差值。
-  **snt1_d1_nettargetpercent** ：（分析师给出上调目标价建议的数量 - 分析师给出下调目标价建议的数量） / 所有分析师数量。表示分析师对公司股价目标调整的净方向和程度，正数意味着更多分析师看好股价上升。
-  **snt1_d1_sellrecpercent** ：分析师给出卖出建议的比例，即（分析师给出卖出建议的数量 / 所有分析师数量）。与买入建议比例相对，反映了分析师对公司股票的卖出倾向。
-  **snt1_d1_stockrank** ：范围为0 - 100，数值高为买入信号，数值低为卖出信号。综合各种因素给出的一个关于股票投资价值的总体排名，方便投资者快速判断股票的吸引力。
-  **snt1_d1_uptargetpercent** ：分析师给出上调目标价建议的比例，即（分析师给出上调目标价建议的数量 / 所有分析师数量）。体现了分析师对公司股价向上调整的预期程度，比例高可能暗示公司股价有上升潜力。*  **Step 2: 关系挖掘** 
 ***直接联系** :
- 这些字段大多围绕公司的盈利预期、市场情绪以及分析师对公司股票的看法展开，都服务于对公司投资价值和市场预期的分析框架。
- 如 `snt1_d1_buyrecpercent` 、 `snt1_d1_sellrecpercent` 、 `snt1_d1_netrecpercent` 都基于分析师的买卖建议数量计算，相互关联，从不同角度反映分析师的买卖倾向。
-  `snt1_d1_earningsrevision` 、 `snt1_d1_earningssurprise` 、 `snt1_d1_earningstorpedo` 都与盈利数据相关，分别从盈利预测变化、实际与预期盈利差异、预期与上期实际盈利比较等方面反映公司盈利情况。*  **间接联系/洞察** :
- 结合 `snt1_cored1_score` （市场情绪分数）与 `snt1_d1_analystcoverage` （分析师覆盖数量），可以反映市场情绪与专业关注度之间的关系。例如，高分析师覆盖下的看跌情绪，可能预示着公司存在潜在问题。
-  `snt1_d1_buyrecpercent` 、 `snt1_d1_sellrecpercent` 与 `snt1_d1_earningssurprise` 组合，能评估分析师的买卖建议与公司实际盈利惊喜之间的关联，判断分析师建议的准确性和前瞻性，进而反映公司盈利能力质量。
- 综合 `snt1_d1_longtermepsgrowthest` （长期盈利增长预期）、 `snt1_d1_earningsrevision` （短期盈利预测变化）和 `snt1_d1_dtstsespe` （分析师预测离散度），可以从长期和短期、确定性和不确定性等多个维度评估公司的投资强度和财务健康度。长期盈利增长预期高且短期盈利预测稳定上调、分析师预测离散度低的公司，可能具有较强的投资吸引力和财务稳定性。

 ***Step 3: 特征工程方案 (核心)***

- **方案 1: analyst_bias_score**
  - **计算:**   `(snt1_d1_buyrecpercent - snt1_d1_sellrecpercent) * snt1_d1_analystcoverage`
  - **意义解释:**  该指标综合考虑了分析师的买入和卖出倾向以及分析师覆盖数量。买入倾向与卖出倾向的差值体现了分析师观点的偏向程度，再乘以分析师覆盖数量，可衡量这种偏向在整体分析师关注中的影响力。若值为正且较大，说明分析师整体更倾向于买入且关注程度高，对公司股价有积极影响；若值为负且较大，则相反。它能捕捉分析师观点对公司股价影响的强度维度。
  - **(可选) 数据处理/相关性:**  数值型特征，建议进行标准化处理，可能与 snt1_d1_stockrank 强正相关，因为分析师的净推荐倾向和关注程度对股票综合评级有重要影响。
  - **(可选) 预测提示:**  潜在用于预测股价波动，分析师观点偏向及关注程度对股价走势有重要指引作用。
  - **(可选) 外部知识参考:**  参考分析师推荐对股价影响的金融研究，搜索关键词“analyst recommendations and stock price movement”。

- **方案 2: earnings_surprise_impact**
  - **计算:**   `snt1_d1_earningssurprise * snt1_d1_cored1_score`
  - **意义解释:**  这个特征结合了公司实际收益与预期的差异以及市场情绪得分。当实际收益超出预期且市场情绪为看涨时，该值会较大，表明公司业绩超出预期对市场情绪的正向影响较大，反之亦然。它能捕捉公司业绩超出预期对市场情绪的影响维度，反映公司盈利能力变化对市场预期的触动程度。
  - **(可选) 数据处理/相关性:**  数值型特征，可能需要进行缩放，预期与  `snt1_d1_stockrank`  正相关，因为业绩超出预期且市场情绪好通常会提升股票综合评级。
  - **(可选) 预测提示:**  可用于预测公司盈利能力变化对市场预期的影响，进而对股价波动和企业风险评分可能有预测力。
  - **(可选) 外部知识参考:**  参考收益惊喜与市场反应的金融理论，搜索关键词“earnings surprise and market reaction”。
- **方案 3: target_adjustment_ratio**
  - **计算:**   `snt1_d1_uptargetpercent / snt1_d1_downtargetpercent`
  - **意义解释:**  该指标衡量了上调目标价比例与下调目标价比例的相对关系。若值大于1，说明上调目标价的分析师比例高于下调的，市场对公司股价上行预期更强；反之则下行预期更强。它能捕捉分析师对公司股价目标调整的方向和程度维度，反映市场对公司股价预期的变化趋势。
  - **(可选) 数据处理/相关性:**  比例型特征，建议进行缩放，可能与  `snt1_d1_stockrank`  正相关，因为上调目标价比例相对高通常意味着股票综合评级可能较高。
  - **(可选) 预测提示:**  潜在用于预测股价波动，分析师对目标价的调整方向和程度对股价走势有重要影响。
  - **(可选) 外部知识参考:**  参考目标价调整与股价关系的金融研究，搜索关键词“target price adjustment and stock price”。
- **方案 4: net_earnings_revision_strength**
  - **计算:**   `snt1_d1_netearningsrevision * snt1_d1_analystcoverage`
  - **意义解释:**  综合考虑了分析师对收益预期调整的净方向和程度以及分析师覆盖数量。净收益预期调整比例乘以分析师覆盖数量，反映了这种调整在整体分析师关注中的影响力。若值为正且较大，说明分析师整体更倾向于上调收益预期且关注程度高，对公司未来盈利预期较乐观；若值为负且较大，则相反。它能捕捉分析师对公司盈利预期调整的强度维度。
  - **(可选) 数据处理/相关性:**  数值型特征，建议进行标准化处理，可能与  `snt1_d1_longtermepsgrowthest`  正相关，因为分析师对盈利预期的积极调整可能与公司长期盈利增长预期相关。
  - **(可选) 预测提示:**  可用于预测公司盈利能力变化，分析师对盈利预期的调整对公司未来盈利情况有一定预示作用。
  - **(可选) 外部知识参考:**  参考分析师盈利预期调整与公司盈利关系的金融研究，搜索关键词“analyst earnings revision and company profitability”。
- **方案 5: sentiment_stability_score**
  - **计算:**   `1 / snt1_d1_dtstsespe * snt1_d1_cored1_score`
  - **意义解释:**  该指标结合了分析师收益估计的离散程度和市场情绪得分。分析师收益估计离散程度的倒数乘以市场情绪得分，离散程度越低（即分析师观点越一致）且市场情绪得分越高，该值越大，说明市场情绪越稳定且偏向积极。它能捕捉市场情绪的稳定性维度，反映市场对公司看法的一致性和方向。
  - **(可选) 数据处理/相关性:**  数值型特征，可能需要进行缩放，预期与  `snt1_d1_stockrank`  正相关，因为市场情绪稳定且积极通常对股票综合评级有正向影响。
  - **(可选) 预测提示:**  潜在用于评估企业风险评分，市场情绪稳定与否对企业面临的市场风险有影响。
  - **(可选) 外部知识参考:**  参考市场情绪稳定性与企业风险关系的金融研究，搜索关键词“market sentiment stability and corporate risk”。
- **方案 6: long_term_vs_short_term_earnings**
  - **计算:**   `snt1_d1_longtermepsgrowthest / snt1_d1_earningsrevision`
  - **意义解释:**  此特征对比了公司长期盈利增长预期与短期收益估计变化的关系。若值较大，说明长期盈利增长预期相对短期收益估计变化更为乐观，公司可能具有较好的长期发展潜力但短期波动可能较大；反之则可能短期表现相对稳定但长期增长潜力有限。它能捕捉公司盈利预期的长短期平衡维度，帮助分析公司盈利增长的可持续性和稳定性。
  - **(可选) 数据处理/相关性:**  比例型特征，建议进行缩放，可能与  `snt1_d1_earningstorpedo`  有一定相关性，因为它们都涉及到公司不同时期收益预期的变化。
  - **(可选) 预测提示:**  可用于预测公司盈利能力的可持续性和稳定性，对企业风险评分和盈利能力变化有潜在预测力。
  - **(可选) 外部知识参考:**  参考公司盈利预期长短期关系的金融研究，搜索关键词“long - term vs short - term earnings expectations”。
- **方案 7: buy_sell_balance_index**
  - **计算:**   `(snt1_d1_buyrecpercent + snt1_d1_uptargetpercent) - (snt1_d1_sellrecpercent + snt1_d1_downtargetpercent)`
  - **意义解释:**  该指标综合了分析师的买入、上调目标价倾向与卖出、下调目标价倾向。值为正表示买入和上调目标价的综合倾向更强，值为负则相反。它能捕捉分析师对公司股票买卖和目标价调整的综合平衡维度，反映市场对公司股价的整体预期方向。
  - **(可选) 数据处理/相关性:**  数值型特征，建议进行标准化处理，可能与  `snt1_d1_stockrank`  强正相关，因为该指标综合反映了市场对公司股价的预期方向，与股票综合评级密切相关。
  - **(可选) 预测提示:**  潜在用于预测股价波动，分析师对公司股价的整体预期方向对股价走势有重要影响。
  - **(可选) 外部知识参考:**  参考分析师买卖和目标价调整对股价影响的金融研究，搜索关键词“analyst buy - sell and target price adjustment on stock price”。
- **方案 8: earnings_surprise_magnitude**
  - **计算:**   `abs(snt1_d1_earningssurprise) * snt1_d1_analystcoverage`
  - **意义解释:**  此特征考虑了收益惊喜的绝对值和分析师覆盖数量。收益惊喜绝对值乘以分析师覆盖数量，反映了收益惊喜在整体分析师关注中的影响力大小。绝对值越大且分析师覆盖越多，说明收益惊喜对市场的影响越大。它能捕捉收益惊喜对市场影响的强度维度，体现公司实际业绩与预期差异对市场的触动程度。
  - **(可选) 数据处理/相关性:**  数值型特征，建议进行标准化处理，可能与  `snt1_d1_cored1_score`  有一定相关性，因为收益惊喜对市场情绪可能产生影响。
  - **(可选) 预测提示:**  可用于预测公司业绩变化对市场的影响，进而对股价波动和企业风险评分可能有预测力。
  - **(可选) 外部知识参考:**  参考收益惊喜与市场影响关系的金融研究，搜索关键词“earnings surprise and market impact”。
- **方案 9: dynamic_fundamental_correlation**
  - **计算:**   `correlation(snt1_d1_dynamicfocusrank, snt1_d1_fundamentalfocusrank)`
  - **意义解释:**  通过计算动态交易信号指标和基本面投资信号指标的相关性，衡量市场短期交易信号与基本面投资信号的一致性程度。若相关性高，说明短期交易行为与基于基本面的投资观点较为一致；反之则可能存在分歧。它能捕捉市场交易行为与基本面分析的契合度维度，帮助分析市场投资决策的一致性。
  - **(可选) 数据处理/相关性:**  数值型特征，范围在[-1, 1]，无需额外标准化，与  `snt1_d1_stockrank`  可能有一定相关性，因为股票综合评级可能受到交易信号与基本面信号一致性的影响。
  - **(可选) 预测提示:**  潜在用于评估市场投资决策的稳定性，对股价波动和企业风险评分有一定预测力。
  - **(可选) 外部知识参考:**  参考交易信号与基本面分析关系的金融研究，搜索关键词“trading signals and fundamental analysis correlation”。
- **方案 10: sentiment_earnings_combined_rank**
  - **计算:**   `rank((snt1_d1_cored1_score + snt1_d1_earningssurprise) / 2)`
  - **意义解释:**  该指标先将市场情绪得分与收益惊喜进行平均，再进行排序。综合考虑了市场情绪和公司实际业绩与预期的差异，通过排序反映公司在市场中的相对表现。排名越高，说明公司在市场情绪和实际业绩方面表现越好。

***Step 4: 外部资源整合说明 (总结)*** 在思考过程中，主动考虑并引用了金融市场情绪分析、投资决策中分析师意见一致性、市场情绪与公司盈利关系、企业盈利增长可持续性、股价目标调整与股价波动关系以及金融市场情绪平衡分析等相关概念。搜索关键词包括“analyst consensus and stock price movement”、“market sentiment and earnings surprise correlation”、“sustainable earnings growth analysis”、“stock price target adjustment and stock price volatility”、“financial market sentiment balance analysis”，这些外部知识为特征工程方案的设计提供了理论支持和实践参考，使新特征能够更准确地反映公司运营、投资效率和现金流状况等多方面信息，增强预测模型的解释性和预测力。

---

## 讨论与评论 (20)

### 评论 #1 (作者: YY58435, 时间: 1 year ago)

这个不错啊，主信号都给出来了。用123阶跑跑看。

---

### 评论 #2 (作者: FG26814, 时间: 1 year ago)

感谢 分享，我也正在探索中，我是用操作符组合出来一些，但是意义都不强， 
看了大佬的分享受到启发， 是不是先对数据字段进行一些经济意义的探索， 有信号后再进行操作符的组合？ 

我之前生成的一些组合，请大家品鉴品鉴。

# 行为经济学Alpha模板

self.templates = {

# 1. 过度反应假说 - 均值回归

'overreaction_mean_reversion': {

'template': 'group_rank(reverse(ts_zscore({field}, 20)), sector)',

'theory': '过度反应假说',

'logic': '极端情绪后的均值回归'

},

# 2. 锚定偏差 - 历史偏离

'anchoring_deviation': {

'template': 'rank(subtract({field}, ts_mean({field}, 252)))',

'theory': '锚定偏差理论',

'logic': '当前值与历史均值的偏离'

},

# 3. 羊群效应 - 极端共识反转

'herding_contrarian': {

'template': 'group_neutralize(if_else({field} > 0.8, reverse(ts_zscore({field}, 60)), 0), sector)',

'theory': '羊群效应理论',

'logic': '极端共识后的反转'

},

# 4. 注意力偏差 - 关注度不匹配

'attention_mismatch': {

'template': 'group_rank(divide(ts_zscore({field}, 60), add(log(snt1_d1_analystcoverage), 1)), industry)',

'theory': '注意力偏差理论',

'logic': '高关注度低覆盖度的机会'

},

# 5. 保守偏差 - 修正延续性

'conservative_momentum': {

'template': 'rank(ts_mean(ts_delta({field}, 5), 21))',

'theory': '保守偏差理论',

'logic': '分析师修正的延续性'

},

# 6. 确认偏差 - 信号一致性

'confirmation_consistency': {

'template': 'group_rank(ts_corr({field}, snt1_d1_fundamentalfocusrank, 30), industry)',

'theory': '确认偏差理论',

'logic': '多信号一致性确认'

},

# 7. 代表性偏差 - 模式外推

'representativeness_pattern': {

'template': 'group_neutralize(ts_regression({field}, snt1_d1_earningstorpedo, 60), sector)',

'theory': '代表性偏差理论',

'logic': '基于历史模式的外推'

},

# 8. 多因子综合 - 加权融合

'multi_factor_weighted': {

'template': 'group_normalize(add(multiply(ts_zscore({field}, 60), 0.6), multiply(ts_zscore(snt1_d1_fundamentalfocusrank, 60), 0.4)), sector)',

'theory': '多因子模型理论',

'logic': '多维信息加权融合'

},

# 9. 稳健统计 - 中位数基础

'robust_median': {

'template': 'group_rank(ts_median(winsorize({field}, std=2.5), 45), industry)',

'theory': '稳健统计理论',

'logic': '基于中位数的稳健估计'

},

# 10. 动量反转 - 短期动量

'momentum_short_term': {

'template': 'scale(ts_mean(ts_delta({field}, 1), 10))',

'theory': '动量理论',

'logic': '短期动量效应'

}

}

---

### 评论 #3 (作者: WL13229, 时间: 1 year ago)

很多人在评论区评论，但是都还没有人真的打开LAB看看数据

---

### 评论 #4 (作者: TC20311, 时间: 1 year ago)

correlation(snt1_d1_dynamicfocusrank, snt1_d1_fundamentalfocusrank)
这个可以当作价值回归的判断手段，当情绪背离时可以稍微避开一些

我试了最简单的

-returns 是一开始学习的第一个alpha

改成
a=ts_corr(snt1_d1_dynamicfocusrank, snt1_d1_fundamentalfocusrank,7);

trade_when(a>0.5,-returns,0)

情况会好的很多
换了下天数好像60天不错 总之这是个特别好的开仓指标 我是这么觉得 抛砖引玉了

---

### 评论 #5 (作者: WL13229, 时间: 1 year ago)

for idea 1:


> [!NOTE] [图片 OCR 识别内容]
> Sntl
> buyrecpercent
> IE6
> Sntl
> J1 sellrecpercent
> Sntl
> dI_analystcoverage
> 12
> 200000
> 120000
> 1.0
> 100000
> 150000
> 80000
> 
> 100000
> 
> 
> 60000
> 40000
> 50000
> 20000
> 100
> 120
> 140
> 160
> 100
> Values
> Values
> Values



> [!NOTE] [图片 OCR 识别内容]
> 3]
> 7177
> ICn
> 0TTC 5
> (datafranes [1)
> Non-NaN and Non-Zero Count
> 1TL(II((LII(L((((((
> (((rr(err(r((((c((r((r(
> 2400
> 11 ( (1 (((14(1 (( |
> ((((|
> (((I((I((1(
> (((1(1(((11((
> 2200
> 2000
> 1800
> Counts
> 薏
> Non-NaN Count
> 1600
> Non-NaN and Non-Zero Count
> 1400
> 1200
> 1000
> ((U(r(((a
> 111((
> 800
> 2020-01
> 2020-05
> 2020-09
> 2021-01
> 2021-05
> 2021-09
> 2022-01
> 2022-05
> 2022-09
> 2023-01
> Date
> PI
> 1(41!
> (o
> Ut[


---

### 评论 #6 (作者: WL13229, 时间: 1 year ago)

idea2:


> [!NOTE] [图片 OCR 识别内容]
> le6
> sntl 41
> earningssurprise
> sntl coredl
> SCOre
> 160000
> 175
> 140000
> 1.50
> 120000
> 1.25
> IOOOOO
> 
> 100
> 
> 80000
> 0.75
> 60000
> 0.50
> 40000
> 0.25
> 20000
> 0.00
> 一400
> -200
> 200
> 400
> 600
> 800
> -20
> 一10
> Values
> Values



> [!NOTE] [图片 OCR 识别内容]
> Non-NaN and Non-Zero Count
> Counts
> N(I((IIUI((((((
> Non NaN Count
> TI(t((I(((IC(UI(((
> 2500
> Non NaNand Non Zero Count
> vectcfl(c(Cuuettrefrtre
> (((I((
> CII
> 1((((((1((1((1((1((1 ( (
> (r
> 2475
> 1!4(1(11114
> TCITCC
> 2450
> 
> 2425
> 2400
> (((((((
> 1 ((1 ((1 (((11(1 ((1 ((1 ((1 (
> 2375
> ((I (1(((1((
> Ohurrrar
> ((I((I(
> III(I(
> 2350
> 41(($
> 2020-01
> 2020-05
> 2020-09
> 2021-01
> 2021-05
> 2021-09
> 2022-01
> 2022-05
> 2022-09
> 2023-01
> Date
> Crr
> Or(
> MIII(
> tiusir
> Vg(lk


---

### 评论 #7 (作者: LL87164, 时间: 1 year ago)

Lab 中查看一个字段  *-  **snt1_cored1_score** ：*

数据分布显示为[ -15, 15 ]（Lab 自带函数 visulizations.plot_values_distribution）


> [!NOTE] [图片 OCR 识别内容]
> sntl
> coredl
> sCore Values distribution
> 100000
> 80000
> 
> 60000
> 40000
> 20000
> 15
> 一10
> -5
> 5
> 10
> 15
> 20
> Values


更新频率（自己写的一个函数）：基本为周更新


> [!NOTE] [图片 OCR 识别内容]
> Update Frequency of Datafeld Value
> Metncs
> Updaze Interal(days)
> 20
> 18
> 16
> 
> 1
> 
> 8
> 12
> 10
> 202101
> 202104
> 202107
> 202110
> 202201
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Dale Ol updale


检查缺失值（Lab 自带函数 visulizations.plot_instruments_values）： 22 年 7 月之后比较平稳


> [!NOTE] [图片 OCR 识别内容]
> AlI Instruments
> Instruments
> E00010630100002000
> 10.0
> 7.5
> 5.0
> 2.5
> 
> 0.0
> 一2.5
> 一5,0
> 一7.5
> 2021-01
> 2021-04
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01


---

### 评论 #8 (作者: WL13229, 时间: 1 year ago)

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

这个看更新频率的函数很好。可否分享，代码或者思路都可以

---

### 评论 #9 (作者: WL13229, 时间: 1 year ago)

[TC20311](/hc/en-us/profiles/31484220422423-TC20311)

思路是对的，但是做法不好。还没有检查

snt1_d1_dynamicfocusrank和snt1_d1_fundamentalfocusrank的数据情况，就使用

correlation(snt1_d1_dynamicfocusrank, snt1_d1_fundamentalfocusrank)

是很危险的。要结合LAB才能把Alpha做得精彩

---

### 评论 #10 (作者: LL87164, 时间: 1 year ago)

[WL13229](/hc/zh-cn/profiles/12285040305687-WL13229)  多谢 Weijie 老师点评。

以下是最新版本的代码。Lab 里没有留历史版本，只记得最新修订的思路是用数据值实际更新的时点换掉上一个版本中 Index 更新的时点。如：一周内数据值都没有变化，以后面实际变化的时间点为准进行统计。

```
# Data Filed Value Update Frequencydata_field_df.index = pd.to_datetime(data_field_df.index)data_field_df = data_field_df.sort_index()date_to_compare = data_field_df.drop(columns=['date', 'time_diff'], errors='ignore')date_to_compare = date_to_compare.apply(pd.to_numeric, errors='coerce')is_changed = date_to_compare.diff().any(axis=1).fillna(False)updated_df = data_field_df[is_changed].copy()if not updated_df.empty:    updated_df['time_diff'] = updated_df.index.to_series().diff().dt.daysprint("changed df:", len(updated_df))print(updated_df['time_diff'].head())# Displayplt.style.use('default')fig, ax = plt.subplots(figsize=(15,7))if not updated_df.empty:    ax.plot(updated_df.index, updated_df['time_diff'], label='Update Interval(days)', color='#008B8B', marker='o', linestyle='--')else:    ax.text(0.5, 0.5, 'Never changed in the selected period', horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)ax.set_title('Update Frequency of DataField Value', fontsize=12)ax.set_xlabel('Date of update', fontsize=12)ax.set_ylabel('Days between updates', fontsize=12)ax.legend(title='Metrics', fontsize=10)ax.grid(True, linestyle='--', alpha=0.7)plt.tight_layout()plt.show()
```

妥否，请指正。

---

### 评论 #11 (作者: WL13229, 时间: 1 year ago)

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)

漂亮

---

### 评论 #12 (作者: YQ76635, 时间: 1 year ago)

看了老师的文章，觉得特别收益，而且能把我相对薄弱的基础加强，而且，这些数据是我非常喜欢使用的类型。

---

### 评论 #13 (作者: IM49242, 时间: 1 year ago)

idea3:数据的值如下,不需要调整量纲。通过no-nan和no-zero-nan的函数观察，发现0值过多。感觉两个数据相减会比相除更有含义。如何处理0值可能会更好改善该alpha性能 
> [!NOTE] [图片 OCR 识别内容]
> Ie6
> shtl
> OL_uptargetpercent
> Ie6
> Shtl
> dl_downtargetpercent
> 1.0
> 1.0
> 0.8
> 0.6
> 
> 
> 0.2
> 25
> 50^75
> 100
> 125
> 150
> 175
> 200
> 25
> 50
> 75
> 100
> 125
> 150
> 175
> 200
> Values
> Values


---

### 评论 #14 (作者: HX47598, 时间: 1 year ago)

### 方案 4: net_earnings_revision_strength

### 计算: snt1_d1_netearningsrevision * snt1_d1_analystcoverage

首先查看 snt1_d1_netearningsrevision，这个数值理论的上下限应该是100%和-100% （实际值乘以了100），但是有时会出现超过这个范围的数值，应该可以定义为异常，需要处理 。


> [!NOTE] [图片 OCR 识别内容]
> Cy
> Tistazizations
> Dlot_descr-Ptie_stats (df
> Logir
> Ealso
> Descriptive Statistics Line Plot (Excluding
> count )
> StatistIcs
> 300
> mean
> std
> mln
> 25%
> 200
> 50%
> 75%
> ULALA
> Iax
> 100
> 
> 
> 一100
> 一200
> 一300


其次看0值和nan， 显然大部分数值都是0值，这可能是有意义的，但也可能是数据缺失的表现，可先当做nan处理看表现如何。


> [!NOTE] [图片 OCR 识别内容]
> NOI-NaI GTO NOT-CerO COUIC
> 2500
> UII
> UUII
> I(ICIUCI(
> IUI(II(UI(
> (T(ICI
> (I(I(I(
> IUTI(
> UI UIITII(IIIINIIIIe
> 2000
> 1500
> Counts
> 
> Non NaN Count
> Non-NaN and Non-Zero Count
> 1000
> 500
> 202101
> 202104
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Date


顺便看了一下by sector的分布，都还算是比较集中， sector之间没有特别明显的区别。正向极值一般出现在Tech，Industrial，负向的在Basic Materials比较多 - 可能这也反映最近几年的风向，吹高科技的比较多，而传统能源不太被看好。


> [!NOTE] [图片 OCR 识别内容]
> Groups
> Baslc Materlals
> Communications
> Consumer
> Cyclicals
> Consumer Non-Cycllcals
> Diversified
> Energy
> fnanclal
> Government
> Industrial
> 
> Technology
> Utilities
> 
> 2021-01
> 2021-04
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Date


### Simulation尝试1

首先只用snt1_d1_netearningsrevision 字段:

**#1 把极值和0值都当做null处理， backfill**

```
signal = and(snt1_d1_netearningsrevision < 101, snt1_d1_netearningsrevision > -101) ? snt1_d1_netearningsrevision != 0 ? snt1_d1_netearningsrevision: nan : nan;ts_backfill(signal, 66) 
```

> sharpe: 0.39 turnover: 9.27%

**#2 不做任何处理**

```
snt1_d1_netearningsrevision
```

> sharpe: 0.07 turnover: 22.58%

### 加入snt1_d1_analystcoverage

分布上看起来是比较漂亮的，但注意到没有0值？有可能是nan值代表了0 analyst coverage的情况。


> [!NOTE] [图片 OCR 识别内容]
> ValUes
> dustribution
> 80000
> 60000
> 
> 40000
> 20000
> Values


于是查看nan值，两条线是重合的


> [!NOTE] [图片 OCR 识别内容]
> Non-NaN and Non-Zero Count
> 2520
> Counts
> IUI((I
> (OIMOI(UI(IIo
> Non-NaN Count
> UITUUI
> uo((
> Non NaN and Non Zero Count
> UITI(IG
> 2500
> NTIIIIIIIMITIIIIII
> VIIC(
> 2480
> 2460
> 薏
> 2440
> 2420
> 2400
> IIII(III
> 2021-01
> 2021-04
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Date
> qI(AIUe


没有发现需要特别处理的数据值，应该是简单的ts_backfill即可满足要求

值得一提的是by sector的分布：


> [!NOTE] [图片 OCR 识别内容]
> Group-Wise Average Datafields Over Time
> GroUps
> Basic Materials
> Communications
> Consumel
> Cyclicals
> Consumer Non-Cyclicals
> Diversifed
> Energy
> fnanclal
> Government
> Industrial
> 
> Technology
> Utilities
> 
> 2021-01
> 2021-04
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Date


这里每个sector是有明显不同的，反映了不同sector的分析师“热度”；我试着用industry也看了一下，但实在太多了图没法看。

这里的启示是analyst coverage信号一定做sector/industry中性化处理。

### Simulation尝试2

**#3**

将第一步处理的信号直接乘以snt1_d1_analystcoverage

```
signal = and(snt1_d1_netearningsrevision < 101, snt1_d1_netearningsrevision > -101) ? snt1_d1_netearningsrevision != 0 ? snt1_d1_netearningsrevision: nan : nan;ts_backfill(signal, 66) * snt1_d1_analystcoverage
```

> sharpe: 0.36 turnover: 12.01%

这里发现直接乘以snt1_d1_analystcoverage的话，performance是下降了

**#4 对coverage做backfill以及industry中性化**

```
signal = and(snt1_d1_netearningsrevision < 101, snt1_d1_netearningsrevision > -101) ? snt1_d1_netearningsrevision != 0 ? snt1_d1_netearningsrevision: nan : nan;coverage = group_rank(ts_backfill(snt1_d1_analystcoverage, 66), industry);rank(ts_backfill(signal, 66)) * (1+coverage) 
```

> sharpe: 0.52 turnover: 9.29%

这里对signal使用了rank，和group_rank区别不大，但比完全不用要好一些；同时coverage使用group rank by industry或sector差别不大

以上是我初步的分析，可以看到lab对于数据的洞察是非常有用的，甚至可以让废掉的idea起死回生。

对于这个alpha，我也想听听各位有什么继续改进的思路。

---

### 评论 #15 (作者: WL13229, 时间: 1 year ago)

[HX47598](/hc/en-us/profiles/28983508383127-HX47598)  又是非常漂亮，可以看到，不同个sector，走势非常相同，且某些sector一直在某些sector之上。所以neutral可以考虑以industry或者subindustry.

---

### 评论 #16 (作者: WL13229, 时间: 1 year ago)

把每次探索和收到的启发记录下来，以后都能用上

---

### 评论 #17 (作者: LL87164, 时间: 1 year ago)

[HX47598](/hc/en-us/profiles/28983508383127-HX47598)

数据分析和处理思路很受启发。多谢分享！

延展了一下，将 snt1_d1_analystcoverage 按 pv13_hierarchy_min51_f2_sector 分布：


> [!NOTE] [图片 OCR 识别内容]
> Group-wise Average Datafields Over Time
> GroUps
> 40
> 200000000
> 400000000
> 600000000
> 35
> 800000000
> 1000000000
> 30
> 25
> 詈
> 20
> 簋
> 15
> 10
> 5
> 2021-01
> 2021-04
> 2021-07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01


想探讨的问题是：
pv13_hierarchy_min51_f2_sector 分组字段一共也就分 5 组，数据分布却“ **密集成一团** ”。是否说明：正在分析的变量与 pv13_hierarchy_min51_f2_sector 分组字段的 **相关性较弱** 。也就是说，这个分组字段（行业分类）可能无法有效区分目标变量，导致不同组的数据在数值上差异很小，表现为“密集成一团”？

---

### 评论 #18 (作者: WL13229, 时间: 1 year ago)

[LL87164](/hc/en-us/profiles/28834270391959-LL87164)  是这个道理的，所以用这个来分组不太好

---

### 评论 #19 (作者: LL87164, 时间: 1 year ago)

**分析特征工程方案 1: analyst_bias_score**

1. 首先查看单个字段 snt1_d1_buyrecpercent

依次检查其数据的：数值分布、非零非 NaN、极值、缺失值、更新频率、行业分布

**
> [!NOTE] [图片 OCR 识别内容]
> data fled Values distnbution
> 40000
> 35000
> 30000
> 25000
> 
> 20000
> 15000
> 10000
> 5000
> 20
> 40
> 50
> 80
> 100
> Values
**

根据图示，第一直觉是需要先判断 0 是不是异常值，更主要的是，具体到这个字段所在的业务场景下， **到底算不算一个需要被“修正”的异常值？**

**
> [!NOTE] [图片 OCR 识别内容]
> Non-NaN and Non-Zero Count
> IUI(II
> 4I(I4
> IUIIIUIIIII
> VI
> 1100
> 1080
> V0VOMIW
> 1060
> 蒿
> 1040
> 1020
> 1000
> Counts
> Non NaN Count
> 40 (O(M
> Non NaNand Non Zero Count
> 2021-01
> 2021-04
> 2021 07
> 2021-10
> 2022-01
> 2022-04
> 2022-07
> 2022-10
> 2023-01
> Date
**

从图中可以看出同时有 0 和 NaN 存在，说明 0 不是缺失值

**
> [!NOTE] [图片 OCR 识别内容]
> Outlier
> Visualizazions
> Dlot_Jescriotive_Stats (Jata_llezJ_d,
> IEAIsel
> Descriptive Statistics Line Plot (Excluding 'count')
> 160
> Slalislics
> mcan
> sd
> 140
> mn
> 253
> 502
> 120
> 75%
> Mx
> 100
> 鼍
> 80
> 
> 60
> I0
> 20
> 202101
> 20210-
> 202107
> 202110
> 202201
> 2022-04
> 2022 07
> 202210
> 202301
> Date
> 109
**

这个图有值得注意的信息：

- 方差大于均值的一半，说明数据的波动性较大
- 四分位数 25% 与 75% 间隔较大（约 50），说明数据比较分散

基于以上分析，首先想到的是  **ts_decay_exp_window** 来平滑数据。但是回头又一想，这么做对吗？如果建议买入的分析师的百分比这个数字本身就应该波动较大和分散，说明对不同标的，分析师的建议就应该有很大不同。那么这种离散和波动就是正常的，应该是一种有用的信息，而不是异常。如果使用平滑函数来处理，反倒会丢失这种信号。

**
> [!NOTE] [图片 OCR 识别内容]
> AIIInstruments
> Instruments
> EQ0010121600001000
> 40
> 38
> 36
> 34
> 詈
> 32
> 30
> 28
> 26
> 202101
> 202104
> 202107
> 202110
> 202201
> 202204
> 2022.07
> 202210
> 202301
> Date
**

**
> [!NOTE] [图片 OCR 识别内容]
> Update Frequency of Datafield Value
> Melrics
> Update Interval(days)
> 20
> 18
> 16
> 
> 14
> 鲁
> 笞
> 12
> 10
> 202101
> 202104
> 202107
> 202110
> 202201
> 2022.0-
> 202207
> 2022-10
> 202301
> Date of update
**

根据以上两个图示，考虑ts_decay_exp_window的参数，d=45, factor=0.75

**
> [!NOTE] [图片 OCR 识别内容]
> Group-wIse Average Datafelds Over Time
> 100
> Goups
> Basic Materials
> Comhunicazons
> Consumer Cyclicals
> 90
> Consumer Non-Cyclicals
> Dversifed
> Energy
> Hnancial
> 80
> Govemment
> Idustrial
> 
> Technology
> Utilities
> 70
> 訾
> 60
> 50
> 40
> 202101
> 202104
> 202107
> 202110
> 202201
> 202204
> 202207
> 202210
> 202301
> Dte
**

从以上图示不确认是否需要行业中性化

**Insight:**

尽管有大量 0 值存在，但先假设 0 是有意义的，只过滤大于 100 的异常值（21-10～22-01这个时段出现）并回填

```
a = snt1_d1_buyrecpercent > 100 ? nan : snt1_d1_buyrecpercent;ts_backfill(a, 21)
```

**
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Turnover
> 1496
> 129
> 109
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.11
> 1.129
> -0.02
> -0.379
> 12.539
> -6.62%o。
**

结果分析：和不做任何处理相比， **没有变化** ，包括 turnover 的峰值也没有变化。说明直接回填的作用不大，也说明没有缺失值需要回填。

接着把 0 值当做异常值处理，to_nan 后再回填。

```
a = to_nan(snt1_d1_buyrecpercent);ts_backfill(a, 63)
```


> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.32
> 1.249
> -0.09
> -1.109
> 18.05%
> -17.77900


结果分析：Sharpe 和 Fitness 指标均有提升，说明 **应该对 0 值进行处理（这跟 GPT 的建议不一样）** 。但 Turnover 没什么变化（包括峰值，图略），看来换手率的峰值是另有原因。

**是否应该对 0 值进行处理，** 跟 GPT 的建议不一样。GPT 的分析和建议是：

```
1. 证据表明：零值是“常规状态”，而非“异常值”在决定“修正”一个值之前，我们需要极强的证据证明它是“异常”的。但目前我们看到的证据恰恰相反：
```

- ```
  data filed values distribution
  ```
- ```
  Non-NaN and Non-Zero Count
  ```

```
把一个系统最主要、最常见的状态定义为需要修正的“异常”，在统计上是有风险的，可能会导致对数据现实的严重误判。
```

但这跟实际回测后性能指标的提升相左。 **到底哪一个是对的呢** ？

GTP 的回复是： *“这是一个非常棒的反馈，也是量化分析中皇冠上的明珠： **当实证结果（回测）与理论分析似乎相悖时，背后一定隐藏着更深层次的洞见。”***  下面是其进一步的解释，看完发现还是有道理的。

- **零值的含义** ： `buyrecpercent = 0`  可能意味着“当前没有任何分析师覆盖这只股票并给出买入评级”。这可以被解读为  **“信息真空期”** 。
- **回填的合理性** ：在这种“信息真空期”，假设“市场之前的共识（即上一个非零值）仍然有效，直到有新信息进来”，这是一种非常合理且常见的做法。您的 `ts_backfill(a, 63)` 正是在执行这个逻辑。

直接用平滑函数进行处理，观察其性能指标的变化。

```
ts_decay_exp_window(snt1_d1_buyrecpercent,45, factor=0.75)
```


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> TRAIN
> TEST
> IS
> 0S
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.10
> 1.129
> -0.02
> -0.349
> 12.339
> -6.159oo


结果发现：指标没有变化，没有增强信号，当然也没有减弱信号。和直接回填一样，不增不减。

来自和 GPT 的讨论：

- **方法A（处理零值）** ：这是一个  **“事件驱动”**  或  **“问题导向”**  的解决方案。您准确地识别了策略的“阿喀琉斯之踵”——对零值的过度反应。您通过回填，“手术式”地移除了这个特定的问题，相当于告诉策略：“当看到零时，请冷静，维持原来的建议”。因此，性能得到了巨大提升。
- **方法B（平滑处理）** ：这是一个  **“通用降噪”**  的解决方案。它的设计初衷是消除信号中普遍存在的高频随机波动。但您的信号的主要问题并非高频噪音，而是一个特定的、有意义的“零值事件”。所以，用一个通用的降噪工具去处理一个特定的结构性问题，自然是无效的。

进一步做行业中性化（Sector 和 Industry）测试

```
a = to_nan(snt1_d1_buyrecpercent);b = ts_backfill(a, 63);group_neutralize(b, industry)
```

结果分析：指标没有变化，看来尽管行业有差别（某些线始终在另一些线之上），但是这种差别幅度（40～60）没有什么影响。


> [!NOTE] [图片 OCR 识别内容]
> o IS Summary
> Period
> TRAIN
> TEST
> IS
> 0S
> 目
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.32
> 1.249
> -0.09
> -1.109
> 18.049
> -17.76%0。


2. 字段 snt1_d1_sellrecpercent 的情况和 snt1_d1_buyrecpercent 类似。尽管缺失值不太一样，大于 100 的异常值没有，但这两项不影响后续分析，不再赘述和附图。另外，字段 snt1_d1_analystcoverage 在之前另一个评论中也已有分析。

3. 最后对 snt1_d1_sellrecpercent 和 snt1_d1_buyrecpercent 都做 0 值处理，snt1_d1_analystcoverage 做中性化处理，结果如下：

```
a = ts_backfill(to_nan(snt1_d1_buyrecpercent), 63);b = ts_backfill(to_nan(snt1_d1_sellrecpercent), 63);c = ts_backfill(snt1_d1_analystcoverage, 63);group_neutralize((a - b),industry)*group_neutralize(c,industry)
```


> [!NOTE] [图片 OCR 识别内容]
> 叫 IS Summary
> Period
> TRAIN
> TEST
> IS
> 05
> 自
> Single Data Set Alpha
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> -0.36
> 3.029
> -0.13
> -1.739
> 21.269
> -11.479。
 
（注：重点在于数据特征的分析，没有做 reverse 处理）

综上，还需要继续探索。

---

### 评论 #20 (作者: WL13229, 时间: 1 year ago)

数据处理得很好，接着可以试一试简单的一些idea，比如group rank

---

