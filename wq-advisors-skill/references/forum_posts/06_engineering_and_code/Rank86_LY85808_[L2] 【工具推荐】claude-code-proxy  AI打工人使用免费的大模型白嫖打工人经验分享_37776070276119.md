# 【工具推荐】claude-code-proxy + AI打工人：使用免费的大模型白嫖打工人！经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【工具推荐】claude-code-proxy  AI打工人使用免费的大模型白嫖打工人经验分享_37776070276119.md
- **作者**: JC25837
- **发布时间/热度**: 5 months ago, 得票: 98

## 帖子正文

AI打工人只提供了kimi与deepseek，如果想使用其他的大模型还可以通过修改Step4_SetAPI_And_Check_LLMModel.py里面的参数进行新增，但是国内的大模型普遍收费，唯一的iflow免费但是不支持anthropic，使用claude-code-proxy就可以解决Claude Code与OpenAI兼容API之间的互操作性问题，项目地址： [https://github.com/fuergaosi233/claude-code-proxy。](https://github.com/fuergaosi233/claude-code-proxy%E3%80%82)

## **部署Claude Code Proxy**

### **安装与配置**

### **1. 安装依赖**

项目Clone到本地后，直接运行 `pip install -r requirements.txt` 即可安装依赖。

### **2.**  **配置环境变量**

```
cp .env.example .env
# 编辑.env并添加您的API配置

```

主要配置项包括：

- **必需配置** ：
  - OPENAI_API_KEY：目标提供商的API密钥，例如：your-openrouter-api-key
- **安全配置** ：
  - ANTHROPIC_API_KEY：输入的预期Anthropic API密钥（随便输入以区分openai_ai_key）
- **模型映射配置** ：
  - BIG_MODEL：Claude opus请求的映射模型（例如：anthropic/claude-sonnet-4）
  - MIDDLE_MODEL：Claude sonnet请求的映射模型（例如：anthropic/claude-sonnet-4）
  - SMALL_MODEL：Claude haiku请求的映射模型（例如：anthropic/claude-3.5-haiku:beta）
- **API端点配置** ：
  - OPENAI_BASE_URL：API基础URL（例如： [https://openrouter.ai/api/v1）](https://openrouter.ai/api/v1%EF%BC%89)

### **3.**  **启动代理服务器**

```
# 直接运行
python start_proxy.py

```

代理启动成功后，会显示类似如下的信息：


> [!NOTE] [图片 OCR 识别内容]
> C: Users cministrator〉
> C: /Users / Administrator/NPpDatalLocal/Programs
> Python/Python313/python.exe
> C:  Users
> Acministraor
> DOCU
> Ments /rae_projects/claude
> Code-proxy-main/start_proxy.Py
> Configuration Ioaded: API_KEY= 烹寰熹熹寰寰寰寰熹寰寰寰寰熹寰寰寰寰熹寰
> BASE_URL= 'https: /lapis.iflow.cn/vl
> Clauce-
> TO-OpendI
> API Proxy
> V1.8
> Configuration loaded successfully
> OpenI Base URL: https: /Japis.iflow.cn/vl
> B Model
> (OpUs): deepseek-V3.2
> Middle Wodel (sonnet): deepseek-v3.2
> SMall Model
> (haiku):
> Ceepseek-v3.2
> Ilax Tokens
> Liniz:
> 48968
> Request Timeout:
> 985
> Server:
> 8.0.0.0:8882
> CLient
> API
> Key Validation: Enabled
> INF0:
> Started
> seryer process
> [13096]
> INF0:
> Waiting
> for
> application startup
> INF0:
> Application
> SCarUP
> Complete
> INF0:
> Uicomn
> On http: //0.0.0.0:8082 (Press
> CTRLtC TO quit)
> runnine


### **与Claude Code集成**

启动代理服务器后，

配置Claude Code使用该代理：

```
ANTHROPIC_BASE_URL=http://localhost:8082 
ANTHROPIC_AUTH_TOKEN="your openrouter api key"
ANTHROPIC_API_KEY="输入的预期Anthropic API密钥" 
claude

```

也可以将这些设置添加到环境变量中，以便持久化使用，同时将打工人设置的其他环境变量全部删除。

如下图所示，Claude Code已经通过Claude Code Proxy成功连接到iflow上的模型：

```

```

---

## 讨论与评论 (8)

### 评论 #1 (作者: CL86067, 时间: 5 months ago)

感谢大佬分享，这个真的太及时了，ai打工人急需这方面的支持，另外不知道大家最近听说opencode没，这个个似乎算是claude code的开源版，模型都支持还有免费模型，也可以试一下这个

---

### 评论 #2 (作者: PY32594, 时间: 5 months ago)

请问怎么获得iflow的免费大模型

---

### 评论 #3 (作者: XW83124, 时间: 5 months ago)

这个地方要按照例如里面输入吗? 
> [!NOTE] [图片 OCR 识别内容]
> 主要配置项包括:
> 必需配置:
> OPENAI_API_KEY:
> 目标提供商的4P|密钥。例如: your-openrouter-api-key
> 安全配置:
> ANTHROPIC_API_KEY: 输入的预期Anthropic API密钥
> 盲便输A以区分openaiai
> Kal)
> 模型映射配置:
> BIC_MODEL: Claude 0pUs请求的映射模型 (例如: anthropiclclaude-sonnet-4)
> MIDDLE_MODEL: Claude sonnet请求的]映肘模型 (例如: anthropiclclaude-sonnet-4)
> SMALL_MODEL: Claude haiku请求的映射
> (例如: anthropiclclaude-3.5-haiku:beta)
> API端点配置:
> OPENAI_BASE_URL: API基础URL (例如:
> htps:llopenrouterailapifl)


目前已成功启动袋里服务器.但是打开之后就报错了. 
> [!NOTE] [图片 OCR 识别内容]
> Claude Code
> Tips
> for
> gettizg
> Started
> Ielcome bacl
> Rul !ii
> create
> CLA[JIIE.Id file nith ilstructions for
> Plaude
> Recelt activity
> J
> recelt  actirity
> Solet
> 4.5_
> I [Jsaae Billirzi
> Clalde
> ! Iltl Colfl
> ct:
> Both
> tolell
> (NUIHOPIC_SJTH_T}E)
> ald
> al SI
> key {NUIIHOPIC_fI_J:
> aLe
> Set。
> Tlis
> IaY lead
> lllezected belatior
> TIyirna
> USe
> SIHOPIC_SJT珏_10k 凹?
> Inset tle AIHOPICfI_J'
> ellrirolmellt  Tariable,
> Cr claude !1ozont then
> Sa
> J
> to the S1
> Lej aPPIOTa1
> before
> Oi。
> TIyirna
> USe
> NIHOPIC_-工_嘎m? Inset tlhe SIHOPIC_SlJIH_T0斑EL eironert Tariable
> !odel
> tr3 Vplls
> 你是什么模型
> 41
> detail" :"Ilalid SI
> Le。
> Please Proride
> Talid Itlrop1
> SI
> Le3
> Retrying i 3 seconds
> (attelwt 410〉
> SI_TIJEOIJT_JIS=gOOOOOS
> tr icreasiila it
> Boopina
> (ctrltc
> to interrupt}
> for
> Shortcllts
 请指导一下,是哪个地方出错了.整个过程使用的方法都是配置环境变量. 
> [!NOTE] [图片 OCR 识别内容]
> 娈昼
> ANTHROPIC_API_KEY
> sl-2
> ANTHROPIC_AUTH_TOKEN
> sk-2bcffa72ACE
> ANTHROPIC_BASE_URL
> http:i Ilocalhost:8082
  
> [!NOTE] [图片 OCR 识别内容]
> 娈昼
> ANTHROPIC_API_KEY
> BIG_MODEL
> anthropic /claude-sonnet-4


---

### 评论 #4 (作者: JC25837, 时间: 5 months ago)

@ [XW83124](/hc/zh-cn/profiles/36656210166935-XW83124)  环境变量不用设置BIG_MODEL，只要在env里设置

---

### 评论 #5 (作者: BX86068, 时间: 5 months ago)

那个项目地址点进去404是什么鬼，项目下架了吗

---

### 评论 #6 (作者: YS94888, 时间: 5 months ago)

Claude通过Claude Code Proxy成功连接iflow，但是使用过程中老是出现【API Error: 422】错误，这个应该是iflow服务器端的限制吧？

---

### 评论 #7 (作者: YQ84572, 时间: 4 months ago)

很好的分享claude-code+ai打工人是很好的组合，感谢大佬的分享
=============================================================================

The only thing permanent is change. What we need to do is to constantly improve ourselves.

=============================================================================

---

### 评论 #8 (作者: XH28239, 时间: 3 months ago)

点进去，报404

---

