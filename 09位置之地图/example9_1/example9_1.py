import os
from pyecharts.charts import Map
import pyecharts.options as opts

# 准备原始数据（从文件中读取数据的过程省略）：各国排名世界top500财富榜的企业个数
# 在地图上做可视化的绘图数据格式：[("地点1", 对应数值1), ("地点2", 对应数值2), ...]
# 国家和对应的数据，组成了列表dataList
dataList = [('China', 124), ('United States', 121), ('Japan', 53), ('France', 31), ('Germany', 27),
            ('United Kingdom', 22), ('Korea', 14), ('Switzerland', 14), ('Canada', 13), ('Netherlands', 13)]


# 地图绘制需求
# 1. 数据系列名为空
# 2. 参数图片类型设置为世界地图（参数怎么指定，需要查阅文档）
# 3. 数据标签隐藏
# 4. 视觉映射配置项，将最大映射值设为130
# 5. 设置标题为"排名前10的国家"
# 6. 保存
# 存储路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 存储文件名
resultFileName = "top10property_world_map.html"
# 执行绘图
mapChart = (
    Map()
    .set_global_opts(
        title_opts=opts.TitleOpts("排名前10的国家"),
        visualmap_opts=opts.VisualMapOpts(max_=130)
    )
    .add(
        series_name="",
        data_pair=dataList,
        label_opts=opts.LabelOpts(is_show=False),
        maptype="world"
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
