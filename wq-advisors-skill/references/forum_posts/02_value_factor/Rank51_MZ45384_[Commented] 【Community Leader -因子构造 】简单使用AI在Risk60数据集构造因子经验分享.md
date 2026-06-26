# 【Community Leader -因子构造 】简单使用AI在Risk60数据集构造因子经验分享

- **链接**: [Commented] 【Community Leader -因子构造 】简单使用AI在Risk60数据集构造因子经验分享.md
- **作者**: ZZ81992
- **发布时间/热度**: 6个月前, 得票: 24

## 帖子正文

**构造前提** :近段时间参与了几个分享会和研讨会,听很多大佬都分享了使用AI和MCP来构造Alpha,参考了论坛的帖子和分享会上大佬有提过可以选择自己感兴趣的数据集来入手,所以这几天我也选择Risk数据集来进行测试构造因子

**数据集:Risk60** (首选这个的原因是因为数据少且简单易懂,一眼看去就具有金融学意义,而且我在risk数据集没有点塔完成)

```

```

**了解数据集:** 第一反应就觉得利率相关的两个data具有很强的经济学意义 
> [!NOTE] [图片 OCR 识别内容]
> 字段的金融学意义分析
> 宇段
> 核心金词学逻辑
> 对』市场异惫
> 「SkGO_
> crowding
> 行为金荣学-羊群效应:  篌量'#空活动袄黛二程_
> 音C,度反映投咨者观点趋同
> 可导致走 效萃
> C挤交易反转
> ("空抿!度
> 下降
> 创造反转机会。当多数人傲空时。潜在轧空风险上升
> 轧空机会识别
> TSkGO_Iast
> 市场徽观结构-资金成本:  实示发生钓借P成本
> 直接反映儆空的实际资金玉力。}利萃抑制儆空意
> 熟资压力溢价
> [最云成嫩利南
> 影响卡汤供需平。
> 流动性风俭
> TSkGO_Offer
> 信息不对祢-预期定,: 贷方要茹?卒
> 包含其对标钓证券风险钓预期。报价与戒交,的差异反旷市
> 信息不对称港价
> [报|利。
> 场分程。
> 市场预期差异
> rSkGO_datatime
> 时序行为+式
> 市场时序结构:  儆空活动的对阆分布挎~
> 如E内模式  周期等。可捕捉行为靓律_
> [时间数捂
> 活动弼质节奏
> 因子构建的有效性评估
> 优势持征:
> 数据质量优异
> 10030
> 覆盖率:  磅保在全市场范围内钓可用性
> 高Alphas值:  历史表现潜力大
> (如offer字段818个Alphas)
> Vector类型:  支持多维持征提敢
> 2.经济学逻辑坚实
> 壹接关联卖空约束理论
> (Miller。 1977)
> 捕捉行为倚差
> (如兰群效应。过庹反应)
> 反映市场摩擦 (鬲资成本_
> 流动性一
> 增量信息显著
> 与佞统价量
> 基本面因子枵关性低
> -供独特的行为视角和资金面洞察
> 有效因子构造示例
> 基于这些字段
> 可以构造以下几类高效因子:


**Alpha构建:**

1. 将数据和全部操作符丢给AI生成10个alpha(使用少于6个运算符和1-2个数据)


> [!NOTE] [图片 OCR 识别内容]
> 基于您提供竹Vector类型做空数据字段
> (rskGO_crowding。
> rSkGO_last
> TSkGO_offer) 和世坤平台操作符
> 我为您设计了10个具有坚实经济
> 学逻辑的高效Alpha表达式_
> 这些表达式严袼遵徒Vector教据类型处理规范
> 每个表达式使用1-2个数据字段
> 运算符总数56
> 并基于做空
> 市场微观结构理论
> 10个做空数据Alpha表达式 (按综合优先级排序)
> 做空插挤度动量加速因子
> Download
> Cory
> Run
> SFOUP_
> rank(ts_delta(ts_ZsCore(VeC_aVg(rsk6o_Crowding), 20), 5),
> SECtor)
> 经济学逻辑:  做空抿挤度向量平均值208标化值钓58娈化。做空活动加速聚集的股票可能面临更大轧空风险
> (Boehmer等
> 2008)
> 行业内排名控制行业做空偏好_
> 使用ec_avg处理Vector类型数据
> 2.融资利率期限结构因子
> Python
> Download
> Cory
> Run
> SFOUP_
> neutralizz (divide(VEC_aVE(rskGa_offer),
> VE
> aVE(FsKEB_IEst))。 Industry)
> 经济学逻辑:  做空酃资利率报价与最后成交利率的比率。比率>1表明融资成本上升
> 做空压力塔大 (D'Avolio, 2002)
> 行业中性化控爷
> 行业融资成本差异
> 伎用两个Vector宁段的交互
> 做空活动均值回归因子
> Pthon
> Download
> Run
> ts_ZsCOrE (ts_rank(VEC_aVE(rskEO_Crowding), 10),
> 68)
> 经济学逻辑:  做空掘挤度109非名的609标准化值歌反。傲空活动极端掬挤后的均值回归
> (Jones & Lamont, 2002)
> 捕捉轧空机会
> VEC
> avg将Vecto聚合为标量
> 憨资成本娈化质量因子
> Pthon
> Download
> Run
> SrOUP_
> rank(Ts_ir(Ts_celta(vec_aVg(rskGO_Last),
> 3)15)
> Irkst)
> 经济学逻辑
> 最后鹬资利率38娈化的159信息比率。融资成本上升趋势的稳定性和预测能力
> 高信息比率表明做空压力持续
> 使用
> VC_
> ave处理Vector类型
> 5.做空活动分歧度监测因子
> Python
> Copy
> Copy



> [!NOTE] [图片 OCR 识别内容]
> 融资利率相对价值因子
> python
> Download
> Run
> subtraCt (ts_rank(VEC_aVE(rskGO_OffEr),
> 29),
> SFJUP_
> Ian(ts_rank(VEC_avE(rskGO_OTfer),
> 29),
> SECTOI) )
> 经济学逻辑
> 融资利率报价208排名减去行业均值。识别行业内融资成本棺对较高的股票
> 可能面临更大做空压力。使用v2c_av5处瑾
> VETOT
> 7.做空活动-憨资成本协同因子
> python
> Download
> Run
> Corr(ts
> rank(Vec_aVg(rsk6o_Crowding), 10),
> ts_Fank(J_
> aVE(rskGO_OTfer), 10),
> 经济学逻辑
> 做空捅挤度与融资利率报价排名的短期殂关性
> 正桧关表明做空活动与融资成本同步上升
> 做空压力加剧
> (G2czy等
> 2002)
> 使用两个Vector字段。
> 做空活动极端值稳健因子
> Python
> Download
> Cory
> Run
> group_rank(signed_power(ts_delta(VEC_avg(rskGo_crowding), 1),0.5), sector )
> 经济学逻辑
> 做空抿挤度曰变化稳健测度
> 平方根娈换降低极端日娈化的影响
> 捕捉做空活动的温和娈化趋势。
> J
> aVE处理Vector类
> 融资成本标准化动量因子
> Download
> Run
> ZsCOrE (ts_delta(VEC_aVE(rskGB_Iast), 5),
> 23)
> 经济学逻辑
> 最后融资利率5曰变化钓209标准化。融资成本变化的横截面比较
> 识别融资环境边际恶化的股票
> 使Avec_avg处瑾
> Ve-OF
> 10.多维度做空压力综合因子
> Download
> Copy
> Run
> SFOUP_nEUtFEIiZE (
> IUTIpIy (
> ZsCOrE (VEC_aVS(FskES_CrOwdins), 15),
> signed_pOwer(divide(vEC_avg(rskGO_offer)。
> V
> aVg(rsLcg_Iast)),
> 0.3)
> Copy
> Copy
> Python
> Coay
> t_
> Python


2.回测完,经过简单修改AI给的第二个alpha便可以得到提交的alpha.

AI给出的表现不好,由于两个数据都是借贷利率相关的,于是便先想到将相除换成相乘、相加、相减。

最后经过一番运算符和中性化测试后,得到可以提交的最优alpha,且相关性在USA低区下难得的低.


> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (divide
> Vec_aVg(rskGg_offer),
> Vec_avg(rsk6o_last)), industry)
  
> [!NOTE] [图片 OCR 识别内容]
> PASS
> Turnover oT 8.76%
> abOVE CUtOff O 196
> Turnoer 3T8.76%
> below cutoff oT 709.
> Walah:
> Jistributed OVErinsruments
> Sub-universe Sharpe Of 0.14is aboive CUtOff OT0.1。
> Pyramid theme USAIDIIRISK mazches with multiplier of 1.3. Effective Pyramid count for Genius is
> These thEMes match with -he
> followins multjpliers: Scalable ATOM Theme
> 2; USAJDTIRISK Pyramid Theme
> 1.3ThE fina
> thEME multipler
> 2.3,
> 4FAIL
> Of 0.25 is below CUTof of
> Fitness Of0.09is below CutOffof1.
> Mos-illiquid 5035 instruments after cost Sharpe of-0.16 is below CUOff of-0.07 {0.16 orisina
> Unierse Efter COs-Sharpsj
> 2year Sharpe Of-1.14is below Cutcff of 1.58.
> SharO


优化后: 
> [!NOTE] [图片 OCR 识别内容]
> Broup_neutralize (subtract (vec
> aVg (rskGg_offer),
> VeC_aVg(rskGg_last) ), subindustry)



> [!NOTE] [图片 OCR 识别内容]
> 14PASS
> Fitness OT
> abOVE CUOff of1.
> TurnoweroT 12.06%
> abOe CUtOff oT 1%
> TurnoieroT12.06%
> below cutoff oT 7096.
> Walah:is WE
> Jistributed OVErinsruments;
> Sub-uriverse Sharpe Of 1.29 is above CUtOff of 0.58.
> Mos-illiquid 501 instruments after Cost
> Of0.89 1saboire Cutoff of 0.67(1,27 orisina
> uniVerse afzer Cost Sharpe]。
> Self-correlation
> 0.2618 which
> aboVe CUof Of 0.7,orSharpe
> better by
> 00S5 Ormore
> Data OverUss CECk Passed
> Prod correlation 0.4912is belOW CUtOff of 0.7,or Sharpe
> better by
> 0.05
> U 11012
> AIpna submissions
> bElOw GUOta Of
> 2year Sharpe Of 3.77isabove CUOff of 1.58
> Power Poo
> Orrelation
> 1959
> below Cuoff 0.5,
> bEtz=
> by 10.04 ormore。
> PyramidthEME USAIDIIRISK mazches ith multiplierof 1.3
> Effective pyramid count for Genius
> These themes match with -he followins multipliers: Scalable ATOM Theme
> 2; USALDTIRISK Pyramid Theme
> 1.3ThE fnzltheme multipleris 2.3
> SharO
> Sharue


简单总结:我是一个新手顾问,刚刚加入两个月,这个alpha的生成方式可能说不上有多大的参考价值,但是我觉得对于同样是新手迷茫期的顾问,对于我自己有很大的鼓励作用,只要善于发现和利用AI一样也可以生成可以提交且表现不错的alpha.在听了最近的研讨会后,我也要开始善于发现数据的意义,然后继续学习大佬的MCP帖子,继续产出多好的alpha.

最后再附上一个也是同样简单利用AI产出的可以提交的risk70模版


> [!NOTE] [图片 OCR 识别内容]
> Broup_rank(ts_scale (ts_delta
> short
> interest_factor
> SCore, 2
> 168),
> Sector


祝愿国区越来越好,VF多多提高！我也继续加油!大家可以借此延伸,多多讨论！谢谢。

---

## 讨论与评论 (14)

### 评论 #1 (作者: RL71875, 时间: 5个月前)

这优化的效果也太好了，比起大浪淘沙找信号，如何优化alpha也是门必修的学问

---

### 评论 #2 (作者: HG61318, 时间: 5个月前)

感谢分享,一起加油.

ts_scale这个天数设置这么大的吗?
有什么特别的意义呢?

###################################################
摸摸后缀
###################################################

---

### 评论 #3 (作者: 顾问 MZ45384 (Rank 51), 时间: 5个月前)

Wonderful！没想到USA的risk60居然还能跑出相关性这么低的regular alpha，ai推荐的其它idea怎么样？另外大佬用的是什么模型和插件。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 Where there is a will, there is a way.
======================================================================================

---

### 评论 #4 (作者: LJ85703, 时间: 5个月前)

不错的idea,给我不错的启发

---

### 评论 #5 (作者: YQ84572, 时间: 5个月前)

很好的因子构造实践方案，我也曾在risk60尝试过，单字段好像很难出较好的alpha，这次分享对我很有帮助，对rsk60数据集有了更深入的理解，现在就开始尝试

--------------------------------------------------------------------------------------------------------------------

感谢分享，祝vf0.9+

--------------------------------------------------------------------------------------------------------------------

---

### 评论 #6 (作者: JZ74499, 时间: 5个月前)

神了，企图复现倒数第二条表达式时出现一个prod0.58并且fitness更高的结果，把group操作符去掉后fitness还提升了，依然有0.7以下的prod corr
为了回馈社区，在这里借楼补充一点：decay66，truncation0.01是我已经见到两个用这个配置的alpha了，而且必须用这个配置才能出信号

---

### 评论 #7 (作者: YB15978, 时间: 5个月前)

------------------------------------------------------------------------------------------------------

太厉害了，作为新人能有如此思考，又多了一位未来的g master，不但要向老人学习也要向新人学习

--------------------------------------------------------------------------------------------

---

### 评论 #8 (作者: XG98059, 时间: 5个月前)

尝试了一下，没有通过，不过换了个别参数就好了，感谢大佬。

---

### 评论 #9 (作者: LL46807, 时间: 5个月前)

USA用比率或者两个以上的组合可以降低pc 学到了大佬！=================================================================================
Hard work builds and idleness ruins; thorough planning succeeds and haste fails. Aim high to achieve middling results; aim middling and you will fall short.
=================================================================================

---

### 评论 #10 (作者: XW23690, 时间: 5个月前)

比起让AI从零生成alpha表达式，给它运算符和数据集生成合适的模板有时候似乎效果更好。有时候我调用API去生成alpha，容易陷入调参过拟合的循环中。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #11 (作者: JC24357, 时间: 5个月前)

非常感谢分享，佬用ai的思路很不错，学到了~

先让ai充分理解数据集和字段含义，再根据经济学直觉来构造表达式，然后进行批量回测以及alpha的优化，这样一步步来确实会让ai的幻觉少一点，出货更加轻松呢。

======================= (・∀・(・∀・(・∀・*) 保持进步，保持好奇，坚持探索  =============================
=====================================================================================================

---

### 评论 #12 (作者: JQ70858, 时间: 5个月前)

我感觉自己也是这个大概的思路，但是AI给出的表达式总是不太给力，而且似乎自己对优化这块的的能力也不够，每次都只能放弃。看来还是得耐下心多尝试多学习。谢谢分享。

---

### 评论 #13 (作者: XW23690, 时间: 5个月前)

感谢分享，大佬的思路值得学习。我自己现在使用ai提供模板也是同样的思路，先让ai整理分析出数据特点，并根据描述分好类。然后引导ai生成有经济意义，特别是有数学和统计意义的模板。这样做搜索空间减少很多，并且容易出信号，或者作为0阶也是很不错的选择。

---------------------------------------------------------------------------
α≠运气 |α=Edge E [PnL]=∑(E [r_i]×w_i) σ↓→Sharpe↑
Factor=Signal-Noise Backtest→Live→Repeat βNeutral|αMax
Win>Loss|Risk<Reward InSample→OutOfSample
---------------------------------------------------------------------------

---

### 评论 #14 (作者: JX14975, 时间: 5个月前)

很多人对risk70这个数据集的了解还仅限于31个标注了mfm的数据字段,而对risk70在11月新上的数据字段缺乏探索，现在我们知道了楼主在这方面的探索成功的例子。

---

