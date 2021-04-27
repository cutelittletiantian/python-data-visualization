# 前排提示

内容有在续建设中，请持续关注，爱你们哟ღ( ´･ᴗ･` )。

# 简介

近期工作压力巨大，常年在地铁上刷着干瘪的短视频和段子，我看到了**世界的参差**\_(:з」∠)\_，对于美的追求的精神世界无比枯竭。直到有一天，我看到了，在一些学术论文中，出现了许多美丽的图片（如反映多维数据分布及相关性的**散点图和气泡图**、表现流量分布的**桑基图**等），这些图片的美感在于，它们将冰冷的数据用生动的图像演绎出来，无比炫酷，给人以无限的遐想和学习的兴趣。

想想马上就要读研究生的我，也许多年后需要自己生成~~美丽的~~图像，为了多年后别把自己精心研究的数据绘图成跟shi一样，更重要的是**为了在感受世界的参差时静下心来，享受学术的美丽、数据的美丽**，我决定入坑学习Python数据可视化，并把学习成果与大家交流共享。

持续建设中，大家可以关注，平日里要打工，不定期更新（提前为自己的咕咕咕找好借口）

# 配置要求

> OS: ``Windows 10``或者``MacOS``均可（注意：``Windows 10``或者``MacOS``仅在某些方面，比如文件路径的表示上可能略有不同）
> 
> Python版本: 本项目采用``3.9.x 64-bit``版本（截至2021年4月26日查询Python官网``https://www.python.org``，Python最新版本为3.9.x）
> 
> 推荐的编辑器：``Pycharm``或``Jupyter``，看你喜好啦~推荐使用虚拟环境（venv），在为本项目进行必要的第三方库配置时，不影响其它Python项目的配置，不污染系统Python的环境。

# 需要用到的Python库

``pyecharts``：本项目**最主要的**第三方库之一，打开cmd（或其它操作系统的终端），使用``pip install pyecharts``进行安装。

> 用途：将数据进行可视化，生成各种可交互式的图表。
>
> 导入方式：直接采用``import pyecharts``导入有其不足点，通常我们这样导入pyecharts包

```python
# 导入options模块并简写为opts
import pyecharts.options as opts
# 从pyecharts.charts中导入“某一特定类型图”（some-package）模块
from pyecharts.charts import <some-package>
```

其中上述``<some-package>``，根据需要绘制的图形类型进行特别指定，画柱状图就换成``Bar``，画线状图就指定``Line``，画桑基图就指定``Sankey``等。

举例：假如要绘制柱状图（Bar chart），就这样导入``pyecharts``库

```python
# 导入options模块并简写为opts
import pyecharts.options as opts
# 从pyecharts.charts中导入 Bar 模块
from pyecharts.charts import Bar
```

***

``openpyxl``：第三方库，打开cmd（或其它操作系统的终端），使用``pip install openpyxl``进行安装。

> 用途：对excel表格进行读写操作。
>
> 导入方式：原则上采用``import openpyxl``便足以满足开发需要，但是为了尽可能发挥代码提示的功能，推荐如下方式导入

```python
import openpyxl  # 最主要的导入
from openpyxl.utils import cell
from openpyxl import Workbook  # 这个导入和type注释会共同起作用
from openpyxl.worksheet.worksheet import Worksheet  # 这个导入和type注释会共同起作用
```

另注：为了显示代码提示，建议在对工作簿、工作表变量赋值后，用注释在同一行指明类型（格式：``# type: 类型名``），例如

```python
import openpyxl  # 最主要的导入
from openpyxl.utils import cell
from openpyxl import Workbook  # 这个导入和type注释会共同起作用
from openpyxl.worksheet.worksheet import Worksheet  # 这个导入和type注释会共同起作用

workBook = openpyxl.load_workbook(filename=recordPath)  # type: Workbook
workSheet = photoParamBook["示例"]  # type: Worksheet
```

***

**安装第三方包出错的解决方法**：有时安装失败是因为国内网络有一些限制，这时您可以尝试使用清华大学镜像下载相应的包，即``pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package``，其中``some-package``换成自己所需要安装的第三方库名。

***

# 请注意

* 当您在运行Python的样例时，请预先安装好所需的第三方库依赖，**并关闭resources目录中所涉及的文件**（如果有），以免因为文件占用导致程序不能处理打开着的文件。
* 使用库的时候，不要死记硬背，常见的思路记住即可，细节的东西可以随机应变或者查官方文档进行处理。
* 导入第三方库时，部分第三方库（例如``openpyxl``）的类单独导入进来，结合形如``# type: ...``格式的注释，有利于充分利用好编辑器的代码填充提示，使第三方库的封装更有意义。

# 快捷传送门

本项目中，所涉及库等内容的文档链接如下。

``Python``官网及其官方文档

> 官网：https://www.python.org
> 
> 文档：https://docs.python.org/3/

本项目**最主要的**第三方库之一``pyecharts``官方文档

> https://pyecharts.org/

``openpyxl``第三方库官方文档

> https://openpyxl.readthedocs.io/en/stable/index.html

清华大学开源软件镜像站（当第三方库无法直接下载时，可以考虑镜像站）

> 网址：[清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/)
>
> 使用镜像安装第三方库格式：``pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package``
>
> （请将上述``some-package``换成自己需要的第三方库名，例如``pyecharts``）

# 小添添的其它Python坑

**Python自动化办公**：使用``os`` ``openpyxl`` ``python-docx`` ``pdfplumber``等第三方库批量分类文件、批量读写Excel文档、批量读写Word文档、批量获取文字类Pdf文档内容等，通过一些典型的应用场景，大幅提升职场办公室工作效率。

> 传送门：https://github.com/cutelittletiantian/python-for-office