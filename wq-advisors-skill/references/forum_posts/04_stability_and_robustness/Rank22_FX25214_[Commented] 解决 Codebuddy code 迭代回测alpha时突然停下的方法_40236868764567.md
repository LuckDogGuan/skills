# 解决 Codebuddy code 迭代回测alpha时突然停下的方法

- **链接**: https://support.worldquantbrain.com[Commented] 解决 Codebuddy code 迭代回测alpha时突然停下的方法_40236868764567.md
- **作者**: HZ32281
- **发布时间/热度**: 1个月前, 得票: 5

## 帖子正文

最近尝试了一下用codebuddy code来回测，发现在使用完自带credit额度之后如果换上第三方API，运行过程中经常会突然就不动了。其实主要是上下文过长导致的，原本在使用自带credit的时候它就会自动运行“/compact”（上下文压缩），在加入models.json了之后就不会自动触发了，说明触发机制在全局文件夹中，在我让AI分析codebuddy全局文件夹之后了解了自动compact的机制，简单来说就是达到上下文限制70%的时候自动触发 /compact。

那么如果自己设置了第三方API，可以通过设置两个文件来实现，首先是~/.codebuddy/settings.json，在其中加入： "autoCompactEnabled": true，例如：

{

"trustedDirectories": [

"你的项目文件夹"

],

"model": "custom-local:glm-5.1",

"autoCompactEnabled": true

}

然后是~/.codebuddy/models.json，在其中加入："maxInputTokens": 128000   （通常glm-5.1的上下文设置是128000，可以你自己设置），例如：

{

"models": [{

"id": "glm-5.1",

"name": "你的厂商模型",

"vendor": "openai",

"apiKey": "sk-***",

"url": "你的厂商url",

"supportsToolCall": true,

"supportsReasoning": true

"maxInputTokens": 128000

}]

}

---

## 讨论与评论 (6)

### 评论 #1 (作者: HH34943, 时间: 1个月前)

大佬你不使用geminicli来工作了吗

---

### 评论 #2 (作者: BW14163, 时间: 1个月前)

glm还没用过，听说挺好用的，该天去试试。

看到出现这个问题，一开始默认的设置上下文长度应该比较低，学到了，以后遇到这个问题让ai帮忙在这个方向调整下。

**********************************
紧跟大佬的脚步，每天坚持至少学一个知识点，尽量不混信号，不过拟合。
Prioritize diversity, strong margin, low correlation, stable diversification; strictly control costs and overfitting.
**********************************

---

### 评论 #3 (作者: 顾问 FX25214 (Rank 22), 时间: 1个月前)

那请问佬是否有尝试过通过将一段长的prompt换成多个数个小的prompt来分解长任务或者复杂任务来解决这个停下的问题呢？还是说这个问题就只能通过本质的框架修改进行解决？
希望佬能给出实例化的解答
------------------------------------------来自传奇耐打王的小疑问-----------------------------------------------------------------------

---

### 评论 #4 (作者: HZ32281, 时间: 20天前)

@ [HH34943](/hc/en-us/profiles/37523541660567-HH34943)  用的，主要那段时间Gemini经常 think a bit longer 卡住一两个小时一动不动。就想着试试其他的，正好可以交叉验证了

---

### 评论 #5 (作者: HH34943, 时间: 16天前)

OKOK谢谢

---

### 评论 #6 (作者: HZ32281, 时间: 16天前)

[顾问 FX25214 (Rank 22)](/hc/en-us/profiles/32678330190999-顾问 FX25214 (Rank 22))  你说的是sub-agent或者agent-team的模式对吧，每个agnet处理各自的部分？我用过的，Gemini只有sub-agent的模式，每个agent互不沟通，独立工作，除非工作流设计非常巧妙，否则效果并不好，经常会卡住，然后自动cancel。现在大部分的模型都是agent-team了，我用glm5.1尝试过，当时设置了5个agent，说我设置的agent过多，运行不了，然后就没试过了。

---

