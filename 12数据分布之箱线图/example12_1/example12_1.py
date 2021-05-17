import os
from pyecharts.charts import Boxplot, Grid
import pyecharts.options as opts

# 准备原始数据（为方便直观表达绘制过程，这里读表的过程先跳过）
# x轴数据
xData = ["15℃", "20℃", "25℃", "30℃", "35℃"]
# 用于绘制y轴的原始数据（假设一组yi对应一个x_data下的实验组测得的一组数据）
y1 = [383, 312, 348, 388, 375, 389, 432, 373, 377, 384]
y2 = [412, 432, 421, 354, 378, 392, 407, 413, 415, 405]
y3 = [400, 388, 397, 352, 423, 447, 378, 377, 395, 387]
y4 = [278, 288, 254, 213, 256, 278, 267, 256, 278, 266]
y5 = [213, 215, 234, 232, 278, 188, 223, 234, 225, 231]

# 绘制箱线图
boxplot = Boxplot()
# 生成绘箱线图图用的y轴数据（即每一组yi）的[下限值，下四分位点，中位数，上四分位点，上限值]
yData = boxplot.prepare_data([y1, y2, y3, y4, y5])
# print(y_data)
# 得到绘制5组温度下对应箱线图的[下限值，下四分位点，中位数，上四分位点，上限值]数据
# [[312, 366.75, 380.0, 388.25, 432], [354, 388.5, 409.5, 416.5, 432], [352, 377.75, 391.5, 405.75, 447],
# [213, 255.5, 266.5, 278.0, 288], [188, 214.5, 228.0, 234.0, 278]]

# 执行绘图
# 添加x轴数据
boxplot.add_xaxis(xaxis_data=xData)
# 添加y轴数据
boxplot.add_yaxis(series_name="实验组数据", y_axis=yData)

# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFilePath = "experiment_gp_boxplot.html"
# 设置标题和副标题
boxplot.set_global_opts(
    title_opts=opts.TitleOpts(title="探究温度对化肥有效成分含量的影响", subtitle="每种温度下共采集10组数据"),
    xaxis_opts=opts.AxisOpts(name="温度"),
    yaxis_opts=opts.AxisOpts(name="有效含量值(单位: g/500g)")
)

# 调整图形位置，解决副标题和y轴重叠问题
grid = (
    Grid(init_opts=opts.InitOpts(height="600px"))
    .add(
        chart=boxplot,
        grid_opts=opts.GridOpts(pos_top="20%")
    )
)

# 执行保存
grid.render(path=os.path.join(resultPath, resultFilePath))
