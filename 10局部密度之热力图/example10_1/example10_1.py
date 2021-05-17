import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import HeatMap
import pyecharts.options as opts

# 资源文件所在目录
resourcesPath = "./resources"
# 便利店文件名
storeBookName = "便利店.xlsx"
# 一周订单量工作表名
orderSheetName = "一周订单量"
# 打开工作表
orderSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, storeBookName)
)[orderSheetName]  # type: Worksheet
# 取出各行的所有原始数据
org_data = [list(row_item) for row_item in orderSheet.iter_rows(values_only=True)]
# print(org_data)


# 提取数据
# 作为x轴坐标的几点钟数据
timeList = [time_order_num[0] for time_order_num in org_data[1:]]
# 作为y轴坐标的星期几数据
weekList = org_data[0][1:]
# 提取热力图中的色块取值信息
heatMapList = []
for row_index, row_item in enumerate(org_data[1:]):
    for col_index, sales_value in enumerate(row_item[1:]):
        heatMapList.append(
            [row_index, col_index, sales_value]
        )
# print(heatMapList)


# 绘制所需的热力图要求
#
# 1. x轴是几点钟的时间；
# 2. 图例隐藏
# 3. y轴是星期几的时间
# 4. 色块每一个地方的坐标及取值用上；
# 5. 视觉映射配置项，将最大值映射值设置为70；
# 6. x轴标签90度旋转防止遮挡；
# 7. 标题设置为：一周订单量；
# 8. 执行保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 存储文件名称
resultFileName = "week_order_heatmap.html"

heatMap = (
    HeatMap()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="一周订单量"),
        visualmap_opts=opts.VisualMapOpts(max_=70),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=90))
    )
    .add_xaxis(xaxis_data=timeList)
    .add_yaxis(
        yaxis_data=weekList,
        value=heatMapList,
        series_name="一周订单量"
    )
    .render(path=os.path.join(resultPath, resultFileName))
)


