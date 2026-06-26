# [代码优化] cnhkMCP在GeminiCLI中使用报错问题的解决经验分享

- **链接**: [Commented] [代码优化] cnhkMCP在GeminiCLI中使用报错问题的解决经验分享.md
- **作者**: GC13416
- **发布时间/热度**: 6个月前, 得票: 12

## 帖子正文

在使用 Gemini CLI 调用cnhkMCP时，经常遇到：MCP ERROR (worldquant-brain-forum-v2) **，** 
具体日志如图：


> [!NOTE] [图片 OCR 识别内容]
> [Feedback Details
> for "MCP ERROR
> Cworldquant
> brain-forum-v2)"] SyntaxError=
> Unexpected token
> "running the
> SerVer"
> is
> not Valid JSON
> at JSON .parse C<anonymous )
> at deserializeMessage (file: ///F: /brainauto /node_modules / @modelcontextprotocol/sdk /dist /esm /shared /stdio.js: 26:44)
> at ReadBuffer.readMessage (file: ///F: /brainauto /node_modules / @modelcontextprotocol /sdk /dist /esm/shared /stdio.js: 19: 16)
> at StdioclientTransport . processReadBuffer (file: ///F: /brainauto /node_modules / @modelcontextprotocol/sdk /dist /esm/client /stdio.js: 126:50)
> at
> Socket
> <anonymous> (file: ///F: /brainauto /node_modules
> @modelcontextprotocol /sdk /dist /esm/client /stdio.js: 92:22)
> at
> Socket
> emit Cnode
> eVents
> 519:28]
> at
> addchunk Cnode:internal/streams /readable: 561:12]
> at readableAddchunkPushByteMode Cnode:internal/streams /readable: 512:3)
> at Readable . push (node:internal/streams /readable: 392:5)
> at Pipe.onstreamRead
> Cnode:iternal /stream_base
> Commons
> 189:23)


查询资料后发现原因是：

MCP（Model Context Protocol）底层依赖  **JSON-RPC**  协议进行通信，其传输介质是进程的  **标准输入输出 (stdio)** 。

- **stdout (标准输出)** ：MCP 的“数据专用道”，只能传输纯净的 JSON 包。
- **stderr (标准错误)** ：MCP 的“日志专用道”，用于打印开发者调试信息。

**报错原因** ：代码中直接使用了  `print()`  语句。由于 Python 的  `print()`  默认将内容推送到  `stdout` ，这会导致非 JSON 文本混入数据流。客户端尝试解析这些文本时就会由于格式不符而直接崩溃。

修复方案：

将platform_functions.py内部的所有  `print`  替换为自定义的  `log`  函数。

 **错误写法 (导致崩溃)** 

**正确写法 (安全运行)**

 `print("Connecting...")` 
 `self.log("Connecting...")` 

 `print(f"Done: {id}")    ` 
 `sys.stderr.write(f"Done: {id}\n")` 

这是我的修改示例，各位可以自行替换修改即可
 
> [!NOTE] [图片 OCR 识别内容]
> Fos=
> 171
> 172
> Print
> instructions
> print (
> In"
> file=sys.stderr)
> print
> BIONETRIC AUTHENTICATION REQUIRED'
> file=sys
> stderp )
> print("
> file=sys.stderr)
> print
> Browser Window is open with biometric authentication page
> file=sys.stderr)
> print
> Complete
> the
> biometric authentication
> the
> browser
> file=sys.stderr)
> print("The system Will automatically check
> When YOU re
> done
> file=sys.stderr )
> print
> file=sys.stderr)
> 173
> seIf.IOg("In"
> 174
> seIf.IOg
> BIOMETRIC
> AUTHENTICATION REQUIRED"
> 175
> self.IOg(
> seIf.Iog (
> Browser
> Windou
> open With
> biometric
> authentication page'
> 器
> self.Iog
> Complete the biometric authentication
> in the
> browser
> self.IOg
> The System Will
> automatically check when yoU're
> done
> 179
> self.10g('
> -39
> 181
> Keep
> Checking until authentication is
> CowhLete
 
我之前写过一篇帖子： “cnhkMCP在Antigravity配置失败的解决方法”： [[代码优化] cnhkMCP在Antigravity配置失败的解决方法 – WorldQuant BRAIN]([L2] [代码优化] cnhkMCP在Antigravity配置失败的解决方法代码优化_37022069038231.md) 
如果使用的是Antigravity的IDE，可在这个基础上稍微完善一下即可，代码在80行： 
> [!NOTE] [图片 OCR 识别内容]
> IoBging.debug (f"Forwarded:
> {len(clean_json_bytes) }
> bytes
> except
> 1500
> ISONDecodeEpror
> Iogging warning(f"BLOCKED NOISE:
> flinel
> 迸襁眵非 JSON
> 祆西 (厕 print
> 『G) 记录<只盂丈件
> IoBging.info(f" [SUBPROCESS LOG] {decoded_line}
> except Exception
> IoBging.error(f"Error
> processing Iine:
> {e}'


把：  logging.warning(f"BLOCKED NOISE: {line}")
替换为：

logging.info(f"[SUBPROCESS LOG] {decoded_line}")

以上respect！
各位有疑问可以提出。

---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 NL80893 (Rank 16), 时间: 5个月前)

不得不佩服大佬的技术钻研能力！不仅找到报错的底层原因（JSON-RPC 协议 /stdout/stderr 分工），还给出了针对性的修复方案，甚至兼顾了 Antigravity IDE 的适配，考虑得太周全了。这个问题其实在 MCP 开发中很容易踩坑，大佬的分享不仅解决了当下问题，还能帮大家规避类似的 stdio 使用误区，太有参考价值了！

====================================================================================祝大佬base多多，vf高高，分享更多知识呀～～====================================================================

---

### 评论 #2 (作者: HW93328, 时间: 5个月前)

============================HW93328======================================

感谢楼主的分享，最近看了一些论坛帖子才把gemini cli配置好，很多结合brian平台的功能都要靠论坛的各位大佬分享，ai时代还是要多和ai做朋友，目前还在进一步研究，希望能够早日驾驭，总之感谢楼主分享，一起加油！！！

============================HW93328=======================================

---

