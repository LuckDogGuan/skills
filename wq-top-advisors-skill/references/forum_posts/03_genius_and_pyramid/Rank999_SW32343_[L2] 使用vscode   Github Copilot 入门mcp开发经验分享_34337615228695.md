# 使用vscode +  Github Copilot 入门mcp开发经验分享

- **链接**: https://support.worldquantbrain.com[L2] 使用vscode   Github Copilot 入门mcp开发经验分享_34337615228695.md
- **作者**: SW32343
- **发布时间/热度**: 10 months ago, 得票: 13

## 帖子正文

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
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
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
NWS_API_BASE = " [https://api.weather.gov](https://api.weather.gov) "
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

## 讨论与评论 (2)

### 评论 #1 (作者: SW32343, 时间: 10 months ago)

在platform_functions.py 入口函数改成

if __name__ == "__main__":

try:

print("WorldQuant BRAIN MCP Server Starting...", file=sys.stderr)

mcp.run(transport='stdio')

except Exception as e:

print(f"Failed to start MCP server: {e}", file=sys.stderr)

sys.exit(1)

mcp.json：

{

"servers": {

"worldquant-brain-platform": {

"command": "D:\anaconda3\python.exe",

"args": [

"D:\anaconda3\Lib\site-packages\cnhkmcp\untracked\platform_functions.py"

],

}

}

}

就可以正常使用了，


> [!NOTE] [图片 OCR 识别内容]
> XTC)
> b(
> 亚佯()
> 旦a)
> 牧(3)
> U
> C{[
> 资源管理器
> {} mcpijson
> platform_functions:py 5
> USeT
> configjson
> 十S'  1 X
> MCP
> VSCode
> mcpJson
> VsCode
> 获取所有的operator
> SerVers
> mcpijson
> V正在运行|停止 |重启 |40  个工具 |更多。
> cnhkmcp
> Shortcutlnk
> "worldquant-brain-platform"
> 己运行
> operators
> worldquant-
> Command"
> "0: | lanaconda3 | Ipython.exe
> brain-platform (MCP 服务器)
> 'args"
> "0: | lanaconda3 |ILiblIsite-packages | Icnhkmcp | luntracked | Iplatform_functions .py"
> 所有可用的 operator (算子)  如下。部分示例:
> add: 加法。支持多个输入,
> 可过滤 NaN 为
> 10
>  multiply: 乘法。支持多个输入
> filter 可过滤
> NaN 为1。
> n
> sign: 符号函数
> 返回输入的符号
> subtract: 减法
> 支持 filter。
> log: 自然对数。
> maxlmin: 最大/最小值。支持多个输入
> abs: 绝对值。
> sigmoid/tanh: 激活函数。
> divide: 除法。
> powerlsigned_power: 幂运算。
> orland/not: 逻辑运算。
> tS_corr/ts_Zscore/ts_mean/ts_std_dev /ts_sum/ts_r
> ankts
> delay 等:  时序相关算子。
> rank/scale/normalize/quantile/zscore: 横截面相
> 关算子。
> group_mean/group_rank/group_neutralize 等
> 分组相关算子。
> reduce_avg/reduce_max/reduce_min/reduce_SU
> m 等:  归约算子。
> 己更改2个文件
> mcPjson .vscode
> platform_functions Py D:lanaconda3lLiblsite-
> 0添加上下文
> IcpJSOn
> ~加
> 凸(#]
> CR(
> (0
> get
> flter


---

### 评论 #2 (作者: WC83400, 时间: 8 months ago)

谢谢大佬的分享，对新顾问很实用!

---

