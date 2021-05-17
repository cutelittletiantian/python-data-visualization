import os
from pyecharts.charts import Pie
import pyecharts.options as opts

"""准备原始数据：IT网站各分区下的访问量

略去读文件过程，读取结果如下：
"""
# 绘制饼状图，数据项及其取值按照一个个元组进行组合
user_data = [('深度学习', 1000), ('数据分析', 700), ('Web开发', 500), ('爬虫开发', 350),
             ('图像处理', 250), ('机器学习', 220), ('数据挖掘', 200), ('人工智能', 180),
             ('自然语言处理', 160), ('游戏开发', 140), ('数据库开发', 120), ('可视化工程', 832)]
# 预处理：依照值将user_data从大到小排个序，后面显示会更漂亮
user_data.sort(key=lambda data_item: data_item[1], reverse=True)


"""执行绘图

1. 将列表中的元组按照元组中的第二个数的大小，也就是阅读量的大小，从大到小排序。
2. 设置数据标签的格式为“图例: 占比”（占比在显示时要带上百分号），（怎样设置格式formatter去查pyecharts官方文档）
3. 设置按照玫瑰图的方式显示，且圆心角相同，数值大小通过每一块饼的大小直观比对（这一步需要查pyecharts官方文档）。
4. 设置图表的标题为"阅读量统计”。
5. 适当调整图表中一些元素的位置，避免遮挡、排版凌乱等问题
6. 生成图表，保存
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "web_visit_rose_pie.html"

rose_pie = (
    Pie()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="阅读量统计", subtitle="技术专栏模块"),
        # 图例位置默认会遮挡标题，下面这样的调整是不断试错找出的布局方式
        legend_opts=opts.LegendOpts(
            pos_left="1%",
            pos_top="60%",
            orient="vertical",
            type_="scroll"
        )
    )
    .add(
        series_name="用户数据",
        data_pair=user_data,
        label_opts=opts.LabelOpts(
            # {b}和{d}表示图例名称和占比数值（不带百分号），这一步控制每一块饼旁边显示的东西是什么，具体地可以查文档
            formatter="{b}: {d}%"
        ),
        rosetype="area"  # 圆心角相同，数据差别靠每一块饼的半径凸显出来
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
