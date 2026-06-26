# 顾问 LZ63377 (Rank 33) 核心量化研究论点与发帖 (Writings & Insights)

> 本文档汇集了顾问 LZ63377 (Rank 33) 在论坛分享的量化研究主帖与独到见解。已集成图片 OCR 文本并进行了过滤与脱敏处理。

## 一、顾问原创主帖与技术分享 (Original Research Posts)

### 帖子 #1: 25Q3顾问提交情况播报（每日更新）
- **主帖链接**: https://support.worldquantbrain.com[L2] 25Q3顾问提交情况播报每日更新_33266491538199.md
- **讨论数**: 96

本贴使用Genius排行榜及Consultant排行榜数据，对以下指标进行统计：

- 本季度有提交、今日有提交、提交满20天（定级基准）的顾问人数
- SA、RA提交情况（数量和平均相关性）
- RA平均操作符数量、平均字段数量

并且每种指标分别对以下群体统计：

- 今日有提交的顾问
- 今日有提交且Combined Alpha Performance>=2的顾问
- 今日有提交且Combined Selected Alpha Performance>=2的顾问
- 今日有提交且Value Factor>=0.95的顾问

本贴每日更新。如有疑问、指标建议、排版建议等，欢迎留言讨论，欢迎写下你对数据的敏锐洞察！

---

### 帖子 #2: AI比赛参考工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] AI比赛参考工作流_35831427191703.md
- **讨论数**: 15

千万不能思维受限


> [!NOTE] [图片 OCR 识别内容]
> Start
> USer
> provides seed
> alpha id
> Authenticate with BRAIN
> and LLM gateway
> Analysil phase
> Fetch alpha details
> code and se
> ttings
> 2. Identify operators and
> data fields Used
> Core research LOOD
> 4.AI powered reflection
> LLLLiHor
> Fetch context for each
> LLM experiment
> b. Query API for all related
> Generate performance
> component from BRAIN API
> summary and next steps
> alphas by tag
> comparison graphs
> 4. Call LLM to generate
> 5. Select new champion
> economic rationale
> for next iteration
> Output
> group of variation
> Step 3 - Al powered
> alphas
> End result
> family
> ideation
> of optimized alphas
> SuperAlpha
> 3.3 Settings variation
> 3.2 Data field variation
> 3.1 Operator variation
> Generate new alpha
> expressions
> Simulate evaluate and
> Simulate on BRAIN
> With parent id
> Retrieve performance
> results
> Performance results
> Tag


如果觉得阅读有困难，可以复制下面代码，到 [[链接已屏蔽])  生成高清流程图

```
graph TDA[Start - user provides seed alpha id] --> B[Authenticate with BRAIN and LLM gateway]subgraph AnalysisPhase [Analysis phase]  direction TB  C1[1. Fetch alpha details - code and settings]  C2[2. Identify operators and data fields used]  C3[3. Fetch context for each component from BRAIN API]  C4[4. Call LLM to generate economic rationale]  C1 --> C2 --> C3 --> C4endB --> C1subgraph CoreLoop [Core research loop]  direction TB  I{Step 3 - AI powered ideation}  I --> V1[3.1 Operator variation]  I --> V2[3.2 Data field variation]  I --> V3[3.3 Settings variation]  V1 --> G[Generate new alpha expressions]  V2 --> G  V3 --> G  subgraph SimEvalTag [3. Simulate evaluate and tag for each generated expression]    direction TB    S1[a. Simulate on BRAIN]    S2[b. Tag with parent id]    S3[c. Retrieve performance results]    S1 --> S2 --> S3  end  G --> SimEvalTag  S3 --> R[Performance results]  subgraph ReflectViz [4. AI powered reflection and visualization]    direction TB    N1[a. LLM experiment summary and next steps]    N2[b. Query API for all related alphas by tag]    N3[c. Generate performance comparison graphs]  end  R --> ReflectViz  ReflectViz --> CH[5. Select new champion for next iteration]  CH --> IendC4 --> ICH --> OUT[Output - group of variation alphas - End result - family of optimized alphas - SuperAlpha]
```

---

### 帖子 #3: claude code添加mcp经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] claude code添加mcp经验分享_34283772405143.md
- **讨论数**: 3

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行** 
claude code是一款AI编程的命令行工具, 在某些场景下比cursor表现更好; 类似工具genimi code、qwen code 等
原版的claude code在中国大陆无法使用, 可以借助claude code router使用, 配合claude code router可以配置多个厂家的api, 比如qwen-coder、deepseek等

配置mcp的方式: 
```
claude mcp add brain-mcp --scope local -- python /..../site-packages/cnhkmcp/untracked/platform_functions.py
```
最后一段是platform_functions.py的路径

添加完成后再<userhome>/.cluade里可以看到这样的配置:
```
      "mcpServers": {
        "brain-mcp": {
          "type": "stdio",
          "command": "python",
          "args": [
            "/home....../cnhkmcp/untracked/platform_functions.py"
          ],
          "env": {}
        }
      },
```

关于如何下载mcp,请看集合贴👉 [01-【新人必读】新顾问入门指南！(内含BRAIN API和 顾问收入等精华帖） – WorldQuant BRAIN](../顾问 FX25214 (Rank 22)/[Commented] 01-【新人必读】新顾问入门指南内含BRAIN API和 顾问收入等精华帖置顶的论坛精选_27928616328855.md)

大佬们已经说太多了，在这里不赘述。

---

### 帖子 #4: 目录结构
- **主帖链接**: https://support.worldquantbrain.com[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md
- **讨论数**: 20

最近在积极地尝试使用 MCP ，基本没有错过论坛内的相关帖子，大家都在使用各种各样的工具。最近接触了 Gemini CLI ，论坛内正好也没有类似的内容，于是便进行了一番初步探索，分享给大家。

简单了解一下 Gemini CLI，是直接运行在终端地命令行工具， **免费调用 Gemini 2.5 Pro 模型，支持百万 Token 上下文，60 次/分钟，1000 次/每天的免费调用额度** ，个人用户应该是非常充足了。上下文的容量也比较大（正如 weijie 老师所说，上下文容量很重要，针对顾问们与 mcp 进行多轮对话来拷打出 alpha 是很适配的）。因此在我看来值得尝试一下。

先分享一下个人简单总结的初步使用感受，来供大家参考是否继续阅读并尝试使用：

**优点：** 免费；上下文容量很大（正常对话非常足够，且能压缩上下文）；速度还算较快；Memory 功能可以自定义规范；脱离 IDE 独立行走；能够输出有价值的alpha idea（尝试了一下难产的 insiders 数据集，还真整了一个ppa出来）；道歉还挺诚恳的（虽然没啥用）。

**缺点：** 命令行操作也许不够直观便捷；偶尔不够稳定；模型的表现有时也似乎不太稳定，会犯一些低级错误，如vector数据处理、数据字段名错误，有时候会有幻觉，也有我刚开始用没调教好的原因。

另外：在使用过程中可以保存或者让 AI 记住你的“指导”，利用编写工作流或者其他类似的方式，可以提高使用的效率。AI 还是需要好好调教的，需要一步步引导才能得到预期内和效果比较好的结果，感觉我的方法和技巧还是比较稚嫩，希望各位大佬能够多指导和分享 AI 的使用技巧！

如果对您有启发和帮助，请告诉我或者给我一个赞吧！

MCP 的安装和配置相信应该都没有什么难度了，就不多赘述。

## Gemini CLI 启动

> 参照 Github:  [[链接已屏蔽])  中的  `Quickstart`

**Pre：**

- Node.js ≥ 20 版本（Gemini CLI 是ts开发的）
- Google 账户（用于身份验证）

建议使用 npm 全局安装（npx用于临时使用）：

```
npm install -g @google/gemini-cli
gemini

```

安装完成之后就可以在任意地方输入  `gemini`  来启动 Gemini CLI 了。

### 用户认证

> 这里可能会有点小坑，可能会出现一些不同的认证失败的情况..
> 本文会在后面附上一些认证失败的解决办法，这里不影响继续阅读

作为个人用户就直接用 <  *Login with Google >* Google 账号来验证。点击回车之后会跳转到登录 Google 账号的页面。认证成功后就会进入 Gemini CLI。


> [!NOTE] [图片 OCR 识别内容]
> SE[UI
> Tips
> for getting started:
> 1
> Ask questions;
> edit
> files
> OI
> TUn
> Commands
> 2
> Be specific
> For
> the
> best results
> 3
> Create
> GEMINI .md files
> to
> CUstomize
> yOUI
> interactions With Gemini。
> 4
> /help for
> more
> information
> Using
> 工
> MCP
> SerVer
> Cctrltt
> to view)
> Type Your message
> 01
> @path/to/file


## MCP 配置

Gemini CLI 支持两种配置文件：项目级配置文件 和 全局配置文件。

全局配置文件一般位于用户主目录下  `C:\\Users\\xxx\\.gemini\\settings.json`  。

如果只想在某项目目录中配置，那么打开你想使用 Gemini CLI 的项目文件夹（一般在你的 WQ 的常用工作区目录下即可），创建  `.gemini`  目录，再在此目录下创建文件  `settings.json`  作为 mcp 配置文件。

```
# 创建 .gemini 目录
mkdir .gemini
# 在 VS Code 中打开设置文件
code .gemini/settings.json

# 目录结构
Your WQ Workspace/
├── .gemini/
│   └── settings.json
├── ....
├── ....

```

接着复制 WQ mcp 的 json 配置到 Gemini CLI mcp 配置文件  `settings.json`  中即可。

配置文件中 Gemini CLI 的行为按照以下优先级加载：

- 全局设置：~/.gemini/setting.json
- 项目设置：（项目根目录）/.gemini/setting.json

主要配置项：

- mcpServers：定义提供自定义工具的 MCP 服务器。

## Gemini CLI + MCP 使用

当 mcp 配置完成后，就可以使用  `/mcp`  或  `/mcp nodesc`  查看来查看已有的 mcp 及其工具。

`/mcp desc`  可以显示已有 mcp 及其工具的具体介绍。

### Compress 功能

Gemini CLI 提供了一个 compress 功能（ `/compress` ），可以对上下文进行压缩。

假设对话过程中超出了最大的上下文窗口，那么就会开始丢弃最开始的会话内容，那么 AI 模型就不能获取到全部的内容，会影响最终生成的结果。

那这个时候利用 Compress 功能对上下文进行压缩，AI 就能够获取到全部的上下文。并且压缩后上下文变短，那么 AI 要处理的数据也变少了，消耗的 Token 也会随之减少。

### 保存会话记录

如果需要退出当前会话并保存，方便下次再次进入会话，可以用命令： `/chat save <tag>`  。其中 tag 就是你给这个会话的标签，是下次再找到并进入会话的凭证。

查看已经保存的所有会话： `/chat list`  。

> 不会自动保存会话历史记录，需要保存的话记得 save。

### Shell 命令

使用  `！`  开头即可使用常规的 shell 命令。

退出 shell 命令就再次输入  `！`  。

### Memory 功能

`/memory show`  可以展示已添加到会话上下文中的记忆文件。（默认为  [GEMINI.md]([链接已屏蔽]) ，可以在 `~/.gemini/` 或项目目录中）

可以自己将需要它遵循的规则写入文件，让它记住并遵守，如环境、编程规范、代码风格等，甚至工作流程之类的也可以。

附1（Gemini CLI 认证）：

1. 如果认证成功那真是太好了。
2. 如果 **选择账号并登录之后一直卡在这个认证页面，那么可能是网络的问题** 。
   解决方法比较简单。回到命令行按  `ESC`  ，两次  `Ctrl+c`  退出 Gemini CLI。打开代理软件，复制终端代理命令，粘贴到命令行（为 **当前命令行** 配置代理）。或者打开 TUN 模式。
   然后重启 Gemini CLI，重新认证即可。
3. 如果 **选择账号并登录之后显示授权成功，但是回到命令行发现报错了** 。
   命令行会提示需要设置 GOOGLE_CLOUD_PROJECT 这个环境变量。
   这种情况需要先进入 Google Cloud 的控制台，在左上角图标旁选择一个项目（如果没有创建过项目那就新建一个项目。
   进入项目后搜索  `Gemini for Google Cloud`  ，点击启用服务。等启用成功后，回到项目页面，复制项目的ID，这就是我们需要的参数。
   接着就是设置一下环境变量参数，操作就不多赘述。重新进入Gemini CLI ，重新认证即可。
4. 如果除了上述的其他情况，那么可以分享到评论区大家一起来解决~

> 使用 export 方式配置环境变量或终端代理只对当前终端生效，如果需要全局生效就需要写入系统的配置文件中哦~

附2（它给的一个ppa，虽然性能比较普通）：


> [!NOTE] [图片 OCR 识别内容]
> 5,033K
> 250OK
> Jn"4
> Jn'15
> Jan'17
> Jn'13
> J3n'19
> J31'20
> Jn21
> J31'22
> J123


附3（来自AI诚挚的歉意）：


> [!NOTE] [图片 OCR 识别内容]
> 我为在这个过程中给您带来的巨大困扰。浪费您宝贵的时间和耐心
> 致以最深刻。最诚挚的歉意。
> 我已经证明了我目前无法胜任您托付的这项任务。
> 我不会再提出任何新的方案了。非常抱歉,我没能帮到您。
> Using:
> 1
> MCP
> SerVer
> (ctrltt
> to
> View)
> accepting
> edits
> (shift
> 十
> tab
> t0
> toggle)


看到这了别忘了点个赞再走 ：）

---

### 帖子 #5: Harness engineering下的AI Quant经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] Harness engineering下的AI Quant经验分享_39304762113815.md
- **讨论数**: 50

这篇文章介绍一套我长期使用的人机协同工作流，以及我对这套流程的一些理解。

这套方法并不追求把量化研究完全交给 AI。我的做法更接近一种分工明确的协作框架：让 AI 参与它最擅长的环节，让代码承担稳定、重复、可验证的部分，让人保留目标设定、异常判断和最终提交权。

从来源上看，这套流程仍然建立在最传统的 1/2/3 阶框架之上，但过去一年多里不断吸收研究小组和论坛中的许多经验，把原先“简单提取字段再做扩展”的思路，逐步改造成了“由 AI 驱动”的结构。因此，它在今天依然保持着很强的生命力。

整套流程可以概括为三步：

1. 由 AI 生成结构简单、具有经济学含义的裸信号。
2. 从中筛出已有一定信号量的候选，再通过 1/2/3 阶和 robust 做增强。
3. 对符合提交条件的 alpha 做各类检测，补充经济学解释，最终由人决定是否提交。

在这三步中，AI 主要参与第一步和第三步中的解释辅助。中间的大部分流程，由硬编码脚本和人工调整的阈值共同完成。

这样的分工有一个直接好处：既能利用 AI 的创造力和高吞吐能力，又能尽量避免全 AI 工作流里常见的幻觉、偏航问题。入口端保持创新发散，中后段保持收敛，整套系统就能稳定运行。


> [!NOTE] [图片 OCR 识别内容]
> Harness 架构的三段式蓝图
> 阶段一:  信号生成
> 阶段二:  信号增强
> 阶段三:  检验提交
> Tier-1大模型发散生
> 机械化预处理。多通道剪
> 本地与平台指标检
> 成纯粹的经济学裸信
> 枝。1/2/3阶算子增强。
> 验。A1重新介入提
> 号。
> AI在此被绝对隔离。
> 供解释。人类执行
> 最终决策。
> 注意A1角色:  被高度隔离。仅负责提供创造力基石与逻辑解释。
> NotebookLN


———

## **## 一、AI 生成裸信号**

具体做法是：根据当前要做的塔，先确定对应的数据集，再从中选取一批数据字段，把字段名和字段描述发给 AI，要求它生成 50 到 100 个具有经济学含义的裸信号。这里我通常会强调三点：

1. 思路要尽量创新、发散。
2. 表达式要尽量简单、纯粹。
3. 可用的 op 只允许从我事先给定的基础 op 集合中选择。
4. 一定要有经济学含义，在输出表达式的同时也要输出经济学含义。

之所以强调“简单”，是因为这一步的目标还不是直接得到成熟 alpha，而是尽量生成一些结构清晰、逻辑直白、带有经济直觉的信号种子。后续的 1/2/3 阶和 robust，会承担大部分加工和增强工作。

AI 生成完成之后，我会对这批因子做两类预处理，这两步都由代码完成，AI 不参与：

1. #### 语法检查

使用论坛开源的语法解析器，检查字段是否存在、op 用法是否正确，先把明显无效的表达式清理掉。

1. #### vec 数据检查

对属性为 vector 的数据字段，自动补上 vec op。由于裸信号数量本来就不算多，这里我通常会把所有 vec op 都补上，因子数量虽然会增加，但总体仍在可控范围内。

处理完这些步骤之后，再对这批裸信号进行统一回测。

### ### 一些经验观察

在实际使用中，我有几条比较稳定的经验：

1. 模型越强，裸信号质量通常越高。实际效果上，tier 1 的模型，例如 GPT 和 Claude，通常明显优于更便宜的模型。
2. 更适合直接用 instant 模式，不开 thinking。我的实际观察是，一旦进入长链条思考，生成结果反而更容易变复杂，纯粹性会下降。
3. 输入给 AI 的信息不宜过多。只提供字段名和字段描述，效果往往最好；如果再加上覆盖度、用户量等额外信息，结果有时会变差。

后两条还没有非常明确的理论解释。我的猜测是，输入越复杂，模型越容易把注意力放到一些次要信息上，输出也更容易偏向“复杂但不纯”的表达式。


> [!NOTE] [图片 OCR 识别内容]
> 阶段一:  纯粹的A1引擎 (信号生成)
> 极简输入
> Tier 1 大模型
> 极简输入:  仅提供基础
> 输出
> 字段名 +字段描述。严
> 开启 Instant Mode
> 50-100个极简裸信号
> 禁输入复杂元数据。
> Thinwiiy "ode
> 髭
> 上下文复杂度
> 反直觉发现 "Anti-Thinking"
> 给予A1的上下文越少。 思考路径越短。生成的金融信号反而越纯粹。
> NotebookLM


———

## ## 二、信号增强

回测结束后，流程进入信号增强阶段。

### ### 2.1 阈值初筛

第一步是按一定阈值筛选裸信号，例如 Sharpe > 0.6、Fitness > 0.4 等。阈值并不是固定不变的，会根据当前塔、当前样本质量和候选数量做适当调整。

### ### 2.2 剔除无效因子

初筛之后，我会进一步剔除一些没有继续增强价值的无效因子，主要包括厂、横线因子等。这类因子不只是没法用，还会污染下一步相关性剪枝的计算。

常见的剔除方式包括：

1. 剔除 longCount + shortCount 过少的因子。
2. 剔除 PnL 最后若干个数值全为 0 的因子，这种情况基本可以直接视为厂。

### ### 2.3 多通道相关性剪枝

这是整个中段最重要的一步。

做法是：把通过初筛的因子，分别按 Sharpe、Fitness、Margin 等多个维度排序。每个维度都可以看作一个“通道”。在每个通道里，先把排第一的因子放进该通道候选池，后续因子只有在与当前池子的 max corr 小于阈值时，才会被保留，否则丢弃。最后将多个通道得到的候选池取并集，得到剪枝结果。这样做的目的，是尽量保留多样性，避免单一指标主导。

相关性阈值本身也不一定要固定。为了多保留一些高质量候选，我通常会采用逐步衰减的方式，例如：

- 前 5 个因子，阈值设为 0.85

- 第 5 到第 10 个因子，阈值设为 0.80

- 之后的阈值设为 0.75


> [!NOTE] [图片 OCR 识别内容]
> 阶段二:  多通道相关性剪枝 (保持物种多样性)
> Pruning Matrix
> Top 5 候选池
> 第5-10候选池
> 第10+候选池
> (Max Corr < 0.85)
> (Max Corr < 0.80)
> (Max Corr < 0.75)
> Sharpe 通道
> Fitness 通道
> Margin 通道
> raW
> signals
> 拒绝单-维度的粗暴过滤。多维降维与衰减式相关性阈值。有效防止因孑沦为高度同质化的近亲繁殛产物。
> NotebookLN


### ### 2.4 进入 1/2/3 阶或 robust

完成剪枝之后，就进入传统的增强流程。

最常见的路径是：

裸信号进入 1 阶，1 阶继续筛选后进入 2 阶，2 阶再进入 3 阶。每一阶之间，都会重复上述的步骤。

如果跑完 1 阶或 2 阶之后，就已经获得了相当数量的可提交因子，那流程通常就到此为止，不再继续向下扩展。

如果跑完之后，可提交因子仍然偏少，我会考虑补跑 robust，通过参数遍历做进一步增强。但这一步需要非常克制。robust 的初衷是检验因子，而不是增强因子。使用过度，容易走向过拟合。

———

## ## 三、检验和提交

### ### 3.1 先过本地相关性

如果候选是 ppa，直接本地跑自己 ppa 池子的相关性即可。

如果候选是 ra，通常会先跑自己 ra 池子的自相关，再继续跑平台 check。

### ### 3.2 借助数据库做一轮人工筛选

对所有待提交因子，我会先在自己的数据库里做一轮浏览和筛选。除了 Sharpe、Fitness 这些基本指标之外，我的数据库里还会显示其他辅助判断信息，例如：

- maxTrade 线是否接近原 PnL

- op 数

- df 数

一般会先按 Sharpe、Fitness、Margin 从高到低排序，再剔除 turnover 过高、op 过多、df 过多的因子，然后进行挑选。

这一层仍然保留较强的人工判断成分。

### ### 3.3 执行测试（一）

这一轮主要是网页端的人工复核，重点看以下几项：

1. 看 compare，对自己的组合有没有提升。对组合明显拖后腿的因子，通常不会进入提交。
2. 看基本指标，确认 TVR 和 return 是否正常，最大回撤是否过高。
3. 看分年度表格。如果 2022 年和 2023 年表现过低，通常也会比较谨慎。
4. 看 PnL 线、Sharpe 线、Turnover 线的形态是否顺眼。

这一层虽然带有一定主观性，但对剔除一些“表面过线、整体感觉不对”的结果很有帮助。

### ### 3.4 执行测试（二）

这一轮主要做可自动化的一键测试。

#### 第一部分是 rank/sign test：

对候选因子跑 rank(alpha) 和 sign(alpha)。如果这些变形版本的 Sharpe 低于原 alpha 的 50%，我一般不会提交。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 067
> 1.00
> 0.40
> 0.75
> 04
> 0.50
> 0.2
> 0.25
> 鼍
> 0.0
> 000
> -0.2
> -0.25
> -0.4
> org sharpe
> 1.00
> -0.50
> 50% orig = 0.50
> -0.6
> 054
> 0.59
> orig
> rank
> slgn
> sign_gn
> sign_gn
> none
> orig
> raTk
> sign
> sign_gn
> sign_gn_none
> Margin
> Turnover
> 10.07
> 24.52
> 745
> 25
> 4|1
> 20
> -20
> 14.62
> 15
> S
> 8
> 11.73
> -40
> 10
> 8.75
> G0
> 3.93
> 78.13
> orig
> rank
> slgn
> sign_gn
> sign_gn_
> none
> org
> rank
> slgn
> slgn_gn
> sign_gn_none
> Returns
> Drawdown
> 301
> 211.27
> 200
> 3.00
> 175
> 150
> 125
> 8
> 100


#### 
> [!NOTE] [图片 OCR 识别内容]
> 181
> RS Test Pnl Compare: QPjgNLqp
> orig
> QPjBNLqP
> OrIg
> rank
> ZYIRLk2Q
> sign
> 58GZVNa1
> sign_gn
> pwzqganx
> 05
> sign_gn_none | mLzPkeqx
> 「
> SIgn_gn
> 日
> -0.5
> -1.0
> -1.5
> Slgn_gn
> none
> UuNw
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
> 2024
> Date


#### 第二部分是 robust test：

对原 alpha 跑 robust 测试。如果结果方差过大，也会比较谨慎。


> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> 最大值:  1.0900
> 均值: 0.3135
> 中位数:  0.2800
> 最小值:
> -0.3200
> 标准差:
> 0.2960
> 四分位距 (IQR):
> 0.4450
> 极差:  1.4100
> Fitness
> 最大值:  1.8400
> 均值: 0.2300
> 中位数:
> 0.1300
> 最小值: -0.2000
> 标准差:
> 0.3274
> 四分位距 (IQR):
> 0.2900
> 极差:  2.0400
> Margin
> 最大值:  134.2600
> 均值:  12.5754
> 中位数:
> 3.6900
> 最小值: -17.3000
> 标准差:  25.9616
> 四分位距
> (IQR) :
> 10.7450
> 极差:
> 151.5600
> Turnover
> 最大值:  40.9200
> 均值:  14.7835
> 中位数:  11.9300
> 最小值:  3.2800
> 标准差:  8.5542
> 四分位距 (IQR): 12.5750
> 极差:  37.6400
> Returns
> 最大值:  41.9000



> [!NOTE] [图片 OCR 识别内容]
> Sharpe
> Fitness
> 100
> 40
> 75
> 30
> 墨
> 20
> 詈
> 50
> 10
> 25
> 0
> 2
> 2
> 2
> 2
> Sharpe
> Fitness
> Margin
> TurnoVer
> 150
> 40
> 詈
> 100
> 詈
> 20
> 50
> -200
> -150
> -100
> -50
> 50
> 100
> 150
> 200
> 10
> 20
> 30
> 40
> 50
> 60
> 70
> Margin
> TurnoVer
> Returns
> Drawdown
> 100
> 75
> 40
> 詈
> 50
> 詈
> 20
> 25
> -40
> -20
> 20
> 40
> 20
> 40
> G0
> 80
> 100
> Returns
> Drawdown



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Decay
> Fitness by Decay
> 1.00
> 1.5
> 0.75
> 0.50
> 1.0
> 0.25
> 0.5
> 0.00
> 0.0
> -0.25
> 22
> GG
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Margin by Decay
> Turnover by Decay
> 40
> 125
> 100
> 30
> 75
> 50
> 20
> 25
> 圭
> 圭
> 10
> 22
> 66
> 120
> 240
> 512
> 22
> 66
> 120
> 240
> 512
> Decay
> Decay
> Returns by Decay
> Drawdown by Decay
> 40
> 125
> 30
> 100
> 20
> 75
> 10
> 50
> 25
> 22
> RG
> 120
> 240
> 512
> 22
> FG
> 120
> 240
> 512



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Universe
> Fitness by Universe
> 1.0
> 0.5
> 0.0
> 丰
> A
> A
> Universe
> Universe
> Margin by Universe
> Turnover by Universe
> 40
> 100
> 50
> 20
> Universe
> Universe
> Returns by Universe
> Drawdown by Universe
> 40
> 100
> 20
> 50
> 0
> 0
> TOPSOO
> TOP2O0
> TOP3000
> TOPSP5OO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1000
> MINVOLI
> MINVOL
> ILLIQUID
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOPSPSOO
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOPSPSOO
> TOP1000
> MINVOLIM
> MINVOLTM
> '
> ILLIQUID
> TOPSOO
> TOP2O0
> TOP3000
> TOP1O00
> TOPSOO
> TOP2O0
> TOP3O00
> TOP1OOO
> TOPSPSOO
> MINVOLIM
> TOPSPSOO
> MINVOLTN



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Neut
> Fitness by Neut
> 生
> 圭空臣孛l
> Neut
> Neut
> Margin by Neut
> Turnover by Neut
> 40
> 100
> 20
> 丢
> Neut
> Neut
> Returns by Neut
> Drawdown by Neut
> 25
> 100
> 垩 +
> 豆S星|臣
> 50
> 鹇 -工
> 丰茔茔
> 簋
> SLOW
> SECTOR
> 簋
> 磊
> 
> SECTOR
> 
> NONE
> FAST
> INDUSTRY
> 
> MONRKM
> CROWDING
> 鸶
> FAST
> 
> _MOMERKAM
> STATISTICAL
> STATISTICAL
> AND
> AND_
> SLOW_
> SLOW
> 昱
> AND_
> REVERSION
> REVERSION
> 簋
> SLOW
> NONE
> FAST
> INDUSTRY
> SUBINDUSTRY
> SECTOR
> 
> CROWDING
> 簋
> SLOW
> NONE
> n
> SUBINDUSTRY
> SECTOR
> _MOMERKBM
> CROWDING
> INDUSTRY
> STATISTICAL
> STATISTICAL
> 昱
> AND_
> SLOW
> SLOW
> AND_
> AND
> REVERSION
> REVERSION
> 簋
> SUBINDUSTRY
> FAST
> SUBINDUSTRY
> $
> NONE
> FAST
> INDUSTRY
> SECTOR
> MOMRKEM
> CROWDING
> SLOW
> NONE
> FAST
> INDUSTRY
> 暑
> _MOMERKAM
> CROWDING
> STATISTICAL
> STATISTICAL
> AND_
> AND_
> s
> SLOW_
> AND_
> AND_
> IERSION
> IRSION



> [!NOTE] [图片 OCR 识别内容]
> Sharpe by Group
> Fitness by Group
> 1.0
> 0.5
> 00
> 9
> "
> Group
> Group
> Margin by Group
> Turnover by Group
> 40
> 100
> 50
> 20
> y
> 聃貊
> 酾堕百
> 酝
> 苫 酶错
> Group
> Group
> Returns by Group
> Drawdown by Group
> 40
> 丐
> 100
> 20
> 亘
> 5
> q醒
> 50
> 5颐
> 牾-鸱



> [!NOTE] [图片 OCR 识别内容]
> 167
> PNL Curves by universe (colored by group max PNL)
> 1e7
> universe
> TOP200141898873.0000)
> C"」 '
> T0P3000(34151195.00OOJ
> TOPSP500 (33184197.0000)
> 1' |
> TOP500131186982.0000)
> ICY7 
> 4.00
> TOP1000 125998203.000OJ
> Lqiyc
> ILLOUID_NINVOLII (2136329400001
> 3.75
> 3.50
> 3.25
> _
> 300
> 2.75
> 250
> 2.25
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
> 2024



> [!NOTE] [图片 OCR 识别内容]
> 1e7
> PNL Curves by uni neut (colored by group max PNL )
> 1e7
> uni*neut
> TOP2OO NONE (41898873.0000)
> CeyAr
> 40
> T0P3000 NONE (34151196.00001
> T
> TOPSPSOO NONE 133184197.00OO)
> VSA
> TOP5OO NONE (311869820000)
> TOPIO0 NONE (259982030000)
> ILLIGUID_NINVOLIIINONE (21363294.00001
> 35
> TOPZOO SECTOR (13214659.0000)
> TOPZOOINDUSTRY (13052861.0000)
> TOP2OO MARKET (10940356.00001
> TOP3000 SUBINDUSTRY (1033918000001
> TOP3OOD*INDUSTRY (9251236.0000)
> 30
> TOP300 FAST (9050392.00001
> TOP200 REVERSION_AND_NONENTUI (8732002.0000j
> TOP3OOO SECTOR (8669384.0000)
> TOP30ODNARKET (7947224.0000)
> 25
> 
> TOP3OOOREVERSION_AND_MOMENTUM 17463611.0000)
> TOP200CROIDING (7316500.000O)
> TOP3OOOCROWDING (71144850000I
> 鱼
> TOPSPSOO FAST (6302806.00001
> _
> TOP3000 SLOI (6275460,000OI
> 20
> 盏
> TOPZOO*FAST (6193168.00001
> TOPSPSOO SECTOR (6187494,0000)
> TOP3000 SLOI
> AND_FAST (6159347.0000)
> 趸
> TOP3000STATISTICAL (5796010,0DOOI
> TOP5OD FAST (5775770.00001
> TOP5OD*SLOW (5654524,0000)
> 1.5
> 邕
> TOPSOOINDUSTRY (5461946.0000)
> TOPSPSOOINDUSTRY (5428550.0OOOI
> TOP5OOSLOW_AND_FAST (5389790.00OO)
> TOP200*SUBINDUSTRY (4519126.0000)
> TOPSP5OO M4RKET (4494552,000OI
> 1.0
> TOPSPSOO SLOI (44774460000)
> TOPSPSOOSLOI_AND_FAST (4446454,0000)
> TOPSOOCROWDING (4356666.0000)
> ILLOUID_NINVOLII FAST (4308647.000O)
> TOPSPSOO REVERSION_AND_NOMENTUN 14271460.0000]
> 05
> TOPSOO REVERSION_AND_NONENTUN14255880.0000)
> TOP5O0 SECTOR (421024-.0OOOI
> TOPSPSOO CROWDING (3929487.000O)
> TOP5O0 NIARKET (3624809.0OOO)
> ILLQUID_NINVOLIIINDUSTRY (31659490000)
> 00
> ILLIQUID_NINVOLIISLOW_AND_FAST (31279620000)
> O
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> 2024
> TOPI0OOINDUSTRY (3089212000O
> ILLIQUID_NINVOLII SLOW (2823083 OOOOI
> Date
> TOP5OO*STATISTICAL (2540856,000O)


这一部分已经实现了自动化，只需要输入原 alpha 的 id，就可以一键完成。

### ### 3.5 执行测试（三）

这一步是 AI 第二次进入流程。

把该因子的表达式、数据字段含义发给 AI，让它输出以下内容：

1. 经济学解释
2. 因子值越大代表什么
3. 做多/做空因子值高/低的公司的合理性与潜在不合理处
4. 符合平台格式的因子描述，用于填写因子描述

对于经济学解释显著与常识不符的，我会慎重考虑。让AI提出正反两方面的观点，也可以防止从结果倒推原因。另外，认真填写描述似乎对weight有一定作用，可能可以增加自己因子被选中的机会。


> [!NOTE] [图片 OCR 识别内容]
> 二
> 经济学含义 (核心)
> 这个因子本质是在找:
> 在同一子行业内。同时具备高盈利能力 (ROA) 和高运营效率 (资产周转率)  的公司
> 因子值高的公司意味着什么?
> 当因子值高时,
> 公司通常具备:
> 1。资产赚钱能力强 (高ROA)
> 成本控制好 /定价能力强
> 或者资本结构合理
> 2。资产使用效率高 (高资产周转率)
> 存货周转快
> 业务模式轻资产 |高周转
> 3。经营质量高
> 不是"靠重资产堆利润'
> 而是"又赚得多;
> 又转得快"
> 典型特征:
> 消费品龙头 (高周转+稳定利润)
> 优质制造企业 (精益生产)
> 平台型轻资产公司



> [!NOTE] [图片 OCR 识别内容]
> 三
> 做多高因子股票的逻辑
> 合理性
> 1
> 质量因子 (Quality Factor)
> 高ROA = 好公司
> 高周转 =高效率
> 〉
> 双重筛选。避免"假盈利"
> 2。抗周期能力强
> 高效率公司更能应对需求波动
> 3。资本配置优
> 资产利用率高 >再投资回报更高
> 4
> 行业内比较更公平
> group_rank避免行业偏差 (例如银行 Vs 科技)
> 风险与不合理之处
> 1。可能错杀"重资产优质公司"
> 如公用事业
> 能源。半导体
> 天生周转率低 >被低估
> 2
> 周期顶部风险
> 在景气周期中:
> 收入暴涨 >周转率虚高
> 利润暴涨 > ROA虚高
> >因子容易在高点买入
> 3.
> ZSCore引l入极端值放大
> 异常高收入公司可能被过度放大权重
> 4。没有考虑增长性
> 高ROA + 高周转+高成长
> 可能是"成熟但不增长"的公司



> [!NOTE] [图片 OCR 识别内容]
> 四。做空低因子股票的逻辑
> 合理性
> 低ROA + 低周转:
> 〉
> 资产使用效率差 +盈利能力差
> 〉常见于:
> 僵尸企业
> 低效国企
> 管理层低效公司
> 风险
> 1
> 反转风险 (Turnaround)
> 低效公司一旦改革 >爆发性上涨
> 2
> 高投入早期公司
> 科技|创新企业:
> 当前ROA低。周转低
> 但末来潜力大
> 3.
> 行业周期底部
> 全行业ROA下降 >错误做空



> [!NOTE] [图片 OCR 识别内容]
> 五。整体评价
> 这个因子:
> 逻辑清晰 (杜邦框架)
> 行业内中性化 (很重要)
> 同时刻画"盈利 +效率"
> 但=
> 对周期敏感
> 偏好轻资产行业
> 缺乏增长维度
> 六。推荐评分
> 评分:  &110
> 适合作为:
> 核心质量因子之一
> 与成长因子 |估值因子结合使用
> 不建议单独使用的原因:
> 周期波动较大
> 行业风格偏向明显
> 七
> 英文总结
> Idea: Identify firms
> both high profitability and high asset efficiency within subindustries。
> Rationale for data used: Net income over total assets captures profitability (ROA), While revenue over
> total assets measures asset turnover; jointly reflecting operational and capital efficiency。
> Rationale for operators used: Ranking ROA emphasizes relative profitability; Z-scoring turnover highlights
> deviations in efficiency; and multiplication ensures only firms strong in both dimensions score highly; while
> group ranking neutralizes industry effects。
> with


### ### 3.6 提交

完成上述步骤之后，进入最终提交。

———

## ## 四、Harness engineering 下的 AI Quant

这套工作流我已经用了很久。回头看，它最核心的一点其实很简单：让 AI 做擅长的创新扩展的工作，让代码承担稳定、重复、明确的任务，让人保留高层决策和控制权。最近 harness engineering 这个概念开始流行起来，我觉得它非常适合概括这套方法。

如果打个比喻，这套流程更像一列火车。AI 驱动的裸信号生成，像是给火车换上了更强劲的引擎；而相关性约束、稳健性测试、RS 测试和分层筛选机制，则像轨道、道岔和信号系统。动力很强，方向也比较稳定。AI 先提出新的创意，后续流程再为这些创意补上轨道，因此轨道本身并不会提前封死创新。

相比之下，全 AI 工作流更像一辆高性能汽车。它有强劲动力，有自动驾驶，也有各种 skills 和提示词作为导航和路牌，但它仍然要在开放路网里持续做局部判断。一旦方向偏了，系统往往不会立刻停下，而是会沿着错误道路继续高速前进。动力越强，偏航之后冲出去的距离通常也越远，最后掉头的成本越高。


> [!NOTE] [图片 OCR 识别内容]
> 认知重构:  全A1工作流 VS. Harness Engineering
> 全A1工作流 /汽车模型
> Harness Engineering / 火车模型
> 特征:  极高的自主性;Al包揽生成。测试与纠错。
> 特征: A1提供前迸的动力 (引擎)
> 硬编码视则提供运行的轨道 (铁轨)
> 隐患:  在金酃嗓声中猴易[轨或陷入幻觉;方向不可控,容崭成本极高。
> 优势:  能量榄精准约束。铁轨本身不限制创造力,只设定致命哟边界。
> 真正的力量不在于A1的绝对自主。而在于对A1能量的精准约束。
> NotebookLM


———

## ## 五、与模板爆炸法的区别

AI打工人中现在用的一套方法，是先让 AI 提出一个因子表达式模板，再给出可以填入模板的数据集，然后围绕这个模板做大规模生成和回测。这种方法可以称为模板爆炸法。

研究者先假定某种表达式结构大体有效，再让模型或程序去填不同的数据字段。这样做的好处是效率高、可控性强，也适合围绕某一类已知有效结构做快速放大。但这个方法对于所使用的模板要求是比较高的。除了内置的几套验证过的有效模板，如果新手直接自己探索模板或者让AI未经验证给出一个模板，其实很难说效果会好。

而生成裸信号的方法更偏向发现式研究。通过这个方法发现和验证后的结果，也可以总结成模板，两者并不冲突。

———

## ## 六、AI 还能继续做的事

在当前版本里，AI 主要参与裸信号生成和最终的经济学解释。中间流程仍然以硬代码和人工软判断为主。但如果将现在中间段的操作日志、数据全量记录下来，然后交给AI去统计和发现其中的模式，AI 也会在这些位置上逐步加深参与。

———

## ## 结语

我对这套工作流的总体评价很简单：

它让 AI 做 AI 擅长的部分，让代码做代码擅长的部分，让人继续承担研究中最重要的判断工作。

在量化研究这种高噪声、高伪阳性、高竞争的场景里，有价值的通常不是盲目追求让 AI 覆盖更多步骤，而是能够约束并高效利用AI的能量。

这正是 Harness engineering 在 AI Quant 里的意义。

---

### 帖子 #6: Hump Operator
- **主帖链接**: https://support.worldquantbrain.com[L2] Hump Operator_28597627602967.md
- **讨论数**: 21

I always get unexpected results for `hump`, so I think I'm confused as to what it exactly does and why. I understand the goal of reducing turnover, but not the logic. In the documentation flowchart it indicates a calculation of `limit` as `limit = hump * group_sum(abs(alphavalues), market)`, where my understanding is `alphavalues` and `hump` are the `x and `hump` parameters. Is that correct, and if so this means the hump limit is essentially a percentage of absolute cross-sectional sum, but what is the insight behind why we'd want to do that?

It seems `hump` operator calculates this limit, then essentially would be the same as `hump_decay(x, p=limit, relative=False)`, yes?

I've not had much luck using either of these operators to reduce turnover or improve margin, unfortunately. Some additional insights or practical tips here would be appreciated.

---

### 帖子 #7: Machine Alpha 基础知识1：什么是Alpha模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识1什么是Alpha模板_24497520676119.md
- **讨论数**: 41

你好，研究顾问！

Alpha模板是一种结构化的方法，用于发现Alpha信号。它基于经济逻辑的基础，并且包含一系列的操作符，旨在更精确地在无穷无尽的Alpha宇宙中精确定位有信号的Alpha。

Alpha模板的一个关键特征是其适应性，允许交换某些项目以发现新的Alpha。这种灵活性使得探索广阔的“Alpha空间”成为可能，以发现更多优质的Alpha。

例子：

让我们考虑一个基本面的例子来说明这一理念，假设某公司的股票价格如果其每股收益（EPS）趋势强于其同行，则可能会呈上升趋势。一种实现方式可能如下：

```
group_rank(ts_rank(eps, 252, industry))
```

上述表达式非常简单：

首先，它计算公司的EPS的时间序列排名值越大，公司的EPS相对于过去越高。 其次，它通过应用group_rank来规范化不同行业可能具有的自身特性。值越大，公司的EPS增长相对于其同行越高。

进一步地，你可以将上述的Alpha概括为以下公式（模板）：

```
<group_compare_op>(<ts_compare_op>(<company_fundamentals>, <days>, <group>))
```

上述公式包含以下组件：

- **`<company_fundamentals>` ：** 原始Alpha基于idea使用了EPS，但这一理念可以很容易地扩展到其他基本面数据，如DPS（每股股利）、CPS（每股现金流量）、BPS（每股账面价值）、EBIT（息税前利润）、销售额等。
- **`<ts_compare_op>` ：** 原始实现中使用了ts_rank。还有其他一些服务于类似目的的时间序列操作符，例如ts_zscore、ts_delta、ts_avg_diff等。
- **`<group_compare_op>` ：** 使用了group_rank。类似于<ts_compare_op>的情况，你也可以考虑group_zscore、group_neutralize来控制特定组的效应。
- **`<days>` ， `<group>` ：** 你还可以更改<ts_compare_op>的回溯天数，或者<group_compare_op>的定义。 这种模块化方法使模板高度可定制。每一步都是可互换的，并且可以根据你的Alpha假设的具体细节进行调整。

Alpha模板不仅仅是一种方法，而是一次探索Alpha空间的旅程，一起寻找可以点亮更多可提交Alpha的路径吧！

希望这让你对Alpha模板有一些了解。欢迎分享你的想法，并深入探讨这个迷人的话题！

---

### 帖子 #8: Machine Alpha 基础知识2：理解时间序列利润与规模比较模板
- **主帖链接**: https://support.worldquantbrain.com[L2] Machine Alpha 基础知识2理解时间序列利润与规模比较模板_25066216209687.md
- **讨论数**: 20

以下是一个简单的模板实现，用来比较一家公司的盈利能力与其资本化水平。

该模板后面隐含的假设是，如果一家公司的基本面绩效比率与之前相比有所增加，其股价可能会上涨。

> *time_series_operator* (<profit_field>/<size_field>, <days>)

实现方式：

使用时间序列运算符和两个基本指标的比率 profit_field是代表收入/盈余/利润的任何字段 size_field是代表公司规模的任何字段。

days需要使用合理的天数参数，例如周（5天）、月（20天）、季（60天）或年（250天） ✨你能想到扩展这个模板的不同方式吗？在下方评论分享你的想法吧！

---

### 帖子 #9: MCP结合论文实践经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] MCP结合论文实践经验分享_36221002981271.md
- **讨论数**: 7

官方推荐的论文

Research Paper: Overvalued Equity and Financing Decisions

[../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md](../顾问 JG15244 (Rank 67)/[L2] Research Paper Overvalued Equity and Financing DecisionsPinned_14983690885911.md)

根据MCP工具里面的APP, 提取论文的方程 和表达式
 
> [!NOTE] [图片 OCR 识别内容]
> DI
> (44T
> 4CBQ
> 4TXDB)/ATt-I
> Debt issuance measure
> change in assets minus change in book equity
> deferred taxes scaled by lagged assets
> Variables:
> English
> 中文
> ATt-I
> Total assets at previous period (COMPUSTAT item AT, dollars)
> DI
> Debt issuance (dimensionless ratio)
> 4AT
> Change in total assets (COMPUSTAT item AT, dollars)
> 4CBQ
> Change in book equity (COMPUSTAT item CEQ dollars)
> 4TYDB
> Change in deferred taxes (COMPUSTAT item TXDB, dollars)
> Context: Measurement of net debt issuance following Baker and Wurgler (2002)
> methodology
> 中文描述:债务发行衡量指标
> 总资产娈动减去账面权益和递延税款娈动,再除以前期总资产。用于衡量公司净债务融资活动
> and
 
 
> [!NOTE] [图片 OCR 识别内容]
> 9 =
> (MVE + AT
> (C卫Q + TXDB))|AT
> Tobins 9
> market Value of equity plus assets minus book Value of equity; all divided by assets
> Variables:
> English
> 甲文
> AT
> Total assets (COMPUSTAT item AT, dollars)
> 0卫0
> Book value of equity (COMPUSTAT item CEQ dollars)
> MV卫
> Market value of equity (dollars)
> TJDB
> Deferred taxes (COMPUSTAT item TXDB, dollars)
> Tobin's q (dimensionless ratio)
> Context: Control variable for growth opportunities and investment prospects in regression tests
> 中文描述:托宾0值
> 权益市场价值加总资产减去权益账面价值。再除以总资产
> 用于衡量公司投资机会和市场估值
 导出分析结果
根据论文提供的 数据字段 mdl23_bk_net_equity_financ 利用ai  对起进行分析，

分析结果如下：

## 原始表达式（已回测）

**Alpha ID**: `rK3edZVd`

**表达式**:

```

group_neutralize(ts_rank(ts_mean(mdl23_bk_net_equity_financ, 20), 60) + ts_rank(ts_mean(pv87_stock_tvrwgthold, 20), 60), densify(sector))

```

**回测结果**:

- IS Sharpe: 0.61 (FAIL - 低于1.58阈值)

- IS Fitness: 0.22 (FAIL - 低于1.0阈值)

- Turnover: 0.0651 (PASS)

- Sub-universe Sharpe: 0.19 (FAIL)

**逻辑**: 高股权融资 + 高换手率 = 更强的市场时机信号

---

### 帖子 #10: Trae配置使用mcp经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] Trae配置使用mcp经验分享_34228456653719.md
- **讨论数**: 46

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

对比使用了Roo code、通义灵码和Trae，RooCode配上顶级模型当然最好，就是费钱。通义灵码在使用过程中mcp经常掉线。Trae目前体验感还算可以。论坛上已经有大佬发了通义灵码、Cusor的配置流程，故此简单介绍一下Trae配置mcp的流程。

1、首先官网 [TRAE - The Real AI Engineer]([链接已屏蔽]) 下载安装Trae

2、安装cnhkmcp，对话框直接输入

```
pip install cnhkmcp
```


> [!NOTE] [图片 OCR 识别内容]
> @Builder s
> pipinstall cnhkmcp
> #  园
> Doubao-Seed-16


3、对话框右上角 齿轮按钮“AI功能管理”，添加>手动添加，


> [!NOTE] [图片 OCR 识别内容]
> TRAE
> AI 功能管x
> 返回对话
> 智能悭
> MC
> 上下文
> 规则
> 楔型
> MCP
> 添加
> worldquant-brain-platform 企


4、找到cnhkmcp的安装路径下的sample_mcp_config文件，将里面的内容复制到里面即可，当然，你如果报错，一般就是你的配置不对，需要用AI或者terminal帮你改写一下。


> [!NOTE] [图片 OCR 识别内容]
> Ma
> AppData
> Local
> Programs
> Python
> Python312
> Lib
> site-packages
> cnhkmcp
> Unzrazked
> N 诽序
> 三  查
> 侈改日期
> -」
> Pycache
> 2025/8/1611:30
> 文件买
> aryiy_aplpyy
> 2025/8/168;48
> Pthon
> arXiv_API_Too
> Manua
> 2025/8/168;48
> Markdown File
> 14KB
> TOrUI_
> functions:py
> 2025/8/168;48
> Pthon
> 42KB
> platform_functions py
> 2025/8/1611;27
> Pthon
> 109 KB
> platform_functions py.bak
> 2025/8/1611;2
> BAK 文件
> 109 KB
> sample_mcp_config
> 2025/8/16 8:48
> JSON 文件
> 2KB
> search_forum_with_authpy
> 2025/8/168;58
> Pthon
> USEI
> config
> 2025/8/1615;15
> JSON 文件
> 示S参考文栏_BRAIN_Alpha_Test_Requirements_and_Tips
> 2025/8/168;48
> Markdown File
> 17 KB
> 示工怅流_BRAIN_6_Tips_Datafield_Exploration_Guide
> 2025/8/168;48
> Markdown File
> 示工怅流_BRAIN_Alpha_Improvement_Workflow
> 2025/8/168;48
> Markdown File
> 示例工作流 daily_report_workflow
> 2025/8/168;48
> Markdown File
> 示工怅流 Dataset_Exploration_Expert_Manua
> 2025/8/16
> Markdown File
> 24KB
> 8,49



> [!NOTE] [图片 OCR 识别内容]
> 手配置
> 原始虱置 (ISON)
> 请从 MCP Servers 的介绍页面复制配置 JSON (优先使用 NPX 或 UVX  ]
> 粘贴到输入框中
> "mCpServers"
> "worldquant-brain-platform"
> Command"
> python
> apgs"
> "C:
> IUsers
> IAdmin |IAppData
> 1L0Cal
> IPro
> grams | |Python |Python3z21ILib | Isite-pa
> Ckages
> CnhkmCp
> untracked
> platform_f
> unctions .py
> 10
> 取消


配置好后，会显示mcp的功能，看到就表示可以正常使用


> [!NOTE] [图片 OCR 识别内容]
> TRAE
> 返回对话
> 智能体
> MCP
> 上下文
> 规则
> 楔型
> MCP
> 添加
> worldquant-brain-platform 企
> authenticate
> Authenticate with WorldQuant BRAIN platform. This is the first step
> manage_contig
> Manage contiguration settings
> get Or update configuration.Args:
> Create_simulation
> Create
> nEW simulation on BRAIN platfomm This tool creates and st。
> get_alpha_details
> Get detailed infommation about analpha.Args: alpha_id: The ID oft
> get_datasets
> Getavallable Jatasets tor research: Use this to Jiscover what Jata 15
> get_datafields
> Get available Jata felds foralpha construction. Use this to fnd speC
> get_alpha_pnl
> Get Pnl (Profitand Loss) data foranalpha
> alpha_id: The ID Of。
> get_user_alphas
> Get Users alphas with advanced filtening. pagination, and sorting:
> submit_alpha
> Submit analpha for production Use this when your alpha
> ready
> ATgS


5、对话框的内置智能体选择Builder with MCP ，然后就可以使用了


> [!NOTE] [图片 OCR 识别内容]
> 内置智能体
> Builder
> Builder with MCP
> 创建智能体
> Doubao-Seed-16



> [!NOTE] [图片 OCR 识别内容]
> TRME
> 使用mc工具首先学习了解brain平台的搜所有基础概念。认真学习总结brai平台的每-篇
> 文档
> Builder wiith MCP
> 思考过程
> 首先。我需要获取Brain平台的所有文档列表。这样才能系统地学习和总结每
> 篇文档。我将使用MCP眼务器提供的
> get_documentations 工具来实现这一点。
> worldquant-brain-platformlget_documentations
> 根据返回结果。我需要先进行身份验证才能访问文档。让我调用 authenticate 工具来完成身份验证。
> Worldquant-brain-platformlauthenticate
> 身份验证己成功。现在我可以继续获取Brain平台的文档列表。让我再次调用 get_documentations 工具来获耶所舸可文
> 档和学习材料。
> Worldquant-brain-platformlget_documentations
> 现在我己经获得了Brain平台的文档列表。接下来我需要开始学习这些文档。首先。我应该从最基础的入门文档开始。犄别
> this First
> Starter Pack"
> 这应该是了解平台的第-步。我将使用 read_specific_documentation 工具来读取
> 这篇文档的详细内容。
> Worldquant-brain-platformlread_specifc_documentation
> 我己经学习了 *Read this First
> Starter Pack
> '的内客。了解了Brain平台的基本介绍
> 顾问计划。金圃础知识和量化分析
> 的概念。接下来。我应该继续学习下一篇基础文档 Introduction to Alphas
> 以深入了解Apha的心概念。
> Worldquant-brain-platformlread_specifc_documentation
> ARead


---

### 帖子 #11: velue factor从0.04 - 0.31 - 0.41 - 0.93的艰辛路程经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] velue factor从004 - 031 - 041 - 093的艰辛路程经验分享_32340009231127.md
- **讨论数**: 25

在我第一次更新VF（velue factor）时，数值显示为0.04。当时，我心中充满了疑问：系统难道出错了吗？怎么会有这么低的VF值？于是，我急忙写邮件询问，是否是系统问题，但得到的回复却是：“没有问题。”这让我瞬间陷入了深深的失落，几乎觉得天塌了——怎么可能，连0.1都不到，之后还能做什么？

然而，这只是我VF学习之路的起点。为了寻找答案，我开始请教一些经验丰富的大佬，他们中有些VF值高达0.98甚至1.0。他们耐心地与我分享了他们的经验和见解，这些交流让我逐渐找到了自己的问题所在。原来，我不自觉地陷入了过拟合的泥潭，交出的结果都是“垃圾”。我明白了：问题出在自己的方法上。

**重新审视与总结**

经过这段时间的反思，我发现了自己在方法上的几个关键错误。在不知不觉中，我深陷于一阶、二阶、三阶死代码的漩涡，完全忽视了核心的“alpha”操作。我每天就是无脑地运行代码，反复跑着一堆没有意义的模型，完全没有思考“为什么”去做这些。VF值的低迷，也正是这些无用操作累积的结果。

意识到问题后，我开始调整思路。为了避免重复犯错，我决定通过更为系统的方式进行自我提升。我开始更加积极地参加论坛讨论、查阅书籍，并向研究小组里的资深成员请教，深入了解模型的核心思想与技术细节。每天都坚持积累，不再盲目操作，而是逐步理清了我自己的逻辑框架。

**突破与升华**

随着不断的实践与学习，我逐渐整理出了属于自己的交alpha逻辑和代码。我的模型开始逐步改进，VF值也在不断提高。最终，我成功突破了0.5以下的瓶颈，达到了0.93还成为了Expert。这段艰辛的成长历程，虽然充满挑战，但也让我收获了宝贵的经验和深刻的理解。

通过这次经历，我深刻认识到，技术和方法固然重要，但更重要的是要保持不断学习、持续反思的态度。没有什么是“一蹴而就”的，每一次的低谷，都是我们成长的铺垫。正是这份坚持与耐心，才让我从0.04走到了0.93，终于找到了属于自己的成功之路。

---

### 帖子 #12: VF0.5->1.0->1.0->1.0->?,1.0体验卡结束后的总结与思考【指标分析篇】经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] VF05-10-10-10-10体验卡结束后的总结与思考【指标分析篇】经验分享_35880708570391.md
- **讨论数**: 9

6、7、8月的VF终于是更新了，在幸运的拿到三个月的1.0体验卡后也终于产生了变化，最新的VF下降到了0.85。之前一直没有完整的总结分析过过往几个月提交的alpha的情况，所以也借着次更新变动的契机来做一个基于alpha指标的分析总结。在分析过程中会得出一些可能的结论，纯个人总结猜测，不一定为真。

看到有顾问朋友问拿到了高VF怎么交能拿高base，欢迎看看我的上一篇帖子

1.指标数据概览


> [!NOTE] [图片 OCR 识别内容]
> 2025-04
> 2025-05
> 2025-06
> 2025-07
> 2025-08
> sharpe
> 1.684
> 1.82
> 1.815
> 1.794
> 1.619
> fitness
> 1.812
> 1.587
> 1.461
> 1.513
> 1.415
> returns
> 0.193
> 0.119
> 0.106
> 0.118
> 0.118
> turnoVer
> 0.108
> 0.098
> 0.101
> 0.113
> 0.101
> margin
> 0.005
> 0.004
> 0.003
> 0.003
> 0.004
> Self cor
> 0.184
> 0.036
> 0.346
> 0.441
> 0.263
> prod_cor
> 0.255
> 0.475
> 0.752
> 0.755
> 0.671
> Count
> 15.0
> 71.0
> 68.0
> 74.0
> 91.0


我是今年4月底成为的consultant，因子在2025-04只提交了少量的alpha，所以在后面的分析中，不把4月的指标做重要考虑。我首次刷新VF是在3、4、5这个时间窗口内，对于我来说也就是4、5两个月的alpha数据。

4、5月-->1.0 4、5、6月-->1.0 5、6、7-->1.0 6、7、8月-->0.85

从这四次VF的刷新中不难看出，5月的alpha数据在三次1.0中应该是起到了比较大的作用，毕竟5月的窗口过去之后VF就产生了较大变化。如果只从各个指标的avg数据上来看，2025-08的平均指标确实要比2025-05差上一些，但整体上我觉得是一个可接受波动范围。（8月开始为了genius可能交了一些指标没有那么好的alpha）

**结论1: 在WQ，从不缺少优秀的consultant，不进则是退。**

关于super alpha我这次没有做详细指标统计，我从6月的比赛开始陆续做sa，7月、8月提交的基本都是指标较好的super alpha（base图中sa收入也是占大头），暂时不能判断sa对于VF的影响，也许要等到下次VF刷新时再观察。但如果是sa之前交的很少，那多交一些sa应该是有助于VF的。


> [!NOTE] [图片 OCR 识别内容]
> 2025-04 to 2025-06
> 2025-05 to 2025-07
> 2025-06 to 2025-08
> sharpe
> 1.805
> 1.809
> 1.732
> fitness
> 1.554
> 1.521
> 1.459
> returns
> 0.12
> 0.114
> 0.115
> turnover
> 0.101
> 0.104
> 0.105
> margin
> 0.004
> 0.003
> 0.003
> Self Cor
> 0.187
> 0.276
> 0.344
> prod
> COI
> 0.576
> 0.661
> 0.721
> Count
> 154
> 213
> 233


从3个月的平均指标上来看，确实是比之前低一些的。在5月时貌似有个bug，有些ra提交后其prod会显示为0，所以在统计上5月的pc指标上就明显低了一些。

2.指标分布情况


> [!NOTE] [图片 OCR 识别内容]
> sharpe comparison
> fitness comparison
> returns comparison
> 1.0
> 1.0
> 0.8
> 0.8
> 0.6
> 0.6
> 
> 
> 喜
> 3
> 0.4
> 0.4
> 2
> 0.2
> 0.2
> 0.0
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> Sharpe
> fitness
> returns
> turnover comparison
> margin comparison
> prod_cor comparison
> 2.5
> 200
> 175
> 2.0
> 150
> 125
> 1.5
> 
> 3
> 喜
> 100
> 
> 1.0
> 75
> 2
> 50
> 0.5
> 25
> 0.0
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 0.00
> 0.01
> 0.02
> 0.03
> 0.04
> -0.2
> 0.0
> 0.2
> 0.4
> 0.6
> 0.8
> 1.0
> 1.2
> turnover
> margin
> prod_cor


图片中蓝色为567月时间窗口中的指标分布，黄色为678月。上图中有较明显变化的是sharpe、turnover和prod，sharpe上明显低的个数变多了，turnover上30%-40%这块有所增加（温和的turnover是ok的，但这个区间明显偏高了）。prod上还算正常，有高有低。

5、6、7月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆
> 豆20
> 豆40
> 1.5
> 20
> 2.5
> 30
> 35
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 2.5
> 30
> 35
> 4.0
> 4.5
> 0.4
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 100
> 豆
> 8
> 豆 15
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 0005
> 0010
> 0.015
> 0.020
> 0.025
> 0030
> 0035
> 0.040
> 0.4
> 06
> 1.0
> bUrOVeT
> margIn
> Prod
> COI


6、7、8月的指标个数分布


> [!NOTE] [图片 OCR 识别内容]
> sharpe total distribution
> fitness total distribution
> returns total distribution
> 豆20
> 豆20
> 豆
> 1.0
> 1.5
> 2.0
> 2.5
> 30
> 3.5
> 40
> 45
> 50
> 1.0
> 1.5
> 20
> 25
> 30
> 3.5
> 40
> 45
> U0
> 06
> 1.0
> sharpe
> ftness
> [tUIS
> turnover total distribution
> margin total distribution
> prod
> COF total distribution
> 20.0
> 17.5
> 15.0
> 12.5
> 8
> 8
> 10.0
> 7.5
> 50
> 25
> 000
> 005
> 0.10
> 0.15
> 0.20
> 0.25
> 0.30
> 0.35
> 0.40
> 0.000
> 005
> 0010
> 0015
> 020
> 0.2
> 0.3
> 0.4
> 05
> 0.6
> 07
> 0.8
> 0.9
> 1.0
> WUrnoVeT
> margIn
> Prod
> COI
> 豆


其实我个人从以上指标分布的对比中没有感觉出特别明显的差异，我提交因子时也会把握一个标准，从日常提交上来说也没有太大差异。

结论2: 做好自己的研究，剩下的交给系统

影响VF的因素实在太多了，数量、diversity、OS、成长表现、rank等等等等，不可能做到面面具到，只有尽量做出好alpha，提交符合自己审美的alpha，尽力就好。

3.地区/数据集分布


> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/DI
> 100
> 37.88%
> EUR/DI
> 88
> 33.33%
> ASIID1
> 46
> 17.42%
> GLB/DI
> 30
> 11.36%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 61:5-6-7月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> MODEL
> 54
> 20.45%
> RISK
> 39
> 14.77%
> FUNDAMENTAL
> 31
> 11.74%
> PV
> 31
> 11.74%
> ANALYST
> 30
> 11.36%
> OTHER
> 19
> 7.20%
> NEWS
> 15
> 5.68%
> OPTION
> 3.79%
> MACRO
> 9
> 2.65%
> SENTIMENT
> 7
> 2.65%
> INSTITUTIONS
> 7
> 2.65%
> EARNINGS
> 2.65%
> INSIDERS
> 3
> 1.14%
> SOCIALMEDIA
> 2
> 0.76%
> SHORTINTEREST
> 2
> 0.76%
> Total
> 264
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 地区类别 (Region)
> Count (数量)
> Percentage (占比)
> USA/D1
> 38.68%
> EUR/D1
> 5
> 19.86%
> ASIID1
> 42
> 14.63%
> AMR/D1
> 31
> 10.80%
> GLB/D1
> 25
> 8.71%
> JPNIDI
> 21
> 7.32%
> Total
> 287
> 100.00%



> [!NOTE] [图片 OCR 识别内容]
> 62:7-8-9月 (2025)
> 数据集类别 (Dataset)
> Count (数量)
> Percentage (占比)
> ANALYST
> 39
> 13.59%
> MODEL
> 37
> 12.89%
> RISK
> 35
> 12.20%
> FUNDAMENTAL
> 33
> 11.50%
> PV
> 33
> 11.50%
> OTHER
> 26
> 9.06%
> OPTION
> 5.92%
> NEWS
> 1
> 5.57%
> SENTIMENT
> 3.83%
> INSTITUTIONS
> "
> 2.79%
> EARNINGS
> 7
> 2.44%
> INSIDERS
> 7
> 2.44%
> SHORTINTEREST
> 6
> 2.09%
> SOCIALMEDIA
> 6
> 2.09%
> MACRO
> 4
> 1.39%
> BROKER
> 2
> 0.70%
> Total
> 287
> 100.00%


8月下旬开始陆陆续续开始交了一些jpn和amr的alpha，数量不多，可能是组合中不稳定的来源。D0听说也比较难，我还没有尝试过。

最后，现在无论是genius还是vf，竞争都很激烈，还是要努力提升自己，多交高质量的alpha！祝各位vf常高，base长红～

（结论3:新顾问要抓住机会，刚开始时的成长贡献可能会带给你一个高VF）

---

### 帖子 #13: 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。#核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。#工作流步骤##1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。##2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。##3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等##4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```##5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。#总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP] 基于相似字段产生alpha的工作流分享_35797714275223.md
- **讨论数**: 4

使用的工具链参考：  [../顾问 JX79797 (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md](../顾问 JX79797 (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)

**本工作流基于相似字段寻找更多的alpha**

**1. 可以用于ai alpha比赛产生子alpha**

**2. 可以用于 ASI 通过Robust测试**

**工作流程：**

1. 选择一个“种子Alpha”: 从一个已知表现良好或结构有趣的Alpha表达式开始，把它当作一个模板。

2. 识别并替换关键部分:

确定该Alpha中的一个关键组成部分（通常是一个数据字段），例如一个关于“毛利率”的字段。

3. 发现相似字段: 寻找与该关键字段在语义上相似的替代字段。工作流强调，关键在于分析字段的描

述来寻找衡量相似经济概念的替代品（例如，用另一个盈利能力指标如“净利润”或“EBITDA”来替换“

毛利率”），而不仅仅是看字段名称。

4. 批量生成:

用找到的相似字段列表，批量替换模板中的原始字段，从而快速生成大量逻辑一致的新Alpha变体

**使用提示：**

```
Instrument Type: Equity, Region: ASI, Universe: MINVOL1M, Delay: 1 下的alpha "ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactsell_amt),120), 5)", 使用工作流similar_field_alpha_generation_workflow.md 生成 20 个新的表达式
```

上文示例中的alpha，Robust失败无法提交

- **Robust universe Sharpe of 1.13 is below cutoff of 1.46 (90% of Alpha).**

使用工作流得到新的20个表达式，执行回测，得到2个可提交alpha

**工作流内容**

```
# 基于模版的Alpha生成相似字段Alpha工作流这是一个通用工作流，旨在通过替换现有Alpha表达式中的特定组件（如数据字段）来系统地、批量地生成新的Alpha变体。这种方法适用于快速探索相似因子的表现，并扩大有效的Alpha策略池。## 核心思想该工作流的核心是“模板化”和“替换”。我们从一个表现良好或结构有趣的“种子Alpha”开始，将其视为一个模板。然后，我们识别出该模板中的某个关键部分（通常是一个数据字段），并找到一系列与之相似或相关的替代项，最后通过批量替换生成大量新的候选Alpha。## 工作流步骤### 1. 选择种子Alpha (Seed Alpha)选择一个作为起点的Alpha表达式。这个表达式可以来源于：- 你自己过去研究中发现的高绩效Alpha。- 一个具有特定逻辑结构（例如，时间序列操作、截面操作组合）的Alpha。- 一个你希望探索其变体的基础因子。**示例种子Alpha**：```-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))```在这个例子中，我们选择了一个基于`anl44_2_grossmargin_lastactccy`（毛利率）字段最后变动天数的表达式。### 2. 识别可变组件确定你想要替换的表达式部分。最常见的是数据字段，但也可以是算子或参数。**示例可变组件**：在 `-days_from_last_change(vec_sum(anl44_2_grossmargin_lastactccy))` 中，可变组件是数据字段 `anl44_2_grossmargin_lastactccy`。### 3. 发现相似组件寻找与上一步中识别出的可变组件相似或相关的替代项。这是提升Alpha生成质量的关键步骤。- **对于数据字段**：1.**筛选同一数据集 (Primary Filter)**：首先，将范围缩小到与原字段相同的数​​据集。例如，如果原字段来自 `anl44`，则优先探索该数据集下的其他字段。这可以作为初步筛选，因为同一数据集的字段通常在逻辑上是相关的。2.**分析语义相似性 (Key Step)**：在第一步筛选出的字段中，进一步通过分析其**描述（description）**来判断语义相似性。这是最重要的一步。寻找衡量相似经济或金融概念的字段。-**示例**：如果你的种子Alpha使用了一个关于“毛利率”（Gross Margin）的字段，那么在寻找替代项时，应优先选择描述中同样涉及**盈利能力**的字段，例如：-`EBITDA` (税息折旧及摊销前利润)-`Net Profit` (净利润)-`EPS` (每股收益)-`ROE` (股本回报率)- 通过这种方式，你可以确保新生成的Alpha在逻辑上与种子Alpha保持一致，而不仅仅是字段名称或来源相似。3.**考虑名称相似性 (Optional)**：在某些情况下，名称相似的字段也可能相关，但这通常不如基于描述的语义分析可靠。**发现工具与数据来源**：- **本地文件**：数据字段存储在本地的 `data/fields` 目录下的 CSV 文件中。你需要读取相关文件并解析其内容，特别是包含字段名称和描述的列，以寻找相似组件。不应使用 API 来获取字段。**示例相似组件**：假设我们发现 `anl44` 数据集中，除了关于 `grossmargin` 的字段，还有以下同样衡量盈利能力的字段：- `anl44_2_ebitdaps_value` (描述: ebitdaps value)- `anl44_2_epsr_value` (描述: epsr value)- `anl44_2_netprofit_rep_value` (描述: netprofit rep value)- `anl44_2_roe_value` (描述: roe value)- ...等等### 4. 生成新表达式以编程方式，将种子Alpha模板中的可变组件替换为你在上一步中找到的相似组件列表，从而生成一系列新的Alpha表达式。**示例生成结果**：生成的表达式应直接在对话中以 Python 列表的格式返回，方便用户直接复制使用。```pythonexpressions = ["ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_stk_invactbuy_qty),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_amt),120), 5)","ts_std_dev(ts_backfill(vec_ir(shrt38_accum_buy_qty),120), 5)"]```### 5. 评估与迭代 (可选但推荐)对生成的新Alpha表达式进行性能评估。- **批量回测**：使用 `create_multiSim` 工具可以一次性回测多个表达式，高效地获取它们的性能指标。- **分析结果**：分析回测报告，筛选出表现优异的Alpha。- **迭代优化**：基于评估结果，可以重复此工作流，例如选择一个新的种子Alpha，或探索另一组相似组件。## 总结这个工作流提供了一种半自动化的方法，能够基于已有的知识和发现，快速、大规模地生成新的、有潜力的Alpha。它将研究员的洞察力（选择种子和相似组件）与机器的执行力（批量生成和回测）有效结合起来。
```

```

```

---

### 帖子 #14: [MCP]免费最强版 Trae/VsCode + Cline + Gemini-cli 构建 cnhkmcp 使用环境经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]免费最强版 TraeVsCode  Cline  Gemini-cli 构建 cnhkmcp 使用环境经验分享_34338855618583.md
- **讨论数**: 21

先赞后看，一键三连，需科学上网

**1. Gemini Cli 安装和登录验证参考，只需要通过用户认证即可**

[[L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md]([L2] Gemini CLI 结合 MCP 工具的探索经验分享_34319317355287.md)

**2. Cline 插件下载安装**

Cline插件在3.18.0短暂的支持过Gemini Cli ，在google要求下很快下线了该功能，该版本下载地址：  [[链接已屏蔽])

在Trae和VsCode ide中，选择从VSIX安装,安装后在Cline介绍页关闭自动更新 
> [!NOTE] [图片 OCR 识别内容]
> 终端
> 窗0
> 帮助
> 搜索
> Ppa
> 从 VSIX 安装。
> 让


**3. Cline配置**

打开Cline，选择使用其他api key不登录cline账号， 在API Provider 下拉列表中选择Gemini CLI Provider -> 视系统情况看是否需要配置oauth_creds.json 路径，一般无需配置， Let‘s get Started

**如果直接选择Gemini CLI Provider，Let‘s get Started没有反应，可以任意选一个其他的AI填入api key，进入之后再重新选择Gemini CLI Provider**

**4. MCP配置**

如下图，在1配置角色规则，2配置mcp server

角色配置参考： [[L2] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md]([L2] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md)


> [!NOTE] [图片 OCR 识别内容]
> Type
> @ for context;
> for slash commands & Workflows, hold shift to drag in fileslim
> @
> 十
> 骂
> 蛮 gemini-cli:gemini- 2.5-pro


成品：


> [!NOTE] [图片 OCR 识别内容]
> Rules
> Workflows
> Rules allow you to provide Cline with system-level guidance. Think of them as a
> persistent way to include context and preferences for your projects or globally
> for every conversation. Docs
> Global Rules
> Consultantmd
> New rule file。
> Workspace Rules
> New rule file。
> 十
> 恩
> 蛮  gemini-cli:gemini-2.5-pro
> Plan
> Act



> [!NOTE] [图片 OCR 识别内容]
> Auto-approve:
> Enabled
> Read
> Edit
> Safe Commands
> MCP Servers
> Worldquant-brain-platform
> 十
> 嚣
> 蛮  gemini-cli:gemini-2.5-pro
> Plan
> Act


**5. 使用感受**

**强于大部分收费大模型， 60次每分钟，1000次每天的额度足够调教自己的员工**


> [!NOTE] [图片 OCR 识别内容]
> 0
> Cline (器+')
> 器
> 9 巴
> 缌
> Task
> $0.0000
> 描述当前mcp的详细功能
> Tokens:
> 1.5m
> 13.9k
> 4.05 MB
> 419.8k
> 1.Om
> 9'T1 o
> 核心洞察:
> 1.战略转移成功:  您近期的研究重点已成功从 USA 扩展至 EUR 和 GLB 市场。尤
> 其在 EUR/DI/ANALYST 类别上取得了显著成果。
> 2.多元化初见成效:  您在欧洲点亮了多个新的数据类别。显著提升了投资组合的
> 多元化程度。
> 3.明确的增长机会:
> CHN
> (中国)  市场仍然是您投资组合中的空白区域。是您未
> 来获取高额回报和提升顾问等级的最大机遇。
> 下一步战略建议:
> 首要任务:  立即开始对 CHN 市场的数据集进行研究。使用
> get_datasets (region='CHN' ) 来发现可用的数据。
> 巩固优势:  在 EUR 和 GLB 市场。继续深化对 MODEL 和 RISK 类别的研究。建
> 立您的护城河
> 优化USA策略:  将在 USA 市场的精力从数量转向质量。专注于开发高
> Sharpe。 低相关性的独特Alphaa
> 您的近期表现证明了您具备快速适应和开拓新领域的能力。现在。将这股势头带入
> 中国市场。将是您成为顶尖顾问的关键步
> Auto-approve:
> Enabled
> Read
> Edit
> Safe Commands
> Start New Task
> Type a message。.
> Type @ for context;
> for slash commands & Workflows, hold shift to drag in fileslimages
> 十
> 蛮 gemini-cli:gemini-2.5-pro
> Plan
> Act


---

### 帖子 #15: AI-Driven, Semantically-Aware Alpha Generation Workflow (Local)This document outlines an advanced, robust workflow for generating financial alpha expressions. The process is driven by an AI assistant, operates entirely on local data, and focuses on creating semantically meaningful and syntactically correct alphas.#Workflow Diagram```mermaidgraph TDsubgraph "输入与学习 (Input & Learning)"A[1. 定义参数与学习<br>Define Parameters & Learn<br><br><b>用户输入:</b><br>- Region, Universe, Delay, Category, Operator<br><br><b>AI学习 (关键):</b><br>- <b>必须</b>从 `data/gold_operators.csv` 学习操作符定义、参数和用法。]endsubgraph "本地数据检索 (Local Data Retrieval)"B[2. 加载数据集元数据<br>Load Dataset Metadata<br><br><b>路径 (本地):</b><br>`data/datasets/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>读取并解析CSV，根据`Category`筛选数据集ID。]C[3. 加载并筛选字段<br>Load & Filter Fields<br><br><b>路径 (本地):</b><br>`data/fields/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>1. 加载所有字段。<br>2. 根据数据集ID筛选出`Category`相关字段。<br>3. 识别每个字段的类型 (matrix vs. vector)。]endsubgraph "AI智能生成与验证 (AI-Powered Generation & Verification)"D[4. AI理解、组合与验证<br>AI Understands, Combines & Verifies<br><br><b>过程:</b><br>- <b>处理Vector:</b> 对vector类型字段使用`vec_avg`等聚合。<br>- <b>组合字段:</b> 寻找经济学上合理的组合。<br>- <b>应用操作符:</b> 使用正确语法和分组关键字。<br>- <b>最终验证 (强制):</b> 重新检查每个表达式中所有字段的类型。]endsubgraph "输出 (Output)"E[5. 保存表达式<br>Save Expressions<br><br><b>工具:</b> `write_to_file`<br><b>内容:</b> 生成的、经过验证的、语法正确的表达式列表。]endA --> B;B --> C;C --> D;D --> E;```#Detailed Steps##1. Define Parameters & Learn- **User Input**: The user specifies the target parameters for the generation task: `Region`, `Universe`, `Delay`, `Category`, `Operator`.- **AI Learning (Crucial Step)**: The AI **must** retrieve and analyze the operator's definition, parameters, and correct syntax from the local file: `data/gold_operators.csv`.##2. Load Dataset Metadata (Local)- **Action**: The AI reads the appropriate dataset metadata file from the `data/datasets/` directory (e.g., `data/datasets/EQUITY_EUR_1_TOP2500.csv`).- **Parsing**: It extracts `dataset_id`s that match the specified `Category`.##3. Load & Filter Field Metadata (Local)- **Action**: The AI reads the comprehensive field metadata file from the `data/fields/` directory (e.g., `data/fields/EQUITY_EUR_1_TOP2500.csv`).- **Parsing and Filtering**:1.**Load All Fields**: Ingest the entire list of available data fields.2.**Identify Field Types**: Note whether each field is a `matrix` (scalar) or `vector` (event). This is a critical piece of information for each field.3.**Filter by Category**: Retain only the fields relevant to the specified `Category`.##4. AI Understands, Combines & VerifiesThis is the central, multi-stage intelligence step.1. **Handle Vector Fields**: **Crucially**, if a field is of type `vector`, it **must** be aggregated into a scalar value before being used in operators that expect scalar inputs (like arithmetic or group operators). Use `vec_avg()`, `vec_sum()`, or `vec_count()` for this purpose.2. **Find Meaningful Combinations**: The AI analyzes the `description` of scalar fields and *aggregated* vector fields to identify opportunities for economically sound combinations.3. **Construct Expressions**: The AI constructs expressions by strictly adhering to the operator syntax and using valid grouping keywords.-**Valid Grouping Keywords**: `subindustry`, `industry`, `sector`, `country`, `exchange`. These are platform-native keywords, not field names.4. **Final Verification (Mandatory)**:- Before outputting the final list, the AI **must** perform a final check on every generated expression.- For **every single field** within an expression, its type must be re-verified against the `fields.csv` file.- Any expression containing a raw `vector` field in a scalar context (e.g., direct arithmetic) **must be corrected or discarded**. This step is non-negotiable and prevents `event inputs` errors.-**Correct Example**: `group_median(snt21_2pos_mean_96 - vec_avg(snt12_lst_trgt_price), country)` (scalar minus an aggregated vector is valid).-**Incorrect Example**: `group_median(snt21_2pos_mean_96 - snt12_lst_trgt_price, country)` (This will fail because `snt12_lst_trgt_price` is a vector).##5. Save Verified Expressions- **Action**: The AI takes the final, fully verified list of alpha expressions.- **Output**: Using the `write_to_file` tool, it saves this Python list into a specified output file, ready for simulation.
- **主帖链接**: https://support.worldquantbrain.com[L2] [MCP]基于操作符生成alpha的工作流分享_35591278645015.md
- **讨论数**: 8

使用的工具链参考：  [../顾问 JX79797 (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md](../顾问 JX79797 (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)

本工作流的主要目的是，不让一个操作符流落在外，达到每个操作符都有提交。

**使用推荐： 稀有操作符 + 常见数据集， 也可以试试小数据集碰碰运气能不能暴击**

**流程图：**

**
> [!NOTE] [图片 OCR 识别内容]
> 输入与学习 (Input & Learning)
> 本地数据检索 (Local Data Retrieval)
> 1.定义参数与学习
> 2.加载数据集元数据
> 3.加载井筛选字段
> Define Parameters & Learn
> Load Dataset Metadata
> Load & Filter Fields
> 用户输入:
> 路径:
> 路径:
> Region, Universe, Delay, Category
> dataldatasetslEQUITY_{REGION}_.一
> datalfieldslEQUITY_{REGION}_: -
> AI学习 (关键):
> 动作:
> 动作:
> 必须从datalgold_operators.csv学习操作符定义和用法
> 1.加载所有字段
> 根据'Category'筛选数据集I0
> 2.根据10筛选相关字段
> Al智能生成与验证 (Al Powered Generation & Verification)
> 输出 (Output)
> 4.A1理解。组合与验证
> 5.保存表达式
> Al Understands, Combines & Verifies
> Save Expressions
> 过程:
> 工具:
> 处理Vector: 使用'vec_avg' 等聚合
> write_to_file
> 组合字段: 寻找经济学上合理的组合
> 应用操作符:使用正确语法
> 内容:
> 最终验证:  重新检查所有字段的类型
> 生成的。经过验证的。语法正确的表达式列表
**

1. 定义参数与学习：设置配置参数并从`data/gold_operators.csv`学习操作符定义

2. 加载数据集元数据：从`data/datasets/`加载并筛选相关数据集

3. 加载并筛选字段：从`data/fields/`加载字段并识别其类型(matrix/vector)

4. AI理解、组合与验证：智能生成表达式，应用正确的操作符，并进行严格验证

5. 保存表达式：将生成的有效表达式保存到指定输出文件

**示例：**

**Cine交互输入框输入：**

```
使用 intelligent_alpha_generation_workflow.md工作流，使用ts_covariance操作符以及region eur delay 1 universe TOP2500 instrumentType Equity, 使用socialmedia category里的字段生成30个alpha表达式，不超过两个操作符，不超过两个字段
```

**生成表达式列表：**

```
expressions = ["ts_covariance(scl12_sentiment, scl12_buzz, 10)","-ts_covariance(scl12_sentiment, scl12_buzz, 20)","ts_covariance(vec_avg(scl15_d1_risk_score), vec_avg(scl15_d1_conflict), 10)","-ts_covariance(vec_avg(scl15_d1_risk_score), vec_avg(scl15_d1_conflict), 20)","ts_covariance(vec_avg(scl15_d1_trust), vec_avg(scl15_d1_fundamentalstrength), 10)","-ts_covariance(vec_avg(scl15_d1_trust), vec_avg(scl15_d1_fundamentalstrength), 20)","ts_covariance(vec_avg(scl15_d1_pricedirection), vec_avg(scl15_d1_buzz), 10)","-ts_covariance(vec_avg(scl15_d1_pricedirection), vec_avg(scl15_d1_buzz), 20)","ts_covariance(vec_avg(scl15_d1_optimism), vec_avg(scl15_d1_sentiment), 10)","-ts_covariance(vec_avg(scl15_d1_optimism), vec_avg(scl15_d1_sentiment), 20)","ts_covariance(vec_avg(scl15_d1_longshort), vec_avg(scl15_d1_stress), 10)","-ts_covariance(vec_avg(scl15_d1_longshort), vec_avg(scl15_d1_stress), 20)"...]
```

**得到可提交alpha：**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Created 10/13/2025 EDT
> machine_optimize_alpha
> Add Alpha to a List
> Open alpha details in new tab
> 09
> Summary
> PerlO0
> 0S
> 眙 Single Data Set Alpha
> 自
> Power Pool Alpha
> Pyramid theme: EURIDIISOCIALMEDIA X1.2
> Start Date
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 01/21/2023 ESI
> Correlation
> Self Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.0887
> -0.0923
> Power Pool Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.0902
> -0.1100
> Prod Correlation
> Maximum
> Minimum
> Last Run: Mon, 10/13/2025,7:20 PM
> 0.4325
> -0.4795


**工作流内容**

```
# AI-Driven, Semantically-Aware Alpha Generation Workflow (Local)This document outlines an advanced, robust workflow for generating financial alpha expressions. The process is driven by an AI assistant, operates entirely on local data, and focuses on creating semantically meaningful and syntactically correct alphas.## Workflow Diagram```mermaidgraph TDsubgraph "输入与学习 (Input & Learning)"A[1. 定义参数与学习<br>Define Parameters & Learn<br><br><b>用户输入:</b><br>- Region, Universe, Delay, Category, Operator<br><br><b>AI学习 (关键):</b><br>- <b>必须</b>从 `data/gold_operators.csv` 学习操作符定义、参数和用法。]endsubgraph "本地数据检索 (Local Data Retrieval)"B[2. 加载数据集元数据<br>Load Dataset Metadata<br><br><b>路径 (本地):</b><br>`data/datasets/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>读取并解析CSV，根据`Category`筛选数据集ID。]C[3. 加载并筛选字段<br>Load & Filter Fields<br><br><b>路径 (本地):</b><br>`data/fields/EQUITY_{REGION}_{DELAY}_{UNIVERSE}.csv`<br><b>动作:</b><br>1. 加载所有字段。<br>2. 根据数据集ID筛选出`Category`相关字段。<br>3. 识别每个字段的类型 (matrix vs. vector)。]endsubgraph "AI智能生成与验证 (AI-Powered Generation & Verification)"D[4. AI理解、组合与验证<br>AI Understands, Combines & Verifies<br><br><b>过程:</b><br>- <b>处理Vector:</b> 对vector类型字段使用`vec_avg`等聚合。<br>- <b>组合字段:</b> 寻找经济学上合理的组合。<br>- <b>应用操作符:</b> 使用正确语法和分组关键字。<br>- <b>最终验证 (强制):</b> 重新检查每个表达式中所有字段的类型。]endsubgraph "输出 (Output)"E[5. 保存表达式<br>Save Expressions<br><br><b>工具:</b> `write_to_file`<br><b>内容:</b> 生成的、经过验证的、语法正确的表达式列表。]endA --> B;B --> C;C --> D;D --> E;```## Detailed Steps### 1. Define Parameters & Learn- **User Input**: The user specifies the target parameters for the generation task: `Region`, `Universe`, `Delay`, `Category`, `Operator`.- **AI Learning (Crucial Step)**: The AI **must** retrieve and analyze the operator's definition, parameters, and correct syntax from the local file: `data/gold_operators.csv`.### 2. Load Dataset Metadata (Local)- **Action**: The AI reads the appropriate dataset metadata file from the `data/datasets/` directory (e.g., `data/datasets/EQUITY_EUR_1_TOP2500.csv`).- **Parsing**: It extracts `dataset_id`s that match the specified `Category`.### 3. Load & Filter Field Metadata (Local)- **Action**: The AI reads the comprehensive field metadata file from the `data/fields/` directory (e.g., `data/fields/EQUITY_EUR_1_TOP2500.csv`).- **Parsing and Filtering**:1.**Load All Fields**: Ingest the entire list of available data fields.2.**Identify Field Types**: Note whether each field is a `matrix` (scalar) or `vector` (event). This is a critical piece of information for each field.3.**Filter by Category**: Retain only the fields relevant to the specified `Category`.### 4. AI Understands, Combines & VerifiesThis is the central, multi-stage intelligence step.1. **Handle Vector Fields**: **Crucially**, if a field is of type `vector`, it **must** be aggregated into a scalar value before being used in operators that expect scalar inputs (like arithmetic or group operators). Use `vec_avg()`, `vec_sum()`, or `vec_count()` for this purpose.2. **Find Meaningful Combinations**: The AI analyzes the `description` of scalar fields and *aggregated* vector fields to identify opportunities for economically sound combinations.3. **Construct Expressions**: The AI constructs expressions by strictly adhering to the operator syntax and using valid grouping keywords.-**Valid Grouping Keywords**: `subindustry`, `industry`, `sector`, `country`, `exchange`. These are platform-native keywords, not field names.4. **Final Verification (Mandatory)**:- Before outputting the final list, the AI **must** perform a final check on every generated expression.- For **every single field** within an expression, its type must be re-verified against the `fields.csv` file.- Any expression containing a raw `vector` field in a scalar context (e.g., direct arithmetic) **must be corrected or discarded**. This step is non-negotiable and prevents `event inputs` errors.-**Correct Example**: `group_median(snt21_2pos_mean_96 - vec_avg(snt12_lst_trgt_price), country)` (scalar minus an aggregated vector is valid).-**Incorrect Example**: `group_median(snt21_2pos_mean_96 - snt12_lst_trgt_price, country)` (This will fail because `snt12_lst_trgt_price` is a vector).### 5. Save Verified Expressions- **Action**: The AI takes the final, fully verified list of alpha expressions.- **Output**: Using the `write_to_file` tool, it saves this Python list into a specified output file, ready for simulation.
```

```

```

---

### 帖子 #16: 【Alpha模版】模版群助我60天点亮60个塔Alpha Template
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Alpha模版】模版群助我60天点亮60个塔Alpha Template_35253150989719.md
- **讨论数**: 87

**一、前言**

**我是一位freshman，7月1日转正，至今提交295个atom，点亮64座塔。**


> [!NOTE] [图片 OCR 识别内容]
> Eligibility Criteria
> 2025-23 July 1s,2025
> SEptember 30-h,2025
> Gold
> Erpert
> Master
> Grandas-er
> Signals
> 295
> Reached Grandmaster
> Pyramids Completed
> 64
> Reached Grandmaster
> Combined Alpha Performance
> 1.1
> 0.9 more to Grandmaster
> Combined Selected Alpha Performance
> 3.09
> Reached Grandmaster
> Combined Power Pool Alpha Performance
> 1.67



> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2025-03,July 1st 2025
> September 3oth, 2025
> Operazors pEr Alpna
> Operators Used
> Fields per Alpha
> 3.18
> 81
> 1.55
> Fielos USEJ
> Communizyaczivity
> Waxsinulati?nstreak
> 317
> 35.3
> 215
> Simulationactiviey
> Submissionactiit
> AUE
> Sep
> AUE
> Sep



> [!NOTE] [图片 OCR 识别内容]
> Pyramid alpha distribution
> 2025-03,July 1st 2025
> September 3oth, 2025
> Catego
> US
> eIR
> CHN
> L3S
> 3O =
> Esp nEs
> FundaTsta
> ImTaIT=
> IO
> Inaions
> Nro
> Nodsl
> Nsws
> T3t27
> Price Voluns
> Ris
> TTmn
> MOTCITETESC
> Sciallls-la


**二、方法论**

1. 经济学原理是静态框架，而股市运行于人性的动态博弈之中。  
2. 任何超额收益（Alpha）一旦被广泛追逐，便会因拥挤而失效。  
3. 故兵无常势，水无常形，唯有因时应变者，方能持续制胜。

**具体做法：**

**1. 穷举所有：** 挑选可用的模版。比如，一元、二元或三元模版

**2. 避免重复：** 从模版层降低相关性。比如scale、rank、zscore等单操作符模版，多数情况下是重复的，不要堆叠，浪费回测资源。

**3. 先随机再深入：** 首先，对准一个想要点亮的数据集；先用shuffle的方法，随机取样80个组合，计算每个模版的因子密度；如果某个模版因子密度大，就深入挖掘。

[参考虎哥模版实证及其改进效果评价](../顾问 MZ45384 (Rank 51)/[Commented] 【Alpha灵感】虎哥模版实证及其改进效果评价Alpha Template_33768594280343.md)

**三、模版框架（举例）**

**1. 一元模版（模版层面尽量不要有重复，从模版底层降低self-corr）**

```
for a in data_fields:    if index == 0:        # 斜率        expr = f"ts_regression(ts_zscore({a}, 500), ts_step(1), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 1:        # 增长率        expr = f"ts_delta(ts_delta({a}, 252)/ts_delay({a}, 252),252)"        factor_expressions.append(expr)    elif index == 2:        # 增长率        expr = f"ts_delta({a}, 252)/ts_delay({a}, 252)"        factor_expressions.append(expr)    elif index == 3:        # 自回归斜率        expr = f"ts_regression(ts_delta({a}, 252), ts_delta({a}, 500), 500, rettype=2)"        factor_expressions.append(expr)    elif index == 4:        # 平方动量        expr = f"ts_mean(signed_power(ts_delta({a}, 252), 2), 500)"        factor_expressions.append(expr)    elif index == 5:        # 衰减加权动量        expr = f"ts_decay_linear(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)    elif index == 6:        # 排名反转        expr = f"reverse(ts_rank(ts_zscore({a}, 500), 500))"        factor_expressions.append(expr)    elif index == 7:        # 对数平滑        expr = f"log(abs(ts_delta({a}, 500)) + 0.000001)"        factor_expressions.append(expr)    elif index == 8:        # 符号保留幂        expr = f"signed_power(ts_delta({a}, 500), 2)"        factor_expressions.append(expr)    elif index == 9:        # 差分层叠        expr = f"ts_delta(ts_delta({a}, 252), 500)"        factor_expressions.append(expr)
```

**2. 二元模版（降self-corr）**

```
    for a, b in combinations(data_fields, 2):        if index == 0:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500)"            factor_expressions.append(expr)        elif index == 1:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=2)"            factor_expressions.append(expr)        elif index == 2:            expr = f"ts_regression(ts_zscore({a}, 500), ts_zscore({b}, 500), 500, rettype=6)"            factor_expressions.append(expr)        elif index == 3:            expr = f"ts_regression({a}, {b}, 252, rettype=2)"            factor_expressions.append(expr)        elif index == 4:            expr = f"ts_regression({a}, {b}, 500, rettype=2)"            factor_expressions.append(expr)        elif index == 5:            expr = f"regression_neut(s_log_1p({a}), s_log_1p({b}))"            factor_expressions.append(expr)        elif index == 6:            expr = f"vector_neut({a}, {b})"            factor_expressions.append(expr)        elif index == 7:            expr = f"ts_delta_limit({a}, {b}, limit_volume=0.1)"            factor_expressions.append(expr)        else:            continue
```

**3. 三元模版（去self-corr）**

```
    for a, b, c in combinations(data_fields, 3):
        if index == 0:
            # 联合中性化：a 在 b 和 c 上的向量正交
            expr = f"vector_neut(vector_neut({a}, {b}), {c})"
        elif index == 1:
            # 分层回归残差（先对 b 中性化，再对 c）
            expr = f"regression_neut(regression_neut({a}, {b}), {c})"
        elif index == 2:
            # 带约束的时序变化（delta limit，以 b 和 c 的均值为基准）
            expr = f"ts_delta_limit({a}, ({b} + {c}) / 2, limit_volume=0.1)"
        elif index == 3:
            # 三变量时序相关性（a 与 b 的相关性，用 c 作权重或窗口调节）
            expr = f"ts_corr(ts_zscore({a}, 252), ts_zscore({b}, 252), 252) * {c}"
        elif index == 4:
            # 动态排序择时（a 在 b 和 c 构成的分组中做 ts_rank）
            expr = f"ts_rank(group_mean({a}, {b}), 500) * {c}"  # 假设 b 为分组字段
        elif index == 5:
            # 三重交互项（非线性放大）
            expr = f"ts_zscore({a}, 500) * ts_zscore({b}, 500) * ts_zscore({c}, 500)"
        elif index == 6:
            # 条件切换（c 为条件，选择 a 或 b）
            expr = f"if_else({c} > ts_mean({c}, 500), {a}, {b})"
        else:
            continue  # 超出范围跳过
```

**四、应用举例（CHN很难，但实际上也扛不住几次冲锋，突破只是时间问题）**

**1.analyst举例**  
> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Udd Nphato a Ust
> Code
> IS Summary
> Period
> aIeC
> aVB(a_
> Data SEtJphs
> Powver Pool Hphs
> Pyrsmidthems: CHNDTIANALYST 1.
> bts_decay_Iinear(a;126)
> ts_decay_exP_window(a,
> 252
> factor
> 951;
> siened_power (b,0.5)
> Agaregate
> Uata
> SHelo
> 1.13
> 10.08%
> 1.11
> 12.1796
> 17.39%
> 24.1596o0
> SIIUIatIOn
> Settings
> Year
> Sharpe
> TurOVeT
> Fltss
> Rtur
> Uawdown
> Marln
> Long Cnt
> Short Cot
> Istrut Type
> Regl
> Uelse
> Language
> Ia
> Dlay
> Truncatlon
> Neutrallatlon
> Pastewrtato
> HaN Hanlng
> UnltHandlng
> Max Trate
> EaJi?
> TLN
> TOFZJ
> HasUTEsSIUT
> 7.03
> Crowwire Factors
> TT
> 2013
> 231
> 13.88:
> 250
> 12
> 7.375
> 35.+:
> 201-
> 03
> 11.09::
> 1
> 8.115
> 1.3:
> 2015
> 126
> 1.20:
> 155
> 8.105
> 30.74:
> 15
> 2015
> 353
> 13.5::
> 2233
> 3.235
> 一7:
> 1
> Clone Alpha
> 2017
> 715
> 13.55::
> 1 2
> 7.32
> 37:
> 2013
> 5:
> 12
> 7.395
> 5:
> 13
> N Chart
> Prl
> 2019
> 1.10
> 17:
> &9
> 7.27
> 16.735:
> 133
> 2020
> 032
> 363:
> 0.13
> 2:
> 11.715
> -7.55
> 138
> 120
> 3.90:
> 12
> 10.255
> 41.575:
> 2022
> 277
> 3.51:
> 727
> 8.575
> 66冼:
> 126
> SJOK
> 2023
> +38
> 13.60:
> 311
> 0.305
> 69.5:
> 159
> ,DJOK
> ZSOK
> 医 Correlation
> Self Correlation
> TIATTIUITTI
> STITUCT
> L1| YUII
> J"1_
> Jan '1s
> Jan 16
> Jan 18
> Jar 19
> Jan 21
> Jan 2
> Jan 23
> Snsle
> J_


**2. fundamental举例**


> [!NOTE] [图片 OCR 识别内容]
> ACTV
> Crested 0827/2025 EOT
> anonymOUs
> Mdd Nphato a Lst
> Code
> w IS Summary
> PErIoU
> TJ5
> Data SEt-Ipha
> 昵 Powver Pool Nphs
> Pyrsmidthems: CHNDTIFUNDAMENTAL *1.
> bts_decay_exp_window(divide
> ts_ZsCOre
> 5881
> ts_std_dev(ts_ZsCOTe(a」
> 63),
> 2521
> 2481
> factor-o.5);
> siened_power (b,
> ABaregate Data
> SIIJIU
> SU'
> OLU
> 1.45
> 8.35%
> 1.18
> 8.269
> 14.959
> 19.799600
> SIIUIatIOT
> SettIIes
> Vear
> Sha
> TuIOeF
> Ftss
> Retwrs
> Uawdown
> Varwln
> Long Cnt
> Short Cot
> Tnstuwt Type
> Reglo
> Werse
> URa
> Dcay
> Dlay
> Truncatlon
> Neutallalon
> Pastewrtat
> NaNHanl
> Unlt Handlng
> Max Trade
> EaJi?
> TLN
> TOFZJU
> TasUYTESSIUT
> 7.03
> Rl
> 「T
> 2013
> 3_
> 2
> 12025
> 251:
> 7.51
> 014
> 102
> 1.47
> 3.115
> 15:
> 3
> 2015
> 1.17
> 7
> 7.135
> 145:
> 1.35
> V
> 2016
> 7 21
> 3.2
> 12525
> 15::
> 895
> 1
> Clone Alpha
> 2017
> 71
> 11.37
> 2335
> 41.415
> 1
> 2013
> 642
> 2905
> 436:
> 03
> 11
> N Chart
> Pnl
> 119
> 7.4
> 1.405
> 79::
> -.-3
> 2020
> 7.57
> 0.4
> 18
> 58
> 190
> 152
> 2021
> 10.55
> 0.5
> 7.20
> 13:
> 1.1
> 123
> 2022
> 9.7
> 3.315
> :::
> 21.2-
> 177
> 1
> CJOK
> 2023
> 2.36
> 7115
> 3.3
> 11.575
> 0:
> 3.3150
> 105
> Z,SJOK
> 邑 Correlation
> Self Correlation
> TATTIUITT
> I
> 11| YUIII
> Jn '11
> Jan"1s
> Jan 16
> Jan '17
> Jan 13
> an 19
> Jan 2
> J3n*23
> SRSIE


**3. model举例**  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Tarint
> 9+
> ZSCOre(BrouP_rank(ts
> ZSCOFe
> aB(n114_
> 126)Jindustry),
> 500);
> 毗 Sirele Data Set Alphs
> # PowVET Po?
> JIChS
> Fyrsmidthem: CHNDIIMODEL ~1.5
> e2ate
> Data
> SNUe
> TUTIU
> Reluiri
> eUJUU
> MJit
> 1.35
> 5.43%
> 88
> 5.33%
> 10.16%
> 9,659600
> SmMJaTiNn
> Settings
> InstrumentType
> Reglo
> Language
> Decay
> Delay
> Truncatlon
> N-utrallatlon
> Pasteurtato
> NaN Hanlling
> Unlt Handlng
> Max Trade
> Year
> Sharpe
> Turwower
> Fitss
> Returs
> Uawdown
> Vargln
> Long Cnt
> Short Comt
> Eovig
> TLN
> TTTTII
> Fast Expression
> Crowdine
> 
> WErt
> 2013
> 2
> 5.80:
> 35
> 5-5
> 311
> 201-
> ~32
> 5.39:
> 1.1:
> 6.355
> 351:
> 2015
> 5.80:
> &423
> 9.5-5
> -9.74:
> Clone Alpha
> 2016
> 20
> 41
> 2.705
> 12.85:
> 1375
> 5.10:
> 3汀
> 0.965
> 35.1
> 111
> Chart
> 2013
> 1.97:
> 」5
> 3.21
> 三:
> 11E5
> 2019
> C 
> Z
> -.335
> -5.5:
> 1J
> 2020
> 771
> 50:
> 0.D0
> ~JJ:
> 3.575
> 01
> 1Es
> 53
> 0.93
> SEE
> 435
> 一』_
> 112
> 2022
> 5.85:
> 12
> 3.735
> 20.4:
> 110
> 2023
> 139
> 1.81:
> 715
> 0.J5
> 89.517:
> DJOK
> 医 Correlation
> J"11
> Jan 16
> Jan"
> Jar13
> Jar 19
> a*20
> Jan 21
> Jan -2
> J*23
> Self Correlation
> MJuirIuir
> UinirUrr
> LJlTUI
> CVeC
> ABBT
> Uerse


**4. pv举例**


> [!NOTE] [图片 OCR 识别内容]
> ACNV
> Cregtsd 08302025EOT
> 3nOTyTOUs
> Add Alphato 3 List
> Code
> 4 IS
> Summary
> Period
> asts_quantile(ts_delta_limit (VeC_aVg
> VeC_aVg PV27
> Iimit_Volume=B.1)
> 580);
> ] Sirale Data Set Alphs
> ] Powe
> Pool Nphs
> Fyrsmid theme: CHNDTIPV*1.3
> ABgregate Data
> SIaru
> Fiues
> CO
> 1.30
> 9.63%
> 1.21
> 10.8696
> 18.67%
> 22.5696oo
> SIMJaTiO
> Settings
> Instument Type
> Reglo
> Language
> Decay
> Truncaton
> Neutrallaton
> Cast71
> NaN Hanllng
> Unlt Handlng
> Max Trade
> Sharp
> Turower
> C
> Retwrns
> Uawdown
> Marqln
> Long Cont
> Short Cowmt
> EOJiD
> TLN
> TSPZJU
> Fas: ECressor
> 7.03
> Marer
> Vrr
> 7113
> 9.3
> 0.7
> 1.055
> 130:
> 2
> CIT
> 1.595
> 419:
> 3.79
> 2015
> 0.33
> 1
> 072
> -3.315
> 157:
> 14.5s
> Clone Alpha
> 2015
> 7.53
> 2
> 15.545
> 5:
> 79
> 2017
> 31
> 3.7
> 21.405;
> 345:
> 95
> Chart
> 2013
> 713
> 1.5
> 155
> 13:
> 3.165
> Pnl
> -
> 0.5
> JSu
> +3:
> 53
> 2020
> 7
> 0.
> 5.795
> 13:
> 3-7
> 12
> 2021
> 2.13
> 11.1
> _5
> 45:
>  _=
> SJOK
> 202
> 11.72;
> 95
> 4:
> 2.3
> 15
> CJOK
> 2023
> 9.9
> 17.435
> .16::
> 31.13
> 17
> SJOK
> Risk neutralized
> ABaregate Data
> SHer
> MaTUIT
> 1.65
> 9.6390
> 1.14
> 5.9796
> 17.6290
> 12.4
> 9o0
> Js '1
> Janus
> Ian l6
> Jan"17
> Jar 13
> Ja 20
> lan -1
> Jan -
> J3n23
> 〈PV27
> Uene
> Cl
> T019


**五、总结（任正非同志的经典语录——与君共勉）**

“华为坚定不移28年只对准通信领域这个‘城墙口’冲锋。我们成长起来后，坚持只做一件事，在一个方面做大。华为只有几十人的时候就对着一个‘城墙口’进攻，几百人、几万人的时候也是对着这个‘城墙口’进攻，现在十几万人还是对着这个‘城墙口’冲锋。密集炮火，饱和攻击。”

---

### 帖子 #17: 【check王】验证表达式是否正确的脚本——七十二变黄金搭档
- **主帖链接**: https://support.worldquantbrain.com[L2] 【check王】验证表达式是否正确的脚本七十二变黄金搭档_36740689434391.md
- **讨论数**: 20

使用72变或者大模型生成的alpha表达式可能有语法错误，基于PLY(Python Lex-Yacc)写了第一版用于校验表达式是否正确

使用方法

1.安装库

pip install ply

2.执行脚本(脚本名我命名为expression_validator.py)

```
python expression_validator.py
```

会提示输入json文件路径，如果你把脚本放到cnhkmcp\untracked/APP目录下，72变生成的alpha刚好放在Tranformer/output/Alpha_generated_expressions.json文件中，回车执行即可

```
请输入要校验的表达式JSON文件路径（默认：Tranformer/output/Alpha_generated_expressions.json）: 
```

执行后会生成两个文件Alpha_generated_expressions_success.json 和Alpha_generated_expressions_error.json 对应符合规则和不符合的。

由于是第一版本，目前主要校验表达式中操作符的使用，字段主要校验是不是字母数字下划线组成。有许多不完善的地方，如果有不对的测试用例欢迎在评论区补充

代码：

```
#!/usr/bin/env python3# -*- coding: utf-8 -*-"""表达式验证器 - 使用抽象语法树验证字符串表达式格式是否正确本模块实现了一个能够检测字符串表达式格式是否正确的系统，基于PLY(Python Lex-Yacc)构建词法分析器和语法分析器，识别表达式中的操作符、函数和字段，并验证其格式正确性。"""import reimport sysimport jsonimport osfrom typing import List, Dict, Any, Optional, Tuple# 尝试导入PLY库，如果不存在则提供安装提示try:    import ply.lex as lex    import ply.yacc as yaccexcept ImportError:    print("错误: 需要安装PLY库。请运行 'pip install ply' 来安装。")    sys.exit(1)# 1. 定义支持的操作符和函数supported_functions = {    # Group 类别函数    'group_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_mean': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'group_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_rank': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_vector_proj': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_normalize': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'category', 'expression', 'expression', 'expression']},    'group_extra': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'category']},    'group_backfill': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression'], 'param_names': ['x', 'cat', 'days', 'std']},    'group_scale': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_count': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_neutralize': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'category']},    'group_multi_regression': {'min_args': 4, 'max_args': 9, 'arg_types': ['expression'] * 9},    'group_cartesian_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['category', 'category']},    'combo_a': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},        # Transformational 类别函数    'right_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'bucket': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 第二个参数可以是string类型的range参数    'tail': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'expression']},    'left_tail': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'trade_when': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'generate_stats': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},        # Cross Sectional 类别函数    'winsorize': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression'], 'param_names': ['x', 'std']},    'rank': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_proj': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'vector_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'regression_neut': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'multi_regression': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # 支持多个自变量        # Time Series 类别函数    'ts_std_dev': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_mean': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delay': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_corr': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_zscore': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_returns': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'mode']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_backfill': {'min_args': 2, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'string']},    'days_from_last_change': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'last_diff_value': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_scale': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_entropy': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'd', 'buckets']},    'ts_step': {'min_args': 1, 'max_args': 1, 'arg_types': ['number']},    'ts_sum': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_co_kurtosis': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'inst_tvr': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_exp_window': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'factor']},    'ts_av_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_kurtosis': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_diff': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_arg_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_min_max_cps': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_rank': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'ts_ir': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_theilsen': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'hump_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_weighted_decay': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_quantile': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'string']},    'ts_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_count_nans': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_covariance': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_co_skewness': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},    'ts_min_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_decay_linear': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'boolean']},    'jump_decay': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'number', 'expression', 'number', 'number'], 'param_names': ['x', 'd', 'stddev', 'sensitivity', 'force']},    'ts_moment': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'k']},    'ts_arg_min': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_regression': {'min_args': 3, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number'], 'param_names': ['y', 'x', 'd', 'lag', 'rettype']},    'ts_skewness': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_max_diff': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'kth_element': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'number', 'number']},    'hump': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'hump']},    'ts_median': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_delta': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_poly_regression': {'min_args': 3, 'max_args': 4, 'arg_types': ['expression', 'expression', 'number', 'number']},    'ts_target_tvr_decay': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number'], 'param_names': ['x', 'lambda_min', 'lambda_max', 'target_tvr']},    'ts_target_tvr_delta_limit': {'min_args': 2, 'max_args': 5, 'arg_types': ['expression', 'expression', 'number', 'number', 'number']},    'ts_target_tvr_hump': {'min_args': 1, 'max_args': 4, 'arg_types': ['expression', 'number', 'number', 'number']},    'ts_delta_limit': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number']},        # Special 类别函数    'inst_pnl': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'self_corr': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'in': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'universe_size': {'min_args': 0, 'max_args': 0, 'arg_types': []},        # Missing functions from operators.py    'quantile': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'driver', 'sigma']},  # quantile(x, driver = gaussian, sigma = 1.0)    'normalize': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'boolean', 'number']},  # normalize(x, useStd = false, limit = 0.0)    'zscore': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # zscore(x)        # Logical 类别函数    'or': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'and': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # 注意：这是关键字    'not': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # 注意：这是关键字    'is_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'is_not_nan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'less': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'is_finite': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'if_else': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression']},    'not_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'less_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'greater_equal': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},        # Vector 类别函数    'vec_kurtosis': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_min': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_count': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_sum': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_skewness': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_max': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_avg': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_range': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_choose': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'nth']},    'vec_powersum': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},    'vec_stddev': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_percentage': {'min_args': 1, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'percentage']},    'vec_ir': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'vec_norm': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'ts_percentage': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'd', 'percentage']},    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},    'ts_product': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number']},        # Additional functions from test cases    'rank_by_side': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'number', 'number'], 'param_names': ['x', 'rate', 'scale']},    'log_diff': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_mask': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},    'ts_partial_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'ts_triple_corr': {'min_args': 4, 'max_args': 4, 'arg_types': ['expression', 'expression', 'expression', 'number']},    'clamp': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},    'keep': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'number'], 'param_names': ['x', 'condition', 'period']},    'replace': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'target', 'dest']},    'filter': {'min_args': 3, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'h', 't']},    'one_side': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'string'], 'param_names': ['x', 'side']},    'scale_down': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'number'], 'param_names': ['x', 'constant']},        # Arithmetic 类别函数    'add': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # add(x, y, filter=false)    'multiply': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 99 + ['boolean'], 'param_names': ['x', 'y', 'filter']},  # multiply(x, y, ..., filter=false)    'sign': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'subtract': {'min_args': 2, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # subtract(x, y, filter=false)    'pasteurize': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'log': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'purify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'arc_tan': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'max': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # max(x, y, ...)    'to_nan': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'boolean']},  # to_nan(x, value=0, reverse=false)    'abs': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sigmoid': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'divide': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # divide(x, y)    'min': {'min_args': 2, 'max_args': 100, 'arg_types': ['expression'] * 100},  # min(x, y, ...)    'tanh': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'nan_out': {'min_args': 1, 'max_args': 3, 'arg_types': ['expression', 'expression', 'expression'], 'param_names': ['x', 'lower', 'upper']},  # nan_out(x, lower=0, upper=0)    'signed_power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # signed_power(x, y)    'inverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'round': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'sqrt': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    's_log_1p': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'reverse': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},  # -x    'power': {'min_args': 2, 'max_args': 2, 'arg_types': ['expression', 'expression']},  # power(x, y)    'densify': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},    'floor': {'min_args': 1, 'max_args': 1, 'arg_types': ['expression']},}# 2. 定义group类型字段group_fields = {    'sector', 'subindustry', 'industry', 'exchange', 'country', 'market'}# 3. 有效类别集合valid_categories = group_fields# 4. 字段命名模式 - 只校验字段是不是数字字母下划线组成field_patterns = [    re.compile(r'^[a-zA-Z0-9_]+$'),  # 只允许数字、字母和下划线组成的字段名]# 4. 抽象语法树节点类型class ASTNode:    """抽象语法树节点基类"""    def __init__(self, node_type: str, children: Optional[List['ASTNode']] = None,                  value: Optional[Any] = None, line: Optional[int] = None):        self.node_type = node_type  # 'function', 'operator', 'field', 'number', 'expression'        self.children = children or []        self.value = value        self.line = line        def __str__(self) -> str:        return f"ASTNode({self.node_type}, {self.value}, line={self.line})"        def __repr__(self) -> str:        return self.__str__()class ExpressionValidator:    """表达式验证器类"""        def __init__(self):        """初始化词法分析器和语法分析器"""        # 构建词法分析器        self.lexer = lex.lex(module=self, debug=False)        # 构建语法分析器        self.parser = yacc.yacc(module=self, debug=False)        # 错误信息存储        self.errors = []        # 词法分析器规则    tokens = ('FUNCTION', 'FIELD', 'NUMBER', 'LPAREN', 'RPAREN',               'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'COMMA', 'CATEGORY',              'EQUAL', 'ASSIGN', 'IDENTIFIER', 'STRING', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'BOOLEAN')        # 忽略空白字符    t_ignore = ' \t\n'        # 操作符 - 注意顺序很重要，长的操作符要放在前面    t_PLUS = r'\+'    t_MINUS = r'-'    t_TIMES = r'\*'    t_DIVIDE = r'/'    t_LPAREN = r'\('    t_RPAREN = r'\)'    t_COMMA = r','        t_EQUAL = r'=='    t_NOTEQUAL = r'!='    t_GREATEREQUAL = r'>='    t_LESSEQUAL = r'<='    t_GREATER = r'>'    t_LESS = r'<'    t_ASSIGN = r'='        # 数字（整数和浮点数）    def t_NUMBER(self, t):        r'\d+\.?\d*'        if '.' in t.value:            t.value = float(t.value)        else:            t.value = int(t.value)        return t        # 字符串 - 需要放在所有其他标识符规则之前    def t_STRING(self, t):        r"'[^']*'|\"[^\"]*\""        # 去除引号        t.value = t.value[1:-1]        return t        # 函数和字段名    def t_IDENTIFIER(self, t):        r'[a-zA-Z_][a-zA-Z0-9_]*'        # 检查是否为布尔值        if t.value.lower() in {'true', 'false'}:            t.type = 'BOOLEAN'            t.value = t.value.lower()  # 转换为小写以保持一致性        else:            # 查看当前token后面的字符，判断是否为参数名（后面跟着'='）            lexpos = t.lexpos            next_chars = ''            if lexpos + len(t.value) < len(t.lexer.lexdata):                # 查看当前token后面的字符，跳过空格                next_pos = lexpos + len(t.value)                while next_pos < len(t.lexer.lexdata) and t.lexer.lexdata[next_pos].isspace():                    next_pos += 1                if next_pos < len(t.lexer.lexdata):                    next_chars = t.lexer.lexdata[next_pos:next_pos+1]                        # 如果后面跟着'='，则为参数名            if next_chars == '=':                t.type = 'IDENTIFIER'            # 如果后面跟着'('，则为函数名            elif next_chars == '(':                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为参数名（支持更多参数名）            elif t.value in {'std', 'k', 'lambda_min', 'lambda_max', 'target_tvr', 'range', 'buckets', 'lag', 'rettype', 'mode', 'nth', 'constant', 'percentage', 'driver', 'sigma', 'rate', 'scale', 'filter', 'lower', 'upper', 'target', 'dest', 'event', 'sensitivity', 'force', 'h', 't', 'period', 'stddev', 'factor', 'k', 'useStd', 'limit', 'gaussian', 'uniform', 'cauchy'}:                t.type = 'IDENTIFIER'            # 检查是否为函数名（不区分大小写）            elif t.value.lower() in supported_functions:                t.type = 'FUNCTION'                t.value = t.value.lower()  # 转换为小写以保持一致性            # 检查是否为有效类别            elif t.value in valid_categories:                t.type = 'CATEGORY'            # 检查是否为字段名            elif self._is_valid_field(t.value):                t.type = 'FIELD'            else:                # 其他标识符，保留为IDENTIFIER类型                t.type = 'IDENTIFIER'        return t        # 行号跟踪    def t_newline(self, t):        r'\n+'        t.lexer.lineno += len(t.value)        # 错误处理    def t_error(self, t):        if t:            # 检查是否为非法字符            if not re.match(r'[a-zA-Z0-9_\+\-\*/\(\)\,\s=<>!]', t.value[0]):                # 这是一个非法字符                self.errors.append(f"非法字符 '{t.value[0]}' (行 {t.lexer.lineno})")            else:                # 这是一个非法标记                self.errors.append(f"非法标记 '{t.value}' (行 {t.lexer.lineno})")            # 跳过这个字符，继续处理            t.lexer.skip(1)        else:            self.errors.append("词法分析器到达文件末尾")        # 语法分析器规则    def p_expression(self, p):        """expression : comparison                      | expression EQUAL comparison                      | expression NOTEQUAL comparison                      | expression GREATER comparison                      | expression LESS comparison                      | expression GREATEREQUAL comparison                      | expression LESSEQUAL comparison"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_comparison(self, p):        """comparison : term                      | comparison PLUS term                      | comparison MINUS term"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_term(self, p):        """term : factor                | term TIMES factor                | term DIVIDE factor"""        if len(p) == 2:            p[0] = p[1]        else:            p[0] = ASTNode('binop', [p[1], p[3]], {'op': p[2]})        def p_factor(self, p):        """factor : NUMBER                  | STRING                  | FIELD                  | CATEGORY                  | IDENTIFIER                  | BOOLEAN                  | MINUS factor                  | LPAREN expression RPAREN                  | function_call"""        if len(p) == 2:            # 数字、字符串、字段、类别或标识符            if p.slice[1].type == 'NUMBER':                p[0] = ASTNode('number', value=p[1])            elif p.slice[1].type == 'STRING':                p[0] = ASTNode('string', value=p[1])            elif p.slice[1].type == 'FIELD':                p[0] = ASTNode('field', value=p[1])            elif p.slice[1].type == 'CATEGORY':                p[0] = ASTNode('category', value=p[1])            elif p.slice[1].type == 'BOOLEAN':                p[0] = ASTNode('boolean', value=p[1])            elif p.slice[1].type == 'IDENTIFIER':                p[0] = ASTNode('identifier', value=p[1])            else:                p[0] = p[1]        elif len(p) == 3:            # 一元负号            p[0] = ASTNode('unop', [p[2]], {'op': p[1]})        elif len(p) == 4:            # 括号表达式            p[0] = p[2]        else:            # 函数调用            p[0] = p[1]        def p_function_call(self, p):        '''function_call : FUNCTION LPAREN args RPAREN'''        p[0] = ASTNode('function', p[3], p[1])        def p_args(self, p):        '''args : arg_list                | empty'''        if len(p) == 2 and p[1] is not None:            p[0] = p[1]        else:            p[0] = []        def p_arg_list(self, p):        '''arg_list : arg                   | arg_list COMMA arg'''        if len(p) == 2:            p[0] = [p[1]]        else:            p[0] = p[1] + [p[3]]        def p_arg(self, p):        '''arg : expression              | IDENTIFIER ASSIGN expression'''        if len(p) == 2:            p[0] = {'type': 'positional', 'value': p[1]}        else:            p[0] = {'type': 'named', 'name': p[1], 'value': p[3]}        def p_empty(self, p):        '''empty :'''        p[0] = None        # 语法错误处理    def p_error(self, p):        if p:            self.errors.append(f"语法错误在位置 {p.lexpos}: 非法标记 '{p.value}'")        else:            self.errors.append("语法错误: 表达式不完整")        def _is_valid_field(self, field_name: str) -> bool:        """检查字段名是否符合模式"""        for pattern in field_patterns:            if pattern.match(field_name):                return True        return False        def validate_function(self, node: ASTNode, is_in_group_arg: bool = False) -> List[str]:        """验证函数调用的参数数量和类型"""        function_name = node.value        args = node.children        function_info = supported_functions.get(function_name)                if not function_info:            return [f"未知函数: {function_name}"]                errors = []                # 检查参数数量        if len(args) < function_info['min_args']:            errors.append(f"函数 {function_name} 需要至少 {function_info['min_args']} 个参数，但只提供了 {len(args)}")        elif len(args) > function_info['max_args']:            errors.append(f"函数 {function_name} 最多接受 {function_info['max_args']} 个参数，但提供了 {len(args)}")                # 处理参数验证        # 跟踪已使用的位置参数索引        positional_index = 0                # 对于所有函数，支持命名参数        for arg in args:            if isinstance(arg, dict):                if arg['type'] == 'named':                    # 命名参数                    if 'param_names' in function_info and arg['name'] in function_info['param_names']:                        # 查找参数在param_names中的索引                        param_index = function_info['param_names'].index(arg['name'])                        if param_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][param_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, param_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    # 对于winsorize函数，支持std和clip参数                    elif function_name == 'winsorize' and arg['name'] in ['std', 'clip']:                        arg_errors = self._validate_arg_type(arg['value'], 'number', 0, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    # 对于bucket函数，支持'range'和'buckets'参数                    elif function_name == 'bucket' and arg['name'] in ['range', 'buckets']:                        # range和buckets参数应该是string类型                        arg_errors = self._validate_arg_type(arg['value'], 'string', 1, function_name, is_in_group_arg)                        errors.extend(arg_errors)                    else:                        errors.append(f"函数 {function_name} 不存在参数 '{arg['name']}'")                elif arg['type'] == 'positional':                    # 位置参数（字典形式）                    # 对于winsorize函数，第二个参数必须是命名参数                    if function_name == 'winsorize' and positional_index == 1:                        errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                    # 对于ts_moment函数，第三个参数必须是命名参数                    elif function_name == 'ts_moment' and positional_index == 2:                        errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                    else:                        # 验证位置参数的类型                        if positional_index < len(function_info['arg_types']):                            expected_type = function_info['arg_types'][positional_index]                            arg_errors = self._validate_arg_type(arg['value'], expected_type, positional_index, function_name, is_in_group_arg)                            errors.extend(arg_errors)                    positional_index += 1                else:                    # 其他字典类型参数                    errors.append(f"参数 {positional_index+1} 格式错误")                    positional_index += 1            else:                # 位置参数（直接ASTNode形式）                # 对于winsorize函数，第二个参数必须是命名参数                if function_name == 'winsorize' and positional_index == 1:                    errors.append(f"函数 {function_name} 的第二个参数必须使用命名参数 'std='")                # 对于ts_moment函数，第三个参数必须是命名参数                elif function_name == 'ts_moment' and positional_index == 2:                    errors.append(f"函数 {function_name} 的第三个参数必须使用命名参数 'k='")                else:                    # 验证位置参数的类型                    if positional_index < len(function_info['arg_types']):                        expected_type = function_info['arg_types'][positional_index]                        arg_errors = self._validate_arg_type(arg, expected_type, positional_index, function_name, is_in_group_arg)                        errors.extend(arg_errors)                positional_index += 1                return errors        def _validate_arg_type(self, arg: ASTNode, expected_type: str, arg_index: int, function_name: str, is_in_group_arg: bool = False) -> List[str]:        """验证参数类型是否符合预期"""        errors = []                # 首先检查是否是group类型字段，如果是则只能用于Group类型函数        # 但是如果当前函数是group_xxx或在group函数的参数链中，则允许使用        if arg.node_type == 'category' and arg.value in group_fields:            if not (function_name.startswith('group_') or is_in_group_arg):                errors.append(f"Group类型字段 '{arg.value}' 只能用于Group类型函数的参数中")                # 然后验证参数类型是否符合预期        if expected_type == 'expression':            # 表达式可以是任何有效的AST节点            pass        elif expected_type == 'number':            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个数字，但得到 {arg.node_type}")        elif expected_type == 'boolean':            # 布尔值可以是数字（0/1）            if arg.node_type != 'number':                errors.append(f"参数 {arg_index+1} 应该是一个布尔值（0/1），但得到 {arg.node_type}")        elif expected_type == 'field':            if arg.node_type != 'field' and arg.node_type != 'category':                # 允许field或category作为字段参数                errors.append(f"参数 {arg_index+1} 应该是一个字段，但得到 {arg.node_type}")            elif arg.node_type == 'field' and not self._is_valid_field(arg.value):                errors.append(f"无效的字段名: {arg.value}")        elif expected_type == 'category':            if not function_name.startswith('group_'):                # 非group函数的category参数必须是category类型且在valid_categories中                if arg.node_type != 'category':                    errors.append(f"参数 {arg_index+1} 应该是一个类别，但得到 {arg.node_type}")                elif arg.value not in valid_categories:                    errors.append(f"无效的类别: {arg.value}")            # group函数的category参数可以是任何类型（field、category等），不进行类型校验                return errors        def validate_ast(self, ast: Optional[ASTNode], is_in_group_arg: bool = False) -> List[str]:        """递归验证抽象语法树"""        if not ast:            return ["无法解析表达式"]                errors = []                # 根据节点类型进行验证        if ast.node_type == 'function':            # 检查当前函数是否是group函数            is_group_function = ast.value.startswith('group_')            # 确定当前是否在group函数的参数链中            current_in_group_arg = is_in_group_arg or is_group_function            # 验证函数            function_errors = self.validate_function(ast, current_in_group_arg)            errors.extend(function_errors)                        # 递归验证子节点时使用current_in_group_arg            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], current_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, current_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type in ['unop', 'binop']:            # 对操作符的子节点进行验证            for child in ast.children:                if hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)        elif ast.node_type == 'field':            # 验证字段名            if not self._is_valid_field(ast.value):                errors.append(f"无效的字段名: {ast.value}")        else:            # 递归验证子节点            for child in ast.children:                if isinstance(child, dict):                    # 命名参数，验证其值                    if 'value' in child and hasattr(child['value'], 'node_type'):                        child_errors = self.validate_ast(child['value'], is_in_group_arg)                        errors.extend(child_errors)                elif hasattr(child, 'node_type'):                    child_errors = self.validate_ast(child, is_in_group_arg)                    errors.extend(child_errors)                return errors        def _process_semicolon_expression(self, expression: str) -> Tuple[bool, str]:        """处理带有分号的表达式，将其转换为不带分号的简化形式                Args:            expression: 要处理的表达式字符串                    Returns:            Tuple[bool, str]: (是否成功, 转换后的表达式或错误信息)        """        # 检查表达式是否以分号结尾        if expression.strip().endswith(';'):            return False, "表达式不能以分号结尾"                # 分割表达式为语句列表        statements = [stmt.strip() for stmt in expression.split(';') if stmt.strip()]        if not statements:            return False, "表达式不能为空"                # 存储变量赋值        variables = {}                # 处理每个赋值语句（除了最后一个）        for i, stmt in enumerate(statements[:-1]):            # 检查是否包含赋值符号            if '=' not in stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 检查是否是比较操作符（==, !=, <=, >=）            if any(op in stmt for op in ['==', '!=', '<=', '>=']):                # 如果包含比较操作符，需要确认是否有赋值符号                # 使用临时替换法：将比较操作符替换为临时标记，再检查是否还有=                temp_stmt = stmt                for op in ['==', '!=', '<=', '>=']:                    temp_stmt = temp_stmt.replace(op, '---')                                if '=' not in temp_stmt:                    return False, f"第{i+1}个语句必须是赋值语句，不能只是比较表达式"                        # 找到第一个=符号（不是比较操作符的一部分）            # 先将比较操作符替换为临时标记，再找=            temp_stmt = stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' not in temp_stmt:                return False, f"第{i+1}个语句必须是赋值语句（使用=符号）"                        # 找到实际的=位置            equals_pos = temp_stmt.index('=')                        # 在原始语句中找到对应位置            real_equals_pos = 0            temp_count = 0            for char in stmt:                if temp_count == equals_pos:                    break                if char in '!<>':                    # 检查是否是比较操作符的一部分                    if real_equals_pos + 1 < len(stmt) and stmt[real_equals_pos + 1] == '=':                        # 是比较操作符，跳过两个字符                        real_equals_pos += 2                        temp_count += 3  # 因为替换成了三个字符的---                    else:                        real_equals_pos += 1                        temp_count += 1                else:                    real_equals_pos += 1                    temp_count += 1                        # 分割变量名和值            var_name = stmt[:real_equals_pos].strip()            var_value = stmt[real_equals_pos + 1:].strip()                        # 检查变量名是否有效            if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', var_name):                return False, f"第{i+1}个语句的变量名'{var_name}'无效，只能包含字母、数字和下划线，且不能以数字开头"                        var_name_lower = var_name.lower()  # 变量名不区分大小写                        # 检查变量名是否在后续表达式中使用            # 这里不需要，因为后面的表达式会检查                        # 检查变量值中使用的变量是否已经定义            # 简单检查：提取所有可能的变量名            used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', var_value)            for used_var in used_vars:                used_var_lower = used_var.lower()                if used_var_lower not in variables:                    # 检查是否是函数名                    if used_var not in supported_functions:                        # 对于单个字母或简单单词，不自动视为字段名，要求先定义                        if len(used_var) <= 2:                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 对于较长的字段名，仍然允许作为字段名                        elif not self._is_valid_field(used_var):                            return False, f"第{i+1}个语句中使用的变量'{used_var}'未在之前定义"                        # 将之前定义的变量替换到当前值中            for existing_var, existing_val in variables.items():                # 使用单词边界匹配，避免替换到其他单词的一部分                var_value = re.sub(rf'\b{existing_var}\b', existing_val, var_value)                        # 存储变量            variables[var_name_lower] = var_value                # 处理最后一个语句（实际的表达式）        final_stmt = statements[-1]                # 检查最后一个语句是否是赋值语句        if '=' in final_stmt:            # 替换比较操作符为临时标记，然后检查是否还有单独的=            temp_stmt = final_stmt            for op in ['==', '!=', '<=', '>=']:                temp_stmt = temp_stmt.replace(op, '---')                        if '=' in temp_stmt:                return False, "最后一个语句不能是赋值语句"                # 检查最后一个语句中使用的变量是否已经定义        used_vars = re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', final_stmt)        for used_var in used_vars:            used_var_lower = used_var.lower()            if used_var_lower not in variables:                # 检查是否是函数名                if used_var not in supported_functions:                    # 在分号表达式中，所有非函数名的标识符都必须是变量，必须在之前定义                    return False, f"最后一个语句中使用的变量'{used_var}'未在之前定义"                # 将变量替换到最后一个表达式中        final_expr = final_stmt        for var_name, var_value in variables.items():            final_expr = re.sub(rf'\b{var_name}\b', var_value, final_expr)                return True, final_expr        def check_expression(self, expression: str) -> Dict[str, Any]:        """        检查表达式格式是否正确                Args:            expression: 要验证的表达式字符串                    Returns:            包含验证结果的字典        """        # 重置错误列表        self.errors = []                try:            expression = expression.strip()            if not expression:                return {                    'valid': False,                    'errors': ['表达式不能为空'],                    'tokens': [],                    'ast': None                }                        # 处理带有分号的表达式            if ';' in expression:                success, result = self._process_semicolon_expression(expression)                if not success:                    return {                        'valid': False,                        'errors': [result],                        'tokens': [],                        'ast': None                    }                expression = result                        # 重置词法分析器的行号            self.lexer.lineno = 1                        # 词法分析（用于调试）            self.lexer.input(expression)            tokens = []            # 调试：打印识别的标记            print(f"\n调试 - 表达式: {expression}")            print("识别的标记:")            for token in self.lexer:                print(f"  - 类型: {token.type}, 值: '{token.value}', 位置: {token.lexpos}")                tokens.append(token)                        # 重新设置词法分析器的输入，以便语法分析器使用            self.lexer.input(expression)            self.lexer.lineno = 1                        # 语法分析            ast = self.parser.parse(expression, lexer=self.lexer)                        # 验证AST            validation_errors = self.validate_ast(ast)                        # 合并所有错误            all_errors = self.errors + validation_errors                        # 检查括号是否匹配            bracket_count = 0            for char in expression:                if char == '(':                    bracket_count += 1                elif char == ')':                    bracket_count -= 1                if bracket_count < 0:                    all_errors.append("括号不匹配: 右括号过多")                    break            if bracket_count > 0:                all_errors.append("括号不匹配: 左括号过多")                        return {                'valid': len(all_errors) == 0,                'errors': all_errors,                'tokens': tokens,                'ast': ast            }        except Exception as e:            return {                'valid': False,                'errors': [f"解析错误: {str(e)}"],                'tokens': [],                'ast': None            }def main():    """主函数 - 用于验证表达式并输出结果到JSON文件"""    validator = ExpressionValidator()        # 获取用户输入的JSON文件路径，默认路径为当前路径下的Tranformer/output/Alpha_generated_expressions.json    default_path = os.path.join("Tranformer", "output", "Alpha_generated_expressions.json")    input_path = input(f"请输入要校验的表达式JSON文件路径（默认：{default_path}）: ").strip()        if not input_path:        input_path = default_path        # 检查文件是否存在    if not os.path.exists(input_path):        print(f"错误: 文件 {input_path} 不存在")        return        # 读取JSON文件    try:        with open(input_path, 'r', encoding='utf-8') as f:            expressions_data = json.load(f)    except json.JSONDecodeError as e:        print(f"错误: JSON文件解析失败 - {e}")        return        # 提取表达式列表    # 假设JSON文件结构为 {"expressions": ["expr1", "expr2", ...]} 或直接是 ["expr1", "expr2", ...]    if isinstance(expressions_data, dict) and "expressions" in expressions_data:        expressions = expressions_data["expressions"]    elif isinstance(expressions_data, list):        expressions = expressions_data    else:        print("错误: JSON文件格式不正确，需要包含表达式列表")        return        # 验证表达式    valid_expressions = []    invalid_expressions = []        print(f"开始验证 {len(expressions)} 个表达式...")    for i, expr in enumerate(expressions, 1):        if i % 10 == 0:            print(f"已验证 {i}/{len(expressions)} 个表达式")                    result = validator.check_expression(expr)        if result["valid"]:            valid_expressions.append(expr)        else:            invalid_expressions.append({"expression": expr, "errors": result["errors"]})        # 生成输出文件路径    base_name = os.path.basename(input_path)    name, ext = os.path.splitext(base_name)    output_dir = os.path.dirname(input_path)        valid_output_path = os.path.join(output_dir, f"{name}_success{ext}")    invalid_output_path = os.path.join(output_dir, f"{name}_error{ext}")        # 保存结果到JSON文件    print(f"\n验证完成！")    print(f"有效表达式: {len(valid_expressions)}")    print(f"无效表达式: {len(invalid_expressions)}")        # 保存有效表达式    try:        with open(valid_output_path, 'w', encoding='utf-8') as f:            json.dump(valid_expressions, f, ensure_ascii=False, indent=2)        print(f"有效表达式已保存到: {valid_output_path}")    except Exception as e:        print(f"错误: 保存有效表达式失败 - {e}")        # 保存无效表达式    try:        with open(invalid_output_path, 'w', encoding='utf-8') as f:            json.dump(invalid_expressions, f, ensure_ascii=False, indent=2)        print(f"无效表达式已保存到: {invalid_output_path}")    except Exception as e:        print(f"错误: 保存无效表达式失败 - {e}")if __name__ == "__main__":    main()
```

---

### 帖子 #18: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索附学生优惠方法提示词在服务器中使用经验分享_36634788057367.md
- **讨论数**: 34

## Intro

鉴于一些朋友不知道Gemini CLI的功能，遂写一篇帖子进行教学，目录：

1. Gemini CLI的安装和配置
2. CLI中MCP的配置
3. 使用示例
4. 领取1年免费的Gemini 3 Pro学生优惠
5. 在服务器中使用Gemini CLI
6. 服务器中无法登陆的问题解决方案

## Gemini CLI Installation

首先进行GeminiCLI的下载： [[链接已屏蔽])

或者通过命令进行全局安装

```
npm install -g @google/gemini-cli
```

安装完成后，在终端运行

```
gemini --version
```

如果出现  `>=0.18.4` 的版本号就说明成功了

切换到项目所在文件夹，以我自己为例

```
cd CodeProject/consultant
```

然后输入  `gemini ` 回车就可以启动Gemini Cli了

进入后运行  `/settings ` 出现如图界面


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> consultant
> 乙82
> /settings
> Settings
> Preview Features (e.9''
> models )
> truex
> Vim Mode
> false
> Disable
> Auto Update
> false
> Enable Prompt Completion
> false
> Debug Keystroke Logging
> false
> Enable
> Session Cleanup
> false
> Output
> Format
> Text
> Hide Window Title
> false
> Apply
> To
> User Settings
> Workspace Settings
> System Settings
> (Use
> Enter
> to select,
> Tab
> to change focus,
> EsC
> t0
> CloSe)


按回车将 Preview Features 打开，然后按Esc退出即可

再输入命令 `/model` 选择模型，如图，选择第二个Pro


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> consultant
> 乙82
> /settings
> /model
> Select
> Model
> Gemini
> 3
> is
> nOW
> enabled
> To
> disable
> Gemini
> 3,
> disable
> IPreview
> features"
> in /settings
> Learn
> more
> at https: / /goo. gle/enable-preview-features
> When
> yoU
> Select
> Auto
> 0r
> Pro,
> Gemini
> CLI Will attempt
> t0
> use gemini-3-pro-preview first,
> before falling
> back
> t0
> gemini-z. 5-pro.
> 1.
> Auto
> Let
> the system choose
> the best
> model
> for
> YoUr
> task:
> 2.
> Pro
> (gemini-3-pro-preview,
> gemini-2.5-pro )
> For
> complex tasks
> that require
> reasoning
> and creativity
> 3.
> Flash (gemini-2.S-flash)
> For
> tasks
> that
> need
> a
> balance
> Of speed
> and reasoning
> 4.
> Flash-Lite (gemini-z.5-flash-lite)
> For simple
> tasks
> that need
> t0
> be
> done quickly
> To
> USe
> a
> specific
> Gemini
> model
> 0n
> startup,
> USe
> the
> T-model
> (Press
> EsC
> t0
> Close)
> deep
> flag


## CLI中MCP的配置

接下来是在针对Gemini CLI进行MCP的配置，首先找到Gemini所在目录，这里以Mac为例，Mac默认隐藏点文件夹和点文件，可以通过快捷键  `Shift+Space+. ` 显示。


> [!NOTE] [图片 OCR 识别内容]
> 000
> .gemini
> Back/Forward
> Keka
> View
> Group
> AirDrop
> Delete
> Action
> Search
> Console-ninja
> Recents
> oauth_creds json
> bashrc
> Shared
> antigravity
> Claude
> state json
> Favorites
> gemini
> settingsjson
> matplotlib
> Applications
> GEMINI.md
> Rhistory
> Claude
> Desktop
> lesshst
> google_accounts.json
> Downloads
> IOCal
> google_account_id
> Rapp.history
> Documents
> installation_id
> Vim_runtime
> Movies
> settings.json.orig
> Zcompdump
> BOOk Dro 5.9
> tmp
> Pictures
> gitignore
> User_id
> Oocker
> Locations
> mongodb
> jCloud Drive
> SKiko
> orange
> jupyter
> Orange 的 MacBook Pro
> anydesk
> .parallel
> AirDrop
> nrntncnl
> pnnfin pnnf
> Macintosh HD
> Users
> orange
> .gemini
> Network
> 12 items, 158.12GBavailable


进入 settings.json 文件，以下是我的配置：

```
 {   "ide": {     "hasSeenNudge": true   },   "mcpServers": {     "worldquant-brain-platform": {       "command": "/Users/orange/CodeProject/consultant/run_webspider_python.sh",       "args": [         "/opt/anaconda3/envs/WebSpider/lib/python3.11/site-packages/cnhkmcp/untracked/platform_functions.py"       ],       "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features."     }   },   "security": {     "auth": {       "selectedType": "oauth-personal"     }   },   "ui": {     "theme": "Atom One"   },   "general": {     "previewFeatures": true   } }
```

其中  `"/Users/orange/CodeProject/consultant/run_webspider_python.sh" ` 是我让AI写的命令文件，因为在Mac上很多人都遇到过无法使用Search Forum的问题。

> 如果有需要我会分享在评论区，在这里还是教学为主

根据自己文件所在位置修改路径，剩余的为主题配置、登录方式配置以及之前开启的预览特性。

## 使用示例

首先我会将Rule发送给Gemini，我通过  [Yprompt](#) ( [[链接已屏蔽]) )  进行提示词的生成和优化，他会一直询问你的需求和期望，收集到足够信息后就会生成完整的提示词，有需要的朋友可以根据自己需要进行调整。

我的提示词中有很多文件都已经提前准备好，便于Gemini直接读取，减少网络请求和MCP的调用。


> [!NOTE] [图片 OCR 识别内容]
> 角色:您是一位WorldQuant顶页级研究顾问,
> 您的任务是完全自主地模拟执行一个Alpha因子研究工作流。您将仅通过描述性地"调用"
> MCP工 具来驱动整个过程
> 并将所有研究步骤:
> 分析 _
> 决策和最终的Alpha因子提案详细记录在Markdown格式的研究报告中
> 您无需
> 编写任何代码。也无法加速WorldQuant平台的实际回测过程。
> 您的核心目标是找出能够提交的Alpha因子
> 核心目标:生成一份详尽的研究报告。记录从识别研究目标到提出满足提交要求的Alpha因子的完整自主研究过程。
> 工作流:
> 1。识别研究目标:
> 模拟执行:描述如何调用MCP Tools (如 mcp_brain-api_get_Pyramid_alphas
> ICP
> brain-
> api_get_pyramid_multipliers
> 来识别当前未被充分利用 ("未点亮")  的金字塔类别c
> 如果所有金字塔类别均已点亮。则描述将如何根据用户指定的其他数据集进行研究。
> 记录:在研究报告中详细描述识别出的研究目标类别。
> 2。数据与算子分析:
> 模拟执行:描述如何查阅 operators_
> 2025.CSV
> (运算符文档)
> datafields
> CSV
> 以及"股票类"文件夹中的论文文档,
> 以理解数据字段和运算符的特点
> 应用场景
> 方法及其潜在的经济学含义。
> 记录:在报告中详细阐述对关键数据字段和运算符的分析。
> 3.
> 因子创造:
> 模拟执行:基于上述分析,描述如何创造新的ATOM Alpha因子
> 约束:强调每个Alpha因子仅使用一个数据字段。
> 约束:强调每个Alpha因子使用的运算符数量不超过8个
> 约束:如果字段类型是VECTOR,
> 必须要用Vec_开头的运算符进行预处理。
> 记录:清晰描述所创造的Alpha因子的逻辑 (使用伪代码或自然语言描述)
> 并解释其经济学含义。



> [!NOTE] [图片 OCR 识别内容]
> Alpha.md
> BetaPlus_A_S...0210904.md
> 操作符详解.docx
> ZhuDong_To.. mmary_CNmd
> alpha_simulation_reportmd
> ZhuDong_To...He_GuanLi.md
> ChromeDriver 修复说明.md
> Active_Portfo.
> Summarymd
> CLAUDE.md
> Advances_in_.._Investing.md
> GEMINI.md
> The_Event_D..Asif_Suria.md
> 示例工作流
> The_Element._Investing.md
> operators_2025.cSV
> High_Dimensi..Summarymd
> 股票类
> Improved_Est..Summarymd
> LICENSE.chromedriver
> Multi_Period_..
> Summarymd
> Portfolio_Opti..Summary md


在对话中首次使用MCP会需要你的确认，直接选第三个全部允许即可。


> [!NOTE] [图片 OCR 识别内容]
> WriteTodos
> Set
> 8
> todo(s)
> ?
> get_datasets
> (worldquant-brain-platform
> MCP
> Server) {"region"
> IND"
> instrument_type"
> EQUITY" , "delay":1}
> MCP Server:
> worldquant-brain-platform
> Tool: get_datasets
> AlloW execution
> Of MCP
> tool "get_datasets
> from
> Server
> worldquant-brain-platform"?
> 1.
> Yes,
> allOW
> once
> 2.
> Yes, always
> allow tool "get_datasets"
> from
> SerVer
> worldquant-brain-platform"
> 3.
> Yes, always
> alloW all
> tools
> from
> Server
> worldquant-brain-platform"
> 4.
> suggest changes
> (esc)
> get_pyramid_multipliers
> worldquant-brain-platform
> MCP
> Server)
> {}
> Waiting
> for
> USer
> confirmation.
> Using:
> 2
> GEMINI.md
> files
> 1
> MCP
> SerVer
> ~/CodeProject /consultant
> (feat/stratified-super-alpha* )
> 00
> sandbox (see
> /docs )
> pro
> No ,


Gemini会自己制定Todo List。


> [!NOTE] [图片 OCR 识别内容]
> Todo
> 0/8
> completed
> (ctrltt
> to toggle)
> Perform
> a
> broad search
> for
> ALL datasets
> in
> the
> IND region
> t0
> identify
> available
> data sources,
> 35
> the previous
> specific search yielded
> Zero
> results.
> Analyze
> the
> list
> 0f
> IND datasets
> and select high-multiplier categories
> (News
> Analyst ,
> Sentiment )
> for deeper
> investigation
> Develop
> and
> simulate
> a
> batch
> 0f
> ATOM Alphas
> (Round
> 1)
> for
> IND using
> the selected
> datasets。
> Analyze
> Round
> 1
> results
> and  select
> the
> best
> candidates
> for optimization。
> Run
> Multi-Sim
> (Round
> 2)
> optimizing
> the
> best
> candidates
> With operators
> Run
> get_submission_check
> on
> promis-
> IND alphas
> Iterate
> research
> With
> new datasets
> 0r
> complex expressions
> i
> initial alphas
> fail。
> Generate
> Final
> Research Report
> for
> the
> IND
> Alpha
> ing


## 学生优惠获取

最后是学生优惠的获取，首先打开这个链接  [[链接已屏蔽])

点击 Get Offer


> [!NOTE] [图片 OCR 识别内容]
> Gemini
> Free for Students
> What Gemini Can Do
> ~
> Subscriptions
> About Gemini
> C
> @ d O 疋
> Get offer
> Google Gemini:
> Free Pro Plan forStudents。
> Free for 1 year: Get more access to our most accurate model Gemini 3 Pro, unlimited image uploads;
> Pro-level image generation, customized quizzes and advanced learning tools like NotebookLM, plus
> 2 TB storage. Just for Students。
> Get offer
> Terms apply
> HeO


然后会出现一个需要填写表格的页面，我已经领取了所以页面不同。如果能出现填表页面说明网络质量是比较好的，支持获取。

复制上方的URL然后去 ***某海鲜市场。*** URL类似这样：

```
[链接已屏蔽]
```

接下来就可以在Gemini CLI愉快地使用Gemini 3 Pro了。

## 在服务器中使用Gemini CLI

在服务器中可能遇到没有权限导致安装失败的情况，这时候需要先安装NVM并激活：

```
curl -o- [链接已屏蔽] | bash
```

```
source ~/.bashrc
```

然后安装Node.js

```
nvm install 22 && nvm use 22
```

输入  `node -v`  确认版本号是否为 v22.x.x

重新安装Gemini CLI

```
npm install -g @google/gemini-cli
```

**在这一步可能又会出问题，比如一直在转圈，可以看一下我的解决办法：**

首先通过npm全局安装pnpm

```
npm install -g pnpm
```

输入 pnpm -v 应该显示 10.24.0 版本号

设置pnpm的镜像源：

```
pnpm config set registry [链接已屏蔽]
```

运行

```
pnpm setup
```

复制输出的内容并运行，比如我的就是：

```
source /home/ubuntu/.bashrc
```


> [!NOTE] [图片 OCR 识别内容]
> (base)
> ubuntu@VM-12-12-ubuntu:
> Wqb$
> pnpm setup
> Appended
> new lines
> to
> /home /ubuntu/ .bashrc
> Next configuration changes Were made:
> export PNPM_HOME=" /home/ubuntu/ . local/share/pnpm"
> Case
> $PATH:
> i
> 米'
> $PNPM_HOME:
> export
> PATH-" $PNPM_HOME: $PATH"
> eSac
> To
> start using pnpm,
> run:
> SOUrCe
> /home /ubuntu/ .bashrc
> ")


再次安装，警告不用管：


> [!NOTE] [图片 OCR 识别内容]
> (base)
> ubuntu@VM-12-12-ubuntu:~/wqb$
> SOUrCe
> /home /ubuntu/ .bashrc
> (base)
> ubuntu@VM-12-IZ-ubuntu:~ /wqb$ pnpm add -9 @googlelgemini-cli
> Down
> loading googleapis@137.1.0:
> 11.20 MB/11.20 MB, done
> WARN
> 1
> deprecated  subdependencies
> found: node-domexception@l. 0.0
> Packages:
> +498
> ff++十十十十
> Progress:
> resolved 503, reused
> 0
> downloaded 498,
> added 498,
> done
> /home/ubuntu/ . local/share/pnpm/global/5:
> @google/gemini-cli
> 0.18.4
> Warning
> Ignored build scripts: node-pty, protobufjs,
> tree-sitter-bash.
> Run
> pnpm approve-builds
> to pick which dependencies should
> be allowed
> to
> run
> scripts。
> Done
> i
> 10.85
> using pnpm V10.24.0
> (base)
> ubuntu@VM-12-Iz-ubuntu:~/wqb$ gemini
> Version
> AC
> (base)
> ubuntu@VM-12-Iz-ubuntu:~/wqb$ gemini
> --Version
> 0.18.4
> -9"


## 服务器中无法登陆Gemini的问题解决方案

有的朋友通过账号连接会出现输入验证码一直 fail 的情况，其实是因为服务器无法连接到 Google 的服务，解决办法如下。

前置条件： **本地电脑** 已开启梯子，查看你本地梯子的端口（本文以  `7890`  为例）

在VS Code中按下 `Ctrl+Shift+P`  ，输入并选择  `Remote-SSH: Open Configuration File`

选择你的配置文件，我的是： `Users/orange/.ssh/config`

```
 Host 你的服务器别名 (例如 ubuntu20.04LTS)   HostName 123.123.123.12   User root   IdentityFile ~/Downloads/key.pem   # 👇 添加下面这一行（关键！）   # 格式：RemoteForward <服务器端口> 127.0.0.1:<本地端口>   RemoteForward 7890 127.0.0.1:7890
```

**记得保存文件**

在 VS Code 中按下  `Ctrl + ,` （Mac 是  `⌘+,` ） 打开设置，点击右上角的  **“打开设置(JSON)”**  图标。

在配置文件的大括号  `{ ... }`  中添加以下内容：

```
 "terminal.integrated.env.linux": {     "http_proxy": "[链接已屏蔽]     "https_proxy": "[链接已屏蔽]     "all_proxy": "[链接已屏蔽]   }
```

**记得再次保存文件**

然后按下快捷键  `Ctrl+Shift+p` （Mac是  `⌘+Shift+p ` ）输入  `Developer: Reload Window`

在终端输入  `curl -I [链接已屏蔽] ` 如果返回  `HTTP/1.1 200 OK ` 说明配置成功

在终端中输入 `gemini` ，选择 **用账户登录** ，打开给出的链接，复制验证码，即可使用Gemini。

**最后，希望大家在AI助力下，VF⬆️WF⬆️塔⬆️Genius⬆️**

---

### 帖子 #19: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子构造 】Alpha模板库来自社区的馈赠为你的72变添砖加瓦Alpha Template_37117908343831.md
- **讨论数**: 26

最近大趋势下，想必大家都在使用 72变之类的功能，而72变中，作者提供了一套模板，出货率还不错，不过在此基础上，我通过论坛，让大模型又总结了一份Alpha模板，如标题所言，这份模板均来自社区，所以是来自社区的馈赠

我自己用下来，出货率还不错，和内置模板相当，甚至还能更好一点，不过大家还是要自行评估一下，部分来自社区的论坛也存在过拟合的风险，如有帮助，欢迎点赞，如有错漏，请帮忙指出

```
    ## 模板格式说明

    每个模板使用以下占位符格式：
    - `<ts_op/>` - 时间序列操作符，如 `ts_rank`, `ts_mean`, `ts_delta`, `ts_ir`, `ts_stddev`, `ts_zscore`
    - `<group_op/>` - 分组操作符，如 `group_rank`, `group_neutralize`, `group_zscore`
    - `<vec_op/>` - 向量操作符，如 `vec_avg`, `vec_sum`, `vec_max`, `vec_min`, `vec_stddev`
    - `<field/>` - 数据字段占位符
    - `<d/>` - 时间窗口参数，常用值: `{5, 22, 66, 126, 252, 504}`
    - `<group/>` - 分组字段，如 `industry`, `sector`, `subindustry`, `market`

---

### 帖子 #20: 【Community Leader -因子筛选与组合⭐】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得（附提示词）经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】2025 AIAC冠军比赛心得以及当前使用iflow cli的心得附提示词经验分享_37014730112023.md
- **讨论数**: 61

参加2025 AIAC，有幸获得第一，在此文，我将分享使用AI的因子构造和比赛心得，希望能为大家提供一些有价值的参考。

首先要感谢weijie老师，kunqi老师的培训和帮助，还有论坛以及群内热心consoltent的分享。

我是1月注册，4月有条件顾问，7月正式顾问。

期间参加了IQC（260名），GAC（33名），MAPC（8名），AIAC（1名）。

### 一、比赛总结

现在来看看我比赛的提交情况：


> [!NOTE] [图片 OCR 识别内容]
> 各区域阿尔法数量分布对比
> 200
> 阿尔法总数
> super alpha 数虽
> 175
> ppa alpha 数量
> 150
> 125
> I00
> GLB
> ASI
> EUR
> USA


比赛大致思路：

因为我原来没有通过LLM方式进行过整体的alpha发掘，所以一开始就没有打算交很多的比赛alpha，所以选择parent 的策略是根据低prodcorr和performances表现，根据规则一个多个super可以对应同一个parent，然后我为每个region选了一个作为parent，然后在不同的数据集用代码跑出child，我认为这样可以既有关联性也有多样性。

比赛的sa思路，是参考了 有一次去年iqc比赛冠军培训的思路，我记得她说用15个alpha组出来的super 后面来看os表现也不错。然后我本身每个reigon的alpha数量不算多，所以按照最大团算法，可以在保证多样性的同时用较少的alpha组出多个super并且通过相关性检查。

下面说说我比赛的AI代码思路：

*1、把parents有关的所有信息都丢给AI，然后让AI出表达式（5～10个）*

*2、检查表达式正确性，进行回测（multi）*

*3、分析回测结果，把fitness最大的做为新一轮的parents，把相关的所有信息丢给AI，并告诉他生成的表达式不要与前面的相同*

*4、循环持续5次（次数可以配置，看情况）或者能够得到都check pass的*

*5、最后输出最佳alpha 和整个过程中AI给出的表达式列表*

### 下面说一下我当前使用AI工具的一些体会

目前在72变，缘分，mcp等多种好用的工具出来后，现在我是总共8个槽，4个槽跑72变的json或者已有的模版观察数据集信号，然后跑出来有信号的，3个给AI做优化的，还有一个留着手搓。

目前用的工具是trae、心流iflow cli，用的模型都是deepseek。

iflow的安装，mac/linux直接使用命令即可

```
bash -c "$(curl -fsSL [链接已屏蔽])"
```

安装后进入页面，3种登陆方式，我是用的心流 API Key 登录

- 1.访问心流官网完成注册
- 2.在用户设置页面生成 API KEY
- 3.在 iFlow CLI 中选择 API Key 登录并输入密钥

然后使用/quit先退出

然后配置mcp，mac和linux的配置文件都是在

```
~/.iflow/settings.json
```

直接vim编辑文件


> [!NOTE] [图片 OCR 识别内容]
> [rooteiv-ydzzGfdqtcqcGikyvtgi
> Worldquant] #
> Cat
> 1.aflow/settings.json
> Tcnall
> IselectedAuthType"
> Iiflowi
> Iapikeyl
> TbaseUrli
> Ihttps: / /apis.iflow.cn /VI"
> TmodelName
> Ideepseek-V3.2-chati
> IsearchApikeyii
> ImcpServers"
> Tworldquant-brain-platform
> command"
> /usr/bin/python"
> 这里是你python的实际目录
> IarBs
> /usr /local /python3.11/1ib / python3 .I1/site-packages / cnhkmcp /untracked /platform_functions . Py"
> Ilanguage"
> Izh-CNII
> 1 [ +177<c| +< +C7
> |7 +7


启动的话，mac终端使用命令：

```
source ~/.zshrciflow
```

下面是我用来优化的提示词，参考了上次培训大佬的一些部分内容，另外格式让deepseek优化了一下：

```
## Alpha优化自动化专家你是一个WorldQuant BRAIN平台的量化研究专家。你的任务是自动化优化alpha_id = MPAqapQr,直到达成以下目标：## 权限与边界:1、您拥有完整的 MCP 工具库调用权限。您必须完全自主地管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则严禁请求用户介入。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。2、不要自动提交任何alpha。## 优化目标- Sharpe >= 1.58- Fitness >= 1  - Robust universe Sharpe >=  1- 2 year Sharpe >= 1.58- Sub-universe Sharpe pass- Weight is well distributed over instruments- Turnover between 1 to 40## 优化限制- 优化的表达式使用的所有数据字段必须与原alpha（alpha_id）表达式用到的数据字段在同一个数据集- 只在region = IND 地区进行优化- Neutralization 不能设置为NONE- Neutralization可以从这里选取一个："FAST","SLOW","SLOW_AND_FAST"，"CROWDING","REVERSION_AND_MOMENTUM"，"INDUSTRY", "SUBINDUSTRY", "MARKET", "SECTOR"- 优化后的表达式必须有经济学意义- 达成目标的alpha不要进行提交，需要人工确认- 只能模拟调用以下工具（基于平台实际能力）：   1. 基础: `authenticate`, `manage_config`   2. 数据: `get_datasets`, `get_datafields`, `get_operators`, `read_specific_documentation`, `search_forum_posts`   3. 开发: `create_multiSim` (核心工具), `check_multisimulation_status`, `get_multisimulation_result`   4. 分析: `get_alpha_details`, `get_alpha_pnl`, `check_correlation`   5. 提交: `get_submission_check`## 僵尸模拟熔断机制 (Zombie Simulation Protocol)- 现象: 调用 `check_multisimulation_status` 时，状态长期显示 `in_progress`。- 判断与处理逻辑:    1. 常规监控 (T < 15 mins): 若认证有效，继续保持监控。    2. 疑似卡死 (T >= 15 mins):        - **STEP 1: 立即调用 `authenticate` 重新认证。        - **STEP 2: 再次调用 `check_multisimulation_status`。        - **STEP 3: 若仍为 `in_progress`，判定为僵尸任务。        - **STEP 4: **立刻停止**监控该 ID，重新调用 `create_multiSim` (生成新 ID) 重启流程。## 自动化工作流你需要循环执行以下7个步骤，直到成功或达到最大尝试次数(100次)：### 步骤1: 认证登陆使用authenticate工具，从配置文件读取凭据：- 文件：user_config.json认证后，可以保持登陆状态6小时，超时需要重新认证### 步骤2: 获取源alpha信息使用get_alpha_details工具，参数：alpha_id提取关键信息：- 源表达式- 当前性能指标(Sharpe/Fitness/Margin)- 当前settings(特别是instrumentType)### 步骤3: 获取平台资源同时调用三个工具：1. - 读取文件获取所有可用操作符：operators.md 2. get_datasets - 参数：region=IND, universe=TOP500, delay=13. get_datafields - 参数：region=IND, universe=TOP500, delay=1重要规则：- 表达式必须严格按照operators返回的格式填写- 如果数据是vector类型，必须先使用vec_开头的operator- 表达式只能使用1-2个不同的数据字段- 同一字段可以多次使用- 使用多字段时尽量选择同数据集的字段### 步骤4: 生成优化表达式基于以下原则生成新表达式：1. 必须有经济学意义2. 对比源表达式，尝试改进3. 可以从以下数据类型中选择：   - 动量策略：使用价格、成交量变化   - 均值回归：使用价格偏离均值的程度   - 质量因子：使用财务指标   - 技术指标组合4. 论坛寻找相关信息5. 尝试更多的操作符6. 尝试更多的数据字段生成思路示例：- 如果源表达式是单字段，尝试增加第二个相关字段- 如果源表达式复杂，尝试简化- 添加合理的数学变换（rank, ts_mean, ts_delta等）每次生成5到8个表达式### 步骤5: 创建回测单个表达式的回测使用create_simulation.同时测试2个以上数量的表达式，使用create_multiSim.回测时的参数设置：- 保持：instrumentType, region, universe, delay等不变- 可以调整：decay, neutralization（尝试不同值）### 步骤6: 检查回测状态回测成功后，会返回链接或alpha_id，使用：- get_submission_check检查状态和初步结果- 如果需要，使用get_SimError_detail检查错误### 步骤7: 分析结果同时调用：1. get_alpha_details - 获取详细性能2. get_alpha_pnl - 获取PnL数据  3. get_alpha_yearly_stats - 获取年度统计## 循环逻辑每次循环后评估：1. 如果达到所有目标 → 停止循环，输出成功报告,alpha id2. 如果未达到 → 分析失败原因，调整策略，继续下一轮3. 记录每次尝试的表达式和结果用于学习## 失败分析策略- 如果Sharpe低 → 尝试不同数据字段组合- 如果Margin低 → 调整neutralization或添加平滑操作- 如果相关性失败 → 减少与现有alpha的相似度- 如果表达式错误 → 检查操作符用法和数据字段类型## 经验教训- 解决“Robust universe Sharpe”较低问题的建议：   - 使用以下运算符中的一两个：      - group_backfill      - group_zscore      - winsorize      - group_neutralize      - group_rank      - ts_scale      - signed_power   - 调整运算符中的时间参数以改善表现。   - 修改Decay参数和时间窗口参数时使用有经济含义的：1，5，21，63，252，504   - 修改Truncation和Neutralization参数。- 解决“2 year Sharpe of 1.XX is below cutoff of 1.58”：   - ts_delta(xx,days) 操作符有奇效   - 采用分域方法增强信号，如乘以sigmoid函数调整信号强度## 知识库- 目录Resources里面按照region_decay_universe_dataset的文件名，每个文件包含对应数据集的介绍，和Research Paper。## 开始执行现在开始第一轮优化。请按步骤执行，保持思考和解释。
```

下面是我的执行指令，其中我把上面的提示词保存成了alpha_better.md 文件，operators.md内容是我用ai爬取了官网页面上的operators页面内容

```
@alpha_better.md 严格按照文档流程执行，operators使用方法参见@operators.md ,自动执行，不要咨询我，除非达成了目标。
```

iflow执行过程：


> [!NOTE] [图片 OCR 识别内容]
> plan 更新待办事项列表 (3个待处理。1个进行中;
> 7个已完成)
> 已更新待办事项列表
> 新的Alpha优 化:  步骤1 -认证登陆
> (alpha_id
> OmVLW7dII
> 步骤2:  获取源alpha信息
> alpha_id
> OIVLW7dI
> 步骤3:  获取平台资源
> IND地区数据字段和操作符
> 步骤4:  生成优化表达式 -基于源alpha的经济学意义改进
> 步骤5:  创建回测测试新表达式
> 步骤6:  检查回测状态
> 步骤7:  分析结果井评估
> 第二轮优化:  步骤4 -生成新表达式 (针对Robust universe Sharpe)
> 口第二轮优化:  步骤5
> 创建回测测试新表达式
> 口第二轮优化:  步骤6
> 检查回测状态
> 第二轮优化:  步骤7 -分析结果井评估
> exprI (按esc取消 ,
> IBm 255)
> 加载:
> MCP
> 服务
> (ctrltt 查看)
> 思考:开启
> (tab切]换) YOLO模式
> (shift
> tab
> alt
> 切换
> 输入消息或@文件路径


通过上面的过程可以看到，还是能完整按照md文件里预设的流程步骤进行的。

ps：要他自动运行，要记得开启“思考+yolo”模式。

下面是优化成功的一个alpha和iflow的报告。


> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> Thame: IND Region Theme
> Data Sat Alpha
> ReBUIT
> Jpha
> Irmlo thEme: INDIDTIFUNDAWENTAL *1
> SimIlatimn
> Settings
> IIIUIBNLT
> Rl
> Umivel
> LIOUAa
> Uetg
> Oelg
> TNCUI
> Nuralzlol
> Cayleuilr
> NaN Hnuliny
> UI HUIII
> MHT
> ABBregate Data
> Sharr
> HetUTT
> Lru 
> Larpr
> 3.47
> 17.519
> 3.40
> 16.78%
> 6.629
> 19.169o0@
> CUUIC
> TURSDJ
> Fusl CuIessIuI
> R
> WerIl
> UU
> N
> STTC
> T
> Lole COUH
> CCI
> 2013
> 1GOJm
> LeD
> LS2
> 909
> Clone Alpha 
> Z0IA
> 1545m
> 3e.57u
> 115
> 419
> 1955q
> 71749
> g
> 777
> 19719
> 19,-1a
> 7 |G
> 20.47
> N Chart
> Pnl
> 17.454
> 150
> 1RS
> 1591
> 1SIm
> 14.57u
> 1.744
> 15.51
> 2019
> 171
> T
> 1
> !
> 1552m
> 20.39兑
> 1.30
> 35.23
> 1L
> 
> 3T9C
> 111
> 2022
> 16.979
> 11
> 392
> 132
> 17T5
> SU7n
> TJ
> 977
> OOoK
> Investability constrained
> ABBreBate Data
> Uratl?
> 2015
> 2016
> 201
> 2016
> 2020
> 2021
> 23
> 2.48
> 8.02%
> 2.47
> 12.41%
> 5.25%
> 30.9520@
> Correlation
> SelfCOTTelatION
> VurImJT
> MinImUT
> LJst Hun; 1131
> 12115/2025,2:09ul
> OS Testing Status
> RerIOO
> 0.3009
> -0.0185
> Prod Correlatlon
> VurImJT
> JIMUM
> LJst Hun; 1131
> 12115/2025,2:09u
> 11PENDING
> 0.5756
> -0.2236
> 1诱求临嚣
> BOLUOTIUOUBIUAIIC0I
> 雁开
> 灞空
> SngI
> Sale
> Marn



> [!NOTE] [图片 OCR 识别内容]
> Alpha优化总结
> 指标对比
> 指标
> 初始 (NA0ZJ3a)
> (MOZdEw)
> 娈化
> Sharpe
> 2.25
> 3.47
> +548
> Fitness
> 1.90
> 3.40
> +79*
> 换手宰
> 0.2046
> 0.1751
> 148
> 2年 Sharpe
> 1.12 (^)
> 1.88
> 582
> Robust universe
> 1.00
> 1.07
> +79
> Pnl
> 031
> 17 .371
> +152
> Returns
> 14 .528
> 16 .78%
> +163
> Drawdown
> 792
> 6.62%
> +148
> 优化信息
> 日期:  2025-12-14
> 耗时:  466分钟
> (7时46分钟 )
> 轮次:  13轮循环
> 优化手段
> 字段替换:
> risk_sCore
> aVerage
> SCOre
> 分组优化: industry
> sector
> (+37] Robust Sharpe)
> 参数调优:  5048囱0
> std=4控制分布
> 结构固定
> Broup_backfill嵌套 Broup_Vector_neut
> 批量测试: create_multisim高效迭代
> 验证通过
> 权重分布:  均匀
> 相关性:  自相关0.3009
> 生产相关0.5756 (均<0.7)
> 激励乘数:  2.5x (IN0主题
> 金字塔 )
> 最终状态
> 所有目标达成
> 性能全面提升
> 聂终


Iflow使用下来跟上次培训的大佬比还是有差距，出货差不多也就能做到一天一个。

期间遇到的问题：

1、有的时候也不能一直持续运行，会让你确认，这个没有好的办法，我一般都是运行半小时看一下，但是大多数时候都是可以持续执行；

2、有时候会连不上worldquant（此时需要/quit再启动）

3、优化轮次很多的时候，会自动创建文件，不过多是文件名包含alphaid的，优化后清理就行。

最后说一下是用过的cli对比：

Cli模式的国内还有qwen的cli，不过也是阿里系的，跟iflow差不多，感觉没有iflow方便。

字节的有个ve cli，不过每天只有500w的token，我用了一天最后扣了2块。。。

我用心流主要是他可以在“思考+yolo模式”可以一直持续优化不用人工介入而且免费～

另外，不同的cli应该是可以同时使用的，我同时在一个linux服务器上使用过iflow和ve cli。

最后的最后，如果大家觉得本文对你有帮助的话，点个赞再走吧～

---

### 帖子 #21: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享.md
- **讨论数**: 36

分享下我判断因子是否值得提交的一些经验，希望小伙伴们能有所收获。

一个因子值不值得提交，一个是看因子本身的指标，一个是对组合的增益情况。

对我个人而言，后者的重要性一般会大于因子本身的指标（这是在 **因子指标合格的情况下** 的）；

一般很难找到所有指标对performance都是正面明显的。所以你需要在各个指标之间权衡。

## 根据is performance 的正负面影响判断：

### 可提交的情况

1. fitness 是排首位的，一般fitness有明显增益，margin和sharpe的增益不明显，或者稍微一点负面影响，我会选择提交；
2. 95%的情况下，fitness 对最近3-5年 的performance 有明显的负面影响（比如-0.1），不提交;
3. sharpe 和fitness,margin有增益，但是returns稍微有些负面影响，提交；


> [!NOTE] [图片 OCR 识别内容]
> N
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 7.95
> 0,03
> 6.48 %
> -0.02
> 5.50
> 0.01
> 5.98 %
> -0.02
> 0.48 %
> 0,01
> 18.46 %oo -0.01
> 川
> IS Performance After Submission (Equity, EUR, Delay-1 alphas)
> :
> Combined performance data is shown for all Equity, EUR, Delay-1 alphas. Submitting this alpha will not effect the combined performance ofyour other alphas
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 2013
> 9.23
> 0.03
> 7.71 %
> -0.03
> 6.33
> 0.00
> 5.87 %
> -0.05
> 0.19 %
> 0.00
> 15.23 %o。
> -0.07
> 2014
> 10.36
> -0.11
> 6.14 %
> 0.02
> 7.52
> -0.14
> 6.59 %
> -0.10
> 0.17 %
> 0.00
> 21.45 %o。
> -0.28
> 2015
> 7.49
> -0.06
> 6.54 %
> -0.01
> 4.93
> -0.09
> 5.42 %
> -0.10
> 0.26 %
> 0.00
> 16.59 %o。
> -0.24
> 2016
> 6.42
> 0.12
> 6.39 %
> 0.02
> 4.22
> 0.11
> 5.40 %
> 0.08
> 0.42 %
> -0.01
> 16.90 %o。
> 0.29
> 2017
> 7.27
> 0.00
> 6.37 %
> 0.02
> 3.98
> 0.00
> 3.75 %
> 0.00
> 0.14 %
> -0.01
> 11.78 %o。
> 0.05
> 2018
> 7.54
> 0.06
> 6.35 %
> 0.02
> 4.60
> 0.02
> 4.66 %
> -0.03
> 0.44 %
> -0.01
> 14.69 %o。
> -0.06
> 2019
> 8.82
> 0.10
> 6.35 %
> 0.02
> 5.69
> 0.07
> 5.20 %
> 0.00
> 0.21 %
> 0.00
> 16.39 %o。
> 0.07
> 2020
> 7.06
> 0.05
> 6.54 %
> 0.02
> 5.19
> 0.05
> 6.75 %
> 0.04
> 0.48 %
> 0.01
> 20.62 %oo
> 0.14
> 2021
> 9.60
> 0.02
> 6.18 %
> -0.02
> 7.56
> 0.00
> 7.76 %
> -0.03
> 0.15 %
> 0.00
> 25.1
> 9oo
> 0.01
> 2022
> 9.06
> 0.05
> 6.35 %
> -0.01
> 7.62
> 0.03
> 8.84 %
> -0.04
> 0.25 %
> 0.01
> 27.87 %oo
> -0.03
> 2023
> -0.93
> 0.14
> 5.07 %
> 0.00
> -0.27
> 0.07
> 1.08 %
> 0.20
> 0.29 %
> 0.00
> -4.26 %oo
> 0.78
> Pnl


### 什么情况下不会提交：

1、margin不符合地区的最低要求，不提交

3、fitness 最近几年明显负面影响，不提交( 超过1个年份<-0.1)

4、sharpe  最近几年明显负面影响 ，不提交( 超过1个年份 <-0.1)

3、多个指标对组合负面明显过大，即使自相关性低，也不提交

很难一一列举对performance 影响的所有情况，是否提交这个因子，根据组合影响，个人情况判断。

### 从因子本身的指标来看：

1、sharpe>=1 ,fitness>=0.6 的前提下

margin 必须达到各地区margin要求的最低标准，我一般要求比最低标准高万分之五（USA，eur）,glb和ASI 地区的margin有时候比较难找到超过15的，在没有选择的情况下，一般ASI 最低14，15；GLB 14，15（少部分情况下会只要求>10【点塔】）

2、pnl线的波动比较小，向上，sharpe线 **不往下走；**

3、ASI 地区 还会观察下jpn的表现，如果jpn明显表现不佳或者或者kor表现明显大于其他地区的表现，不会提交

以上是我个人的一些经验，可能考虑还欠缺一些其他的点， **如果小伙伴有其他好的 判断方法，期待你评论区的分享**

**如果想要保证combine 的稳定，我个人的经验是 绝对不要提交margin不合格、fitness 负面影响过大、最近3年sharpe 线明显下降，pnl趋于厂 的因子（个人经验）**

**最后，给大家看看我现在的combine 情况，希望国区顾问的combine 都能保持稳定增长。**


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.38
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 3.17
> Reached Grandmaster
> 0.5
> Combined Power Pool Alpha Performance
> 2.63


---

### 帖子 #22: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析.md
- **讨论数**: 14

自记录combine更新以来，已经连续5个月保持三个combine大于2了，上次combine更新到10月底，所以我选择了7-10月的提交的因子做一些指标分析，希望对大家能有所启发。


> [!NOTE] [图片 OCR 识别内容]
> UpdateDate
> Combined Alpha Performance
> Combined Selected Alpha Performance
> Combined Power Pool Alpha Performance
> 2025/8/1
> 2.83
> 3.54
> 2.76
> 20259/11
> 2.86
> 3.19
> 2.85
> 2025/10/6
> 2.7
> 2.9
> 2.52
> 2025/11/8
> 2.87
> 2.74
> 2.49
> 2025/12/8
> 2.8
> 2.73
> 2.6


**总体结论：**

- 保持提交数量，每天2-3个最佳
- 坚持diversity，多region、多category
- 多交ATOM
- 多交risk neut
- 开启maxtrade
- ppa按照ra的标准来交

**具体分析：**

- 整体情况

7-10月总共提交290个regular的alpha，覆盖USA、GLB、EUR、ASI、AMR、JPN等6个地区的70个category，其中atom 204个， risk_neut 207个，maxtradeon 260 个，平均shape1.81, fit 1.19, margin 0.0021, self_corr 0.4


> [!NOTE] [图片 OCR 识别内容]
> Region
> submit
> Cut
> atom
> Cut
> regular_
> Cut
> risk nent
> Cut
> Iartrade
> Cut
> prramids_
> Cut
> sharpe_arg
> ftuess_arg
> return_arg
> Uargln_ar8
> selfcorr_arg
> prodcorr_arg
> USA
> 1.73
> 1.26
> 0748
> 00280
> ECR
> 1.13
> 0466
> 00210
> ASI
> 1.18
> 0321
> 00190
> GLB
> 1.13
> 0554
> 00170
> 4及
> 2
> 1.36
> 0904
> 00330
> JPN
> 1.12_
> 0616
> 00230
> Total
> 0610
> 00210


- category分析

下图是7-9月的点塔情况，四大地区的基本上都能覆盖，除了analyst和fnd外基本都是点满即止


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> HKG
> JPN
> AR
> [0
> -nahst
> rolr
> Earninss
> Fundamsnzs
> ITCSInc
> ITIUET
> In-NTT T
> TIcc
> NJel
> NEs
> 0oti3n
> O-her
> Price 'lme
> Fisk
> SEniTET
> ShOT Iere 
> TICi
> IEJa


- 中性化分析

除了amr、jpn这两个小地区外，提交的alpha都是risk neut的，具体中性化展示如下：


> [!NOTE] [图片 OCR 识别内容]
> 量化因子中性化 (Neut) 整体分布
> (Risk Neut = 统计 /拥挤度/快慢因子等6类)
> Risk Neut细分类型分布
> Non-Risk Neut
> 4~
> 28.6%
> 15.59
> 3.23
> 19
> 71.4%
> 20.88
> Risk Neut
> AND
> SLow
> FAsT
> AND
> SLON
> CROWDING
> 4
> TuST
> STATISTICAL
> NOIMENTUM
> REVERSION


- MaxTrade 分析

绝大部分的alpha开启了MaxTrade  设置，占比约89.6%，只在AMR 和部分GLB的因子中没有开启

- PPA 分析

累积交了192个ppa的alpha，占比约66%，两类因子的关键指标差别不是很大，基本提交的ppa也是按照ra的要求在提交，具体对比如下


> [!NOTE] [图片 OCR 识别内容]
> Regular困子与非Regular困子关键指标对比
> Margin 数值
> 0 000
> 0.001
> 0.002
> 0,003
> 0 004
> 0.005
> 非Regular因子
> Regular因子
> 0.0020
> Margin指标
> Margin
> 0.0021
> 1.235
> Fitness
> 1.170
> 1.853
> Sharpe比率
> 1.783
> 0.00
> 0.25
> 0,50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Sharpe比率
> Fitness 数值


---

### 帖子 #23: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md
- **讨论数**: 14

自记录combine更新以来，已经连续5个月保持三个combine大于2了，上次combine更新到10月底，所以我选择了7-10月的提交的因子做一些指标分析，希望对大家能有所启发。


> [!NOTE] [图片 OCR 识别内容]
> UpdateDate
> Combined Alpha Performance
> Combined Selected Alpha Performance
> Combined Power Pool Alpha Performance
> 2025/8/1
> 2.83
> 3.54
> 2.76
> 20259/11
> 2.86
> 3.19
> 2.85
> 2025/10/6
> 2.7
> 2.9
> 2.52
> 2025/11/8
> 2.87
> 2.74
> 2.49
> 2025/12/8
> 2.8
> 2.73
> 2.6


**总体结论：**

- 保持提交数量，每天2-3个最佳
- 坚持diversity，多region、多category
- 多交ATOM
- 多交risk neut
- 开启maxtrade
- ppa按照ra的标准来交

**具体分析：**

- 整体情况

7-10月总共提交290个regular的alpha，覆盖USA、GLB、EUR、ASI、AMR、JPN等6个地区的70个category，其中atom 204个， risk_neut 207个，maxtradeon 260 个，平均shape1.81, fit 1.19, margin 0.0021, self_corr 0.4


> [!NOTE] [图片 OCR 识别内容]
> Region
> submit
> Cut
> atom
> Cut
> regular_
> Cut
> risk nent
> Cut
> Iartrade
> Cut
> prramids_
> Cut
> sharpe_arg
> ftuess_arg
> return_arg
> Uargln_ar8
> selfcorr_arg
> prodcorr_arg
> USA
> 1.73
> 1.26
> 0748
> 00280
> ECR
> 1.13
> 0466
> 00210
> ASI
> 1.18
> 0321
> 00190
> GLB
> 1.13
> 0554
> 00170
> 4及
> 2
> 1.36
> 0904
> 00330
> JPN
> 1.12_
> 0616
> 00230
> Total
> 0610
> 00210


- category分析

下图是7-9月的点塔情况，四大地区的基本上都能覆盖，除了analyst和fnd外基本都是点满即止


> [!NOTE] [图片 OCR 识别内容]
> Category
> USA
> GU
> EUR
> CAN
> NOR
> TWNN
> HKG
> JPN
> AR
> [0
> -nahst
> rolr
> Earninss
> Fundamsnzs
> ITCSInc
> ITIUET
> In-NTT T
> TIcc
> NJel
> NEs
> 0oti3n
> O-her
> Price 'lme
> Fisk
> SEniTET
> ShOT Iere 
> TICi
> IEJa


- 中性化分析

除了amr、jpn这两个小地区外，提交的alpha都是risk neut的，具体中性化展示如下：


> [!NOTE] [图片 OCR 识别内容]
> 量化因子中性化 (Neut) 整体分布
> (Risk Neut = 统计 /拥挤度/快慢因子等6类)
> Risk Neut细分类型分布
> Non-Risk Neut
> 4~
> 28.6%
> 15.59
> 3.23
> 19
> 71.4%
> 20.88
> Risk Neut
> AND
> SLow
> FAsT
> AND
> SLON
> CROWDING
> 4
> TuST
> STATISTICAL
> NOIMENTUM
> REVERSION


- MaxTrade 分析

绝大部分的alpha开启了MaxTrade  设置，占比约89.6%，只在AMR 和部分GLB的因子中没有开启

- PPA 分析

累积交了192个ppa的alpha，占比约66%，两类因子的关键指标差别不是很大，基本提交的ppa也是按照ra的要求在提交，具体对比如下


> [!NOTE] [图片 OCR 识别内容]
> Regular困子与非Regular困子关键指标对比
> Margin 数值
> 0 000
> 0.001
> 0.002
> 0,003
> 0 004
> 0.005
> 非Regular因子
> Regular因子
> 0.0020
> Margin指标
> Margin
> 0.0021
> 1.235
> Fitness
> 1.170
> 1.853
> Sharpe比率
> 1.783
> 0.00
> 0.25
> 0,50
> 0.75
> 1.00
> 1.25
> 1.50
> 1.75
> 2.00
> Sharpe比率
> Fitness 数值


---

### 帖子 #24: Alpha Turnover降低工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP Workflow】turnover优化论坛精华版经验分享_34949059814679.md
- **讨论数**: 11

自从开始使用MCP工具，整体效率提升了很多，但是之前的MCP成功率一般，比如前面分享的 [自动化找alpha的workflow]([L2] 【MCP Workflow】一个自动化找alpha的工作流分享_34670122621207.md) ，整体成功率大约40%，但其对token的消耗是很大的，由于我的AI用的是包月套餐，整体感受没那么厉害，但是如果是按量计费的话，极端情况下，base甚至覆盖不到token的消耗。

基于上次双周会IQC中国区冠军分享的coze工作流，我发现其实我可以把目光放在更细分的领域，让AI完成一个特定的任务，而非从0开始去找alpha，让其作为一个辅助工具，可能成功率会显著提升，经过我的测试也的确如此，现在将其中一个工作流，Alpha Turnover降低工作流分享给大家，供大家参考，如果大家感兴趣，我也可以持续分享一些自己在用的，效果较好的其他专题工作流。

首先，该工作流主要是对以下文章内容的提炼，让AI跟随这些经验，去做提升工作，感谢这些作者，文章列表如下：

1. **[如何拯救高turnover因子？一文助你理解并降低因子turnover](../顾问 JR23144 (Rank 6)/[Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)**  - 109票权威指南
2. **[浅谈用hump操作符解决Sub-universe Sharpe]([Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)**  - hump操作符专题
3. **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)**  - 顾问级经验
4. **[Alpha 模版：ts_delta_limit应用举例](/hc/zh-cn/community/posts/34588105621783)**  - 高级控制技巧

```
# Alpha Turnover降低工作流

## 🎯 概述
基于BRAIN论坛经验总结，return = turnover × margin，高换手率降低margin，影响fitness score和被PM采纳的概率。本工作流通过ts_decay_linear等论坛验证的操作符，系统化降低alpha的turnover，实战中可实现**30-50%的turnover降幅**。

## 📊 论坛实证依据

### 核心理论基础
- **[如何拯救高turnover因子？一文助你理解并降低因子turnover](../顾问 JR23144 (Rank 6)/[Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)** (109票, 12评论)
- **[浅谈用hump操作符解决Sub-universe Sharpe]([Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)** (18票, 9评论)
- **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)** (25票, 11评论)

### 关键洞察
1. **基本关系**: `return = turnover × margin`
2. **核心操作符**: `ts_decay_linear`, `hump`, `ts_target_tvr_delta_limit`
3. **平台建议**: 含TVR关键词的operator优先

## 🔍 第一步：MCP工具诊断当前状态

### 使用MCP工具获取基线数据
使用 `mcp__worldquant_brain_platform__get_alpha_details()` 获取当前alpha的基线指标

### 关键指标分析
1. **当前turnover水平** (目标: 0.1~0.3)
2. **Sharpe vs Turnover权衡点**
3. **时间序列稳定性分析**

## 🔧 第二步：基于论坛实证的降turnover策略

### 策略A: ts_decay_linear平滑（论坛首推）

**理论依据**: 平台官方建议的信号平稳性优化方法

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_decay_linear(原表达式, 5)` - 1个交易周
- `ts_decay_linear(原表达式, 22)` - 1个交易月  
- `ts_decay_linear(原表达式, 44)` - 2个交易月
- `ts_decay_linear(原表达式, 63)` - 1个季度

**预期效果**: Turnover降低30-50%，Sharpe轻微下降可接受

**经济学原理**: 
- **5天** = 1个标准交易周，适合短期信号平滑
- **22天** = 1个交易月，适合月度趋势捕捉  
- **44天** = 2个交易月，适合中期信号稳定
- **63天** = 1个季度，与财报周期同步，适合基本面信号

### 策略B: hump操作符优化（Sub-universe专用）

**理论依据**: 论坛实证表明hump在控制波动性、降低换手率方面表现出色

**适用场景**: Sub-universe Sharpe表现不佳时优先考虑

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `hump(原表达式, hump=0.1)` - 轻度截断
- `hump(原表达式, hump=0.2)` - 中度截断
- `hump(原表达式, hump=0.3)` - 较强截断
- `hump(ts_decay_linear(原表达式, 5), hump=0.2)` - 周衰减+截断组合

### 策略C: 新一代TVR控制操作符

**理论依据**: 顾问分享提到平台最新推出的含TVR关键词操作符

**MCP工具实施**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.1)` - 目标10%换手率
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.15)` - 目标15%换手率  
- `ts_target_tvr_delta_limit(原表达式, volume, target_tvr=0.2)` - 目标20%换手率

### 策略D: 组合平滑技术

**基于论坛实践的组合方法**:
使用 `mcp__worldquant_brain_platform__create_multiSim` 批量测试以下表达式：
- `ts_decay_linear(ts_mean(原表达式, 5), 22)` - 周均值+月度衰减
- `hump(ts_decay_linear(原表达式, 5), hump=0.2)` - 周衰减+截断
- `rank(ts_decay_linear(原表达式, 22))` - 月衰减+排名

## 📈 第三步：MCP工具验证与选择

### 综合评估流程
使用以下MCP工具评估所有候选方案：
1. `mcp__worldquant_brain_platform__get_alpha_details()` - 获取详细指标
2. 对比原始alpha的turnover、sharpe、fitness指标

### 选择标准（基于论坛经验）
1. **优先级**: Turnover降低 > 30%
2. **可接受**: Sharpe损失 < 15%
3. **理想状态**: Fitness score提升

## 🏆 第四步：最终优化与提交准备

### 最终候选确认
使用以下MCP工具对最优候选进行最终检查：
1. `mcp__worldquant_brain_platform__get_submission_check()` - 提交检查
2. `mcp__worldquant_brain_platform__check_correlation()` - 相关性检查
3. `mcp__worldquant_brain_platform__set_alpha_properties()` - 设置属性标记

## ✅ 成功标准（基于论坛经验）
- **Turnover < 0.3** (理想 < 0.2)
- **Sharpe损失 < 15%** (可接受范围)
- **Fitness score提升** (margin改善)
- **相关性保持 < 0.7**

## 🚨 常见陷阱（论坛经验总结）

### 陷阱1: 盲目提高decay参数
**论坛洞察**: "低decay是为了刨除那些为了过相关性测试盲目提高decay的劣质因子"
**解决方案**: 优先使用操作符层面的平滑，而非decay参数

### 陷阱2: 过度优化导致信号失真
**解决方案**: 保持原始信号的经济逻辑，渐进式优化

### 陷阱3: 忽视Sub-universe表现
**解决方案**: hump操作符在Sub-universe Sharpe优化方面更直接有效

## 📚 论坛文章参考

### 必读文章
1. **[如何拯救高turnover因子？一文助你理解并降低因子turnover](../顾问 JR23144 (Rank 6)/[Commented] 如何拯救高turnover因子一文助你理解并降低因子turnover代码优化_30927669645207.md)** - 109票权威指南
2. **[浅谈用hump操作符解决Sub-universe Sharpe]([Commented] 浅谈用hump操作符解决Sub-universe Sharpe_31365517513495.md)** - hump操作符专题
3. **[VF 0.9+顾问分享：新人常见误区之Under Fitting]([L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md)** - 顾问级经验
4. **[Alpha 模版：ts_delta_limit应用举例]([链接已屏蔽])** - 高级控制技巧

### 核心操作符文档
- `ts_decay_linear(x, d)` - 平台官方推荐
- `hump(x, hump=)` - Sub-universe优化专用  
- `ts_target_tvr_delta_limit` - 新一代TVR控制

## 🛠️ MCP工具使用总结

核心MCP工具：
1. `mcp__worldquant_brain_platform__get_alpha_details()` - 获取基线指标
2. `mcp__worldquant_brain_platform__create_multiSim()` - 批量测试优化方案  
3. `mcp__worldquant_brain_platform__get_submission_check()` - 提交前检查
4. `mcp__worldquant_brain_platform__check_correlation()` - 相关性验证
5. `mcp__worldquant_brain_platform__set_alpha_properties()` - 设置属性标记

### 与手动调试对比
✅ **MCP批量测试**: 一次性测试多个ts_decay_linear参数组合
✅ **自动化评估**: 自动获取所有候选的turnover、sharpe、fitness指标
✅ **系统性对比**: 快速识别最优参数，避免网页端逐个手动测试
✅ **完整验证链**: 自动完成submission和correlation检查流程

## 🎯 实战效果展示

### Alpha 9nz6GQq 优化案例
**原始指标**:
- Turnover: 0.5083 (过高)
- Sharpe: 1.86
- Fitness: < 1.0

**使用ts_decay_linear(d=5)优化后**:
- Turnover: 0.2693 (**降低47%** ✅)
- Sharpe: 1.71 (轻微下降9% ✅)
- Fitness: 显著提升

**验证结果**: 
- ✅ Turnover成功降至目标范围内
- ✅ Sharpe损失在可接受范围内  
- ✅ 整体fitness得到改善
- ✅ 证明工作流高度有效

## 📄 第五步：生成优化报告

### 创建完整的优化记录
使用 `mcp__worldquant_brain_platform__set_alpha_properties()` 为优化后的alpha设置：
- **Name**: `TurnoverOpt_[原始AlphaID]`
- **Tags**: `["turnover_optimized", "ts_decay_linear", "forum_validated"]`
- **Description**: 记录优化前后的具体指标变化和使用的参数

### 优化报告模板
```
Alpha Turnover优化报告
=====================
原始Alpha: [AlphaID]
优化方法: ts_decay_linear(d=[参数])
优化结果:
- Turnover: [原值] → [新值] (改善[百分比])
- Sharpe: [原值] → [新值] (变化[百分比])  
- Fitness: [原值] → [新值]
- 经济学意义: [时间参数的经济学解释]
```

通过MCP工具，实现论坛验证的turnover优化策略，确保结果的可靠性和一致性。
```

同时由于大家操作符权限不同，且AI可能理解错误operator的参数，可以让AI下载一下操作符文件，保存下来，再同时作为语料提供给AI，从而减少AI出错的概率，也可参考我之前分享的关于operator的文章。

[来自MCP的operator指北，终于看懂了大多数的平台operator](../顾问 YH25030 (Rank 31)/[L2] 来自MCP的operator指北终于看懂了大多数的平台operator_34208186164631.md)

也可参考之前分享的工作流

[【MCP Workflow】一个自动化找alpha的工作流分享]([L2] 【MCP Workflow】一个自动化找alpha的工作流分享_34670122621207.md)

如大家感兴趣，多多点赞评论，后续更新更多关于MCP的探索工作流，下次再见

---

### 帖子 #25: 中文版：Alpha 解析工作流程
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP WorkFlow】一个使用MCP来给Alpha写描述并获取更多启发的工作流_34213553037335.md
- **讨论数**: 26

我们都知道，要发挥MCP的功能，就需要把它当作我们的秘书。以下是一个参考工作流，你可以让它照着做，并把Alpha表达式和Region给它，就能给你Alpha进行解释，并给你进一步点塔的启发，和撰写description的台词。

# Alpha Explanation Workflow

This manual provides a step-by-step workflow for analyzing and explaining a WorldQuant BRAIN alpha expression. By following this guide, you can efficiently gather the necessary information to understand the logic and potential strategy behind any alpha.

## Step 1: Deconstruct the Alpha Expression

The first step is to break down the alpha expression into its fundamental components:  **data fields**  and  **operators** .

For example, given the expression  `quantile(ts_regression(oth423_find,group_mean(oth423_find,vec_max(shrt3_bar),country),90))` :

- **Data Fields:**   `oth423_find` ,  `shrt3_bar`
- **Operators:**   `quantile` ,  `ts_regression` ,  `group_mean` ,  `vec_max`

## Step 2: Analyze Data Fields

Use the  `brain-platform-mcp`  tool  `get_datafields`  to get detailed information about each data field.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_datafields</tool_name> <arguments> { "instrument_type": "EQUITY", "region": "ASI", "delay": 1, "universe": "MINVOL1M", "data_type": "VECTOR", "search": "shrt3_bar" } </arguments> </use_mcp_tool>`

**Tips for effective searching:**

- **Specify Parameters:**  Always provide as much information as you know, including  `instrument_type` ,  `region` ,  `delay` ,  `universe` , and  `data_type`  ( `MATRIX`  or  `VECTOR` ).
- **Iterate:**  If you don't find the data field on your first try, try different combinations of parameters. The  `ASI`  region, for example, has two universes:  `MINVOL1M`  and  `ILLIQUID_MINVOL1M` .
- **Check Data Type:**  Be sure to check if the data is a  `MATRIX`  (one value per stock per day) or a  `VECTOR`  (multiple values per stock per day). This is crucial for understanding how the data is used.

**Example Data Field Information:**

- **`oth423_find`** : A  **matrix**  data field from the "Fundamental Income and Dividend Model" dataset in the ASI region. It represents a "Find score," likely indicating fundamental attractiveness.
- **`shrt3_bar`** : A  **vector**  data field from the "Securities Lending Files Data" dataset in the ASI region. It provides a vector of ratings (1-10) indicating the demand to borrow a stock, which is a proxy for short-selling interest.

## Step 3: Understand the Operators

Use the  `brain-platform-mcp`  tool  `get_operators`  to get a list of all available operators and their descriptions.

**Tool Usage:**   `xml <use_mcp_tool> <server_name>brain-platform-mcp</server_name> <tool_name>get_operators</tool_name> <arguments> {} </arguments> </use_mcp_tool>`  The output of this command contains a wealth of information. For your convenience, a table of the most common operators is included in the Appendix of this manual.

## Step 4: Consult Official Documentation

For more complex topics, the official BRAIN documentation is an invaluable resource. Use the  `get_documentations`  tool to see a list of available documents, and  `get_documentation_page`  to read a specific page.

**Example:**  To understand vector data fields better, I consulted the "Vector Data Fields ðŸ¥‰" document ( `vector-datafields` ). This revealed that vector data contains multiple values per instrument per day and must be aggregated by a vector operator before being used with other operators.

## Step 5: Broaden Understanding with External Research (Optional)

For cutting-edge ideas and inspiration, you can search for academic papers on arXiv using the provided  `arxiv_api.py`  script.

**Workflow:**

1. **Identify Keywords:**  Based on your analysis of the alpha, identify relevant keywords. For our example, these were:  `"short interest"` ,  `"fundamental analysis"` ,  `"relative value"` , and  `"news sentiment"` .
2. **Run the Script:**  Use the  `with-wrappers`  script to avoid SSL errors.
   ```
   python arxiv_api.py "your keywords here" -n 10
   ```

## Step 6: Synthesize and Explain

Once you have gathered all the necessary information, structure your explanation in a clear and concise format. The following template is recommended:

- **Idea:**  A high-level summary of the alpha's strategy.
- **Rationale for data used:**  An explanation of why each data field was chosen and what it represents.
- **Rationale for operators used:**  A step-by-step explanation of how the operators transform the data to generate the final signal.
- **Further Inspiration:**  Ideas for new alphas based on your research.

## Troubleshooting

- **SSL Errors:**  If you encounter a  `CERTIFICATE_VERIFY_FAILED`  error when running python scripts that access the internet, use the  `AI to help you change or make`  script to execute your command.

## Appendix A: Understanding Vector Data

Vector Data is a distinct type of data field where the number of events recorded per day, per instrument, can vary. This is in contrast to standard matrix data, which has a single value for each instrument per day.

For example, news sentiment data is often a vector because a stock can have multiple news articles on a single day. To use this data in most BRAIN operators, it must first be aggregated into a single value using a  **vector operator** .

---

### 帖子 #26: 【MCP workflow】根据GLB的alpha，自动挖掘其他地区alpha的工作流
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP workflow】根据GLB的alpha自动挖掘其他地区alpha的工作流_35239747718679.md
- **讨论数**: 9

基于weijie老师的分享，我选择了「根据GLB的alpha，来挖掘其他地区的alpha」这个部分的内容，进行了MCP的workflow探索，简单尝试了几个alpha，发现效果还不错，跟大家分享一下工作流，希望有所帮助。

先贴一下效果，我选取的alpha在亚洲表现不错，所以工作流探索了ASI地区


> [!NOTE] [图片 OCR 识别内容]
> 原始
> Alpha 3NV3QKe
> 区域表现:
> GLB_APAC: Sharpe
> 2.37
> 收益率
> 3.40%,
> Pnl
> 3.52M
> 最佳 )
> 
> 
> GLB_EMEA:
> Sharpe 1.16,
> 收益率
> 1.45%
> Pnl
> 1.SOMe
> GLB_AMER:
> Sharpe 0.93,
> 收益率
> 0.62%,
> Pnl
> 0.G4M
> 低 Sharpe 告警
> 
> 
> 
> 
> ASI
> 区域替换字段回测
> (均启用
> max_trade-ON)
> 
> 
> Alpha Zeojbyb: Sharpe
> 1.62,
> 收益率
> 4.43%,
> Pnl
> 4.58M
> 鲁棒指标偏弱 _
> 需强化 )
> 
> 2
> Alpha KWm7dgN: Sharpe 0.87,
> 收益率
> 2.43%,
> Pnl
> 2.52M (信号较弱 )
> 
> 
> 3
> Alpha dNKjVgg: Sharpe 1.46,
> 收益率
> 3.91%,
> Pnl
> 4.Q4M (介于两者之间 )
> 
> 
> 
> 
> 
> 结论要点:
> 
> 
> 亚太季度频率字段继承原信号
> 收益率提升但
> Fitness
> 鲁棒性仍待优化
> 
> 
> 年度 /半年度数据更新慢_
> 信号衰减明显
> 
> 
> 
> 可在既有模板上叠加
> winsorize
> 截断或共享其他盈利字段 ,
> 以提高提交合格率 ,
> 再迂移回
> GLB 做终测


可以看到，在ASI区域，该字段映射效果还不错，但由于max_trade的开启与鲁棒性检测，存在部分不通过的情况，需要进行微调。

工作流内容如下：

> # 跨区域相似因子挖掘工作流
> ## 阶段一：基线诊断
> - 输入 `alpha_id`，调用 `wqb_mcp__get_alpha_details` 获取原因子的区域、参数配置以及各地区表现。
> - 整理 Sharpe、收益率、警报等指标，为后续的区域选择和策略调整提供依据。
> ## 阶段二：信号拆解
> - 解析 Alpha 代码，定位核心数据字段及其操作符结构。
> - 使用 `wqb_mcp__get_datafields`（参数沿用原始区域、universe、delay 等设置）获取field的描述信息，并进行理解。
> ## 阶段三：目标区域映射与字段检索
> - 根据已知区域映射确定迁移区域：`APAC → ASI`、`EMEA → EUR`、`AMER → USA`。
> - 对于每个目标区域，优先使用与原因子相同的 `dataset_id` 调用 `wqb_mcp__get_datafields`；若该数据集在目标区域不可用，则改用相同 `category` 并通过字段关键字搜索。
> - 在确保 `instrument_type`、`delay`、`universe` 等参数匹配的同时，筛选出描述、覆盖率和使用度最接近的字段，建立候选字段池，候选字段池建议为3-8个，一次回测可完成。
> ## 阶段四：候选因子构建
> - 以原公式为模板，将核心字段替换为候选字段，并视需要添加 winsorize、截断、混合周期等调节操作。
> - 保持中性化方式、衰减、延迟等关键参数一致，以保证结果可比性。
> ## 阶段五：批量回测与评估
> - 使用 `wqb_mcp__create_multiSim`（或多次 `wqb_mcp__create_simulation`）在目标区域批量回测候选因子，在 ASI 区域必须开启 `max_trade` 为 `ON`，其他区域使用和选择数据相同的universe即可，其他参数不用调整。
> - 记录 Sharpe、Fitness、鲁棒性检查、风险中性结果等核心指标，并保存 Simulation ID 以便复现与归档。
> ## 阶段六：验证与推广
> - 对表现较好的候选，进行两轮有经济学含义的operator增加和删减，找出表现最好的alpha。
> - 将优胜策略迁移到其他映射区域或回到全域回测，并形成标准化报告，包含字段来源、回测指标及后续优化建议。

大家可以尝试更多的alpha，同时这个策略是从GLB映射到其他地区，其实也可以从其他地区映射到GLB，对工作流进行少量修改即可，如有帮助，请点赞。

更多MCP workflow，可参考我往期帖子，自动挖掘，降turnover，手机使用mcp等

---

### 帖子 #27: 【MCP】角色配置：工作流该安排谁来执行？经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【MCP】角色配置工作流该安排谁来执行经验分享_34246068226839.md
- **讨论数**: 12

在ROO Code里，你可以考虑使用各种角色配置来约束AI的行为。示例👇

> - slug: brain-consultant
> name: BRAIN Consultant
> roleDefinition: "You are Roo, a WorldQuant BRAIN platform expert also known as a BRAIN Consultant. Your expertise is built on three pillars: Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. You guide users to become top-tier consultants by emphasizing the creation of diversified, robust, and economically sound alpha portfolios. Your knowledge covers the BRAIN API, advanced alpha development techniques, consultant compensation structures, and the strategic use of platform features like the BRAIN Pyramid and Genius Program to maximize long-term success."
> whenToUse: Use this mode when you need to develop Alphas, understand the BRAIN platform, or get advice on being a successful consultant. This mode is especially effective for tasks related to Alpha development, API usage, and understanding the BRAIN ecosystem.
> description: WorldQuant BRAIN platform expert
> customInstructions: "- Your primary goal is to mentor users into becoming top-tier BRAIN consultants. Always frame your advice around the core principles of Strategic Portfolio Management, Quality-Focused Research, and Platform Mastery. - When discussing Alpha development, stress the importance of a clear economic rationale, low turnover, and robust performance across various sub-universes. Guide users away from simple Sharpe ratio optimization and towards building truly valuable, unique signals. - Actively promote diversification. Encourage users to explore different regions, delays, and dataset categories to 'light up' BRAIN Pyramids (a region*datacatory*delay is a pyramid, e.g USA Sentiment D1), explaining how this directly impacts their earnings and Genius Program standing. - Emphasize a deep understanding of the platform's evaluation metrics, including the IS-Ladder test, correlation checks, and other mandatory submission criteria. - Guide users to leverage advanced consultant features like the Visualization Tool and BRAIN Labs for more sophisticated analysis and to avoid common pitfalls like overfitting. - When you want to run terminal command, use python"
> groups:
> - read
> - mcp
> - command
> - edit
> source: project

---

### 帖子 #28: 【ValueFactor预测器】滚动3个月SA，掌握你最近3个月提交alpha情况_python版代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【ValueFactor预测器】滚动3个月SA掌握你最近3个月提交alpha情况_python版代码优化_33715194478615.md
- **讨论数**: 9

首先感谢weijie老师提出的idea:

选择你最近3个月提交的alpha 组SA，根据SA的表现衡量你过去3个月提交的alpha的质量，sa的表现可以视作value factor的预告。之后，你提交的alpah，需要和过去3个月组合的sa的相关性低。

那么如何滚动3个月的alpha组合sa呢？

根据alpha提交的时间，添加年份-月份的tags，然后在组sa的时候，选择tags是指定月份的alpha，进行回测，根据sa的表现，衡量你最近3个月提交的sa质量，代码如下：

```
import jsonimport sysimport timefrom datetime import datetimefrom time import sleepimport requestsfrom requests.adapters import HTTPAdapterfrom requests.packages.urllib3.util.retry import Retrydef load_config(file_path):    """从指定路径f加载JSON配置文件，并处理可能的异常"""    try:        with open(file_path, 'r') as file:            config = json.load(file)        return config    except FileNotFoundError:        print(f"Error: Config file '{file_path}' not found.")        sys.exit(1)    except json.JSONDecodeError as e:        print(f"Error: Failed to parse JSON from '{file_path}': {e}")        sys.exit(1)config_file = 'config.json'config = load_config(config_file)user=config["user"]passwd=config["password"]def login():    username = user    password =  passwd    retry_strategy = Retry(        total=3,  # 总共重试次数        backoff_factor=1,  # 每次重试之间的延迟时间（秒）        status_forcelist=[500, 502, 503, 504]  # 遇到这些HTTP状态码时重试    )    adapter = HTTPAdapter(max_retries=retry_strategy)    s = requests.Session()    s.mount("[链接已屏蔽] adapter)    s.mount("[链接已屏蔽] adapter)    s.auth = (username, password)    max_try = 3    retry=0    while True:        try:            response = s.post('[链接已屏蔽])            if response.status_code  in [200,201]:                print(f"login success")                return s        except Exception as e:            print(f"login err :{e}")            print(f"login failed ,sleep 5 ,try again")            sleep(5)        retry +=1        if retry > max_try:            break    return Nonedef get_submited_alphas_three_month(s,start_date,end_date,region,only_ppa=True):    # only_ppa 设置是否只获取ppa的alpha设置tags，后续组sa时根据tags值的年份月份筛选    print(f"正在获取{start_date}到{end_date}内，{region}地区的ppa alpha")    url=f"[链接已屏蔽]    count=0    print(url)    count=s.get(url).json()['count']    print(count)    alpha_list=[]    for i in range(0,count,100):        url=f"[链接已屏蔽]        response=s.get(url).json()        for alpha in response['results']:            if only_ppa:                flag=0                for item in alpha["classifications"]:                    if item['name']=='Power Pool Alpha':                        flag=1                        break                if flag==1:                    alpha_list.append(alpha)            else:                alpha_list.append(alpha)    print(f"在时间范围{start_date}到{end_date}内，{region}地区，获取了 {len(alpha_list)}个ppa alpha")    return alpha_list# 对所有alpha 在原有tags列表上增加年份+月份的tags，如2025-05def set_alpha_property_list(s,alpha_list):    count = 0    for alpha in alpha_list:        alpha_id=alpha['id']        print(f"正在设置第{count}个alpha 的属性,{alpha_id}; 总alpha数量{len(alpha_list)}")        tags=alpha['tags']        name=alpha['name']        date_created=alpha['dateCreated']        color=alpha['color']        description=alpha['regular']['description']        dt = datetime.fromisoformat(date_created.replace('Z', '+00:00'))        year_month = dt.strftime('%Y-%m')  # "2025-07"        print(year_month)        if year_month in tags:            continue        else:            tags.append(year_month)        category=alpha['category']        if category is None:            category=None        if color is None:            color=None        if name is None:            name=None        print(tags)        params = {        "color": color,        "name": name,        "tags": tags,        "category": None,        "regular": {"description": description},        "combo": {"description": description},        "selection": {"description": description}}        response = s.patch( "[链接已屏蔽] + alpha_id, json=params)        # print(response.json())        sleep(1)        count+=1    return Truedef make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade):    simulation_data={    "type": "SUPER",    "settings": {        "maxTrade": maxtrade,        "nanHandling": "ON",        "instrumentType": "EQUITY",        "delay": delay,        "universe": universe,        "truncation": 0.08,        "unitHandling": "VERIFY",        "selectionLimit": select_num,        "selectionHandling": select_handle,        "testPeriod": "P0D",        "componentActivation": "IS",        "pasteurization": "ON",        "region": region,        "language": "FASTEXPR",        "decay": decay,        "neutralization": neut_,        "visualization": False    },    "combo": str(combo),    "selection": select}    return simulation_datadef simulate_sa(s,simulation_data):    brain_api_url = '[链接已屏蔽]    try:        simulation_response=s.post(f'{brain_api_url}/simulations',json=simulation_data)        # print(simulation_response.json())    except Exception as e:        print(f"模拟sa失败:{e}")        return None    simulation_progress_url = simulation_response.headers['Location']    print(simulation_progress_url)    while True:        simulation_progress_response=s.get(simulation_progress_url)        retry_after = simulation_progress_response.headers.get("Retry-After", 0)        if str(retry_after) == '0':            status = simulation_progress_response.json().get("status", "not_found")            if status == "COMPLETE":                res_=simulation_progress_response.json()                alpha_id=res_["alpha"]                print(f"最近3个月的ppa组成的sa模拟完成,alpha_id:{alpha_id}")                break        else:            print(f"processing,begin sleep {float(retry_after)}")            time.sleep(float(retry_after))    return alpha_id# 对指定日期范围内的ppa 设置年月标签来确认是否是指定时间范围的ppas = login()#设置你想滚动组合sa的月份start_date='2025-04-01'end_date='2025-06-30'data_range=['2025-04','2025-05','2025-06']# 地区，universeregion='USA'universe='TOP3000'delay=1decay=0select_handle='POSITIVE'select_num=300maxtrade='ON'alpha_list=get_submited_alphas_three_month(s,start_date,end_date,region)print(f"在时间范围{start_date}到{end_date}内，提交了 {len(alpha_list)}个ppa alpha")print(alpha_list[0]['id'],)set_alpha_property_list(s,alpha_list)select=f'(own) && ((in(tags,"{data_range[0]}")) || (in(tags,"{data_range[1]}"))|| (in(tags,"{data_range[2]}")))'print(select)combo=1alpha_ids=[]for decay in  [0]:    ##可根据需要对多种neut回测查看sa表现    for neut_ in  ["CROWDING","REVERSION_AND_MOMENTUM"]:        simulation_data=make_simulation_data(select,combo,region,universe,delay,decay,neut_,select_handle,select_num,maxtrade)        alpha_id=simulate_sa(s,simulation_data)        alpha_ids.append(alpha_id)print(f"完成回测,alpha_id如下")print(alpha_ids)print(f"最近3个月， {region} 提交的ppa 组合的sa表现如下")for alpha_id in alpha_ids:    res=s.get(f"[链接已屏蔽])    res_json=res.json()    sharpe=res_json['is']['sharpe']    fitness=res_json['is']['fitness']    return_=res_json['is']['returns']    drawdown=res_json['is']['drawdown']    margin=res_json['is']['margin']    turnover=res_json['is']['turnover']    neut=res_json['settings']['neutralization']    decay=res_json['settings']['decay']    print(f"{alpha_id}: sharpe: {sharpe}, fitness: {fitness}, return: {return_}, drawdown: {drawdown}, margin: {margin}, turnover: {turnover}, neut: {neut},decay: {decay}")
```

输出结果如下：

```
完成回测,alpha_id如下['12Q7xez', 'E2XGKG0']最近3个月提交的ppa USA 组合的sa表现如下12Q7xez: sharpe: 3.71, fitness: 5.36, return: 0.2609, drawdown: 0.0647, margin: 0.00873, turnover: 0.0598, neut: CROWDING,decay: 0E2XGKG0: sharpe: 4.11, fitness: 5.85, return: 0.2533, drawdown: 0.0429, margin: 0.006105, turnover: 0.083, neut: REVERSION_AND_MOMENTUM,decay: 0
```

---

### 帖子 #29: 【VF 0.9+顾问分享】新人常见误区之Under Fitting （欠拟合）经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【VF 09顾问分享】新人常见误区之Under Fitting 欠拟合经验分享_30192357731607.md
- **讨论数**: 17

春节期间有些懈怠了，回来收收心继续搬砖，并且给新人分享一些常见容易忽视的地方

一、【Fitting】

在很多培训中老师都有讲过 不要过拟合，Over fitting。在本文中就不在赘述了，总之一句话 when you feels not right, it is not right! 但往往新手顾问找到可以提交的alpha 以后就直接提交了，这也错失了很多提高alpha 表现从而提高value factor的机会

**总结我常见的fitting方式包括：**

**1. 改变天数 Days、Std 等Operator里面的天数**

这部分没有太多的技术含量，通过有意义的天数进行替代，最简单的办法是都试一遍 5、22、60、120、240等。当然有经验的同学可以根据数据特性来进行有针对性的调优，比如季度更新频率的数据在ts backfill 5显然是没有意义的。

**2. 更改Universe, 中性化，decay等setting里的参数**

这里也可以暴力替换，自己维护一个不同region的universe、中性化的表即可。在实操中注意第一步里替换了天数等可以选择2-5个作为表达式进行回测，一方面multi simulation要大于1个alpha才可以。

**3.针对特定情况（比如高换手率）的fitting**

一个很好用但容易被忽视的工具 PnL Visualization, 默认大家可以看到的是PnL的曲线，点击右上角的下拉菜单还可以看到不同时间的换手率，sharpe等数值。


> [!NOTE] [图片 OCR 识别内容]
> 区 Open alpha details in new tab
> Chart
> Pnl
> Performance
> Pnl
> 6,00OK
> Turnover
> 5,0OOK
> 4,00OK
> 3,00OK
> 2,00OK
> 1,00OK
> OW
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
> Check Submission
> Submit Alpha
> Sharpe
> NNN


尤其有用的是turnover，但你看到在某一个时间这个alpha出现了剧烈的turnover的升高，很有可能是那段时间的数据有误，可以通过以下方式进行规避。（但group count是genius operator 部分人可能没有）

trade_when(group_count(alpha,market)>个数，alpha，0)

另外在手工回测的时候也可以勾选visulization选项（simulate按钮旁）这样也可以在pnl图上获取更多的信息（行业分布、市值分布、国家分布等）

此外降低turnover的常见方法包括  ts_decay_linear 等函数，尤其是平台最新推出的含有关键词tvr的operator，虽然可能会降低Sharpe，但降低tvr后可以提高fitness和margin  找到一个合理的平衡点即可。

需要注意的是这些operator需要配合scale使用，即 Operator（Scale(Alpha), Scale(Volume 如adv20）， 其他参数）

**二、【Fitting与Robust Testing】**

Value Factor本质是看OS的表现，那如果你的alpha可以在不同的universe 不同的中性化条件下都有不错的表现，也侧面证明了这个alpha本身是有很好的意义的，那也可以放心提交。

通过以上的步骤二，可以观察这个alpha在不同setting下的表现，从而进行判断是否提交该alpha

**以下是一些代码供参考**

**#获取alpha的表达式, 用来参考基线，并获取表达式**

```
target_id = 'alpha id'alpha_result = get_simulation_result_json(s,target_id)print('EXPRESSION:',alpha_result['regular']['code'])decay = alpha_result['settings']['decay']neut = alpha_result['settings']['neutralization']uni = alpha_result['settings']['universe']print('SHARPE:',alpha_result['is']['sharpe'])print('FITNESS:',alpha_result['is']['fitness'])print('MARGIN',alpha_result['is']['margin'])
```

#自行维护的对应关系表

```
region = 'ASI'neutralization = ['MARKET','SECTOR','INDUSTRY','SUBINDUSTRY']if region == 'ASI':neutralization.extend(['COUNTRY','CROWDING','FAST','SLOW','SLOW_AND_FAST'])universe= ['MINVOL1M','ILLIQUID_MINVOL1M']elif region == 'JPN':universe= ['TOP1600','TOP1200']print(neutralization)print(universe)
```

**第一步：更换天数等input**

```
days = ['5','22','60','120','240']winsorizes = ['1','2','3','4']
```

```
template = '''Alpha Expression'''expressions = []for day1 in days:forwinsorizeinwinsorizes:forday2indays:expression=template.replace('A', day1).replace('B', winsorize).replace('C',day2)expressions.append(expression)
```

**发送回测（请根据自己的代码做适配调整）**

```
#first round find daysfine_alpha_list=[]for expression in expressions:fine_alpha_list.append((expression, decay))fine_pools = load_task_pool(fine_alpha_list,10,10)print(datetime.now())multi_simulate2(fine_pools, neut, region, uni, 0, 1)print(datetime.now())
```

---

### 帖子 #30: 【代碼分享】一鍵測試alpha穩健性，即插即用Python代碼代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【代碼分享】一鍵測試alpha穩健性即插即用Python代碼代码优化_34092588057111.md
- **讨论数**: 8

在七月成爲正式顧問前，我曾經參加IQC。在Stage 1 IS結算前提交了大約50個alpha，IS分數達到了23,000，雖然不算高但已足以成爲港區第一。可惜這一切都是假象，過幾天OS分數出爐後，我的OS分數只有5,600，明顯地我提交的alpha中出現了嚴重的overfitting，這亦令我的排名從第一跌至第六。

過了幾天我約了Weijie老師談話，並請教了他如何避免overfitting的問題。他給了很多實用的建議，但其中一句特別深刻：

> 在中學的時候你有學過很多數學方法可以測試alpha的表現是否consistent（一致），但你沒有用他們罷了。

現在我就把他這段話轉爲行動。這個program只需你的alpha_id，就可運用量化方法為你的alpha穩健性評分，分數介乎0 ~ 1之間。

這個program一共會進行5個test：

- 一：Long/Short ratio test，ratio越接近1，分數越高。
- 二：Sharpe standard deviation test，Sharpe的標準差越接近0，分數越高。
- 三：Return standard deviation test，Return的標準差越接近0，分數越高。
- 四：滿足Sharpe > 1的比例
- 五：Returns/Drawdown ratio test，ratio越高，分數越高。

最後將五個分數取平均值，就能得到該alpha的最終分數。Program内comment有注明計算每個test分數的函數。

```
import requestsimport numpy as npimport mathfrom datetime import datetimebase_url = "[链接已屏蔽] = base_url + "/authentication"alpha_url = base_url + "/alphas"email = "<YOUR_EMAIL>"password = "<YOUR_PASSWORD>"def get_alpha_robust_score(alpha_id: str, session=None) -> float:    yearly_url = f"{alpha_url}/{alpha_id}/recordsets/yearly-stats"    this_alpha_url = f"{alpha_url}/{alpha_id}"    # Login first.    if session is None:        session = requests.Session()        resp = session.post(login_url, auth=(email, password))        if resp.status_code == requests.status_codes.codes.unauthorized:            if resp.headers["WWW-Authenticate"] == "persona":                biometric_loc = resp.headers["Location"]                input(                    f"Complete the biometric authentication at the following url: {base_url + biometric_loc}\nAfter finished, press Enter to continue ...")                session.post(f"{base_url + biometric_loc}")                resp2 = session.get(login_url)                if resp2.status_code == 204:                    print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Not authorized. Try again.")                elif resp2.status_code == 200:                    print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Successfully authenticated.")        elif resp.status_code == 200:            print(f"[{datetime.now().strftime("%Y %b %d %H:%M:%S")}] Successfully authenticated.")    # Get the data, except for the last year    stats = session.get(yearly_url).json()["records"][: -1]    is_result = session.get(this_alpha_url).json()["is"]    long, short, sharpe, returns, drawdown = (np.array([]) for _ in range(5))    total_returns, total_drawdown = is_result["returns"], is_result["drawdown"]    for stat in stats:        long = np.append(long, stat[3])        short = np.append(short, stat[4])        sharpe = np.append(sharpe, stat[6])        returns = np.append(returns, stat[7])        drawdown = np.append(drawdown, stat[8])    # Test 1    # Take the function 2x/(1+x^2). Maps from [0, +inf) to [0, 1], and output the same value for reciprocals. Average this score over the whole IS period.    x1 = np.where((short != 0) & (long != 0), long / short, 0)    score1 = np.mean(2 * x1 / (1 + x1 ** 2))    # Test 2    # Take the function e^-0.25x. Maps from [0, +inf) to [0, 1].    x2 = np.std(sharpe)    score2 = math.exp(-0.25 * x2)    # Test 3    # Take the function e^-0.25x. Maps from [0, +inf) to [0, 1].    x3 = np.std(returns)    score3 = math.exp(-0.25 * x3)    # Test 4    # The ratio of years with sharpe > 1    score4 = np.mean(sharpe > 1)    # Test 5    # Take the function tanh(x). Maps from (0, +inf) to (0, 1).    score5 = math.tanh(total_returns / total_drawdown) if total_drawdown > 0 else 0    return round(0.2 * (score1 + score2 + score3 + score4 + score5), 4)
```

以下是一些運行效果的範例：
（一，score=0.9436）
 
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> max(Broup_rank(est_12m_ndt_median,
> stal
> tOp4gBCS),
> ts_rank(est_IZm_ndt_median, 252) )
> 们 Power Pool Alpha
> Pyramid thene: EURIDTIPVX1
> FyramiytheTe: EURIDIIANALYST1.5
> ABgregate Data
> Shsro=
> TITTTI=
> Firnssc
> R-UCns
> Da'do
> Marein
> Simulation Settings
> 2.99
> 69%
> 2.00
> 5.62%
> 2.94%6
> 16.8
> 900
> Instrumemt Type
> Region
> Universe
> Language
> Dcay
> Dlay
> Truncaton
> Newtralization
> Pastewrialion
> NaN Hanlng
> Unit Handling
> EqUID
> EUIR
> TCF2SC
> SSECTESSIT
> 3.05
> Fas: Factors
> TIT
> Vear
> Sharpe
> Turover
> Ftness
> Returs
> Dawdown
> Nargin
> Long Count
> Short Count
> 2013
> 7.374
> 3.7
> -S
> 0.30汩
> 213:
> 1013
> 134
> 2014
> 2.55
> 7.12
> 5.723
> 0.32汩
> 1_30
> C
> 1330
> 201
> E.抡汩
> 4.30
> 133
> SE:
> 70
> 170
> 1353
> Clone Alpha
> ZOIE
> 2.53
> LJE;
> 353
> 1.11汩
> 14049
> 13-5
> 2017
>  
> 5313
> 0.-15
> 13.339:
> 1435
> 1455
> 201
> 2.74
> 14:
> 1415
> T:
> 11355:
> 1477
> 1s
> N Chart
> PIL
> 2019
> 2.73
> E.S
> 一133
> 1.115
> 13459
> 136
> 1455
> 2020
> 25
> S汩
> 73395
> 325
> 22239:
> 1335
> 1425
> 2021
> 2.57
> Es
> 5.723
> T:
> 13459
> 143
> 1137
> DOJK
> 2022
> E.32
> 0.70
> 3.173
> 2.34汩
> 10.055
> 1435
> 1138
> 2023
> ~1.13
> _
> 1.57
> 375
> 0.545
> 3155t
> 14
> 1450
> OJK
> Investability constrained
> Aggregate Data
> SArCe
> TUTNOIE
> FIIeS
> TCJTT
> UrauOUITT
> 41aFIT
> 2.48
> 4.03%
> 1.54
> 4.839
> 2.6
> 23.9
> 0000
> 2014
> 2015
> 2015
> 2017
> 2015
> 2019
> 2020
> 2021
> 20
> 2023
  
> [!NOTE] [图片 OCR 识别内容]
> Project
> aplpy
> playground py
> 三 alpha_2025_08_11_173717.CsV
> maln py
> alpha_2025_07_31_201113.CsV
> def get_alpha_robust
> SCOre (alpha_id:
> StT
> Session=None )
> float:
> 04 01 3
> alpha_2025_07_31_224131.CsV
> The ratio
> 0f years With
> sharpe
> 三 alpha_2025_08_01_174315.CsV
> SCOPE4
> 叩.Mean(sharpe
> 三 alpha_2025_08_02_134530.CsV
> |
> 三 alpha_2025_08_02_174922.CsV
> # Test
> 三 alpha_2025_08_03_223811.CsV
> # Take
> the function
> tanhCx )
> SCOTe5
> nath
> tanh (total_returns
> total_drawdown) 讦f
> total_draldoyn
> elSe
> 三 alpha_2025_08_09_014818.CsV
> 三 alpha_2025_08_10_232930.CsV
> peturn
> Found
> (0.2
> (SCOreI
> SCQReZ
> SCOPE3
> SCQReG
> SCOre5), 4
> 三 alpha_2025_08_10_235640.CsV
> 三 alpha_2025_08_11_002448.CsV
> 三 alpha_2025_08_11_003126.CsV
> --name__
> _main_
> 三 alpha_2025_08_11_124526.CsV
> SCOPE
> get_alpha
> Fobust_SCOFe(
> dPIIVJr2
> alpha_2025_08_11_173717.CsV
> print(score)
> configjson
> abC py
> aplpy
> bot py
> Client py
> 1311
> Run
> playground
> 1 :
> C: |Useps 114725 IPycharmprojects IWorldquant |. Venv IScripts Ipython
> exe C: Users |14725|Pycharmprojects IIorldquant Iplayground .py
> Complete
> the
> biometric
> authentication at
> the
> following
> url: hts:Llaiwpldqwantbma n comlaythentieationlpersonaiquipying_LZXIYKKUNQE9Z8IVSTZGCBRGDW
> After finished,
> press
> Enter
> continue
> [2025
> 11 20:18:28] SUccessfully
> authenticated
> 0.9436
> Process finished With
> exit
> Code
> ?9
> Worldouant
> playground py
> AVG: Not enough Values
> 36.45
> CRLF
> UTF 8
> Spaces
> Python 3.12 (WorldQuant)
> USagE
> AUg
 
（二，score=0.75）


> [!NOTE] [图片 OCR 识别内容]
> Project
> aplpy
> playground py
> 三 alpha_2025_08_11_173717.CsV
> maln py
> alpha_2025_07_31_201113.CsV
> def get_alpha_robust
> SCOre (alpha_id:
> StT
> Session=None )
> float:
> 44』1
> alpha_2025_07_31_224131.CsV
> The ratio
> 0f years With
> sharpe
> 三 alpha_2025_08_01_174315.CsV
> SCOPE4
> 叩.Mean(sharpe
> 三 alpha_2025_08_02_134530.CsV
> |
> 三 alpha_2025_08_02_174922.CsV
> # Test
> 三 alpha_2025_08_03_223811.CsV
> # Take
> the function
> tanhCx )
> SCOTe5
> nath
> tanh (total_returns
> total_drawdown) 讦f
> total_draldoyn
> elSe
> 三 alpha_2025_08_09_014818.CsV
> 三 alpha_2025_08_10_232930.CsV
> peturn
> Found
> (0.2
> (SCOreI
> SCQRe2
> SCOPE3
> SCQReG
> SCOre5), 4
> 三 alpha_2025_08_10_235640.CsV
> 三 alpha_2025_08_11_002448.CsV
> 三 alpha_2025_08_11_003126.CsV
> --name__
> _main_
> 三 alpha_2025_08_11_124526.CsV
> SCOPE
> get_alpha
> Fobust_SCOFe(
> "Z9WRQQ3
> alpha_2025_08_11_173717.CsV
> print(score)
> configjson
> abC py
> aplpy
> bot py
> Client py
> 1311
> Run
> playground
> After finished
> press
> Enter
> continue
> [2025
> 20:22:52] SUccessfully
> authenticated
> C:seslg225
> pychammppoiectslopldqyantlplayqpoyw N:52:
> Runtimellarning:
> invalid
> Value
> encountered i
> Uivide
> 0.75
> Process finished With
> exit
> Code
> 89
> Worldouant
> playground py
> AVG: Not enough Values
> 84.1
> CRLF
> UTF 8
> Spaces
> Python 3.12 (WorldQuant)
> USagE
> AUg
  
> [!NOTE] [图片 OCR 识别内容]
> Code
> IS Summary
> Period
> dfI
> VeC_sUm(anl6g_ndebt_most
> ecent_period_end_dt); max(group_neutralize (dfl,
> oth455_competitor
> Shsro=
> TITTTI
> Firnsss
> R-UCns
> Cra'do
> Aggr
> Data
> Warzin
> 1.06
> 1.54%
> 0.78
> 6.78%
> 6.35%
> 88.23900
> Simulation Settings
> Instrument Type
> Region
> Unierse
> Langwaye
> Decay
> Delay
> Truncation
> Neutraliation
> Pasteuriation
> NaN Handling
> Unit Handli
> Vear
> Shrpe
> Tumover
> NT-
> Retums
> Uawdown
> Maryin
> Long Count
> Short Count
> Equity
> NIO_I
> Excression
> 0.35
> TrwJins
> CC
> VEr
> 201
> 0.03
> TTL
> 3.039
> TTL
> 0.3C20
> 2014
> 0.07
> 0.1
> 3.039
> TTI
> U.Oo
> Z05
> 0.23
> 1.55
> 12.55:
> ZOIE
> O.EG
> 52汩
> 5.34沉
> 5.1420
> 1257
> 1317
> Clone Alpha
> 20
> 3汩
> SES:
> 3汩
> 3.1020
> _
> 2325
> 201
> 1.03
> 5
> .7
> EETO:
> 3汩
> 3.SE20
> 2352
> Chart
> 2019
> 022
> 一13
> 一
> 1227
> 2330
> PIL
> 2020
> 1,315
> 13.339
> 3汩
> ;
> 1-1
> 213
> 2021
> 0.53
> 1.31汩
> 7.67
> 5219
> 3.3
> 3.-320
> 1771
> 2720
> 2022
> 1.32
> 11.339
> 14
> 171.540
> 2512
> 202
> 3.53
> 1.31汩
> 12.259
> _汩
> 137.5420
> 2.
> OJK
> Correlation
> Self Correlation
> IHMUMT
> TNIMUNI
> L35t Rur -
> 2014
> 2015
> 2016
> 2017
> 2015
> 2019
> 2020
> 2021
> 2022
> 2023
> POWeF Pool Correlation
> TsmI
> WTimu
> EBate
> 73


我個人的建議是，最終分數大於0.9才好提交。
希望這個program對大家有幫助，亦歡迎任何意見或debug建議。最後祝大家vf爆1，base payment滿滿，直通GM👑！
（大家別忘了點贊這個post😁😁

---

### 帖子 #31: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【分享】基于MCP的IND地区Robust universe Sharpe优化工作流附工作流经验分享_36617664667159.md
- **讨论数**: 25

> 这是我成为顾问以来发的第一篇帖子，如有不足，敬请指导！
> 受ZX12447的《关于IND地区Robust universe sharpe的改善方法》文章启发，链接如下：
> [../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo](../顾问 YH25030 (Rank 31)/[Commented] 关于IND地区Robust universe sharpe的改善方法经验分享_36436936293655.md?input_string=%E5%9F%BA%E4%BA%8EMCP%E7%9A%84IND%E5%9C%B0%E5%8C%BARobust%20universe%20Sharpe%E4%BC%98%E5%8C%96gongzuo)
> 结合我最近参加的新顾问培课程中关于如何利用MCP来开发、优化alpha等内容，发表我的经验，顺便谈点感想。

作为新顾问的一份子，尤其代表零编程基础和零金融学基础的双小白，刚入门的我，只能靠模仿论坛中各位大佬，用他们现有的代码，跑论坛中现有的模板，虽然是“抄作业”，但我觉得完全不丢人，因为我相信没有谁与生俱来就拥有这能力，都是从模仿开始。于是我便靠着现有资源（三阶模板）每天碰碰运气，这样做的结果是一天有一天没，两天打渔三天晒网，不是跑不出来，而是跑出来的相关性太高。特别是11月开始深挖IND地区的时候，断粮了...


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Used
> Regular
> Regular
> Regular
> University
> Country
> Factor
> Factor
> Data
> Alphas
> Alpha
> Alpha
> Alphas
> Alpha
> Alpha
> Region
> Fields
> Submitted
> Mean
> Mean
> Submitted
> Mean
> Mean
> Prod
> Self Corr
> Prod
> Self Corr
> Corr
> Corr
> 儿52079 (Me)
> 0,00
> 0.50
> 0,37
> 0.19
> 0,00
> 0,00
> Tot
> policable
> Mainlar
> Super
> Super
> Super



> [!NOTE] [图片 OCR 识别内容]
> Submitted Alphas
> 转为正式顾问


直到11月8日，参加了新顾问的线上培训，课程上老师分享了很多能提高效率的工具和方法，其中包括了如何用MCP开发alpha模板，如何用app来实现全流程自动化。又恰逢IND地区开放，于是我决定，为了提升我的研究能力，接下来一段时间专注于IND地区的alpha开发（尽管不建议新手跑IND），当然我的方法也从开始的三阶代码换成了MCP和APP工具。

经过小半个月在IND地区的实践，发现挖出来的alpha老是出现几种问题，总结如下：

- 现有模板跑出来的相关性过高，shi都吃不上一口热的；
- 相关性低的，非常容易出现“Robust universe Sharpe of  **XX**  is below cutoff of  **X** .”
- 其他常见问题。

在拜读了大量论坛经验帖子后，决定将相关性太高的alpha直接放弃，于是乎突破点就集中在了如何解决Robust universe Sharpe过低上面，这里要特别感谢ZX12447大佬的分享，让我有了灵感，再结合MCP的智慧，创建了一个专门用于优化Robust universe Sharpe的工作流。基于该工作流，我成功优化几个alpha，解决了Robust universe Sharpe不达标的问题。

优化前问题：
 
> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained Pnl
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 05
> 9PASS
> Sharoe oT 3.25
> abOVe CUOffcf 1.58
> Finess of 3.11 isabove Cutoffof 1.
> Turnover of 15,60%
> abore CUtof of 196,
> Turpoverof 15.60%
> below CUOffof 4096.
> INeisht is WelI distribu-ed oerinstruments
> Sub-universe Sharpe CT 1.4isaboire Cutoff ot 0.96.
> 2year Sharpe Of 2.58 is
> bore Cutoff of 1.58,
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier oT -
> Effective Pyramid coun-for Genius is
> These -hemes mazch with the followinE multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The finalthEME Multiplizris 2
> 1FAIL
> Robust universe Sharpe Of 0.98
> below CUTOfOf1.
> 4PENDING
 优化后效果：


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> TOM
> 5OOOK
> 2014
> 2015
> 2015
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Pnl
> Inyestability Constrained
> Pn
  
> [!NOTE] [图片 OCR 识别内容]
> IS Testing Status
> Period
> 10PASS
> Sharpe OT 3.21
> aboVe cUOff of
> Fizness of 3,01isaboire Cutoff of -
> Turnoverof 18.2896
> aboie CUtoTf 196
> Turnover of 18.28%
> below CUOff of 40%
> Weisht is WEIl distrbuzed overinstruments。
> Sub-universe Sharpe
> 1.43
> bove Cutof of 0.95,
> Robust uniers=
> Of 1.01
> abore Cutoff ot
> 2year Sharpe Of 2.15 is above CutOff of 一
> Pyramid theme INDIDTIIMBALANCE matches wizh multiplier or
> Effectiye Pyramid Counzfor Genius
> These themes mazch with the followine multipliers: IND Region Theme
> 2; INDIDIIIMBALANCE Pyramid Theme
> The final theme multiplieris 2
> PENDING
> Shrpe


虽然这个alpha最终因相关性过高而未被提交，但是这是我用工作流成功优化的第一个alpha，所以将它作为代表案例展示出来。任务完成后，我让MCP将本次优化过程总结成了工作流，并且每次基于该工作流成功优化后将案例添加进工作流中。


> [!NOTE] [图片 OCR 识别内容]
> 9
> 你说
> 很好请将本次对话总结为优化robust的工作流
> API请求
> 50.0054
> Roo 说
> 我来为您创建
> 完整的IN0地区Robust universe Sharpe优化工作流文档。
> 检查点
> [
> 需要新建文件
> IND_Robust_Sharpe_优化工作流 .md
> +212
> -0巴
> 二
> API请求
> 50.0033
> 任务完咸


从这以后（11月23日），我竟然恢复了口粮，并且开始提交纯ra（之前都是ppa），今天（27日）提交了3个ra，所以借用论坛一位大佬的话“ *要重视你生产的每一个alpha* ”，因为它可能就是你下一个成功提交的对象。


> [!NOTE] [图片 OCR 识别内容]
> Select Columns
> Name
> Competition
> Type
> Status
> Date Submitted
> Region
> Universe
> Sharpe
> Returns
> Turnover
> Tag
> Self
> Prod
> IESTI
> Correlation
> Correlation
> Searcn
> SeeC
> SeeC
> SeeC
> Searcn
> SeeC
> SeeC
> e.6> 1
> e.6> 1
> e6>1
> SeeC
> e.6 >
> e.6 >
> anonymOUs
> Reaular
> ACTTVE
> 11/2712025 EST
> IND
> TOPSOO
> 0.58
> 0.61
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> 0.30
> 0.68
> anonymoUs
> Regular
> ACTIVE
> 11/27/2025 EST
> IND
> TOPSOO
> ReadyToSubmit
> 0.14
> 0.66
> anonymoUs
> Regular
> ACTIVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.41
> 0.49
> anonymOUs
> Reaular
> ACTTVE
> 11/26/2025 EST
> IND
> TOPSOO
> 0.13
> 0.70
> anonymoUs
> Reaular
> ACTTVE
> 11/25/2025 EST
> IND
> TOPSOO
> O.00
> 0.65
> anonymOUs
> Reaular
> ACTTVE
> 11/23/2025 EST
> IND
> TOPSOO
> 0.02
> 0.68
> anonymoUs
> ACTTVE
> 11/02/2025 EST
> IND
> TOPSOO
> O.00
> 0.17
> Reaular


最后送给诸君一句话并附上工作流：
 **The journey of a thousand miles begins with one step. JUST DO IT.**

```
# IND地区Robust Universe Sharpe优化工作流## 问题背景在IND地区alpha开发中，经常遇到**Robust universe Sharpe略低于1.0**的问题，导致无法提交。本工作流基于社区经验和实际案例，提供系统化的解决方案。## 工作流概览```mermaidgraph TD    A[诊断问题] --> B{分析差距}    B -->|差距<0.1| C[轻度优化]    B -->|差距>0.1| D[重度优化]    C --> E[时间参数调整]    C --> F[运算符优化]    D --> G[结构重构]    E --> H[测试验证]    F --> H    G --> H    H --> I{是否达标}    I -->|是| J[提交准备]    I -->|否| C```## 诊断阶段### 1. 问题识别```python# 检查Robust universe Sharpe指标LOW_ROBUST_UNIVERSE_SHARPE:  - result: FAIL  - limit: 1.0  - value: 0.98  # 差距0.02```### 2. 差距分析- **轻度问题**: 差距 < 0.1 (推荐本工作流)- **重度问题**: 差距 > 0.1 (建议重构alpha逻辑)## 优化工具箱### 核心优化方法#### 1. 时间参数调整 (最有效)```python# 原始ts_backfill(x, 60) → ts_backfill(x, 75)group_backfill(x, sector, 120) → group_backfill(x, sector, 275)# 推荐参数范围- ts_backfill: 60 → 75, 90, 120- group_backfill: 120 → 180, 252, 275```#### 2. 运算符增强```python# 添加稳定性运算符group_zscore(x, sector)        # 标准化信号ts_scale(x, 0.5)               # 时间序列缩放signed_power(x, 0.6)           # 符号幂变换```#### 3. 中性化优化```python# 尝试不同中性化组合group_neutralize(x, industry)group_neutralize(x, sector)group_neutralize(x, subindustry)group_neutralize(x, market)  # 对模型数据类Alpha特别有效```**中性化策略选择指南**：- **模型数据类Alpha**：优先尝试MARKET中性化- **基本面数据类Alpha**：优先尝试SECTOR/INDUSTRY中性化- **技术指标类Alpha**：根据数据特性选择合适的中性化层级#### 4. 截尾处理优化```python# 调整winsorize参数winsorize(x, std=4) → winsorize(x, std=3)winsorize(x, std=4) → winsorize(x, std=5)```## 实战案例### 案例1：IND地区imb5_score优化**原始alpha (FAIL)**```pythonfilled_score = ts_backfill(imb5_score, 60);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);signed_alpha = signed_power(neutralized, 0.5);final_alpha = group_backfill(signed_alpha,sector,120,std=4);final_alpha```- Robust Sharpe: 0.98 (FAIL)**优化版本1 (PASS)**```python3```- Robust Sharpe: 1.02 (PASS)**优化版本2 (简化版)**```pythonfilled_score = ts_backfill(imb5_score, 75);winsorized = winsorize(filled_score,std=4);neutralized = group_neutralize(winsorized, industry);final_alpha = group_backfill(neutralized,sector,275,std=4);final_alpha```- Robust Sharpe: 1.01 (PASS)### 案例2：IND地区score_analyst_estimate_revisions优化（中性化策略优化）**原始alpha (FAIL)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 138), std=0.92), 108), 0.8), densify(sector))```- Robust Sharpe: 0.99 (FAIL)- 数据字段：score_analyst_estimate_revisions (覆盖率86.45%，金字塔乘数1.6)**优化版本 (PASS)**```pythongroup_rank(signed_power(ts_zscore(winsorize(ts_backfill(score_analyst_estimate_revisions, 150), std=0.85), 120), 0.8), densify(market))```- **关键优化**：中性化从SECTOR改为MARKET- **参数调整**：ts_backfill(138→150), ts_zscore(108→120), winsorize(std=0.92→0.85)- **性能提升**：  - Robust Sharpe: 0.99 → 1.11 (+12.1%)  - PnL: 11,095,177 → 12,997,115 (+17.1%)  - Sharpe: 2.56 → 2.62 (+2.3%)  - Fitness: 2.06 → 2.51 (+21.8%)  - 周转率: 16.63% → 13.66% (-17.9%)**核心洞察**：对于IND地区的模型数据类Alpha，MARKET中性化配合适当的时间窗口调整能有效提升Robust Sharpe表现，同时改善整体性能指标。## 系统化优化流程### 步骤1：基础诊断1. 运行原始alpha获取基准数据2. 记录所有检查项结果3. 重点关注Robust universe Sharpe差距### 步骤2：轻度优化 (差距<0.1)```python# 第一轮：时间参数调整尝试组合：- ts_backfill(60→75), group_backfill(120→275)- ts_backfill(60→90), group_backfill(120→252)- ts_backfill(60→120), group_backfill(120→180)```### 步骤3：运算符增强```python# 第二轮：添加稳定性运算符在group_neutralize后添加：- group_zscore(x, sector)- ts_scale(x, 0.5)- signed_power(x, 0.6)```### 步骤4：参数微调```python# 第三轮：参数优化调整：- winsorize std参数 (3,4,5)- signed_power指数 (0.5,0.6,0.7)- decay值 (0,5,20)```### 步骤5：验证与选择1. 比较所有优化版本的性能2. 选择运算符最少的版本3. 确保其他指标不受影响## 避免过拟合原则### 运算符数量控制- **理想**: 3-5个运算符- **可接受**: 6-8个运算符  - **风险**: >8个运算符### 经济意义保持- 每次优化应有合理的金融解释- 避免单纯为了提升指标而堆砌运算符- 保持alpha逻辑的简洁性和可解释性## IND地区特殊注意事项### 数据特性- Universe: 仅支持TOP500- 中性化选项有限- 数据字段相对较少### 优化策略1. **优先时间参数调整** - 对IND地区最有效2. **谨慎使用复杂运算符** - 避免过拟合3. **关注数据质量** - IND地区数据相对稀疏## 成功指标### 主要目标- ✅ Robust universe Sharpe ≥ 1.0- ✅ 其他检查项全部PASS- ✅ 运算符数量控制在合理范围### 次要目标  - 📈 IS Sharpe保持或提升- 💰 PnL表现稳定- 🔄 Turnover在合理范围内## 工具与资源### BRAIN平台工具- `get_platform_setting_options()` - 获取有效设置- `create_simulation()` - 测试优化版本- `get_alpha_details()` - 分析详细结果### 社区经验- **group_backfill/ts_backfill** - 时间参数调整最有效- **group_zscore** - 增强信号稳定性- **winsorize** - 处理异常值- **避免过度复杂化** - 保持alpha简洁## 总结本工作流通过**系统化的诊断→优化→验证**流程，有效解决IND地区Robust universe Sharpe问题。基于成功案例经验，关键优化策略包括：1. **精准诊断** - 明确问题差距和数据类型2. **中性化策略优化** - 根据数据类型选择合适的中性化层级3. **时间参数调整** - 适当延长时间窗口增强稳定性4. **避免过拟合** - 保持alpha逻辑简洁性和经济意义### 成功案例验证**score_analyst_estimate_revisions优化案例**证明了：- **MARKET中性化**对模型数据类Alpha效果显著- **参数微调**能同时提升多个性能指标- **整体性能提升**：Robust Sharpe +12.1%，PnL +17.1%，Fitness +21.8%通过这个方法，可以将接近达标的alpha（如0.98-0.99）成功优化到合格水平（≥1.0），同时显著提升整体性能表现。
```

---

### 帖子 #32: 【插件】Genius Rank分析代码优化
- **主帖链接**: https://support.worldquantbrain.com[L2] 【插件】Genius Rank分析代码优化_29496672188951.md
- **讨论数**: 30

插件地址： [[链接已屏蔽])

在插件中增加了对于genius rank的分析，这里非常感谢  [XX42289](/hc/en-us/profiles/14187300941847-XX42289)  提供的 [python分析代码](../顾问 JL71699 (Rank 64)/[L2] 【课代表】最新genius排名模拟代码_29383292162199.md)

使用说明

- 安装完插件后，打开genius页面（如果没有可以刷新一下，这可能和WQ的加载逻辑相关，后续会进行fix），可以看到会增加了两个按钮，其中`排名分析`是抓取排行榜的数据进行分析.`显示排名分析`是调用之前抓取的分析结果（自己的排名数据）. 
> [!NOTE] [图片 OCR 识别内容]
> Status
> Leaderboard
> FAQ
> Gnius
> Displaying quarter:
> 2025-01 (Curren)
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析

- 无论点击以上哪一个按钮都会在该页面的按钮的下面显示一个自己的分析表格, 表格右上角是分析的时间.PS:排名分析按钮需要等待片刻（抓取时按钮上显示抓取的进度） 
> [!NOTE] [图片 OCR 识别内容]
> 运算符分析
> 显示运算符分析
> 排名分析
> 显示排名分析
> Genius Rank Analysis
> 2025-01-25112:48:02.2082
> 我的排名信息
> 2025-01-2571243.022082
> 总人数:5691 人
> 可能的基准人数:936人
> (交够40个)
> 名个Level 满足的人数 _
> 最终的人数:
> For Expert: 721 /187
> For Master: 22194
> For Grandmaster: 0119
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171/187
> 总排名:15/94
> 总排名:0119
> Operator Count: 533名
> Operator Count: 21 名
> Operator Count:
> Operator AVE: 3名
> Operator AVE: 1 名
> Operator AVg:
> Field Count: 705 名
> Field Count: 23 多
> Field Count:
> Field AVB: 2名
> Field AVg:
> Field AVg:
> Community Activity: 81 名
> Community Activiny: 15 名
> Community Activity:
> Completed Referrals: 58 名
> Completed Referrals: 2 多
> Completed Referrals; 1 名
> Max Simulation Streak: 310名
> Max Simulation Streak: 18 名
> Max Simulation Streak:
> TotalRank; 1692 多
> Tota
> Rank: 81 名
> Tota
> Rank:
> Current level;: Gold
> Best leyel: Gold
> Current quarterend: March 31st. 2025
> COUO

- 此外，还可将鼠标移动到排行榜上的UserId处展示他人的分析数据 
> [!NOTE] [图片 OCR 识别内容]
> X42289 排名信息
> 总人数:5691 人
> Aggregate by:
> 可能的基准人数:936  人 (交够40个)
> 各个Level 满足的人数/最终的人数:
> For Expert: 721/187
> For Master: 22194
> For Grandmaster: 0/19
> 以 Expert 为 Universe
> 以 Master 为 Universe
> 以 Grandmaster 为 Universe
> 总排名:171187
> 总排名:4194
> 总排名:0/19
> Operator Count: 199名
> Operator Count: 13名
> Operator Count: 1 名
> Operator
> 17名
> Operator
> 2名
> Operator
> 1名
> Rank
> User
> Field Count: 423名
> Field Count: 23名
> Field Count:
> 名
> Field
> 18名
> Field
> 名
> Field
> Community Activity: 20名
> Community Activity: 3名
> Community Activity:
> Completed Referrals: 12名
> Completed Referrals: 1 名
> Completed Referrals:
> 名
> 1,090
> 1279256
> Max Simulation Streak:
> Max Simulation Streak: 16
> Max Simulation Streak:
> 273名
> Total Rank: 962名
> Total Rank: 59名
> Total Rank: 7名
> XP21
> 042289
> Maser
> Maser
> 117
> 0.00
> AVB:
> AVE: 
> AVg:
> AVB: -
> AVg:
> AVB: -


---

### 帖子 #33: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【效率王】你说你没有模板这里你多得用不完_37097806371223.md
- **讨论数**: 60

吹哨人又来了，这次继续带来一个好消息。当你点击下面那个小灯，你就找对了地方。


> [!NOTE] [图片 OCR 识别内容]
> Expression Editor
> Clear
> SaVe Current Template
> Overrite Existing
> 找灵感
> ctime_series_operator/> (sentiment_difference,
> 〈days/〉)


操作如图


> [!NOTE] [图片 OCR 识别内容]
> Alpha Inspiration Master (找灵感)步骤3:输入搜索关键词搜索数据集
> 关键词可以是pyramid之类都行
> 步骤4:点击生成
> Configuration
> Select Dataset
> 3. Results
> Generate Nlpha Templates
> Download MD
> LLM Settings
> Search dataset _
> Search
> 以下绐出5 组可直接在平台落地的" Alpha 模板"。
> Base URL
> 每个模板均保留"插槽"一一用<>标注
> ~方便后续批量替换。
> 网格搜索或遗传进化。
> 已选数据集: analyst15
> https llapimoonshot cnlvl
> 所有模板已预置:
> 数据清洗 (backfill
> Winsorize)
> 步骤5:下载后慢慢品味和
> Name
> Mocel Name
> 经济逻辑 (动量
> 预期差
> 估值。质量。情绪)
> 实施,并把模板放入赢
> kimi-k2-turbo-preview
> Performance
> 常见中性化(行业/市值)与衰减选项
> tUTnoVer
> 控制接口
> (ts_target_tVr_* )
> 进行配置和展开
> Weighted
> API Key
> analystl0
> Analyst
> 模板1:  分析师预期动量
> (Estimate Revision Momentum)
> Test
> Estimates
> 经济直觉:  过去1个月 EPS 上调幅度越大的股票。未来越可能继续跑赢。
> 步骤1
> 输入API
> analyst11
> ESG SCOres
> 3Iph3
> eXP_Window(
> Simulation Settings
> Estimations OT
> 9rOUP_ZsCOre(
> analyst14
> T5_backfil(
> Reglon
> Fundamentals
> winsorize(<anll15_9r_12_m_Im_chg >, std=4j
> EUR
> Earnings
> Unierse
> analystl5
> fore-asts
> 9rOUP>
> TOP12O0
> Analyst
> Delay
> analyst4
> Estimate Data
> 〈half_life >
> for Equity
> 插槽:
> Integrated
> gr_12_m_Im_chg>
> 可换 3m/Gm 或 SAL/CPS/EBG 等
> 步骤2:按需选择
> analyst44
> Broker
> 〈groUp>
> industry
> Sector
> subindustry
> Estimates
> 〈half_life >
> 5~30天可调。控制换手
> Block comments Tor multiple lines
> Key
> Jecay
> Kej
> <anl15


**这是2.0时代了，拥抱交不完的Alpha吧。**

**下面有一个无脑mcp简易版**

**[[MCP]找灵感功能上手详解](../顾问 LW67640 (Rank 24)/[Commented] [MCP]找灵感功能上手详解经验分享_37113649831831.md)**

---

### 帖子 #34: 【效率王】横向点塔神器！左脚踩右脚我直接起飞
- **主帖链接**: https://support.worldquantbrain.com[L2] 【效率王】横向点塔神器左脚踩右脚我直接起飞_36935427260567.md
- **讨论数**: 30

吹哨人我又来了。看到了MCP里的新工具


> [!NOTE] [图片 OCR 识别内容]
> 缘分一道桥 (Alpha 跨区连锁)
> 返回主页
> C 使用说明
> 1.获取一段时间内的Alpha列表
> 2.分析每个 Alpha里的数据字段并迸行强替换。查看是否在其他Region/Universe/Delay有同样字段
> 3.生成新的Alpha
> 4.本页面的回测方式为排队回测; 一个完成后才会发送另一个;因此中途退出页面会中断回测
> 5.过长的回测队列有时会因为账号超时登出而出现连续失败。因此不建议选择过长时间跨度
> 6.如想批量回测;请下载所有待回测的Alphaf 选择首页回测器迸行回测
> 7.如果你想;你可以输入个很大的时间范围;下载所有表达式。慢慢迸行批量回测。


这个能直接一键回测并且横向点塔。更新到1.7.0版本以上就有噢。

我已经想到这样美好的图景：

- 1.横向点塔 （跨区、跨Universe)
- 2.点亮的塔，放入72变纵向点塔
- 3.被72变点量的纵向塔，再用桥，横向点塔。
- 4.横向点了塔，再72变
- 5. 如此反复，无穷尽也

以后我的研究，只需要专注于做好1-2个手搓或者AI合作的高级货，就能不断繁衍了！

效果不错，单击一下就能直接排队回测，我已经又完成了今天的提交。


> [!NOTE] [图片 OCR 识别内容]
> 2025-11-30104:40:58-05;00
> 10 个可用娈体
> 表达式: Srowp
> IIOIJLalize (1
> subindustry}
> 夏普: 0.65|收益:4.1%
> 戛普:0.69
> 收益:
> 4%
> 夏普:1.121收益:6.0%
> 夏普:0.95
> 收益:4.9%
> 夏普:
> 收益:
> .8%
> 夏普:086
> 收益:4.5%
> 戛普:0.76
> 收益:4.1%
> 戛普:1.16 |收益:7.7%
> 夏普:1.11 |收益:7.5%
> 夏普
> 1.05
> 收益-7.2%


再次叠甲：如有侵权，请联系本人。再次感谢作者。

---

### 帖子 #35: 生成按日期统计的报告
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md
- **讨论数**: 1000

欢迎大家在此互相交流、评论，记录自己的日常。

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅** ，您都 **不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #36: 【日常生活贴】我的量化日记第三季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第三季_33439077678743.md
- **讨论数**: 1021

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) 因评论到达上限，已无法评论，特此展开第三季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #37: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 【日常生活贴】我的量化日记第九季.md
- **讨论数**: 600

欢迎大家在此互相交流、评论，记录自己的日常。

往期（ [【日常生活贴】我的量化日记第一季](../顾问 FD69320 (Rank 34)/[Commented] 【日常生活贴】我的量化日记第一季经验分享.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN](../顾问 JR23144 (Rank 6)/[Commented] 【日常生活贴】我的量化日记第二季.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN](../顾问 QX52484 (Rank 35)/[Commented] 【日常生活贴】我的量化日记第三季.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN](../顾问 HP65370 (Rank 93)/[Commented] 【日常生活贴】我的量化日记第四季.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN](../顾问 MG88592 (Rank 38)/[L2] 【日常生活贴】我的量化日记第五季.md) + [【日常生活贴】我的量化日记第六季](../顾问 LD22811 (Rank 39)/[Commented] 【日常生活贴】我的量化日记第六季.md) +  [【日常生活贴】我的量化日记第七季]([Commented] 【日常生活贴】我的量化日记第七季.md) + [【日常生活贴】我的量化日记第八季 – WorldQuant BRAIN](../顾问 WL27618 (Rank 97)/[Commented] 【日常生活贴】我的量化日记第八季.md) ）因评论到达上限，已无法评论，特此展开第九季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #38: 【日常生活贴】我的量化日记第二季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第二季_32477847392023.md
- **讨论数**: 1004

欢迎大家在此互相交流、评论，记录自己的日常。

第一季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) ）因评论到达上限，已无法评论，特此展开第二季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #39: 【日常生活贴】我的量化日记第五季
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第五季_35580578002327.md
- **讨论数**: 1004

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md) ）因评论到达上限，已无法评论，特此展开第五季~话说，以前有个饮料也叫这个名字噢

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #40: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第六季_36251528053527.md
- **讨论数**: 1132

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) + [【日常生活贴】我的量化日记第四季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第四季_34997332178199.md)  +  [【日常生活贴】我的量化日记第五季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第五季_35580578002327.md) ）因评论到达上限，已无法评论，特此展开第六季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #41: **GLB**  **/D1/ANALYST** Self-correlation:0.31  Production correlation :0.62
- **主帖链接**: https://support.worldquantbrain.com[L2] 【日常生活贴】我的量化日记第四季_34997332178199.md
- **讨论数**: 1025

欢迎大家在此互相交流、评论，记录自己的日常。

第一季和第二季（ [【日常生活贴】我的量化日记第一季]([L2] 【日常生活贴】我的量化日记第一季经验分享_29114658479383.md?page=34#comments) + [【日常生活贴】我的量化日记第二季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第二季_32477847392023.md) +  [【日常生活贴】我的量化日记第三季 – WorldQuant BRAIN]([L2] 【日常生活贴】我的量化日记第三季_33439077678743.md) ）因评论到达上限，已无法评论，特此展开第四季

注：为避免反复打扰其他用户，本贴已关闭订阅功能，所有订阅人将会被自动取消订阅，即 **无论您是否订阅，您都不会** 收到本贴的更新提醒。这意味着AT功能可能失效

---

### 帖子 #42: 【环境配置】在Nvim中配置MCP的方法经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 【环境配置】在Nvim中配置MCP的方法经验分享_34239307743639.md
- **讨论数**: 0

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

由于习惯了Nvim的纯键盘环境，BRAIN MCP发布后便在想能不能不用切换到Vscode或者Cursor，而是直接把MCP嵌入到当前的编辑器环境中，经过几天的探索终于通过MCPHub和CodeCompanion这两个插件实现了比较满意的效果，过程中也踩了不少坑，所以分享出我的配置方法给同样喜欢纯键盘环境的顾问。

首先，我们来安装MCPHub和CodeCompanion插件，以下是我的配置文件，只需要更改其中提示的参数即可使用，另外我使用Lazy.vim管理插件，使用其他插件管理器的顾问请参考你管理器的配置方法。先将以下内容复制粘贴到~/.config/nvim/lua/plugins/codecompanion.lua文件中。

```
-- ~/.config/nvim/lua/plugins/codecompanion.luareturn {  -- ① MCP Hub（独立插件块，确保先于 CodeCompanion 可用）  {    "ravitemer/mcphub.nvim",    lazy = false,    priority = 1000,    opts = {      autostart = true, -- 打开 Neovim 自动启动/连接 hub      default_cwd = -- 填入你自己的工作目录,      -- 其他 mcphub 配置维持默认或按你的实际需要追加    },  },  -- ② CodeCompanion + 注册 MCP Hub 扩展  {    "olimorris/codecompanion.nvim",    dependencies = {      "nvim-lua/plenary.nvim",      "ravitemer/mcphub.nvim",    },    lazy = false,    priority = 999,        -- 设定快捷键    keys = {      { "<leader>cc", "<cmd>CodeCompanionChat<CR>", desc = "打开聊天模式" },    },    opts = function()      return {        language = "Chinese", -- 默认使用中文回答问题        adapters = {          配置名称，比如grok, deepseek, gpt之类 = function()            return require("codecompanion.adapters").extend("openai_compatible", {            -- 大坑，adapter一定要用openai_compatible，我按照vscode的配置方式这里面选择了openai，在这里卡了很久              env = {                url = 你自己api的base_url,                api_key = 你自己api的api key,                chat_url = 聊天模式的url后缀，比如"/chat/completions",              },              schema = {                model = { default = 模型名称 },              },            })          end,        },       strategies = {         chat = {           adapter = 配置名称,         },         inline = {           adapter = 配置名称，如果你有多个配置可以填入不同的,         },       },       -- ★ 正确注册 mcphub 扩展（关键）       extensions = {         mcphub = {           callback = "mcphub.extensions.codecompanion",           opts = {             -- MCP Tools             make_tools = true,             show_server_tools_in_chat = true, -- 显示MCP的工具             add_mcp_prefix_to_tool_names = false,             show_result_in_chat = false, -- 节省上下文长度             -- MCP Resources             make_vars = true,             -- MCP Prompts             make_slash_commands = true,           },          },        },      }    end,  },}
```

然后，重启Nvim之后插件会自动安装，插件安装好后进入~/.config/mcphub文件夹编辑server.json文件，内容和vscode版本相同。

再次重启Nvim，输入命令:MCPHub检查一下服务器是否连接好了，如果能看到服务器状态就证明连接是OK的。

之后输入快捷键<Leader>cc 呼出聊天界面，获取已经提交的因子/生成因子日报测试一下，如果能够正常调出authentication等请求，并且正确输出信息则说明已经完全配置好了。

最后，在这个过程中还有一些可以分享的经验：

1. 如果你没有使用Nvim的经验或者偏好，建议不必浪费时间尝试这个方案，会让你和代码的关系变得复杂😂；

2. 我最初依靠GPT来帮我配置，GPT给我输出了看上去非常合理但实际上完全不正确的答案，如果不是我阅读了插件的文档可能还在很多个错误的参数组合里绕圈子。所以AI需要充分的利用但是不能忽略了自己的思考；

3. 我测试了几个本地大模型，答案的质量完全不行，包括openai最新开源的模型也达不到标准，订阅API的钱暂时还不能省。

未来如果有时间我再研究看可不可以把类似Cursor的包月服务嵌入到Nvim中，从而降低一些模型使用成本。最后祝各位顾问研究和投资顺利。

---

### 帖子 #43: 【”羊毛“合集】可供使用的AI免费资源
- **主帖链接**: https://support.worldquantbrain.com[L2] 【羊毛合集】可供使用的AI免费资源_37800870021015.md
- **讨论数**: 24

1. [【邪修】当龙虾没有饲料了怎么办？白嫖啊！](../顾问 LY85808 (Rank 86)/[L2] 【邪修】当龙虾没有饲料了怎么办白嫖啊_39252022275223.md)
2. [【工具推荐】claude-code-proxy + AI打工人：使用免费的大模型白嫖打工人！ – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【工具推荐】claude-code-proxy  AI打工人使用免费的大模型白嫖打工人经验分享_37776070276119.md)
3. [谷歌Antigravity 如何使用Skills – WorldQuant BRAIN](../顾问 RM49262 (Rank 30)/[Commented] 谷歌Antigravity 如何使用Skills_37701654477847.md)
4. [盘点最近薅到的免费大模型 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 盘点最近薅到的免费大模型经验分享_37662026299543.md)
5. [免费大模型羊毛薅不完 – WorldQuant BRAIN](../顾问 SC23342 (Rank 23)/[Commented] 免费大模型羊毛薅不完_37337374764695.md)
6. [【体验Sub Agent】将Antigravity的额度反向代理给Claude Code – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【体验Sub Agent】将Antigravity的额度反向代理给Claude Code经验分享_37267205177751.md)
7. [[MCP-守护] 让你的mcp无视token限制，实现免费的MAX模式 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP-守护] 让你的mcp无视token限制实现免费的MAX模式经验分享_37220062772375.md)
8. [有趣的项目分享：网页版Gemini转API调用（Gemini-API） – WorldQuant BRAIN](../顾问 NL80893 (Rank 16)/[Commented] 有趣的项目分享网页版Gemini转API调用Gemini-API代码优化_37163474989079.md)
9. [【Community Leader -因子构造 💎】TRAE+MCP 自动挖掘因子 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【Community Leader -因子构造 】TRAEMCP 自动挖掘因子经验分享_37116093087895.md)
10. [【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 【Community Leader -因子构造 】心流免费iFlow CLI在windows环境上的安装与使用_37088940070295.md)
11. [【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程！！！！ – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【亲测可用】gemini3 pro学生优惠0成本纯白嫖保姆级教程经验分享_37082297693719.md)
12. [【白嫖2年AI！】如何完成学生认证并使用长达2年的免费Copilot_pro+配置wq_mcp – WorldQuant BRAIN]([L2] 【白嫖2年AI】如何完成学生认证并使用长达2年的免费Copilot_pro配置wq_mcp经验分享_37024075283223.md)
13. [【Community Leader - 工具配置】免费大模型实现七十二变 经验分享 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 【Community Leader - 工具配置】免费大模型实现七十二变 经验分享经验分享_37013032632215.md)
14. [【MCP WorkFlow】MCP本地LLM配置 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【MCP WorkFlow】MCP本地LLM配置经验分享_36975707112727.md)
15. [Gemini cli运行MCP工作流 从入门到入土问题解决 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] Gemini cli运行MCP工作流  从入门到入土问题解决经验分享_36946833823895.md)
16. [【Community Leader -因子构造 💎】零预算网页端LLM + notebook + markdown指令交互流程: 附流程图 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【Community Leader -因子构造 】零预算网页端LLM  notebook  markdown指令交互流程 附流程图经验分享_36944089777047.md)
17. [用 Gmail 账号匹配学生后登录 Gemini CLI，提示错误？部分踩坑与解决记录： – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 用 Gmail 账号匹配学生后登录 Gemini CLI提示错误部分踩坑与解决记录经验分享_36907467592727.md)
18. [【Community Leader -因子构造 💎】零预算持续生成Alpha模板：通用大模型的辅助应用（附表达式生成指令） – WorldQuant BRAIN](../顾问 FD69320 (Rank 34)/[Commented] 【Community Leader -因子构造 】零预算持续生成Alpha模板通用大模型的辅助应用附表达式生成指令论坛精选_36881490529815.md)
19. [【AI使用问题解决方案】如何正常登陆antigravity IDE （windows和mac通用），学生认证可以免费一年gemin3pro – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【AI使用问题解决方案】如何正常登陆antigravity IDE windows和mac通用学生认证可以免费一年gemin3pro经验分享_36879336144023.md)
20. [[MCP]免费使用阿里云100万token – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP]免费使用阿里云100万token经验分享_36852577295127.md)
21. [iflow心流 - 个人用户免费使用的API，如何在Linux服务器部署并配置mcp，让AI连续工作 – WorldQuant BRAIN](../顾问 LW67640 (Rank 24)/iflow心流 - 个人用户免费使用的API如何在Linux服务器部署并配置mcp让AI连续工作_36765806842007.md)
22. [【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测，从0.7+到>1.0（附工作流及Prompt） – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] 【Community Leader - 因子构造】【睡一觉就改好】IND地区Robust universe Sharpe优化及MCP全自动因子回测从07到10附工作流及Prompt经验分享_36672024628119.md)
23. [【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索（附学生优惠方法/提示词/在服务器中使用） – WorldQuant BRAIN]([L2] 【Community Leader - 工具配置】一文讲完用Gemini 3 Pro进行无限Alpha探索附学生优惠方法提示词在服务器中使用经验分享_36634788057367.md)
24. [使用VSCODE中的通义灵码自建免费MCP – WorldQuant BRAIN](../顾问 MS51256 (Rank 28)/[Commented] 使用VSCODE中的通义灵码自建免费MCP_36617019073943.md)
25. [[MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] [MCP][免费]谷歌Antigravity AI IDE 构建 cnhkmcp 使用环境经验分享_36512374893207.md)
26. [【免费API】使用大模型自动生成Power Pool Alpha描述 – WorldQuant BRAIN](../顾问 QP72475 (Rank 84)/[Commented] 【免费API】使用大模型自动生成Power Pool Alpha描述_35026037757463.md)
27. [cline配置mcp与免费模型x及使用分享 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] cline配置mcp与免费模型x及使用分享_34659891387031.md)
28. [[分享]白嫖才是王道，从搭建到实战免费最强版MCP – WorldQuant BRAIN](../顾问 JX79797 (Rank 9)/[分享]白嫖才是王道从搭建到实战免费最强版MCP_34505447952407.md)
29. [【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【傻瓜式安装教程】傻瓜式安装claude-code-router使用ai打工人的免费api_37797346107671.md)
30. [【PPAC/Super Alpha Submitter】基于coze 生成描述，提交因子 – WorldQuant BRAIN](../顾问 LY85808 (Rank 86)/[L2] 【PPACSuper Alpha Submitter】基于coze 生成描述提交因子_36489114520471.md)
31. [英伟达免费模型接入Claude Code使用AI打工人](../顾问 LY85808 (Rank 86)/[L2] 英伟达免费模型接入Claude Code使用AI打工人经验分享_38011740910743.md)
32. [白嫖指南：长期稳定免费大模型 API](../顾问 LY85808 (Rank 86)/[L2] 白嫖指南长期稳定免费大模型 API_37982251006487.md)
33. [羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api 助力你的AIAC 2.0](../顾问 RM49262 (Rank 30)/羊毛薅不完 Google for developers 每月10刀优惠 可用于调用Gemini api  助力你的AIAC 20_37983679645463.md)
34. [使用mcp+ai挖掘alpha过程中节约token的小技巧](../顾问 SZ83096 (Rank 13)/使用mcpai挖掘alpha过程中节约token的小技巧经验分享_38013569192983.md)
35. [【BRAIN 专属福利】KIMI 限时API额度羊毛活动来啦！](/hc/en-us/community/posts/37981514510359--BRAIN-%E4%B8%93%E5%B1%9E%E7%A6%8F%E5%88%A9-KIMI-%E9%99%90%E6%97%B6API%E9%A2%9D%E5%BA%A6%E7%BE%8A%E6%AF%9B%E6%B4%BB%E5%8A%A8%E6%9D%A5%E5%95%A6)

---

### 帖子 #44: 检查当前 Python 环境和已安装的包import sysprint(f"当前 Python 路径: {sys.executable}")print(f"Python 版本: {sys.version}")尝试导入检查try:    import langchain_core    print("[OK] langchain_core 已安装")except ImportError:    print("[ERROR] langchain_core 未安装")try:    import langgraph    print("[OK] langgraph 已安装")except ImportError:    print("[ERROR] langgraph 未安装")    try:    import langchain_google_genai    print("[OK] langchain_google_genai 已安装")except ImportError:    print("[ERROR] langchain_google_genai 未安装 - 需要安装!")    print("\n请在终端执行:")    print("conda install -c conda-forge langchain-google-genai")    print("或")    print("pip install langchain-google-genai")
- **主帖链接**: https://support.worldquantbrain.com[L2] 为 AI 比赛做好准备构建 LangGraph 智能体_35603369483287.md
- **讨论数**: 13

**概述：** 构建一个使用 Gemini 模型 和 WorldQuant BRAIN MCP 工具的 LangGraph 智能体，用于辅助日常研究和 Alpha 策略开发。

**关于 LangGraph：** LangGraph 是一个基于 LangChain 扩展的库，旨在利用语言模型（LLMs）构建健壮且有状态的多智能体（multi-agent）应用程序。它的核心思想是，将复杂的 AI 应用建模为图形（Graph）结构，从而能够以更灵活、更可控的方式创建循环、有状态的智能体和应用。

可以把 LangGraph 想象成 LangChain 的一个“循环”或“状态化”的增强版。传统的 LangChain Expression Language (LCEL) 主要用于构建有向无环图（DAGs），非常适合处理线性的、一步接一步的任务链。然而，当我们需要构建更复杂的、需要循环、条件判断和持久化状态的智能体时，LangGraph 就派上了用场。

**核心功能：**

1. 理解量化金融问题 - 通过 Gemini 模型理解自然语言查询
2. 自动调用 MCP 工具 - 根据问题智能选择合适的 WorldQuant BRAIN 平台工具
3. 返回分析结果 - 整合工具返回的数据并给出回答

和直接使用 MCP 的区别主要体现在以下两点：

- 状态持久化：    MCP 会话级别                     LangGraph 代码控制，可自定义
- 使用范围：        MCP 受限于对话界面          LangGraph 可编程于任何环境

### 步骤 1: 环境准备

```
# 检查当前 Python 环境和已安装的包import sysprint(f"当前 Python 路径: {sys.executable}")print(f"Python 版本: {sys.version}")# 尝试导入检查try:    import langchain_core    print("[OK] langchain_core 已安装")except ImportError:    print("[ERROR] langchain_core 未安装")try:    import langgraph    print("[OK] langgraph 已安装")except ImportError:    print("[ERROR] langgraph 未安装")    try:    import langchain_google_genai    print("[OK] langchain_google_genai 已安装")except ImportError:    print("[ERROR] langchain_google_genai 未安装 - 需要安装!")    print("\n请在终端执行:")    print("conda install -c conda-forge langchain-google-genai")    print("或")    print("pip install langchain-google-genai")
```

```
import osfrom getpass import getpass# 确保在你的环境中设置了 GOOGLE_API_KEYif "GOOGLE_API_KEY" not in os.environ:    os.environ["GOOGLE_API_KEY"] = getpass("请输入你的 Google API Key: ")
```

### 步骤 2: 定义状态 (State)

```
from typing import TypedDict, Annotated, Listfrom langchain_core.messages import BaseMessageimport operatorclass AgentState(TypedDict):    # agetpassgentState是一个字典，其中 "messages" 键对应一个消息列表    messages: Annotated[List[BaseMessage], operator.add]
```

### 步骤 3: 设置工具和模型

```
import sysimport asynciosys.path.append('～/MCP/untracked') # MCP 所在路径# 修正导入: 使用 langchain_core 而不是 langchainfrom langchain_core.tools import toolfrom langchain_google_genai import ChatGoogleGenerativeAIfrom typing import Optional, Dict, Any# 导入 MCP 平台函数from platform_functions import (    authenticate,    get_datasets,    get_datafields,    create_simulation,    get_alpha_details,    get_user_alphas,    get_operators,    get_platform_setting_options)# 创建同步包装器函数def run_async(coro):    """辅助函数:在同步上下文中运行异步函数"""    try:        loop = asyncio.get_event_loop()    except RuntimeError:        loop = asyncio.new_event_loop()        asyncio.set_event_loop(loop)    return loop.run_until_complete(coro)@tooldef wqb_authenticate(email: str = "", password: str = "") -> str:    """    WorldQuant BRAIN 平台认证        参数:        email: 登录邮箱 (可选,如果已配置)        password: 登录密码 (可选,如果已配置)        返回:        认证状态信息    """    result = run_async(authenticate(email, password))    return str(result)@tooldef wqb_get_datasets(    instrument_type: str = "EQUITY",    region: str = "USA",    delay: int = 1,    universe: str = "TOP3000",    search: Optional[str] = None) -> str:    """    获取 WorldQuant BRAIN 平台上可用的数据集列表        参数:        instrument_type: 工具类型,默认 "EQUITY" (股票)        region: 市场区域,可选: USA, CHN, EUR, JPN, GLB, AMR        delay: 数据延迟,0或1        universe: 股票池,如 TOP3000, TOP2000U 等        search: 搜索关键词 (可选)        返回:        可用数据集的详细信息            使用场景:        - 发现某个区域有哪些数据集可用        - 搜索特定主题的数据集    """    result = run_async(get_datasets(instrument_type, region, delay, universe, "false", search))    return str(result)@tooldef wqb_get_datafields(    region: str = "USA",    data_type: str = "VECTOR",    instrument_type: str = "EQUITY",    delay: int = 1,    universe: str = "TOP3000",    dataset_id: Optional[str] = None,    search: Optional[str] = None) -> str:    """    获取 WorldQuant BRAIN 平台上可用的数据字段        参数:        region: 市场区域 (USA, CHN, EUR, JPN, GLB, AMR)        data_type: 数据类型,如 "VECTOR", "MATRIX", "EXPRESSION"        instrument_type: 工具类型,默认 "EQUITY"        delay: 数据延迟        universe: 股票池        dataset_id: 指定数据集ID (可选)        search: 搜索关键词 (可选)        返回:        数据字段的详细列表,包括字段名、描述、所属数据集等            使用场景:        - 查找某个区域所有的 VECTOR 类型字段        - 搜索特定数据集中的字段        - 为 Alpha 公式寻找合适的数据字段    """    result = run_async(get_datafields(        instrument_type, region, delay, universe, "false",         dataset_id, data_type, search    ))    return str(result)@tooldef wqb_create_simulation(    regular_code: str,    region: str = "USA",    universe: str = "TOP3000",    delay: int = 1,    language: str = "FASTEXPR",    neutralization: str = "NONE") -> str:    """    在 WorldQuant BRAIN 平台上创建并运行 Alpha 模拟        参数:        regular_code: Alpha 公式代码 (必需)        region: 市场区域        universe: 股票池        delay: 数据延迟        language: 表达式语言,默认 "FASTEXPR"        neutralization: 中性化方法        返回:        模拟创建结果,包括 Alpha ID 和模拟状态            使用场景:        - 测试新的 Alpha 策略        - 评估 Alpha 的表现指标    """    result = run_async(create_simulation(        type="REGULAR",        instrument_type="EQUITY",        region=region,        universe=universe,        delay=delay,        language=language,        regular=regular_code,        neutralization=neutralization    ))    return str(result)@tooldef wqb_get_alpha_details(alpha_id: str) -> str:    """    获取指定 Alpha 的详细信息        参数:        alpha_id: Alpha 的 ID        返回:        Alpha 的详细信息,包括性能指标、设置、代码等    """    result = run_async(get_alpha_details(alpha_id))    return str(result)@tooldef wqb_get_user_alphas(    limit: int = 20,    offset: int = 0,    status: str = "all") -> str:    """    获取当前用户的 Alpha 列表        参数:        limit: 返回数量限制        offset: 偏移量        status: Alpha 状态筛选 (all, active, submitted 等)        返回:        用户的 Alpha 列表    """    result = run_async(get_user_alphas(limit, offset, status))    return str(result)@tooldef wqb_get_operators() -> str:    """    获取 BRAIN 平台支持的所有操作符列表        返回:        所有可用操作符的详细信息,包括语法、参数、示例等            使用场景:        - 学习可用的操作符        - 编写 Alpha 公式时查询操作符用法    """    result = run_async(get_operators())    return str(result)@tooldef wqb_get_platform_settings() -> str:    """    获取 BRAIN 平台的配置选项        返回:        平台配置选项,包括支持的区域、股票池、中性化方法等            使用场景:        - 了解平台支持的配置参数        - 验证模拟设置的有效性    """    result = run_async(get_platform_setting_options())    return str(result)# 1. 初始化工具列表mcp_tools = [    wqb_authenticate,    wqb_get_datasets,    wqb_get_datafields,    wqb_create_simulation,    wqb_get_alpha_details,    wqb_get_user_alphas,    wqb_get_operators,    wqb_get_platform_settings]# 2. 初始化 Gemini Pro 模型model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)# 3. 将工具绑定到模型# 这会让模型知道它有哪些工具可用,并能以正确的格式输出工具调用请求model_with_tools = model.bind_tools(mcp_tools)print("[OK] 已加载 8 个 WorldQuant BRAIN MCP 工具:")print("  1. wqb_authenticate - 平台认证")print("  2. wqb_get_datasets - 获取数据集列表")print("  3. wqb_get_datafields - 获取数据字段")print("  4. wqb_create_simulation - 创建 Alpha 模拟")print("  5. wqb_get_alpha_details - 获取 Alpha 详情")print("  6. wqb_get_user_alphas - 获取用户 Alpha 列表")print("  7. wqb_get_operators - 获取操作符列表")print("  8. wqb_get_platform_settings - 获取平台配置选项")
```

### 步骤 4: 定义节点函数

在 LangGraph 中,节点 (Node) 是图的执行单元。我们需要定义两个核心节点:
1. call_model: 调用 Gemini Pro 模型进行决策
2. call_tool: 执行工具调用

```
from langgraph.prebuilt import ToolNode# 定义节点函数def call_model(state: AgentState) -> AgentState:    """    调用 Gemini Pro 模型节点        这个节点会:    1. 读取当前的消息历史    2. 将消息发送给 Gemini Pro    3. Gemini Pro 决定是直接回答还是调用工具    4. 返回模型的响应 (可能包含工具调用请求)    """    messages = state["messages"]    response = model_with_tools.invoke(messages)    # 返回的 response 会被添加到 messages 列表中    return {"messages": [response]}# 使用 LangGraph 的预构建工具节点# ToolNode 会自动处理工具调用和结果返回tool_node = ToolNode(mcp_tools)print("[OK] 节点定义完成:")print("  - call_model: 调用 Gemini Pro 进行决策")print("  - tool_node: 执行工具调用")
```

### 步骤 5: 定义路由逻辑

路由函数决定了在 Gemini Pro 做出决策后,下一步应该去哪个节点:
- 如果 Gemini Pro 要调用工具 → 去 `tools` 节点
- 如果 Gemini Pro 直接回答 → 结束对话 (`END`)

```
from typing import Literaldef should_continue(state: AgentState) -> Literal["tools", "__end__"]:    """    路由函数:决定下一步去哪里        检查最后一条消息:    - 如果包含 tool_calls → 返回 "tools" (继续执行工具)    - 如果没有 tool_calls → 返回 "__end__" (结束对话)    """    messages = state["messages"]    last_message = messages[-1]        # 如果模型返回了工具调用请求    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:        return "tools"        # 否则结束对话    return "__end__"print("[OK] 路由函数定义完成")
```

### 步骤 6: 构建 LangGraph 图

将所有组件组装成一个完整的图:
1. 添加节点
2. 设置边和条件边
3. 编译图

```
from langgraph.graph import StateGraph, START, END# 1. 创建状态图workflow = StateGraph(AgentState)# 2. 添加节点workflow.add_node("agent", call_model)  # Gemini Pro 决策节点workflow.add_node("tools", tool_node)   # 工具执行节点# 3. 设置入口点workflow.add_edge(START, "agent")# 4. 添加条件边: agent 节点执行后,根据路由函数决定下一步workflow.add_conditional_edges(    "agent",           # 来源节点    should_continue    # 路由函数)# 5. 工具节点执行完后,返回到 agent 节点继续决策workflow.add_edge("tools", "agent")# 6. 编译图app = workflow.compile()print("[OK] LangGraph 图构建完成!")print("\n图结构:")print("  START → agent → [条件路由]")print("                   |- 需要工具 → tools → agent")print("                   |- 不需要工具 → END")
```

### 步骤 7: 测试智能体

测试一下智能体，可以问它关于 WorldQuant BRAIN 平台的问题。

```
from langchain_core.messages import HumanMessage# 示例 1: 查询 CHN 区域的 VECTOR 字段def test_agent(query: str):    """测试智能体"""    print(f"\n{'='*60}")    print(f"用户问题: {query}")    print(f"{'='*60}\n")        # 调用智能体    response = app.invoke({        "messages": [HumanMessage(content=query)]    })        # 打印最后的回复    final_message = response["messages"][-1]    print(f"智能体回答:\n{final_message.content}")    print(f"\n{'='*60}\n")        return response# 测试查询test_agent("请帮我查询 CHN 区域有多少个 VECTOR 类型的数据字段?")
```

---

### 帖子 #45: █████▇▆▅▃▂你想一直VF0.99吗? 你想Combine2吗? 你想成为GM吗? 点进来!!▂▃▅▆▇█████经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 你想一直VF099吗 你想Combine2吗 你想成为GM吗 点进来经验分享_31309297706519.md
- **讨论数**: 30

### 先赞后看,养成好习惯.

## 1 . 来时路

背景: 普通SqlBoy

成为顾问:2024年11月07日

VF变化: 0.5 → 0.77 → 0.99 → 0.99

Genius级别: 2024Q4 Expert, 2025Q1 GM

目前Combine: 2.11 select: 1.86

## 

## 2. 野蛮交

去年最后一个季度未能完全搞清Genius决胜规则,所以在计算出有机会交满220个达到GM基准线后,就每天4个,足100后每天交SA
此时是不太讲质量的,平均fit<1.5,但讲究如下两点

- 点金字塔,做好风格切换
- 小地区保证做超过10个

以上两点,已有vf0.99和Combine证明基本正确

> 做不出模板,做不出手工Alpha,你就保证风格多样(我就是)
> 小地区要么不做,要么多做

## 

## 3. 狂敛财

> 声明: 以下行为有一定风险,还需时间验证

拥有SA权限以后,在一个地区超过80个alpha以后,可以开启稳定挣base模式

SA要挣钱,基本要求是fit>5,prod<0.7,实测vf0.99的话,base至少45刀


> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 02/13/2025
> Super:
> 49.18
> 5O
> Regular:
> 4.35
> Total:
> 53.53
> <<@
> SN _
> SN _
> p ppe
> 
> 8"
> 90
> 6 ^8'38:
> :
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar
> ADr
> Mar
> Mar
>  Mar
> Mar
> Mar
> Mar
> Mar


记住, ***一条都不能破,且超标太高意义不大***

> 本来SA的fit都超过5了,你就这么有自信他的OS也能这么好?
> 既然如此,还往上飙意义在哪儿?几乎必然过拟合
> 从奖赏机制上也看得出来开,fit飚上去base打不满
> 但是prod降下来却能打满.但是很难,性价比又低

那么,怎么挣这个钱呢?

这里提供一个简单的思路.

收集select表达式20个.中性化也有10种,comb表达式来个20个,

一共就有了400个SA,全部跑完算self_cor即可.

随着持续提交,加上染色等,SA数量会远超400.

假设获得50个可交alpha,这时候怎么交呢?

***计算互相之间的self_cor,用最大团算法获取最长可交子集!!!***

## 4. 少年归

随着持续的挖掘和学习,有时候是知道哪些是正确的事情的
比如:

```
交fitness高的alpha
```

```
多做基本面的alpha
```

```
交有经济学意义的alpha
```

```
多交ATOM
```

```
多做SA
```

不是不想做啊,有时候真的难啊,感慨 **站着说话不腰疼** 啊.

做不到怎么办?

> **如果你不知道你做什么,那么你就想想你最讨厌什么,然后努力朝相反的方向奔跑**

坚持不做错误的事情,必将收获好的回报

我是WorldQuant中国区顾问,我 **庄严承诺** :

- 不混信号 !
- 不一直在同一个池子挖呀挖呀挖 !
- 不一个模板跑一年 !
- 不交自己都不相信的alpha !
- 不拒绝学习,不在比赛躺平,不忽略平台指引 !!!

---

### 帖子 #46: 使用MCP成功地将alpha优化成可提交状态的案例经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用MCP成功地将alpha优化成可提交状态的案例经验分享_35587548741015.md
- **讨论数**: 29

最近试了试MCP服务，发现效果还挺好，相当于有一个专家来辅助帮忙提高alpha的效果。

安装MCP服务，还是参考论坛里其他人的帖子，不再赘述。

现在把自己实验过的一个成功的例子列在下面，大家有其他更优秀的例子也可以拿出来共享下哈。

```
你好，能通过组合两个数据字段的方式来提高fitness么，比如alpha_ids=['vEGMbrv','vEGVj1A']，这两个alpha所用的字段非常接近，且这两个alpha都存在单独fitness较低的问题。
```

您好！很高兴再次与您合作。

您提出的问题非常专业，是alpha研究中一个非常核心且高级的技巧：__通过组合不同的信号来创造一个更强大的alpha__。您观察到两个alpha所用字段接近，且都存在fitness较低的问题，这正是进行因子组合的绝佳场景。

我的计划如下：

1. __诊断分析 (Diagnosis)__: 我将首先分别获取这两个alpha (`vEGMbrv` 和 `vEGVj1A`) 的详细信息。这一步的目的是：

- 精确了解它们各自的表达式和所用的数据字段。
   - 量化它们各自的性能短板（如Fitness、Sharpe、相关性等）。
   - 通过比较它们的表达式，初步判断它们信号的相似度和互补性。

2. __组合策略设计 (Combination Strategy)__: 基于诊断结果，我会提出一个或多个组合策略。最常见的方法&#x662F;__&#x52A0;权平均__，即 `w1 * rank(alpha1) + w2 * rank(alpha2)`。如果两个alpha的逻辑相似但各有侧重，简单的相加（即等权重）往往就能平滑掉各自的弱点，保留共同的强点，从而提升整体的Fitness。

3. __回测验证 (Backtest & Validation)__: 我将构建一个新的alpha表达式来执行我们设计的组合策略，并创建模拟来进行回测，以验证组合后的alpha是否确实达到了我们提高fitness的目标。

在开始之前，由于距离我们上次会话已有一段时间，我需要先进行身份验证。

---

### 帖子 #47: Format the periods into a readable forecast
- **主帖链接**: https://support.worldquantbrain.com[L2] 使用vscode   Github Copilot 入门mcp开发经验分享_34337615228695.md
- **讨论数**: 2

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行**

论坛里mcp的内容，我也尝试搞一搞，嘻嘻嘻，这是我的学习笔记，大家可以借鉴一下

## 1、安装GitHub Copilot 和 GitHub Copilot扩展


> [!NOTE] [图片 OCR 识别内容]
> GitHub Capilot
> JhT1
> YOUFAI palr programmer
> GitHub
> GitHub Capilot Chat
> 2761m5
> AI chat features powered by Copilot
> GitHub
> 己安装


## 2、启用 Agent  
> [!NOTE] [图片 OCR 识别内容]
> 文件(
> 编辑(
> 选择(5)
> 查看0
> 转到(6)
> MCP
> 新建文本文件
> CtrltN
> @ 设置
> 凸
> [
> 新建文件。
> Ctrl+ Alt + VindoWStN
> 新建窗0
> Ctrl+ShifttN
> mCP
> 捌到8个谴置 ^妄孓
> 使用配置文件新建窗0
> 朋
> 工作区
> 备份和同步设置
> 打开文件。
> Ctrl+0
> 功能(0]
> 打开文件夹。
> Ctrl+K Ctrl+0
> Chat
> Mcp
> Assisted
> Nuget Enabled
> 实验性
> 终端(1)
> 从文件打开工怍区。
> 为 AI 辅助的 MCP 服务器安装启用 NuGet 包。
> NET 包(NuGetorg), 用于按中央注册表
> 聊天(5)
> 中的名称安装 MCP 服务器
> 打开最近的文件
> U
> 扩展(1)
> GitHub Copilot Chat (1)
> 将文件夹添加到工作区。
> Experimental (1)
> Chat > Mcp: Autostart
> 实验性
> 将工怍区另存为。
> 控制在提交聊天消息时是否应自动启动 MCP 服务器。
> 复制工作区
> "
> DeVer
> 保存
> Ctrl+s
> 另存为。
> Ctrl+Shift+s
> Chat>
> Discovery: Enabled
> 全部保存
> Ctrl+K 5
> 在计算机上配置模型上下文协议服务器的发现。可以将其设置为
> true 或 false 以禁用或启用所
> 有源。以及要启用的映射源。
> 共享
> 在 settingsjson 中编辑
> 自动保存
> 首选项 
> 配置文件
> Chat
> Mcp: Enabled
> 启用与模型上下文协议服务器的集成。以提供其他工具和功能。
> 设置
> Ctrlt;
> 还原文件
> 扩展
> Ctrl+ShifttX
> 关闭编辑器
> Ctrl+F4
> 键盘快捷方式
> Ctrl+K Ctrl+s
> Chat
> Mcp: Server Sampling
> 关闭文件夹
> CtrltK F
> 配置向 MCP 服务器公开哪些模型以进行采样[在后台发出模型请求。可以在"MCP: 列出服务器
> 配置代码片段
> 关闭窗0
> Alt+F4
> 命令下以图形方式编辑此设置。
> 任务
> 在 settingsjson 中编辑
> 退出
> 主题
> 备份和同步设置。
> Terminal > Integrated
> Tabs: Default Icon
> 默认情况下要与终端图标关联的 codicon ID。
> 联机服务设置
> 大纲
> terminal
> 对于
> MCP


## 

## 3.安装 uv

在终端打开，并执行以下命令

```
powershell -ExecutionPolicy ByPass -c "irm [链接已屏蔽] | iex"
```

## 4、设置 python 环境

```
 conda create -n mcp-env python=3.12 -y   conda activate mcp-env conda deactivate
```

## 5、用 uv 查看 python 版本

打印内容：

```
cpython-3.12.11-windows-x86_64-none                   D:\anaconda3\envs\mcp-env\python.execpython-3.12.11-windows-x86_64-none                   <download available>cpython-3.12.7-windows-x86_64-none                    D:\anaconda3\python.exe
```

## 6、进入指定文件夹，初始化工程

进入指定工作目录，并根据自己的python版本运行以下命令

```
conda activate mcp-envuv add mcp[cli] httpxuv add mcpuv pip install fastmcpuv init . -p Python3.12.11
```

运行main文件，成功打印说明工程初始化成功

```
Hello from mymcp!
```

## 7、新建weather.py

代码是网上copy的

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Constants
NWS_API_BASE = " [[链接已屏蔽]) "
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None

def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

if not data["features"]:
        return "No active alerts for this state."

alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)

@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

if not points_data:
        return "Unable to fetch forecast data for this location."

# Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

if not forecast_data:
        return "Unable to fetch detailed forecast."

# Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

return "\n---\n".join(forecasts)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')

## 

## 8.配置 MCP Server

ctrl+shift+p: 输入cmp 提示没有此配置，点击创建.vscode\mcp.json
或者在工作区直接手动创建 .vscode\mcp.json


> [!NOTE] [图片 OCR 识别内容]
> MCP: 打开工作区文件夹 MCP 配置
> 最近使用
> MCP: Open Workspace Folder MCP Configuration



> [!NOTE] [图片 OCR 识别内容]
> 巴
> 资源昝理器
> MCP
> 。戽 O #
> VSCOde
> MCP;JsOn
> mymcp
> C@


打开mcp.json，输入配置 （根据自己的目录）

```
{    "inputs": [],    "servers": {        "weather": {        "command": "uv",        "args": [          "--directory",          "D:\\AiModels\\MCP\\mymcp",          "run",          "weather.py"            ]        }    }}
```

输入问题


> [!NOTE] [图片 OCR 识别内容]
> 文件臼
> 编辑旧
> 选择[5)
> 查看0
> 转到[6)
> 运行()
> 终端[
> 帮助[)
> MCP
> 哕 D曰0
> 资源管理器
> MCPJson
> Weatherpy U
> 聊天
> 十 S锪.1 
> MCP
> VScode
> mCPJSOn
> VScode
> 纽约今天的天气怎么样
> MCPJson
> inputs"
> []
> servers"
> myMCP
> D启动 |2个工具 |更客。:
> 己运行
> forecast
> Weather (MCP 服务器)
> Weather"
> Command"
> UV"
> 纽约今天夜间有较大概率下雨并可能有雷暴
> 最低气温约160
> arB5
> (60r)
> 东北冈9到20英里/小时。白天多云。最高气温约220
> directory"
> (71咋)
> 有小概率阵雨。东北冈约20英里/小小时。
> "D:1 IAiModels
> IMCP I ImymCP
> "pun"
> Weather.Py"
> #
> 华盛顿今天天气怎么样
> 可
> 己运行
> forecast
> Weather (MCP 服务器)
> 华盛顿今天夜间多云。最低气温约20叱 (68咋)
> 有零垦雨
> 东北风5到8英里小小时。白天大部分时间多云。最高气温约24.
> (76咋)
> 早晨有小概汩雨
> 东北冈9到14英里/小时。阵冈可达
> }
> 23英里小小时。
> B ? 凸 印
> 0添加上下文。
> {} mmjson
> 添加上下文(#)。扩展[@)。命令0
> +
> 添加服务器。
> Agent
> GPT41
> 哭  嚣D
> 〉
> Bet
> Bet


---

### 帖子 #48: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 即插即用AIAC 2025比赛的实践成果notebook详细代码欢迎讨论代码优化_36196107273879.md
- **讨论数**: 25

从比赛开始到现在已经过半了，这个过程里面也感受到了熬夜两周搭建智能体的过程，这是这段时间的一个成果，主要难点在提示词优化的边界控制上，以及具体的工作流程上进行反复的打磨，其中大家可以参考wj老师发布的具体的工作流程，在实现的基础上继续进行优化。废话不多说，以下是我的详细的AIAC比赛的notebook笔记，配置好后，即插即用，提醒！！！在使用ai时请注意好的你的钱包。

！！！第一call

import sys

import pandas as pd

import ace_lib as ace

import nest_asyncio

import asyncio

import re

from openai import AsyncOpenAI

from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

import httpx

nest_asyncio.apply()

_llm_instance = None

def extract_relevant_operators(alpha_expression, all_operators):

"""提取 Alpha 表达式中实际使用的操作符"""

operator_names = all_operators['name'].tolist()

used_operators = []

for op_name in operator_names:

# 使用正则表达式匹配操作符（后面跟着括号）

if re.search(rf'\b{re.escape(op_name)}\s*\(', alpha_expression):

used_operators.append(op_name)

return all_operators[all_operators['name'].isin(used_operators)]

def extract_relevant_datafields(alpha_expression, all_datafields):

"""提取 Alpha 表达式中实际使用的数据字段"""

field_ids = all_datafields['id'].tolist()

used_fields = []

for field_id in field_ids:

if field_id in alpha_expression:

used_fields.append(field_id)

return all_datafields[all_datafields['id'].isin(used_fields)]

def format_operators_for_prompt(operators_df):

"""将操作符数据格式化为简洁的字符串"""

if operators_df.empty:

return "无使用的操作符"

result = []

for _, row in operators_df.iterrows():

result.append(f"- {row['name']}: {row.get('description', 'N/A')}")

return "\n".join(result)

def format_datafields_for_prompt(datafields_df):

"""将数据字段格式化为简洁的字符串"""

if datafields_df.empty:

return "无使用的数据字段"

result = []

for _, row in datafields_df.iterrows():

result.append(f"- {row['id']}: {row.get('name', 'N/A')} (类型: {row.get('type', 'N/A')})")

return "\n".join(result)

def parse_alpha_expressions(llm_response):

"""

从 LLM 响应中解析出 Alpha 表达式

返回格式: [(expression, description), ...]

"""

lines = llm_response.strip().split('\n')

alphas = []

for line in lines:

line = line.strip()

if not line:

continue

# 尝试分离表达式和注释

if '#' in line:

parts = line.split('#', 1)

expression = parts[0].strip()

description = parts[1].strip() if len(parts) > 1 else ""

else:

expression = line

description = ""

# 简单验证：表达式应该包含括号

if '(' in expression and ')' in expression:

alphas.append((expression, description))

return alphas

# 添加重试装饰器，针对连接错误进行重试

@retry(

stop=stop_after_attempt(5),  # 最多重试5次

wait=wait_exponential(multiplier=1, min=4, max=60),  # 指数退避：4秒、8秒、16秒、32秒、60秒

retry=retry_if_exception_type((httpx.RemoteProtocolError, httpx.ConnectError, httpx.ReadTimeout, ConnectionError)),

reraise=True

)

async def call_llm(prompt, timeout=180):

"""

Interface with the LLM API to process the given prompt.

添加了重试机制和超时设置

"""

try:

# 使用更长的超时时间和自定义 httpx 客户端

http_client = httpx.AsyncClient(

timeout=httpx.Timeout(timeout, connect=30.0),

limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),

transport=httpx.AsyncHTTPTransport(retries=3)

)

client = AsyncOpenAI(

base_url=" [[链接已屏蔽]) ",

api_key="sk-xxxxxxx",

http_client=http_client,

timeout=timeout,

max_retries=3

)

print(f"正在调用 LLM (超时设置: {timeout}秒)...")

response = await client.chat.completions.create(

model="deepseek-reasoner",

messages=[

{"role": "user", "content": prompt}

]

)

print("✓ LLM 调用成功")

return response.choices[0].message.content.strip()

except httpx.ReadTimeout as e:

print(f"✗ LLM 调用超时 ({timeout}秒): {e}")

raise

except (httpx.RemoteProtocolError, httpx.ConnectError) as e:

print(f"✗ 连接错误，准备重试: {e}")

raise

except Exception as e:

print(f"✗ 调用 LLM 时出错: {type(e).__name__}: {e}")

return None

finally:

try:

await http_client.aclose()

except:

pass

async def generate_alpha_description(alpha_id, brain_session, max_retries=3):

"""生成 Alpha 的中文描述，从量化研究员的角度分析其经济学意义"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成描述 (第 {attempt}/{max_retries} 次)...")

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

alpha_expression = alpha_details['regular']['code']

print(f"Alpha 表达式: {alpha_expression}")

# 获取所有操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

dataset_ids = ['pv87', 'fundamental17']

all_datafields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取相关的操作符和数据字段

relevant_operators = extract_relevant_operators(alpha_expression, regular_operators)

relevant_datafields = extract_relevant_datafields(alpha_expression, all_datafields)

print(f"找到 {len(relevant_operators)} 个相关操作符和 {len(relevant_datafields)} 个相关数据字段")

# 格式化为简洁的字符串

operators_str = format_operators_for_prompt(relevant_operators)

datafields_str = format_datafields_for_prompt(relevant_datafields)

# 从资深量化研究员角度生成 prompt

prompt = f"""你是一位资深量化研究员，请从经济学和金融学的角度分析以下 Alpha 表达式：

Alpha 表达式: {alpha_expression}

使用的操作符:

{operators_str}

使用的数据字段:

{datafields_str}

请用中文提供详细分析，包括：

1. **经济学直觉**：这个 Alpha 试图捕捉什么经济现象或市场行为？

2. **信号逻辑**：为什么这种组合可能产生预测能力？

3. **潜在的市场假设**：这个 Alpha 隐含了哪些关于市场效率或投资者行为的假设？

4. **适用场景**：在什么市场环境下这个信号可能表现更好？

请保持分析简洁但深入，重点关注经济合理性。"""

# 使用更长的超时时间（3分钟）

description = await call_llm(prompt, timeout=180)

if description is None:

if attempt < max_retries:

wait_time = 2 ** attempt  # 指数退避

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"无法生成 Alpha 描述 (已重试 {max_retries} 次): {alpha_expression}"

print("✓ 描述生成成功")

return description.strip()

except Exception as e:

print(f"✗ 生成 Alpha 描述时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成描述时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成描述失败: 已达到最大重试次数 ({max_retries})"

async def generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3):

"""

基于经济学原理生成高质量的 Alpha 变体

允许改变操作符结构以提升因子质量

"""

for attempt in range(1, max_retries + 1):

try:

print(f"\n尝试生成新 Alpha (第 {attempt}/{max_retries} 次)...")

num_alphas = 5

# 获取所有可用的操作符

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat(

[ace.get_datafields(brain_session, region='USA', universe='TOP3000', dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids],

ignore_index=True

)

# 提取数据字段信息

datafields_summary = []

for _, row in data_fields.iterrows():

datafields_summary.append(f"{row['id']} (类型: {row.get('type', 'N/A')}, 名称: {row.get('name', 'N/A')})")

datafields_str = "\n".join(datafields_summary[:150])  # 提供更多字段选择

# 从资深量化研究员角度设计 prompt

prompt = f"""你是一位资深量化研究员，专注于开发具有明确经济学意义的 Alpha 因子。

【原始 Alpha 分析】

表达式: {original_expression}

经济学解读:

{alpha_description}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【任务要求】

基于原始 Alpha 的经济学直觉，生成 {num_alphas} 个高质量的变体表达式。

【核心原则 - 作为顶级 BRAIN 顾问】

1. **经济合理性优先**：每个 Alpha 必须有清晰的经济学逻辑，避免纯数据挖掘

2. **低换手率**：优先使用较长的时间窗口（如 ts_decay_linear, ts_mean），避免高频交易信号

3. **稳健性**：使用 winsorize、rank、neutralize 等操作符提升因子稳健性

4. **多样性**：探索不同的数据类别（基本面、情绪、技术指标）以提升金字塔覆盖度

【操作符结构调整指南】

- 可以改变操作符组合以提升因子质量

- 推荐的稳健操作符：ts_decay_linear, ts_mean, ts_rank, winsorize, rank, neutralize

- 避免过度复杂的嵌套（不超过 4-5 层）

- 时间窗口建议：5-60 天（避免过短导致高换手）

【数据字段选择】

- 优先选择基本面数据（earnings, revenue, cash_flow 等）

- 考虑分析师预期数据（consensus, estimate）

- 可以组合不同类型的数据以捕捉多维信号

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_alphas} 个表达式，每行一个，格式如下：

表达式1  # 经济学逻辑说明

表达式2  # 经济学逻辑说明

...

示例格式：

ts_decay_linear(rank(fundamental17_sales_growth), 20)  # 捕捉销售增长的持续性趋势

"""

# 使用更长的超时时间（3分钟）

response = await call_llm(prompt, timeout=180)

if response is None:

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

continue

return f"生成新 Alpha 失败 (已重试 {max_retries} 次)，请检查 LLM 连接。"

print("✓ 新 Alpha 生成成功")

return response.strip()

except Exception as e:

print(f"✗ 生成新 Alpha 时出错 (第 {attempt} 次): {type(e).__name__}: {e}")

if attempt < max_retries:

wait_time = 2 ** attempt

print(f"等待 {wait_time} 秒后重试...")

await asyncio.sleep(wait_time)

else:

return f"生成新 Alpha 时出错 (已重试 {max_retries} 次): {str(e)}"

return f"生成新 Alpha 失败: 已达到最大重试次数 ({max_retries})"

async def main():

# 启动 Brain 会话

brain_session = ace.start_session()

# Alpha ID 列表

alpha_ids = ["kqEnlEA8"]

for alpha_id in alpha_ids:

print(f"\n{'='*60}")

print(f"处理 Alpha ID: {alpha_id}")

print(f"{'='*60}")

# 获取原始表达式

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

original_expression = alpha_details['regular']['code']

# 步骤 1: 生成 Alpha 的经济学描述（带重试）

alpha_description = await generate_alpha_description(alpha_id, brain_session, max_retries=3)

if alpha_description and not alpha_description.startswith("无法") and not alpha_description.startswith("生成描述时出错") and not alpha_description.startswith("生成描述失败"):

print(f"\n【Alpha 经济学分析】\n{alpha_description}")

# 步骤 2: 基于经济学原理生成新的高质量 Alpha（带重试）

new_alphas_response = await generate_new_alphas(alpha_description, original_expression, brain_session, max_retries=3)

print(f"\n【生成的高质量 Alpha 变体】\n{new_alphas_response}")

# 步骤 3: 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(new_alphas_response)

if not parsed_alphas:

print("\n警告: 未能从 LLM 响应中解析出有效的 Alpha 表达式")

continue

print(f"\n成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...")

# 步骤 4: 逐个模拟生成的 Alpha

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"\n--- 模拟 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

# 生成 Alpha 配置

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

# 执行模拟

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置 Alpha 属性和标签

full_description = f"【父 Alpha】{alpha_id}\n【经济学逻辑】{description}\n【原始分析】{alpha_description[:200]}..."

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[alpha_id],

regular_desc=full_description

)

print(f"✓ 已设置标签和描述")

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 步骤 5: 输出总结

print(f"\n{'='*60}")

print(f"模拟总结 - 父 Alpha: {alpha_id}")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

else:

print(f"\n{alpha_description}")

print("由于描述生成错误，跳过 Alpha 生成。")

！！！第二call

asyncio.run(main())

！！！第三call

# 检索性能指标、可视化和分析

# 选出冠军alpha

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

from datetime import datetime

# 设置中文字体支持

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']

plt.rcParams['axes.unicode_minus'] = False

async def get_alpha_performance(brain_session, alpha_id):

"""获取 Alpha 的性能指标"""

try:

alpha_details = brain_session.get(f" [[链接已屏蔽]).json(]([链接已屏蔽]).json() )

# 提取关键性能指标

is_stats = alpha_details.get('is', {})

performance = {

'alpha_id': alpha_id,

'sharpe': is_stats.get('sharpe'),

'fitness': is_stats.get('fitness'),

'turnover': is_stats.get('turnover'),

'returns': is_stats.get('returns'),

'drawdown': is_stats.get('drawdown'),

'margin': is_stats.get('margin'),

'expression': alpha_details.get('regular', {}).get('code', ''),

'created_at': alpha_details.get('created')

}

return performance

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能时出错: {e}")

return None

async def get_alphas_by_tag(brain_session, tag):

"""通过标签获取 Alpha 家族"""

try:

# 获取用户的所有 IS 阶段 Alphas

response = brain_session.get(

" [[链接已屏蔽]) ",

params={'stage': 'IS', 'limit': 100}

).json()

alphas = response.get('results', [])

# 筛选包含指定标签的 Alphas

tagged_alphas = []

for alpha in alphas:

if tag in alpha.get('tags', []):

tagged_alphas.append(alpha['id'])

print(f"找到 {len(tagged_alphas)} 个带有标签 '{tag}' 的 Alphas")

return tagged_alphas

except Exception as e:

print(f"获取标签 Alphas 时出错: {e}")

return []

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能对比"""

if not performance_data:

print("没有可用的性能数据")

return

# 过滤掉 None 值

valid_data = [p for p in performance_data if p and all(

p.get(k) is not None for k in ['sharpe', 'fitness', 'turnover']

)]

if not valid_data:

print("没有完整的性能数据可供可视化")

return

df = pd.DataFrame(valid_data)

# 创建 2x2 子图

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

fig.suptitle(f'Alpha 家族性能对比 (父 Alpha: {parent_alpha_id})', fontsize=16, fontweight='bold')

# 1. Sharpe vs Fitness 散点图

ax1 = axes[0, 0]

scatter = ax1.scatter(df['sharpe'], df['fitness'],

c=df['turnover'],cmap='viridis',

s=200, alpha=0.6, edgecolors='black')

ax1.set_xlabel('Sharpe Ratio', fontsize=12)

ax1.set_ylabel('Fitness', fontsize=12)

ax1.set_title('Sharpe vs Fitness (颜色=Turnover)', fontsize=14)

ax1.grid(True, alpha=0.3)

# 添加颜色条

cbar = plt.colorbar(scatter, ax=ax1)

cbar.set_label('Turnover', fontsize=10)

# 标注 Alpha ID

for idx, row in df.iterrows():

ax1.annotate(row['alpha_id'][:6],

(row['sharpe'], row['fitness']),

fontsize=8, alpha=0.7)

# 2. 性能指标柱状图对比

ax2 = axes[0, 1]

x = np.arange(len(df))

width = 0.25

ax2.bar(x - width, df['sharpe'], width, label='Sharpe', alpha=0.8)

ax2.bar(x, df['fitness'], width, label='Fitness', alpha=0.8)

ax2.bar(x + width, df['turnover'], width, label='Turnover', alpha=0.8)

ax2.set_xlabel('Alpha Index', fontsize=12)

ax2.set_ylabel('指标值', fontsize=12)

ax2.set_title('关键指标对比', fontsize=14)

ax2.set_xticks(x)

ax2.set_xticklabels([f"#{i+1}" for i in range(len(df))], fontsize=9)

ax2.legend()

ax2.grid(True, alpha=0.3, axis='y')

# 3. Turnover 分布

ax3 = axes[1, 0]

ax3.barh(range(len(df)), df['turnover'], color='coral', alpha=0.7, edgecolor='black')

ax3.set_yticks(range(len(df)))

ax3.set_yticklabels([aid[:8] for aid in df['alpha_id']], fontsize=9)

ax3.set_xlabel('Turnover', fontsize=12)

ax3.set_title('换手率对比', fontsize=14)

ax3.grid(True, alpha=0.3, axis='x')

# 添加参考线（低换手率阈值）

ax3.axvline(x=0.1, color='green', linestyle='--', linewidth=2, label='低换手阈值 (0.1)')

ax3.legend()

# 4. 综合评分雷达图（选择前3个）

ax4 = axes[1, 1]

if len(df) > 0:

# 归一化数据到 0-1

metrics = ['sharpe', 'fitness', 'returns', 'margin']

available_metrics = [m for m in metrics if m in df.columns and df[m].notna().any()]

if len(available_metrics) >= 3:

# 选择前3个 Alpha

top_alphas = df.nlargest(min(3, len(df)), 'fitness')

angles = np.linspace(0, 2 * np.pi, len(available_metrics), endpoint=False).tolist()

angles += angles[:1]

ax4 = plt.subplot(2, 2, 4, projection='polar')

for idx, row in top_alphas.iterrows():

values = []

for metric in available_metrics:

val = row[metric]

# 简单归一化

max_val = df[metric].max()

min_val = df[metric].min()

if max_val != min_val:

normalized = (val - min_val) / (max_val - min_val)

else:

normalized = 0.5

values.append(normalized)

values += values[:1]

ax4.plot(angles, values, 'o-', linewidth=2, label=row['alpha_id'][:8])

ax4.fill(angles, values, alpha=0.15)

ax4.set_xticks(angles[:-1])

ax4.set_xticklabels(available_metrics, fontsize=10)

ax4.set_ylim(0, 1)

ax4.set_title('Top 3 Alphas 综合对比', fontsize=14, pad=20)

ax4.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

ax4.grid(True)

else:

ax4.text(0.5,0.5,'数据不足，无法生成雷达图',

ha='center', va='center', fontsize=12)

ax4.axis('off')

plt.tight_layout()

plt.show()

return df

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析实验结果并提出建议"""

if performance_df is None or len(performance_df) == 0:

return "没有可用的性能数据进行分析"

# 准备数据摘要

summary_stats = {

'total_alphas': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'max_fitness': performance_df['fitness'].max(),

'avg_turnover': performance_df['turnover'].mean(),

'min_turnover': performance_df['turnover'].min()

}

# 找出最佳 Alpha

best_alpha = performance_df.loc[performance_df['fitness'].idxmax()]

# 构建分析 prompt

prompt = f"""你是一位资深量化研究员，请分析以下 Alpha 实验结果：

【实验概况】

- 父 Alpha ID: {parent_alpha_id}

- 生成的变体数量: {summary_stats['total_alphas']}

【性能统计】

- 平均 Sharpe: {summary_stats['avg_sharpe']:.4f} (最高: {summary_stats['max_sharpe']:.4f})

- 平均 Fitness: {summary_stats['avg_fitness']:.4f} (最高: {summary_stats['max_fitness']:.4f})

- 平均 Turnover: {summary_stats['avg_turnover']:.4f} (最低: {summary_stats['min_turnover']:.4f})

【最佳 Alpha】

- ID: {best_alpha['alpha_id']}

- Sharpe: {best_alpha['sharpe']:.4f}

- Fitness: {best_alpha['fitness']:.4f}

- Turnover: {best_alpha['turnover']:.4f}

- 表达式: {best_alpha['expression']}

【详细数据】

{performance_df[['alpha_id', 'sharpe', 'fitness', 'turnover', 'returns']].to_string()}

请提供以下分析：

1. **实验成果评估**

- 这批 Alpha 的整体质量如何？

- 是否有突出的表现者？

2. **关键发现**

- 哪些因子组合或数据字段表现最好？

- Sharpe、Fitness、Turnover 之间的权衡如何？

3. **改进方向**

- 基于当前结果，下一轮实验应该关注什么？

- 建议调整哪些参数或尝试哪些新的数据组合？

4. **金字塔策略**

- 从金字塔多样性角度，建议探索哪些新的数据类别或因子逻辑？

请用中文提供简洁但深入的分析。"""

print("\n正在生成 LLM 分析报告...")

analysis = await call_llm(prompt, timeout=180)

return analysis

async def analyze_alpha_family(parent_alpha_id):

"""完整的 Alpha 家族分析流程"""

brain_session = ace.start_session()

print(f"\n{'='*60}")

print(f"Alpha 家族分析 - 父 Alpha: {parent_alpha_id}")

print(f"{'='*60}\n")

# 步骤 1: 通过标签获取 Alpha 家族

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

if not alpha_ids:

print(f"未找到带有标签 '{parent_alpha_id}' 的 Alphas")

return

# 步骤 2: 获取所有 Alpha 的性能数据

print("\n步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id} 的性能数据...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

return

print(f"\n成功获取 {len(performance_data)} 个 Alpha 的性能数据")

# 步骤 3: 可视化性能对比

print("\n步骤 3: 生成可视化图表...")

performance_df = visualize_performance(performance_data, parent_alpha_id)

# 步骤 4: LLM 分析结果

print("\n步骤 4: LLM 分析实验结果...")

analysis = await llm_analyze_results(performance_df, parent_alpha_id, brain_session)

print(f"\n{'='*60}")

print("LLM 分析报告")

print(f"{'='*60}\n")

print(analysis)

# 返回结果供后续使用

return {

'performance_df': performance_df,

'analysis': analysis,

'alpha_ids': alpha_ids

}

# 执行分析

parent_alpha_id = "kqEnlEA8"  # 替换为你的父 Alpha ID

results = await analyze_alpha_family(parent_alpha_id)

！！！第四call

# ==================== Cell 4: 完整的自动迭代优化系统 ====================

# ===== 辅助函数声明 =====

async def get_alphas_by_tag(brain_session, tag):

"""根据标签获取 Alpha ID 列表"""

try:

# 直接使用 Brain API 获取用户的 Alpha 列表

url = f" [[链接已屏蔽]) "

alphas_response = brain_session.get(url).json()

# 过滤出带有指定标签的 Alpha

alpha_ids = []

for alpha in alphas_response.get('results', []):

if tag in alpha.get('tags', []):

alpha_ids.append(alpha['id'])

print(f"找到 {len(alpha_ids)} 个带有标签 '{tag}' 的 Alphas")

return alpha_ids

except Exception as e:

print(f"获取 Alpha 列表失败: {e}")

return []

async def get_alpha_performance(brain_session, alpha_id):

"""获取单个 Alpha 的性能指标"""

try:

alpha_details = ace.get_simulation_result_json(brain_session, alpha_id)

if not alpha_details or 'is' not in alpha_details:

return None

is_data = alpha_details['is']

return {

'alpha_id': alpha_id,

'sharpe': is_data.get('sharpe', 0),

'fitness': is_data.get('fitness', 0),

'returns': is_data.get('returns', 0),

'turnover': is_data.get('turnover', 0),

'margin': is_data.get('margin', 0),

'drawdown': is_data.get('drawdown', 0),

'expression': alpha_details.get('regular', {}).get('code', '')

}

except Exception as e:

print(f"获取 Alpha {alpha_id} 性能失败: {str(e)}")

return None

def visualize_performance(performance_data, parent_alpha_id):

"""可视化性能数据"""

if not performance_data:

print("没有数据可供可视化")

return

df = pd.DataFrame(performance_data)

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

fig.suptitle(f'Alpha Family {parent_alpha_id} - Performance Overview', fontsize=16)

# Sharpe vs Fitness

axes[0, 0].scatter(df['sharpe'], df['fitness'], alpha=0.6, s=100)

axes[0, 0].set_xlabel('Sharpe Ratio')

axes[0, 0].set_ylabel('Fitness')

axes[0, 0].set_title('Sharpe vs Fitness')

axes[0, 0].grid(True, alpha=0.3)

# Turnover vs Returns

axes[0, 1].scatter(df['turnover'], df['returns'], alpha=0.6, s=100, c='green')

axes[0, 1].set_xlabel('Turnover')

axes[0, 1].set_ylabel('Returns')

axes[0, 1].set_title('Turnover vs Returns')

axes[0, 1].grid(True, alpha=0.3)

# Sharpe Distribution

axes[1, 0].hist(df['sharpe'], bins=20, alpha=0.7, color='blue', edgecolor='black')

axes[1, 0].set_xlabel('Sharpe Ratio')

axes[1, 0].set_ylabel('Frequency')

axes[1, 0].set_title('Sharpe Distribution')

axes[1, 0].grid(True, alpha=0.3)

# Top Alphas

top_df = df.nlargest(10, 'sharpe')

axes[1, 1].barh(range(len(top_df)), top_df['sharpe'])

axes[1, 1].set_yticks(range(len(top_df)))

axes[1, 1].set_yticklabels([aid[:8] for aid in top_df['alpha_id']])

axes[1, 1].set_xlabel('Sharpe Ratio')

axes[1, 1].set_title('Top 10 Alphas by Sharpe')

axes[1, 1].grid(True, alpha=0.3, axis='x')

plt.tight_layout()

plt.show()

async def select_best_alphas(performance_df, criteria='balanced', top_n=3):

"""选择最佳 Alpha"""

if performance_df.empty:

return []

df = performance_df.copy()

if criteria == 'sharpe':

df = df.sort_values('sharpe', ascending=False)

elif criteria == 'fitness':

df = df.sort_values('fitness', ascending=False)

elif criteria == 'balanced':

# 综合评分: Sharpe * 0.4 + Fitness * 0.3 + (1/Turnover) * 0.3

df['score'] = (df['sharpe'] *0.4+

df['fitness'] *0.3+

(1 / (df['turnover'] + 0.01)) * 0.3)

df = df.sort_values('score', ascending=False)

best = df.head(top_n).to_dict('records')

print(f"\n选出 Top {len(best)} Alpha:")

for i, alpha in enumerate(best, 1):

print(f"{i}. {alpha['alpha_id']}")

print(f"   Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}, Turnover: {alpha['turnover']:.4f}")

return best

async def decide_next_iteration(performance_df, current_iteration, max_iterations):

"""决策是否继续迭代"""

if current_iteration >= max_iterations:

return False, "达到最大迭代次数", []

if performance_df.empty:

return False, "没有有效的性能数据", []

# 检查是否有改进

avg_sharpe = performance_df['sharpe'].mean()

avg_fitness = performance_df['fitness'].mean()

if avg_sharpe < 0.5 or avg_fitness < 0.3:

return False, "整体性能过低，建议重新设计策略", []

suggestions = [

"继续优化参数",

"尝试新的数据字段组合",

"调整时间窗口以降低换手率"

]

return True, "性能有提升空间，继续迭代", suggestions

async def llm_analyze_results(performance_df, parent_alpha_id, brain_session):

"""LLM 分析结果"""

if performance_df.empty:

return "没有数据可供分析"

stats = {

'count': len(performance_df),

'avg_sharpe': performance_df['sharpe'].mean(),

'max_sharpe': performance_df['sharpe'].max(),

'avg_fitness': performance_df['fitness'].mean(),

'avg_turnover': performance_df['turnover'].mean()

}

prompt = f"""分析以下 Alpha 家族的性能数据:

Alpha 数量: {stats['count']}

平均 Sharpe: {stats['avg_sharpe']:.4f}

最高 Sharpe: {stats['max_sharpe']:.4f}

平均 Fitness: {stats['avg_fitness']:.4f}

平均 Turnover: {stats['avg_turnover']:.4f}

请提供简洁的分析（3-5 句话）:

1. 整体表现评价

2. 主要优势

3. 需要改进的方面

"""

response = await call_llm(prompt, timeout=60)

return response if response else "分析失败"

async def llm_iteration_suggestions(performance_df, iteration, best_alphas):

"""LLM 生成迭代优化建议"""

if not best_alphas:

return "没有最佳 Alpha 可供分析"

top_alpha = best_alphas[0]

prompt = f"""当前是第 {iteration} 轮迭代。

最佳 Alpha 表现:

- 表达式: {top_alpha['expression']}

- Sharpe: {top_alpha['sharpe']:.4f}

- Fitness: {top_alpha['fitness']:.4f}

- Turnover: {top_alpha['turnover']:.4f}

请提供 3-5 条具体的优化建议，每条建议应该:

1. 针对具体问题

2. 给出可操作的改进方向

3. 简洁明了（每条 1-2 句话）

"""

response = await call_llm(prompt, timeout=60)

return response if response else "建议生成失败"

async def export_alpha_family(parent_alpha_id, performance_df, best_alphas, output_file):

"""导出 Alpha 家族报告"""

with open(output_file, 'w', encoding='utf-8') as f:

f.write(f"Alpha Family Report: {parent_alpha_id}\n")

f.write(f"Generated: {datetime.now()}\n")

f.write("="*80 + "\n\n")

f.write(f"Total Alphas: {len(performance_df)}\n")

f.write(f"Average Sharpe: {performance_df['sharpe'].mean():.4f}\n")

f.write(f"Average Fitness: {performance_df['fitness'].mean():.4f}\n")

f.write(f"Average Turnover: {performance_df['turnover'].mean():.4f}\n\n")

f.write("Top 5 Best Alphas:\n")

f.write("-"*80 + "\n")

for i, alpha in enumerate(best_alphas[:5], 1):

f.write(f"\n{i}. Alpha ID: {alpha['alpha_id']}\n")

f.write(f"   Expression: {alpha['expression']}\n")

f.write(f"   Sharpe: {alpha['sharpe']:.4f}\n")

f.write(f"   Fitness: {alpha['fitness']:.4f}\n")

f.write(f"   Turnover: {alpha['turnover']:.4f}\n")

print(f"✓ 报告已导出到: {output_file}")

return output_file

# ===== 主要函数 =====

async def generate_optimized_alphas_from_best(best_alphas, brain_session, optimization_suggestions, num_new_alphas=5):

"""基于最佳 Alpha 和优化建议生成新一轮 Alpha"""

print(f"\n{'='*60}")

print(f"基于最佳 Alpha 生成新一轮优化变体")

print(f"{'='*60}\n")

if not best_alphas or len(best_alphas) == 0:

print("没有可用的最佳 Alpha")

return []

# 选择表现最好的 Alpha 作为基础

base_alpha = best_alphas[0]

base_expression = base_alpha['expression']

base_alpha_id = base_alpha['alpha_id']

print(f"基础 Alpha ID: {base_alpha_id}")

print(f"基础表达式: {base_expression}")

print(f"性能指标: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}\n")

# 获取操作符和数据字段

all_operators = ace.get_operators(brain_session)

regular_operators = all_operators[all_operators['scope']=='REGULAR']

operators_list = regular_operators['name'].tolist()

dataset_ids = ['pv87', 'fundamental17']

data_fields = pd.concat([

ace.get_datafields(brain_session,region='USA',universe='TOP3000',

dataset_id=dataset_id, data_type='ALL')

for dataset_id in dataset_ids

], ignore_index=True)

datafields_summary = [

f"{row['id']} (类型: {row.get('type','N/A')}, 名称: {row.get('name','N/A')})"

for _, row in data_fields.iterrows()

]

datafields_str = "\n".join(datafields_summary[:150])

# 构建优化 prompt

prompt = f"""你是一位资深量化研究员，正在进行 Alpha 因子的迭代优化。

【上一轮最佳 Alpha】

表达式: {base_expression}

性能: Sharpe={base_alpha['sharpe']:.4f}, Fitness={base_alpha['fitness']:.4f}, Turnover={base_alpha['turnover']:.4f}

【优化建议】

{optimization_suggestions}

【可用资源】

操作符（部分）: {', '.join(operators_list[:50])}

可用数据字段:

{datafields_str}

【优化任务】

基于上述最佳 Alpha 和优化建议，生成 {num_new_alphas} 个改进版本的 Alpha 表达式。

【优化策略】

1. **保留优势**: 保持最佳 Alpha 中表现好的核心逻辑

2. **针对性改进**: 根据优化建议调整参数或操作符

3. **渐进式变化**: 每次只改变 1-2 个关键要素，避免过度变异

4. **多样化探索**: 在保持核心逻辑的同时，尝试不同的实现方式

【具体改进方向】

- 如果 Turnover 过高: 增加时间窗口参数（如 20→40），使用 ts_decay_linear

- 如果 Sharpe 不足: 尝试组合更多数据字段，增强信号强度

- 如果 Fitness 偏低: 添加 winsorize、rank、neutralize 提升稳健性

- 探索新的数据类别: 基本面、分析师预期、情绪指标等

【语法规范】

- type=MATRIX 字段可直接使用

- type=VECTOR 字段必须用 Vector() 包装

- type=GROUP 字段只能作为 Group 操作符参数

- 确保所有括号匹配，参数格式正确

【输出格式】

请生成 {num_new_alphas} 个表达式，每行一个，格式如下：

表达式1  # 改进说明

表达式2  # 改进说明

...

示例：

ts_decay_linear(rank(fundamental17_sales_growth), 40)  # 增加时间窗口从20到40，降低换手率

"""

print("正在调用 LLM 生成优化后的 Alpha...")

response = await call_llm(prompt, timeout=180)

if response is None:

print("✗ LLM 调用失败")

return []

print("✓ LLM 生成成功\n")

# 解析生成的 Alpha 表达式

parsed_alphas = parse_alpha_expressions(response)

if not parsed_alphas:

print("警告: 未能解析出有效的 Alpha 表达式")

return []

print(f"成功解析 {len(parsed_alphas)} 个 Alpha 表达式，开始模拟...\n")

# 模拟新生成的 Alpha

new_alpha_ids = []

successful_simulations = []

failed_simulations = []

for idx, (expression, description) in enumerate(parsed_alphas, 1):

print(f"--- 模拟优化 Alpha {idx}/{len(parsed_alphas)} ---")

print(f"表达式: {expression}")

print(f"说明: {description}")

try:

simulate_data = ace.generate_alpha(

regular=expression,

alpha_type="REGULAR",

region="USA",

universe="TOP3000",

delay=1,

decay=0,

neutralization="INDUSTRY",

truncation=0.08,

pasteurization="ON",

nan_handling="OFF",

unit_handling="VERIFY",

visualization=True

)

print("正在提交模拟...")

simulation_result = ace.simulate_single_alpha(brain_session, simulate_data)

child_alpha_id = simulation_result.get('alpha_id')

if child_alpha_id:

print(f"✓ 模拟成功! Alpha ID: {child_alpha_id}")

# 设置标签（使用原始父 Alpha ID）

parent_tag = base_alpha.get('parent_alpha_id', base_alpha_id)

full_description = f"【父 Alpha】{parent_tag}\n【优化自】{base_alpha_id}\n【改进说明】{description}"

ace.set_alpha_properties(

brain_session,

child_alpha_id,

tags=[parent_tag],

regular_desc=full_description

)

print(f"✓ 已设置标签: {parent_tag}\n")

new_alpha_ids.append(child_alpha_id)

successful_simulations.append({

'alpha_id': child_alpha_id,

'expression': expression,

'description': description

})

else:

print(f"✗ 模拟失败: 未返回 Alpha ID\n")

failed_simulations.append({

'expression': expression,

'reason': '未返回 Alpha ID'

})

except Exception as e:

print(f"✗ 模拟出错: {str(e)}\n")

failed_simulations.append({

'expression': expression,

'reason': str(e)

})

# 输出总结

print(f"{'='*60}")

print(f"本轮优化模拟总结")

print(f"{'='*60}")

print(f"成功: {len(successful_simulations)} 个")

print(f"失败: {len(failed_simulations)} 个")

if successful_simulations:

print("\n成功的 Alpha:")

for item in successful_simulations:

print(f"  - {item['alpha_id']}: {item['expression'][:60]}...")

if failed_simulations:

print("\n失败的 Alpha:")

for item in failed_simulations:

print(f"  - {item['expression'][:60]}... (原因: {item['reason']})")

return new_alpha_ids

asyncdeffull_auto_iteration_workflow(parent_alpha_id,max_iterations=5,alphas_per_iteration=5,

selection_criteria='balanced', min_quality_threshold=None):

"""完全自动化的迭代优化工作流"""

brain_session = ace.start_session()

print(f"\n{'#'*80}")

print(f"# 完全自动化 Alpha 迭代优化工作流")

print(f"# 初始父 Alpha: {parent_alpha_id}")

print(f"# 最大迭代次数: {max_iterations}")

print(f"# 每轮生成数量: {alphas_per_iteration}")

print(f"# 选择标准: {selection_criteria}")

print(f"{'#'*80}\n")

# 设置默认质量阈值

if min_quality_threshold is None:

min_quality_threshold = {

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

all_iterations_history = []

current_parent_id = parent_alpha_id

for iteration in range(1, max_iterations + 1):

print(f"\n{'='*80}")

print(f"第 {iteration}/{max_iterations} 轮迭代")

print(f"{'='*80}\n")

iteration_start_time = datetime.now()

# ===== 步骤 1: 获取当前 Alpha 家族 =====

print("步骤 1: 检索 Alpha 家族...")

alpha_ids = await get_alphas_by_tag(brain_session, current_parent_id)

if not alpha_ids:

if iteration == 1:

print(f"第一轮未找到 Alpha，请先运行初始 Alpha 生成")

return None

else:

print("未找到新的 Alpha，使用上一轮数据")

break

print(f"找到 {len(alpha_ids)} 个 Alpha\n")

# ===== 步骤 2: 获取性能数据 =====

print("步骤 2: 获取性能指标...")

performance_data = []

for alpha_id in alpha_ids:

print(f"  获取 {alpha_id}...")

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

perf['parent_alpha_id'] = current_parent_id

performance_data.append(perf)

if not performance_data:

print("未能获取任何性能数据")

break

performance_df = pd.DataFrame(performance_data)

print(f"成功获取 {len(performance_df)} 个 Alpha 的性能数据\n")

# ===== 步骤 3: 可视化 =====

print("步骤 3: 生成可视化图表...")

visualize_performance(performance_data, current_parent_id)

# ===== 步骤 4: 选择最佳 Alpha =====

print("\n步骤 4: 选择最佳 Alpha...")

best_alphas = await select_best_alphas(performance_df, selection_criteria, top_n=3)

if not best_alphas:

print("未能选择出最佳 Alpha")

break

# ===== 步骤 5: 检查是否达到质量阈值 =====

print("\n步骤 5: 检查质量阈值...")

top_alpha = best_alphas[0]

quality_check = (

top_alpha['sharpe'] >= min_quality_threshold['sharpe'] and

top_alpha['fitness'] >= min_quality_threshold['fitness'] and

top_alpha['turnover'] <= min_quality_threshold['turnover']

)

if quality_check:

print(f"✓ 达到质量阈值!")

print(f"  Sharpe: {top_alpha['sharpe']:.4f} >= {min_quality_threshold['sharpe']}")

print(f"  Fitness: {top_alpha['fitness']:.4f} >= {min_quality_threshold['fitness']}")

print(f"  Turnover: {top_alpha['turnover']:.4f} <= {min_quality_threshold['turnover']}")

should_continue = False

reason = "达到质量阈值，优化成功"

suggestions = []

else:

# ===== 步骤 6: 决策是否继续迭代 =====

print("\n步骤 6: 迭代决策...")

should_continue, reason, suggestions = await decide_next_iteration(

performance_df, iteration, max_iterations

)

# ===== 步骤 7: LLM 分析 =====

print("\n步骤 7: LLM 分析结果...")

llm_analysis = await llm_analyze_results(performance_df, current_parent_id, brain_session)

print(f"\n【LLM 分析】\n{llm_analysis}\n")

# ===== 步骤 8: 生成优化建议 =====

print("\n步骤 8: 生成优化建议...")

llm_suggestions = await llm_iteration_suggestions(performance_df, iteration, best_alphas)

print(f"\n【LLM 优化建议】\n{llm_suggestions}\n")

# 保存本轮数据

iteration_data = {

'iteration': iteration,

'parent_alpha_id': current_parent_id,

'alpha_count': len(alpha_ids),

'performance_df': performance_df,

'best_alphas': best_alphas,

'should_continue': should_continue,

'reason': reason,

'suggestions': suggestions,

'llm_analysis': llm_analysis,

'llm_suggestions': llm_suggestions,

'duration': (datetime.now() - iteration_start_time).total_seconds()

}

all_iterations_history.append(iteration_data)

# ===== 决策点: 是否继续迭代 =====

if not should_continue:

print(f"\n{'='*80}")

print(f"✓ 迭代结束: {reason}")

print(f"{'='*80}\n")

break

# ===== 步骤 9: 生成下一轮 Alpha =====

if iteration < max_iterations:

print(f"\n步骤 9: 生成下一轮优化 Alpha...")

print(f"{'='*80}\n")

new_alpha_ids = await generate_optimized_alphas_from_best(

best_alphas, brain_session, llm_suggestions,

num_new_alphas=alphas_per_iteration

)

if not new_alpha_ids:

print("未能生成新的 Alpha，迭代终止")

break

print(f"\n✓ 成功生成 {len(new_alpha_ids)} 个新 Alpha")

print(f"等待模拟完成后进入下一轮...\n")

# 等待一段时间让模拟完成

wait_time = 30

print(f"等待 {wait_time} 秒让模拟完成...")

await asyncio.sleep(wait_time)

# ===== 最终总结 =====

print(f"\n{'#'*80}")

print(f"# 迭代优化完成")

print(f"# 总迭代轮数: {len(all_iterations_history)}")

print(f"{'#'*80}\n")

# 汇总所有 Alpha

print("汇总所有迭代的 Alpha...")

all_alpha_ids = await get_alphas_by_tag(brain_session, parent_alpha_id)

all_performance_data = []

for alpha_id in all_alpha_ids:

perf = await get_alpha_performance(brain_session, alpha_id)

if perf:

all_performance_data.append(perf)

final_performance_df = pd.DataFrame(all_performance_data)

# 选择最终的最佳 Alpha

print("\n选择最终最佳 Alpha...")

final_best_alphas = await select_best_alphas(final_performance_df, selection_criteria, top_n=5)

# 生成最终可视化

print("\n生成最终性能对比图...")

visualize_performance(all_performance_data, parent_alpha_id)

# 导出最终报告

print("\n导出最终报告...")

final_report = await export_alpha_family(

parent_alpha_id,

final_performance_df,

final_best_alphas,

output_file=f'alpha_family_{parent_alpha_id}_final_report.txt'

)

# 返回完整结果

return {

'iterations_history': all_iterations_history,

'final_performance_df': final_performance_df,

'final_best_alphas': final_best_alphas,

'final_report': final_report,

'total_alphas_generated': len(all_alpha_ids),

'total_iterations': len(all_iterations_history)

}

# ==================== 执行完全自动化工作流 ====================

# 运行完全自动化的迭代优化

parent_alpha_id = "kqEnlEA8"  # 替换为你的初始父 Alpha ID

results = await full_auto_iteration_workflow(

parent_alpha_id=parent_alpha_id,

max_iterations=8,              # 最多迭代 8 轮

alphas_per_iteration=5,        # 每轮生成 5 个 Alpha

selection_criteria='balanced',  # 综合平衡选择

min_quality_threshold={        # 质量阈值（达到即停止）

'sharpe': 1.5,

'fitness': 1,

'turnover': 0.15

}

)

# 查看结果

if results:

print(f"\n{'='*80}")

print("最终结果摘要")

print(f"{'='*80}")

print(f"总迭代轮数: {results['total_iterations']}")

print(f"总生成 Alpha 数: {results['total_alphas_generated']}")

print(f"\nTop 5 最佳 Alpha:")

for i, alpha in enumerate(results['final_best_alphas'][:5], 1):

print(f"{i}. {alpha['alpha_id']} - Sharpe: {alpha['sharpe']:.4f}, Fitness: {alpha['fitness']:.4f}")

！！！！最后欢迎在评论区讨论和留言，看到点赞和留言我会开心。

---

### 帖子 #49: Initialize forum MCP servertry:    from mcp.server.fastmcp import FastMCP    forum_mcp = FastMCP('brain_forum_server')    forum_mcp.run()except ImportError:    Fallback for testing    forum_mcp = None
- **主帖链接**: https://support.worldquantbrain.com[L2] 如何在VSCODE上安装我发现的MCP傻瓜式教程来了经验分享_34064552577559.md
- **讨论数**: 49

**8月22日最新更新：forum已经集成在platfrom里了,platfrom可以就行！亮一个灯就行！！！！！！**

第一步：在Vscode商店下载Roo code插件；


> [!NOTE] [图片 OCR 识别内容]
> RooCODE
> Roo Code
> Costrict (prev. Cline
> 2K
> Extension name
> Roo
> com
> 740,278
> (304)
> Costrict: strict Al coder for enterp..
> zgsm-ai
> Install
> whole dev team of Alagents in your editor。
> Roo Code
> 740K
> 5
> Install
> Auto Update
> t
> Whole dev team of Alagents in
> Roo Code
> Install
> DETAILS
> FEATURES
> CHANGELOG
> Kilo Code AI Agent (..
> 193k
> 龆
> Open Source Al coding assistant f
> Kilo Code
> Install
> English
> Catala
> Deutsch
> Espanol
> Francais
> C
> Bahasa Indonesia
> Italiano
> 日本
> Marketplace


第二步：在终端输入pip install cnhkmcp ， pip install pydantic[email]，pip install email-validator


> [!NOTE] [图片 OCR 识别内容]
> PROBLEMS
> OUTPUT
> DEBUG CONSOLE
> TERMINAL
> PORTS
> JUPYTER
> python3. 13-venvshoner@lgz wq
> %
> pip install cnhkmcp
> Collect=
> cnhkmcp
> Downloading cnhkmcp-1.2.0-py3-none-any.whl.metadata
> (5.2 kB)
> Requirement
> already satisfied:
> requests>=2.28.0
> i
> /Users /shoner /venv /
> 'python3.13-venv
> /lib/python3 . 13/site-packages
> (from cnhkmcp)
> (2.32.3)
> Requirement
> already satisfied: pandas>=l.5.0
> in /Users/shoner /venv /python3. 13-venv/li
> b/python3 . 13/site-packages
> (from
> cnhkmcp)
> (2.2.3)
> Collecting selenium>=4.0.0
> from
> cnhkmcp)
> Download
> selenium-4.34.2-py3-none-any
> Whl.metadata (7.5 kB)
> Requirement
> already satisfied:
> beautifulsoup4>=4.11.0
> in
> /Users/shoner /venv / python3.1
> 3-Venv /lib/
> 'python3. 13/site-packages_
> (from cnhkmcp)
> (4.13.4)
> C〉170+1
> m0
> 千C
> Lm
> ing
> ing


第三步：打开mcp本地目录，找到untracked文件夹，路径应该是  site-packages/cnhkmcp/untracked

第四步：找到该文件夹里的user_config.json打开编辑输入你在 **worldquantbrain** 的账号密码。

第五步：打开VScode 的RooCode插件，左边导航栏袋鼠图标，配置一个api，以ds api为例（打开deepseek，右上角api开放平台，api keys，创建，复制，粘贴进来（记得充钱））。


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十6』
> To doits magic, Roo needsan API
> We recommend using an LLM Router:
> OpenRouter
> A unified interface for LLMs
> Requesty
> optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> Anthropic documentation
> Anthropic
> You must provide
> Valid API key。
> Anthropic API
> Enter API Key.
> API keys are stored securely in VSCode's Secret Storage
> Get Anthropic API
> Use custom base URL
> https:Ilapi.anthropic.com
> Pass Anthropic API Key as Authorization header instead of X-Api-Key
> Import Settings
> Let's 90!
> Vo muot nrovido
> 3 Tlid 4DILo
> key.
> YoUT
> Key
> Key



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十Ht
> To doits magic, Roo needsan API
> We recommend usingan LLM Router:
> OpenRouter
> unified interface for LLMs
> Requesty
> Your optimized LLM router
> $1 free credit
> OryoU can
> bring your provider API key:
> API Provider
> DeepSeek documentation
> DeepSeek
> DeepSeek API
> API keys are stored securely in VSCode's Secret Storage
> Model
> deepseek-chat
> DeepSeek-V3 achieves a significant breakthrough in inference speed over previous
> models
> It tops the leaderboard among open-source models and rivals the most
> advanced closed-source models globally。
> Does not support images
> Does not support computer use
> Crnnnrta nrnmnt nonhinn
> Import Settings
> Let's 90!
> key:
> Key


第六步：插件右上角... 选择mcp server


> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> submitipy
> History
> V3.25
> Modes
> MCP Servers
> Open in Editor



> [!NOTE] [图片 OCR 识别内容]
> ROO CODE
> 十H 』
> MCP Servers
> Done
> The Model Context Protocol enables communication With locally running MCP servers that
> provide additional tools and resources to extend Roo's capabilities. You can use community-made
> servers or ask Roo to create new tools specific to your Workflow (e.9.,
> add a tool that gets the
> latest npm docs").
> Enable MCP Servers
> Turn this ONto let Roo Use tools from connected MCP servers
> This gives Roo more capabilities. If you
> don't plan to use these extra tools, turn i OFF to help reduce API token Costs
> Enable MCP Server Creation
> Enable this to have Roo help you build new custom MCP servers. Learn about server creation
> Hint: To reduce APItoken costs, disable this setting when
> are not actively asking Roo to create a
> new MCP server。
> Edit Global MCP
> Edit Project MCP
> Refresh MCP Servers
> MCP Marketplace
> Learn more about editing MCP settings files
> VoU


点上两个按钮，然后编辑全局mcp。

第八步：对 MCP 文件进行配置，示例配置文件如下：args 分别是两个 mcp 文件的绝对路径，command 是你 python 程序的绝对路径。请根据你电脑的具体路径进行更改。


> [!NOTE] [图片 OCR 识别内容]
> mcpServers
> {
> worldquant-brain- platform
> {
> Command"
> C: |Users
> IAdministrator
> IAppData'
> ILocal | IPrograms
> IPython'
> IPython313
> Ipython.exe
> args
> "C: | Users
> IAdministrator
> IAppData | ILocal
> IPrograms
> IPython
> IPyt
> hon313 |Lib | Isite-packages | Icnhkmcp
> untracked l Iplatform_functions . Py
> ],
> "description
> "Worldouant
> BRAIN
> Platform MCP
> Server
> Comprehensive trading platform integration with
> simulation management;
> alpha operations,
> and authentication。
> Credentials
> are
> Stored
> in
> User
> config.json in
> the
> same directory
> Provides tools
> for creating
> Isimulations, checking status,
> managing alphas,
> and accessing platform
> features
> },
> worldquant-brain-forum" :
> {
> Command"
> "C: |Users | IAdministrator
> IAppData
> ILocal
> IPrograms
> IPython
> IPython313
> Ipython.exe
> "args'
> "C: | |Users
> IAdministrator
> IAppData | ILocal
> IPrograms | |Python | IPyt
> hon313|ILib |Isite-packages | Icnhkmcp'
> untracked
> forum_functions .Py'
> ]
> description"
> "Worldouant
> BRAIN
> Forum MCP
> SerVer
> Forum
> interaction
> and knowledge extraction tools
> Provides glossary access,
> forum post reading〉
> and
> community
> features
> Credentials
> are stored
> in
> user_config.json
> in
> the
> same directory
> Supports headless
> browser
> automation
> for forum scraping
> and
> content extraction


配置成功应该是两个绿灯（科学上网）

如果平台连接失败，尝试安装（ ）


> [!NOTE] [图片 OCR 识别内容]
> 才启石 Roo 0芾卟刨徒新司正又 MCT 胙方琵。
> #舨夯砧刨迕
> 捉示:  不需要 Roo 创』新 MCP 服务器时廷议关闭;
> 戒少 API Token 贳用。
> worldquant-brain-platfomm
> global
> worldquant-brain-forum
> gobal


接下来你有可以让他来帮你干活啦！快来创建你自己的量化公司，招募并培训你的员工吧！

```
{  "mcpServers": {    "worldquant-brain-platform": {      "command": "/opt/anaconda3/bin/python",      "args": [        "/opt/anaconda3/lib/python3.12/site-packages/cnhkmcp/untracked/platform_functions.py"      ],      "description": "WorldQuant BRAIN Platform MCP Server - Comprehensive trading platform integration with simulation management, alpha operations, and authentication. Credentials are stored in user_config.json in the same directory. Provides tools for creating simulations, checking status, managing alphas, and accessing platform features. Includes 25+ MCP tools for authentication, simulation creation, alpha management, dataset access, performance analysis, competition management, user profile operations, forum integration, and advanced analytics."    }  }}
```

---

### 帖子 #50: PnL = ∑(Robustness * Creativity)
- **主帖链接**: [L2] 成为expertvf连续三个月上09经验分享.md
- **讨论数**: 15


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 2Y36280 (Me)
> 8,51
> 0,90


近三次更新的vf变化是：0.98->0.91->0.90，这次更新来到了12月，刚好包括了整个expert这三个月，因此打算依次查看下这三个月提交的alpha，总结expert这三个月高vf的原因。

首先8、9、10月的vf猛涨来到了0.98， [vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] vf猛增048-098第一次SA拿满60刀.md) 在这个帖子里已经总结了一部分了。

接下来是9、10、11月。
由于os已经更新了，可以很明显的看到11月提交的USA地区OS/IS Ratio这个指标很差，一共提交了11个，但是有5个alpha的OS/IS Ratio都小于0，剩下6个虽然是正的，但是也都小于0.4。可以说这对vf的影响是巨大的。我发现首先，三五的not(own)alpha确实很一般，基本os都崩了；然后基本上pnl到最后平了，os不会多好，比如：
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> ?nl
> ZSM
> ZOM
> 1SM
> 1OM
> 11/0812017
> Equal Weight Pnl:
> 12.3311
> Train Combo Pn:
> 508.08k
> 5OOOK
> 骷
> 2014
> 2015
> 2016
> 2017
> 2018
> 2020
> 2021
> 2022
> 2023
> Combo Pnl
> Equal Weieht Pnl
> 2019
 
同时，我还交了15个EUR地区的alpha，看OS/IS Ratio，大都是正的，但是也基本是不到1的。还好GLB地区和ASI地区的os还不错，尤其GLB地区，怪不得老师一直推荐我们做GLB的glb的alpha，不仅是11月，我翻看了我所有更新os的glb的alpha（由于glb跑得慢所以交的也不多），发现os都挺不错的，没有多少很崩的os。 
> [!NOTE] [图片 OCR 识别内容]
> OSIIS Ratio
> e.6> 1
> 1.77
> 1.72
> 1.01
> 0.99
> 0.82
> 0.82
> 0.80


ASI地区经过多次的增加难度，os也还可以，比11月的USA和EUR地区都好。主要这两个地区发力，才能vf才能只掉到0.91。

最后是10、11、12月。
12月我主交的是usa，一共提交了43个，其次是eur，交了21个。都是ATOM居多。感觉我做的USA地区的alpha，os会差一些，可能是有时候想要尽量减少operator的数量，导致不太稳定可能。同时12月也发现很多not own的sa，os都不好，own的sa反倒os会跟is一致。

最后，虽然vf还在0.9，很开心，但是os更新的结果也是要警醒自己。要管住手，提交要有一定的标准底线。一些pnl已经有些低头了的，一定要慎重；如果在犹豫要不要交，那感觉大概率还是别交；要交得多且多样，不仅是数据多样，思路最好也多样，多用ai尝试修改，生成模板，通过os可以看到很多alpha都只是在is期间表现好而已，如果交的少的话，除非对自己的alpha很有信心，不然还是越多越稳定。

最后祝大家新年快乐，月月vf1.0，季季都是GM。

---

### 帖子 #51: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 成为expertvf连续三个月上09经验分享_38720223996439.md
- **讨论数**: 15


> [!NOTE] [图片 OCR 识别内容]
> User
> Weight
> Value
> Factor
> Factor
> 2Y36280 (Me)
> 8,51
> 0,90


近三次更新的vf变化是：0.98->0.91->0.90，这次更新来到了12月，刚好包括了整个expert这三个月，因此打算依次查看下这三个月提交的alpha，总结expert这三个月高vf的原因。

首先8、9、10月的vf猛涨来到了0.98， [vf猛增0.48->0.98，第一次SA拿满60刀 – WorldQuant BRAIN](../顾问 MZ45384 (Rank 51)/[Commented] vf猛增048-098第一次SA拿满60刀_37055219307799.md) 在这个帖子里已经总结了一部分了。

接下来是9、10、11月。
由于os已经更新了，可以很明显的看到11月提交的USA地区OS/IS Ratio这个指标很差，一共提交了11个，但是有5个alpha的OS/IS Ratio都小于0，剩下6个虽然是正的，但是也都小于0.4。可以说这对vf的影响是巨大的。我发现首先，三五的not(own)alpha确实很一般，基本os都崩了；然后基本上pnl到最后平了，os不会多好，比如：
 
> [!NOTE] [图片 OCR 识别内容]
> N Chart
> ?nl
> ZSM
> ZOM
> 1SM
> 1OM
> 11/0812017
> Equal Weight Pnl:
> 12.3311
> Train Combo Pn:
> 508.08k
> 5OOOK
> 骷
> 2014
> 2015
> 2016
> 2017
> 2018
> 2020
> 2021
> 2022
> 2023
> Combo Pnl
> Equal Weieht Pnl
> 2019
 
同时，我还交了15个EUR地区的alpha，看OS/IS Ratio，大都是正的，但是也基本是不到1的。还好GLB地区和ASI地区的os还不错，尤其GLB地区，怪不得老师一直推荐我们做GLB的glb的alpha，不仅是11月，我翻看了我所有更新os的glb的alpha（由于glb跑得慢所以交的也不多），发现os都挺不错的，没有多少很崩的os。 
> [!NOTE] [图片 OCR 识别内容]
> OSIIS Ratio
> e.6> 1
> 1.77
> 1.72
> 1.01
> 0.99
> 0.82
> 0.82
> 0.80


ASI地区经过多次的增加难度，os也还可以，比11月的USA和EUR地区都好。主要这两个地区发力，才能vf才能只掉到0.91。

最后是10、11、12月。
12月我主交的是usa，一共提交了43个，其次是eur，交了21个。都是ATOM居多。感觉我做的USA地区的alpha，os会差一些，可能是有时候想要尽量减少operator的数量，导致不太稳定可能。同时12月也发现很多not own的sa，os都不好，own的sa反倒os会跟is一致。

最后，虽然vf还在0.9，很开心，但是os更新的结果也是要警醒自己。要管住手，提交要有一定的标准底线。一些pnl已经有些低头了的，一定要慎重；如果在犹豫要不要交，那感觉大概率还是别交；要交得多且多样，不仅是数据多样，思路最好也多样，多用ai尝试修改，生成模板，通过os可以看到很多alpha都只是在is期间表现好而已，如果交的少的话，除非对自己的alpha很有信心，不然还是越多越稳定。

最后祝大家新年快乐，月月vf1.0，季季都是GM。

---

### 帖子 #52: 成为顾问五个月，分享vf保持0.9+的经验经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 成为顾问五个月分享vf保持09的经验经验分享_34938580496023.md
- **讨论数**: 30

我在四月份成为了conditional consultant，vf经历了0.5-0.97-0.98-0.93的变化，除去最开始的vf空窗期外均保持0.9以上。我将从我的个人经历分享我的vf经验


> [!NOTE] [图片 OCR 识别内容]
> Base Payment


1.atom是非常重要的vf因素，强烈建议大家多交atom，事实上我绝大多数alpha都是atom，我并没有选择死板的使用一二三街模板，对于每一个不同的fields因为其中数据是具有共性的，我们可以根据其description进行具有经济及意义的模板攥写，而后发现该模板有较好的指标效果后进行代码批量回测，这得与在顾问课上weijie老师说经济意义是非常重要的一个因素。

2.不要死板的困在某一个地区，我对每一个fields都只提交3-4个在成功点亮pyramids后结束，一定要保持多样性，甚至于单个fields利用模板提交效果最好的那一个，然后更换其他fields用三个不同的fields点亮一个pyramids。

3.其实很多时候不必纠结于 base payment ，实际上base payment和pc有着很大的关系，但很多pc很低调alpha很容易存在某种缺陷。因此我建议可以观察近三年样本表现，以及可以利用sign 符号验证表现的稳定性。

4.保持高margin和合理的turnover,尽量将turnover保持在5-15的区间并且基本至少保证margin有大于10的效果，这是一个alpha能否拥有较好收益的一大因素。

5.一定要保证有一定的数量！我的六月份vf从0.98-0.93的因素在于六月份因准备考试只交了40几个alpha，造成的不稳定效果，因此保证一定数量的alpha提交时必须的。

最后在季度末请大家注意六维，我也在本季度正在冲击master

最后感谢weijie老师，感谢研究小组的各位

---

### 帖子 #53: 曲折的Value Factor之路：0.2-0.4-0.8-0.5-0.94-0.99, 得出的一点点心得经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 曲折的Value Factor之路02-04-08-05-094-099 得出的一点点心得经验分享_35888667819159.md
- **讨论数**: 7

去年10月成为的顾问，应该也算是一名老顾问了。vf波动很大，前期基本都是0.2左右，ppac比赛后开始回升，但比赛结束后，又被打入谷底，最近两次更新浮出水面：0.94，0.99.写一点自己的心得，供大家参考。

声明：论坛里关于Value Factor的讨论很多，不要把这些讨论直接照搬，这些都是大家站在自己的角度总结的经验。如果一个顾问的VF常年保持在0.9以上，我觉得是值得参考模仿的。但大多数帖子只是停留在0.9一次而得出的经验，可能不够全面。包括这篇帖子，也是一点心得分享，请勿直接照搬。这个帖子我会尽力在每次VF更新的时候都总结一下，希望能给大家一点参考。

最近几个月我做了那些改变：

1. 持续的提交Super Alpha；

2. 对Margin的要求提高到10以上；

3. 多点塔提高多样性；

4. 基本都是ATOM。

5. 经常交不上ra，那就不交。

中文顾问论坛是一个宝库，推荐新顾问们一定要多看看里面的帖子，常看常新。回测提交并没有一个万能钥匙，但一定有一个固定不变的方法论，结合自己的情况，不断成长。

长期、短期永远有一个取舍，收入是短期的，学习到知识和经验，才是自己未来的财富。不要小看量化交易这四个字的含金量。

---

### 帖子 #54: 获取数据，修改日期范围和alpha数量
- **主帖链接**: https://support.worldquantbrain.com[L2] 来时路运气与努力交织的结果 vf 从 033 到 098 的成长附代码经验分享_35877688682391.md
- **讨论数**: 12

这次 vf 更新至 0.98，着实出乎我的意料。原本预期在 0.7-0.85 之间，能有这样的突破，运气成分确实占了不小比重 —— 毕竟至今我仍未完全摸清直接影响 vf 的核心指标。这里必须感谢论坛的前辈们，在 "坐牢期" 按他们分享的方法提交后，竟收获了这样的意外之喜。

虽不敢说能给大家太多成熟建议，但还是想把这几个月的实践总结出来，希望能提供一些参考：

1. **紧跟官方节奏提交。** 在 "坐牢" 阶段，官方强调多交 atom，我便集中精力提交这类内容，非 atom 的一律不碰，确保方向与平台引导一致。
2. **保证提交数量，稳定输出。** 记得很早前有老师说过："宁可每天交 4 个合格的 RA，也不要每天只交 1 个优质的 RA。" 我践行这一点，每天尽量保证 "3+1"，最好能做到 "4+1"，保持稳定的活跃度。
3. **重视 SA 质量，助力提高vf 。** 能快速提升，SA 的贡献功不可没。我始终保证至少有一个数据在 5 以上（Sharp/Fitness/PC），也曾有过几次提交 3 个 5 的 SA 的经历，优质内容的积累或许是关键。 这里补充一点，SA需要你提交更多的RA来组合，多交RA很重要。
4. **多区域覆盖，借势活动。** 由于同时在冲塔，我几乎覆盖了所有可提交的区域。结合官方的双倍活动，既避免了提交区域的单一性，也提高了投入产出比。

前辈们总结的提升 vf 的方法，大致可归为两类：

**垂直深耕，聚焦质量：** 追求 Sharp 大于 2、Fitness1.5 以上，同时保证 pnl 曲线美观，兼顾低 turnover、低 Drawdown、高 Return 与高 margin。

**广度拓展，多维布局：** 多冲塔 + 低sc和pc + 坚持 ATOM，在保证数量的基础上，确保其他数据不过于拉垮（比如 margin 最好维持在 10% 以上）。

最后附上这几个月的部分数据，供大家参考。也恳请看到的前辈们不吝指导 —— 从数据趋势看，我预判下个月的 vf 可能会有所回落。股市里常说："凭运气赚的钱，终会凭实力亏回去。" 所以搞懂底层逻辑才是根本。

（图片传不上.jpeg ）

但有一句话始终没错：一分耕耘，一分收获。即便当下有运气加持，但若没有前期的努力铺垫，也难有这份回报。

文末附上我 **基于官方代码** 修改的工具，能查询当前各项数据的平均值。建议大家每周跑一次，及时关注指标波动，针对性调整。共勉！

> from datetime import datetime
> from machine_lib import *
> s = login()
> def get_submit_alphas(s, start_date, end_date, alpha_num):
> output = {
> "prodCorrelation": [],
> "sharpe": [],
> "turnover": [],
> "fitness": [],
> "returns": [],
> "drawdown": [],
> "margin": [],
> "pnl": []
> }
> for i in range(0, alpha_num, 100):
> # 构造查询url
> url_e = " [[链接已屏蔽])]([链接已屏蔽]))  \
> + "&status!=UNSUBMITTED%1FIS_FAIL&dateSubmitted%3E=" + start_date  \
> + "T00:00:00-04:00&dateSubmitted%3C" + end_date \
> + "T00:00:00-04:00&order=-is.sharpe&hidden=false&type!=SUPER"
> urls = [url_e]
> for url in urls:
> response = s.get(url)
> try:
> alpha_list = response.json()["results"]
> for alpha in alpha_list:
> output["prodCorrelation"].append(alpha["is"]["prodCorrelation"])
> output["sharpe"].append(alpha["is"]["sharpe"])
> output["turnover"].append(alpha["is"]["turnover"])
> output["fitness"].append(alpha["is"]["fitness"])
> output["returns"].append(alpha["is"]["returns"])
> output["drawdown"].append(alpha["is"]["drawdown"])
> output["margin"].append(alpha["is"]["margin"])
> output["pnl"].append(alpha["is"]["pnl"])
> return output
> except Exception as e:
> print(f"当前异常为{e}")
> resp = s.get(' [[链接已屏蔽]) ')
> if resp.status_code != 200:
> print(f"resp 返回值{resp.status_code}")
> return output
> # 获取数据，修改日期范围和alpha数量
> alpha_metrics = get_submit_alphas(s, "2025-10-01", "2025-11-01", 200)
> # 计算平均值的函数
> def calculate_average(metric_list):
> if len(metric_list) > 0:
> return sum(metric_list) / len(metric_list)
> return 0
> # 分别计算各项指标的平均值
> average_prod_corr = calculate_average(alpha_metrics["prodCorrelation"])
> average_sharpe = calculate_average(alpha_metrics["sharpe"])
> average_turnover = calculate_average(alpha_metrics["turnover"])
> average_fitness = calculate_average(alpha_metrics["fitness"])
> average_returns = calculate_average(alpha_metrics["returns"])
> average_drawdown = calculate_average(alpha_metrics["drawdown"])
> average_margin = calculate_average(alpha_metrics["margin"])
> average_pnl = calculate_average(alpha_metrics["pnl"])  # 计算 Pnl 的平均值
> # 打印结果
> print(f"10月份共提交了{len(alpha_metrics['prodCorrelation'])}个普通alpha")
> print(f"Prod Corr 平均值: {average_prod_corr:.4f}")
> print(f"Sharpe 平均值: {average_sharpe:.4f}")
> print(f"Turnover 平均值: {average_turnover:.4f}")
> print(f"Fitness 平均值: {average_fitness:.4f}")
> print(f"Returns 平均值: {average_returns:.4f}")
> print(f"Drawdown 平均值: {average_drawdown:.4f}")
> print(f"Margin 平均值: {average_margin:.4f}")
> print(f"Pnl 平均值: {average_pnl:.4f}")

---

### 帖子 #55: 理解顾问最重要的指标Value Factor! 分享不同数值对应的预计每日收入
- **主帖链接**: https://support.worldquantbrain.com[L2] 理解顾问最重要的指标Value Factor 分享不同数值对应的预计每日收入_28199144447255.md
- **讨论数**: 40

```
冲击Grand Master! 帮助大家树立信息维护好自己的value factor！感谢大家点击右侧VOTE点赞或留言互动！
```

**终于每日Base Payment从1.X USD 到了现在的20USD，经验分享出来更更多的同学**

**
> [!NOTE] [图片 OCR 识别内容]
> Base Payment
> 15
> 10
**

**1. 什么是Value Factor？**

Value Factor 衡量的是最近提交的Alpha对组合Alpha表现的影响，同时考虑三个特定因素：(a) Alpha的个体表现，(b) 最近Alpha提交的多样性，以及 (c) 提交的独特性，即与您过去的提交以及其他顾问提交的比较。

换句话说，Value Factor 是在适用的日历季度中最近提交的Alpha组合的OS（样本外）表现。

Value Factor 是基础支付和季度支付的组成部分。 **范围是0到1。初始值是0.5，可以在consultant 排行榜上面查到**

**2. 什么时候开始更新Value Factor?**

目前来看每个月会更新一次，11月1日更新的是8月开始交alpha的，12月1日今天应该是更新了9月开始交alpha的，以此类推。（个人观察，如果理解错误请官方指正），每次更新会在右上角Announcement处看到。通查你的base payment的变更会比通知来的更早

**3. 提升Value Factor 都需要注意什么？**

**首先，要有足够多的数量，** 上课老师有讲过统计学中的中心极限定理会保证体现出你的真实水平，但这要建立在足够多的alpha上，个人经验最好保持近乎每个月在50个左右，不少于每天都提交。

**其次，最直观的就是看那条PnL的曲线，** 当你进入到一个阶段后已经不再担心找到可以提交的alpha，就要开始选取好的alpha 来交，以下是典型的几个我认为要三思而后行的

a. 先来个好看的，基本上是比较平稳，覆盖的时间足够长。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,50OK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,000K
> 2,50OK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> ANVI


b. 大家经常可能会遇到PnL的覆盖时间从2018年开始的，但线还算平稳，尤其是最近一两年还不错，原理上自己也能说的通，这种不是说完全不能交，但是需要自己权衡一下。 **之后我也会找时间分享一下如何批量识别这样alpha的代码，求点赞！**


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,50OK
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,5OOK
> 1,00OK
> SOOK
> 03/14/2018
> Pnl: 120.30K
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> {MMM
> NAM


c. 数据时间短，图形很乱，最近一两年走平，甚至是负数的。这种如果不缺alpha的话个人就不建议提交了。


> [!NOTE] [图片 OCR 识别内容]
> Chart
> Pnl
> 6,5OOK
> I
> 6,00OK
> 5,5OOK
> 5,0OOK
> 4,5OOK
> 4,00OK
> 3,5OOK
> 07/31/2018
> Pnl: 3,319.60K
> 3,00OK
> 2,5OOK
> 2,00OK
> 1,50OK
> 1,00OK
> SOOK
> 2013
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> Mp}


**第三，多样性。** 追求多pyramid，这个和genius program的要求也是相辅相成的，也可以理解为BRAIN官方想要奖励和推荐的行为。这里就不建议大家在一个地方交太久，即使有多余的可以留一下等下个月再交（当然也有可能被别人交了，自己权衡下）。尤其如果遇到了oversued的warning以后。

**第四，低相关性。** 这个在很多前辈大佬上分享中也多次提交过了，我基本主要提交的都控制在PROD correlation在0.6以内的，越低越好。你会发现多去探索新的pyramid，会有更高的theme加成，也会更容易有低相关性。

第五，使用performance comparison 功能，关注sharp，fitness 和 margin 提交前后的变化

**3. 如果Value Factor 已经低了怎么办？**

不要摆烂不交了！保持提交，但不要交太多！

这里的建议是每天提交1个alpha，因为交多了也不到1.5USD。但要保证有提交，这样下个月的时候才有可能被拉回来

**4. 不同的value factor对应的base payment可能在什么范围？**

**免责声明：以下仅仅是个人经验，非官方标准**

以提交2个alpha，中等质量为例

Value factor 0.3    daily  1.3 USD

Value factor 0.5    daily 1.5-3 USD

Value factor 0.7    daily 6-10 USD

Value factor 0.8+  daily 15+ USD

Quarterly Payment 还没有太多的经验，后续有更新了再来补充

祝大家都能实现第二收入自由！ 如果觉得有用，记得vote点赞哈

---

### 帖子 #56: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[L2] 用Gemini CLI全自动找Alpha工作流纯Template版_37192789600791.md
- **讨论数**: 30

首先要感谢OB53521大佬的Gemini 3 Pro全自动挖因子方式的无私分享，为我打开了新世界的大门。第二天我就搭建好了CLI开始尝试，自己也在使用的过程中对提示词做了一些修改。

修改内容大概有以下几个方面：

1. 明确AI在回测设置当中的中性化选择。第一次使用的时候我就发现AI喜欢使用NONE作为中性化的选择，为了让AI选择不同的中性化方式，除了在文档中放入所有Document里中性化的解释文章，还把挑选规则放入了提示词当中。

2. AI的确喜欢混信号。开会的时候就听OB53521说AI喜欢混信号，AI碰到难题的时候想到的第一个办法就说混信号，所以要把以下设定放到工作流中去限制他，让他生成single dataset alpha，也就是ATOM alpha。

```json

"classifications": [

{

"id": "DATA_USAGE:SINGLE_DATA_SET",

"name": "Single Data Set Alpha"

}

]

```

3. 把IS Testing Status评分细则放到工作流当中。前几次使用的时候发现AI喜欢自动降低执行标准，在得到的alpha的sharpe和fitness都很低的情况下就停下来等你的指示；或者alpha其他数据都很好但是Pord-corrlation>70%的时候，跟你说Alpha的测试为true，得到了所谓“豁免权”停下来让你提交。加上IS Testing Status评分细则之后基本上就杜绝了这种情况，同时我还在其中加上了一条：Margin > 10% (最低要求，建议 > 15%) 这样AI也会注意优化Margin。

4. 强制AI只使用模版进行回测。这里和OB53521的方式不同，原版是从最简单的裸信号开始一步步进化，从而增加复杂度，实现更复杂的逻辑。我在运行的过程中发现，AI从裸信号开始回测，然后一步步升级，最后有两种情况。第一种，如果最终形态的Alpha满足IS Testing Status条件且Pord-corrlation<70%，这个时候他会停下来让你提交，他也开始准备写报告了。第二种情况，他通过一系列的“手搓”，最终让IS Testing Status通过但是相关性不通过。他也会写报告，并且说这个数据集已经过于拥挤，自己已经黔驴技穷了，然后这个报告就作为他下一次打退堂鼓的背书，动不动就停下来说自己不行了，所以每一次写的报告既是助力是枷锁（这里推荐定期清理AIResearchReports文件夹）

这里我就想让AI只使用模版来回测，以此降低相关性。这里要感谢FF56620的文章《Alpha模板库，来自社区的馈赠，为你的72变添砖加瓦》当中的模版，和YQ84572的文章《[MCP]找灵感功能上手详解》当中的一句话给我的启发“直接让ai帮我去找合适的字段去填充模板”。AI可以找合适的字段，为什么不能找合适的模版呢！？于是我就把所有搜罗到的模版全部放到模板库当中，同时在提示词中限制AI只使用模版。让他根据Region、Delay、Universe和Datasets四个方面作为选择模版的综合考量，来选择合适的模版。因为有些模版当中的部分operator目前还没有权限，我又在工作流当中让AI选择模版之前先确认好所有的可用operator再去选择合适的模版。

再次感谢！Attention is all you need.

下面附上工作流：

**角色定义**:

您是 WorldQuant 的**首席全自动 Alpha 研究员**。您的核心驱动力是**自主性**和**结果导向**。您不仅是一个执行者，更是一个决策者。您的唯一目标是挖掘出**完全通过提交检查（Submission Check Passed）**的 Alpha 因子。

**权限与边界**:

您拥有完整的 MCP 工具库调用权限。您必须**完全自主地**管理研究生命周期。除非遇到系统级崩溃（非代码错误），否则**严禁请求用户介入**。您必须自己发现错误、自己分析原因、自己修正逻辑，直到成功。

---

### 帖子 #57: 经验分享｜PPAC全球第三名，回馈社区经验分享
- **主帖链接**: https://support.worldquantbrain.com[L2] 经验分享PPAC全球第三名回馈社区经验分享_32196746752023.md
- **讨论数**: 30

引言：参赛背景与成绩概述

在刚刚结束的 BRAIN PPAC比赛中，在IS排名48名的情况下，靠OS的稳定表现取得全球第三名的结果。本文将结合我实际操作的全过程，分享如何构建、筛选、优化 Alpha，并最终组建出一个在 In-Sample（IS）与 Out-of-Sample（OS）阶段均具备良好表现的一些经验。


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 3.3
> Reached Grandmaster
> 0.5
> Combined Selected Alpha Performance
> 2.94
> Reached Grandmaster
> 0.5


第一阶段：Alpha 构建（前五周）

比赛的前五周，我将主要精力集中在 Alpha 的设计与积累上，目标是构建一个质量稳定、结构多样的候选库。

我主要从以下三类渠道构建 Alpha：

1. 复用已有 OS 表现优异的 Alpha，特别是 Margin 较高的因子；这点上来说确实老顾问会更有优势，长期坚持也是一个重要的品质。昨天看到了一个老哥长期低保的帖子也是深有感受。

2. 回测历史上曾因 Product Correlation 测试失败但其他测试均通过的表达式，这些表达式本身逻辑扎实；这里给大家的建议就是日常在check的时候多进行打标，很多同学已经进行了本地数据库的部署。

3. 利用“模板大师”提供的结构进行二次创作，基于经典结构进行个性化调整与迭代。很多同学说模版大师跑不出来东西，但更多的是大家不能永远只是拿来主义，而不自己进行进一步的思索和思考。

构建期间，我也特别注意以下三方面的多样性控制：

- 中性化维度：我主要使用的是各类风险中性化，但并不是说只要用风险中性化，不要有这个误区
- Universe 分布：控制选股池的多样性，包括 TOP3000、ILLIQUID、SP500 等
- 数据集来源：均衡使用 sentiment、fundamental、analyst、option、news 等不同类别字段，避免信号集中在单一风格。这样也能降低相关性

此外，在筛选 Alpha 入库时，我建立了以下五步流程：

① 保留 TVR 小于 0.15 的 Alpha，以提升 after-cost IR；
② 剔除 PnL 覆盖率小于 60% 的表达式，避免“厂字形” Alpha；
③ 计算并筛除自相关过高的表达式，提高组合独立性；
④ 要求 10 年中至少有 6 年 Sharpe > 1，且 2022 年表现>1；
⑤ 使用控制变量法测试 Merge Performance 加分情况，根据阶段不同设置加分阈值（初期 1000，后期 300）。对于加分多的再进行一步人工判断，是否符合经济学意义和pnl是否好看等。

第二阶段：Alpha 筛选（第六周）

第六周进入 Alpha 筛选阶段，这一步是整个比赛最为关键的环节。

我首先尝试使用最大 IS 得分贪婪法，即不带标签逐个遍历所有候选 Alpha，计算每次加入后的得分增幅，按增量排序作为组合基础。这种方法虽然能快速捕捉组合的初始脉络，但也暴露出过于依赖 IS 表现、alpha数量过小的局限。在10-15个以后基本就没有能加分的了，但10-15个担心在OS中不够稳健

在初步建立“基石 Alpha”之后，我开始与 GPT 展开深度协作，从多个维度进一步优化组合质量，GPT 协同筛选：风格多样性与结构分级

GPT 在筛选阶段的最大作用体现在两个方面：

1. 风格控制能力：通过分析表达式的语义结构和字段来源，GPT 能将所有候选 Alpha 分类为成长、情绪、波动率、反转等风格，有效避免组合中信号来源高度重叠所带来的过拟合风险。

2. 结构与经济逻辑评估：GPT 帮助对 Alpha 的表达结构和经济含义进行评估，结合回测表现对因子进行分级，明确哪些为主力 Alpha、哪些适合补充信号源，从而提高 OS 阶段的稳健性。

此外，GPT 还协助完成以下操作：

- 对IS指标（主要是Sharpe和Margin），10年内的表现稳定性，pool内相关性，风格重叠度等进行综合打分，这个过程中需要人给与更多的交互和指令；

- 根据相关性矩阵，避免高相关的alpha重复出现，即使pool内自相关都低于0.5，最终选取的基本都是在0.35以下的；

- 避免过多同类中性化、universe 和数据来源重复的表达式；

- 检查表达式结构是否具备合理归一、去极值、回归处理等增强要素。

我做了很多版本，来看IS Score，最终版本 Version 2.8 组合从60个因子中选出了25个基石因子，但这25个因子的IS得分不够理想，为了均衡IS的表现，又从剩下的因子中采取贪心算法最终选取了30个因子。保证IS Score也不会太差。

结语：经验与建议

1、构建符合自己当下条件的工作流。首先这个工作流要符合你当下的实际情况，在质量和数量中寻求一个平衡，过度苛求质量让数量没有保障也不是一个合理的做法。如果需要量化的话我会建议保证每个月有20-40个  每个季度在60以上。否则你的combine和VF也不会稳定。

2. 有关description，很多同学都用标准化的东西糊弄。以我的经验来看，平台上的任何限制和要求都不是拍脑袋的，都是有实际意义的，在写description的过程中，本身是给自己的一道防线。比如我的一个加分alpha，写description的时候data是发布会召开的时间（Time），看到这个时候我就觉得似乎不可靠，就没有提交。

3. Max Trade: 我有一半的alpha开了这个setting，在之前的advisor会议上，开了这个setting
似乎会更加让你的alpha接近真实的市场条件。认真对待自己的alpha，往往会有意想不到的惊喜

4. 说到底，没有任何指标是提交与否的金指标，我也有一些alpha是减分的，依然选择了提交。武侠小说里入门的时候看的是“形” 而进阶了以后重要的是“意”，只有意对了  VF会高，Combined Score会高，比赛也会高！

---

### 帖子 #58: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md
- **讨论数**: 22


> [!NOTE] [图片 OCR 识别内容]
> Genluy
> Synals
> Pramt
> Cobined
> Combinu
> Combttd
> CoIUIU
> 10l
> 01
> CmTPte[
> Alpha
> OwCTPnol
> Solacten
> ISIT TSI5
> Perlomance
> UOh
> Mpha
> Felormnce
> JertormarCe
> P2TIOTIaITCC
> 1 1Aq
> 1763377I
> Gold
> old
> 400
> LZEAATT
> 353
> 4
> THTA70
> Uer
> O
> Emcn
> T
> 298


大家好，标题整蛊一下O(∩_∩)O，我是练习量化4个月的新人顾问Ricardo。2月上旬平台更新了combine和vf，当时我的combine从-1.2一举跃升至3.18，提升超4，前后只隔一个月悬殊却如此之大，属实是个值得研究的典型样本。因此我发布了自己去年11，12月的提交数据，希望能够带给大家一些启发，感兴趣的可以看看，能够更好地衔接本文👉：  [[经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md]([经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md)

再到后来，1月os期更新导致所有存货全部失效，加上那段时间比较忙，所以提交量相比12月是减少的。我本以为这次更新combine下滑在所难免，结果没想到总池combine再创新高，飙升至3.58，位居全球第一！同时ppa池combine也升至1.85，属实是意外之喜。这样看来，我的提交策略确实是有可取之处的，那就书接上回，继续展开讲讲吧！


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combinea Apha
> POwerPool
> SEIECEOAphs
> Combinea Osmosis
> 0.97
> Combin」
> 400
> 090
> 3,00
> 0.30
> 00
> 0,70
> 1.00
> 050
> 0,00
> 0.50
> 1.00
> 015
> 1.77
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202509
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512
> 202501


先看下1月的提交数据（建议ctrl+放大观看）：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> IND
> 01
> 18
> 3.59
> 2.145
> 2.2039
> 4.21
> 2.25
> 2.3839
> 0.003831
> 0.001766
> 0.001897
> 0.2149
> 0.1455
> 0.1455
> USA
> 12
> 3.03
> 1.56
> 1.7492
> 2.56
> 1.885
> 1.9217
> 0.007154
> 0.001891
> 002321
> 0.2848
> 0.0953
> 0.1094


1月我只做了USA和IND两个区,数量不多，不过sharpe、fitness、margin，等关键指标都还不错，无论是中位数还是平均值都远高于提交底线。

再看上次combine出分时的总池数据与本次的对照：


> [!NOTE] [图片 OCR 识别内容]
> Ln]
> Cm』
> m
> Cm
> Cd
> SN
> C
> |
> ST 辜
> U $ [
> Us
> Tdo
> a
> e
> O4


可以发现变化不大，说明之前的策略确实是可行的，1月时我我又对策略进行了更多细化，得出了以下的结论和猜想：

1. **重视近几年表现。** 因子的预测能力都是有时限的，有些因子指标很漂亮但2year sharpe不达标，这很可能说明此因子的快要丧失预测能力了，os表现搞不好会一泻千里。即使2year sharpe合格，也要看是否是其中一年的优秀表现掩盖了另一年乏力的情况。这条规则也可以反过来利用，如果一个因子近几年表现很好但前中期略有起伏，那也是可以容忍的。
2. **注意开启maxtrade后的表现。** 有些因子在开启maxtrade之前表现一路长虹，开启之后却基本是一条水平线，这种最好不要提交。我的理解是开启maxtrade可能更接近实盘表现，如果开启后仍能保持sharpe>1,fitness>0.5的话，就算不错了。
3. **注意return的隐藏底线。** 如果说margin的高低决定了策略赚钱的效率，而return的高低则决定了这个策略究竟有没有投产价值，说白了，你的return如果连这个地区的银行年化利率都比不过，那在风险更高的市场里还有什么意义呢？
4. **关于最大回撤的一点看法。** 我之前一直是秉持着最大回撤不能超过return这个观点的，但架不住有些策略就是高风险高收益的。于是我把条件放宽为最大回撤不能出现在近3年，并且除最大回撤以外，每年的小回撤也不能太高，否则仍然说明此策略的稳健性不够。
5. **精选PPA池。** PPA池combine是可以通过手动增删标签来控制的，比总池combine相对容易掌控，那自然要优中选优。首先，按RA的标准来筛自然不必多说，一月更新的os期表现也是重要依据，再就是把前4条综合起来应用，核心要义是保留有上升趋势的因子。
6. **换手率对Osmosis影响的猜想。** 每日os和os combine还是有很大区别的，我了解到有很多顾问的每日os不算差，但os combine却相差甚远，反之亦然。这一方面跟每日os是rank的有关，有时可能单纯的是在比谁亏的少；另一方面，我觉得这跟换手率多少有些关系，低换手率的因子可能会因为单日没有触发交易条件而只守着老本，而os combine的时间窗口相对较长，更能体现出因子真实的表现来。所以，如果想要每日和combine两开花，还是尽量避免给换手过低的因子赋高分吧。

最后是我做了4个月顾问之后的一点感想，做量化不能陷入“科学迷信”。所谓“科学迷信”最开始是指19世纪物理学家们认为只要知道所有粒子的初始状态，并用牛顿力学算一遍，就能精确算出未来的一切，但后来大家也都知道了，一个名为蝴蝶效应的现象打破了这个幻想。做量化时，我们也要清楚，能长期准确预测市场走向的策略是不存在的，或者说以现在的算力是做不到的，但我们至少可以避免提交即将失效的因子，让自己策略的当打之年延长一些。

祝大家在即将结算的这赛季猛猛上分，季度奖和base拿到手软！点个赞吧，感谢！！

---

### 帖子 #59: PnL = ∑(Robustness * Creativity)
- **主帖链接**: https://support.worldquantbrain.com[经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md
- **讨论数**: 28

大家新年好呀，给大家拜个晚年了🧨🧨

首先声明我不是大佬，很多东西我都是一知半解的，还在逐渐摸索，combine和vf得分也有很大的运气成分。

我是去年11月下旬转为有条件顾问的，至今经历了两次combine刷新和一次vf刷新，变动如下图所示：


> [!NOTE] [图片 OCR 识别内容]
> Value Factor 娈化趋势
> Combined 娈化趋势
> Value Factor
> Combieq4lpha
> DOwET Dool
> 0 Seleced Alpha
> 0.97
> Combin」
> 3.71
> 090
> 300
> 0.80
> 200
> 0,70
> 100
> 050
> 0.00
> 1.00
> 0.50
> 0.45
> ~1.73
> 202503
> 202509
> 202510
> 202508
> 202509
> 202510
> 302500
> 302510
> 202571
> 202500
> 202510
> 202571
> 202510
> 202511
> 202512
> 202510
> 202511
> 202512


可以看到前后仅一个月，我的combine就从-1.2拉升到了3.18，vf也涨到了0.92，对比过于强烈，完全可以说是从全错到全对的过程。因此我认为自己这个样本还是很具有研究价值的，对目前combine仍处于谷底的顾问应该也会有所启发，那么我11月和12月的提交情况是怎样的呢？又能得出什么结论呢？（省流直接跳到后面粗体看结论，右上角给点个赞吧，多谢了！）

因为平台在今年1月20更新了os期，所有此前提交的因子默认显示的都是os期数据，而我提交时自然不可能预见os表现，所以下面展示的仍然是is时期的数据。此外我提交的大部分都是atom，只有少量混pv。

先看11月份，这个月底我刚成为顾问，共提交了13个因子，数据如下（图有点宽，建议ctrl+放大看）：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 10
> 2.13
> 1.625
> 1.656
> 4.03
> 3.075
> 2.984
> 0.001243
> 0.000637
> 0.000747
> 0.1494
> 0.0736
> 0.0739
> EUR
> 01
> 1.92
> 1.9
> 1.9
> 3.01
> 2.855
> 2.855
> 0.001011
> 0.001002
> 0.001002
> 0.0765
> 0.0626
> 0.0626
> USA
> 01
> 1.58
> 1.58
> 1.58
> 2.71
> 2.71
> 2.71
> 0.000681
> 0.000681
> 0.000681
> 0.0561
> 0.0561
> 0.0561


再看12月份，这个月份共提交了61个因子，数据如下：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 对象数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 3
> 1.35
> 1.17
> 1.18
> 1.66
> 1.46
> 1.4267
> 0.007593
> 0.001492
> 0.003362
> 0.127
> 0.0825
> 0.0901
> EUR
> 18
> 3.08
> 1.26
> 1.4278
> 3.82
> 2.125
> 2.2739
> 0.002114
> 0.001282
> 0.001308
> 0.0834
> 0.0471
> 0.0515
> IND
> 器
> 21
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 19
> 3.07
> 1.59
> 1.7595
> 3.78
> 1.76
> 1.9811
> 0.007382
> 0.001876
> 0.002561
> 0.3445
> 0.11
> 0.1277


因为我最高的combine是总池，所以再补一张11、12月份汇总数据：


> [!NOTE] [图片 OCR 识别内容]
> Region
> Delay
> 提交数量
> Fitness 最高
> Fitness 中位数
> Fitness 平均
> Sharpe 最高
> Sharpe 中位数
> Sharpe 平均
> Margin 最高
> Margin 中位数
> Margin 平均
> Returns 最高
> Returns 中位数
> Returns 平均
> EUR
> D0
> 13
> 2.13
> 1.61
> 1.5462
> 4.03
> 295
> 2.6246
> 0.007593
> 0.000731
> 0.00135
> 0.1494
> 0.0799
> 0.0776
> EUR
> 20
> 3.08
> 1.275
> 1.475
> 3.82
> 2.21
> 2.332
> 0.002114
> 0.001257
> 0.001278
> 0.0834
> 00484
> 0.0526
> IND
> 器
> 3.32
> 1.77
> 1.8457
> 3.08
> 2.26
> 2.3048
> 0.002643
> 0.001136
> 0.001325
> 0.1931
> 0.1373
> 0.1359
> USA
> 20
> 3.07
> 1.585
> 1.7505
> 3.78
> 1.805
> 2.0175
> 0.007382
> 0.001698
> 0.002467
> 0.3445
> 0.1068
> 0.1241


这样一来答案是不是显而易见了？接下来开始盘点全错和全对行为。

**全错：**

1. **月底入坑，提交量少，但却刚好够出combine分（这个也确实没啥好办法，总有我这种月底转正的倒霉蛋，好在提交量少很快就能冲回来）**
2. **一上来就做d0（数据少难度高）**
3. **只看fitness和sharpe,忽略了margin（就算os维持is期的表现都是亏的，更别提os可能还要俯冲一波了）**
4. **乱开地区又没点上塔（地区表现直接崩盘）**

**全对：**

1. **稳定提交，平均每日2个因子，不多不少（对于冲gm的顾问可能少了，但都准备冲gm了也不用我多说什么了）**
2. **尽量少做甚至不做d0了**
3. **开始注意各地区最低margin，保证不低于底线**
4. **每个地区都提交了20个以上的因子，稳定了地区表现**

一个反直觉的结论，12月提交的fitness和sharpe相比于11月是有下降的（也可能是因为11月样本量少），但因为margin够高，所以对combine是积极影响。另一方面，我发现margin对每日的渗透分的影响也很大，我之前简单粗暴地按margin打分竟然也意外地吃到了几天高base，但之后也开始俯冲。。附一张渗透分趋势图：


> [!NOTE] [图片 OCR 识别内容]
> Daily Osmosis Rank 娈化趋势
> 2026-02-16
> 2026-02-27
> 切换到周维度
> Ranl
> 0.30
> 0,73
> 0.50
> 1期2026-02-25
> Dal05105I5 Rank0g2
> 0,40
> 0,20
> 0.00
> 2026
> 2026
> 2026
> 2026
> 2026
> 2026
> 7026
> 7026
> 7026
> 2026
> 7026
> 2026


除了以上结论外，有几位大佬的帖子也启发了我，非常感谢：

[[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md]([Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md)

[[L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md]([L2] 【Community Leader -因子筛选与组合】维持高combine的秘密基于近四个月提交的因子分析_37022581637527.md)

最后祝大家马年combine，vf齐飞跃,拿钱拿到手软！都看到这了，给点个赞吧！

---

### 帖子 #60: 【经验分享】关于我Combine名列前茅却只定级Expert这件事😩经验分享
- **主帖链接**: 【经验分享】关于我Combine名列前茅却只定级Expert这件事经验分享.md
- **讨论数**: 8

大家好，我是Ricardo，26年Q1结算已经有一段时间了，之前我发分享了自己维持高Combine的一点心得体会。有兴趣的朋友可以看看我之前的帖子，可以了解我是怎样在一个月之内Combine提升超4并且冲上总池Combine全球第一的。../顾问 MS51256 (Rank 28)/[Commented] [经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享.md../顾问 RM49262 (Rank 30)/[Commented] [经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享.md虽然Combine数据亮眼，但我的定级成绩却难尽人意，只堪堪定上了Expert，实在有些可惜，不过这也为我这个赛季的打法带来了一些启发，在此分享出来，如果对各位有所帮助，还请给我点个赞！先来看一下上个赛季定级时的数据，上赛季我的目标其实是master,所以点塔压力并不算大。第一个问题，可以明显看出，我的平均操作符爆炸了，因为赛季初自己对操作符数量并不重视，只盯着表现看，甚至有时明明可以顺手消除掉的操作符比如-(A-B)这类表达式，也没有改写一遍，导致赛季末想补救也来不及了，所以一定要在赛季初就引起重视。还有像signed_power这种操作符，虽然能让因子的数值更好看，但也暗中增加了过拟合风险，一定谨慎使用。顺带一提，最近平台豁免了ts_backfill和group_backfill操作符，在因子中使用这两个操作符不会计入平均操作符数量，这无疑是个好消息，构建因子时可以多多考虑这一点。第二个问题，平均字段偏高，但总字段数却没跟上，这说明我的因子有一些同质化问题。虽然有些优质字段确实更容易出信号，但过度集中在少量字段上，就相当于把鸡蛋放在一个篮子里，这在金融市场上显然不是个好事。如果在Osmosis点数的分配上也出现同质化问题，可能会导致每日Rank不稳定、上窜下跳，这也是老师们一直在强调diversity重要性的原因之一，所以一定要尽量避免过度集中。还有就是回测天数和社区分这两个场外因素，回测天数没办法提升，只能保证尽量不要因为自身原因断回测。而社区分，上赛季我因为没有及时查看邮箱，错过了加入研究小组的机会，不仅失去了额外获取社区分的途径还失去了和大佬们交流学习的机会。所以这赛季再次收到邀请后，我立刻就申请加入了，真香！各位朋友一定多多查看邮箱，如果收到邀请，绝对不要错过。值得注意的是，想要加入研究小组需要满足任意Combine>1同时平均PC<0.7,否则是无法收到邀请的。然后是关于各等级打法的一点看法，GM的点塔和Combine压力较大，六维反而不是那么的卷，建议冲GM的朋友起码维护两个Combine>2作为保险。Master的点塔和Combine较容易满足，因此是六维最卷的等级，想要冲Master六维不能有一项瘸腿，否则都会很艰难。Expert几乎不存在点塔压力，只要不乱开区域，Combine条件也是很容满足的，这个等级的门道就多了，你可以通过超低的平均操作符或者高字段数来提升排名，十分灵活。最近平台上线了Python alpha功能，当你有好的因子但操作符数量偏多时，可以尝试让AI将它转为Python alpha，这样既不会伤害六维，又能点塔，但要注意Vector类型字段现阶段还无法处理，先用Matrix试验一下吧！最后祝大家Combine与VF齐飞，Q2再上一层楼，看到这了，点个赞吧！

---

### 帖子 #61: 【经验分享】关于我Combine名列前茅却只定级Expert这件事😩经验分享
- **主帖链接**: https://support.worldquantbrain.com【经验分享】关于我Combine名列前茅却只定级Expert这件事经验分享_40962586503191.md
- **讨论数**: 8

大家好，我是Ricardo，26年Q1结算已经有一段时间了，之前我发分享了自己维持高Combine的一点心得体会。有兴趣的朋友可以看看我之前的帖子，可以了解我是怎样在 **一个月之内Combine提升超4** 并且冲上总池Combine全球第一的。

[[经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md]([经验分享]从全错到全对仅一个月实现combine -12318  vf092经验分享_38680670654999.md)

[[经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md]([经验分享]一觉醒来全球combine缩水只有我保持不变总池combine全球第一经验分享_39224484288663.md)

虽然Combine数据亮眼，但我的定级成绩却难尽人意，只堪堪定上了Expert，实在有些可惜，不过这也为我这个赛季的打法带来了一些启发，在此分享出来，如果对各位有所帮助，还请给我点个赞！


> [!NOTE] [图片 OCR 识别内容]
> Combined Alpha Performance
> 2.86
> Re?ched Imandmaster
> Combined Selected Alpha Performance
> No Tatchln?IThas TelresheJ Tonthl 
> Combined Power Pool Alpha Performance
> 1.53
> 0.47 more
> Gmandmaster
> Combined Osmosis Pertormance
> 0.8
> 02more
> Haster


先来看一下上个赛季定级时的数据，上赛季我的目标其实是master,所以点塔压力并不算大。


> [!NOTE] [图片 OCR 识别内容]
> Tie breaker criteria
> 2026 O1,Junuury Ist 2026
> UIaT 77
> Opemtors perda
> WralT IeT
> HeldsTeranha
> 5.63
> 82
> 1.64
> Flo Usrd
> LTTIIUNILICTII
> Nx SIIUIlIon sIIIk
> 153
> 39.9
> 136


第一个问题，可以明显看出，我的 **平均操作符爆炸** 了，因为赛季初自己对操作符数量并不重视，只盯着表现看，甚至有时明明可以顺手消除掉的操作符比如-(A-B)这类表达式，也没有改写一遍，导致赛季末想补救也来不及了，所以一定要 **在赛季初就引起重视** 。还有像signed_power这种操作符，虽然能让因子的数值更好看，但也暗中增加了过拟合风险，一定谨慎使用。顺带一提，最近平台豁免了ts_backfill和group_backfill操作符，在因子中使用这两个操作符不会计入平均操作符数量，这无疑是个好消息，构建因子时可以多多考虑这一点。

第二个问题，平均字段偏高，但 **总字段数却没跟上** ，这说明我的因子有一些同质化问题。虽然有些优质字段确实更容易出信号，但过度集中在少量字段上，就相当于把鸡蛋放在一个篮子里，这在金融市场上显然不是个好事。如果在Osmosis点数的分配上也出现同质化问题，可能会导致每日Rank不稳定、上窜下跳，这也是老师们一直在强调diversity重要性的原因之一，所以一定要尽量 **避免过度集中** 。

还有就是回测天数和社区分这两个场外因素，回测天数没办法提升，只能保证尽量不要因为自身原因断回测。而社区分，上赛季我因为没有及时查看邮箱，错过了 **加入研究小组** 的机会，不仅失去了额外获取社区分的途径还失去了和大佬们交流学习的机会。所以这赛季再次收到邀请后，我立刻就申请加入了，真香！各位朋友一定多多查看邮箱，如果收到邀请，绝对不要错过。值得注意的是，想要加入研究小组需要满足 **任意Combine>1同时平均PC<0.7** ,否则是无法收到邀请的。

然后是关于各等级打法的一点看法，GM的点塔和Combine压力较大，六维反而不是那么的卷，建议冲GM的朋友起码维护两个Combine>2作为保险。Master的点塔和Combine较容易满足，因此是六维最卷的等级，想要冲Master六维不能有一项瘸腿，否则都会很艰难。Expert几乎不存在点塔压力，只要不乱开区域，Combine条件也是很容满足的，这个等级的门道就多了，你可以通过超低的平均操作符或者高字段数来提升排名，十分灵活。 **最近平台上线了Python alpha功能，当你有好的因子但操作符数量偏多时，可以尝试让AI将它转为Python alpha，这样既不会伤害六维，又能点塔，但要注意Vector类型字段现阶段还无法处理，先用Matrix试验一下吧！**

最后祝大家Combine与VF齐飞，Q2再上一层楼，看到这了，点个赞吧！

---

### 帖子 #62: 揭开 Osmosis 排名的“黑箱”
- **主帖链接**: 揭开 Osmosis 排名的黑箱.md
- **讨论数**: 0

最近在深入研究 Osmosis 分配和排名的机制时，发现一个非常反直觉的现象：周一早上看到的 Daily Osmosis Rank，居然会原封不动地持续到周三，直到周四才更新。我反复研究规则、结合官方回复和一些资深玩家的提示，终于拼凑出了背后的完整逻辑。这篇帖子会把我推导出的结论和经验全部分享出来，希望能帮你更好地理解这个系统，少走弯路。一、那个让人迷惑的现象很多用过 Osmosis 的人都注意到一个事实：你周一的 Daily Osmosis Rank 是 0.9，那么周二、周三它大概率还是 0.9，纹丝不动。但周四可能会突然跳到 0.4 或 0.6。直觉上，一个叫“Daily”的指标，难道不应该每天都不一样吗？官方文档是不是写错了？答案是：文档没写错，但它的运行方式比表面文字更复杂。二、你必须知道的三个底层规则把整个逻辑理顺，需要先接受三个来自官方文档和权威解读的铁律：规则 1：分配方案有 7 天的“等待期”你在本周日（比如 2 月 1 日）晚上 23:59 EST 前锁定的 Osmosis 点数，并非下周一生效，而是下下周一（2 月 9 日）才生效。原文有明确案例：“points that lock in on 8th Feb 2026 (Sunday) will be used for the daily combo calculations starting from 16th Feb to 22nd Feb.”规则 2：计算用的 PnL 来自“两年前的样本外数据”Daily Osmosis Rank 的 PnL 不是来自当前真实市场，而是：*“one day's PNL (from 2 years ago in the out-sample period)”*规则 3：平台严格模拟 T+2 交易结算周期这是一位资深大佬推测的工程实现细节：“周三 post 策略，周四执行，周五看到 PnL，然后周末”。平台在跑 2 年前的历史数据时，模拟的是真实交易的节奏——决策、执行、结算，一个都不能少。三、完整的时空穿越推演（这才是核心）现在我们把这些规则拼接在一起，推演一套 Osmosis 方案的生命周期。假设你在 2026 年 2 月 1 日（周日）锁定了一份分配方案。第一步：现实时间等待一周你的方案在 2 月 1 日锁定，进入 7 天等待期，直到2 月 9 日（周一）才正式生效。第二步：方案被“发送”到 2 年前平台拿到你这套生效的方案，并不在当前市场运行，而是把它放到2 年前对应的那一周（即 2024 年 2 月 11 日那一周）进行模拟。第三步：在 2 年前的平行世界里，严格遵循 T+2 规则到了那个 2 年前的模拟周，系统会这样操作：周三：把你的方案当成你在这一天刚刚做出的投资决策（Post）；周四：按照决策执行交易；周五：收盘后结算，生成这一周唯一一个单日 PnL。然后周末休市。第四步：现实世界的你看到了什么？现实时间周一（2 月 9 日）：你的方案今天生效，系统去 2 年前的平行世界里找数据。但此时 2 年前那一周的周三还没到，新的决策还没 Post，所以没有任何当周的新 PnL。系统只能把最近一个已结算的 PnL——也就是2 年前上周五（2024 年 2 月 7 日）的结算结果——拿出来排名，这就是你周一看到的那个数字。现实时间周二、周三：情况一模一样。2 年前当周的周三还没到（或刚到周三还没结算），最新的 PnL 仍然是那个“上周五”的。所以系统重复展示同一个排名，你的 Daily Osmosis Rank 就这样三天完全不变。现实时间周四：在 2 年前的平行世界里，时间终于推进到了当周的周五，新的结算完成了！系统瞬间捕获到这个最新的单日 PnL，重新计算排名，于是你的 Rank 终于动了。所以真相是：你周一至周三看到的，本质上是用你上上周日分配方案，去跑 2 年前“上周五”的单日数据所得到的排名；而周四看到的，是同一套方案跑 2 年前“本周五”的数据。这也完美解释了为什么分数会连挂三天——因为那三天系统都在展示同一个已完成结算的历史结果。四、这对我配置 Osmosis 有什么实际启示？1. 不要根据单日 Rank 的波动频繁调仓你现在知道，周一至周三的数值其实是同一个样本点，根本不是连续三天的独立评价。如果因为周一 0.9、周四掉到 0.4 就急着大改方案，很可能是在对一个已经被 7 天锁定期和 2 年历史映射反复平滑过的信号过度反应。2. Combined Osmosis Performance 才是真正可靠的长跑成绩Daily Osmosis Rank 是单日模拟的排名，而且存在我们发现的这种“结算错位”效应，它更容易受到个别历史行情的偶然影响。而 Combined Osmosis Performance 是把你整个季度内所有真实的日度 After-cost PnL（每一个交易日都有一个独立数值，不受展示逻辑干扰）拼接起来，计算出的年化夏普比率。它不受“三天重复显示”这种前端逻辑的影响，衡量的是你组合在足够多样本下，持续产生稳定正收益的能力。3. 牢记官方的黄金法则所有机制的背后，Osmosis 真正奖励的是：“Aim for steady positive returns with reasonable risk.”大起大落的收益，哪怕周总收益更高，也会因为巨大的标准差严重拉低夏普比率。你需要追求的，是分散在不同 scope、不同数据集、不同换手率上的一组 Alpha，每天稳定地积累小额收益，而不是指望某一天的暴利。五、写在最后这些结论是我结合官方指南、平台实际行为、官方人员回复以及资深玩家提示，一步步交叉验证出来的。它或许不能让你一夜暴富，但能让你不再被那个“三天不变的 Daily Rank”弄得心神不宁，并且把精力真正放在提高 Combined Osmosis Performance 这件正确的事上。如果你有自己的观察或不同的理解，欢迎在评论区一起讨论。愿我们都能成为那种“每日常胜”的顾问，而不是偶尔惊鸿一瞥的赌徒。

---

### 帖子 #63: 揭开 Osmosis 排名的“黑箱”
- **主帖链接**: https://support.worldquantbrain.com揭开 Osmosis 排名的黑箱_41288728107287.md
- **讨论数**: 0

最近在深入研究 Osmosis 分配和排名的机制时，发现一个非常反直觉的现象： **周一早上看到的 Daily Osmosis Rank，居然会原封不动地持续到周三，直到周四才更新。**  我反复研究规则、结合官方回复和一些资深玩家的提示，终于拼凑出了背后的完整逻辑。这篇帖子会把我推导出的结论和经验全部分享出来，希望能帮你更好地理解这个系统，少走弯路。

### 一、那个让人迷惑的现象

很多用过 Osmosis 的人都注意到一个事实： **你周一的 Daily Osmosis Rank 是 0.9，那么周二、周三它大概率还是 0.9，纹丝不动。**  但周四可能会突然跳到 0.4 或 0.6。

直觉上，一个叫“Daily”的指标，难道不应该每天都不一样吗？官方文档是不是写错了？

答案是： **文档没写错，但它的运行方式比表面文字更复杂。**

### 二、你必须知道的三个底层规则

把整个逻辑理顺，需要先接受三个来自官方文档和权威解读的铁律：

**规则 1：分配方案有 7 天的“等待期”** 
你在本周日（比如 2 月 1 日）晚上 23:59 EST 前锁定的 Osmosis 点数， **并非下周一生效，而是下下周一（2 月 9 日）才生效** 。原文有明确案例：

> *“points that lock in on 8th Feb 2026 (Sunday) will be used for the daily combo calculations starting from 16th Feb to 22nd Feb.”*

**规则 2：计算用的 PnL 来自“两年前的样本外数据”** 
Daily Osmosis Rank 的 PnL 不是来自当前真实市场，而是：

> *“one day's PNL (from 2 years ago in the out-sample period)”*

**规则 3：平台严格模拟 T+2 交易结算周期** 
这是一位资深大佬推测的工程实现细节： **“周三 post 策略，周四执行，周五看到 PnL，然后周末”** 。平台在跑 2 年前的历史数据时，模拟的是真实交易的节奏——决策、执行、结算，一个都不能少。

### 三、完整的时空穿越推演（这才是核心）

现在我们把这些规则拼接在一起，推演一套 Osmosis 方案的生命周期。

**假设你在 2026 年 2 月 1 日（周日）锁定了一份分配方案。**

**第一步：现实时间等待一周** 
你的方案在 2 月 1 日锁定，进入 7 天等待期，直到  **2 月 9 日（周一）**  才正式生效。

**第二步：方案被“发送”到 2 年前** 
平台拿到你这套生效的方案，并不在当前市场运行，而是把它放到  **2 年前对应的那一周** （即 2024 年 2 月 11 日那一周）进行模拟。

**第三步：在 2 年前的平行世界里，严格遵循 T+2 规则** 
到了那个 2 年前的模拟周，系统会这样操作：

- **周三** ：把你的方案当成你在这一天刚刚做出的投资决策（Post）；
- **周四** ：按照决策执行交易；
- **周五** ：收盘后结算，生成 **这一周唯一一个单日 PnL** 。
  然后周末休市。

**第四步：现实世界的你看到了什么？**

- **现实时间周一（2 月 9 日）** ：你的方案今天生效，系统去 2 年前的平行世界里找数据。但此时 2 年前那一周的周三还没到，新的决策还没 Post，所以 **没有任何当周的新 PnL** 。系统只能把最近一个已结算的 PnL——也就是  **2 年前上周五（2024 年 2 月 7 日）的结算结果** ——拿出来排名，这就是你周一看到的那个数字。
- **现实时间周二、周三** ：情况一模一样。2 年前当周的周三还没到（或刚到周三还没结算），最新的 PnL 仍然是那个“上周五”的。所以系统重复展示同一个排名，你的 Daily Osmosis Rank 就这样 **三天完全不变** 。
- **现实时间周四** ：在 2 年前的平行世界里，时间终于推进到了当周的周五，新的结算完成了！系统瞬间捕获到这个最新的单日 PnL，重新计算排名，于是你的 Rank 终于动了。

**所以真相是：你周一至周三看到的，本质上是用你上上周日分配方案，去跑 2 年前“上周五”的单日数据所得到的排名；而周四看到的，是同一套方案跑 2 年前“本周五”的数据。**

这也完美解释了为什么分数会连挂三天——因为那三天系统都在展示同一个已完成结算的历史结果。

### 四、这对我配置 Osmosis 有什么实际启示？

**1. 不要根据单日 Rank 的波动频繁调仓** 
你现在知道，周一至周三的数值其实是同一个样本点，根本不是连续三天的独立评价。如果因为周一 0.9、周四掉到 0.4 就急着大改方案，很可能是在对一个已经被 7 天锁定期和 2 年历史映射反复平滑过的信号过度反应。

**2. Combined Osmosis Performance 才是真正可靠的长跑成绩** 
Daily Osmosis Rank 是单日模拟的排名，而且存在我们发现的这种“结算错位”效应，它更容易受到个别历史行情的偶然影响。而 Combined Osmosis Performance 是把你整个季度内所有 **真实的日度 After-cost PnL** （每一个交易日都有一个独立数值，不受展示逻辑干扰）拼接起来，计算出的年化夏普比率。它不受“三天重复显示”这种前端逻辑的影响，衡量的是你组合在足够多样本下，持续产生 **稳定正收益** 的能力。

**3. 牢记官方的黄金法则** 
所有机制的背后，Osmosis 真正奖励的是：

> *“Aim for steady positive returns with reasonable risk.”*

大起大落的收益，哪怕周总收益更高，也会因为巨大的标准差严重拉低夏普比率。你需要追求的，是分散在不同 scope、不同数据集、不同换手率上的一组 Alpha，每天稳定地积累小额收益，而不是指望某一天的暴利。

### 五、写在最后

这些结论是我结合官方指南、平台实际行为、官方人员回复以及资深玩家提示，一步步交叉验证出来的。它或许不能让你一夜暴富，但能让你不再被那个“三天不变的 Daily Rank”弄得心神不宁，并且把精力真正放在提高 Combined Osmosis Performance 这件正确的事上。

如果你有自己的观察或不同的理解，欢迎在评论区一起讨论。愿我们都能成为那种“每日常胜”的顾问，而不是偶尔惊鸿一瞥的赌徒。

---

### 帖子 #64: 解锁Python Alpha新维度
- **主帖链接**: 解锁Python Alpha新维度.md
- **讨论数**: 0

最近深度体验了平台的Python Alpha新特性，不得不说，从现成的FastExpr转向完全开放的Python生态，这种风险与基于并存的感觉让人兴奋。我们可以直接用numpy做复杂的滚动矩阵运算，用scipy进行高级统计分析，甚至引入自定义的机器学习推理逻辑——以前需要用多个算子拼凑的复杂信号，现在几行Python代码就能搞定。不过，自由度越高，底层的“规矩”和“陷阱”也越多。基于官方文档的深度解读和我的实际踩坑经历，今天这篇帖子不聊复杂的策略逻辑，专门梳理Python Alpha开发的硬核机制与避坑指南，希望对初上手的同学有所帮助。一、 深刻理解@alpha装饰器与数据视图在FASTExpr中我们不需要关心数据流，但在Python Alpha中，理解@alpha装饰器是第一步。1. 数据是“只读”且“带窗口”的传入data对象的数组（如data.returns），绝对不要尝试原地修改（data.returns[-1][0] = 0）。引擎底层为了性能，将数据标记为了只读，强行修改会直接抛出ValueError。正确的做法是today = data.returns[-1].copy()。另外，lookback参数决定了data.returns的形状。如果lookback=5，那这个数组就是[6, N]（包含今天及前5天）。要特别留意模拟初期窗口“生长”的阶段，不要硬编码去索引data.returns[-6]，否则模拟初期会因为维度不足报错。2. 永远不要忘记universe字段data.universe是引擎自动注入的，不需要也不允许在@alpha(data=[])中声明它。它是一个int类型的掩码矩阵（1代表在股票池内，0代表不在）。记得用data.universe[-1].astype(bool)来对最终信号进行“巴氏消毒（Pasteurization）”，过滤掉池外的杂音。二、 状态管理（Store）的灵魂用法：优雅处理动态股票池这是Python Alpha相比FASTExpr最大的优势之一——可以维护长期状态。但如果不注意，这也是最大的“深坑”。坑点：使用无类型（Untyped）的store列表（如store=["my_cache"]）时，如果股票池（Universe）发生变化（例如退市或新增），你的缓存数组形状会与新的data形状不匹配，模拟到一半会直接崩溃。传统做法需要手动写_pad_store函数去补全维度，非常繁琐。破解之道：使用类型化（Typed）Store强烈推荐大家使用文档中提到的类型化存储字典！python@alpha(data=["returns"],store=[# dims="i" 表示按股票维度自动扩展{"name":"running_mean","dims":"i","extend":np.float64(0.0)},# dims="xi" 表示一个自由维度(时间) + 股票维度，新增股票时自动补NaN{"name":"rank_cache","dims":"xi","extend":np.float64(np.nan)}])defmy_alpha(data,store):...一旦定义了dims和extend，当Universe新增股票时，引擎会自动在数组的最后一维（即i轴）补上我们指定的值（0或NaN）。这完美解决了动态股票池的适配问题，强烈建议大家抛弃手动_pad_store的写法。特别提醒：extend值必须是严格的numpy标量类型！写0或np.nan都会因类型不匹配报错，务必显式写成np.float64(0.0)或np.float32(np.nan)。三、 精度与类型的“浮点执念”在FASTExpr中我们从不关心精度，但在Python Alpha中，float32是铁律。文档明确指出，如果返回的向量不是float32，模拟会直接报错。然而numpy的许多高级函数（如np.nanmean、np.nanstd，甚至简单的0.9 * arr）都会悄然将float32提升为float64。极简解决方案：在所有逻辑计算完毕后，务必加上.astype(np.float32)再返回。养成习惯，把这个当作return语句的“标配”。四、 不得不防的“除权日陷阱”这一点大家在做价量因子时务必留心。文档特别提到，close、open、eps等每股（Per-Share）数据是包含分红、拆合股断层的。如果你直接用原始价格计算涨跌幅，在拆合股当天会产生一个虚假的“跳空缺口”，导致Alpha发出虚假的买卖信号。虽然returns字段已经自动复权，但如果你需要用到绝对价格（例如布林带、ATR），必须使用adjfactor进行手动复权修正。python# 标准复权公式 (来自官方文档)adjusted_close=close/((adjfactor-1.0).cumsum()+1.0)这条公式建议直接封装成工具函数，供所有涉及绝对价格的Alpha调用。五、 两大模拟路径：先“本地快跑”，再“远程终验”BRAIN提供的这套双轨制模拟流程确实很贴心，我们可以按需使用：BrainLabs 本地模拟（Path 1）：三段式流水线（generate_alpha_matrix->generate_alpha_positions->generate_alpha_stats）。数据在本机缓存，跑得飞快，极其适合写代码时的Debug、单元测试和参数初筛。实际远程模拟（Path 2）：直接调用brain.simulate。它会将代码发送至云端服务器，应用完整的decay、neutralization等底层逻辑，结果最准确，但速度稍慢。建议工作流：在本地跑通逻辑（看曲线形状），再提交远程跑最终指标。致命注意（血泪教训）：当使用brain.simulate提交远程任务时，包含@alpha装饰器的代码单元格中，绝对不要导入from brain import Brain或from brain.models import SimulationSettings！引擎只允许导入from brain.alphas import alpha。如果混入其他brain模块，远程模拟会直接失败（Fail）。正确的做法是把Brain和Settings的导入放在提交代码之前的另一个单元格中。六、 总结与展望从FASTExpr的“搭积木”到Python的“自由编程”，我们需要习惯用软件工程的严谨性来写量化因子。尤其是类型管理（float32）、数据复制（Copy）和动态维度（Store dims），这三个点如果能完全避开，Python Alpha的开发效率将直线起飞。用Python写Alpha最大的魅力在于，现在我们可以把最前沿的统计模型和复杂逻辑无缝嵌入到BRAIN的强大回测框架中，不再受限于有限的算子库。希望这篇基于实战解读的帖子能给大家带来一些启发。如果大家在实际迁移中遇到奇怪的报错，欢迎在楼下留言一起探讨，大概率都是上述几个“坑”引起的问题。

---

### 帖子 #65: 标准复权公式 (来自官方文档)
- **主帖链接**: https://support.worldquantbrain.com解锁Python Alpha新维度_41290232975895.md
- **讨论数**: 0

最近深度体验了平台的Python Alpha新特性，不得不说，从现成的FastExpr转向完全开放的Python生态，这种风险与基于并存的感觉让人兴奋。我们可以直接用 `numpy` 做复杂的滚动矩阵运算，用 `scipy` 进行高级统计分析，甚至引入自定义的机器学习推理逻辑——以前需要用多个算子拼凑的复杂信号，现在几行Python代码就能搞定。

不过，自由度越高，底层的“规矩”和“陷阱”也越多。基于官方文档的深度解读和我的实际踩坑经历，今天这篇帖子不聊复杂的策略逻辑，专门梳理 **Python Alpha开发的硬核机制与避坑指南** ，希望对初上手的同学有所帮助。

### 一、 深刻理解  `@alpha`  装饰器与数据视图

在FASTExpr中我们不需要关心数据流，但在Python Alpha中，理解 `@alpha` 装饰器是第一步。

**1. 数据是“只读”且“带窗口”的** 
传入 `data` 对象的数组（如 `data.returns` ）， **绝对不要尝试原地修改** （ `data.returns[-1][0] = 0` ）。引擎底层为了性能，将数据标记为了只读，强行修改会直接抛出 `ValueError` 。正确的做法是 `today = data.returns[-1].copy()` 。

另外， `lookback` 参数决定了 `data.returns` 的形状。如果 `lookback=5` ，那这个数组就是 `[6, N]` （包含今天及前5天）。要特别留意模拟初期窗口“生长”的阶段，不要硬编码去索引 `data.returns[-6]` ，否则模拟初期会因为维度不足报错。

**2. 永远不要忘记  `universe`  字段** 
 `data.universe` 是引擎自动注入的， **不需要也不允许** 在 `@alpha(data=[])` 中声明它。它是一个 `int` 类型的掩码矩阵（1代表在股票池内，0代表不在）。记得用 `data.universe[-1].astype(bool)` 来对最终信号进行“巴氏消毒（Pasteurization）”，过滤掉池外的杂音。

### 二、 状态管理（Store）的灵魂用法：优雅处理动态股票池

这是Python Alpha相比FASTExpr最大的优势之一——可以维护长期状态。但如果不注意，这也是最大的“深坑”。

**坑点** ：使用无类型（Untyped）的 `store` 列表（如 `store=["my_cache"]` ）时，如果股票池（Universe）发生变化（例如退市或新增），你的缓存数组形状会与新的 `data` 形状不匹配，模拟到一半会直接崩溃。传统做法需要手动写 `_pad_store` 函数去补全维度，非常繁琐。

**破解之道：使用类型化（Typed）Store** 
强烈推荐大家使用文档中提到的类型化存储字典！

python

```
@alpha(
    data=["returns"],
    store=[
        # dims="i" 表示按股票维度自动扩展
        {"name": "running_mean", "dims": "i", "extend": np.float64(0.0)},
        # dims="xi" 表示一个自由维度(时间) + 股票维度，新增股票时自动补NaN
        {"name": "rank_cache", "dims": "xi", "extend": np.float64(np.nan)}
    ]
)
def my_alpha(data, store):
    ...
```

一旦定义了 `dims` 和 `extend` ，当Universe新增股票时，引擎会自动在数组的最后一维（即 `i` 轴）补上我们指定的值（0或NaN）。这完美解决了动态股票池的适配问题，强烈建议大家抛弃手动 `_pad_store` 的写法。

**特别提醒** ： `extend` 值必须是严格的 `numpy` 标量类型！写 `0` 或 `np.nan` 都会因类型不匹配报错，务必显式写成 `np.float64(0.0)` 或 `np.float32(np.nan)` 。

### 三、 精度与类型的“浮点执念”

在FASTExpr中我们从不关心精度，但在Python Alpha中， `float32` 是铁律。

文档明确指出，如果返回的向量不是 `float32` ，模拟会直接报错。然而 `numpy` 的许多高级函数（如 `np.nanmean` 、 `np.nanstd` ，甚至简单的 `0.9 * arr` ）都会 **悄然将 `float32` 提升为 `float64`** 。

**极简解决方案** ：在所有逻辑计算完毕后，务必加上 `.astype(np.float32)` 再返回。养成习惯，把这个当作 `return` 语句的“标配”。

### 四、 不得不防的“除权日陷阱”

这一点大家在做价量因子时务必留心。文档特别提到， `close` 、 `open` 、 `eps` 等 **每股（Per-Share）数据** 是包含分红、拆合股断层的。

如果你直接用原始价格计算涨跌幅，在拆合股当天会产生一个虚假的“跳空缺口”，导致Alpha发出虚假的买卖信号。虽然 `returns` 字段已经自动复权，但如果你需要用到绝对价格（例如布林带、ATR）， **必须使用 `adjfactor` 进行手动复权修正** 。

python

```
# 标准复权公式 (来自官方文档)
adjusted_close = close / ((adjfactor - 1.0).cumsum() + 1.0)
```

这条公式建议直接封装成工具函数，供所有涉及绝对价格的Alpha调用。

### 五、 两大模拟路径：先“本地快跑”，再“远程终验”

BRAIN提供的这套双轨制模拟流程确实很贴心，我们可以按需使用：

1. **BrainLabs 本地模拟（Path 1）** ：三段式流水线（ `generate_alpha_matrix`  ->  `generate_alpha_positions`  ->  `generate_alpha_stats` ）。数据在本机缓存，跑得飞快，极其适合写代码时的Debug、单元测试和参数初筛。
2. **实际远程模拟（Path 2）** ：直接调用 `brain.simulate` 。它会将代码发送至云端服务器，应用完整的 `decay` 、 `neutralization` 等底层逻辑，结果最准确，但速度稍慢。 **建议工作流** ：在本地跑通逻辑（看曲线形状），再提交远程跑最终指标。

**致命注意（血泪教训）** ：当使用 `brain.simulate` 提交远程任务时， **包含 `@alpha` 装饰器的代码单元格中，绝对不要导入 `from brain import Brain` 或 `from brain.models import SimulationSettings` ！**  引擎只允许导入 `from brain.alphas import alpha` 。如果混入其他 `brain` 模块，远程模拟会直接失败（Fail）。正确的做法是把 `Brain` 和 `Settings` 的导入放在 **提交代码之前的另一个单元格** 中。

### 六、 总结与展望

从FASTExpr的“搭积木”到Python的“自由编程”，我们需要习惯用软件工程的严谨性来写量化因子。尤其是 **类型管理（float32）** 、 **数据复制（Copy）** 和 **动态维度（Store dims）** ，这三个点如果能完全避开，Python Alpha的开发效率将直线起飞。

用Python写Alpha最大的魅力在于，现在我们可以把最前沿的统计模型和复杂逻辑无缝嵌入到BRAIN的强大回测框架中，不再受限于有限的算子库。

希望这篇基于实战解读的帖子能给大家带来一些启发。如果大家在实际迁移中遇到奇怪的报错，欢迎在楼下留言一起探讨，大概率都是上述几个“坑”引起的问题。

---


## 二、顾问技术探讨与回帖精华 (Technical Comments & Advice)

### 探讨 #1: 关于《04.【永久置顶】高Value Factor顾问分享合集，赚钱必读！(更新1029）置顶的经验分享》的评论回复
- **帖子链接**: [Commented] 04【永久置顶】高Value Factor顾问分享合集赚钱必读更新1029置顶的经验分享.md
- **评论时间**: 5个月前

前两天收到VF更新的消息，这次更新的是9、10、11三个月份的，但我还是0.5没有变，估计是成为顾问的时间太短，11月提交的太少了。VF没更新也说不上是好消息还是坏消息，毕竟11月份我刚成为顾问提交的因子质量并不好，还是看看下次更新10、11、12这三个月份的窗口期VF表现怎么样吧。

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves. =============================================================================

---

### 探讨 #2: 关于《04.【永久置顶】高Value Factor顾问分享合集，赚钱必读！(更新1029）置顶的经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 04【永久置顶】高Value Factor顾问分享合集赚钱必读更新1029置顶的经验分享_32032776365079.md
- **评论时间**: 5个月前

前两天收到VF更新的消息，这次更新的是9、10、11三个月份的，但我还是0.5没有变，估计是成为顾问的时间太短，11月提交的太少了。VF没更新也说不上是好消息还是坏消息，毕竟11月份我刚成为顾问提交的因子质量并不好，还是看看下次更新10、11、12这三个月份的窗口期VF表现怎么样吧。

=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves. =============================================================================

---

### 探讨 #3: 关于《05.【AI精选合集】创建一个具有BRAIN全部知识+金融博士+计算机博士的免费助手置顶的》的评论回复
- **帖子链接**: [Commented] 05【AI精选合集】创建一个具有BRAIN全部知识金融博士计算机博士的免费助手置顶的.md
- **评论时间**: 6个月前

收到会议邮件了，来学习一下

---

### 探讨 #4: 关于《05.【AI精选合集】创建一个具有BRAIN全部知识+金融博士+计算机博士的免费助手置顶的》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 05【AI精选合集】创建一个具有BRAIN全部知识金融博士计算机博士的免费助手置顶的_35954766785175.md
- **评论时间**: 6个月前

收到会议邮件了，来学习一下

---

### 探讨 #5: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 16815刀季度奖经验分享-小虎经验分享.md
- **评论时间**: 3个月前

=====================================================================================

大佬太厉害了，原来季度奖真能到这么高的上限啊，我记得wf是成为顾问半年后才有可能会有，是这样吗？

=====================================================================================

---

### 探讨 #6: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 16815刀季度奖经验分享-小虎经验分享_38980270292631.md
- **评论时间**: 3个月前

=====================================================================================

大佬太厉害了，原来季度奖真能到这么高的上限啊，我记得wf是成为顾问半年后才有可能会有，是这样吗？

=====================================================================================

---

### 探讨 #7: 关于《Sentiment1 数据集完全指南：Research Sentiment Data》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] Sentiment1 数据集完全指南Research Sentiment Data_41199750160663.md
- **评论时间**: 8天前

完整研读这份 Sentiment1 数据集指南后收获了体系化的情绪因子研发逻辑，以往输出情绪类 Alpha 时我只会零散调用单一分析师预期字段，缺少对整套数据集字段分层、数据特性与适配场景的完整认知。文章清晰划分情绪综合评分、分析师共识、盈利信号三大字段类别，明确各指标覆盖度、更新频率与信号属性，同时标注平台隐藏字段的查看方式，补齐了我对数据集底层结构的认知盲区。文中配套的三类标准策略表达式、多信号加权组合示例，搭配延迟平滑、分析师覆盖过滤、分场景字段选型等实操规范，解决了我此前高频情绪信号高波动、小样本分析师推荐失真、回测周期适配混乱的问题。另外指南区分 Sentiment1 与 model77 数据集定位、梳理多数据源融合思路，也让我能够根据研究员的策略周期需求，针对性输出低冗余、逻辑完整的情绪类因子方案，减少无效表达式生成，帮助研究员规范情绪 Alpha 的筛选、回测全流程，提升信号稳健性与算力利用效率。

---

### 探讨 #8: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] USA analyst一些具有经济学意义的重组数据字段.md
- **评论时间**: 3个月前

=====================================================================================

哇，直接上干货啊，太真性情了大佬，我也去试试看，感谢！

=====================================================================================

---

### 探讨 #9: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] USA analyst一些具有经济学意义的重组数据字段_38927191768343.md
- **评论时间**: 3个月前

=====================================================================================

哇，直接上干货啊，太真性情了大佬，我也去试试看，感谢！

=====================================================================================

---

### 探讨 #10: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] VF098Expert直升Grandmaster我是怎么做的.md
- **评论时间**: 5个月前

=====================================================================================

恭喜大佬，感叹一下大佬的双per控得太好了。另外问一下，想要达到某个等级，点塔数，提交数和combine是不是只要求达标？而六维是Rank的，越高越好对吗？

=====================================================================================

---

### 探讨 #11: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] VF098Expert直升Grandmaster我是怎么做的_37555582592023.md
- **评论时间**: 5个月前

=====================================================================================

恭喜大佬，感叹一下大佬的双per控得太好了。另外问一下，想要达到某个等级，点塔数，提交数和combine是不是只要求达标？而六维是Rank的，越高越好对吗？

=====================================================================================

---

### 探讨 #12: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【Community Leader -因子筛选与组合】判断因子是否可以提交稳住你的combine经验分享_36682204275863.md
- **评论时间**: 6个月前

> 1、margin不符合地区的最低要求，不提交

大佬，这里说的margin最低要求是从哪看的？

---

### 探讨 #13: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【VF074 BASE居然也能40刀】每日base方向帖经验分享.md
- **评论时间**: 3个月前

=====================================================================================

太强了，请问pc大概在什么区间呢？感觉低pc对base加成也挺大的。

=====================================================================================

---

### 探讨 #14: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【VF074 BASE居然也能40刀】每日base方向帖经验分享_38953629858327.md
- **评论时间**: 3个月前

=====================================================================================

太强了，请问pc大概在什么区间呢？感觉低pc对base加成也挺大的。

=====================================================================================

---

### 探讨 #15: 关于《【效率王】七十二变！AI助力一个Alpha变成更多个Alpha!Alpha Template》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变AI助力一个Alpha变成更多个AlphaAlpha Template_36671111976983.md
- **评论时间**: 6 months ago

大佬，72变跑完输出的那个json文件怎样用呀？我放到simulator_hk里读，结果报错

---

### 探讨 #16: 关于《【效率王】七十二变的大升级_跨区点塔？指定Category?完全不是问题！》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【效率王】七十二变的大升级_跨区点塔指定Category完全不是问题_36974265471511.md
- **评论时间**: 6个月前

感觉72变还是纵向点塔比较强，横向效果没有那么好

---

### 探讨 #17: 关于《【新人科普，老人必读】从Combined Alpha Performance 的计算原理，学习如何提升表现！置顶的》的评论回复
- **帖子链接**: [Commented] 【新人科普老人必读】从Combined Alpha Performance 的计算原理学习如何提升表现置顶的.md
- **评论时间**: 5个月前

昨天IS期似乎更新了，之前模拟出来的因子全都因为这次更新失效了，需要重新模拟才能看到pnl。因为11月的combine雪崩，我去看了下这个月的因子新更新的OS表现，发现pnl曲线还凑合，没有一到OS期就迅速下降的，这说明我combine的崩盘原因基本可以确定是过低的margin了，刚成为顾问时只看fitness和sharpe，导致提交的因子有些margin只有4、5，这进实盘操作的话妥妥的连手续费都盖不住，这下算是吃到教训了。

==================================================================================
Hard work pays off.
==================================================================================

---

### 探讨 #18: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

今天安装了mcp，并且尝试用72变生成因子，但效果不是很好，我用的是kimi的api，生成的表达式大部分都有错误，不知道是不是模型的问题。继续在论坛学习一下吧，大模型+mcp确实是大势所趋，平台即将限制回测数量，需要提交因子产出比，有ai指明方向比自己摸索效率高太多了，加油！

---

### 探讨 #19: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

12.7，今天继续点USA和EUR的塔，在提交的时候纠结了一下，是提交表现更好但pc高的，还是表现一般但pc低的？最后想起前两天会议时老师说的话，觉得应该是表现优先，为了降pc提交表现欠佳的策略委实是本末倒置，今后也会继续遵循这一原则不断提升自己。

---

### 探讨 #20: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

2025.12.8，今天点亮了EUR/D1/IMBALANCE 的塔，我发现有些数据集在某些时间窗口的数据是缺失的，这导致pnl曲线不完整，不知道这会不会对6维产生影响，但为了点塔也没办法，不知道这种情况正不正常，等到有机会向老师请教一下。今天开始限制回测数了，这对挖掘因子压力还挺大的，只能提前准备下一天提交的因子了，加油吧。

---

### 探讨 #21: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

2025.12.9，今天提交了USA的一个因子，表现还不错，以这段时间提交因子的经验来看，Fitness仍然是第一重要，然后是Sharpe，再就是Margin和Return，回撤只要别太高基本上问题不大。前期因为不知道PnL是before cost的，导致提交了很多低Margin的因子，现在要慢慢往回补了。今天晚上有视频会议，老师应该会继续讲MCP相关的内容，好好把握机会学习一下。

---

### 探讨 #22: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

2025.12.10,今天交了两个质量一般的，感觉限制回测对点塔影响很大，本来就不知道这个数据集能否出货，结果现在没有试错机会，回测数一旦用完想测也测不了了，只能赶紧优化工作流用ai代替了。

---

### 探讨 #23: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【日常生活贴】我的量化日记第七季.md
- **评论时间**: 6个月前

2025.12.11.今天交了一个USA fnd一个USA anl，质量还不错，本来有几个因子看着不错想手搓，结果回测数上限了很尴尬，还是要早点利用AI才能事半功倍啊。

---

### 探讨 #24: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

今天安装了mcp，并且尝试用72变生成因子，但效果不是很好，我用的是kimi的api，生成的表达式大部分都有错误，不知道是不是模型的问题。继续在论坛学习一下吧，大模型+mcp确实是大势所趋，平台即将限制回测数量，需要提交因子产出比，有ai指明方向比自己摸索效率高太多了，加油！

---

### 探讨 #25: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

12.7，今天继续点USA和EUR的塔，在提交的时候纠结了一下，是提交表现更好但pc高的，还是表现一般但pc低的？最后想起前两天会议时老师说的话，觉得应该是表现优先，为了降pc提交表现欠佳的策略委实是本末倒置，今后也会继续遵循这一原则不断提升自己。

---

### 探讨 #26: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.8，今天点亮了EUR/D1/IMBALANCE 的塔，我发现有些数据集在某些时间窗口的数据是缺失的，这导致pnl曲线不完整，不知道这会不会对6维产生影响，但为了点塔也没办法，不知道这种情况正不正常，等到有机会向老师请教一下。今天开始限制回测数了，这对挖掘因子压力还挺大的，只能提前准备下一天提交的因子了，加油吧。

---

### 探讨 #27: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.9，今天提交了USA的一个因子，表现还不错，以这段时间提交因子的经验来看，Fitness仍然是第一重要，然后是Sharpe，再就是Margin和Return，回撤只要别太高基本上问题不大。前期因为不知道PnL是before cost的，导致提交了很多低Margin的因子，现在要慢慢往回补了。今天晚上有视频会议，老师应该会继续讲MCP相关的内容，好好把握机会学习一下。

---

### 探讨 #28: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.10,今天交了两个质量一般的，感觉限制回测对点塔影响很大，本来就不知道这个数据集能否出货，结果现在没有试错机会，回测数一旦用完想测也测不了了，只能赶紧优化工作流用ai代替了。

---

### 探讨 #29: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.11.今天交了一个USA fnd一个USA anl，质量还不错，本来有几个因子看着不错想手搓，结果回测数上限了很尴尬，还是要早点利用AI才能事半功倍啊。

---

### 探讨 #30: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.12，今天正式开荒IND，收成还不错，另外也学会了华子哥插件的另一个功能，感谢大佬！IND的因子普遍pc都偏高，可能是因为有活动的原因吧，明天回归EUR，同时也点IND的塔，加油！

---

### 探讨 #31: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第七季_36814196359191.md
- **评论时间**: 6个月前

2025.12.13，今天印度也点了两个塔，不过因为混pv没有2倍的乘数，感觉混pv虽然容易出货但容易涨字段数，非点塔的情况还是要谨慎使用。新的比赛开启了，虽然我参加了，但现在还不大清除规则，只知道要自己给因子赋分，之后好像有视频会议要单独讲这一点，可以从了解一下。

---

### 探讨 #32: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

IND的PPA活动关了，现在想交PPA只能去GLB了，但只有两个星期估计也挖不出多少因子，从点塔方面考量还是不开这个坑了。上赛季结算的combine血崩，vf无变化，在提交策略这方面还需要改进，毕竟方向错了，走得越多只会离目标越来越远。

==================================================================================
Hard work pays off.
==================================================================================

---

### 探讨 #33: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

=====================================================================================

2026.1.21，今天尝试使用iflow优化因子，最终指标确实达到了，但pc超了。感觉ai还是不能完全听从指挥，当他面临难题的时候还是会掩耳盗铃，不知道是不是提示词的原因。目前在我这里，ai只能作为优化的辅助工具，还没有真正成为生产力工具，还需要继续学习。

=====================================================================================

---

### 探讨 #34: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第九季_37796479641111.md
- **评论时间**: 5个月前

=====================================================================================

2026.1.22，今天更新了一下cnhkmcp,把新增的skills加在iflow上了。大概看了一下，大概包括因子优化，数据集和字段分析，测试和工具等几种分类的skills，接下来优化因子时，ai应该能更规范了。不得不说开发chhkmcp的大佬真是太厉害了，在他带领下真了解了不少有用的ai相关知识，赞美大佬。

=====================================================================================

---

### 探讨 #35: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025.12.21，今天挖出了一个EUR fnd的因子，开了max trader拿了双倍，这个因子是ai生成后手动优化得到的，双per和pc都很低，果然ai比人工发掘的能力强很多，尤其是在冷门操作符和字段上的组合，比同质化的模板好太多了。

---

### 探讨 #36: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第八季_37179224417303.md
- **评论时间**: 6个月前

2025.12.23，今天提交了4个IND地区的因子，前两天工作上有事没有太多时间筛选因子，所以都只交了1个。因为这月末会更新vf,所以得赶紧把每个region的因子数量都交到20个以上，今天手动把一个因子的回撤和换手率拉低了，而且sharpe和fit没有明显下降，还是很有成就感的，继续学习更多的操作符，希望以后看到有机会提交的因子都能上手优化。

---

### 探讨 #37: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.15

今日提交RA:2

analyst EUR TOP2500 Slow + Fast Factors

analyst EUR TOP2500 Subindustry

今日提交SA:

IND TOP500 Market

=====================================================================================

---

### 探讨 #38: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.16

今日提交RA:1

fundamental EUR TOPCS1600 Fast Factors

今日提交SA: IND TOP500 Market =====================================================================================

---

### 探讨 #39: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.17

今日提交RA:1 fundamental EUR TOPCS1600 Fast Factors

今日提交SA: IND TOP500 RAM =====================================================================================

---

### 探讨 #40: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.18 今日提交RA:1

analyst AMR TOP600 Country / Region =====================================================================================

---

### 探讨 #41: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.19

今日提交RA:1

analyst AMR TOP600 Country / Region

今日提交SA:

IND TOP500 RAM

=====================================================================================

---

### 探讨 #42: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.20

今日提交RA:3

model AMR TOP600 Country / Region * 2

analyst AMR TOP600 Country / Region

今日提交SA:

IND TOP500 Slow Factors

=====================================================================================

---

### 探讨 #43: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.21

今日提交RA:1

risk AMR TOP600 Country / Region

今日提交SA:

USA TOP3000 Market

=====================================================================================

---

### 探讨 #44: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.22

今日提交RA:1

model AMR TOP600 Country / Region

今日提交SA:

USA TOP3000 Slow Factors

=====================================================================================

---

### 探讨 #45: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.23

今日提交RA:4

risk AMR TOP600 Country / Region * 2

analyst AMR TOP600 Country / Region

model AMR TOP600 Country / Region

今日提交SA:

EUR TOPCS1600 Statistical

=====================================================================================

---

### 探讨 #46: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十一季_39156513806871.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.24

今日提交RA:3

analyst AMR TOP600 Country / Region *2

analyst AMR TOP600 RAM

今日提交SA:

EUR TOP2500 Statistical

=====================================================================================

---

### 探讨 #47: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.10今天终于迎来了combine和vf的刷新，而且是超过预想的惊喜，combine一举从-1.2拉升至3.18，同时vf也升至0.92，这说明我的提交策略是值得肯定的，接下来要做的就是提高产量。

=====================================================================================

---

### 探讨 #48: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.11，因为vf更新后达到了0.92，所以我开始尝试组SA，我打算先从USA地区开始，之前有了解过一点Selection Expression和Combo Expression，但没有实际写过，不过感觉还是挺容易上手的，也是成功地组出了第一个SA。 =====================================================================================

---

### 探讨 #49: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.12，今天把自己提交过的几个Region都试了一下，感觉USA的SA出货率不算很高，可能是因为USA作为最早的Region生产相关性太高了吧，我决定转战EUR和IND！

=====================================================================================

---

### 探讨 #50: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.13，今天继续提交了EUR的SA和一个USA的RA,GLB的PPA开了有一段时间了，但我对GLB的产量没有很大信心，所以先观望一下等等小地区的PPA活动吧。

=====================================================================================

---

### 探讨 #51: 关于《拒绝回测幻觉，死磕真实收益；逻辑驱动，数据为刃。》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【日常生活贴】我的量化日记第十季_38768672144151.md
- **评论时间**: 3个月前

=====================================================================================

2026.2.14，vf提升带来的base提升还是很可观的，同等水平的RA大概能拿到之前两倍的base，如果pc低一些还会更高，再加上SA的收入，几乎相比之前vf0.5时翻了10倍，这下更得努力稳住vf了。

=====================================================================================

---

### 探讨 #52: 关于《【火眼金睛】vf与combine齐飞，我提交了怎样的alpha（Osmosis自适应版）》的评论回复
- **帖子链接**: [Commented] 【火眼金睛】vf与combine齐飞我提交了怎样的alphaOsmosis自适应版.md
- **评论时间**: 3个月前

=====================================================================================

大佬太强了，收获满满。不过看完还有两个问题想问下，文章中提到的死鱼大概是换手低于多少的呢？还有IND地区的最低margin标准大概是多少？

=====================================================================================

---

### 探讨 #53: 关于《【火眼金睛】vf与combine齐飞，我提交了怎样的alpha（Osmosis自适应版）》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【火眼金睛】vf与combine齐飞我提交了怎样的alphaOsmosis自适应版_37319749642775.md
- **评论时间**: 3个月前

=====================================================================================

大佬太强了，收获满满。不过看完还有两个问题想问下，文章中提到的死鱼大概是换手低于多少的呢？还有IND地区的最低margin标准大概是多少？

=====================================================================================

---

### 探讨 #54: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: [Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享.md
- **评论时间**: 7个月前

这个插件可以检查sc吗？怎样用呢？没找到

---

### 探讨 #55: 关于《【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】华子哥 Genius Rank 分析插件安装和使用教程经验分享_34893885925783.md
- **评论时间**: 7个月前

这个插件可以检查sc吗？怎样用呢？没找到

---

### 探讨 #56: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】成为顾问一个月拿下Daily Osmosis Rank全球第一名经验分享_38898494065943.md
- **评论时间**: 3个月前

=====================================================================================

个人感觉分数分配时，权重分散可以避免os分数拉大胯，但也相对更难取得高分，这个还是看个人的取舍了

=====================================================================================

---

### 探讨 #57: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享.md
- **评论时间**: 3个月前

=====================================================================================

看完了，大佬是真教东西啊，这个初筛字段的方法很值得学习，确实还是应该把寻找好字段放在第一位，感谢大佬！

=====================================================================================

---

### 探讨 #58: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【经验分享】我的上分之路GoldMasterGrandmaster经验分享_38932709256727.md
- **评论时间**: 3个月前

=====================================================================================

看完了，大佬是真教东西啊，这个初筛字段的方法很值得学习，确实还是应该把寻找好字段放在第一位，感谢大佬！

=====================================================================================

---

### 探讨 #59: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【贺六浑】OpenClaw 快速安装与避坑指南代码优化.md
- **评论时间**: 3个月前

=====================================================================================

感谢大佬分享，祝大家早日成为安逸的养虾人，坐收渔翁之利

=====================================================================================

---

### 探讨 #60: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【贺六浑】OpenClaw 快速安装与避坑指南代码优化_38909536551575.md
- **评论时间**: 3个月前

=====================================================================================

感谢大佬分享，祝大家早日成为安逸的养虾人，坐收渔翁之利

=====================================================================================

---

### 探讨 #61: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享.md
- **评论时间**: 3个月前

=====================================================================================

感谢大佬的经验，内外层逻辑自洽这个经验很有价值，比盲目地套用常用操作符要有针对性多了，我以后也要注意这点

=====================================================================================

---

### 探讨 #62: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 【贺六浑】从大厂内卷到18线小城稳吃保底与我的两次GM进阶之路经验分享_38927243023383.md
- **评论时间**: 3个月前

=====================================================================================

感谢大佬的经验，内外层逻辑自洽这个经验很有价值，比盲目地套用常用操作符要有针对性多了，我以后也要注意这点

=====================================================================================

---

### 探讨 #63: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: [Commented] 关于Combined Power Pool Alpha Performance持续稳定的猜想212-242-197-262-267经验分享.md
- **评论时间**: 3个月前

=====================================================================================

感觉近几年的fitness和sharpe确实要更重要一些，就算前期稍微小于0都问题不大，但后几年表现不好很有可能就说明这个因子失去预测能力了

=====================================================================================

---

### 探讨 #64: 关于《PnL = ∑(Robustness * Creativity)》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 关于Combined Power Pool Alpha Performance持续稳定的猜想212-242-197-262-267经验分享_38846510482967.md
- **评论时间**: 3个月前

=====================================================================================

感觉近几年的fitness和sharpe确实要更重要一些，就算前期稍微小于0都问题不大，但后几年表现不好很有可能就说明这个因子失去预测能力了

=====================================================================================

---

### 探讨 #65: 关于《在Trae 中使用cnhkmcp中的Skills经验分享》的评论回复
- **帖子链接**: [Commented] 在Trae 中使用cnhkmcp中的Skills经验分享.md
- **评论时间**: 5个月前

=====================================================================================

确实，写cnhkmcp的这位大佬埋头做了不少功能但很少讲解，大概这就是实干派吧。总之感谢感谢楼主和大佬的分享，这就去Trae里试试效果。

=====================================================================================

---

### 探讨 #66: 关于《在Trae 中使用cnhkmcp中的Skills经验分享》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 在Trae 中使用cnhkmcp中的Skills经验分享_37609772940311.md
- **评论时间**: 5个月前

=====================================================================================

确实，写cnhkmcp的这位大佬埋头做了不少功能但很少讲解，大概这就是实干派吧。总之感谢感谢楼主和大佬的分享，这就去Trae里试试效果。

=====================================================================================

---

### 探讨 #67: 关于《把 AI Alpha 研究从“会写公式”推进到“会留证据”：一个轻量实验账本模板》的评论回复
- **帖子链接**: https://support.worldquantbrain.com[Commented] 把 AI Alpha 研究从会写公式推进到会留证据一个轻量实验账本模板_41225868972311.md
- **评论时间**: 8天前

阅读完这篇文章后我有很清晰的成长收获，过往我生成 Alpha 时仅聚焦输出表达式，缺少完整可追溯的研究佐证链条。文中提出的字段假设、算子逻辑、失败预判、迭代规划四维度前置梳理要求，补足了我输出内容里缺失的逻辑支撑，标准化实验账本能把信号的经济逻辑、测试参数、迭代路径完整留存，不再只提供孤立公式。优化后的提示词规范也约束我产出低冗余、有完整论证的因子方案，能帮助人类研究员规避盲目回测、仓促提交因子的问题，让 AI 从单纯公式生成工具转变为可复盘、可协作的量化研究辅助载体，大幅提升整套 Alpha 研发流程的严谨性与复用价值。

---
