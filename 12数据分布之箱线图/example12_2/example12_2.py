import os
from pyecharts.charts import Boxplot
import pyecharts.options as opts

# 准备原始数据
# x轴：各学科名称
xData = ["物理", "化学", "生物", "历史", "政治", "地理"]
# 以及xi轴对应yi，yi是该科目多次调考的考试成绩
y1 = [83, 88, 93, 79, 86, 89, 95, 90, 94, 92]
y2 = [77, 79, 74, 82, 73, 78, 75, 85, 83, 81]
y3 = [94, 93, 97, 89, 92, 97, 91, 85, 82, 96]
y4 = [82, 81, 79, 85, 88, 73, 78, 82, 75, 79]
y5 = [71, 78, 74, 73, 79, 77, 75, 74, 75, 81]
y6 = [62, 65, 72, 66, 78, 73, 66, 68, 61, 63]

# 绘制箱线图
# 注意用yi生成各科的[min, Q2, mid, Q1, max]数据，用于后续绘制箱线图
# 绘图的其它需求
# 1. 主题为马卡龙画风(macarons)
# 2. 让箱线图的须更长，数据分布更易于观察：把y轴的最小值设为数据的最小值，而不是从0开始
# （这一步怎么设置的，建议查一下文档，写得明明白白）
# 3. 全图标题“各科成绩”
boxplot = (
    Boxplot(init_opts=opts.InitOpts(theme="macarons"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各科成绩"),
        yaxis_opts=opts.AxisOpts(min_="dataMin")  # dataMin怎么来的，官方文档上去查，写得明明白白
    )
    .add_xaxis(xaxis_data=xData)
)
# 添加y轴数据
boxplot.add_yaxis(
    series_name="",
    y_axis=boxplot.prepare_data([y1, y2, y3, y4, y5, y6])
)
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "scores_boxplot.html"
# 执行保存
boxplot.render(path=os.path.join(resultPath, resultFileName))
