import os
from pyecharts.charts import Geo
from pyecharts.globals import GeoType
import pyecharts.options as opts

# 使用地理坐标图，表达自己一年来的出差情况

# 准备原始数据，省略读取文档的过程
# 出差去往各点的次数：带权节点(地点, 出差次数)
businessTimes = [("北京", 50), ("广州", 30), ("成都", 40), ("哈尔滨", 10)]
# 每次出差的路线图：边(起点, 终点)
businessFlow = [("上海", "广州"), ("上海", "哈尔滨"), ("上海", "北京"), ("上海", "成都"), ("北京", "成都"), ("哈尔滨", "广州")]

# 绘制地理坐标图需求
# 1. 坐标轴设置：选择中国地图
# 2. 带权节点设置：图例系列名为空，设置为动态散点显示，隐藏数据标签
# 3. 边的设置：图例名称为空，设置为流向显示，隐藏数据标签；美化涟漪特效（查文档说明）：箭头大小为5，黄色，弯曲度20%
# 4. 视觉映射：最大和最小设置分别为60和10
# 5. 标题为“出差大盘点”
# 6. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "on_business_geo.html"
# 执行绘图
geo = (
    Geo()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="出差大盘点"),
        visualmap_opts=opts.VisualMapOpts(max_=60, min_=10)
    )
    .add_schema(maptype="china")
    .add(
        # 带权节点
        series_name="",
        type_=GeoType.EFFECT_SCATTER,
        data_pair=businessTimes,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        # 边
        series_name="",
        type_=GeoType.LINES,
        data_pair=businessFlow,
        effect_opts=opts.EffectOpts(
            symbol="arrow",
            symbol_size=5,
            color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(
            curve=0.2
        ),
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
