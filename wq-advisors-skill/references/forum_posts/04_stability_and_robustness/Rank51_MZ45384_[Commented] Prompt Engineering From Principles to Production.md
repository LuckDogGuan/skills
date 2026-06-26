# Prompt Engineering: From Principles to Production

- **链接**: [Commented] Prompt Engineering From Principles to Production.md
- **作者**: YW93864
- **发布时间/热度**: 7个月前, 得票: 9

## 帖子正文

最近在参与AIAC期间，学习了一些提示词工程的方法论，做了一些读书笔记分享给大家，希望对大家做AI Alpha时有帮助。本文只选取了Chap. 1-3, 5, 6共5章内容，这些内容和文本式的应用场景比较相关。其余章节，与langChain介绍和视频生成有关，更多信息请参考原书。

**文献引用：** Phoenix, J., & Taylor, M. (2024).  *Prompt Engineering for Generative AI: Future-Proof Inputs for Reliable AI Outputs at Scale, O’Reilly Media*

*
> [!NOTE] [图片 OCR 识别内容]
> Prompt Engineering for Generative AI (Reading Jotes)
> HT93864
> [JTT
> AISC CFRA
> October 28 2025
> 核心概念铺垫
> 1.1
> 提示工程定义
> 提示工程是探索能让41模型
> 如文本模型ChatGPT, 扩散模型Nidjolrney
> 稳定产出有用或
> 期望结果的提示的过程。核心目标是通过优化输入指令-
> 提升41响应的质量。可靠性,并降低成本
> 与延迟。
> 1.2
> 基础提示的局限性
> 未经过优化的 "基础提示" (如 "生成适配任何脚码的鞋类产品名")在生产场景中存在五大
> 问题:
> (1)  方向模糊:  未明确名称风袼 (单字/组合词)。语言属性 (真实荧文{造词)等;
> (2) 输出格式混乱:  响应长度不定。有时为编号列表。有时含前缀文本,难以编程解析;
> 缺乏示例:
> 41仅基于互联网训练数据平均值生成。可能含固有偏差;
> 评估缺失:  无统一可扩展的质量判定标准。需人工逐一审核;
> 任务未拆分:  单一提示承担多因素任务,无专业化分工与过程可见性
> 2
> Chapter 1
> 提示工程的五大核心原则
> 2.1
> 原则一:  给出方向 (Give Direction)
> 2.1.1
> 核心逻辑
> 明确41生成内容的风格。属性或场景。减少结果随机性,
> 让41精准匹配需求。本质是为41提
> 供 "创作背景" ,
> 类似给人类创作者的详细brief。
> 2.1.2
> 实现方式
> 1)  详细描述风袼:  如
> 产品名需简洁易记,包含
> 适配'  相关含义。避免生僻词" =
> 1〉)  引用相关人物 /角色:  指定模仿某领域权威人物的风格,利用其在训练数据中的特征;
> 1)  融入行业规则:  将外部权威标准
> 如品牌命名指南一
> 写入提示,作为41的创作约束。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 2.1.3
> 示例
> 文本生成:
> 生成适配任何脚码的鞋类产品名,
> 风袼模仿Steve ,Jobs (简洁。含科技感前缀如
> 'i')"
> 最终输出
> "jiFoot.
> ierfectFit , iShoeSize
> 图像生成: .生成4人商务会议场景图
> 背景为森林篝火旁,而非传统办公室"
> Nidjourney会
> 生成户外露营风格的会议图像。而非常规室内场景。
> 2.2
> 原则二:  指定格式 (Specify Format)
> 2.2.1
> 核心逻辑
> 统一4响应的输出结构,
> 确保结果可直接用于后续处理
> 如编程解析。视觉展示 ),
> 避免因格
> 式混乱导致的额外开发成本。
> 2.2.2
> 适用场景
> 1)  文本格式:  需编程处理时。捐定JSON, HAIIL , 逗号分隔列表等结构化袼式;
> 1)  图像格式:  需特定视觉风袼时,指定
> 股票照片,插画,油画, Llinecraft 风格
> 等。
> 2.2.3
> 示例
> 文本生成: "生成适配任何脚码的鞋类产品名
> 输出袼式XISON,
> 包含
> Product cescrip
> tion
> (产品描述)和
> Product
> 1a1188
> (名称列表)字段"
> 最终输出:
> IProduct
> degcription "
> pair
> Shoeg
> that
> Can
> Lit
> ay
> foot
> 812e
> IProduct
> Iame3
> [IFlexFit
> Footwear"
> Onesize Step"
> Adapt-a-Shoe"]
> 图像生成:
> 生成4人商务会议场景图,
> 风格为Linecraft 像素风 "
> Lidjourney 会生成方块化
> 游戏质感的会议图像。
> 2.3
> 原则三:  提供示例 (Provide Examples)
> 2.3.1
> 核心逻辑
> 通过 "零样本 (无示例) >单样本 (1个示例) -少样本 (多个示例) "的递进,
> 为41提供
> 确案例" 参考
> 降低其对训练数据偏差的依赖,提升结果可靠性。研究表明,
> 1个示例可使部分任
> 务准确率从10%提升至近50%。
> 2.3.2
> 关键注意事项
> 1)  示例数量: 3-5个示例可平衡可靠性与创造性。超过5个可能导致41过度拟合。限制创造性;
> 1)  示例多样性:  示例风格 /场景差异需足够,避免4生成结果局限于单一类型;
> 1) 版权问题:  图像示例需使用尤版权素材
> 如Unsplash图片 ),避免侵权。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 2.3.3
> 示例
> 生成适配任何脚码的鞋类产品名,输出格式为
> 产品描述:
> KXX; 产品名: KKX' ,
> 参考以
> 下示例: -产品描述:  能 dispense 啤酒的袱箱;  产品名: iBarFridge, jridgeBeer , jrinkBeerFridge
> 产品描述:  能在太空精淮计时的于表;  产品名:
> iallt ,
> iSpace,
> iile
> 最终41会模仿示例的
> "1-前缀+功能关联
> 风格,输出 "产品描述:  适配任何脚码的鞋;  产品名:  RitFoot, jerfectFit,
> iShoegize
> 2.4
> 原则四:  评估质量 (Evaluate Quality)
> 2.4.1
> 核心逻辑
> 建立 "生成>评估+优化"  的闭环,通过量化或定性标稚判断A1结果质量。避免低质量结果流
> 入下游环节,尤其适用于生产环境中规模化使用的提示。
> 2.4.2
> 评估方式
> 1)  于动评估:  适合主观任务
> 如产品命名 ),采用
> thlmbs-UP /down (1/0分)
> 3/5/10分制"
> 结合盲评随机化减少主观偏差;
> 1)  自动评估:  适合客观任务
> 如数学计算。文本分类) ,基于基淮答案
> grolndl trlth ) 或指标
> (成本。延迟。幻觉率) 判定,可借助OpenAI Evals等框架实现。
> 2.4.3
> 示例
> 手动评估:  用Jupyter widgets创建交互界面,对41生成的鞋名列表
> 如 " UniFit SoleStrides
> FlexiSize All-Fit Shoes
> 进行
> thumbs-UP /down
> 评分。最终统计个同提示的平均得分
> (如少样本提示平均0.6分,零样本提示平均0.2分);
> 自动评估:  对 " AI计 算数学题
> 的结果。通过编程比对标准答案,
> 统计正确率
> 如95%正确
> 牵的提示优于80%的提示 )
> 2.5
> 原则五:  分工协作 (Divide Labor )
> 2.5.1
> 核心逻辑
> 将复架任务拆解为多个单目标子步骤。通过 "多提示 /多模型串联 (4[链)
> 实现专业化分工,
> 提升每个环节的可控性与可追溯性,同时利用下同模型的优势
> 如ChatGPr 擅长文本 , Aidjourney 擅
> 长图像 )。
> 2.5.2
> 实现方式
> 1〉  任务分步:  将 "产品开发"  拆分为
> 生成名称评估名称一生成描述-生成图像"
> 1)  提示内分步:  在提示中加入
> "Let's think step br step
> 引导41分步骤推理。提升结果淮确
> 性;
> 1)  元提示:  让41生成41提示
> 如ChatGPr 将产品描述转化为LIidjournev图像提示)。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 2.5.3
> 示例
> 适配任何脚码的鞋"  产品开发全流程:
> 1。生成名称:  用少样本提示生成鞋名 (如
> "OneRit
> UltraStride Shoes
> 2。评估名称:  用提示
> 为以下鞋名按 '清晰度。记忆点,卖点契合度'  打分
> (满分10分): OneFit UltraStride Shoes
> 输出 "9/10 ('OneFit
> 直接体现适配性,
> 'UltraStride
> 传递舒适感,卖点清晰)":
> 3。生成描述:  用提示
> 详细描述 ' OneFit UltraStride Shoes
> 的设计,
> 材料与功能"
> 生成产品详情文本;
> 生成图像:  用提示 "将以下产品描述转化为Iidjourney 提
> 不:
> [步骤3的描述文本" ,
> 生成产品可视化图像。
> 2.6
> 关键总结
> 五大原则具有 "模型无关性=
> 适用于GPI-4, Nidjourney -
> Stable Diffusion 等各类41模
> 型
> 且可适配未来模型
> 如GP-尔 Nidjourney V7);
> 2。核心价值:  解决基础提示的随机性。不
> 可靠性问题=
> 同时优化成本 (减少无效token ) 与延迟 (避免复架单提示 )
*

*
> [!NOTE] [图片 OCR 识别内容]
> 3
> Chapter 2 - 大型语言模型文本生成导论
> 3.1
> 核心基础概念
> 3.1.1
> 文本生成模型定义
> 文本生成模型通过先进算法理解文本语义。生成与人类输出难以区分的内容。典型案例为ClatGPI,
> 可创作连贯;
> 上下文相关的文本
> 如对话。代码。文学内容)。
> 3.1.2
> Token与分词技术
> Toker:
> VLP 与LLAIs的基础语言单元,
> 可代表句子。单词或于词
> 如字符组合) ,核心换算
> 关系为100个Token~75个英文单词。是控制LLIIs 处理上限的关键指标。
> 分词技术 (Tokenization)
> 预处理核心步骤。不同方法适配不同场景,
> 具体对比如下:
> 表1:_主流分词^法对比
> 分词方法
> 核心优势
> 典型应用场景
> Bvte-Pair Encoding
> 〈BP卫)
> 高效处理广词汇量
> 控制Token 数量
> 早期GP系列等多数LLNIs
> ITordPiece
> 平衡词汇覆盖与Token效率
> BERT 等侧垂输入理解的模型
> SentencePicce
> 支持多语言。诚少未登录词问题
> 多语言 VLP 任务
> B卫E工作示例:
> 以单词
> 为例,
> BPE初始将其拆分为单个字符 「a,P;P1,e」,
> 通
> 过学习数据中字符共现频率
> 逐步合并高频组合
> 如发现
> 常介于
> a"和 "1"  之间,最终将
> apPl
> 作为单个Token )
> 提升模型对罕见词的生成能力。
> 3.2
> LLMs核心技术原理
> 3.2.1
> 向量表示(词嵌入)
> 定义:  将Token转换为多维数值向量。公式表示为山
> U 二
> [u, Uz;
> Un]
> 向量可捕捉单词
> 的语义与句法关系。
> 核心特点:  训练中使语义相近的词在高维空间中距离更近。例如
> virtle (美德)
> 与
> ILIoral
> (道德)
> walked (走。过去式)"与
> 'walking (走。现在分词 )
> 在向量空间中邻近。为上
> 下文理解提供数值基础。
> 3.2.2
> Transformer 架构
> 核功能:  接收词向量后
> 通过数学运算分析词与词的句法(结构)。语义(含义)  关系,生
> 成含上下文信息的新向量。
> 关键组件:
> 自注意力机制:  让句于中每个词
> 关注
> 其他所有词 (类似 "投票
> 判断其他词对自身
> 语义的重要性 )
> 觯决传统模型
> 如RAN) 无法高效处理长文本侬赖的问题。
> 结构差异:  分为 "编码器 ''
> 如BERT, 侧重输入理解)和 "解码器 '
> 如GP工, 侧重输
> 出生成) ,前者适合文本分类。后者适合文本生成。
> apple
*

*
> [!NOTE] [图片 OCR 识别内容]
> 3.2.3
> 概率文本生成机制
> 核心逻辑:  基于当前文本序列。计算下一个词的概率
> 选择概率最大的词作为输出,数学公
> 式为:
> arg IaX P(w
> UU1; 'U2;
> UUm )
> 生成流程:  重复 "计算概率>选最优词>合并上下文"步骤。例如GP1-4可基于 "写一段关
> 于海獭的故事" 的输入,逐步生成连贯文本。
> 33
> LLMs发展历程与主流模型
> 331
> 关键突破: Transformer 架构的诞生
> 2010年代末
> Google Brain团队在论文 《Attention Is AlI Yoll Jeed》 中提出 Transforer架构,
> 其 "注意力机制=
> 可直接关联文本中远距离词汇,无需顺序处理,
> 既提升了长文本理觯能力,又提
> 高了计算效率,
> 成为LLWIs发展的基石。
> 33.2
> 主流模型演进 (核心特点与案例)
> 表 2: 主流Ls核心信息表
> 厂商
> 模型系列
> 关键版术特点
> 典型案例 /数据
> OPelyl
> GPr 系列
> GPr 4 (2024年发布,90%苜分位司法考试分数298/400 )
> 支持多模态,
> 可分析图像十文本
> ChatGPr (基于RLHE 训练,专注对话场景)
> 2023年1达1亿活跃用户(0}5研宄)
> GPI4o
> 2024年5八发布,
> 处理文本/音频/视觉)
> 成本低于前代
> 名3态响宓廷快
> Google
> Gemili 系列
> 前身为Bard,
> 11.5性能接近GP1' 4
> 支持代码生成。实时搜索
> Jleta
> LlaInla 系列
> 开源模型(7/13/70亿参数) ,支持多平台部署
> 可在AIS, Hugging Hace 获取
> Anthropic
> Claude 系列
> Claude ? (10万Token上 下文窗口,支持文件上传 )
> 可总结整本书籍,深度对话更连贯
> 3.3.3
> ChatGPT的RLHE 训练流程 (经典案例)
> ClatGPT通过
> 基于人类反馈的强化学习 (RLHE ) " 实现 "有用。诚实。安全"  的对话能力,
> 核心三步如下:
> 收集演示数据:
> 人类标注者按指令标注提示词
> (如
> 向6岁儿童解释强化学
> 习" ),提供期望输出示例;
> 2。训练监督策略:  用演示数据微调预训练G卫工-3模型,使其学会遵循
> 指令输出;
> 3。强化学习优化:  收集模型多个输出并由标注者排序
> 训练
> 奖励模型 (RNI)" , 再
> 用PP0算法优化模型。最大化奖励分数。
> 3.4
> 练资源与硬件支撑
> 3.4.1
> 训练需求 (以GPT-4为例)
> 数据量:  训练数据需填满约650公里长的书架;
> 参数规模:  约1.7万亿参数 (相当于3万个足球场大小的Excel表格 );
> 成本:  训练成本约6300万美元;
> 风险提示:  训练数据可能携带来源偏见=
> 需人类监督确保伦理应用。
> ILuet
> 7时
*

*
> [!NOTE] [图片 OCR 识别内容]
> 3.4.2
> 硬件市场格局
> 核心硬件: GPT
> 图形处理器),因需高效处理神经网络的张量运算, ATIDIA
> 如H100 Tell
> SOI
> Core GPTJ) 成为主流;
> 趋势: GP[需求远超供给。推动专用41硬件发展
> 如Coogle TPUs) , 微软, Jeta等巨头重
> 金投入硬件研发。
> 3.5
> 开源模型与技术优化
> 3.5.1
> 开源模型的
> '双刃剑"  效应 (以Ieta Llama为例)
> 优势: @普及41技术。中小企业 /开发者可免费使用; @全球社区协作优化,
> 快速修复漏洞;
> 风险:  可能被恶意利用生成虚假信息。恶意代码,
> 需平衡开放与管控。
> 3.6
> 关键优化技术
> 量化 (Quantization): 降低参数数值精度
> 如从32位浮点数降为8位) ,
> 在不显著损失性能
> 的前提下缩小模型体积;
> LORA
> (低秩近似):  优化网络架构。使模型可在消费级电脑上运行,降低微调门槛。
> 37
> 模型对比与核心注意事项
> 37.1
> 模型能力对比 (典型案例)
> 输入需求: "为
> 适配任意脚码的鞋亍
> brainstorm 3个Steve Jobs风格的产品名,格式为
> Product lallles:
> [名称列表]' ,
> 名称需以
> 'i' 开头
> GPr 4输出 (完全符合要求): Product
> LLaIIICS;
> ji; iShoe; jlexible;
> Claude 3输出 (部分符合): Prodluct nares: ji, iComfort, iSole;
> Llala 3 708输出 (格式不符):  含多余描述文字
> 名称含 " OneSize
> (非"i开头)。
> 结论:  目前OpenAI GPT-4在遵循指令精度上领先。开源模型潜力逐步提升。
> 3.7.2
> 核心注意事项
> 数据隐私: LLNIs可 能用输入数据重新训练或微调
> 严禁输入敏感信息
> 如身份证号,
> 商业
> 机密);
*

*
> [!NOTE] [图片 OCR 识别内容]
> Chapter 3
> ChatG卫T文本生成的标准实践
> 4.1
> 基础:  列表生成的优化
> 核心问题:  默认列表存在格式混乱
> 如6卫工自动输出30个编号项,
> 含{分隔)。冗余评论
> 如
> Sure; Iere is a list.. 
> 〉。数量失控。信息混杂 (部分角色带电影名) ,
> 导致下游解析困难。
> 优化方案:  通过精准提示明确4点要求
> 格式:  指定项目符号 (如*)
> 避免编号;
> 数量:  固定列表长度 (如 "5个男性迪士尼角色" );
> 内容:  仅保留核心信息 (如 "仅角色名,不含对应电影" );
> 冗余排除:  禁止前置 /后置评论。仅返回列表。
> 示例效果:
> 输入优化提示后
> 输出为
> TToody
> Bulzz Liglityear
> Stitch
> Jack
> Prilce
> Clarming
> 无额外信息
> 4.2
> 结构化数据生成与解析
> 4.2.1
> 层级列表 (Hierarchical List )
> 核心应用:  生成嵌套式文档大纲
> 如 "数据工程的好处" ),含 "一级标题+二级于标题"  结
> 构。
> 关键提示词:
> 'Wierarclical"
> 引导生成嵌套结构;
> eicredibly detailed=
> 至少10个顶级杯题" =
> 确保细节度与长度。
> Python解析:  用正则表达式提取标题
> 匹配工'*(.+)')与亍标题
> 匹配工'8+ [a-2] |
> (+)' ),
> 转换为宁典。
> 注意事项: LLNI可 能不遵循数量要求
> 需代码适配
> 验证数量或灵活处理长度)。
> 4.2.2
> JSON生 成与解析
> 核心要求:  输出可直接被Prtlon json模块觯析,无语法错误。
> 关键提示约束:
> 仅返回有效JSOV, 无额外文本;
> 禁止反引号()包裹;
> 明确 "适配jsou.loads()
> 常见错误:  无效Payload
> (如缺少逗号)。含代码块标记
> 需提示规避。
> Python解析:  苴接用jsou.loads(openai_json_result )加载,
> 输出为宁典。
> Sparrow
*

*
> [!NOTE] [图片 OCR 识别内容]
> 4.2.3
> YAML生成与数据过滤
> YANL 优势:  无需转义字符
> 可读性高。支持注释。
> 核心应用:  基于Sclema过滤数据
> 完全匹配:  返回符合Sclera的 YANIL;
> 部分匹配:  仅保留一
> 致项;
> 无匹配:
> 返回 " Vo Iters
> 错误处理:  自定义异常
> 如IuvalidResponse , InvalidltemMame等
> 4.3
> 多样化格式生成
> LIermaid流程图:
> 示例输入
> 生成点餐流程"
> 输出
> grapl TD ClooseFood[Cloose Food]
> >
> AddToCart[Add to Cart] AddToCart
> ConfirmCart[Confiim Cart] ConfirCart
> Pay-
> For』leallPay for JIeal]
> 可直接渲染。
> 模拟081数据:  示例输入 "5名学生信息
> (uallle,age,grade -
> 输出结构化CST表格
> 如
> IIallle,
> ,age;grade| |John;16,A |Alex;17,8" )。
> 4.4
> 核心提示工程技巧
> 4.4.1
> 简化解释: "Explain It like I'
> Five
> 目的:  将专业文本转换为5岁儿童可理解的通俗语言。
> 示例:
> 原交本
> 癌症治疗传统上基于肿瘤细胞=
> 一简化为
> 癌症是细胞不正常生长
> 医生用
> 切。吃药等方法处理"
> 4.4.2
> 上下文请求
> 场景:
> LLI信息不足时,
> 引导其主动索要关键参数
> 如选择LIongoDB /PostgreSQL 需的数据
> 结构。扩展性等)。
> 流程:  用户初始输入LU请求补充>用户提供上下文LU生成精准建议。
> 4.4.3
> Least to MIost (分步生成)
> 逻辑:  拆解复杂任务为多步骤
> 基于前一步输出生成后一步内容。
> 示例: Flask项目笫一步生成架构'第二步生成代码'第三步生成测试用例。
> 4.4.4
> 角色提示 (Role Prompting)
> 定义:  为LL分配特定角色
> 如技术评审员 ),输出专业内容。
> 示例:  扮演1o180DB评审员。输出特征。优缺点。竞品对比。
> 挑战:  维持角色一致性。避免偏见
*

*
> [!NOTE] [图片 OCR 识别内容]
> 4.4.5
> 避免幻觉
> 核心策略:  仅基于参考文本回答
> 无信息则返回
> Could Iot Wd
> 81 aISTeI
> 进阶方案:
> 要求标注引用来源
> 如回答核反应堆定义时。附带原交引用 )。
> 4.5
> 文本处理:  分块 (Chunking)
> 4.5.1
> 分块的核心价值
> 适配LLAI上 下文窗口:  避免输入超上限或输出截断;
> 降低成本:  减少token使用,降低4卫I费用;
> 提升性能:
> 减轻工』I负载,加快响应;
> 增强灵活性:  按任务定制块大小。
> 4.5.2
> 分块策略对比
> 按句子分:  优势是保留上下文,劣势是长文档效率低。适用摘要
> 翻译;
> 按段落分:  优势是处理长内容高效。劣势是粒度粗,适用文档分析;
> 按主题分:  优势是精准分离主题,劣势是需先识别主题。适用分类;
> 按token分 (tiktoken ): 优势是适配Ope.4[模型。劣势是复杂度高。适用GPr系列任务。
> 4.5.3
> 关键工具与实现
> SPaCi:
> 加载en_core_web_s皿模型。用doc.sents 提取句子。实现按句子分块;
> tiktoken:   支持Open4I编码。实现token统计与分块;
> 滑动窗口分块:  固定窗口大小
> 如20字符)与步长
> 如5字符),生成重胥块减少信息丢失。
> 4.6
> LM典型应用场景
> 4.6.1
> 情感分析
> 优化方法:
> 预处理 (去特殊字符。转小写。纠错) ,提供示例。约束输出格式。
> 挑战:
> 处理讽刺
> 上下文依赖。
> 4.6.2
> 分类任务
> 核心策略:
> 零样本学习:  无示例。基于预训练知识分类;
> 少样本学习:  提供3-5个示例,定义规则。
> 优化:  多数投票>多次请求。取高频结果。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 4.6.3
> 元提示生成
> 定义:  生成
> 提示的提示" =
> 用于多模态内容生成。
> 示例:  儿童绘本 +生成文本+生成图像提示 +生成插图 +组合绘本。
> 4.7
> 质量评估与优化
> LLMI自I 评:  提示LLMI critique 自 身输出,迭代改进;
> 跨模型评估:  用GPr-4评估GPr-3.5输出 (如评估简洁性);
> 成本平衡:
> 优先程序式评估
> 如统计长度) ,
> 复杂场景用工1[评估。
> 5
> Chapter 5
> 向量数据库与检索增强生成
> (RAG)
> 5.1
> 向量数据库与检索增强生成 (RAG) 核心概念
> 5.1.1
> 向量数据库定义与价值
> 定义: -种特殊数据库,
> 以 "向量" 形式存储文本 (或图像)数据,核心能力是基于语义相
> 似性而非关键词 /1查询数据。
> 核心价值:
> 解决LLMI "幻觉问题"
> 通过引用模型未训练的外部数据,避免41凭空生成信息;
> 突破token限制:  无需将所有数据放入prompt, 仅检索最相关内容,
> 降低成本
> 3.5-t41b0仅4k token, gpt-4-110G-preview 虽128k token但成本为gpt-3.5的10倍);
> 典型应用场景:  文档阅读 (提取相关片段)。相似产品推荐。对话长期记忆 (存储历史聊
> 天记录)
> 向量本质:  文本的高维数值列表
> 如OpenAI的text-embedding-ada-002模型生成1536维向量) ,
> 可类比 "语义坐标
> 训练数据中关联的文本向量距离更近
> 如
> IlIOLSC
> 与
> mickey mouse
> 无关文本距离更远
> 奶
> IIOLLSC
> airplalle
> 5.1.2
> 检索增强生成 (RAG) 原理与作用
> 定义:
> 向量数据库的核心应用,
> 通过 "相似性搜索+检索相关文档'插入prompt 作为上下
> 文"  的流程,
> 让LLN基于精准上下文响应。
> 核心流程 (以聊天机器人记忆为例):
> 1。用户提问 "我的名字是什么? " (3000条历史消息无法全部放入prompt ) ;
> 2。将问题转为向量。在向量数据库中检索t0P-3相似历史消息
> 如 "我的名字是ike =
> "我
> 的狗叫Hercules
> e我的同事叫James
> 将检索结果作为上下文插入prompt , LLM仅基于该上下文回答
> 你的名字是』Like
> 关键作用:  解决LLMI
> 失忆。问题
> 避免无关toke浪费。提升响应准确性与相关性。
> 如gpt-
*

*
> [!NOTE] [图片 OCR 识别内容]
> 5.2
> 嵌入模型:  向量的生成器
> 5.2.1
> 主流嵌入模型对比
> 模型类型
> 代表模型
> 向量维度
> 成本/获取方式
> 适用场景
> 商业模型
> Opclll
> tCxt-
> 1536
> $0.000L/l000
> LoICII
> 通用场景。精度高
> Clbeddilg-ada-002
> (4P[调用)
> 开源模型
> IlBgirg
> EaCe
> Serl
> 381
> 免费 (4PI/本地部署)
> 成本敏感场景
> tCIICC IralisforllCrs
> 开源模型
> (crlsiri IVord2lcc
> 自定义
> 如100)
> 免费 (本地训练)
> 领域特定交本
> 如0-
> rlor语言 )
> 开源模型
> spaCy Glole
> 300
> 免费
> (基于Commorl
> 基RMLP 场景
> Crail训练)
> 表3:  主流嵌入模型对比表
> 5.3
> 嵌入模型核心特性
> 上下文敏感性:  现代Trausformer 模型生成的向量具有上下文相关性,例如
> balk
> 在
> riverbalk =
> (河
> 岸)和 " financial balk 
> (银行)中向量不同。
> 向量类型:
> 稠密向量:  几乎所有维度非零
> 语义信息丰富
> 如Open4I模型) 
> 主流41应用首选;
> 稀疏向量:  高维度
> 如10万+),多零值,适合关键词搜索;
> 混合搜索:  结合稠密与稀疏向量优势,近年逐渐流行。
> 自定义模型需求:  当文本含领域特定词汇
> 如Q-Anon的特殊表述)时。需基于专用语料训练
> 自定义模型
> 如用Tord2Vec训练 ) =
> 5.4
> 向量数据库工具:  向量的存储与检索
> 5.4.1
> 源工具: FAISS (Racebook AI Similarity Search)
> 核心特性:  支持工2距离
> 欧氏距离
> 相似性搜索,本地部署,轻量易用,
> 适合原型开发与小
> 规模数据。
> 关键功能:
> 一索引创建:  基于向量维度初始化索引
> 如1536维);
> 一索引保存/加载:  避免重复生成向量
> 降低成本;
> 索引合并:  支持多个索引合并
> 如批量更新文档 )。
> 5.4.2
> 托管工具: Pinecone
> 核心优势:
> 云端托管。无需维护基础设施, 支持自动扩展。高可用性,元数据过滤。适合生
> 产环境。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 关键参数:
> 维度:  需与嵌入模型匹配
> 如text-embedding-ada-002对应1536维);
> 相似度度量:
> 默认余弦相似度;
> 元数据格式:  支持宁符串。数宁(64位浮点数)。布尔值。宁符串列表。
> 5.5
> 文档处理与进阶检索机制
> 5.5.1
> 文档分块策略
> 核心目标:  乎衡
> 上下文完整性 =
> 与 '语义特异性=
> 分块过大易导致向量
> 均值化" (丢
> 失细节 )
> 过小易切断句于/段落 (丢失逻辑)。
> 常用工具: LangChain的RecrsiveCharacterTextSplitter, 按
> 换行符-空袼+宁符'  优先级
> 拆分, 优先保持段落 /句子完整性。
> 5.5.2
> 元数据设计
> 作用:  辅助过滤检索结果。提升相关性 (如按
> 文档页码"
> 聊天机器人I" "时闻戳"  筛
> 选)。
> 设计原则:
> 仅存储关键信息:  避免冗余
> 如仅存
> batch
> text
> Page_Illllh
> 不存人段文本 );
> 适配检索需求:  若需按时间筛选, 需存储
> tirnestaInP
> 宁段。
> 示例: Pinecole 插入时的元数据格式
> ("batoli" : 0
> text':
> 分块内容"
> page_Illl" 
> 5 )。
> 5.5.3
> 迸阶检索机制
> 检索机制
> 核心逻辑
> 优势与局限性
> 自查询检索 (Self-Query
> LA自动提取查询中的元数据过滤条
> 优势:  无*于动写过滤规则;  局限:
> 件,结合语义搜索
> 定义清晰的元数据schema
> 多查询检索
> (JIulticuer)
> 为单个查询生成多视角子耷询。扩大相
> 优势:  覆盖更多相关内容;  局限:  可能
> 关文档菀围
> 产生重复 /矛盾结果
> 集成检索
> Ensemble )
> 组 ^合  多 ^个  检 ^索 ^器
> 优势:  乎衡不同算法优势;
> 局限:  计算
> 如IISS |Pinecone )
> 结某,
> 加权
> 量大
> 检索速度慢
> 融合
> 上下文压绡检索
> 压缩文档中无关部分, 仅保留与查询相
> 优势:
> 减少prompt 冗余token;
> 局限:
> 关内容
> #精准判断"相关性"
> 表 4: 进阶检索机制对比表
> 5.6
> 章节总结
> 核心逻辑:  向量数据库通过 "文本+向量>相似性检索
> 流程;
> 为』提供动态上下文;
> 解
> 决幻觉与token 限制问题,
> 核心应用是R46。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 关键选择:
> 嵌入模型:  通用场景选OpeuAI text-embedding-ada-002, 成本敏感选开源模型;
> 向量数据库:
> 原型开发用FAISS
> 生产环境用Piecole;
> 分块策略:  优先用LangChain的RecursiveClaracterTextSplitter,
> clllnk_size适配ILAIto
>  ken限制。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 6
> Chapter 6
> 具备记忆与工具的自主智能体
> 6.1
> 思维链推理 (Chain-of-Thought; Cor)
> 6.1.1
> 定义与核心价值
> 思维链推理 (CoT) 是引导大型语言模型 (LLAIs) 通过一系列逻辑步骤或连接达成结论
> 解
> 决问题的方法。核心作用在于:
> 将复杂问题拆解为更小。可管理的组件,
> 使工』聚焦每个部分=
> 提升理解深度;
> 适用于需多因素考量或深度上下文理解的任务
> 如营销计划制定。问题诊断)。
> 6.1.2
> 实践要点与示例对比
> CoT实现有效输出需满足两个关键条件:
> 明确的步骤引导指令
> 如提示中包含
> step-by-step
> 充足的上下文信息 (如任务耳标。蓣算。产品特性 )。
> 通过
> 新软件产品营销计划
> 示例对比C01的有效性:
> 1。无效输出 (无CoT): 输入仅为
> 为新软件产品创建营销计划"
> LN输出通用策略 (无针对
> 性):
> 启动社交媒体 campaign
> 发送邮件
> newsletter
> 提供限时折扣
> 与网红合作
> 组织线上斫讨会
> 2。有效输出 (含CoT): 输入补充上下文
> 面向中小企业的项目管理软件。预算$20.000。聚焦数
> 宁渠道"
> LN输出结构化步骤 (针对性强):
> 市场调研
> 分析竞品及其营销策略
> 挖掘项目管理软件的独特卖点
> 定义目标用户及痛点
> 品牌与信息传递
> 构建统一品牌标识
> 设计针对用户痛点的话术
> 制作官网,
> 博客。社交媒体内容
> 邮件营销
> 制定潜在客户培育策略
> 向新用户发送含使用技巧的个性化引导邮件
*

*
> [!NOTE] [图片 OCR 识别内容]
> 6.2
> 自主智能体 (Agents) 基础
> 6.2.1
> 智能体定义与运行逻辑
> 智能体是在特定环境中
> 感知-行动-诀策"  以实现预设目标的41实体,核心运行逻辑为 "行
> 动-观察
> 循环,
> 伪代码如下:
> Iext
> aCtion
> agent . Bet
> aCtion ()
> Hhile
> Iext
> action
> AgentFinish:
> Observation
> LUI
> (next_action )
> %执行动作并获取观察结果
> IeZt
> action
> agent . Bet
> aCtion (.
> Iext
> action ,
> observation )
> %基于观察调整动作
> Tetlrn
> Iext
> action
> 6.2.2
> 智能体三大核心组件
> 智能体的行为由以下三个组件决定
> 具体定义与示例如下表:
> 组件
> 定义与示例
> 环境中的感官刺激或数据=
> 是智能体决策的基础:
> 自动驾驶:  掇像头, LIDAR , 超声波传感器提供的 "车辆。行
> 人,路况 "  数据;
> 输入
> (Illplts
> LLN眢能体:
> 文本输入 (含视频转录文本。数据结构转文本
> 等) =
> 眢能体的行动指导原则,分 "目标导向"  和 .奖励导向" =
> 目标导向:  自动驾驶
> 安全高效从4地到召地 
> 目标 /奖励函数
> 奖励导向:  特斯拉以
> 无人工干莰行驶里程
> 为正奖励, "急刹
> 偏离车道"  为负奖励。
> 智能体允许执行的行动范围。取决于任务场景:
> 可  用 ^动
> 作
> 自动驾驶:  加速。减速。转弯,娈道;
> (Actiols)
> LLN昝能体:
> A卫I调用。数据库读写。文件操作。
> 6.2.3
> LLN智能体特有组件
> LL智能体除三大核心组件外。还需以下特有模块支撑复杂任务:
> 记忆 (Lemory): 存储智能体步骤间的状态
> 如聊天机器人的对话历史),提升用户体验;
> 规划 /执行策略:  多路径实现目标。需结合
> 任务拆解
> 与 "动作执行";
> 检索 (Retrieval):
> 调用外部数据
> 如向量数据库的语义相似检索, SQI数据库的自定义信息
> 提取) =
*

*
> [!NOTE] [图片 OCR 识别内容]
> 6.3
> ReAct框架
> 6.3.1
> 框架定位与核心逻辑
> ReAct是CoT的改进框架。核心是
> 推理+工具动作
> 结合
> LLL通过工具执行动作后生成
> 观察结果。再基于观察调整后续推理。解决纯C01缺乏外部交互的问题 =
> ReAct的思维循环需遵循固定步骤 (迭代至问题解决或达最大次数):
> 1。观察环境
> 如用户问题。工具执行结果);
> 2。基于观察解读环境 (形成 "思维" =
> 如
> 需搜索用户年龄" );
> 决策需执行的动作 (选择工具;
> 如
> google_search
> );
> 4。执行动作并获取新观察;
> 5。重复步骤1-4,  直至输出
> 最终答案"
> 6.3.2
> 提示模板与Python实现
> 提示模板设计
> ReAct 提示需包含以下关键娈量
> 要求工^结构化输出:
> Yo1l
> N111
> S0IVe
> the
> question Using chain-of-thought reasoning, following
> th13
> pattern:
> Obsere
> the original
> question:
> original_question: {question}
> Create
> 3I
> observation:
> observation:
> [Jour
> obseriation]
> Create
> thought:
> thought:
> [your thought]
> Use tools
> to
> aCt:
> action: {too1_
> Iame」
> aCtion
> input:
> {tool_input}
> Do
> IOt
> B1e55
> to01
> results.
> You
> have
> aCCe53
> to these
> to018:
> {too1s}
> If
> Jou find
> the
> aISTCI
> Tetlrn:
> II've
> found
> the
> aISTer :
> [final
> aISWer ]
> 其中 _
> {tools}需列出工具名及功能
> 如
> SCATCII
> UIL_
> google: 用于搜索实时信息" )。
> Python实现关键步骤
> 以 "查询 Jason Derlo是否有伴侣
> 为例
> ReAct 实现分三步:
> 1。提取动作与输入:  用正则表达式从工N输出中提取工具名和参数 (忽略大小写。空格差异 ):
> inPort
> 工e
> def
> extract_1ast
> action
> and_input (text )
> 匹配action
> 如 "Action:
> Search
> OI
> Boogle"
> action
> pattern
> 工e
> compile (r" (?i)action |8*: |8*([^In]+) "=
> Le
> MUJLTILIIE)
> 匹配action_Input
> 如 "action_input
> Jason
> Derulo relationship
> Statlls "
> action_input_pattern
> 工e .
> compile (r" (?iaction |3*_*input | 5* : |5* ([ ^|n] +) "
> re . MULTILIIE )
> actions
> action_Pattern . findall(text )
> aCtion
> inputs
> action_input_Pattern . findall (text )
> Leturn
> Iaction"
> actions [-1]
> i
> aCtions
> e13e
> None
> "action_input
> action_inputs [-1]
> 讧
> action
> inputs
> e18e
> Ione
*

*
> [!NOTE] [图片 OCR 识别内容]
> 调用工具执行动作:  定义工具函数并执行, 获取结果:
> 定义BooBLe_search工 具 (示例返回模拟结果 )
> def
> SearCh
> On
> Boogle (query:
> Str )
> retlrn
> Jason
> Derulo
> doe3n
> have
> Vife
> OI
> Partner
> 从LLM输出提取动作 (假设L[M输出选择search_
> OI_BoOBLe )
> 11m
> Output
> Observation:
> e
> aon 't
> LIOTT
> Jason
> Derulo
> relationship
> Stat15
> thought: Weed
> to
> Search
> for ni3
> Current
> relationship-
> action:
> Search
> OI
> BooBIe
> aCtion
> iPut:
> Jason
> Derulo
> CuITeIt
> relationshiP
> Statlls
> t001
> info
> extract_
> 1a5t
> aCtion
> and_input (1Im_output )
> tool_result
> Search
> On_BooBle (tool_info ["action_input" ] )
> 3。生成最终答案:  将工具结果反馈给LLAI, 触发最终答案输出:
> I II |
> Current
> Prompt
> Based
> OI
> t001
> result: {too1_
> re811t}
> Return
> the final
> aISNeI
> Tith
> pattern:
> "I've
> found
> the
> aISeI
> [content]
> II / |
> # LLN输出:
> III'Te
> found
> the
> aIISeI
> JaSOI
> Derulo
> doesn
> have
> Vife
> partner
> 6.4
> 工具使用 (LangChain)
> 6.4.1
> 工具的核心价值
> LLA默认仅能生成文本,工其可扩展其能力边界:
> 实现
> 文本生成外的动作":
> 如数据库交互。文件读写
> 4卫I调用
> 如Trilio发送短信 );
> 补充实时 /私有数据:  如通过Google搜索获取实时信息.
> 通过50工其查询企业私有数据。
> 6.4.2
> Chain工 具的三种创建方式
> Chain支持自定义工具。预瞿工具
> 工其集 (Agent 'Toolkits ) , 具体示例如卜:
> 1。自定义工其:
> 以 "字符计数工其" 为例,
> 用To01 .from_function封装函数:
> from  lanBchain. tools
> import Tool
> #  定义字符计数函数
> def
> COlIIIt
> Characters
> -
> string (string)
> Letllrn
> len
> I(string)
> 封装为Langchain工 具
> LangC
> 1418
*

*
> [!NOTE] [图片 OCR 识别内容]
> C18tom
> t001
> Tool . from_
> function (
> Iame=
> Count
> Characters
> i String"
> 工其名 (需清晰)
> Hunc=count
> Characters
> 1
> string,
> #  绑定函数
> description=" 用于计算文本字符串的字符数量"
> 功能描述 (帮助LIM选择 )
> 预置工其:  直接使用LangChain 提供的工具
> 如Calculator ) , 基于LLMathChain实现数学计
> 算:
> from IanBchain. Chains
> ImPOIt
> LLUllathChain
> from langchain_openai
> Chat
> models
> import ChatOpenAI
> #  初妗化ILM
> 11m
> ChatOpenAI (temperature=0 )
> #  创建Calculator工 具 (绑定数学计算链 )
> Calculator
> t001
> Too1 (
> Iame=
> Calculator"
> func-LLUNathChain .from_11m(11m=11m)
> LUIII ,
> description=" 用于解决数学计算问颞
> 如加减乖除_
> 方程求解 )
> 工具集
> Agent 'Toolkits ): 多工其掴绑,用于特定场景
> 如CST分析, SQ工操作):
> CST Agent: 分析CST文件,需安装依赖pip install
> Chain
> experimental Pandas:
> from  Iangchain
> experimental. aBents . agent
> toolkits
> import
> Create
> CST
> aBent
> Irom Langchain_openai
> Chat
> models import ChatOpenAI
> 创建CSV ABent
> 分析heart_
> disease
> UCi
> CSV )
> CST
> aBent
> Create
> CSV_agent (
> 1Im=ChatOpenAI (temperature=0)
> path= "data/heart_
> aisease_Ici
> CSTII
> Verbose=True
> 调用ABent:  查询数据行数。生成相关矩阵
> CST
> aBent
> invoke ("该文件有多少行数据? ")
> # 输出: 920
> CST
> aBent
> invoke ("生成数据的相关矩阵并保存到文件")
> #  输出:  保存至correlation
> matrix
> CST
> SQL Agent: 操作50工数据库
> 需安装依赖pi
> install langchain-community
> PJmonBo:
> Iangchain. aBents
> imPort
> create_SqI_aBent
> from  Iangchain_
> community . agent_toolkits
> imPort
> SQLDatabaseToolkit
> from  Iangchain.
> database import
> SQLDatabase
> LanB
> from
> 591
*

*
> [!NOTE] [图片 OCR 识别内容]
> 连接SQLite数据库
> Ab
> SQLDatabase
> IrOm
> uri ("sqlite: 111
> /aata
> demo
> 4b" )
> 创建50 Toolkit
> Sq1_toolkit
> SQLDatabaseToolkit (ab=db,
> IIm=ChatOpenAI (temperature=0) )
> 创建50
> ABent
> 8qI_aBent
> create_sqI_agent (
> 11m=ChatOpenAI (temperature=0)
> toolkit=sqI_toolkit 
> Verbose=True
> 调用ABent: 新增用户
> 查询用户
> 891_agent . invoke ("添加5个用户
> (John,
> Mary
> Peter
> Pall ,
> Jane
> 到Ugerg表")
> 591_agent . invoke ( "查询数据库中是否有Peter ?
> #  输出:
> 存在
> 显示Peters详
> 细信息
> 6.43
> 工具使用注意事项
> 工具命名与描述需 "表达性强"
> 如
> Colnt
> Claracters 讧
> 比
> CharCount
> 更易
> 被工^理解;
> 控制工其数量:  过多工其会导致LA混淆
> 建议按场景分类
> 如
> 通信类"  含 Twilio,
> 数据
> 类"  含SQL/CSV );
> 验证工具输入:  用Prdantic定义参数 schemna
> 如限制文件类型为pdf/txt ) ,避免无效调用。
> 6.5
> LLM作为API (OpenAI Functions) 与智能体类型对比
> 6.5.1
> OpenAI Functions的核心特点
> OpenAI Functions是基于微调LLA
> 如gt-3.5-turbo-0613, gt-40613)  的工其调用方案,核
> 心优势:
> 输出结构化JSOV: LN直接生成符合函数参数格式的JSOV, 无需正则提取;
> 艾持并行调用:
> 可在单个4卫[请求中调用多个工具
> 如同时查询 "北京天气"  和 "上海天
> 气" );
> 易集成对话:  适合嵌入聊天机器人,
> 自动判断是否需要调用工具
> 如
> 今天星期几"  无需调
> 用,
> 实时天气
> 需调用)。
> 6.5.2
> LangChain主流智能体类型对比
> LangChain 支持多种智能体类型。适配不同场景。核心类型如下表:
> Strine
*

*
> [!NOTE] [图片 OCR 识别内容]
> 智能体类型
> 描述与适用场景
> 基于微调模型。输出J50^函数调用;  适用于开源模型
> 单工具
> OpenAI Fiinctiols
> 任务
> 如简单搜索);己被OpenAI Tools 替代。
> OpenAI Fnctions的增强版,
> 艾持多工具调用
> 提升响应效率;
> OpenAI Tools
> 适用于新模型
> 需高效工具交互的场景。
> 适配擅长X工的模型
> 如Anthropic Claude ) , 输出XAI格式动
> XIII Agent
> 作;
> 适用于非结构化工具 (仅接受单字符串输入 )
> 支持多输入工具;
> 需结构化输入 /输出;
> 适用于复杂任务
> 如
> Structured
> Clat
> 根据用户卫查询订单+生成报表" )。
> 实现Re4ct逻辑
> 依赖搜索/文档工具
> 如Tarily Search); 适用
> ReAct
> 于多步骤工具交互 (如故障排查)。
> 用Intermediate Answer工 具解诀事实问题;
> 适用于快速获取准
> Self  48k vith Search
> 确事实
> 如 "地球半径是多少" )=
> 6.5.3
> OpenAr Eunctions与ReAct的核心差异
> 两者在工具调用逻辑上存在显著差异
> 适用场景互补:
> 对比维度
> OpenAI Functions
> Reuct
> 低 (无需正则提取,
> JSON直接解
> 高 (需设计思维循坏。正则提取动
> 实现难度
> 析 )
> 作)
> 单次决策 (是否调用工具) ,
> 无迭
> 多步骤迭代
> (观察思维动
> 工其调用逻辑
> 代
> 作+观察 )
> 并行调用
> 支持 (单个请求调用多个工其)
> 不支持 (仅支持顺序调用)
> 多意图处理
> 支持 (需明确函数参数)
> 更优 (逋过思维循环拆解多意图)
> 单步工具任务 (如天气查询。数据
> 多步复杂任务 (如 "保存访谈发
> 适用场景
> 提取 )
> 送邮件-+生成摘要" )
> 6.6
> 记忆机制与LangChain记忆类型
> 6.6.1
> 记忆的分类与核心作用
> LL智能体的记忆分
> 长时记忆 (LTNI)
> 和
> 短时记忆 (STNI)
> 功能互补:
> 长时记忆 (LTM):
> 定义为
> 长期存储的海量数据"
> 核心作用是提供外部知识支撑。常见应
> 用:
> 向量数据库:  存储非结构化文本
> 如企业文档 )
> 通过语义相似度检索相关信息;
> 自定义检索器:  按 "相关性。时间。任务目标
> 优先级提取数据
> 如优先检索近3个月的
> 用户反馈);
> 自我反思:  存储LNI的分析结论
> 如用户偏好总结),用于个性化推荐。
> 短时记忆 (STNI):
> 定义为 "临时工作区"
> 核心作用是维持上下文连续性,常见应用:
> 对话历史:  聊天机器人存储前序对话
> 如用户说 "我川James
> 后续可回答
> Jallles,
> 需要什么帮助?" );
> 重复避免:  相同查询时返回一致结果
> 如用户重复问
> 软件价格" -
> 无需重新调用工
> 具)。
*

*
> [!NOTE] [图片 OCR 识别内容]
> 6.6.2
> Chain核心记忆类型
> Chain 提供多种记忆实现。适配不同场景。核心类型及特点如下:
> 记忆类型
> 核心特点
> 适用场景
> ConversationBuffer』Iemory
> 无长度限制,
> 存储完
> 短对话
> (如客服单次咨
> 整  对  话;
> 可 返 回  字  询)。
> 符  串
> 或1[e3888e对
> 象
> 如HumanlIessage ) 
> ConversationBuffer TTindowlIemory
> 仅  保  留  最近正次 交  互
> 只需短期上下文的场景
> 如正-3,
> 仅存最后3轮对
> 如临时任务) =
> 话 );  防止缓冲过大。
> ConversationSummary』lemory
> 实时总结对话
> (如"用户
> 长对话
> 如10轮以上的咨
> 问价格,AI回复899" ); 节
> 询)。
> 省token。
> ConversationSullmary Buffer』Iemory
> 混合"缓冲+总结" :
> 近期
> 需长期维护对话且内容较
> 对话保留完整;
> 早期对话
> 长的场景
> 如用户长期跟
> 自动总结 (按token限制触
> 进)。
> 发)。
> ConversationTokenBuffer』Iemory
> 按token长 度  限  制  缓  冲
> 严格控制token消耗的场景
> 如max_token_limit-100 );
> 如4卫I成本敏感 )
> 超过则清空旧内容。
> 6.7
> 高级智能体框架
> 6.7.1
> 计划-执行智能体 (Plan-and-Execute)
> 计划-执行智能体将 "任务规划"与 "动作执行"  拆分为两个独立模块
> 分别由不同LL处理,
> 核心优势是 "复杂任务拆解更清晰
> 以BabvAGI ( 经典计划-执行框架)  为例,架构逻辑如下:
> 1.步骤1:  拉取未完成任务 (从任务列表中获取首个任务);
> 2。步骤2:  执行任务 (execution_agent 调用OpenAILLM, 结合向量数据库上下文完成任务);
> 3。步骤3:  存储结果 (将任务结果存入Chroma /Teaviate 向 量库,用于后续任务);
> 4.步骤4:  创建新任务 (task_creation_agent基于且标和前序结果。生成新任务列表);
> 5。步骤5:  优先级排序 (prioritization_agent调整任务顺序,确保对齐核心目标);
> 循环步骤1-5,
> 直至任务完成。
> 6.7.2
> 思维树 (Tree Of Thoughts, ToT)
> ToT突破传统
> 线性推理
> 局限,
> 允许工1[探索多
> 思维路径" (连贯文本块) ,
> 核心是
> 回溯
> 与调整"
> 适用于复杂问题解决。
> Lang
> Langc
*

*
> [!NOTE] [图片 OCR 识别内容]
> 核优势与实验效果
> 多路径探索:  LLNI可 生成多个
> 思维分支"
> 如解决24点游戏时,尝试不同数字组合);
> 自我评估:  每步思维后-
> LLN评估路径可行性
> 如 "该组合无法得到24,放弃此路径" );
> 实验效果:  在24点游戏中, GPI-4用CoT成功率仅4%,用ToT 提升至74%;  在迷你填字游戏
> 中。成功率提升30%十。
> 实现逻辑
> ToT 的实现需三个关键步骤:
> 1。思维分解:  将问题拆解为多个 "思维步骤" (如填字游戏的
> 先填横向词->再填纵向词" );
> 2。分支生成:  每个步骤生成多个可能的思维
> 如横向词的3种候选答案);
> 评估剪枝:  删除不可行的思维分支
> 如候选答案与纵向词冲突) ,迭代至找到解决方案。
> 6.8
> 回调函数 (Callbacks) 与Token计数
> 6.8.1
> 回调函数的核心作用与类型
> 回调函数用于监控智能体运行的全生命周期。便于调试
> 目志记录和指标统计, LangChain的
> 核心回调类为BageCallbacklandler。
> 关键回调方法
> On_11m
> Start:
> LLNI开F始运行时触发 (记录请求参数);
> OI
> t001
> end:
> 工具执行结束时触发 (记录工具输出 );
> OI
> Chain
> eTIOI:
> 链运行出错时触发 (捕获异常信息 );
> OI
> agent
> finish: 智能体完成任务时触发 (记录最终答粲)。
> 回调函数的两种作用范围
> 1。全局回调 (绑定实例):  作用于智能体 /链的所有请求。适用于全局监控
> 如日志记录):
> Irom  Ianechain.agents
> import AgentExecutor
> Irom Ianechain. callbacks
> iport
> StdOutCallbackHandler
> #  创建回调处理器 (,出日志到控制台)
> handler
> StaOutCallbackHandler ()
> #  绑定全局回调 (所有请求均触发)
> aBent
> executor
> AgentExecutor (
> agent-agent
> too1s=too18
> callbacks= [handler]
> #  全局回调
> Verbose-True
*

*
> [!NOTE] [图片 OCR 识别内容]
> 2。请求特定回调
> 绑定ivoke ): 仅作用于单个诮求适用于个性化需求
> 如流式输出 ):
> 仅当前请求触发回调
> Legult
> agent
> executor . invoke (
> {"input"
> "计算1+1"},
> {"callbacks"
> [handler] }
> #  请求特定回调
> 6.8.2
> Token计数与成本统计
> Chain 提供Bet_openai
> callback 工具
> 用于统计工4调用的Token消耗和成本,
> 核心指
> 标如下=
> total
> tokens: 总Token数
> 提示Token+ 完成Token ) ;
> Prompt
> tOKens
> Completion
> tokeng:
> 提示 /完成部分的Token数;
> successful_requests: 成功的4卫请求次数;
> total_cost: 总费用 (按Open4I定价计算,如Bpt-3.J-tubo每1k 'Token $0.0015 )。
> 6.9
> 核心内容总结
> 本章围绕
> 具备记忆与工具的自主智能体
> 展开,核心知识点包括:
> 思维链推理 (Cor): 通过步骤引导与上下文补充。提JLN复杂问题解决能力;
> 智能体基础:  三大核心组件〈输入。目标 /奖励函数。可用动作)与 "行动-观察
> 循环;
> ReAct 框架:  结合
> 推理+工具动作"
> 解决纯C0 缺乏外部交互的问题;
> 工具使用:  LangChan的三种工具创建方式 (自定义。预置。工具集)  及使用规范;
> 记忆机制:
> 长时/短时记忆的区别, LangChain的五种记忆类型及持久化方法;
> 高级框架:  计划-执行智能体
> BabyACI) , 思维树 (ToT) 的核心逻辑;
> 监控与统计:  回调函数的使用,
> Token计数与成本统计。
> Laug
*

---

## 讨论与评论 (3)

### 评论 #1 (作者: QW78773, 时间: 7个月前)

非常有用的分享

---

### 评论 #2 (作者: BW14163, 时间: 7个月前)

感谢分享，真是太厉害了，这么厚的一本书，浓缩成了几页纸，方便我们进行查阅。

如果能从这几页纸里面，提取出实际案例，从而进行指导实践，感觉就更棒了。

********************************** 
紧跟大佬的脚步，每天坚持至少学一个知识点，尽量不混信号，不过拟合。 
每当遇到一个RA时，不要忘了在ppac中捡垃圾的日子。 
**********************************

---

### 评论 #3 (作者: 顾问 MZ45384 (Rank 51), 时间: 4个月前)

超有用的分享，学会了在输入层用约束来锚定输出。

======================================================================================
知难上，戒骄狂，常自省，穷途明。“寻找可以重复数千次的东西。”——吉姆·西蒙斯（量化投资之王、文艺复兴科技创始人）
# Alpha∞ Engine Status: ONLINE [♦♦♦♦♦♦♦♦♦♦] 100%
# sys.setrecursionlimit(α∞) 
# PnL = ∑(Robustness * Creativity)
#无限探索、鲁棒性优先，创新性增值 
#Where there is a will, there is a way. 路漫漫其修远兮，吾将上下而求索。
======================================================================================

---

