import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Pie, Timeline
import pyecharts.options as opts

# 资源文件夹
resourcesPath = "./resources"
# 每月销售额工作簿
monthlySalesBookName = "每月销售额.xlsx"
# 工作表名
monthlySalesSheetName = "各商品每月销售额"
# 打开工作表
monthlySalesSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, monthlySalesBookName))[monthlySalesSheetName]


def read_excel(sheet: Worksheet) -> list:
    """
    忠诚地读取出工作表中的原始内容，不做任何处理。

    :param sheet: 正在读取的工作表

    :return: 由各行数据组成的列表，每行也是一个列表
    """
    org_data = [list(data_item) for data_item in sheet.iter_rows(values_only=True)]
    return org_data


def get_data(org_data: list, row: int) -> tuple:
    """
    利用read_excel读取出的数据，取出绘制一个饼图所需的数据。

    屏蔽空数据或者0数据。

    :param row: 指定读取的excel表格中第几行的数据（从2开始，跳过第1行表头）
    :param org_data: excel表格里，由各行数据组成的列表，每行也是一个列表

    :return: 二元组：(月份，[(标签1, 数据1), (标签2, 数据2), ...])
    """
    # 取出用来做标签的数据
    labels = org_data[0][1:]

    # 取出相应行的数据
    row_data = [row_item for row_item in org_data[row]]
    # 月份和数据
    month_, data = row_data[0], row_data[1:]

    # 从标签、数据中组合出绘制饼状图所需的数据对
    sales_list = []
    for index in range(len(labels)):
        if data[index] == 0:
            continue
        data_pair_item = (labels[index], data[index])
        sales_list.append(data_pair_item)

    # 返回(月份, 绘图用的数据对列表)
    return month_, sales_list


# 取出excel表格中的内容
orgData = read_excel(monthlySalesSheet)

# 根据12个月的数据，分别绘制出所需的图形
# 1. 每组数据以环状南丁格尔玫瑰图展示
# 2. 将玫瑰图的数据系名设置为空；
# 3. 环内径为"20%", 最大外径为"60%"；
# 4. 数据项标签的格式为"{百分比}%"
# 5. 标签内置于每块饼中；
# 6. 玫瑰图类型设置为圆心角相同，仅通过半径展示数据项大小差别
# 7. 将每个月份图表的标题设置为"月份"+"销售额组成"：x月销售额组成；
# 8. 轮播图各轮播节点设置为月份：x月；
# 9. 将轮播玫瑰图保存
timeline = Timeline()
for rowNum in range(1, len(orgData)):
    # 得到当前行用于绘图的数据
    month, dataPair = get_data(org_data=orgData, row=rowNum)
    timeline.add(
        time_point=month,
        chart=(
            Pie()
            .set_global_opts(title_opts=opts.TitleOpts(title=f"{month}销售额组成"))
            .add(
                series_name="",
                data_pair=dataPair,
                radius=["20%", "60%"],
                rosetype="radius",
                label_opts=opts.LabelOpts(
                    position="inside",
                    formatter="{d}%"
                )
            )
        )
    )

# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 文件名
resultFileName = "sales_rose_pie_timeline.html"
# 执行保存
timeline.render(path=os.path.join(resultPath, resultFileName))
