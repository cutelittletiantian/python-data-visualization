import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import HeatMap
import pyecharts.options as opts

# 资源文件路径
resourcesPath = "./resources"

# 票价表文件名
ticketBookName = "票价表.xlsx"
# 一号线工作表
lineOneSheetName = "一号线"

# 读文件，选表
lineOneSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, ticketBookName)
)[lineOneSheetName]  # type: Worksheet

# 取出表中所有数据
org_data = [row_item for row_item in lineOneSheet.iter_rows(min_row=1, values_only=True)]
print(org_data)

# x轴上的标签和y轴的标签都是站台名称
# 提取x轴和y轴的标签
xData = org_data[0][1:]
yData = [row_item[0] for row_item in org_data[1:]]
# 扫描行列，组合出热力图取值二维列表（非常注意一点：表的列是数据的x轴，表的行是数据的y轴）
value_list = []
for x_index, sheetRow in enumerate(org_data[1:]):
    for y_index, value_ in enumerate(sheetRow[1:]):
        value_list.append(
            [x_index, y_index, value_]
        )
print(value_list)

# 绘制热力图需求：
# 1. 画布的宽为"1000px",高为"800px"；
# 2. 隐藏图例；
# 3. 数据标签显示在内部居中；
# 4. 视觉配置项，最大值映射值设置为10；
# 5. x轴上的标签旋转90度防止遮挡；
# 6. 标题设置为"一号线票价表"；
# 7. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "ticket_price_heatmap.html"
# 执行绘图
heatMap = (
    HeatMap(
        init_opts=opts.InitOpts(width="1000px", height="800px")
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="一号线票价表", subtitle="单位（元）"),
        legend_opts=opts.LegendOpts(is_show=False),
        visualmap_opts=opts.VisualMapOpts(max_=10),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90))
    )
    .add_xaxis(xaxis_data=xData)
    .add_yaxis(
        series_name="",
        yaxis_data=yData,
        value=value_list,
        label_opts=opts.LabelOpts(position="inside")
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
