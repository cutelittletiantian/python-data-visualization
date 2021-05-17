import os
from pyecharts.charts import Bar
import pyecharts.options as opts

"""准备数据：2020年1-3季度GDP（单位：亿元）
"""
# 创建变量x_data储存季度名称，作为x轴的数据
x_data = ["第一季度", "第二季度", "第三季度"]
# 将每个产业的每个季度的生产值保存在一个字典中
data = {
    "第一产业": [8014.7, 13992.8, 20528.5],
    "第二产业": [67968.9, 93094.8, 94684.4],
    "第三产业": [107685.8, 118408.4, 123963.2]
}

"""执行堆叠柱状图绘制

1. x轴设置为列表x_data。
2. 逐个添加y轴数据data
图例设置为字典的key，取值为key中对应的value
堆积名称stack统一设置为"GDP"，
数据标签的位置设置为内部居中（inside）。
3. 图表标题为"2020年1-3季度GDP（单位：亿元）"
4. 将图表保存。
"""
stacked_bar = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="2020年1-3季度GDP（单位：亿元）"))
    .add_xaxis(xaxis_data=x_data)
)
# 循环添加y轴数据
for key, value in data.items():
    stacked_bar.add_yaxis(
        series_name=key,
        y_axis=value,
        stack="GDP",
        label_opts=opts.LabelOpts(position="inside")
    )
# 保存路径和文件名
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
resultFileName = "GDP_stacked_bar.html"

stacked_bar.render(path=os.path.join(resultPath, resultFileName))
