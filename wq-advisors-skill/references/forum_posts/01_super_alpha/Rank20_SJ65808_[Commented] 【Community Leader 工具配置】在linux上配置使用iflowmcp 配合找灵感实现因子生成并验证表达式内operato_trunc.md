# 【Community Leader 工具配置】在linux上配置使用iflow+mcp 配合“找灵感”实现因子生成并验证表达式内operator用法是否正确经验分享

- **链接**: https://support.worldquantbrain.com[Commented] 【Community Leader 工具配置】在linux上配置使用iflowmcp 配合找灵感实现因子生成并验证表达式内operator用法是否正确经验分享_37188244453911.md
- **作者**: PZ64174
- **发布时间/热度**: 6个月前, 得票: 66

## 帖子正文

我是装的虚拟机+Ubuntu 22.04 LTS版本。我会从安装虚拟机->安装node 22+，python3.11+

请注意，如果不选择Ubuntu 22.04 LTS想考虑其他版本虚拟机的话，需要搜索是否兼容node22+ python3.11+版本，比如CentOS8/9。其他的大家可以自行搜索。如果有任何安装问题可以豆包/kimi/deepseek，ai会很好的解决各种疑难杂症！

安装前准备：

1. 下载VMware Workstation Pro，可以直接官网下载： [Windows VM | Workstation Pro | VMware](https://link.zhihu.com/?target=https%3A//www.vmware.com/products/workstation-pro.html) ，夸克链接： [https://pan.quark.cn/s/a66279b46e6c](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fpan.quark.cn%2Fs%2Fa66279b46e6c&objectId=2481683&objectType=1&contentType=undefined)
2. 下载Ubuntu 22.04 LTS： [https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/22.04/ubuntu-22.04.5-desktop-amd64.iso](https://mirrors.tuna.tsinghua.edu.cn/ubuntu-releases/22.04/ubuntu-22.04.5-desktop-amd64.iso)

准备安装：

1. 先安装VMware Workstation Pro 
> [!NOTE] [图片 OCR 识别内容]
> VMware Workstation
> 文件旧
> 蒎髯[]
> 查看凹
> G拟机(山]
> 选项卡0
> 帮[山]
> 1 `
> 吕 |
> 顷
> Ubuntu 64位
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟讥
> 连接远裎服务器
> Vware

2. 点击创建虚拟机 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> Vware
> 欢迎使用新建虑拟机向导
> WORKSTATION
> PRO"
> 17
> 您希望使用什么类型的配蛊?
> 典型(推荐)(T)
> 通过几个简单的步骤创建 Workstation 17.5
> OT Iater
> 虚拟机=
> 自定义(高级)(C)
> 创建带有
> CSI 控制器类型
> 虚拟磁盘类型
> 芨怕 VMware 产品兼窖性等蒿级r项
> 的虚拟机
> 帮助
> 步(8)
> 步(川)
> 取消
> Vware

3. 默认，点击下一步 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 逑拜虔拟机硬卅兼容性
> 该虚拟机需要何种硬件功能三
> 虚拟机硬件兼容性
> 默认就好
> 硬件兼窖性(H):
> Workstation 17.5 Orlater
> 兼窖:
> ESX Serer(5]
> 兼窖产品:
> 限制:
> Fusion 13.5Orlater
> 128 GB 内存
> Workstation 17.5 OT later
> ~处嚣
> '适配器
> TB 磁盘划小
> 共尊图形内存
> 帮助
> 上一步(8」
> 下-步(川) >
> 取消
> Vware

4. 稍后安装操作系统，点击下一步 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 突装客户机操作系统
> 虚拟机如同物理机,需要操作系统。您将如何安装客户机操作系统?
> 安装来源:
> 安装程序光盘(0]:
> 无可用驱动器
> 安装程序光盘映像交件(is0)(川):
> D;llinu 虚拟机相关 ubuntu-22.04.5-desktop-amd64.i50
> 浏览(尺]。
> 稍后安装操作系统(5)。
> 创建的虚拟机将包含-
> 个空白硬盘。
> 帮助
> 上-步[8)
> 下-步(川) >
> 取消
> Vware

5. 选择linux->ubuntu，点击下一步 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 选拜客户机操作系统
> 此虚拟机中将安装哪种操作系统?
> 客户机操作系统
> Uirrnsnff wndois(w)
> @LnuxfL)
> VMware ESXCX)
> 其他(0]
> 瓣本(
> Ubuntu 64 位
> ROCR LnUx 64 位
> SUn ]33 Desktop System
> SUSE Linux Enterprise 15 64
> LinUx Enterprise 12 64
> 簋
> Linux Enterprise 11 64
> LinUx Enterprise
> Linux Enterprise I0 64 位
> LinUx Enterprise
> E Linux Enterprise 7/8/9 64 位
> Linux Enterprise 7/8/9
> SUSE Linux 64 位
> SUSE Linu
> Turbolinux 64 位
> Ubymye4
> VMware Photon O5 64 位
> 他 Linux 6x 内核 64 位
> 他 Linux 6x 内核
> 他 Linux
> 64位
> 他 Linux
> 他 Linux
> 54位
> LinUY
> 他
> LinUY
> 64位
> 他 Linux
> 他 Linux
> 68
> 64位
> Vware
> 傀
> LinUY
> 68
> LinUY
> 48
> 64位
> 他 Linus

6. 默认下一步（你也可以修改安装路径） 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 命名虔拟机
> 您希望该虚拟机使用什么名称?
> 虚拟机名称(:
> Ubuntu 64 〈
> 位罡():
> C:lUserslAdministratoriDocumentsl Virtual Machines Ubuntu 64 位
> 浏览(尺].
> 茌"编辑" >"首选项"中可更改默认位蛊。
> 上-步()
> 步(川) >
> 取消
> Vware

7. 下面就默认就行 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 处理器虿蛊
> 为此虚拟机指定处理器粼里。
> 处理器
> 处理器粼里(]:
> 个处理器的内核粼(C):
> 处理器内核总数:
> 帮助
> 上-步()
> 下-步(川) >
> 取消
> Vware

8. 虚拟机内存正常是物理内存的一半，个人可以自行修改 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 此直拟机的内存
> 您要为此虚拟机使用咨少内存?
> 指定分酽绐此虚拟机的内存里。内存太小必须为
> 的倍数。
> 123 GB
> 此虚拟机的内存(川]:
> 4096
> 最大推荐内存:
> 13.4G8
> 推荐内存:
> 256 MB
> 123 MB
> 客户机操作系统最低推荐肉存:
> 32MB
> 15 N
> 4MB
> 帮助
> 上-步()
> 下-步(川) >
> 取消
> Vware

9. 默认，下一步 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 网络类型
> 要添加哪类网络?
> 网络连接
> 使用挢接网络(R]
> 氍,'#直&.。太'呶V-
> 客户机茌外部网络上必须
> IP 地址?
> 镳熊C懋:K黛
> 客户机操作系统提供使用主机 IP 地址访问主机拨号连接或外部以太网网络连接的
> 使用仅主机模式网络(4)
> 将客户机操作系统连接到主机上的专用虚拟网络
> 使用网络连接(T)
> 帮助
> <上-步()
> 下-步(川) >
> 取消
> Vware

10. 默认，下一步 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 逑拜 IIO 控劓器类型
> 您希望将哪种 SCSI 控制器类型用于 SCSI 虚拟磁蓝?
> IIO 控制器类型
> SCSI 控制器:
> BUsLOgic(U]
> (不适用于 64 位客户机)
> LSILogic(L)
> (推荐-
> LSI Logic SASCS)
> 淮虚拟化 SCSI(P)
> 帮助
> 上-步(8)
> 慝忑-毖(Nw
> 取消
> Vware
  
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 选拜薛盎类型
> 您要创建何种磁盘?
> 虚拟磁盘类型
> IDE(I)
> u煎煎
> [推荐
> SATA(A)
> NIVMelv]
> 帮助
> 上-步()
> 下-步(川) >
> 取消
> Vware
  
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 选拜薛盎
> 您要使用哪一
> 磁盘?
> 磁盘
> 籁獯籁蔗煦"蕊
> 批磁盘由主机交件系统上的一个或多个文件组成_
> 单个硬盘
> 虚拟磁盘可在
> 台主机上或忽台主机之
> =蠼s麓合将其视为
> 使用现有虚拟磁盘(E)
> 选挥此选项可重新使用以前配罡的磁蓝
> 使用物理磁盘 (适用于高级用户)()
> 选挥此选项可为虚拟机提供直接访问本地硬盘的杈限
> 需要具有管理员特杈。
> 帮助
> 上-步()
> 下-步(川) >
> 取消
> Vware

11. 选单个文件性能效率会更高 
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 措定薛盎容里
> 磁盘太小为多少?
> 最大磁盘大小 (G8)(5)
> 针对 Ubuntu 64 位的建议大小:20 GB
> 立即分配所有磁盘空间(8)。
> 醑蠢黑削奖髁巅:儇.
> 能;但要求斯有物理磁盘空间立即可用
> 如果不立即分配所有
> 虚拟磁盘的空
> 会随着您向其中添加数据而不断变大。
> 将虚拟磁蓝存储为单个交件(@)
> 将虚拟磁盘拆分成咨
> 交件(丛)
> 单个文件性能效率会更高
> 拆分磁蓝后; 可以更轻凇地茌计算机之间移动虚拟机,但可能会降低太窖里磁盘的性
> 帮助
> 上一步(旦)
> 下-步() >
> 取消
> Vware
> R00
  
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 措定6盎文卅
> 您要在何处存槠磁盘交件?
> 磁盘交件(E)
> 将使用多个磁盘文件创建-
> 20 GB
> 虚拟磁盘
> 将抿据此文件名自动命名这些磁盘文
> Ubuntu 64 位 WINk
> 浏览(R)..
> 帮助
> <上-步[旦)
> 下-步() >
> 取消
> Vware
  
> [!NOTE] [图片 OCR 识别内容]
> WORKSTATION PRo" 17
> 创建新的虚拟矶
> 打开虚拟矶
> 连接远裎服务器
> 新建盍拟机向导
> 己准备好创建虔拟机
> 单击"完成"创建虚拟机。然后可以安装 Ubuntu 64 位。
> 将使用下列设罡创建虚拟机:
> 客称
> Ubuntu 64 位
> 位蛊
> C:IUsers Administrator Documents Virtual Machines Ubunt。
> 版本
> Workstation 17.5 Or later
> 操作系统:
> Ubuntu 64 位
> 硬盘
> 20 GB,拆分
> 内存=
> 4096 |
> 网络适配器
> NAT
> 其他设备
> 2个 CPU 内核
> CDIDVD, USB 控制器 声卡
> 自定义硬件(C)
> ~上步(旦)
> 完成
> 职消
> Vware

12. 点击完成之后来到这个界面，点击“编辑虚拟机设置”“CD/DVD (SATA)”“选择使用ISO映像文件”选择上面下载的Ubuntu 22.04 LTS 
> [!NOTE] [图片 OCR 识别内容]
> 主
> Ubuntu 64位
> Ubuntu 64莅
> Ubuntu 64 位
> 虚拟机设置
> 开启此虎抠机
> [E辑盍拟机设置
> 1
> 硬件
> 选项
> 设备
> 摘要
> 设备拢态
> 设备
> 内存
> 己连接(C)
> 匀内存
> 猬处理器
> 启动时连接(0]
> 燕处理器
> 硬盏 (SCSI]
> 20G3
> CRlow (SA
> 鼠#『
> CDIDVD (SATAJ
> 刍动检测
> JHa
> 使用物理驱动器():
> USB
> 控制器
> 存在
> ]网适配器
> NAT
> 声卡
> 自动检测
> 自动检则
> USB 控制器
> 存在
> 显示
> 自动检则
> 使用 ISO 映像交件(w:
> I 声卡
> 兰动检测
> D:llinux虚拟机相关  ubuntu-:
> 浏览(8)
> 显示
> 三动栓讽
> 高级(V.
> 描述
> 在[处篷入对该虚拟机的满述
> 添加(A].
> 移除(R)
> 确定
> 取消
> 帮助
> 虚拟机详细信息
> 状态:
> 已关机
> 配置文件: C: UserslAdministratorDocuments {Virtual Machines Ubuntu 64 位Ubuntu 64 位vmx
> 硬件蒹容性: Workstation 17.5 或啬版本虚拟机
> 主 I 地址:  网络信息阿用

13. 点击开启此虚拟机，虚拟机窗口打开后，选择第一个按回车 
> [!NOTE] [图片 OCR 识别内容]
> 主
> Ubuntu 64位
> Ubuntu 64莅
> Ubuntu 64 位
> 开启U虚拟机
> 犏辑箧拟机设置
> 设备
> 匀内存
> 燕处理器
> 硬盏 (SCSI]
> 20G3
> CDIDVD (SATAJ
> 正在使用文件 D::
> 品网适配器
> NAT
> USB 控制器
> 存在
>  声卡
> 兰动检测
> 9显示
> 亨检测
> 描述
> 虚拟机详细信息
> 状态:  {关机
> 配置文件: C: UserslAdministratorDocuments {Virtual Machines Ubuntu 64 位Ubuntu 64 位vmx
> 硬件蒹容性: Workstation 17.5 或啬版本虚拟机
> 主 I 地址:  网络信息阿用
  
> [!NOTE] [图片 OCR 识别内容]
> BNU
> BRUB
> Uersion
> 2.昵
> &
> Insta11
> Ubuntu
> OM
> ista11
> for
> Hanufacturers )
> Test HeHory
> USe
> the
> ana
> keys
> Select
> Which entry
> is highlighted.
> Pres5
> enter
> t0
> boot
> the
> Selected 05
> edit
> the
> CoHHands
> before
> boot
> for
> CoHHana-
> ie
> The nighlightea entry Will
> b
> executed
> autoHatically
> 385
> 
> ing

14. 到这个界面，选择中文，选择安装Ubuntu，下面就默认，点下一步 
> [!NOTE] [图片 OCR 识别内容]
> Deczz 03:17
> 呼
> Nj (
> 安装
> 欢迎
> E山
> SODN
> +
> Qemne。
> 孓 SC
> 1747lil
> 090
> 试用 Ubuntu
> 安装 Ubuntu
> V
> 您可以直接从此 CD 尝试 Ubuntu, 而不用对您的电脑作任何更改。
> u301
> 如果您已经准备完毕。您可以与现有柔统并存 (或者替代)方式捋 Ubuntu 安装到您的电脑上
> 中文(简体)
> 此过程无需耗时太久。
> 中文(檠髑)
> 日本琵
> 您可以阅读一下发行注记。
> Bsem
  
> [!NOTE] [图片 OCR 识别内容]
> Deczz 03:17
> 呼
> Nj (
> 安装
> 键盘布局
> 选择您的键盘布局
> Belarusian
> Chinese
> Belgian
> Chinese - Hanyu Pinyin (with AltCT dead keys)
> Berber (Algeria, Latin)
> Chinese
> Mongolian (Bichig)
> Bosnian
> Chinese
> Mongolian (Galik)
> Braille
> Chinese - Mongolian (Manchu Calik)
> Bulgarian
> Chinese - Mongolian (Manchu)
> BUrmese
> Chinese - Mongolian (Todo Calik)
> Chinese 
> chinese - Mongolian (Todo)
> Croatian
> Chinese - Mongolian (Xibe)
> Czech
> Chinese
> Tibetan
> Danish
> Chinese
> Tibetan (with ASCIInumerals)
> Dhivehi
> Chinese -Uyghur
> Dutch
> Dzongkha
> English (Australian)
> 在这里输入以测试您的键盘
> 探测键盘布局
> 退出(Q)
> 后退(8)
> 继续
  
> [!NOTE] [图片 OCR 识别内容]
> Deczz 03:18
> 呼
> Nj (
> 安装
> 更新和其他软件
> 您希望先安装哪些应用?
> 正常安装
> 网络浏览器。工具。办公软件。游戏和媒体捂放器。
> 最小安装
> 网络浏览器和垄本工具
> 其他选项
> 安装 Ubuntu 时下载更新
> 这能节约安装后的时问。
> 为图形或无线硬件。以及其它媒体格式安装第三方软件
> 此软件及其文档遵循许可条款。其中一些是专有的。
> 退出(Q)
> 后退(8)
> 继续

15. 继续默认下一步 
> [!NOTE] [图片 OCR 识别内容]
> Dec 22
> 03:19
> 品 I V
> 安装
> 安装类型
> 这台计算机似乎没有安装操作柔统。您准备怎么做 ?
> 清除整个磁盘并安装 Ubuntu
> 注意 : 这会删除所有系统里面的全部程序
> 文档。照片。音乐和其他文仵。
> 高级特性。
> 尚未选择任何项目
> 其他选项
> 您可以自己创建。调整分区;或者为 Ubuntu 选择多个分区。
> 退出(Q)
> 后退(8)
> 现在安装()
  
> [!NOTE] [图片 OCR 识别内容]
> Dec zz 03:20
> 品 I V
> 安装
> 您在什么地方?
> Shanghai
> 后退(8)

16. 填写信息，然后等待安装完毕，请记住你填写的密码！（后面需要你user权限的时候会让你填） 
> [!NOTE] [图片 OCR 识别内容]
> Dec zz 11:20
> 品 I V
> 安装
> 您是谁 ?
> 您的姓名
> 您的计算机名
> 与其他计算机联络时使用的名称。
> 选择
> 个用户名
> 选择一个密码
> 确认您的密码
> 自动登录
> 登录时需要密码
> 使用 Active Directory
> 您将在下一步中输人域和其他详细信息。
> 后退(8)

17. 安装完毕之后重启，到这就安装完毕了，接下来就是命令行安装node，python
18. `首先执行系统包更新，避免安装过程中出现依赖问题：sudo apt update && sudo apt upgrade -y`
19. 先安装nvm：
   步骤1：sudo apt install -y curl wget  //安装 nvm 依赖
   步骤2：curl -o-  [https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh](https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh)  | bash   //安装 nvm
   步骤3：source ~/.bashrc   //激活 nvm
   步骤4：nvm install 22    //安装 Node.js 22
   步骤5：nvm alias default 22  // `设置为默认版本`
   安装 Python 3.11：
   步骤1： `sudo apt install -y software-properties-common  //安装必要依赖`
   `步骤2：添加 deadsnakes PPA（可信的 Python 版本源）`
   ```
   sudo add-apt-repository ppa:deadsnakes/ppa -y
   sudo apt update
   ```
   步骤3 安装 Python 3.11：
   ```
   sudo apt install -y python3.11 python3.11-dev python3.11-venv
   ```
   `步骤4：设置 Python 3.11 为默认 python3`
   ```
   # 查看现有python3链接
   ls -l /usr/bin/python3
   # 添加别名（临时生效，重启终端后需重新执行）
   alias python3=python3.11
   # 永久生效（写入bashrc）
   echo "alias python3=python3.11" >> ~/.bashrc
   source ~/.bashrc
   ```
   步骤5：先升级对应版本的 pip
   ```
   python3.11 -m pip install --upgrade pip
   ```
   步骤6：安装mcp
   ```
   python3.11 -m pip install
   ```
   安装完mcp后，打开主目录设置“显示隐藏文件”，直接进行搜索，cnhkmcp，打开cnhkmcp，找到“platform_functions.py”打开命令行运行这个文件，会提示你缺少什么依赖，用“ `python3.11 -m pip install+包名` ”安装就行了，直到能够正常运行这个文件 
> [!NOTE] [图片 OCR 识别内容]
> Ubuntu 64 位
> VMware Workstation
> 文件旧
> 蒎髯[]
> 查看凹
> G拟机(山]
> 选项卡0
> .印(H]
> 1
> 母
> 主
> Ubuntu 64莅
> 在[处篷入内7迸行{素
> 活动
> 曰文件
> -h品 I (
> 莪的计算机
> Ubuntu 64 位
> 品
> 名称
> 大小
> 修改时间
> 最近使用
> 公共的
> 0个项目
> 09 ;21
> 收藏
> 仑  主目录
> 模板
> 0个项目
> 09 ;21
> 旧 视频
> 视频
> 0个项目
> 09 ;21
> 图片
> 图片
> 0个项目
> 09 ;21
> 眉  文档
> 文档
> 0个项目
> 09 ;21
> 卫 下载
> 几音乐
> 下载
> 0个项目
> 09 ;21
> 彘 回收站
> 音乐
> 0个项目
> 09 ;21
> UbuntU 22.0.
> 桌面
> 0个项目
> 09 ;21
> 其他位置
> SRap
> 3个项目
> 09 ;43
> yoUhUa
> 15个项目
> 10 ;20
> cache
> 16个项目
> 10 ; 19
> config
> 19个项目
> 10 ; 28
> .Tlow
> 8个项目
> 10 ; 17
> local
> 3个项目
> 09 .35
> RPM
> 3个项目
> 09 ; 36
> RVM
> 个项目
> 09 ; 30
> bash_history
> 1.6kB
> 10 ; 23
> bash_logout
> 己选中" local"
> (含有3项)
> 要将k入定向到该虚拟机。违将彘标指针移入其中或按 CtrltG。
  
> [!NOTE] [图片 OCR 识别内容]
> 活动
> 曰文件
> 12月228
> 11 :41
> r Mj (
> 仑主文件夹
> LJoti
> 最近使用
> 公共的
> 丈  收藏
> 撤消(0)
> 仑 主目录
> 模板
> 重做(R)
> 髓 视频
> 视频
> 显示隐藏文件(4)
> 图片
> 显示侧迈栏(5)
> 图片
> 首选项(P)
> 圄  文档
> 文档
> 键盘快捷键(K)
> 卫  下载
> 帮助(4)
> 几音乐
> 下载
> 关于文件(A)
> 回收站
> 音乐
> 个项目
> 09 : 21
> UbUntU 22.0.
> 桌面
> 个项目
> 09 ;21
> 其他位置
> SRap
> 3个项目
> 09 +43
> youhua
> 15个项目
> 10 +20
> cache
> 16个项目
> 10 ; 19
> config
> 19个项目
> 10 ; 28
> .TlOw
> 个项目
> 10 ;17
> .lOcal
> 3个项目
> 09 ;35
> npM
> 3个项目
> 09 ;36
> RVM
> 个项目
> 30
> bash_history
> 1.6kB
> 10
> 23
> bash_logoul
> 220字节
> 09 ;13
  
> [!NOTE] [图片 OCR 识别内容]
> 活动
> 曰文件
> 12月228 11 :44
> 岳 Mj (
> cnhkmcpl
> 最近使用
> 大  收藏
> cnhkmcp
> cnhkmCP
> cnhkmCP
> 2.0.4.dist
> 主目录
> info
> 髓 视频
> 图片
> 圄  文档
> 卫  下载
> 几音乐
> 回收站
> UbUntU 22.0.
> 其他位置
> 己选中"cnhkmcp" (211字节)

   我是用iflow配置的mcp，安装iflow：
   ```
   npm i -g @iflow-ai/iflow-cli@latest
   ```
   找到.iflow
   ```
   which .iflow
   ```
   找到.iflow之后点开settings，配置mcpServers
   ```
   "mcpServers": {    "worldquant-brain-platform": {      "command": "/usr/bin/python3.11",      "args": [        "/home/pingan/.local/lib/python3.11/site-packages/cnhkmcp/untracked/platform_functions.py"      ],      "timeout": 30000,      "requestTimeout": 10000,      "disabled": false    }  }
   ```
   
> [!NOTE] [图片 OCR 识别内容]
> 活动
> 文本编辑器
> 12月228 11 :49
> 品 Ij (
> 主文件夹
> iow
> 大
> 修改时间
> 最近使用
> cache
> 打开(0)
> settingsjson
> 保存(5)
> 0个项目
> 09 +43
> 收藏
> ~LiFlow
> U  主目录
> config
> 个项目
> 09 +43
> 髓  视频
> projects
> 2个项目
> 10 ; 30
> 图片
> [MD
> 2个项目
> 10 ; 20
> TOUCLNOIIC
> 9Lm- 4.6
> 眉  文档
> MCpServers
> IOW
> Ccountsjson
> WOFJquant
> brain-platform"
> 89字节
> 10 ; 45
> 卫  下载
> 10
> Command"
> /Usr/bin/python3. 11"
> installation_id
> 3「95
> 36字节
> 09 +43
>  音乐
> `
> Thome /pingan / . local/lib/python3 .II/site-packages / cnhkmcp /untracked /platform
> functions . Py
> 回收站
> Oauth_credsjson
> timeout"
> 30000
> 229字节
> 10 ; 45
> CequestTimeout"
> 10000
> UbURCU 22.0..
> Seltingsjson
> %
> 0i5abled"
> fal5e
> 559字节
> 1017
> 18
> 19
> 其他位置
> JSON
> 制表符宽度:  8~
> 第8行。第3列
> 插入
> 已选中"settingsjson" (559字节)

   命令行运行：iflow，打开之后就能看到mcp已经配置成功，输入指令去调用mcp方法就行了。
   
> [!NOTE] [图片 OCR 识别内容]
> 活动
> 终端
> 12月228
> 11 :51
> 2h
> r Mj (
> iFlow - 桌面
> VCP
> 1i5t
> 已配置的 McP 服务器 (共 1个)
> Worldquant-brain - platform
> 就绪
> 无描述
> 工具:
> 40
> 提示:
> 0 |
> 上下文长度:  6857 tokens
> 导航:
> N Lor jik
> 上下导航
> Space / Enter
> 查看服务器详情
> 禁用服务器
> 移除服务器
> 退出
> 桌面
> glm-4.6 上下文剩余
> 100%
> OIDE:
> 已断开
> VO.4.7

   至此linux配置完毕。
   ps:如果想要在虚拟机上输入中文，可以使用以下命令：
   ```
   # 更新系统软件包
   sudo apt update
   # 安装中文语言包（可选但推荐）
   sudo apt install language-pack-zh-hans#安装 Fcitx5 框架和中文支持sudo apt install fcitx5 fcitx5-chinese-addons fcitx5-config-qt# 打开设置界面
   im-config
   # 选择"Fcitx5" → 确定 → 重启
   ```
   配合找灵感生成alpha表达式，并且验证alpha表达式operator用法是否正确：
   ***通过找灵感的模板生成表达式的指令*** ：
   ```
   ### 生成alpha1.使用authenticate工具，从配置文件读取凭据：- 文件：user_config.json；认证后，可以保持登陆状态6小时，超时需要重新认证2.获取平台region：USA Universe:TOP3000 DELAY:1 dataset.id:analyst49 数据集数据字段，按照每个模板来对数据字段进行聚类管理，严格按照每个模板的含义来生成表达式，保证每个模板对应生成表达式都是正确的都是对应模板含义的。一个模版生成100个表达式3.严格按照'总结'的内容进行表达式生成4.如果需要operator信息，请根据 Resources/operator_1.md Resources/operator_1.md 获取operator信息，严格按照operator使用方法生成alpha！5.检查生成的表达式是否符合operator使用规则，如有问题请立即修改，确定没问题的alpha保存生成的alpha到usa_analyst49_alpha.json文件，通过check_operator_errors_v2.py 进行二次检查。6.请注意：group类型字段只能作为group_类型操作符的group字段去使用，不能用于其他地方。7.表达式按照[['ts_stddev(zscore((vec_avg(anl27_analyst_accuracy1) + vec_avg(anl27_analyst_consistency)) * vec_avg(anl27_profitabilityprev_analyst_profitability1_20d)), 10)',5]]格式输出
   ```
   ***生成完的表达式验证operator使用是否正确：***
   ```
   import jsonimport refrom typing import Dict, List, Set, Tuple# 定义有效的操作符及其参数要求OPERATORS = {    # Arithmetic operators    "add": {"min_params": 2, "max_params": -1},  # -1 means unlimited    "subtract": {"min_params": 2, "max_params": 3},    "multiply": {"min_params": 2, "max_params": -1},    "divide": {"min_params": 2, "max_params": 2},    "power": {"min_params": 2, "max_params": 2},    "signed_power": {"min_params": 2, "max_params": 2},    "sqrt": {"min_params": 1, "max_params": 1},    "abs": {"min_params": 1, "max_params": 1},    "log": {"min_params": 1, "max_params": 1},    "inverse": {"min_params": 1, "max_params": 1},    "reverse": {"min_params": 1, "max_params": 1},    "sign": {"min_params": 1, "max_params": 1},    "round": {"min_params": 1, "max_params": 1},    "floor": {"min_params": 1, "max_params": 1},    "max": {"min_params": 2, "max_params": -1},    "min": {"min_params": 2, "max_params": -1},    "tanh": {"min_params": 1, "max_params": 1},    "sigmoid": {"min_params": 1, "max_params": 1},    "arc_tan": {"min_params": 1, "max_params": 1},    "s_log_1p": {"min_params": 1, "max_params": 1},    "nan_out": {"min_params": 1, "max_params": 3},    "to_nan": {"min_params": 1, "max_params": 3},    "pasteurize": {"min_params": 1, "max_params": 1},    "purify": {"min_params": 1, "max_params": 1},       # Logical operators    "and": {"min_params": 2, "max_params": 2},    "or": {"min_params": 2, "max_params": 2},    "not": {"min_params": 1, "max_params": 1},    "if_else": {"min_params": 3, "max_params": 3},    "is_nan": {"min_params": 1, "max_params": 1},    "is_not_nan": {"min_params": 1, "max_params": 1},    "is_finite": {"min_params": 1, "max_params": 1},    "less": {"min_params": 2, "max_params": 2},    "greater": {"min_params": 2, "max_params": 2},    "less_equal": {"min_params": 2, "max_params": 2},    "greater_equal": {"min_params": 2, "max_params": 2},    "equal": {"min_params": 2, "max_params": 2},    "not_equal": {"min_params": 2, "max_params": 2},       # Time series operators    "ts_mean": {"min_params": 2, "max_params": 2},    "ts_sum": {"min_params": 2, "max_params": 2},    "ts_std_dev": {"min_params": 2, "max_params": 2},    "ts_zscore": {"min_params": 2, "max_params": 2},    "ts_delta": {"min_params": 2, "max_params": 2},    "ts_delay": {"min_params": 2, "max_params": 2},    "ts_rank": {"min_params": 2, "max_params": 3},    "ts_max": {"min_params": 2, "max_params": 2},    "ts_min": {"min_params": 2, "max_params": 2},    "ts_corr": {"min_params": 3, "max_params": 3},    "ts_covariance": {"min_params": 3, "max_params": 3},    "ts_scale": {"min_params": 2, "max_params": 3},    "ts_backfill": {"min_params": 2, "max_params": 2},    "ts_decay_linear": {"min_params": 2, "max_params": 3},    "ts_weighted_decay": {"min_params": 1, "max_params": 2},    "ts_quantile": {"min_params": 2, "max_params": 3},    "ts_product": {"min_params": 2, "max_params": 2},    "ts_rank": {"min_params": 2, "max_params": 3},    "ts_arg_max": {"min_params": 2, "max_params": 2},    "ts_arg_min": {"min_params": 2, "max_params": 2},    "ts_av_diff": {"min_params": 2, "max_params": 2},    "ts_kurtosis": {"min_params": 2, "max_params": 2},    "ts_entropy": {"min_params": 2, "max_params": 2},    "ts_co_kurtosis": {"min_params": 3, "max_params": 3},    "ts_co_skewness": {"min_params": 3, "max_params": 3},    "ts_count_nans": {"min_params": 2, "max_params": 2},    "ts_min_diff": {"min_params": 2, "max_params": 2},    "ts_min_max_diff": {"min_params": 2, "max_params": 3},    "ts_min_max_cps": {"min_params": 2, "max_params": 3},    "ts_moment": {"min_params": 2, "max_params": 3},    "ts_returns": {"min_params": 2, "max_params": 3},    "ts_step": {"min_params": 1, "max_params": 1},    "ts_theilsen": {"min_params": 3, "max_params": 3},    "ts_ir": {"min_params": 2, "max_params": 2},    "days_from_last_change": {"min_params": 1, "max_params": 1},    "last_diff_value": {"min_params": 2, "max_params": 2},    "inst_tvr": {"min_params": 2, "max_params": 2},    "ts_decay_exp_window": {"min_params": 2, "max_params": 3},    "jump_decay": {"min_params": 3, "max_params": 4},    "hump_decay": {"min_params": 1, "max_params": 2},       # Group operators    "group_mean": {"min_params": 2, "max_params": -1},    "group_std_dev": {"min_params": 2, "max_params": -1},    "group_zscore": {"min_params": 2, "max_params": 2},    "group_neutralize": {"min_params": 2, "max_params": 2},    "group_rank": {"min_params": 2, "max_params": 2},}def parse_function_call(expr_str: str, start_pos: int) -> Tuple[str, List[str], int]:    """解析函数调用，返回函数名、参数列表和结束位置"""    # 提取函数名    func_name = ""    i = start_pos    while i < len(expr_str) and (expr_str[i].isalpha() or expr_str[i] == '_'):        func_name += expr_str[i]        i += 1       # 跳过左括号    if i < len(expr_str) and expr_str[i] == '(':        i += 1    else:        return func_name, [], i       # 解析参数    params = []    current_param = ""    paren_count = 0       while i < len(expr_str):        char = expr_str[i]               if char == '(':            paren_count += 1            current_param += char        elif char == ')':            paren_count -= 1            if paren_count < 0:                # 函数结束                if current_param.strip():                    params.append(current_param.strip())                break            current_param += char        elif char == ',' and paren_count == 0:            # 顶级逗号，分割参数            if current_param.strip():                params.append(current_param.strip())            current_param = ""        else:            current_param += char               i += 1       return func_name, params, idef validate_expression(expr_str: str) -> List[str]:    """验证单个表达式，返回错误列表"""    errors = []    i = 0       while i < len(expr_str):        # 查找函数调用        if expr_str[i].isalpha() or expr_str[i] == '_':            func_name, params, end_pos = parse_function_call(expr_str, i)                       if func_name in OPERATORS:                # 检查参数数量                op_info = OPERATORS[func_name]                param_count = len(params)                               if param_count < op_info["min_params"]:                    errors.append(f"Operator {func_name} requires at least {op_info['min_params']} parameters, got {param_count}")                               if op_info["max_params"] != -1 and param_count > op_info["max_params"]:                    errors.append(f"Operator {func_name} requires at most {op_info['max_params']} parameters, got {param_count}")                               # 特定检查                # 1. ts_delta的第二个参数应该是正整数                if func_name == "ts_delta" and len(params) >= 2:                    try:                        days = int(params[1])                        if days <= 0:                            errors.append(f"ts_delta days parameter should be positive: {days}")                    except ValueError:                        errors.append(f"ts_delta days parameter should be an integer: {params[1]}")                               # 2. ts_delay的第二个参数应该是正整数                if func_name == "ts_delay" and len(params) >= 2:                    try:                        days = int(params[1])                        if days <= 0:                            errors.append(f"ts_delay days parameter should be positive: {days}")                    except ValueError:                        errors.append(f"ts_delay days parameter should be an integer: {params[1]}")                               # 3. 时间序列操作符的天数参数应该合理                time_series_ops = ['ts_mean', 'ts_sum', 'ts_std_dev', 'ts_zscore', 'ts_max', 'ts_min',                                   'ts_corr', 'ts_covariance', 'ts_scale', 'ts_backfill', 'ts_decay_linear',                                   'ts_rank', 'ts_quantile', 'ts_product', 'ts_arg_max', 'ts_arg_min',                                   'ts_av_diff', 'ts_kurtosis', 'ts_entropy', 'ts_co_kurtosis', 'ts_co_skewness',                                   'ts_count_nans', 'ts_min_diff', 'ts_min_max_diff', 'ts_min_max_cps',                                   'ts_moment', 'ts_returns', 'ts_theilsen', 'ts_ir', 'inst_tvr',                                   'ts_decay_exp_window']                               if func_name in time_series_ops and len(params) >= 2:                    try:                        days = int(params[1])                        if days <= 0:                            errors.append(f"{func_name} days parameter should be positive: {days}")                        elif days > 500:  # 合理的上限                            errors.append(f"{func_name} days parameter too large: {days}")                    except ValueError:                        errors.append(f"{func_name} days parameter should be an integer: {params[1]}")                               # 4. group_zscore的第二个参数应该是分组字段                if func_name == "group_zscore" and len(params) >= 2:                    if params[1] not in ['industry', 'sector', 'subindustry']:                        errors.append(f"group_zscore group_by parameter should be a grouping field: {params[1]}")                       i = end_pos + 1        else:            i += 1       # 检查数据字段名称    datafield_matches = re.findall(r'anl49_[a-z0-9_]+', expr_str)    for field in datafield_matches:        # 基本验证，确保是 anl49 字段        if not field.startswith('anl49_'):            errors.append(f"Invalid analyst49 data field format: {field}")       return errorsdef validate_alpha_file(file_path: str) -> Dict:    """验证alpha文件"""    print(f"Validating {file_path}...")       with open(file_path, 'r', encoding='utf-8') as f:        data = json.load(f)       results = {        "total_expressions": 0,        "valid_expressions": 0,        "error_summary": {},        "detailed_errors": {},        "operator_usage": {},        "datafield_usage": set()    }       # 处理列表格式的数据    if isinstance(data, list):        expressions = data    elif isinstance(data, dict) and 'expressions' in data:        expressions = data['expressions']    else:        expressions = []    template_errors = []       print(f"\nChecking {len(expressions)} expressions...")       for i, expr in enumerate(expressions):        if not isinstance(expr, list) or len(expr) != 2:            template_errors.append(f"Expression {i}: Invalid format - {expr}")            continue               expr_str, delay = expr        if not isinstance(expr_str, str) or not isinstance(delay, int):            template_errors.append(f"Expression {i}: Invalid types - {expr}")            continue               results["total_expressions"] += 1               # 验证表达式        errors = validate_expression(expr_str)        if errors:            template_errors.extend([f"Expression {i}: {err}" for err in errors])        else:            results["valid_expressions"] += 1               # 统计操作符使用        operators = re.findall(r'\b([a-z_]+)\(', expr_str)        for op in operators:            if op in results["operator_usage"]:                results["operator_usage"][op] += 1            else:                results["operator_usage"][op] = 1               # 统计数据字段使用        datafields = re.findall(r'anl52_[a-z0-9_]+', expr_str)        results["datafield_usage"].update(datafields)               # 每100个表达式显示一次进度        if (i + 1) % 100 == 0:            print(f"  Processed {i + 1}/{len(expressions)} expressions")       if template_errors:        results["detailed_errors"]["expressions"] = template_errors        print(f"  Found {len(template_errors)} errors")    else:        print(f"  All expressions valid")       # 汇总错误类型    for error in template_errors:        error_type = error.split(":")[-1].strip()        if error_type in results["error_summary"]:            results["error_summary"][error_type] += 1        else:            results["error_summary"][error_type] = 1       return resultsdef main():    file_path = 'E:\\PythonProject\\test\\youhua\\usa_analyst49_alpha.json'    results = validate_alpha_file(file_path)       print("\n" + "="*60)    print("VALIDATION SUMMARY")    print("="*60)    print(f"Total expressions: {results['total_expressions']}")    print(f"Valid expressions: {results['valid_expressions']}")    print(f"Invalid expressions: {results['total_expressions'] - results['valid_expressions']}")       if results['error_summary']:        print(f"\nError Summary:")        for error_type, count in sorted(results['error_summary'].items()):            print(f"  {error_type}: {count}")       print(f"\nOperators Used ({len(results['operator_usage'])}):")    for op, count in sorted(results['operator_usage'].items()):        print(f"  {op}: {count}")       print(f"\nData Fields Used ({len(results['datafield_usage'])}):")    for field in sorted(results['datafield_usage']):        print(f"  {field}")       # 保存详细错误到文件    if results['detailed_errors']:        with open('E:\\PythonProject\\test\\youhua\\validation_errors_v2.json', 'w', encoding='utf-8') as f:            json.dump(results['detailed_errors'], f, indent=2, ensure_ascii=False)        print(f"\nDetailed errors saved to validation_errors_v2.json")       return resultsif __name__ == "__main__":    main()
   ```
   ***配置：复制上面代码到编辑器，找到第三百行，替换成你要验证的表达式文件就行***
   ```
   file_path = 'E:\\PythonProject\\test\\youhua\\usa_analyst49_alpha.json'
   ```
   如果能够帮助到大家，还请大家点点赞！

---

## 讨论与评论 (4)

### 评论 #1 (作者: YQ84572, 时间: 6个月前)

iflow+mcp的经验分享很详细，很有帮助
====================================================================================
祝大佬base多多，vf高高，分享更多小妙招～～
====================================================================================

---

### 评论 #2 (作者: YB15978, 时间: 6个月前)

====================================================================================
感谢大佬，大部分都是系统安装的教程，感兴趣的人不多啊

建议大佬   **把做好的ubuntu + iflow 做成docker，分享给大家直接使用 就方便了** 
====================================================================================

---

### 评论 #3 (作者: 顾问 SJ65808 (Rank 20), 时间: 6个月前)

感谢大佬的分享

====================================================================================
==================纸上得来终觉浅，绝知此事要躬行======================================

---

### 评论 #4 (作者: CY96125, 时间: 5个月前)

首先感谢分享，其次有个问题，这个虚拟机是安装在自己电脑上的，那么在不使用电脑状态下仍然会停止运行，这么看来，去实践的意义也不是很大。。。

---

