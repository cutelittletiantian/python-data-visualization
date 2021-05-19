import os
from pyecharts.charts import Geo, Timeline
import pyecharts.options as opts
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook
from pyecharts.globals import GeoType

# 使用地理坐标图+轮播图，描绘今年来全国气温的变化

# 配置文件
# 资源文件目录
resourcesPath = "./resources"
# 近年来的温度文件
temperatureBookName = "全国十年年平均温度.xlsx"
# 年平均气温工作表
temperatureSheetName = "年平均气温"

# 打开文件，选表
temperatureSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, temperatureBookName)
)[temperatureSheetName]  # type: Worksheet

# 取出所有的原始数据
orgData = [list(row_item) for row_item in temperatureSheet.iter_cols(values_only=True)]
# print(orgData)

# 清洗取值为None的列
# 去掉末尾附加None值，注意，orgData[:]另外深拷贝一个副本，原列表
for row_item in orgData[:]:
    if None in row_item:
        orgData.remove(row_item)
# print(orgData)

# 第一行的列表，去掉”城市”这个字，多余
orgData[0] = orgData[0][1:]
# print(orgData)


# 组装可视化需要的数据
def get_data(col_num) -> tuple:
    """
    用于绘制一张轮播图需要的数据（第i列，i始于1）
    :param col_num:
    :return: (年份，[绘图所需数据对])
    """
    # 从原始数据中，提取年份和各个城市需要的数据
    year_, city_data = orgData[col_num][0], orgData[col_num][1:]
    # 组装城市-数据对
    data_pair = zip(orgData[0], city_data)
    # 返回(年份，[绘图所需数据对])
    return year_, list(data_pair)


# 地理坐标图绘图需求
# 1. 地图坐标类型选择中国地图，用热力图方式体现温度
# 2. 图例为空
# 3. 设置视觉配置项，但隐藏，最大映射值为25，分段型映射（怎么设置可以查查官方文档）
# 4. 轮播节点名为“xxx年”
# 5. 每个图的名字设置为“xxx年全国主要城市平均温度”
# 6. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "TEMP_geo_timeline.html"
# 执行绘图
# 轮播图框架
timeline = Timeline()
# 一个个往里加轮播图
for colNum in range(1, len(orgData)):
    year, dataPair = get_data(col_num=colNum)
    # print(year, dataPair)
    # 添加新的地理坐标图
    timeline.add(
        time_point=f"{year}年",
        chart=(
            Geo()
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{year}年全国主要城市平均温度"),
                visualmap_opts=opts.VisualMapOpts(
                    is_show=False,
                    max_=25,
                    is_piecewise=True
                )
            )
            .add_schema(maptype="china")
            .add(
                series_name="",
                type_=GeoType.HEATMAP,
                data_pair=dataPair,
            )
        )
    )
# 执行保存
timeline.render(path=os.path.join(resultPath, resultFileName))