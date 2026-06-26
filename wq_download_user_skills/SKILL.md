---
name: wq_download_user_skills
description: 增量并发爬取 WorldQuant Brain 论坛 Top 顶级顾问个人主页的发帖、评论、图片本地化以及相对关联引用的流程与逻辑说明
---

# WQ Brain 论坛顶级顾问活动增量并发爬取 Skill

本 Skill 旨在标准化爬取 WorldQuant Brain 社区论坛前 100 名顶级顾问的发帖和回复（最大深度 2 层），实现本地化图片文件以及帖子间的本地相对路径跳转。同时也提供了顾问 ID 与 Zendesk 数字 ID 的自动嗅探与更新机制。

## 📂 目录结构与内容说明

本 Skill 的核心代码与文档归档于以下目录：
* 路径: [wq_download_user_skills/](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/wq_download_user_skills)
  * **[SKILL.md](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/wq_download_user_skills/SKILL.md)**: 本说明文档。
  * **[extract_top100_activity.py](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/wq_download_user_skills/extract_top100_activity.py)**: 并发增量爬虫主控脚本（包含完整的自愈校验、图片本地化、链结重构等逻辑）。

对照表与数据存储目录：
* 对照表路径: [advisor_zendesk_map.json](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/user_activity/advisor_zendesk_map.json)
* 爬取数据路径: [user_activity/](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/user_activity)

---

## 🚀 Zendesk 数字 ID 匹配流程（`advisor_zendesk_map.json`）

Zendesk 社区论坛的个人活动页面必须通过用户专属的**数字 ID** 进行定位（例如顾问 `ZS59763` 对应数字 ID `26858512793111`，访问路径为 `/profiles/26858512793111-ZS59763`）。为避免手动维护对照表，程序中集成了自动的嗅探与补齐机制：

### 1. 自动嗅探 (Regex Sniffing)
在程序运行的所有网页加载过程中（包括搜索页面、主帖内容页面、评论翻页），都会触发 HTML 文本的特征嗅探：
* **匹配模式**：正则模式 `r'/profiles/(\d+)-([A-Z]{2}\d{5})'`。
* **逻辑**：一旦匹配到，程序将数字 ID 和顾问 ID 的对应关系写入内存中的映射表，并立即调用 `save_advisor_zendesk_map()` 持久化到本地的 [advisor_zendesk_map.json](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/user_activity/advisor_zendesk_map.json)。

### 2. 并发缺失解析 (Concurrent ID Resolution)
当启动主爬取任务时：
1. 程序首先对比 `user_rank.md` 中的顾问列表和本地 [advisor_zendesk_map.json](file:///d:/code/WorldQuant%20Brain/consultant/gui/reference/top100Rank-2026Q2/user_activity/advisor_zendesk_map.json) 的键值。
2. 找出所有缺失 Zendesk 数字 ID 的顾问。
3. 利用 `asyncio.Semaphore(5)` 并发限制，同时启动 5 个标签页：
   * 在论坛搜索框输入顾问英文 ID（例如 `TD94100`）。
   * 打开搜索到的前 3 个帖子。
   * 通过帖子页面的 HTML 内容自动触发嗅探，将其数字 ID 解析出来并保存。
4. 解析完毕后，更新后的映射表为接下来的个人主页爬取提供直接访问链接。

---

## 📦 核心可复用函数与调用指南

其他模块或子任务可以导入并直接使用 `extract_top100_activity.py` 中的如下函数：

### 1. `load_advisor_zendesk_map() -> dict`
* **用途**：读取本地的数字 ID 映射 JSON 文件并返回字典。
* **示例**：
  ```python
  from extract_top100_activity import load_advisor_zendesk_map
  m = load_advisor_zendesk_map()
  user_id = m.get("ZS59763")  # 返回 "26858512793111"
  ```

### 2. `sniff_profiles_from_html(html_content: str)`
* **用途**：传入任意页面的 HTML 源码，自动正则嗅探并更新本地映射文件。
* **示例**：
  ```python
  from extract_top100_activity import sniff_profiles_from_html
  html = await page.content()
  sniff_profiles_from_html(html)
  ```

### 3. `fetch_links_from_profile_page(page, user_id: str, adv_id: str) -> tuple`
* **用途**：给定已登录的 Playwright 页面实例和对应 ID，抓取该顾问在个人主页发表的所有帖子链接与评论链接。
* **返回值**：`(links: list, expected_posts: int, expected_comments: int, post_to_comment_ids: dict)`

### 4. `count_local_activity(adv_dir: Path, adv_id: str) -> tuple[int, int]`
* **用途**：扫描指定的本地顾问文件夹，计算实际属于该顾问的主帖数和所有评论数（用作质量校验）。
* **返回值**：`(local_posts, local_comments)`

### 5. `fetch_post_with_cache(page, email, password, url, output_dir, ...)`
* **用途**：具备本地去重缓存与全局缓存的高效文章下载器。如果本地已存在该文件且包含所有所需数据，则跳过网络请求直接返回，极大地减少论坛负载和抓取时间。

---

## 🚀 爬取阶段说明

### 阶段 1: 登录认证与顾问 ID 嗅探
1. **SSO 跨域会话同步**：
   * 脚本在 Playwright 启动时首先访问 `https://support.worldquantbrain.com/hc/zh-cn/signin`，完成跨域单点登录，使当前浏览器上下文在 support 域名下自动带上登录 Cookie。
2. **个人主页游标分页遍历**：
   * 访问 `profiles/{user_id}-{adv_id}?filter_by=posts` (主帖) 和 `filter_by=comments` (回复)。
   * 采用游标分页（`?after=...`），使用 `while` 循环检测并点击 `a.pagination-next-link` 获取下一页。

### 阶段 2: 高并发下载、图片本地化与数据自愈
1. **多线程并发下载 (Semaphore 异步控制)**：
   * 采用 `asyncio.Semaphore(5)` 并发数控制，并发开启 5 个标签页拉取帖子。
2. **二进制图片本地化保存**：
   * 正文和评论中嵌入的图片（`/hc/user_images/...`），脚本会捕获当前登录 Session 进行二进制下载，以 `img_{uuid}.png` 相对引用形式保存到对应顾问的 `images/` 子目录下。
3. **数据自愈与精确校验 (Self-healing)**：
   * 在 Level 1 爬取结束后，统计本地当前顾问目录下的实际帖子数 and 实际评论回复数。
   * 若数量不足（例如评论数少于期望值），则自动对所有相关帖子开启 `force=True` 强制重新拉取（跳过缓存），深度递归补齐，直到达到期望指标。

### 阶段 3: 本地文章引用关联（链接重构）
* 并发拉取结束后，重新扫描已下载的所有本地 `.md` 文件。
* 将其中的 WQ Brain 官方论坛 URL 替换为本地相对路径链接（例如 `../MH33574/【经验分享】_32501258566039.md`），使本地归档库在离线状态下依然可以点击跳转，保持极佳的关联性。

---

## 🛠️ 快速使用指南

### 环境依赖
```powershell
pip install playwright beautifulsoup4
playwright install chromium
```

### 运行脚本
直接在项目根目录下，以 unbuffered 模式执行：
```powershell
python -u reference/top100Rank-2026Q2/wq_download_user_skills/extract_top100_activity.py
```
