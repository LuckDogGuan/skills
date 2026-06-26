# 【骑象人】别再手动点了！一键打开上百个Alpha详情页的神器分享代码优化

- **链接**: [Commented] 【骑象人】别再手动点了一键打开上百个Alpha详情页的神器分享代码优化.md
- **作者**: KK88739
- **发布时间/热度**: 8个月前, 得票: 22

## 帖子正文

Hello～各位小伙伴👋

是不是经常遇到这样的场景：
我们把 Alpha 缓存在本地数据库或 CSV 文件中，筛选出一大批可提交的 Alpha 后，却卡在一个尴尬的步骤——
👉 得一个个复制 AlphaID、手动拼链接、再一个个打开详情页面……
 **费时又枯燥，完全浪费生产力！**

**骑象人出手了！** 
经过多次测试与优化，我开发了一个  **超轻量级小工具页面** ：
只需输入所有的 AlphaID，一键批量打开所有详情页！
再也不用繁琐操作，效率直接起飞

工具获取方式：
👉 [https://pan.quark.cn/s/b996e1b6f9e6](https://pan.quark.cn/s/b996e1b6f9e6%C2%A0)   
或者自己动手，将下方代码保存为  **`openDetail.html`**  文件即可使用。

详细操作手册请见帖子末尾，简单七步即可搞定～

如果这个工具对你有帮助，
 **请多多点赞、收藏、转发支持一下骑象人！** 
你的鼓励，是我继续优化和开发实用工具的最大动力

<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8" />
    <title>批量打开 Alpha 页面</title>
    <!-- 引入 Element-UI 样式 -->
    <link rel="stylesheet" href=" [https://unpkg.com/element-ui/lib/theme-chalk/index.css](https://unpkg.com/element-ui/lib/theme-chalk/index.css) ">
    <style>
        body {
            margin: 0;
            background: #f5f7fa;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }
        .page-container {
            padding: 24px;
            min-height: 100vh;
        }
        .card {
            max-width: 700px;
            margin: auto;
        }
        .card-title {
            font-size: 16px;
            font-weight: bold;
            color: #303133;
        }
    </style>
</head>
<body>
<div id="app" class="page-container">
    <el-card class="card" shadow="hover">
        <div slot="header" class="clearfix">
            <span class="card-title">批量打开 Alpha 页面</span>
        </div>

<el-form label-position="top">
            <el-form-item label="请输入参数（每行一个）">
                <el-input
                        type="textarea"
                        :rows="6"
                        v-model="inputText"
                        placeholder="请输入参数，每行一个"
                ></el-input>
            </el-form-item>

<el-form-item>
                <el-button type="primary" icon="el-icon-link" @click="openPages">
                    打开页面
                </el-button>
                <el-button type="warning" icon="el-icon-delete" @click="clearInput">
                    清空
                </el-button>
            </el-form-item>
        </el-form>
    </el-card>
</div>

<!-- 引入 Vue2 -->
<script src=" [https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script](https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js%22></script) >
<!-- 引入 Element-UI -->
<script src=" [https://unpkg.com/element-ui/lib/index.js"></script](https://unpkg.com/element-ui/lib/index.js%22></script) >
<script>
    new Vue({
        el: '#app',
        data() {
            return {
                inputText: ''
            }
        },
        methods: {
            openPages() {
                const params = this.inputText
                    .split("\n")
                    .map(p => p.trim())
                    .filter(p => p.length > 0);

if (params.length === 0) {
                    this.$message.warning("请输入至少一个参数！");
                    return;
                }

this.$message.success(`成功打开 ${params.length} 个页面`);
                params.forEach(p => {
                    const url = ` [https://platform.worldquantbrain.com/alpha/${p}`](https://platform.worldquantbrain.com/alpha/${p}`) ;
                    window.open(url, "_blank");
                });
            },
            clearInput() {
                this.inputText = "";
                this.$message.info("输入已清空");
            }
        }
    });
</script>
</body>
</html>

以下是操作手册

1. chrome浏览器打开设置


> [!NOTE] [图片 OCR 识别内容]
> 秕昂打开 Alpha 页_
> WorldQuant BRAIN
> 设.
> Chrome
> chrome: IIsettings
> New
> 窳
> 9
> 验证身份
> 有新版 Chrome 可用
> 器 |口 TDH
> 口个
> 口学习
> 口 工具
> D 待处理
> temp
> 设置
> 搜索设置
> 您与 Google
> 您与 Google
> 自动填充和密码
> hhbjvb
> 关闭
> 重新叠录
> 隐私与安全
> 需重新登录才能继续同步
> 性能
> 同步功能和 Google 服务
> 外观
> 自定义您的 Chrome 个人资料
> 搜索引擎
> 导入书签和设置
> 默认浏览器
> 起始页面
> 刘
> 语言
> 下载内"
> 卞
> 无障碍
> 系统
> 重置设置
> 扩展程序
> 区
> 关于 Chrome


1. 隐私与安全，网站设置


> [!NOTE] [图片 OCR 识别内容]
> 秕昂打开 Alpha 页_
> WorldQuant BRAIN
> 设翟
> 隐私与安全
> Chrome
> Chrome:Ilsettingslprivacy
> Am
> 9
> 验证身份
> 有新版 Chrome 可用
> 器 |口 TDH
> 口个
> 0学习
> 0 工具
> D 待处理
> temp
> 设置
> 搜索设置
> 您与 Google
> 开始使用
> 不用了
> 自动填充和密码
> 隐私与安全
> 安全检查
> 性能
> 外观
> Chrome 找到了一些安全建议需要您审核
> 前往"安全检查"页面
> 密码
> 搜索引擎
> 默认浏览器
> 隐私与安全
> 起始页面
> 副除浏览数据
> 剐除历史记录。 Cookie 。 缓存内容及其他数据
> 刘
> 语言
> 隐私保护指南
> 下载内"
> 检查重要的隐私控制设置和安全控件
> 卞
> 无障碍
> 第三方 Cookie
> 允许使用第三方 Cookie
> 系统
> 广告隐私权设置
> 重置设置
> 自定义网站可用来向您投放广告的信息
> 扩展程序
> 区
> 安全
> 安全浏览 (防范危险网站)  和其他安全设置
> 关于 Chrome
> 网站设置
> 控制网站可以使用和显示的信息 (位置信息。摄像头。弹出式商口等)


1. 弹出窗口与重定向


> [!NOTE] [图片 OCR 识别内容]
> 秕昂打开 Alpha 页_
> WorldQuant BRAIN
> 设翟
> 网站设翟
> Chrome
> Chrome:Ilsettingslcontent
> New
> 9
> 验证身份
> 有新版 Chrome 可用
> 器 |口 TDH
> 口个
> 口学习
> 口 工具
> D 待处理
> temp
> 设置
> 搜索设置
> 通知
> 您与 Google
> 收起不篱要昀请求 (推荐)
> 自动填充和密码
> 嵌入式内容
> 网站可以请求使用其保存的与您相关的信息
> 隐私与安全
> 性能
> 更多权限
> 外观
> 内容
> 搜索引擎
> 第三方 Cookie
> 默认浏览器
> 允许使用第三方 Cookie
> 起始页面
> JavaScript
> 网站可以使用 JavaScript
> 刘
> 语言
> 下载内"
> 网站可以显示图片
> 卞
> 无障碍
> 弹出式窗口和重定向
> 下允许网站显示弹出式囱口或使用重定向
> 系统
> 重置设置
> 更多内容设置
> 自动撤消末使用的网站的权限
> 扩展程序
> 区
> 为保护您的数据。对于您近期末访问的网站。请允许 Chrome 移除网站权限。此操作不会停用通知功
> 能。
> 关于 Chrome
> 固片


1. 选择网站可以发送弹出式窗口


> [!NOTE] [图片 OCR 识别内容]
> 秕昂打开 Alpha 页_
> WorldQuant BRAIN
> 设翟
> 弹出式窗口和重定向
> Chrome
> Chrome:Ilsettingslcontentlpopups
> Am
> 9
> 验证身份
> 有新版 Chrome 可用
> 器 |口 TDH
> 口个
> 口学习
> 0 工具
> D 待处理
> temp
> 设置
> 搜索设置
> 您与 Google
> 弹出式窗口和重定向
> 自动填充和密码
> 网站可能会发送弹出式窗口以展示广告。或者使用重定向将您引导至您可能不想访问的网站
> 隐私与安全
> 默认行为
> 性能
> 网站会在您访问时自动采用此设置
> 外观
> 网站可以发送弹出式商口井使用重定向
> 搜索引擎
> 默认浏览器
> 区 不允许网站显示弹出式窗口或使用重定向
> 起始页面
> 自定义的行为
> 下列网站采用的是自定义设置 (而非默认设置)
> 刘
> 语言
> 下载内"
> 下允许发送弹出式窗口或使用重定向
> 添加
> 卞
> 无障碍
> 未添加任何网站
> 系统
> 重置设置
> 允许发送弹出式窗口井使用重定向
> 添加
> https:IwW yuque com: 443
> 扩展程序
> 区
> 关于 Chrome


1. 登陆Worldquant Brain


> [!NOTE] [图片 OCR 识别内容]
> 批量打开 Alpha 页面
> WorldQuant BRAIN
> X
> 设置 -隐私与安全
> 又 +
> @3
> platform. worldquantbrain.comldata?delay=undefined&instrumentType=EQUITY&region=US。
> G@
> New
> 蚯
> 验证身份
> 有新版 Chrome 可用
> TDH
> 个人
> 口学习
> 工具
> 待处理
> temp
> ai
> WORLDQUANT
> BRAINI
> Simulate
> Alphas
> Learn
> Data
> Labs
> Genius
> Competitions (4)
> Region
> Universe
> USA
> TOP3000
> What data do You want to find?
> Bearch by dataset name, field name or description
> Searon
> 00
> Browse all datasets 
> Browse all fields
> Browse by category
> 蚣
> Theme datasets
> Delay


1. 打开openDetail.html，输入alphaid以回撤分割，点击打开页面


> [!NOTE] [图片 OCR 识别内容]
> 批量打开 Alpha 页面
> WorldQuant BRAIN
> 又 。女
> 设置 -隐私与安全
> 又 +
> localhost: 63344/vue-project-demolsrc/viewslopenDetail.html?_ijt=ltohttbpjkvOogpvghuirckhmt&_ijj..
> New
> 蚯
> 验证身份
> 有新版 Chrome 可用
> TDH
> 0  个人
> 口学习
> 工具
> 待处理
> temp
> ai
> 批量打开 Alpha 页面
> 请输入参数 (每行-个)
> rZLgnlm
> gnwVzzQ
> 打开页面
> 茴  清空
> 蚣


1. 成功弹出多个alpha详情页面


> [!NOTE] [图片 OCR 识别内容]
> 批量打开 Alpha 页面
> 义
> WorldQuant BRAIN
> WorldQuant BRAIN
> X
> WorldQuant BRAIN
> X |廿
> 设置 -隐私与安全
> 又 +
> @3
> platform.worldquantbrain.comlalphalgnwVzzQ
> New
> 蚯
> 验证身份
> 有新版 Chrome 可用
> TDH
> 个人
> 口学习
> 工具
> 待处理
> temp
> ai
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Simulation Settings
> 1.24
> 11.769
> 0.70
> 3.999
> 4.729
> 6.789o。
> Instrument Type:
> Equity
> Truncation:
> 0.08
> Region:
> USA
> Neutralization:
> Subindustry
> Universe:
> TOP3000
> Pasteurization:
> On
> Year
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> Long Count
> Short Count
> Language:
> Fast Expression
> NaN
> Handling:
> On
> Decay:
> Unit Handling:
> Verify
> 2013
> 1.20
> 16.41%
> 0.53
> 3.259
> 2.11 %
> 3.979600
> 1416
> 1369
> Delay:
> Max Trade:
> Off
> 2014
> 1.48
> 11.349
> 0.82
> 3.849
> 1.71%
> 6.77900
> 1364
> 1412
> 2015
> 0.65
> 11.389
> 0.25
> 1.789
> 2.399
> 3.13900
> 1402
> 1406
> 2016
> 1.04
> 11.359
> 0.50
> 2.939
> 1.689
> 5.1690。
> 1357
> 1445
> Clone Alpha
> 2017
> 2.96
> 10.699
> 2.28
> 7.41%
> 1.21%
> 13.879600
> 1341
> 1421
> 2018
> 0.54
> 11.499
> 0.19
> 1.569
> 4.729
> 2.729600
> 1445
> 1515
> 2019
> 2.36
> 10.839
> 1.72
> 6.669
> 1.549
> 12.31%o0
> 1482
> 1466
> Chart
> Pnl
> 2020
> -0.23
> 11.589
> -0.06
> -0.959
> 3.609
> -1.6496o。
> 1407
> 1524
> 2021
> 1.69
> 11.7296
> 1.25
> 6.889
> 3.039
> 11.75%o。
> 1460
> 1515
> 蚣
> 2022
> 2.13
> 11.189
> 1.80
> 8.909
> 2.409
> 15.929。
> 1578
> 1456
> 2023
> -15.71
> 8.23%
> -31.64
> 50.71 %
> 2.51%
> -123.21%。
> 1553
> 1502
> 2,00OK
> Risk neutralized
> Aggregate Data
> Sharpe
> Turnover
> Fitness
> Returns
> Drawdown
> Margin
> 0.97
> 11.769
> 0.44
> 2.589
> 6.929
> 4.38%o。
> 2014
> 2015
> 2016
> 2017
> 2018
> 2019
> 2020
> 2021
> 2022
> 2023
> Investability constrained
> Aggregate Data
> Sharpe
> TurnoVer
> Fitness
> Returns
> Drawdown
> Margin
> Pnl
> Risk Neutralized Pnl
> Investability Constrained Pnl
> 0.59
> 10.059
> 0.22
> 1.759
> 5.61%
> 3.489o。


---

## 讨论与评论 (16)

### 评论 #1 (作者: LL11353, 时间: 8个月前)

很有用，谢谢佬

---

### 评论 #2 (作者: CC21336, 时间: 8个月前)

试用了一下，非常方便。

---

### 评论 #3 (作者: XW23690, 时间: 8个月前)

感谢分享，不错的功能

---

### 评论 #4 (作者: CL64349, 时间: 8个月前)

感谢分享，非常实用的工具！

---

### 评论 #5 (作者: HC96989, 时间: 8个月前)

非常方便，感谢分享，用 edge浏览器的可以点击设置—>隐私、搜索和服务—>站点权限—>所有权限—>弹出窗口和重定向，开启这个功能即可正常使用

---

### 评论 #6 (作者: XS25970, 时间: 8个月前)

你好，大佬，文件被删了，能重新分享下吗

---

### 评论 #7 (作者: BW14163, 时间: 8个月前)

******************************************************************************************************************
感谢大佬分享，很不错的工具，非常实用，操作也很简便，！！！

期望在论坛能中，能有更多的大佬分享工具插件~

值得学习，祝大佬vf高高 ，base多多！！

********************************每天坚持学一个知识点，尽量不混信号，不过拟合***********************

---

### 评论 #8 (作者: LR93609, 时间: 8个月前)

感谢分享，非常实用的小工具，果断收藏了。

-----------------------------------------------------------------------
  凡是发生，皆利于我；愿我所愿，尽是美好
  没有顺风，没有坦途，不去经历，无法到达
-----------------------------------------------------------------------

---

### 评论 #9 (作者: MY82844, 时间: 8个月前)

感谢分享，又在论坛学到了新技术

---

### 评论 #10 (作者: 顾问 MZ45384 (Rank 51), 时间: 8个月前)

感谢大佬的分享，真的是很方便的功能。祝大佬value factor 1.0，base蒸蒸日上。

========================================================================

=========================there is a way, there is a way=========================

========================================================================

---

### 评论 #11 (作者: HY20507, 时间: 8个月前)

谢谢分享，很实用的工具！

---

### 评论 #12 (作者: XH77948, 时间: 7个月前)

试用了一下，别说还是挺方便的。

---

### 评论 #13 (作者: CJ35087, 时间: 7个月前)

感谢大佬分享，今天在为这个问题发愁，没想到恰好就看到楼主的分享，十分感谢！！！

---

### 评论 #14 (作者: KK88739, 时间: 7个月前)

链接失效，以下是新链接： [https://pan.quark.cn/s/10a1cd889731](https://pan.quark.cn/s/10a1cd889731)

---

### 评论 #15 (作者: XL98962, 时间: 7个月前)

感谢大佬的分享，真的是很方便的功能。祝大佬value factor 1.0，base蒸蒸日上。

========================================================================

=========================there is a way, there is a way=========================

========================================================================

---

### 评论 #16 (作者: LZ70706, 时间: 5个月前)

前些日子为了看 check 出来的存在 csv 文件里的 Alpha，需要手动打开一个个的页面，然后再手动输入 Alpha ID，很是费时费力，这枯燥而又没有创造力的工作，如今因为有了大佬的分享而改变，chrome 和 edge 都能用，真真好，非常感谢，为大佬点赞！祝大佬 VF 高高，base 多多！

---

