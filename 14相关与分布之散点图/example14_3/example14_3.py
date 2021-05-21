import os
from pyecharts.charts import Scatter, Tab
import pyecharts.options as opts
from pyecharts.globals import ThemeType
import openpyxl
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# 散点图画下面几组很有趣的数据，放在看板里面
# Alberto Cairo教授曾经构造的5组数据文件
# 这5组文件很有特点：x系列数值平均数相同，标准差相同，相关系数也相同；y系列数值亦然
# 但绘制出的散点图却完全不同

# 资源文件目录
resourcesPath = "./resources"
# 工作文件名
acBookName = "dino1.xlsx"
# 工作表名
acSheetName = "数据"

# 打开文件选表
acSheet = openpyxl.load_workbook(filename=os.path.join(resourcesPath, acBookName))[acSheetName]  # type: Worksheet

# 逐列扫描提出数据，跳过表头
orgData = [list(col_item) for col_item in acSheet.iter_cols(min_row=3, values_only=True)]
print(orgData)

# 提取各列用于绘制散点图的数据
awayX = orgData[0]
awayY = orgData[1]
bullseyeX = orgData[2]
bullseyeY = orgData[3]
circleX = orgData[4]
circleY = orgData[5]
dinoX = orgData[6]
dinoY = orgData[7]
dotsX = orgData[8]
dotsY = orgData[9]


def scat_plot(x_data, y_data) -> Scatter:
    """
    用于绘制散点图的x轴和y轴数据

    1. 画布宽度为"1000px"，高度为"600px"，主题为"light"

    2. 隐藏y轴的数据标签

    3. x轴的坐标应该是连续型

    :param x_data: x轴数据

    :param y_data: y轴数据

    :return: 画好的散点图对象，用于后续添加到看板中
    """
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, width="1000px", height="600px"))
        .set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            label_opts=opts.LabelOpts(is_show=False)
        )
    )
    return scatter


# 逐个执行绘图，添加到看板中，并保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 文件名
resultFileName = "acplot_scatter.html"
# 执行绘图和保存
tab = (
    Tab()
    .add(chart=scat_plot(x_data=awayX, y_data=awayY), tab_name="away")
    .add(chart=scat_plot(x_data=bullseyeX, y_data=bullseyeY), tab_name="bullseye")
    .add(chart=scat_plot(x_data=circleX, y_data=circleY), tab_name="circle")
    .add(chart=scat_plot(x_data=dinoX, y_data=dinoY), tab_name="dino")
    .add(chart=scat_plot(x_data=dotsX, y_data=dotsY), tab_name="dots")
    .render(path=os.path.join(resultPath, resultFileName))
)
