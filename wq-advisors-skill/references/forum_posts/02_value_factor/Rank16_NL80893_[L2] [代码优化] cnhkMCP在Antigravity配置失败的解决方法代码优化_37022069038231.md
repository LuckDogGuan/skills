# [代码优化] cnhkMCP在Antigravity配置失败的解决方法代码优化

- **链接**: https://support.worldquantbrain.com[L2] [代码优化] cnhkMCP在Antigravity配置失败的解决方法代码优化_37022069038231.md
- **作者**: GC13416
- **发布时间/热度**: 6 months ago, 得票: 19

## 帖子正文

这份报告详细记录了如何成功配置 cnhkMCP 服务，使其能够与 Windows 环境下的 Antigravity 稳定通信。

1. **问题背景**

在初始配置中，Antigravity 不断报错：

Error: calling "initialize": invalid trailing data at the end of stream.
 
> [!NOTE] [图片 OCR 识别内容]
> Manage MCP servers
> 100tools
> View raw config
> Retresh
> cnhk-mcp
> cnhk-mcp
> Configure
> Error;
> calling "initialize'
> invalid trailing data at the end of stream。


**原因分析** ：

1. **杂音污染** ：cnhkMCP（以及底层的 FastMCP）在启动或运行时，会向标准输出（stdout）打印日志或调试信息。JSON-RPC 协议非常严格，任何非 JSON 格式的输出都会被客户端（Antigravity）视为协议违规。
2. **编码干扰** ：Windows 下 Python 默认的

stdout 是文本模式，会自动处理换行符（CRLF）并可能使用系统默认编码（如 GBK/cp1252），这破坏了 JSON-RPC 要求的严格 UTF-8 编码。

1. **核心解决方案：二进制清洗代理 (Binary Sanitizing Proxy)**

为了彻底解决上述问题，我们没有修改 MCP 的源码，而是开发了一个中间层代理脚本

cnhk_mcp_server_safe.py。

2.1 代理脚本逻辑

该脚本作为 Antigravity 和 MCP 服务之间的“防火墙”：

1. **子进程隔离** ：它启动真实的 MCP 服务作为子进程。
2. **强制二进制模式** ：使用 Windows msvcrt 库强制将标准输入/输出流切换为 **二进制模式 (O_BINARY)** 。这绕过了 Python 的文本编码层，防止任何自动的字符转换。
3. **智能清洗** ：

1. 文件配置

3.1 代理脚本 (

cnhk_mcp_server_safe.py)

位于

C:\Users\chen.gemini\antigravity\cnhk_mcp_server_safe.py。 此脚本负责启动 Python 环境并加载 platform_functions.py。

3.2 MCP 配置文件 (mcp_config.json)

位于 C:\Users\chen\.gemini\antigravity\mcp_config.json。 配置如下：

{

"mcpServers": {

"cnhk-mcp": {

"command": "f:/BRAIN/.venv/Scripts/python.exe",

"args": [

"C:/Users/chen/.gemini/antigravity/cnhk_mcp_server_safe.py"

],

"env": {

"PYTHONUNBUFFERED": "1"

}

}

}

}

1. **验证结果
   
> [!NOTE] [图片 OCR 识别内容]
> 所有功能测试完毕。表现完美!
> 我已经全面测试了 MCP 服务的 4个类别共 40个工具; 结果如下:
> 基础功能 (System):
> 身份认证: 成功识别用户  BC_341E 。
> 配置管理: 成功读取平台和用户设置。
> 数据查询 (Data):
> 数据集/字段: 成功检索到
> Cee
> 等字段和
> Jrialyst
>  =-LJ= t= =
> 等数据集。
> 排行榜/活动:成功获取最新活动和排名信息。
> Alpha & 仿真 (AlphalSim):
> Alpha 详情: 成功读取您的 Alpha
> Q231515
> 及其 Pnl 年化数据。
> 创建仿真: 成功提交了
> ~新的测试仿真
> OamTTSZV Ja
> 批量仿真: 成功执行了
> C2Ht
> RIIt_SIim
> 批虽测试。
> 社区内容 (Community):
> 论坛搜索: 成功搜索井读取了帖子内容 (如"alpha 模拟高效筒")。
> 文档获取: 成功抓取了官方文档内容。
> 唯-的几个报错(如404〉 屑于服务端正常昀逻辑反馈 (例如请求了不存在的数据)
> 完全证
> 实了通信链路畅通无阻。
> 结论:  您的 MCP 服务现在非常健壮。我已经学握了所有工具的用法。随时准备为您效芳!
> Walkthroughmd
> Open
**

下面是我的cnhk_mcp_server_safe.py完整代码，供各位参考：
 **import sys**

**import os**

**import subprocess**

**import threading**

**import json**

**import logging**

**import msvcrt**

***# Path to the python executable and the target script***

**PYTHON_EXE = r"f:\BRAIN\.venv\Scripts\python.exe"**

**TARGET_SCRIPT = r"f:\BRAIN\.venv\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"**

**LOG_FILE = r"C:\Users\chen\.gemini\antigravity\cnhk_mcp.log"**

***# Configure logging***

**logging.basicConfig(**

**filename=LOG_FILE,**

**level=logging.DEBUG,**

**format='%(asctime)s - %(levelname)s - %(message)s'**

**)**

**def run_proxy():**

**logging.info("Starting Binary Sanitizing Proxy...")**

***# 1. Force standard streams to binary mode at the OS level***

**if sys.platform == 'win32':**

**msvcrt.setmode(sys.stdin.fileno(), os.O_BINARY)**

**msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)**

**msvcrt.setmode(sys.stderr.fileno(), os.O_BINARY)**

***# 2. Start the actual MCP server as a subprocess***

**env = os.environ.copy()**

**env["PYTHONUNBUFFERED"] = "1"**

**try:**

**process = subprocess.Popen(**

**[PYTHON_EXE, TARGET_SCRIPT],**

**stdin=subprocess.PIPE,**

**stdout=subprocess.PIPE,**

**stderr=subprocess.PIPE,**

**env=env,**

**bufsize=0  *# Unbuffered***

**)**

**except Exception as e:**

**logging.error(f"Failed to start subprocess: {e}")**

**sys.exit(1)**

**logging.info(f"Subprocess started with PID: {process.pid}")**

***# 3. Setup stdout forwarding & sanitization***

**def forward_stdout():**

**buffer = b""**

**while True:**

**try:**

***# Read raw bytes***

**char = process.stdout.read(1)**

**if not char:**

**break**

**buffer += char**

**if char == b'\n':**

***# Process the line***

**line = buffer.strip()**

**if line:**

**try:**

***# Decode for parsing***

**decoded_line = line.decode('utf-8')**

***# Verify valid JSON***

**obj = json.loads(decoded_line)**

***# Re-serialize to strict UTF-8 bytes without newlines inside***

**clean_json_bytes = json.dumps(obj, ensure_ascii=False).encode('utf-8')**

***# Write raw bytes to stdout buffer + single newline byte***

**sys.stdout.buffer.write(clean_json_bytes + b'\n')**

**sys.stdout.buffer.flush()**

**logging.debug(f"Forwarded: {len(clean_json_bytes)} bytes")**

**except json.JSONDecodeError:**

**logging.warning(f"BLOCKED NOISE: {line}")**

**except Exception as e:**

**logging.error(f"Error processing line: {e}")**

**buffer = b""**

**except Exception as e:**

**logging.error(f"Error in stdout loop: {e}")**

**break**

**logging.info("Stdout forwarding ended")**

***# 4. Setup stderr forwarding***

**def forward_stderr():**

**while True:**

**try:**

**line = process.stderr.readline()**

**if not line:**

**break**

**logging.error(f"STDERR raw: {line}")**

**except:**

**break**

***# 5. Setup stdin forwarding***

**def forward_stdin():**

**while True:**

**try:**

***# Read raw bytes from stdin buffer***

**line = sys.stdin.buffer.readline()**

**if not line:**

**break**

**process.stdin.write(line)**

**process.stdin.flush()**

**logging.debug(f"Forwarded input: {len(line)} bytes")**

**except Exception as e:**

**logging.error(f"Error in stdin loop: {e}")**

**break**

**try:**

**process.stdin.close()**

**except:**

**pass**

***# Start threads***

**t_stdout = threading.Thread(target=forward_stdout, daemon=True)**

**t_stderr = threading.Thread(target=forward_stderr, daemon=True)**

**t_stdin = threading.Thread(target=forward_stdin, daemon=True)**

**t_stdout.start()**

**t_stderr.start()**

**t_stdin.start()**

**process.wait()**

**if __name__ == "__main__":**

**run_proxy()**

---

## 讨论与评论 (3)

### 评论 #1 (作者: LL32212, 时间: 6 months ago)

感谢分享，代码完美运行，之前我也尝试过让ai写这样一个代理文件，但由于不太懂python不会引导就没有成功。有了这个就不用wsl了，节省了计算机资源，赞。

The generous prosper and are satisfied; those who refresh others will themselves be refreshed

To learn, you must love discipline; it is stupid to hate correction.

---

### 评论 #2 (作者: YQ84572, 时间: 6 months ago)

感谢分享，之前使用这个谷歌的ide的时候就遇到了mcp配置没反应的情况，完美解决了
====================================================================================
祝大佬base多多，vf高高，分享更多小妙招～～
====================================================================================

---

### 评论 #3 (作者: YL96878, 时间: 6 months ago)

我注意到了在谷歌反重力中使用Claude模型配合MCP使用会导致Claude模型中断，在搜索油管后印证了这一点，如果需要使用Claude模型时可以先关闭MCP，使用Gemini模型则没有这个问题，目前没有太好的解决方案，希望谷歌在后续的更新中解决吧。免费的额度很好用，但是反重力是个草台子。

---

