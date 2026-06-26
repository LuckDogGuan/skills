# WorldQuant 顾问数据蒸馏、脱敏与分类复用流程指南

本文件夹下提供了一套标准、闭环的量化顾问数据“蒸馏 + 脱敏 + 分类 + 归档”自动化复用流程。用于从微信群聊原始 JSON 语料及官方论坛大容量原始文章（包括海量图片包）中，提取纯技术性量化研究共识，过滤敏感生活话题，并将其归档打包为可直接导入腾讯 IMA 等大模型智能体知识库的 ZIP 压缩包。

---

## 📌 一、核心复用脚本：`distill_pipeline.py`

此目录下的 [distill_pipeline.py](file:///d:/CashFile/weixinCash/王哥蒸馏/复用流程/distill_pipeline.py) 脚本是一键式全流程清洗工具，其主要执行以下任务：

1. **权限初始化**：自动去除目标输出路径下 Windows 历史生成文件可能存在的只读写保护属性（解决 Windows 常见的 Permission Denied 报错）。
2. **群聊记录蒸馏**：读取群聊 JSON 语料，根据触发技术词表进行过滤，在 **15 分钟窗口** 内提取上下文切片，并自动以 **10 分钟无发言间隔** 对对话进行聚类切片。
3. **双重硬过滤脱敏**：
   - 过滤关于**放假、退税、个税、工资、求职实习、毕设/私活、行政、敏感链接**等非技术话题（触发任何一个一票否决敏感词，即整段丢弃，防止带入上下文噪音）。
   - 将敏感主讲人微信号或“王哥”昵称统一替换为正式称谓：`worldquant brain赛博游戏王`。
   - 剔除群聊其他成员名称，统一重命名为 `顾问A`、`顾问B`。
   - 移除群聊中的个人敏感链接与普通 URL（防敏感暴露）。
4. **论坛帖子解码与脱敏**：
   - 读取待导入的论坛文章，正则扫描匹配其内容中夹带的 `search/click?data=` Session 跟踪令牌 URL，通过 **Base64 逆向解码** 自动还原为干净的官方帖子原始 URL，抹除 Session click-data 追踪特征。
   - 正式化文章内部的所有王哥敏感昵称。
5. **论坛图片按需精准剪枝**：
   - 如果直接拷贝论坛整套图片库（如 `images` 目录，通常高达 1.13 GB，包含几千张无关图），打包后体积会过大导致 IMA 等智能体导入超时失败。
   - 脚本会自动正则分析 175 篇论坛 Markdown 中**实际引用的图片文件名**，仅仅提取并物理拷贝这部分有效图（共 800+ 张，约 236 MB），从 1.13 GB 精简了 80%，极大瘦身。
6. **文章自动分类与相对路径重写**：
   - 根据文件名和内容的关键词特征，自动将所有论坛文章分流至 8 个大主题子文件夹。
   - 自动将文章内部的相对图片地址由 `images/` 重写为 `../images/` 以匹配子文件夹相对位置。
7. **生成 Table of Contents 索引**：
   - 自动在 `forum_posts/` 下生成结构化的 [index.md](file:///d:/CashFile/weixinCash/王哥蒸馏/tencent_ima_agent_2026_6-25_14_25/knowledge_base/forum_posts/index.md)，支持点击相对链接直接阅读 8 个板块的所有文章。
8. **更新日志同步与 ZIP 打包**：
   - 自动重写 `distillation_log.md` 的各类计数信息。
   - 将输出文件夹一键打包为 `tencent_ima_agent.zip` 供智能体一键导入。

---

## 🖼️ 二、图片 OCR 推荐与 `nuwa-skill` 图像识别

量化回测或论坛分享的数据中，常夹带大量的图片（例如：算子报错截图、回测 PnL 收益曲线、系统设置、代码截图）。如何高效将它们转换为文本并汇入数据蒸馏中？

### 1. `nuwa-skill` 支持图片识别吗？
* **原生设计**：`nuwa-skill` 的核心逻辑（如 `merge_research.py`、`srt_to_transcript.py` 等脚本）是**文本 centric** 的，主要解析微信聊天文本、字幕 SRT 和 markdown 著作。它本身不包含离线的图像识别代码。
* **大模型多模态能力**：由于 `nuwa-skill` 本质上是一个多智能体（Agent Swarm）协同提炼思维框架的流程，如果运行 `nuwa-skill` 的执行终端具备**多模态大模型**（如 Claude 3.5 Sonnet / GPT-4o / Gemini 1.5 Pro / Qwen2-VL）的 API 接入支持，你完全可以通过提示词引导多模态模型直接“看图说话”。

---

### 2. 业界主流的 OCR 工具推荐与使用方式

为了在数据蒸馏前，将论坛或群聊中的图片转换为格式化的 Markdown 文本，推荐以下几种方案：

#### 方案 A：大模型多模态 API OCR（推荐，效果最佳 🌟）
直接使用 Claude 3.5 Sonnet 或 GPT-4o 等多模态大模型进行图片解析。它不仅能进行文字识别，还能**直接提取出算子公式（转为 LaTeX）和表格（转为 Markdown Table）**，这是传统 OCR 无法做到的。

* **使用示例（Python + GPT-4o API）**：
```python
import base64
import requests

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def ocr_via_llm(image_path, api_key):
    base64_image = encode_image(image_path)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "请做 OCR 识别，如果是代码请用 markdown 代码块包裹；如果是数学公式/因子表达式，请转换为标准 LaTeX 公式；如果是数据，请转为 Markdown 表格形式。只输出识别后的内容，不要有任何多余的解释。"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['message']['content']
```

#### 方案 B：PaddleOCR（离线开源首选，中英文极其精准 🚀）
百度开源的 PaddleOCR 是目前离线部署效果最好的 OCR 框架。对中文、手写体、倾斜表格和繁杂排版有极高的识别率，且运行速度快，适合批量本地离线预处理。

* **安装依赖**：
  ```bash
  pip install paddlepaddle paddleocr
  ```
* **使用示例**：
```python
from paddleocr import PaddleOCR

# 初始化 OCR 引擎（首次运行会自动下载轻量级模型）
ocr = PaddleOCR(use_angle_cls=True, lang="ch") 

def ocr_via_paddle(image_path):
    result = ocr.ocr(image_path, cls=True)
    text_lines = []
    for idx in range(len(result)):
        res = result[idx]
        if not res:
            continue
        for line in res:
            text_lines.append(line[1][0]) # 提取识别的文字内容
    return "\n".join(text_lines)
```

#### 方案 C：EasyOCR（纯 Python 编写，开箱即用 🛠️）
基于 PyTorch 的 EasyOCR 极其易于安装，几乎不会遇到编译错误，支持 80 多种语言。

* **安装依赖**：
  ```bash
  pip install easyocr
  ```
* **使用示例**：
```python
import easyocr

# 初始化 reader，指定中文(ch_sim)和英文(en)
reader = easyocr.Reader(['ch_sim', 'en'])

def ocr_via_easyocr(image_path):
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)
```

---

## 🚀 三、环境准备与依赖安装

若要执行 [distill_pipeline.py](file:///d:/CashFile/weixinCash/王哥蒸馏/复用流程/distill_pipeline.py) 及可选的离线 OCR 功能，请确保本地已配置 Python 3.8+ 运行环境。

### 1. 核心依赖安装（无 OCR）
本复用清洗脚本只使用标准库（如 `json`, `os`, `re`, `shutil`, `zipfile`, `base64`, `urllib` 等），**无需安装任何第三方库**即可直接跑通。

### 2. OCR 拓展依赖安装
若需要集成离线 OCR 脚本，推荐在本地执行：
```bash
# 安装 paddleocr 及 paddlepaddle 框架 (CPU版)
pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## 📝 四、全流程复用运行步骤 (How to Run)

在有新的聊天记录和论坛帖子需要合并蒸馏时，请按照以下标准作业程序执行：

### 第一步：准备源数据
1. **微信聊天记录**：将其导出为规范的 `extracted_chats.json`。格式如下：
   ```json
   [
     {
       "senderUsername": "wxid_7ie6qw9ntyt311",
       "content": "这里是关于 sharpe 计算的一段技术讨论...",
       "createTime": 1719323400,
       "formattedTime": "2026-06-25 14:30:00",
       "type": "文本消息"
     }
   ]
   ```
2. **论坛新帖子**：将抓取到的论坛原始 Markdown 文件放在独立目录下（如 `D:\CashFile\weixinCash\王哥蒸馏\ZS59763`）。
3. **论坛图片**：将所有图片放于图片目录下（如 `D:\CashFile\weixinCash\王哥蒸馏\images`）。

### 第二步：检查并调整路径配置
用编辑器打开复用目录下的 [distill_pipeline.py](file:///d:/CashFile/weixinCash/王哥蒸馏/复用流程/distill_pipeline.py)，修改位于文件头部的参数：
```python
# 修改为你的微信 JSON 文件路径
CHAT_FILE = r"d:/CashFile/weixinCash/王哥蒸馏/extracted_chats.json"      
# 修改为你的论坛 Markdown 文章夹路径
FORUM_SRC_DIR = r"d:/CashFile/weixinCash/王哥蒸馏/ZS59763"              
# 修改为你的海量图片库路径
FORUM_SRC_IMAGES = r"d:/CashFile/weixinCash/王哥蒸馏/images"             
```

### 第三步：一键运行脚本
打开命令行窗口，进入工作目录并运行：
```bash
python "D:\CashFile\weixinCash\王哥蒸馏\复用流程\distill_pipeline.py"
```

### 第四步：检查输出并导入智能体
1. 观察控制台输出日志，确认微信片段过滤数、论坛帖子处理数与图片精简数无误。
2. 确认 `D:\CashFile\weixinCash\王哥蒸馏\` 目录下成功生成了瘦身后的 [tencent_ima_agent.zip](file:///d:/CashFile/weixinCash/王哥蒸馏/tencent_ima_agent.zip)。
3. 在腾讯 IMA 智能体知识库管理页面中，上传该 zip 压缩文件，点击导入，系统即可自动建库并对 8 大分类及 distilled_profiles 建立高精度嵌入索引。
