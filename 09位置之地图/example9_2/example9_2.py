import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Map
import pyecharts.options as opts

# 资源文件统一所在目录
resourcesPath = "./resources"
# 降雨量数据工作簿名
rainFallBookName = "全国降雨量.xlsx"
# 2017年数据工作表名
rainFallSheetName = "2017年降水量"
# 打开文件选表
rainFallSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, rainFallBookName)
)[rainFallSheetName]  # type: Worksheet

# 获取原始数据：2017年全国各省降水量（毫米），跳过表头
orgData = [row_item for row_item in rainFallSheet.iter_rows(min_row=2, values_only=True)]

# 清洗数据，去掉空数据。组装绘图用的数据对
dataPair = [data_item for data_item in orgData
            if None not in data_item]

# 绘制地图需求
# 1. 标记（symbol）隐藏、标签隐藏
# 2. 添加视觉映射，最大值映射值设为230
# 3. 组件过渡颜色设置为["#E0ECF8", "#045FB4"]，冷色系的那种，让人感觉是下雨的感觉
# 4. 标题设为"2017年全国降雨量"
# 5. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "rainfall_china_map.html"
# 执行绘图
mapChart = (
    Map()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2017年全国降雨量", subtitle="单位：mm"),
        visualmap_opts=opts.VisualMapOpts(
            max_=230,
            range_color=["#E0ECF8", "#045FB4"]
        ),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .add(
        series_name="降水量（单位：mm）",
        data_pair=dataPair,
        label_opts=opts.LabelOpts(is_show=False),
        is_map_symbol_show=False
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
