# Error in using Brain ACE

- **链接**: https://support.worldquantbrain.com[Commented] Error in using Brain ACE_32515837451799.md
- **作者**: SD99406
- **发布时间/热度**: 1年前, 得票: 0

## 帖子正文

Hii,

I am facing this error while using Brain ACE

Kindly guide

Thanks in advance


> [!NOTE] [图片 OCR 识别内容]
> Welcome to Alpha Creation Engine (ACE)! T
> This notebook is created to demonstrate functions of ACE that includes ace_lib.py and helpful_functions:py
> To ensure that functions will work properly
> install the required libraries by running this cell:
> [1]:
> !pip install
> requirements.txt
> ERROR:
> Could
> not
> Open
> requirements file:
> [Errno 2]
> NO
> Such file
> Or
> directory:
> requirements.txt
> Now; you need to import following modules:
> 回  个 V  占  罕
> ace_lib and helpful_functions
> modules that we provided for you to comfortably interact with BRAIN API. Documentation for ACEAPI
> pandas
> is a Useful
>  library for interacting with DataFrames and data analysis. Pandas Documentation
> requests
> I53
> Python
> uUsed for
>  making requests for web services Requests Documentation
> plotlyexpress
> that we will use for visualization. Plotly.express Documentation
> tqdm
> is 3
> for
> creating progress bars. tqdm Documentation
> Python
> Library。
> python
> library
> python
> library
> library


---

## 讨论与评论 (2)

### 评论 #1 (作者: 顾问 PN39025 (Rank 87), 时间: 1年前)

Hi, the required file is the file to download the libs. In the error message, the required file cannot be found, so it reports an error. Please check again and find the correct file location.

---

### 评论 #2 (作者: SS63636, 时间: 1年前)

Make sure the folder from which you are executing this code contains the correct 'requirements.txt' file, as it includes all the necessary libraries used in the script. If the file is named differently, please verify and update the filename in your code to avoid import or module-related issues during execution.

---

