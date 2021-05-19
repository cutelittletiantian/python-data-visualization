import os
from pyecharts.charts import Geo
import pyecharts.options as opts
from pyecharts.globals import GeoType

# 地理坐标图表达某人旅游去往某一城市的意向

# 构造原始数据对（省略读表的过程）：10个城市和对应的期望值

data = [('台湾', '10'), ('西安', '30'), ('重庆', '80'), ('香港', '20'), ('广州', '100'),
        ('武汉', '90'), ('长沙', '40'), ('北京', '50'), ('上海', '70'), ('成都', '100')]

# 绘图需求
# 1. 地图坐标系（schema）为中国地图
# 2. 图例系列名称为空，数据标签隐藏
# 3. 地理坐标图的类型设置为在其上打散点（scatter）
# 4. 加视觉映射
# 5. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "travel_geo.html"
# 执行绘图
geo = (
    Geo()
    .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True))
    .add_schema(maptype="china")
    .add(
        series_name="",
        data_pair=data,
        label_opts=opts.LabelOpts(is_show=False),
        type_=GeoType.SCATTER  # 或者直接"scatter"
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
