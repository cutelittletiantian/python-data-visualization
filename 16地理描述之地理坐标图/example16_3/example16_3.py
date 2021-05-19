import os
from pyecharts.charts import Geo
from pyecharts.globals import GeoType, ThemeType
import pyecharts.options as opts
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook

# 用地理坐标图，描述成都一家网店寄往其他地区商品的邮费情况

# 资源文件
resourcesPath = "./resources"
# 全国运输文件
transBookName = "全国运输.xlsx"
# 全国邮费工作表
transSheetName = "全国邮费"
# 开文件、选表
transBook = openpyxl.load_workbook(filename=os.path.join(resourcesPath, transBookName))  # type: Workbook
transSheet = transBook[transSheetName]  # type: Worksheet

# 读取所有原始数据（跳过表头）
# 列含义：[起点, 终点, 邮费]
orgData = [list(row_item) for row_item in transSheet.iter_cols(min_row=2, min_col=1, values_only=True)]
# print(orgData)

# 清洗数据None，[:]深拷贝，防止下标错位
for rowItem in orgData[:]:
    for cellItem in rowItem[:]:
        if cellItem is None:
            rowItem.remove(cellItem)
    if len(rowItem) == 0:
        orgData.remove(rowItem)
# print(orgData)

# 按照[起点, 终点]的方式添加两地的边；按照[终点, 到终点的邮费]这种方式构造目的地的带权节点
# 边数据对的构造
routeList = zip(orgData[0], orgData[1])
# 带权节点的构造
postageList = zip(orgData[1], orgData[2])

# 绘制地理坐标图的需求
# 1. 坐标类型是中国地图
# 2. 同时添加带权节点和边两类坐标图要素，带权节点为动态散点样式，边为流向样式（类型设置可以参照文档）
# 3. 图例系列均设为空，隐藏数据标签
# 4. 图的主题为dark
# 5. 添加最大映射为10，最小映射为4
# 6. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "postage_geo.html"
# 执行绘图
geo = (
    Geo(init_opts=opts.InitOpts(theme=ThemeType.DARK))
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(min_=4, max_=10))
    .add_schema(maptype="china")
    .add(
        series_name="",
        data_pair=postageList,
        type_=GeoType.EFFECT_SCATTER,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        series_name="",
        data_pair=routeList,
        type_=GeoType.LINES,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
