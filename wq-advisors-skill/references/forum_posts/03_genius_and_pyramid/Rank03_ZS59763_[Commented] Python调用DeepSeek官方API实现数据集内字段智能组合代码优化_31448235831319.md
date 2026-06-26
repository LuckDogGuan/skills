# Python调用DeepSeek官方API实现数据集内字段智能组合代码优化

- **链接**: https://support.worldquantbrain.com[Commented] Python调用DeepSeek官方API实现数据集内字段智能组合代码优化_31448235831319.md
- **作者**: YX50005
- **发布时间/热度**: 1年前, 得票: 62

## 帖子正文

在3月第二节顾问课上，老师展示了使用网页版大模型来进行字段组合生成具有经济学含义的新字段的流程，如果能把这个流程放在python中自动执行，可以提高一些效率。

- 大语言模型选择DeepSeek-R1
- 输入给大语言模型的信息遵循老师课上给的例子，包括数据集描述和字段名，字段描述

流程如下：

1.输入数据集描述/字段信息形成prompt

```
def _build_prompt(
        self, dataset_desc: str, fields_info: List[Tuple[str, str]]
    ) -> str:
        """
        构建 prompt
        """
        # 如果字段数量超过100，随机选择100个
        if len(fields_info) > 100:
            fields_info = random.sample(fields_info, 100)

        fields_text = "\\n".join(
            [
                f"{field_name}: {field_desc}; "
                for field_name, field_desc in fields_info
            ]
        )

        prompt_system = f"""
你是一位专业的量化金融分析师。现在有一个数据集提供给你：

1. 数据集描述：  
   {dataset_desc}

2. 现有字段信息：  
   {fields_text}
"""

        prompt_user = f"""
请根据以下要求，生成新的字段表达式列表：
(1) 请尽量多样化地生成新的字段表达式，且每个字段都需具有明确的经济学含义。  
(2) 可使用加减乘除等基本运算符。  
(3) 每个字段的经济学含义需有注释说明
(4) 输出格式：仅返回 JSON 数组，数组中每个元素包含 "description" 和 "expression" 两个字段：  
    • description（描述字段含义）  
    • expression（字段的实际表达式）  

请勿输出除 JSON 数组外的任何额外文字或说明。请直接返回最终的 JSON 数组结果。
"""

        return prompt_system, prompt_user

```

2.调用deepseek API

```
def _call_api(self, system_prompt: str, user_prompt: str) -> dict:
        """
        调用 DeepSeek API
        """
        data = {
            "model": "deepseek-reasoner",
            "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
            "temperature": 0.7,
        }

        response = requests.post(self.api_url, headers=self.headers, json=data)
        response.raise_for_status()

        return response.json()

```

输出的结果类似于


> [!NOTE] [图片 OCR 识别内容]
> "description": "Adjusted
> ROE volatility factor, measuring stability
> of profitability by adjusting
> ROE
> With
> its standard deviation
> OVer
> past
> 60
> months"
> Iexpression":
> 'fnd65_totalcap_cusip_roe
> /
> fnd65_totalcap_cusip_sigma"
> }
> "description":
> ICash
> flow momentum adjusted by price momentum
> combining 18-month alpha change With
> Cash
> flow growth"
> 'expression":
> (fnd65_us5000_cusip_chgGmalphalgm
> fnd65_us5aa0_cusip_pctchgcf)
> /
> 21
> }
> "description": "Composite quality
> SCore
> combining
> debt coverage,
> profitability
> and efficiency
> ratios"
> 'expression":
> fnd65_totalcap_cusip_divcov
> fnd65_us5oao_cusip_mpg
> fnd65_allcap_sedol_ocfroi)
> /
> 3"
> }
> "description":
> "Enterprise value-adjusted operating efficiency
> ratio"
> 'expression":
> 'fnd65_totalcap_cusip_vefcomtt
> 米
> fnd6s_totalcap_cusip_saleicap"
> }
> "description":
> "Leverage-adjusted momentum
> factor
> Comb
> ining relative strength
> With
> debt
> ratio"
> 'expression":
> fnd65_us5000
> CUS
> j_d4lisr
> /
> fnd65_totalcap_Cusip_ed"
> }
> "description":
> "Earnings quality composite
> incorporating surprise persistence
> and
> forecast dispersion
> 'expression":
> (fnd65_totalcap_cusip_Surp
> 十
> fnd65_totalcap_cusip_fc_fqsurstd)
> /
> fnd65_totalcap_cusip_fc_numest"
> }
> "description": "Liquidity-risk adjusted value
> factor combining working capital with bid-ask spread"
> 'expression":
> 'fnd6s_totalcap_cusip_wcast
> fnd65_totalcap_cusip_bapzod"
> }
> "description":
> IGrowth sustainability
> SCore
> combining sales growth consistency
> With
> RSD efficiency"
> 'expression":
> (fnd65_totalcap_cusip_cg3ysales
> fnd65_totalcap_cusip_adverint)
> 米
> fnd65_us5oao_cusip_cv4qsales3y"
> }
> "description": "Composite financial
> health
> indicator combining
> debt
> Coverage
> ratios"
> 'expression":
> (fnd65_totalcap_cusip_totalcov
> 十
> fnd65_totalcap_cusip_voctni)
> /
> fnd65_Us5000
> cusip_debtcf"
> }
> "description":
> IEarnings
> revision
> momentum adjusted by market reaction sensitivity"
> 'expression":
> fnd65_Us5000
> cusip_rev3mylstd
> * fnd65_US5000
> cusip_Cre_cf"
> }
> "description":
> IFree
> cash
> flow yield adjusted
> for capital expenditure efficiency"
> 'expression":
> fnd65_allcap_sedol_pfcomtt
> /
> fnd65_allcap_sedol_capacq"
> }
> "description":
> IRelative
> Value composite comparing multiple
> Valuation
> metrics
> to industry peers"
> "expression":
> fnd65_totalcap_cusip_curindbp_
> fnd65_totalcap_cusip_curindcfp_
> 十
> fnd65_totalcap_cusip_curinddivp_)
> 3"


3.解析输出的json，获取生成的字段

```
def _parse_response(self, response: dict) -> List[str]:
        """
        解析 API 响应
        """
        try:
            content = response["choices"][0]["message"]["content"]
            if content.startswith("```json"):
                content = content[len("```json") :]
            if content.endswith("```"):
                content = content[: -len("```")]
            print(content)
            fields = json.loads(content)
            return [field["expression"] for field in fields]
        except Exception as e:
            print(f"解析响应时出错: {e}")
            return []

```

这样在通过API获取数据集的表述、字段的信息后，就可以自动地为各个数据集生成一批具有经济学含义的新的组合字段了。

更进一步

- Deepseek的官方API需要收费，可以探索其他更经济的调用大模型的方式
- 目前取了一个数据集中的随机100个字段，如果大模型本身支持，并且价格不贵，可以取更多的字段进行输入

---

## 讨论与评论 (3)

### 评论 #1 (作者: DZ31817, 时间: 1年前)

感谢分享，很好的实践。我最近也在使用大模型批量生成信号，但也跟你这段prompt一样，目前仅限于使用加减乘除等基本运算符的时候效果还可以接受，一旦涉及高等的运算符，生成的效果就没那么好了。期待进一步的探索研究。

---

### 评论 #2 (作者: worldquant brain赛博游戏王, 时间: 1年前)

很好的实践，潜在的优化方向是把一些基础的运算符，比如sqrt，tsmean这些也同时扔给ai，供参考。

---

### 评论 #3 (作者: JX14975, 时间: 1年前)

请问你遇到过deepseek无中生有数据字段的情况吗？我用网页版这种情况就特别明显，尤其是在输入的字段多的时候。

---

