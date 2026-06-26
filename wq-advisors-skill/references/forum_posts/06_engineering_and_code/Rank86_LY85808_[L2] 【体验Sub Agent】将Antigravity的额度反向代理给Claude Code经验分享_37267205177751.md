# 【体验Sub Agent】将Antigravity的额度反向代理给Claude Code经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【体验Sub Agent】将Antigravity的额度反向代理给Claude Code经验分享_37267205177751.md
- **作者**: OB53521
- **发布时间/热度**: 6 months ago, 得票: 26

## 帖子正文

很多小伙伴都已经使用过Gemini CLI和Antigravity搭配MCP进行Alpha挖掘，但是目前为止，执行MCP最强的仍然是Claude，但是Claude由于及其严格的风控以及高昂的价额，劝退了很多用户。

今天分享一个可以将Antigravity的额度转换为Claude Code API的工具： [https://github.com/lbjlaq/Antigravity-Manager](http://Antigravity%20Manager)


> [!NOTE] [图片 OCR 识别内容]
> Antigravity Tools
> 仪表盘
> 账号管理
> API 反代
> 设置
> 0
> EN
> d  服务配置
> 服务已停止
> 启动服务
> 监听端口
> 请求超时
> 8045
> 120
> 跟随应用自动启动
> 默认8045,修改端口需重启服务
> 默认120秒。范围30-600  秒。修改后需重启服务生效。
> API 密钥
> 注意:  请妥善保管您的 API 密钥。不要泄露给他人。
> @ 模型路由中心 (Model Router)
> 重置映射
> 按"规格家族"统一路由 OpenAllClaude 模型;
> 或添加最高优先级的"精确映射
> 模型家族分组 (SERIES GROUPS)
> Claude 4.5 系列
> Claude 3.5 系列
> GPT-4 /o1 系列
> GPT-4o/3.5 系列
> 6
> Opus 4.5, Sonnet 4.5 (推理)
> 8^
> Sonnet 3.5, Haiku 3.5
> GPT-4, Turbo, o1-preview
> GPT-4o, Mini, 3.5 Turbo
> claude-opus-4-S-thinking
> claude
> -sonnet-4-S-thinking
> (Default )
> Iemini-3-pro-high
> (Default )
> gemini-3-flash
> (Default)
> 专家精确映射 (EXPERT CUSTOM ROUTING)
> 添加映射 (ADD MAPPING)
> 当前映射列表 (CUSTOM LIST)
> Original (e.9。 gpt-4)
> Target
> (e.9.
> gemini-2.5-pro )
> 原始模型 ID
> 路由目标
> 操作
> 十 添加
> 暂无自定义精确映射
> 支持模型与集成 (Supported Models & Integration)
> 模型名称
> 模型 ID
> 描述
> 操作
> 快速集成 (QUICK INTEGRATION)
> Python (OpenAl SDK)
> g
> Gemini 3 Flash
> gemini-3-flash
> 极速预览
> Copy
> from openai import OpenAI


AM充当一个中转站的角色，你可以把各种 AI 服务（Claude、ChatGPT、Gemini等）账号填进去，它会帮你监控余额/额度，并提供一个本地代理地址。你可以让其他软件，如：Claude Code，连接这个本地地址来调用AI。

通过这种方式，我们就可以将Gemini的额度转换给Claude Code使用，因为AM模拟了Anthropic的接口。

配置成功之后，就可以在Claude Code中创建自己的Sub Agents实现更佳强大的工作流了。


> [!NOTE] [图片 OCR 识别内容]
> Welcome
> to Opus
> 4.5
> lagents
> Agents
> agents
> Create
> neW agent
> Project agents ( /Users /orange / Codeproject /consultant/ .claude /agents)
> I4
> Critic
> Sonnet
> I4
> execUtor
> Sonnet
> Wq-strategist
> Sonnet
> Wq-gatekeeper
> Sonnet
> Built-in agents (always available)
> general -pUrpose
> Sonnet
> statusline-setup
> Sonnet
> Explore
> haiku
> Plan
> inherit
> Claude
> Code-
> ~guide
> haiku
> PresS
> to navigate
> Enter
> t0
> S8leCt
> ESC
> t0
> back


你可以定义多个角色，分配不同的工作。从收集资料、阅读论文，到创建模板、编写表达式，再到分析结果，设计优化策略。

如果你愿意，最后还能分配一个agent（图中的gatekeeper）接收由critic agent传过来的已经通过标准（平台硬性标准+你自己设定的标准）的Alpha，gatekeeper会再次对Alpha进行审核，通过这样两次的双重审核，确保提交上去的Alpha完全符合你的要求。

---

## 讨论与评论 (2)

### 评论 #1 (作者: JR57542, 时间: 5 months ago)

这个反代策略有bug吗，或者说和原生cc订阅有什么缺陷吗，工具调用啥的

---

### 评论 #2 (作者: FF56620, 时间: 4 months ago)

反重力的确很好，不过最近Google封号杀的有点狠，地主家余粮也不多了

-------------------------------------
Pursue scalable, repeatable opportunities rooted in probability.

---

