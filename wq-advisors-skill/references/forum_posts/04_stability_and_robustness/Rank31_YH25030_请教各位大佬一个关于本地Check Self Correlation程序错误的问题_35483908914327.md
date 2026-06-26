# 请教各位大佬一个关于本地Check Self Correlation程序错误的问题？

- **链接**: https://support.worldquantbrain.com请教各位大佬一个关于本地Check Self Correlation程序错误的问题_35483908914327.md
- **作者**: 顾问 YH25030 (Rank 31)
- **发布时间/热度**: 8个月前, 得票: 37

## 帖子正文

最近在做本地check self correlation程序时候，经常报如下错误。

ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

我看同时在运行的回测程序都正常，没有任何报错。

我问了AI， AI让我尝试设置等待时间。我即使设置了检查一个因子，等待60或者120秒。但是运行到200个因子左右，还是有同样报错。

想问问大家有没有遇到相同问题？


> [!NOTE] [图片 OCR 识别内容]
> RemoteDisconnected
> Traceback (most recent call Iast)
> File
> C: IUsers IAdministratorlAppDatalLocallPrograms IPython IPython3l3lLiblsite-packages lurllib3Iconnectionpool.py: 787,
> in HTTPConnectionpool.urlopen(self, method,
> UrI
> headers, retries, redirect,
> assert
> Same_host, timeout
> 786 #
> Nake
> the request
> the HTTPConnection
> object
> 787 response
> SeIf
> make_request(
> 788
> Conn
> 789
> method,
> 790
> UrI
> 791
> timeout-timeout_obj
> 792
> body-body,
> 793
> headers-headers_
> 794
> chunked-chunked,
> 795
> retries-retries
> 796
> response
> Connresponse
> Conn
> 797
> preload_
> content-preload_content,
> 798
> decode
> content-decode_content,
> 799
> *response
> W
> 880
> 882 # Everything went great!
> File
> C: IUsers IAdministratorlAppDatalLocallPrograms IPython lPython3l3 ILiblsite-packages lurllib3 Iconnectionpool.py:534,
> i HTTPConnectionpool
> wake
> request(self, conn, method, url,
> body, headers, retries, timeout, chunked,
> response
> 533 try:
> 534
> response
> conn.Betresponse()
> 535 except
> (BasessLError,
> OSError )
> 684 except MaxRetryError
> 685
> 讦 isinstance(e.reason, ConnectTimeoutError):
> 686
> TODO:
> Remove this
> i 3.0.0:
> See
> #2811
> ConnectionError:
> Connection aborted.
> RemoteDisconnected ( 'Remote
> closed connection without
> response') )
> Output I truncated: View as
> Scrollable element or open in a text editos Adjust cell output Settings:
> body,
> end


---

## 讨论与评论 (1)

### 评论 #1 (作者: JX14975, 时间: 8个月前)

获取pnl也有限流的，只是限制比直接用api接口检查相关性宽很多，你这个问题估计是因为最近api限流变得比较严重了。
建议在检查相关性前先使用基于表达式的剪枝，减少检查量。

【代码优化】基于字段结构的剪枝函数，更准确、更灵活，提升回测效率
 [https://support.worldquantbrain.com/hc/en-us/community/posts/31928133456407](https://support.worldquantbrain.com/hc/en-us/community/posts/31928133456407--%E4%BB%A3%E7%A0%81%E4%BC%98%E5%8C%96-%E5%9F%BA%E4%BA%8E%E5%AD%97%E6%AE%B5%E7%BB%93%E6%9E%84%E7%9A%84%E5%89%AA%E6%9E%9D%E5%87%BD%E6%95%B0-%E6%9B%B4%E5%87%86%E7%A1%AE-%E6%9B%B4%E7%81%B5%E6%B4%BB-%E6%8F%90%E5%8D%87%E5%9B%9E%E6%B5%8B%E6%95%88%E7%8E%87)

---

