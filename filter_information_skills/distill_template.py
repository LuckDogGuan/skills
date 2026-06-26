# -*- coding: utf-8 -*-
"""
WorldQuant 因子挖掘与群聊数据“蒸馏 + 脱敏 + 分类”可复用脚本模板
适用环境：Python 3.x
依赖库：python-docx, pypdf (如有物理文档解析需求时需安装，否则可屏蔽相应函数)
"""

import json
import os
import sys
import re
import shutil
import base64
import urllib.parse
import zipfile
import stat
from collections import Counter

# 强制输出为 UTF-8 避免 Windows 终端乱码
sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 配置参数 (请根据您的本地环境修改)
# ==============================================================================
# 输入源配置
chat_file = r"d:/CashFile/weixinCash/王哥蒸馏/extracted_chats.json"      # 微信聊天 JSON
file_root = r"d:/CashFile/weixinCash/王哥蒸馏/file"                     # 物理资产存放根目录
ref_root = r"d:/code/WorldQuant Brain/consultant/gui/reference"       # 论坛原始 Markdown 目录

# 输出配置
target_folder_name = "tencent_ima_agent_distilled"
target_dir = rf"d:/CashFile/weixinCash/王哥蒸馏/{target_folder_name}"   # 目标输出大文件夹
output_zip = r"d:/CashFile/weixinCash/王哥蒸馏/tencent_ima_agent.zip"    # 最终压缩包生成路径

# 过滤对象设定
target_user = "wxid_7ie6qw9ntyt311"
formal_name = "worldquant brain赛博游戏王"

# ==============================================================================
# 过滤词表 (双重硬拦截列表)
# ==============================================================================
# 触发因子技术词表
keywords = [
    "sharpe", "fitness", "自相关", "decay", "neutralization", "中性", "operator", "算子", "表达式", 
    "datafield", "字段", "pnl", "returns", "turnover", "过拟合", "剪枝", "爬山", "聚类", "相关性",
    "icir", "regular alpha", "superalpha", "super alpha", "zscore", "rank", "ts_", "cross_", "group_",
    "cnhkmcp", "mcp", "单因子", "近年表现", "复现", "相关系数", "回测"
]

# 一票否决生活与敏感话题词表
non_technical_keywords = [
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

# ==============================================================================
# 工具函数
# ==============================================================================
def clear_readonly_attributes(directory):
    """清除 Windows 文件下的只读属性以防 Permission Denied"""
    if not os.path.exists(directory):
        return
    for root, dirs, files in os.walk(directory):
        for f in files:
            fpath = os.path.join(root, f)
            try:
                os.chmod(fpath, stat.S_IWRITE)
            except Exception:
                pass

def sanitize_url(url):
    """提取 Base64 编码的 WorldQuant 论坛原帖链接，剥除 Session 跟踪跟踪"""
    if not url:
        return ""
    if 'search/click?data=' in url:
        try:
            parsed = urllib.parse.urlparse(url)
            query_params = urllib.parse.parse_qs(parsed.query)
            data_param = query_params.get('data', [None])[0]
            if data_param:
                b64_str = data_param.split('--')[0]
                missing_padding = len(b64_str) % 4
                if missing_padding:
                    b64_str += '=' * (4 - missing_padding)
                decoded_bytes = base64.b64decode(b64_str, validate=False)
                url_match = re.search(r'https?://[^\s\x00-\x1f\x7f-\xff]+', decoded_bytes.decode('utf-8', errors='ignore'))
                if url_match:
                    clean_u = url_match.group(0)
                    clean_u = urllib.parse.unquote(clean_u)
                    post_match = re.search(r'https://support\.worldquantbrain\.com/hc/[a-z-]+/community/posts/\d+', clean_u)
                    if post_match:
                        return post_match.group(0)
                    return clean_u
        except Exception:
            pass
    url = urllib.parse.unquote(url)
    if ']' in url:
        url = url.split(']')[0]
    return url

# ==============================================================================
# 执行流程
# ==============================================================================
def main():
    print("====== 1. 初始化目标目录与清除写保护权限 ======")
    clear_readonly_attributes(target_dir)
    
    ima_kb_dir = os.path.join(target_dir, "knowledge_base")
    ima_profile_dir = os.path.join(ima_kb_dir, "distilled_profiles")
    ima_templates_dir = os.path.join(ima_kb_dir, "code_templates")
    ima_docs_dir = os.path.join(ima_kb_dir, "official_docs")
    ima_forum_dir = os.path.join(ima_kb_dir, "forum_posts")
    
    os.makedirs(ima_profile_dir, exist_ok=True)
    os.makedirs(ima_templates_dir, exist_ok=True)
    os.makedirs(ima_docs_dir, exist_ok=True)
    os.makedirs(ima_forum_dir, exist_ok=True)

    print("====== 2. 解析微信群聊记录并进行双重过滤 ======")
    with open(chat_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    messages.sort(key=lambda x: x.get('createTime', 0))

    # 识别触发技术词且排除敏感话题的信息索引
    matched_indices = []
    for idx, m in enumerate(messages):
        if m.get('senderUsername') == target_user:
            content = m.get('content', '')
            if any(kw in content.lower() for kw in keywords):
                if not any(nkw in content for nkw in non_technical_keywords):
                    matched_indices.append(idx)

    # 切片提取 15 分钟前后的对话段落
    filtered_messages = []
    added_ids = set()
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

    print(f"微信历史总消息数: {len(messages)}")
    print(f"技术命中的关联消息数: {len(filtered_messages)}")

    print("====== 3. 对话答疑实录脱敏与格式化生成 ======")
    distilled_convs = []
    distilled_convs.append(f"# 量化优化与回测答疑精选 (Anonymized WQ & Alpha Optimization Q&A - {formal_name})\n")
    distilled_convs.append(f"> [!IMPORTANT]\n> 本文档为经过脱敏与严格技术过滤处理的量化回测与因子优化技术答疑录。已对非公开成员昵称进行了匿名化处理，屏蔽了所有可能含有个人隐私的链接及非公开地址；同时剔除了偏离量化因子主题的非技术交流及生活杂音讨论。\n")

    sender_map = {}
    sender_counter = 1

    def clean_sender(msg):
        username = msg.get('senderUsername')
        if username == target_user:
            return formal_name
        if username not in sender_map:
            nonlocal sender_counter
            sender_map[username] = f"顾问{chr(64 + sender_counter)}" if sender_counter <= 26 else f"顾问{sender_counter}"
            sender_counter += 1
        return sender_map[username]

    # 将消息按 10 分钟或连续性重新归档为对话片段
    groups = []
    current_group = []
    for idx, m in enumerate(messages):
        msg_id = m.get('platformMessageId') or f"{m.get('localId')}_{m.get('createTime')}"
        if msg_id in added_ids:
            if not current_group:
                current_group.append(m)
            else:
                prev_m = current_group[-1]
                time_diff = m.get('createTime', 0) - prev_m.get('createTime', 0)
                # 连续或在 10 分钟以内的合并
                if time_diff <= 10 * 60:
                    current_group.append(m)
                else:
                    groups.append(current_group)
                    current_group = [m]
    if current_group:
        groups.append(current_group)

    segment_count = 0
    kept_messages_count = 0

    for gp in groups:
        # 段落内不能有任何 veto 词
        group_has_veto = False
        for msg in gp:
            if any(nkw in msg.get('content', '') for nkw in non_technical_keywords):
                group_has_veto = True
                break
        if group_has_veto:
            continue
            
        segment_count += 1
        start_time = gp[0].get('formattedTime', 'Unknown Time')
        distilled_convs.append(f"### 技术交流片段 {segment_count} ({start_time.split(' ')[0]})\n")
        
        for msg in gp:
            sender = clean_sender(msg)
            content = msg.get('content', '').strip()
            msg_type = msg.get('type')
            
            # 屏蔽所有原始链接
            content = re.sub(r'https?://[^\s\u4e00-\u9fa5\)]+', '[链接已屏蔽]', content)
            
            if msg_type == '图片消息':
                content = f"[图片消息] (包含回测数据/错误代码/平台设置截图)"
            elif msg_type == '文件消息':
                fname = content.split('/')[-1] if '/' in content else content
                fname = fname.split('\\')[-1] if '\\' in fname else fname
                content = f"[文件消息] {fname}"
            
            if not content or content in ['[表情包]', '[表情]']:
                continue
                
            distilled_convs.append(f"**{sender}**: {content}\n")
            kept_messages_count += 1
        distilled_convs.append("\n---\n")

    # 导出 02-conversations.md
    with open(os.path.join(ima_profile_dir, "02-conversations.md"), "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(distilled_convs))
    print(f"已导出脱敏后的技术对话片段数: {segment_count}，保留消息条数: {kept_messages_count}")

    print("====== 4. 拷贝官方文档、代码文件与论坛原帖 ======")
    # 这里可根据第8步拷贝逻辑执行物理文件和论坛文件移动
    # 模拟拷贝论坛 Markdown
    forum_count = 0
    if os.path.exists(ref_root):
        for root_dir, dirs, files in os.walk(ref_root):
            for f in files:
                if f.endswith('.md') and not f.startswith('README'):
                    try:
                        shutil.copy2(os.path.join(root_dir, f), os.path.join(ima_forum_dir, f))
                        forum_count += 1
                    except Exception:
                        pass
    print(f"已整理论坛帖子数: {forum_count}")

    # 可以在这里扩展拷贝 official_docs 与 code_templates
    # (即使用 shutil.copy2 拷贝 ipynb, py, pdf 等物理文件)

    print("====== 5. 一键生成 zip 压缩包供智能体导入 ======")
    try:
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root_dir, dirs, files in os.walk(target_dir):
                for file in files:
                    fpath = os.path.join(root_dir, file)
                    # 将根目录重命名为标准的 tencent_ima_agent 压缩路径
                    arcname = os.path.join("tencent_ima_agent", os.path.relpath(fpath, target_dir))
                    zipf.write(fpath, arcname)
        print(f"打包成功！输出文件已保存至: {output_zip}")
    except Exception as e:
        print(f"打包 ZIP 发生错误: {e}")

if __name__ == "__main__":
    main()
