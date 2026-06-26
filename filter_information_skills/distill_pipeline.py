# -*- coding: utf-8 -*-
"""
WorldQuant 因子优化与群聊/论坛数据 “清洗 + 脱敏 + 分类 + 打包” 全自动化复用脚本
支持：
1. 微信群聊 JSON 的双列表（触发/否决）时间窗口分段过滤。
2. 敏感词过滤、链接 Session 脱敏、发言人称谓正式化。
3. 论坛文章分类归档（8大板块），图片相对路径自动重构。
4. 论坛文章引用的图片资源精剪枝（只拷贝被引用的图片，极大缩减最终 ZIP 大小）。
5. 自动维护 distillation_log.md 分类计数。
6. 全流程一键打包生成 tencent_ima_agent.zip。
"""

import os
import sys
import re
import json
import shutil
import stat
import base64
import urllib.parse
import zipfile
from collections import Counter

# 强制输出为 UTF-8，防止 Windows 终端中文乱码
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 配置参数 (使用者可根据实际运行环境修改)
# ==============================================================================
# 输入路径
CHAT_FILE = r"d:/CashFile/weixinCash/王哥蒸馏/extracted_chats.json"      # 原始微信群聊 JSON 文件路径
FORUM_SRC_DIR = r"d:/CashFile/weixinCash/王哥蒸馏/ZS59763"              # 待导入的论坛帖子源文件夹 (ZS59763)
FORUM_SRC_IMAGES = r"d:/CashFile/weixinCash/王哥蒸馏/images"             # 论坛原帖对应的海量图片库目录

# 输出路径
TARGET_DIR = r"d:/CashFile/weixinCash/王哥蒸馏/tencent_ima_agent_2026_6-25_14_25" # 输出的 IMA 知识库文件夹路径
OUTPUT_ZIP = r"d:/CashFile/weixinCash/王哥蒸馏/tencent_ima_agent.zip"    # 最终输出的 ZIP 压缩包路径

# 敏感脱敏目标
TARGET_USER = "wxid_7ie6qw9ntyt311"
FORMAL_NAME = "worldquant brain赛博游戏王"

# ==============================================================================
# 双列表过滤词表
# ==============================================================================
# 1. 触发技术词表 (只要主讲人涉及这些词，就截取前后的上下文段落)
KEYWORDS = [
    "sharpe", "fitness", "自相关", "decay", "neutralization", "中性", "operator", "算子", "表达式", 
    "datafield", "字段", "pnl", "returns", "turnover", "过拟合", "剪枝", "爬山", "聚类", "相关性",
    "icir", "regular alpha", "superalpha", "super alpha", "zscore", "rank", "ts_", "cross_", "group_",
    "cnhkmcp", "mcp", "单因子", "近年表现", "复现", "相关系数", "回测"
]

# 2. 一票否决词表 (如果切片窗口内含有以下词，该对话片段直接丢弃，不予保留)
VETO_KEYWORDS = [
    "实习", "养老", "放假", "放什么假", "内部", "北京", "北漂", "退税", "交税", "个人收入", "自掏腰包", "红包", "垫付", 
    "写单", "写毕设", "毕设", "接活", "私活", "杭州", "租房", "借钱", "工资", "奖金", "季度工资", "零头", "税收", 
    "朝九晚六", "11点", "下午5点", "舒服的不谈", "休闲", "头像", "云桌面", "噪音", "微信群", "群里", "群友", 
    "退钱", "答辩", "上学", "学校", "学费", "情侣", "财富自由", "养你", "百事可乐",
    "背调", "签约", "签合同", "合同", "发钱", "理财", "门槛", "起投", "500万", "千禧", "Millennium", "ibkr", 
    "推荐费", "refer", "封号", "账号被封", "被封", "解封", "面试", "面经", "题库", "黑产", "代打", "代练", 
    "出生日期", "身份证", "痛衣", "周边", "礼品", "积分", "助教", "线下", "深圳线下", "福田", "会议号", 
    "腾讯会议", "Zoom", "录播课", "微信公众号", "夸克", "网盘", "新人课", "公开课", "衔接课", "公众号",
    "微信小程序", "小程序", "打钱", "到账", "银行卡", "提现", "出金", "理财产品", "吃尽了wq发展的黑利"
]

# 论坛帖子的分类规则与关键词定义
FORUM_CATEGORIES = {
    "01_super_alpha": {
        "name": "Super Alpha 竞赛与配置 (Super Alpha & SAC)",
        "keywords": ["super alpha", "superalpha", "sa ", "sa竞赛", "sac", "selection", "combo", "择时", "择优"],
        "files": []
    },
    "02_value_factor": {
        "name": "Value Factor 挖掘与提升 (Value Factor & VF)",
        "keywords": ["value factor", "vf", "velue"],
        "files": []
    },
    "03_genius_and_pyramid": {
        "name": "Genius 级别与 Pyramid 晋升 (Genius, Pyramid & Payouts)",
        "keywords": ["genius", "pyramid", "gm", "master", "段位", "晋升", "付款", "薪资分享", "结算"],
        "files": []
    },
    "04_stability_and_robustness": {
        "name": "稳健性与鲁棒性检验 (Stability & Robustness Test)",
        "keywords": ["稳健", "稳定性", "robust", "pnl", "os表现", "过拟合", "近年表现", "自相关"],
        "files": []
    },
    "05_datafields_and_operators": {
        "name": "数据字段与算子研究 (Datafields & Operators)",
        "keywords": ["operator", "datafield", "dataset", "字段", "新闻", "news", "macro", "signed_power", "inst_pnl", "操作符", "vector", "amihud", "数据源"],
        "files": []
    },
    "06_engineering_and_code": {
        "name": "工程优化与回测代码 (Quant Engineering & Code)",
        "keywords": ["code", "优化", "代码", "mysql", "redis", "clickhouse", "sqlite", "多线程", "多进程", "协程", "api", "提交", "缓存", "streamlit", "vscode", "nvim", "插件", "网页监控", "脚本"],
        "files": []
    },
    "07_newbie_and_career": {
        "name": "顾问成长、日常与经验分享 (Career, Diaries & Meme)",
        "keywords": ["新人", "新手", "建议", "日常", "日记", "经历", "心得", "收获", "困惑", "职业", "收入分享", "避坑", "十大qa", "问答", "meme", "漫画", "喜乐会", "春节"],
        "files": []
    },
    "08_general_research": {
        "name": "其他综合研究与分享 (General Quant Research)",
        "keywords": [], # 默认兜底分类
        "files": []
    }
}

# ==============================================================================
# 通用辅助工具函数
# ==============================================================================
def remove_readonly(path):
    """移除文件的只读属性，防止 Windows 环境下 Permission Denied 报错"""
    if os.path.exists(path):
        os.chmod(path, stat.S_IWRITE)

def clear_readonly_attributes(directory):
    """递归清除目录内所有文件的只读属性"""
    if not os.path.exists(directory):
        return
    for root, dirs, files in os.walk(directory):
        for f in files:
            remove_readonly(os.path.join(root, f))

def sanitize_url(url):
    """自动还原 Base64 编码的 WorldQuant 论坛链接，剥离 Session 追踪参数"""
    if not url:
        return ""
    if 'search/click?data=' in url:
        try:
            parsed = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed.query)
            data_param = query_params.get('data', [None])[0]
            if data_param:
                # 剔除 HMAC 校验后缀
                b64_str = data_param.split('--')[0]
                # 自动补全 Base64 填充
                missing_padding = len(b64_str) % 4
                if missing_padding:
                    b64_str += '=' * (4 - missing_padding)
                decoded_bytes = base64.b64decode(b64_str, validate=False)
                decoded_str = decoded_bytes.decode('utf-8', errors='ignore')
                url_match = re.search(r'https?://[^\s\x00-\x1f\x7f-\xff]+', decoded_str)
                if url_match:
                    clean_u = url_match.group(0)
                    clean_u = urllib.parse.unquote(clean_u)
                    # 匹配社区帖子标准 URL 结构
                    post_match = re.search(r'https://support\.worldquantbrain\.com/hc/[a-z-]+/community/posts/\d+', clean_u)
                    if post_match:
                        return post_match.group(0)
                    return clean_u
        except Exception as e:
            pass
    # 兜底 URL 解码
    url = urllib.parse.unquote(url)
    if ']' in url:
        url = url.split(']')[0]
    return url

# ==============================================================================
# 数据清洗与蒸馏流程
# ==============================================================================
def process_chat_data(chat_path, profile_dir):
    """对微信群聊 JSON 语料进行双重过滤、脱敏与按时间聚类导出"""
    print(f" -> 正在解析微信聊天语料: {chat_path}")
    if not os.path.exists(chat_path):
        print(f" [!] 未找到聊天语料文件: {chat_path}，跳过此步。")
        return 0, 0

    with open(chat_path, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    
    # 确保升序排列
    messages.sort(key=lambda x: x.get('createTime', 0))

    # 第一阶段：识别命中技术词且没有被一票否决的信息索引
    matched_indices = []
    for idx, m in enumerate(messages):
        if m.get('senderUsername') == TARGET_USER:
            content = m.get('content', '')
            if any(kw in content.lower() for kw in KEYWORDS):
                if not any(nkw in content for nkw in VETO_KEYWORDS):
                    matched_indices.append(idx)

    # 第二阶段：以 15 分钟窗口进行时间切片
    added_ids = set()
    filtered_messages = []
    for idx, m in enumerate(messages):
        m_time = m.get('createTime', 0)
        in_window = False
        for midx in matched_indices:
            if abs(messages[midx].get('createTime', 0) - m_time) <= 15 * 60:
                in_window = True
                break
        if in_window:
            msg_id = m.get('platformMessageId') or f"{m.get('localId')}_{m.get('createTime')}"
            if msg_id not in added_ids:
                filtered_messages.append(m)
                added_ids.add(msg_id)

    # 第三阶段：再次精细化归并，并按 10 分钟无发言间隔切分成独立“技术交流片段”
    groups = []
    current_group = []
    for m in messages:
        msg_id = m.get('platformMessageId') or f"{m.get('localId')}_{m.get('createTime')}"
        if msg_id in added_ids:
            if not current_group:
                current_group.append(m)
            else:
                prev_m = current_group[-1]
                if m.get('createTime', 0) - prev_m.get('createTime', 0) <= 10 * 60:
                    current_group.append(m)
                else:
                    groups.append(current_group)
                    current_group = [m]
    if current_group:
        groups.append(current_group)

    # 导出脱敏的 Q&A 记录文件 (02-conversations.md)
    distilled_convs = []
    distilled_convs.append(f"# 量化优化与回测答疑精选 (Anonymized WQ & Alpha Optimization Q&A - {FORMAL_NAME})\n")
    distilled_convs.append(
        "> [!IMPORTANT]\n"
        "> 本文档为经过脱敏与严格技术过滤处理的量化回测与因子优化技术答疑录。"
        "已对非公开成员昵称进行了匿名化处理，屏蔽了所有可能含有个人隐私的链接及非公开地址；同时剔除了偏离量化因子主题的非技术交流及生活杂音讨论。\n"
    )

    sender_map = {}
    sender_counter = 1
    segment_count = 0
    kept_messages_count = 0

    for gp in groups:
        # 对话片段中任何一条发言含有 veto 词，则放弃整段，防止带入上下文噪音
        group_has_veto = False
        for msg in gp:
            if any(nkw in msg.get('content', '') for nkw in VETO_KEYWORDS):
                group_has_veto = True
                break
        if group_has_veto:
            continue

        segment_count += 1
        start_time = gp[0].get('formattedTime', 'Unknown Time')
        distilled_convs.append(f"### 技术交流片段 {segment_count} ({start_time.split(' ')[0]})\n")

        for msg in gp:
            # 称谓转换
            raw_sender = msg.get('senderUsername')
            if raw_sender == TARGET_USER:
                sender = FORMAL_NAME
            else:
                if raw_sender not in sender_map:
                    sender_map[raw_sender] = f"顾问{chr(64 + sender_counter)}" if sender_counter <= 26 else f"顾问{sender_counter}"
                    sender_counter += 1
                sender = sender_map[raw_sender]

            content = msg.get('content', '').strip()
            msg_type = msg.get('type')

            # 去除普通的敏感 URL，保护隐私
            content = re.sub(r'https?://[^\s\u4e00-\u9fa5\)]+', '[链接已屏蔽]', content)

            if msg_type == '图片消息':
                content = "[图片消息] (包含回测数据/错误代码/平台设置截图)"
            elif msg_type == '文件消息':
                fname = content.split('/')[-1] if '/' in content else content
                fname = fname.split('\\')[-1] if '\\' in fname else fname
                content = f"[文件消息] {fname}"

            if not content or content in ['[表情包]', '[表情]']:
                continue

            distilled_convs.append(f"**{sender}**: {content}\n")
            kept_messages_count += 1
        distilled_convs.append("\n---\n")

    output_path = os.path.join(profile_dir, "02-conversations.md")
    remove_readonly(output_path)
    with open(output_path, 'w', encoding='utf-8') as f_out:
        f_out.write("\n".join(distilled_convs))

    print(f" -> 微信数据蒸馏完成。生成了 {segment_count} 个技术交流片段，共计 {kept_messages_count} 条发言。")
    return segment_count, kept_messages_count

# ==============================================================================
# 论坛原帖的拷贝、脱敏与分类整理流程
# ==============================================================================
def classify_and_sanitize_forums(forum_src, forum_dest_dir, images_src_dir):
    """
    1. 从原始 ZS59763 中复制并过滤脱敏所有的论坛 MD 文章。
    2. 对内容中的 `search/click?data=` 链接进行解码，还原干净地址。
    3. 识别文章引用的图片资源，精准拷贝这部分图片，从而对 images/ 目录进行按需精简。
    4. 分类文章至 8 个主题子文件夹下，自动适配 `../images/` 路径。
    5. 生成带有点击跳转的 index.md 总索引。
    """
    print(f" -> 开始处理论坛文章目录: {forum_src}")
    if not os.path.exists(forum_src):
        print(f" [!] 未找到论坛帖子源文件夹: {forum_src}，跳过此步。")
        return 0, 0

    forum_images_dest = os.path.join(forum_dest_dir, "images")
    os.makedirs(forum_images_dest, exist_ok=True)

    # 1. 扫描待处理的文章文件列表
    raw_files = [f for f in os.listdir(forum_src) if f.endswith('.md') and not f.startswith('README')]
    print(f"    共扫描到 {len(raw_files)} 篇论坛 Markdown 原始文件。")

    # 准备图片检测正则与分类目标创建
    image_pattern = re.compile(r'\(images/([^\)]+)\)')
    html_img_pattern = re.compile(r'src=["\']images/([^"\']+)["\']')
    referenced_images = set()

    # 初始化分类计数
    for cat_id in FORUM_CATEGORIES.keys():
        os.makedirs(os.path.join(forum_dest_dir, cat_id), exist_ok=True)
        FORUM_CATEGORIES[cat_id]["files"] = []

    processed_count = 0

    # 2. 开始逐篇脱敏、提取图片关联、拷贝并分类
    for fname in raw_files:
        src_path = os.path.join(forum_src, fname)
        with open(src_path, 'r', encoding='utf-8', errors='ignore') as f_in:
            content = f_in.read()

        # 2.1 脱敏处理
        # 还原论坛 Session 跟踪 URL
        urls = re.findall(r'https?://support\.worldquantbrain\.com/hc/[^\s\)\"\'>]+', content)
        for u in set(urls):
            if 'search/click?data=' in u:
                clean_u = sanitize_url(u)
                if clean_u:
                    content = content.replace(u, clean_u)

        # 转换敏感主讲人名字
        content = content.replace(TARGET_USER, FORMAL_NAME)
        content = content.replace("王哥", FORMAL_NAME)

        # 2.2 扫描记录引用的图片文件名
        for img in image_pattern.findall(content):
            referenced_images.add(img)
        for img in html_img_pattern.findall(content):
            referenced_images.add(img)

        # 2.3 判断分类主题
        fname_lower = fname.lower()
        content_lower = content.lower()
        selected_cat = "08_general_research"  # 默认兜底分类

        for cat_id, cat_info in FORUM_CATEGORIES.items():
            if cat_id == "08_general_research":
                continue
            # 根据文件名/内容关键词定位
            if any(kw in fname_lower for kw in cat_info["keywords"]) or any(kw in content_lower for kw in cat_info["keywords"]):
                selected_cat = cat_id
                break

        # 2.4 重构相对路径并拷贝至子文件夹
        # 子文件夹中的文件指向外部 images 目录，所以 images/ 需要重构为 ../images/
        content = content.replace('](images/', '](../images/')
        content = content.replace('src="images/', 'src="../images/')
        content = content.replace("src='images/", "src='../images/")

        dest_path = os.path.join(forum_dest_dir, selected_cat, fname)
        remove_readonly(dest_path)
        with open(dest_path, 'w', encoding='utf-8') as f_out:
            f_out.write(content)

        FORUM_CATEGORIES[selected_cat]["files"].append(fname)
        processed_count += 1

    print(f" -> 论坛文章处理并分类完成，成功处理 {processed_count} 篇文章。")

    # 3. 对被引用的图片执行按需物理拷贝（精简 images 目录）
    copied_images_count = 0
    if os.path.exists(images_src_dir):
        print(f" -> 开始对引用图片进行过滤与物理拷贝，总引用独立图片数: {len(referenced_images)}")
        for img_name in referenced_images:
            # 去除可能的 url 编码或 query 参数
            clean_img_name = urllib.parse.unquote(img_name).split('?')[0]
            img_src_path = os.path.join(images_src_dir, clean_img_name)
            img_dest_path = os.path.join(forum_images_dest, clean_img_name)
            
            if os.path.exists(img_src_path):
                remove_readonly(img_dest_path)
                shutil.copy2(img_src_path, img_dest_path)
                copied_images_count += 1
        print(f" -> 精剪枝图片拷贝完成。仅保留并拷贝了 {copied_images_count} 张物理图片到目录中。")
    else:
        print(f" [!] 未找到图片源文件夹: {images_src_dir}，跳过图片拷贝。")

    # 4. 生成 index.md 总分类索引
    index_file = os.path.join(forum_dest_dir, "index.md")
    index_content = [
        "# WorldQuant Brain 论坛精选分类索引 (Forum Posts Index)\n",
        "> 本文档为 WorldQuant Brain 官方论坛精选文章与顾问经验分享的分类目录结构。所有文章均已进行脱敏处理，去除了个人 Session 跟踪参数及敏感隐私，并在知识库中按照功能主题分类存储，以便快速检索和调用。\n"
    ]

    for cat_id, cat_info in sorted(FORUM_CATEGORIES.items()):
        files_list = cat_info["files"]
        if not files_list:
            continue
        index_content.append(f"## {cat_info['name']} (共 {len(files_list)} 篇)\n")
        for f in sorted(files_list):
            rel_path = f"{cat_id}/{f}"
            # 提取干净的文章标题（剥除 Commented 等前缀与哈希后缀）
            title = f.replace('[Commented] ', '').replace('[L2] ', '').replace('.md', '').split('_')[0]
            index_content.append(f"- **[{title}]({rel_path})**")
        index_content.append("")

    remove_readonly(index_file)
    with open(index_file, 'w', encoding='utf-8') as f_idx:
        f_idx.write("\n".join(index_content))
    print(" -> 分类索引页面 index.md 生成成功。")

    return processed_count, copied_images_count

# ==============================================================================
# 更新日志维护与最终 ZIP 压缩打包
# ==============================================================================
def update_distillation_log(log_path, chat_stats, forum_stats):
    """自动计算分类状态，刷新本地 distillation_log.md 对应目录描述与状态统计"""
    if not os.path.exists(log_path):
        print(f" [!] 未找到日志模版文件: {log_path}，跳过日志同步。")
        return

    print(" -> 正在自动同步并改写 distillation_log.md 统计数据...")
    remove_readonly(log_path)
    with open(log_path, 'r', encoding='utf-8') as f:
        log_content = f.read()

    # 1. 重写文章数量
    # 用确定性块区间匹配替换旧大纲描述
    start_marker = "> - **`forum_posts/`**"
    end_marker = "## 导入状态"
    
    start_idx = log_content.find(start_marker)
    end_idx = log_content.find(end_marker)

    if start_idx != -1 and end_idx != -1:
        new_catalog_text = (
            "> - **`forum_posts/`** (论坛精选文章分类目录)：\n"
            ">   - `index.md` (总分类索引文件，包含各板块文章大纲)\n"
            f">   - `01_super_alpha/` (Super Alpha 竞赛与配置，共计 {len(FORUM_CATEGORIES['01_super_alpha']['files'])} 篇)\n"
            f">   - `02_value_factor/` (Value Factor 挖掘与提升，共计 {len(FORUM_CATEGORIES['02_value_factor']['files'])} 篇)\n"
            f">   - `03_genius_and_pyramid/` (Genius级别与Pyramid晋升，共计 {len(FORUM_CATEGORIES['03_genius_and_pyramid']['files'])} 篇)\n"
            f">   - `04_stability_and_robustness/` (稳健性与鲁棒性检验，共计 {len(FORUM_CATEGORIES['04_stability_and_robustness']['files'])} 篇)\n"
            f">   - `05_datafields_and_operators/` (数据字段与算子研究，共计 {len(FORUM_CATEGORIES['05_datafields_and_operators']['files'])} 篇)\n"
            f">   - `06_engineering_and_code/` (工程优化与回测代码，共计 {len(FORUM_CATEGORIES['06_engineering_and_code']['files'])} 篇)\n"
            f">   - `07_newbie_and_career/` (顾问成长、日常与经验分享，共计 {len(FORUM_CATEGORIES['07_newbie_and_career']['files'])} 篇)\n"
            f">   - `08_general_research/` (其他综合研究与分享，共计 {len(FORUM_CATEGORIES['08_general_research']['files'])} 篇)\n\n"
        )
        log_content = log_content[:start_idx] + new_catalog_text + log_content[end_idx:]

    # 2. 统计数值同步更新（正则查找）
    total_forums = sum(len(cat['files']) for cat in FORUM_CATEGORIES.values())
    log_content = re.sub(
        r'- \*\*提取并脱敏的官方论坛链接数\*\*: \d+ 篇',
        f'- **提取并脱敏的官方论坛链接数**: {total_forums} 篇',
        log_content
    )
    log_content = re.sub(
        r'- \*\*量化过滤与严格脱敏后聊天记录条数\*\*: \d+',
        f'- **量化过滤与严格脱敏后聊天记录条数**: {chat_stats[1]}',
        log_content
    )

    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)
    print(" -> distillation_log.md 日志统计同步刷新完毕。")

def zip_target_package(source_dir, output_zip_path):
    """将输出大文件夹一键压缩为 zip 文件，保证根目录名为 tencent_ima_agent"""
    print(f" -> 开始构建 ZIP 压缩归档包至: {output_zip_path} ...")
    remove_readonly(output_zip_path)
    
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root_dir, dirs, files in os.walk(source_dir):
                for file in files:
                    fpath = os.path.join(root_dir, file)
                    # 将根路径重新映射为 tencent_ima_agent
                    arcname = os.path.join("tencent_ima_agent", os.path.relpath(fpath, source_dir))
                    zipf.write(fpath, arcname)
        print(" -> ZIP 归档包压缩封装成功！")
    except Exception as e:
        print(f" [!] 归档打包过程发生错误: {e}")

# ==============================================================================
# 主入口
# ==============================================================================
def main():
    print("======================================================================")
    print("       WorldQuant 因子挖掘与群聊数据自动蒸馏、脱敏与分类流水线         ")
    print("======================================================================")

    # 1. 权限与输出目录初始化
    print("\n[Step 1] 初始化输出工作空间...")
    clear_readonly_attributes(TARGET_DIR)
    
    kb_distilled_profiles = os.path.join(TARGET_DIR, "knowledge_base", "distilled_profiles")
    kb_forum_posts = os.path.join(TARGET_DIR, "knowledge_base", "forum_posts")
    os.makedirs(kb_distilled_profiles, exist_ok=True)
    os.makedirs(kb_forum_posts, exist_ok=True)

    # 2. 微信群聊记录脱敏过滤
    print("\n[Step 2] 执行微信对话记录技术蒸馏与敏感剔除...")
    chat_stats = process_chat_data(CHAT_FILE, kb_distilled_profiles)

    # 3. 论坛文章分类与图片精简物理拷贝
    print("\n[Step 3] 执行论坛原帖脱敏、8大主题分类归档与图片按需剪枝拷贝...")
    forum_stats = classify_and_sanitize_forums(FORUM_SRC_DIR, kb_forum_posts, FORUM_SRC_IMAGES)

    # 4. 日志计数修正
    print("\n[Step 4] 执行本地蒸馏日志同步更新...")
    log_path = os.path.join(TARGET_DIR, "distillation_log.md")
    update_distillation_log(log_path, chat_stats, forum_stats)

    # 5. 一键归档打包
    print("\n[Step 5] 执行最终导入包 ZIP 打包封装...")
    zip_target_package(TARGET_DIR, OUTPUT_ZIP)

    print("\n======================================================================")
    print(" 流水线全自动流转完毕！请在腾讯 IMA 平台直接上传对应的 zip 压缩包使用。 ")
    print("======================================================================")

if __name__ == "__main__":
    main()
