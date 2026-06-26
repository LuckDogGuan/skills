# 【MCP WorkFlow】MCP本地LLM配置经验分享

- **链接**: https://support.worldquantbrain.com[L2] 【MCP WorkFlow】MCP本地LLM配置经验分享_36975707112727.md
- **作者**: BZ22718
- **发布时间/热度**: 6 months ago, 得票: 13

## 帖子正文

对于刚通过MCP调用AI来解决量化研究问题的新手，这个解决问题的过程本身也需要学习和研究，找到一种或若干种高效的工作流。而学习和研究的过程中需要大量尝试，比如调校MCP一开始就能完成Worldquant BRAIN登录，然后再处理后续流程。

这一过程会消耗大量AI服务商的token，可能会产生一定费用。如果可以使用本地的高性能AI模型，是否能够更低成本地学习和研究MCP的使用？答案是可以的。

本文以LM Studio为例，介绍Visual Studio Code + Roo Code配置MCP访问本地AI Server乃至cnhkmcp「七十二变」等功能调用LM Studio本地AI的方法。

## 第一步：LM Studio准备

LM Studio的安装方法很简单，支持Windows、Linux、MacOS多操作系统，从其官网 [https://lmstudio.ai/下载对应安装文件安装即可。](https://lmstudio.ai/%E4%B8%8B%E8%BD%BD%E5%AF%B9%E5%BA%94%E5%AE%89%E8%A3%85%E6%96%87%E4%BB%B6%E5%AE%89%E8%A3%85%E5%8D%B3%E5%8F%AF%E3%80%82)

注：中国大陆用户需将「huggingface.co」替换为「hf-mirror.com」才能在LM Studio中查找和下载模型。

在LM Studio中下载好模型后 (若不了解方法，请自行搜索，但软体很好使用、很直观)，在左侧开发者tab下，加载模型，右侧即可显示model name和base url (如下图)。


> [!NOTE] [图片 OCR 识别内容]
> Info
> Context
> Inference
> Load
> Model Information
> Model
> quen/qwen3-next-80
> File
> Owen3 Hlext-8BB-AB-Instruct-04_KM。
> Format
> GGUF
> Quantization
> KN
> Arch
> qWennext
> 此横型经过工具使用的训练
> Domain
> ll
> Size On disk
> 48.41 GB
> API Usage
> This model's APIidentifier
> qwen /qwen3-next
> 80b
> The
> 0Cal SerVeT Is reachable at this address
> http: //192.168.1.100:1234
> 99uf


建议在模型设置中，将上下文长度设置为该模型支持的最大值，本文使用「qwen/qwen3-next-80b」，支持256K上下文，这是本地AI相对于许多在线AI服务商的优势。但本地AI模型参数量不及在线AI服务商提供的高端模型，思维能力有所不及。


> [!NOTE] [图片 OCR 识别内容]
> qwen3-next
> 80b
> Change source model file
> Enable override
> Qwen3 Next 808 A3B Instruct
> N_NN
> Parameters yOU Set here Will be Used a5 default Values for the modee
> Nhen
> 1s Used i the Chat orinthe Server。Learn more。
> Load
> Prompt
> Inference
> Speculative Decoding
> 上下文长赓
> 262144
> 横型支持最空
> 262144
> 个tokon
> GPU 卸载
> CPU 线程池大小
> 评估批处理d小
> 512
> RoPE
> 频宰基
> 自动
> ROPE 频宰比例
> 自动
> 将 KV 缓存卸载到 GPU 内存
> (9++LTIT7


## 第二步：Roo Code配置

本文不再赘述Visual Studio Code + Roo Code plugin + python安装cnhkmcp的方法与配置，具体请参考论坛其他文章。

Roo Code集成了LM Studio配置，直接在设置页面MCP tab下「API Provider」中下拉选择「LM Studio」，「Base URL」配置为「http://localhost:1234」或正确的「http://[server_ip]:[server_port]」，「Model ID」配置为LM Studio中对应模型名称，可直接在LM Studio中复制。


> [!NOTE] [图片 OCR 识别内容]
> 凸 Providers
> Contiguration Profile
> Imstudio
> 十 /回
> Save different API configuratons to quichy swtch
> belween providers and settings
> API Provider
> U Studio 8
> LM Studio
> Base URL (optional)
> http;//92.168.10.250.1234
> ModelID
> qwenqwen3-next-8Ob
> The model ID
> (qwenlqweng-next gOOJ yOu
> providedisnotavallable Please Choose a
> Jifferent moJal
> Enable Speculatve
> Decoding
> U Studio aIOWs YOU to run modals Iocall OnyOuT
> Computer Forinstructions on howto gatstarted SEE
> their qulckstart gulde. You Wllalso need tO stan
> U Studos local Serer teature tO UsE I Mith this
> extension
> Note: Roo Code Uses complex prompts
> and works best Mth Claude models Less Capable
> models may not work as
> expected


配置完成后 (上图中红字「The model ...」可以忽略)，选择保存/Save或者完成/Done。然后可以像使用在线AI API一样使用。


> [!NOTE] [图片 OCR 识别内容]
> worldquant brain platform
> Completed
> read_specific_documentation
> Retreyc detalcd CoNertota
> Jooumcntaton
> Daqcarlele
>  {In
> 1"simulation
> settinesIn}
> API Requt
> Roo wants to Use
> tool on the worldquant brain
> platform MCP server
> worldquant brain-platform
> Completed
> read_specific_documentation
> Retrieve detalled content Ofa SpeGfc doqmentaton
> 0ag
> aricle
> {I
> id": |vintermediate-pack-part
> 21"10}"
> APIREeqUeSt
> Roo wants to Use
> toolon the worldquant brin
> platform MCP server
> worldquant brain platform
> Completed
> read_specific_documentation
> Retrove detaled Coentota speoc dooumentamon
> 50cc
> id:
> 4"pane
> "0aB


## 附加：cnhkmcp「七十二变」中本地AI配置

这部分配置主要有两点不一样：

(1) Base URL是「http://[server_ip]:[server_port]/v1」，例如「 [http://192.168.10.250:1234/v1」、「http://localhost:1234/v1」。。](http://192.168.10.250:1234/v1%E3%80%8D%E3%80%81%E3%80%8Chttp://localhost:1234/v1%E3%80%8D%E3%80%82%E3%80%82)

(2) LLM API Key可以随便填写

模型名称还是第一步中得到的。


> [!NOTE] [图片 OCR 识别内容]
> BRAIN Transformer (72娈)
> Configuration
> LLM Model Name
> qwenqwen3-next- 80b
> LLM API Key
> LLM Base URL
> htp:1l192.168.10.250.1234/1
> Test LLI COMeCton
> Connection SUCCESSTUII


配置好了点击「Test LLM Connection」，通过即可。

以上就是我配置MCP使用本地AI的方法，有错误请指出。

---

## 讨论与评论 (4)

### 评论 #1 (作者: HY20507, 时间: 5 months ago)

真不错，通过使用本地大模型，节省了花费，同时因为本地模型，api key随便填写，省去了每次更新cnhkmcp后api key重新输入的情况，最棒的是从这个帖子了解到有LLM studio这种配置本地大模型的方法，很赞

---

### 评论 #2 (作者: YQ84572, 时间: 5 months ago)

很详细的配置方案，对于新人入手mcp很有帮助

--------------------------------------------------------------------------------------------------------------------

感谢分享，祝国区越来越好

--------------------------------------------------------------------------------------------------------------------

---

### 评论 #3 (作者: LT59611, 时间: 5 months ago)

我用ollama也可以。

---

### 评论 #4 (作者: JQ70858, 时间: 1 month ago)

已经下载了，但是旧电脑一直出问题，配置不了。今天新电脑试试。这东西是不是很吃内存？网上说那个模型名字里几B（比如7B）的，需要你的内存是至少1.5*7那么大才好运行。不过我只是想试试用AI跑的感觉，之前用过一段时间，完全没跑出任何好结果。。

---

