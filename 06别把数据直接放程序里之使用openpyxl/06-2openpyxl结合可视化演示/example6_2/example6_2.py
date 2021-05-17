import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Line
import pyecharts.options as opts

"""指定基础配置值

所有路径配置相关的值放在单独的配置文件，或者这里为了方便就放最前面
"""
# 数据资源统一路径
resourcesPath = "./resources"
# 数据资源文件名
resourcesFileName = "table.xlsx"
# 数据所在工作表
colaSheetName = "销量"

# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "sales_line.html"

"""获取数据：不同的可乐在1年内的月销量变化

x轴：月份
y轴：月销量，图例是相应类型可乐的名字
"""


def read_rows(filename="./", sheetname="Sheet") -> list:
    """
    从excel文档中读出所有行，每一行都是列表，所有行存入一个大列表，返回出去
    读取时，不做清洗，只是忠诚地把文件里的数据转移出来到列表里
    :param filename: excel文件名（完整路径）
    :param sheetname: 工作表Worksheet名
    :return: list
    """
    # 加载文件+选表 两步合并
    colaSheet = openpyxl.load_workbook(filename=filename)[sheetname]  # type: Worksheet
    # 读出所有行数据
    rowData = [list(rowContent) for rowContent in colaSheet.iter_rows(values_only=True)]
    return rowData


# 读出表格数据
rowData = read_rows(filename=os.path.join(resourcesPath, resourcesFileName), sheetname=colaSheetName)
# 取出x轴数据（表头，注意第一列空的，要砍掉）
x_data = rowData[0][1:]
# 取出y轴数据（第2行开始）
y_data = dict()
for rowItem in rowData[1:]:
    # eval函数剥开字符串两侧引号，避免字符串数值，适当过滤一下填入数据时候出现的两端空白
    y_data[rowItem[0]] = [eval(str(item).strip()) for item in rowItem[1:]]


"""绘制多y轴折线图

1. 读取文档的月份作为x轴，一共有1～12个月；
2. 读取文档中的数据将商品销量作为y轴，绘制折线图 ；
3. 图例设置为对应行的商品名称；
4. 将整个图表标题设置为：增长趋势的比较 ；
5. 将文件保存
"""
line = (
    Line()
    .set_global_opts(title_opts=opts.TitleOpts(title="增长趋势的比较"))
    .add_xaxis(xaxis_data=x_data)
)
for yaxis_series, yaxis_data in y_data.items():
    line.add_yaxis(series_name=yaxis_series, y_axis=yaxis_data)
line.render(path=os.path.join(resultPath, resultFileName))
