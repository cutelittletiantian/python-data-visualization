import os
from pyecharts.charts import Radar
import pyecharts.options as opts

# 使用雷达图，综合评估两地的各种空气指标
# [AQI(空气质量指数), PM2.5, PM10, CO, NO2, SO2]

# 准备绘图用的初始顺序
# 构造A城市多日空气情况的二维数据表
A = [
    [55, 9, 56, 0.46, 18, 6],
    [25, 11, 21, 0.65, 34, 9],
    [56, 7, 63, 0.3, 14, 5],
    [33, 7, 29, 0.33, 16, 6],
    [42, 24, 44, 0.76, 40, 16],
    [82, 58, 90, 1.77, 68, 33],
    [74, 49, 77, 1.46, 48, 27],
    [78, 55, 80, 1.29, 59, 29],
    [267, 216, 280, 4.8, 108, 64],
    [185, 127, 216, 2.52, 61, 27],
    [39, 19, 38, 0.57, 31, 15],
    [41, 11, 40, 0.43, 21, 7],
]
# 构造B城市多日空气情况的二维数据表
B = [
    [91, 45, 125, 0.82, 34, 23],
    [65, 27, 78, 0.86, 45, 29],
    [83, 60, 84, 1.09, 73, 27],
    [109, 81, 121, 1.28, 68, 51],
    [106, 77, 114, 1.07, 55, 51],
    [109, 81, 121, 1.28, 68, 51],
    [106, 77, 114, 1.07, 55, 51],
    [89, 65, 78, 0.86, 51, 26],
    [53, 33, 47, 0.64, 50, 17],
    [80, 55, 80, 1.01, 75, 24],
    [117, 81, 124, 1.03, 45, 24],
    [99, 71, 142, 1.1, 62, 42],
]

# 绘制雷达图的需求
# 1. 坐标轴一共有6个维度，每个维度取名为相应空气指标的名字，每个维度限制合理的最大值和最小值
# 2. 坐标轴整体为圆形
# 3. A市的图例系列名称为“A市”，B市同理；颜色分别为#6495ed和#ff8c00
# 4. 不显示数据标签
# 5. 标题为"空气质量对比"
# 6. 执行保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "air_quality_radar.html"
# 按照格式设置坐标轴(schema)属性
c_schema = [
    opts.RadarIndicatorItem(name="AQI", max_=300, min_=5),
    opts.RadarIndicatorItem(name="PM2.5", max_=250, min_=20),
    opts.RadarIndicatorItem(name="PM10", max_=300, min_=5),
    opts.RadarIndicatorItem(name="CO", max_=5),
    opts.RadarIndicatorItem(name="NO2", max_=200),
    opts.RadarIndicatorItem(name="SO2", max_=100)
    # 等价于用字典创建
    # {"name": "AQI", "max": 300, "min": 5},
    # {"name": "PM2.5", "max": 250, "min": 20},
    # {"name": "PM10", "max": 300, "min": 5},
    # {"name": "CO", "max": 5},
    # {"name": "NO2", "max": 200},
    # {"name": "SO2", "max": 100}
]
# 执行绘图
radar = (
    Radar()
    .set_global_opts(title_opts=opts.TitleOpts(title="空气质量对比"))
    .add_schema(schema=c_schema, shape="circle")
    .add(
        series_name="A市",
        data=A,
        label_opts=opts.LabelOpts(is_show=False),
        color="#6495ed"
    )
    .add(
        series_name="B市",
        data=B,
        label_opts=opts.LabelOpts(is_show=False),
        color="#ff8c00"
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
