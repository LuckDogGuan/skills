# 【MCP】Windsurf +Mcp 更便宜更贵的模型一键执行七十二变

- **链接**: https://support.worldquantbrain.com[Commented] 【MCP】Windsurf Mcp 更便宜更贵的模型一键执行七十二变_37214384455063.md
- **作者**: YQ84572
- **发布时间/热度**: 6个月前, 得票: 77

## 帖子正文

自从七十二变出来之后有非常多的idea在我脑子里冒出来，因为平时习惯用的国外的大模型是比较好用的，国外的api调用又太贵了，所以就一直想着如何使用Claude4.5去执行七十二变的流程。方法也很简单，找到mcp 工具app中的transform.py文件丢给ai了解流程，让他总结步骤再用mcp替代，如下图它就会总结出来，然后我会让他分步然后自己微调一下流程。你们也可以根据自己的经验修改一下流程让研究符合自己的方向
 
> [!NOTE] [图片 OCR 识别内容]
> 了解清Atransformer的工作流程。分步骤讲解。然后生成mc工具替代的步骤流程
> Thought for 2s
> Read Transfommerpyand
> Otherfles
> Thought for 35
> 让我继续读取 Transformer:py 的剩余部分。以完整理解工作流程:
> Read Transformerpy #1518-1117
> Thought for 35
> Read Transfommerpy #L1117-1716
> Thought for 35
> Read
> Transformerpy #11716-2193
> Thought for 35
> 现在我已完整理解 Transformerpy 的工作流程。让我为您详细分解井生成 MCP 工具替代方案。
> Transformerpy 工作流程详解及 MCP 工具替代方案
> 原始工作流程分解
> Step 0: 配置收集与认证
> 收集信息:
> 工椟型配置
> {nodel_DBIe 
> 4eI_  H'
> beae_Ur1
> BRAIN平台认证
> (u3e-naIe;
> Pagamora)
> 桉板总结文件路径
> (可选]
> Ipha
> IOP *参数
> (数据字段候选数']
> Step 1:
> 启动BRAIN会话
> python
> atart
> 3e83ion (
> EOST
> /althentiation
> Step 2:
> 获取种子Alpha详情井生咸描述
> ASk
> anything [Ctrl+U
> (〉Code
> Claude Opus 4.5 (Thinking]
 总结出来大概的步骤就是：
1. mcp6_authenticate → 登录
2. mcp6_get_alpha_details(alpha_id="xxx") → 获取种子Alpha
3. mcp6_get_operators() → 获取算子列表供解析使用
4. AI分析种子Alpha，基于模板库生成新模板
5. 对模板中的<data_field/>占位符:
mcp6_get_datafields(search="keyword1") 
mcp6_get_datafields(search="keyword2")
合并结果取Top N
6. AI生成所有组合表达式
7. mcp6_create_multiSim(alpha_expressions=[...]) 批量回测
8. mcp6_get_alpha_details() 获取详细结果进行筛选
然后我就开始给他alpha id让他进行变体,这边这个Windusrf是支持批量并发调用mcp的所以我让他开8个槽快速回测
 
> [!NOTE] [图片 OCR 识别内容]
> VRVOZqWQ ,这个alphaid 开始进行娈体生成。开8个批次同时进行1批8个
> Thought for 5s
> 我来为 Alpha ID
> VRVOZGN?
> 执行娈体生成工作流。首先进行认证井获取种孓Alpha详情。
> MCP Tool: worldquant-brain-platfom
> authenticate
> MCP Tool: worldquant-brain-platfomm
> get_alpha_details
> MCP Tool: worldquant-brain-platfomm
> get_operators
> Thought for 4s
> 种子Alpha详情:
> 表式:
> tg_arg
> Tau (C=
> product [Endl3
> SOC」
> 504],
> 23]
> Sharpe: 1.12,ZY Sharpe: 244, Fitness: 0.95, Margin: 0.003897
> 设置: USA TOP3OO0, delay=1, decay=5, CROWDING
> 现在搜索相关数据字段。生成娈体模板:
> MCP Tool: worldquant-brain-platfom
> get_datafields
> MCP Tool: worldquant-brain-platfom
> get_datafields
> Thought for45
> 现在基于种子Alpha
> aTg_TSk (ts
> Product [Fndl3
> 90C」
> 504].
> 22]
> 设计娈体模板。生成64个表
> 达式井分8批回测:
> 娈体策略:
> 时序卓子娈体: ts_arg_max
> ts_arg_min;ts_rank ts_Zscore
> 2。数据宇段娈体: fnd13 系列高覆盖字段
> 时间窗口娈体:504-252/126,22-42/10
> 4。中性化娈体:添加 group_Zscore
> MCP Tool: worldquant-brain-platform
> Create_multisim
> MCP Tool: worldquant-brain-platfom
> Create_multisim
> MCP Tool: worldquant-brain-platfomm
> Create_multiSim
> MCP Tool: worldquant-brain-platfomm
> Create_multiSim
> MCP Tool: worldquant-brain-platfom
> Create_multisim
> MCP Tool: worldquant-brain-platform
> Create_multisim
> MCP Tool: worldquant-brain-platfomm
> Create_multiSim
> MCP Tool: worldquant-brain-platfomm
> Create_multiSim
 
最后的结果如下，达到了我要交ppac的要求，然后我就提交了，其中是有两个可以提交的 
> [!NOTE] [图片 OCR 识别内容]
> 完全达标Alpha (Sharpe 2 1.2, Fitness 2 1.0, Margin 2 0.0015)
> Alpha ID
> 表《式
> Sharpe
> Fitness
> Margin
> Sharpe
> qMZSBRmV
> 1.23
> 1.09
> 0.00465
> 2.54
> gqQGYxnx
> 1.20
> 1.05
> 0.00386
> 2.52
> 1VSGeMmQ
> 4.19
> 1.06
> 0.00378
> 2.56
 
希望大家也可以多多把mcp用起来，mcp工具和app里面的东西都是值得我们学习的，如今有ai的帮助，学起来真的很快

---

## 讨论与评论 (15)

### 评论 #1 (作者: RL71875, 时间: 6个月前)

感谢大佬分享

---

### 评论 #2 (作者: 顾问 YH25030 (Rank 31), 时间: 6个月前)

谢谢大佬分享。想问一下，你的方法在各个Region的产出效率怎么样。我的MCP在EUR和GLB产出效率还可以，不过在ASI产出效率很低。

---

### 评论 #3 (作者: JC25837, 时间: 6个月前)

那么是不是缘分一道桥也可以这么操作？

给大家分享一下下载cnhkmcp的指令，里面有app包含了七十二变、缘分一道桥等等，最好用的就是用清华镜像链接加在最后面，下载速度飞快！直接复制使用（安装）：pip install cnhkmcp -i  [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)  ；附带上更新的指令（更新cnhkmcp）：pip install --upgrade cnhkmcp -i  [https://pypi.tuna.tsinghua.edu.cn/simple](https://pypi.tuna.tsinghua.edu.cn/simple)

---

### 评论 #4 (作者: ZW16380, 时间: 6个月前)

感谢分享，版本更新太快了，还没来得及消化，已经有新的方案了。

-----------------------------------------------------------------------------

早晨submit好心情，base快乐一整天

-----------------------------------------------------------------------------

---

### 评论 #5 (作者: LL83568, 时间: 6个月前)

谢谢大佬

---

### 评论 #6 (作者: JY56809, 时间: 6个月前)

这样72变就可视化了吧！

---

### 评论 #7 (作者: YZ54944, 时间: 6个月前)

妈耶，我这就去搜集我的种子Alpha！！

==================================================================================
                                                     学习一小步，收益一大步
==================================================================================

---

### 评论 #8 (作者: YQ84572, 时间: 6个月前)

[顾问 YH25030 (Rank 31)](/hc/en-us/profiles/28941108652823-顾问 YH25030 (Rank 31))  ASI是真没招，ASI的japantest太影响出货率了，对原始数据字段要求更严格感觉，我这边也是usa和eur出的多asi基本没做，做了一两天放弃了

---

### 评论 #9 (作者: HC58447, 时间: 6个月前)

这个想法不错。你就是把MCP的流程丢给了AI，让AI进行分步的去走是吧，然后在让AI进行裂变，这个不错，就是这个需要给AI投喂这个基础的知识库不？如果不投喂的话会不会跑乱，另外就是对于不同的数据集你要不要先采集相关的知识呢？我想你得给AI定个圈子，别让他跑远来，我的想法是这样的，不知道你怎么想的？

---

### 评论 #10 (作者: ZW16380, 时间: 6个月前)

==================================================================================
学习一小步，收益一大步，感谢分享！！！！！！！！！！！！！！！！！
==================================================================================
我也觉得你利用 Windsurf 的并发 MCP 槽来加速回测的做法很有启发性。在量化研究中，迭代速度常常是一个瓶颈，能够在不管理基础设施的情况下并行化模拟，是一个真正的优势。你是否尝试过不同的并发级别，或者在同时运行多个模拟时注意到系统稳定性或结果一致性方面的权衡？此外，我想知道你是否将此工作流应用到了除所示示例之外的其他类型的 Alpha 变换，例如集成式模板或多因子组合。

---

### 评论 #11 (作者: YB15978, 时间: 6个月前)

==================================================================================
感谢大佬，截图这个是通过命令行运行的吗，我是在网页端操作的72变，没看到大佬截图的界面呢，只是在网页端看到在运行了，运行的结果却找不到
==================================================================================

---

### 评论 #12 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

楼主出货效率如何，ai变体感觉操作符很多

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #13 (作者: ZF97721, 时间: 5个月前)

小白的疑惑，ASI这么看重JPN，各种robust test，怎么不干脆做JPN的因子，直接用到ASI上去。如果是KOR的问题，干脆把KOR从ASI去掉得了。ASI现在各种test，这是不是回测超慢的原因，现在ASI的回测速度感觉跟GLB不想上下。

---

### 评论 #14 (作者: WC79277, 时间: 5个月前)

可以收集app里的prompt，整合到自己的工作流程

---

### 评论 #15 (作者: HW93328, 时间: 5个月前)

============================HW93328============================

感谢大佬分享，从大佬这篇帖子中学到的就是可以让大模型并发调用mcp，实现和代码一样的大规模回测，之前在我的尝试中，很多时候大模型只能使用单个回测来进行测试，可能就和楼主说的一样，要用一些更加聪明的大模型才能更好的执行任务，继续学习！！

============================HW93328============================

---

