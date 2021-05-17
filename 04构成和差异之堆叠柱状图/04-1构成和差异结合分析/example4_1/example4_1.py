import os
from pyecharts.charts import Bar
import pyecharts.options as opts


"""原始数据：2020下半年部分商品销售额变化表

下半年一共跟踪了choc(olate)、gum和walnut的销售情况（单位：元）
接下来分析销售额的组成和比较不同月份各各产品销售情况的差异
"""
# 设置列表
months = ["7月", "8月", "9月", "10月", "11月", "12月"]
choc_sales = [5340, 6078, 6460, 6475, 7431, 8038]
gum_sales = [4340, 4379, 4460, 5075, 5431, 6038]
walnut_sales = [6340, 5579, 4460, 4075, 3431, 3038]


"""执行绘图

1、采取直接数据的堆叠方式展现（同一个x轴下的数据在同一个stack展示）
2、x轴：月份
3、y轴：产品对应月份销售额。图例分别是：巧克力、口香糖、核桃
4、整个图表的标题：2020下半年商品销售额变化
5、堆叠：指定y轴数据在同一个stack（怎么搞的去查pyecharts官方文档）
6、避免数据遮挡：柱子堆叠的时候，底下柱子的数值label会被上面的柱子遮挡，
这是可以设置数值label显示在自己的柱子中间（怎么搞的去查pyecharts官方文档）
"""
# 创建Bar对象，赋值给变量bar
stacked_bar = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="2020下半年商品销售额变化"))
    .add_xaxis(xaxis_data=months)
    .add_yaxis(
        series_name="巧克力",
        y_axis=choc_sales,
        stack="sales",
        label_opts=opts.LabelOpts(position="inside")
    )
    .add_yaxis(
        series_name="口香糖",
        y_axis=gum_sales,
        stack="sales",  # stack同名就堆叠一个柱子上
        label_opts=opts.LabelOpts(position="inside")
    )
    .add_yaxis(
        series_name="核桃",
        y_axis=walnut_sales,
        stack="sales",
        label_opts=opts.LabelOpts(position="inside")
    )
)


# 使用render函数将堆积柱状图保存在指定路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
resultFileName = "sales_stacked_bar.html"

stacked_bar.render(path=os.path.join(resultPath, resultFileName))
