# 筛选历史回测中满足PPAC的alpha（含代码）代码优化

- **链接**: [Commented] 筛选历史回测中满足PPAC的alpha含代码代码优化.md
- **作者**: DZ31817
- **发布时间/热度**: 1年前, 得票: 27

## 帖子正文

PPAC比赛大幅降低了提交条件，给我们带来了增加收入的机会。我们历史的回测中有大量满足PPAC条件的alpha，可以通过代码筛选出来并挑选提交。其中过于久远的alpha需要重新模拟。此外，提交的时候也要尽可能挑选各项指标好的alpha来提交，毕竟PPAC也影响vf。

代码主要原理是通过machine_lib的get_alpha函数，在返回的response中找到response['results']['is']['checks']]中'name' == 'MATCHES_COMPETITION'并且'result' == 'PENDING'的alpha，即为满足PPAC比赛条件的alpha。

参考代码如下：


> [!NOTE] [图片 OCR 识别内容]
> for url
> in  Urls:
> response
> 5.
> get(url)
> #print (response.json() )
> try:
> alpha_list
> response.json ( ) ["results" ]
> #print (response.json() )
> forj
> in range(len(alpha_list)):
> if  competition
> 
> True:
> competition_result
> False
> for k  in alpha_list [j] [
> is ' ] ['checks' ] :
> i k[
> name
> 1
> MATCHES_COMPETITION
> and K[C
> result
> PENDING
> competition_result
> True
> if. competition_result
> True:
> alpha_id
> alpha_list [j] ["id" ]
> name
> alpha_list [j] ["name" ]
> dateCreated
> alpha_list [j] ["datecreated" ]
> Sharpe
> alpha_list [j] ["is" ] ["sharpe" ]
> fitness
> alpha_list [j] ["is" ] ["fitness" ]
> turnover
> alpha_list [j] ["is" ] ["turnover"]
> margin
> alpha_list [j] ["is" ] ["margin" ]
> longCount
> alpha_list [j] ["is" ] ["longCount"]
> ShortCount
> alpha_list [j] ["is" ] ["shortCount" ]
> decay
> alpha_list [j] ["settings" ] ["decay" ]
> eXp
> alpha_list [j] [ ' regular' ] [ ' code
> 1
> #i. (sharpe
> 2`
> 1.2
> and  Sharpe
> 1.6)
> Or
> (sharpe < -1.2.and . sharpe > -1.6) :
> i simu_name
> None
> Or
> simu_name
> in eXp:
> Count
> 十
> 1
> eXp
> eXp.replace( ' #' +simu_namet
> ;n' `
> )
> if (longCount
> ShortCount )
> 100:
> rec
> [alpha_idr
> eXP,  sharpe, fitness, margin,  turnover;
> longCount,  shortCount,
> dateCreated,
> decay]
> print( 'Pick:
> rec)
> next_alphas.append (rec)
> else:


---

## 讨论与评论 (7)

### 评论 #1 (作者: HJ33503, 时间: 1年前)

====================================================================================

好思路，这样可以快速筛选到满足比赛的alpha，我之前都没关注到pending这个result，谢谢分享

====================================================================================

---

### 评论 #2 (作者: OB53521, 时间: 1年前)

非常感谢大佬提供的代码，这两天为了比赛非常头疼，尤其是当比赛放低了标准之后，每个alpha都不能直接进行check，因为不想错过可以提交的、表现不错的alpha。通过这套代码能够更加灵活地调节自己筛选alpha的标准，既节约了时间，又能最大限度地在限流的影响下check足够多的alpha！

---

### 评论 #3 (作者: XZ23611, 时间: 1年前)

建议先从已经提交过的alpha里面找OS好的，如果OS差的就不要交了

---

### 评论 #4 (作者: CC21336, 时间: 1年前)

请教一下代码中 simu_name 是代表什么含义？它与 name=alpha_list[j]['name']是有没有什么关系，我需要从哪里获取到这个simu_name ？

---

### 评论 #5 (作者: DZ31817, 时间: 1年前)

CC21336

这个是我自己加的，在alpha表达式的注释中加入这次模拟的一些信息来打标签，筛选的时候就看表达式中是不是包含相关的字符串，来实现筛选的效果，是打tag的方式的一种平替，如果没有使用此种方法可以忽略。

---

### 评论 #6 (作者: 顾问 JR23144 (贺六浑) (Rank 6), 时间: 1年前)

博主写的不错， 不过在程序中 ，competition_result 本身就是bool 值， 不需要些 if  competition_result==True   直接写   if competition_result  就行了 并且现在 MATCHES_COMPETITION  已经改成了MATCHES_THEMES

```
# 之前代码不变alpha_list = response.json()["results"]# print(response.json())for j in range(len(alpha_list)):    c_r = True      for k in alpha_list[j]["is"]["checks"]:        if k["name"] == 'MATCHES_THEMES' and k['result']=='PENDING':            c_r = False      if c_r: # 如果不是 满足 ppac的 alpha 则跳过        continue    alpha_id = alpha_list[j]["id"]    name = alpha_list[j]["name"]    dateCreated = alpha_list[j]["dateCreated"]    sharpe = alpha_list[j]["is"]["sharpe"]#接后续代码
```

---

### 评论 #7 (作者: ZZ12657, 时间: 6个月前)

写的不错

---

