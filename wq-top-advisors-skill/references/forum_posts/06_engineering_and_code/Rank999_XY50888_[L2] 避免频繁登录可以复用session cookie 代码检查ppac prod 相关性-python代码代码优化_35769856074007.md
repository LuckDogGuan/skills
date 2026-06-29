# 避免频繁登录可以复用session cookie 代码检查ppac prod 相关性-python代码代码优化

- **链接**: https://support.worldquantbrain.com[L2] 避免频繁登录可以复用session cookie 代码检查ppac prod 相关性-python代码代码优化_35769856074007.md
- **作者**: XY50888
- **发布时间/热度**: 8 months ago, 得票: 6

## 帖子正文

"""

使用 Cookie 直接访问 WorldQuant BRAIN API 的测试脚本

避免频繁登录，使用现有的 session cookie

"""

import requests

import json

import time

from typing import Dict, Any, Optional

# 优化配置：根据进度动态调整等待时间

# 参考：WorldQuant API调用神器：告别回测中429、502错误

WAIT_TIME_BEFORE_35_PERCENT = 60 # 35%前等待60秒

WAIT_TIME_AFTER_35_PERCENT = 5 # 35%后等待5秒

PROGRESS_THRESHOLD = 0.35 # 进度阈值

class BrainCookieClient:

"""使用 Cookie 访问 BRAIN API 的客户端"""

def__init__(self, cookie_string: str):

"""

初始化客户端

Args:

cookie_string: 完整的 Cookie 字符串

"""

self.base_url=" [https://api.worldquantbrain.com](https://api.worldquantbrain.com) "

self.session=requests.Session()

# 解析 Cookie 字符串

self.cookies=self._parse_cookie_string(cookie_string)

self.session.cookies.update(self.cookies)

# 设置请求头

self.session.headers.update({

'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',

'Accept': 'application/json',

'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',

'Origin': ' [https://platform.worldquantbrain.com](https://platform.worldquantbrain.com) ',

'Referer': ' [https://platform.worldquantbrain.com/](https://platform.worldquantbrain.com/) ',

})

def_get_smart_wait_time(self, retry_after: float, progress: float=None) -> float:

"""

智能计算等待时间，根据进度动态调整

优化策略：

- 回测在35%进度前卡得最久，等待60秒

- 超过35%后很快完成，只需等待5秒

- 这样可以大幅减少GET请求次数，避免429/502错误

Args:

retry_after: API返回的Retry-After时间

progress: 当前进度（0.0-1.0），如果为None则使用retry_after

Returns:

优化后的等待时间

"""

ifprogressisNone:

# 如果没有进度信息，使用API返回的时间

returnretry_after

# 根据进度动态调整

ifprogress<=PROGRESS_THRESHOLD:

# 35%前使用较长等待时间

returnWAIT_TIME_BEFORE_35_PERCENT

else:

# 35%后使用较短等待时间

returnWAIT_TIME_AFTER_35_PERCENT

def_parse_cookie_string(self, cookie_string: str) -> Dict[str, str]:

"""

解析 Cookie 字符串为字典

Args:

cookie_string: Cookie 字符串，格式如 "key1=value1; key2=value2"

Returns:

Cookie 字典

"""

cookies= {}

foritemincookie_string.split(';'):

item=item.strip()

if'='initem:

key, value=item.split('=', 1)

cookies[key.strip()] =value.strip()

returncookies

deftest_connection(self) -> bool:

"""

测试连接是否有效

Returns:

是否连接成功

"""

try:

response=self.session.get(f"{self.base_url}/users/self")

ifresponse.status_code==200:

user_info=response.json()

print(f"✅ 连接成功！用户信息：")

print(f" - 用户ID: {user_info.get('id', 'N/A')}")

print(f" - 用户名: {user_info.get('username', 'N/A')}")

print(f" - 邮箱: {user_info.get('email', 'N/A')}")

returnTrue

else:

print(f"❌ 连接失败，状态码: {response.status_code}")

print(f" 响应: {response.text}")

returnFalse

exceptExceptionase:

print(f"❌ 连接异常: {e}")

returnFalse

defget_alpha_details(self, alpha_id: str) -> Optional[Dict[str, Any]]:

"""

获取 Alpha 详细信息

Args:

alpha_id: Alpha ID

Returns:

Alpha 详细信息字典，失败返回 None

"""

try:

url=f"{self.base_url}/alphas/{alpha_id}"

response=self.session.get(url)

ifresponse.status_code==200:

alpha_data=response.json()

print(f"\n✅ 成功获取 Alpha {alpha_id} 信息：")

print(f" - 名称: {alpha_data.get('name', 'N/A')}")

print(f" - 状态: {alpha_data.get('status', 'N/A')}")

print(f" - 创建时间: {alpha_data.get('dateCreated', 'N/A')}")

# 如果有 regular 代码

if'regular'inalpha_dataandalpha_data['regular']:

code=str(alpha_data['regular'])

print(f" - Regular 代码: {code[:100]}...")

# 如果有性能指标

if'is'inalpha_data:

is_data=alpha_data['is']

print(f" - Sharpe: {is_data.get('sharpe', 'N/A')}")

print(f" - Fitness: {is_data.get('fitness', 'N/A')}")

print(f" - Returns: {is_data.get('returns', 'N/A')}")

returnalpha_data

else:

print(f"❌ 获取 Alpha 失败，状态码: {response.status_code}")

print(f" 响应: {response.text}")

returnNone

exceptExceptionase:

print(f"❌ 获取 Alpha 异常: {e}")

returnNone

defget_user_alphas(self, stage: str="IS", limit: int=10) -> Optional[list]:

"""

获取用户的 Alpha 列表

Args:

stage: Alpha 阶段，"IS" 或 "OS"

limit: 返回数量限制

Returns:

Alpha 列表，失败返回 None

"""

try:

url=f"{self.base_url}/users/self/alphas"

params= {

'stage': stage,

'limit': limit,

'offset': 0

}

response=self.session.get(url, params=params)

ifresponse.status_code==200:

data=response.json()

alphas=data.get('results', [])

print(f"\n✅ 成功获取 {len(alphas)} 个 {stage} Alpha：")

fori, alphainenumerate(alphas[:5], 1): # 只显示前5个

print(f" {i}. {alpha.get('id', 'N/A')} - {alpha.get('name', 'N/A')}")

if'is'inalpha:

print(f" Sharpe: {alpha['is'].get('sharpe', 'N/A')}, "

f"Fitness: {alpha['is'].get('fitness', 'N/A')}")

iflen(alphas) >5:

print(f" ... 还有 {len(alphas) -5} 个")

returnalphas

else:

print(f"❌ 获取 Alpha 列表失败，状态码: {response.status_code}")

print(f" 响应: {response.text}")

returnNone

exceptExceptionase:

print(f"❌ 获取 Alpha 列表异常: {e}")

returnNone

defcheck_prod_correlation(self, alpha_id: str, verbose: bool=True) -> Optional[Dict[str, Any]]:

"""

检查 Alpha 与生产环境的相关性（循环等待）

Args:

alpha_id: Alpha ID

verbose: 是否显示详细信息

Returns:

相关性数据字典，失败返回 None

"""

try:

url=f"{self.base_url}/alphas/{alpha_id}/correlations/prod"

ifverbose:

print(f"\n🔍 检查 Alpha {alpha_id} 的生产相关性...")

# 循环等待检查完成（使用智能等待策略）

retry_count=0

total_wait_time=0

whileTrue:

try:

response=self.session.get(url, timeout=60)

# 检查是否需要等待

if"retry-after"inresponse.headers:

retry_after=float(response.headers["Retry-After"])

# 尝试获取进度信息（如果API返回）

progress=None

try:

data=response.json()

progress=data.get('progress', None)

except:

pass

# 使用智能等待时间

wait_time=self._get_smart_wait_time(retry_after, progress)

ifverboseandretry_count%5==0: # 每5次显示一次

progress_str=f", 进度: {progress*100:.1f}%"ifprogresselse""

print(f" ⏳ 计算中... (已等待 {retry_count} 次, {total_wait_time:.0f}秒{progress_str})")

time.sleep(wait_time)

retry_count+=1

total_wait_time+=wait_time

else:

# 检查完成

break

exceptrequests.exceptions.Timeout:

ifverbose:

print(f" ⚠️ 请求超时，继续重试...")

time.sleep(2)

continue

ifresponse.status_code==200:

# 检查响应内容

ifnotresponse.textorresponse.text.strip() =='':

ifverbose:

print(f"⚠️ 响应为空，该 Alpha 可能不符合计算条件")

returnNone

corr_data=response.json()

ifverbose:

print(f"✅ 成功获取生产相关性数据 (等待 {retry_count} 次, 总计 {total_wait_time:.0f}秒)")

# 显示最高相关性

if'correlations'incorr_dataandcorr_data['correlations']:

top_corr=corr_data['correlations'][0]

print(f" 最高相关性: {top_corr.get('correlation', 'N/A'):.4f}")

print(f" 相关 Alpha: {top_corr.get('alphaId', 'N/A')}")

# 显示统计信息

if'summary'incorr_data:

summary=corr_data['summary']

print(f" 平均相关性: {summary.get('mean', 'N/A')}")

print(f" 最大相关性: {summary.get('max', 'N/A')}")

returncorr_data

else:

ifverbose:

print(f"❌ 获取失败，状态码: {response.status_code}")

print(f" 响应: {response.text[:200]}")

returnNone

exceptExceptionase:

ifverbose:

print(f"❌ 检查异常: {e}")

returnNone

defcheck_power_pool_correlation(self, alpha_id: str, verbose: bool=True) -> Optional[Dict[str, Any]]:

"""

检查 Alpha 与 Power Pool 的相关性（循环等待）

Args:

alpha_id: Alpha ID

verbose: 是否显示详细信息

Returns:

相关性数据字典，失败返回 None

"""

try:

url=f"{self.base_url}/alphas/{alpha_id}/correlations/power-pool"

ifverbose:

print(f"\n🔍 检查 Alpha {alpha_id} 的 Power Pool 相关性...")

# 循环等待检查完成（使用智能等待策略）

retry_count=0

total_wait_time=0

whileTrue:

try:

response=self.session.get(url, timeout=60)

# 检查是否需要等待

if"retry-after"inresponse.headers:

retry_after=float(response.headers["Retry-After"])

# 尝试获取进度信息（如果API返回）

progress=None

try:

data=response.json()

progress=data.get('progress', None)

except:

pass

# 使用智能等待时间

wait_time=self._get_smart_wait_time(retry_after, progress)

ifverboseandretry_count%5==0: # 每5次显示一次

progress_str=f", 进度: {progress*100:.1f}%"ifprogresselse""

print(f" ⏳ 计算中... (已等待 {retry_count} 次, {total_wait_time:.0f}秒{progress_str})")

time.sleep(wait_time)

retry_count+=1

total_wait_time+=wait_time

else:

# 检查完成

break

exceptrequests.exceptions.Timeout:

ifverbose:

print(f" ⚠️ 请求超时，继续重试...")

time.sleep(2)

continue

ifresponse.status_code==200:

# 检查响应内容

ifnotresponse.textorresponse.text.strip() =='':

ifverbose:

print(f"⚠️ 响应为空，该 Alpha 可能不符合计算条件")

returnNone

corr_data=response.json()

ifverbose:

print(f"✅ 成功获取 Power Pool 相关性数据 (等待 {retry_count} 次, 总计 {total_wait_time:.0f}秒)")

# 显示最高相关性

if'correlations'incorr_dataandcorr_data['correlations']:

top_corr=corr_data['correlations'][0]

print(f" 最高相关性: {top_corr.get('correlation', 'N/A'):.4f}")

print(f" 相关 Alpha: {top_corr.get('alphaId', 'N/A')}")

# 显示统计信息

if'summary'incorr_data:

summary=corr_data['summary']

print(f" 平均相关性: {summary.get('mean', 'N/A')}")

print(f" 最大相关性: {summary.get('max', 'N/A')}")

returncorr_data

else:

ifverbose:

print(f"❌ 获取失败，状态码: {response.status_code}")

print(f" 响应: {response.text[:200]}")

returnNone

exceptExceptionase:

ifverbose:

print(f"❌ 检查异常: {e}")

returnNone

defcheck_correlation_smart(self, alpha_id: str, verbose: bool=True) -> Optional[Dict[str, Any]]:

"""

智能检查相关性：自动判断是 PPAC 还是普通 Alpha，然后检查对应的相关性

Args:

alpha_id: Alpha ID

verbose: 是否显示详细信息

Returns:

相关性数据字典，失败返回 None

"""

try:

# 先获取 Alpha 详情

alpha_data=self.get_alpha_details(alpha_id)

ifnotalpha_data:

ifverbose:

print(f"❌ 无法获取 Alpha {alpha_id} 信息")

returnNone

# 判断是否是 PPAC Alpha

tags=alpha_data.get('tags', [])

classifications=alpha_data.get('classifications', [])

is_ppac='PowerPoolSelected'intagsorany(

c.get('id', '').startswith('POWER_POOL:') forcinclassifications

)

ifverbose:

ifis_ppac:

print(f"🎯 检测到 PPAC Alpha，检查 Power Pool 相关性...")

else:

print(f"📝 检测到普通 Alpha，检查生产相关性...")

# 根据类型检查对应的相关性

ifis_ppac:

returnself.check_power_pool_correlation(alpha_id, verbose=verbose)

else:

returnself.check_prod_correlation(alpha_id, verbose=verbose)

exceptExceptionase:

ifverbose:

print(f"❌ 智能检查异常: {e}")

returnNone

defcheck_alpha_submission(self, alpha_id: str, verbose: bool=True, max_retries: int=3) -> Optional[Dict[str, Any]]:

"""

检查 Alpha 是否可以提交（循环等待检查完成）

Args:

alpha_id: Alpha ID

verbose: 是否显示详细信息

max_retries: 最大重试次数

Returns:

检查结果字典，失败返回 None

"""

try:

url=f"{self.base_url}/alphas/{alpha_id}/check"

ifverbose:

print(f"\n🔍 开始检查 Alpha {alpha_id}...")

# 循环等待检查完成（参考 machine_lib.py 的实现）

retry_count=0

whileTrue:

try:

# 增加超时时间到 60 秒

response=self.session.get(url, timeout=60)

# 检查是否需要等待

if"retry-after"inresponse.headers:

wait_time=float(response.headers["Retry-After"])

ifverbose:

print(f" ⏳ 检查进行中，等待 {wait_time:.1f} 秒...")

time.sleep(wait_time)

else:

# 检查完成

break

exceptrequests.exceptions.Timeout:

retry_count+=1

ifretry_count>=max_retries:

print(f"❌ 请求超时，已重试 {max_retries} 次")

returnNone

ifverbose:

print(f" ⚠️ 请求超时，重试 {retry_count}/{max_retries}...")

time.sleep(2)

continue

ifresponse.status_code==200:

check_data=response.json()

# 检查是否有 is 数据

ifcheck_data.get("is", 0) ==0:

print(f"❌ 会话可能已过期，请重新登录")

returnNone

# 获取检查结果

checks=check_data.get("is", {}).get("checks", [])

ifverbose:

print(f"\n✅ 检查完成！")

print(f"\n检查项目结果：")

forcheckinchecks:

name=check.get('name', 'N/A')

result=check.get('result', 'N/A')

value=check.get('value', '')

# 跳过 REGULAR_SUBMISSION

ifname=="REGULAR_SUBMISSION":

continue

# 根据结果显示不同的图标

ifresult=="PASS":

icon="✅"

elifresult=="FAIL":

icon="❌"

elifresult=="WARNING":

icon="⚠️"

else:

icon="🔍"

value_str=f" (值: {value})"ifvalueelse""

print(f" {icon}{name}: {result}{value_str}")

# 判断是否有失败项

has_fail=any(check.get('result') =='FAIL'forcheckinchecks

ifcheck.get('name') !='REGULAR_SUBMISSION')

ifhas_fail:

print(f"\n❌ 检查未通过，不能提交")

else:

print(f"\n✅ 所有检查通过，可以提交！")

returncheck_data

else:

print(f"❌ 检查失败，状态码: {response.status_code}")

print(f" 响应: {response.text}")

returnNone

exceptExceptionase:

print(f"❌ 检查异常: {e}")

returnNone

defsave_alpha_to_file(self, alpha_id: str, filename: str) -> bool:

"""

保存 Alpha 详细信息到文件

Args:

alpha_id: Alpha ID

filename: 保存的文件名

Returns:

是否保存成功

"""

alpha_data=self.get_alpha_details(alpha_id)

ifalpha_data:

try:

withopen(filename, 'w', encoding='utf-8') asf:

json.dump(alpha_data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Alpha 信息已保存到: {filename}")

returnTrue

exceptExceptionase:

print(f"❌ 保存文件失败: {e}")

returnFalse

returnFalse

def main():

"""主测试函数"""

# 你的 Cookie 字符串

cookie_string="""t=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJuSlBMbkpSSmZKWlRJWDZXVzdNdTFncjN2enMwOEFuVyIsImV4cCI6MTc2MDYwNTYzNX0.wxiGzJf6j18x2vL1Mmte8Zafl3NjUS_24A1TpdObtzA; _ga_9RN6WVT1K1=GS2.1.s1760320377$o54$g1$t1760320626$j58$l0$h0; _ga=GA1.1.674320110.1752718343; _fbp=fb.1.1758005574798.841396862864209087"""

# 测试的 Alpha ID

test_alpha_id="npp805xl"

print("="*60)

print("WorldQuant BRAIN Cookie Session 测试")

print("="*60)

# 创建客户端

client=BrainCookieClient(cookie_string)

# 1. 测试连接

print("\n【步骤 1】测试连接...")

ifnotclient.test_connection():

print("\n⚠️ Cookie 可能已过期或无效，请重新获取")

return

# 2. 获取指定 Alpha 信息

print(f"\n【步骤 2】获取 Alpha {test_alpha_id} 详细信息...")

alpha_data=client.get_alpha_details(test_alpha_id)

ifnotalpha_data:

print(f"❌ 无法获取 Alpha {test_alpha_id} 信息")

return

# 3. 判断是否是 PPAC Alpha

print(f"\n【步骤 3】判断 Alpha 类型...")

tags=alpha_data.get('tags', [])

classifications=alpha_data.get('classifications', [])

# 检查是否有 PowerPoolSelected 标签或 POWER_POOL 分类

is_ppac='PowerPoolSelected'intagsorany(

c.get('id', '').startswith('POWER_POOL:') forcinclassifications

)

ifis_ppac:

print(f" 🎯 这是一个 PPAC Alpha")

print(f"\n【步骤 4】检查 Power Pool 相关性...")

ppc_corr=client.check_power_pool_correlation(test_alpha_id, verbose=True)

else:

print(f" 📝 这是一个普通 Regular Alpha")

print(f"\n【步骤 4】检查生产相关性...")

prod_corr=client.check_prod_correlation(test_alpha_id, verbose=True)

# 5. 获取用户的 Alpha 列表

print(f"\n【步骤 5】获取用户的 IS Alpha 列表...")

client.get_user_alphas(stage="IS", limit=10)

print("\n"+"="*60)

print("测试完成！")

print("="*60)

if __name__ == "__main__":

main()

---

## 讨论与评论 (6)

### 评论 #1 (作者: ZL15100, 时间: 7 months ago)

代码不友好

---

### 评论 #2 (作者: ZL15100, 时间: 7 months ago)

代码逻辑打乱了，需要仔细分析修改代码

---

### 评论 #3 (作者: WC53907, 时间: 7 months ago)

大佬，可以先简单介绍下原理吗？

---

### 评论 #4 (作者: ZL49198, 时间: 7 months ago)

大神，能发一下原代码 吗

---

### 评论 #5 (作者: CM48632, 时间: 7 months ago)

避免频繁登录可以复用session cookie，太棒了，解决了不少问题，代码格式，左对齐，这种还是头次见

---

### 评论 #6 (作者: XY50888, 时间: 7 months ago)

好的，谢谢大家，其实是使用的brower_cookie3库，可以从firefox中读取cookie. 例如ace_lib中想使用它，可以加如下的方法：

def get_session_from_browser(s: SingleSession) -> bool:

"""尝试从浏览器获取 BRAIN Cookie，优先 firefox，再尝试 chrome。

返回:

bool: 只要任一浏览器成功注入了有效 token，则返回 True；否则返回 False。

"""

try:

importbrowser_cookie3

exceptImportError:

logging.warning("browser_cookie3 未安装，将使用账号密码登录")

returnFalse

# firefox 放在前面，因为你已经验证 firefox 正常，chrome 可能因为解密密钥问题失败

candidates= [

("firefox", browser_cookie3.firefox),

("chrome", browser_cookie3.chrome),

]

success=False

forname, extractorincandidates:

try:

cj=extractor(domain_name="worldquantbrain.com")

cookies= {cookie.name: cookie.value forcookieincj}

token=cookies.get("t")

iftokenandlen(token) >10:

forcookieincj:

s.cookies.set(cookie.name, cookie.value)

s.headers.update(

{

"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",

"Accept": "application/json",

"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",

"Origin": " [https://platform.worldquantbrain.com](https://platform.worldquantbrain.com) ",

"Referer": " [https://platform.worldquantbrain.com/](https://platform.worldquantbrain.com/) ",

}

)

logging.info(f"使用 {name} 浏览器 Cookie 登录")

success=True

break

else:

logging.warning(f"{name} Cookie token 无效")

exceptExceptionase:

logging.warning(f"从 {name} 提取 Cookie 失败: {e}")

ifnotsuccess:

logging.info("未能从浏览器提取有效 Cookie，将使用账号密码登录")

returnsuccess

---

