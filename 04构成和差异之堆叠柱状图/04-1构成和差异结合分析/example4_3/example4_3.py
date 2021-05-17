import os
from pyecharts.charts import Bar
import pyecharts.options as opts

"""准备数据：一年来商品的销售

walnut_sales可能是下半年引入的新品
前半年无数据部分用"-"填充空位，确保x轴和y轴对得上位
"""
# 月份
months = [f"{mon}月" for mon in range(1, 13)]
# 各种商品的销售额
choc_sales = [2045, 2580, 2789, 3455, 3256, 3678, 5340, 6078, 6460, 6475, 7431, 8038]
gum_sales = [1234, 1467, 1754, 2354, 2897, 3487, 4340, 4379, 4460, 5075, 5431, 6038]
walnut_sales = ["-", "-", "-", "-", "-", "-", 6340, 5579, 4460, 4075, 3431, 3038]

"""执行堆叠柱状图绘制和保存

1、各月各商品销售额堆积图中：
第一层为巧克力的销售额。
第二层为口香糖的销售额。
第三层为核桃的销售额。
2、x轴是月份
3、y轴是各种销售额，图例分别为巧克力、口香糖、核桃，采用堆叠方式，堆叠stack统一命名为sales
4、数值label要防止被遮挡，显示在柱子中间
5、1~6月部分新品还没有数据，用"-"顶替数据缺项
6、整张图的标题是“2020全年商品销售额变化”
7、考虑到x轴真的太！！！多！！！了！！！
显示的时候考虑把x轴和y轴翻转（reversal）一下（横过来），不然图像太长了......
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "sales_annual_stacked_bar.html"
# 绘图
stacked_bar = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="2020全年商品销售额变化"))
    .add_xaxis(xaxis_data=months)
    .add_yaxis(
        series_name="巧克力",
        y_axis=choc_sales,
        stack="sales",  # 先加y轴的堆叠在底下，后加y轴的堆叠在上面
        label_opts=opts.LabelOpts(position="inside")
    )
    .add_yaxis(
        series_name="口香糖",
        y_axis=gum_sales,
        stack="sales",
        label_opts=opts.LabelOpts(position="inside")
    ).add_yaxis(
        series_name="核桃",
        y_axis=walnut_sales,
        stack="sales",
        label_opts=opts.LabelOpts(position="inside")
    )
    .reversal_axis()  # xy轴翻转，把图表横过来
    .render(path=os.path.join(resultPath, resultFileName))
)
