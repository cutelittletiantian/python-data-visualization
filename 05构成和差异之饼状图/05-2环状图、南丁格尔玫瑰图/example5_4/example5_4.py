import os
from pyecharts.charts import Pie
from pyecharts import options as opts

"""原始数据：两场网络直播带货中，不同产品的销量情况

数据：(产品名称, 销量)
"""
liveCommerceOne = [("衬衫", 111), ("羊毛衫", 122), ("雪纺衫", 113), ("裤子", 210), ("高跟鞋", 170), ("袜子", 109)]
liveCommerceTwo = [("衬衫", 139), ("羊毛衫", 241), ("雪纺衫", 325), ("裤子", 260), ("高跟鞋", 210), ("袜子", 335)]


"""绘制多个南丁格尔玫瑰图（一共2个图表）

整个图表标题设为“网络直播带货销量对比”
图例系列名（series_name）均设为空
玫瑰图最大外径为绘图区（长宽小者）的60%，内径为绘图区的20%
玫瑰图类型设置为圆心角相同，数据大小仅通过
图1位置（即圆心位置）在绘图区的(25%, 50%)处（相对绘图区水平的25%和竖直的50%处）
图2位置（即圆心位置）在绘图区的(75%, 50%)处
数据标签（label）放在每一块饼的内部显示，格式为"{百分比取值}%"
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "live_commerce_rose_pie.html"
# 执行绘图
rose_pie = (
    Pie()
    .set_global_opts(title_opts=opts.TitleOpts(title="网络直播带货销量对比"))
    .add(
        series_name="",
        data_pair=liveCommerceOne,
        rosetype="area",
        radius=("20%", "60%"),
        center=("25%", "50%"),
        label_opts=opts.LabelOpts(
            position="inside",
            formatter="{d}%"
        )
    )
    .add(
        series_name="",
        data_pair=liveCommerceTwo,
        rosetype="area",
        radius=("20%", "60%"),
        center=("75%", "50%"),
        label_opts=opts.LabelOpts(
            position="inside",
            formatter="{d}%"
        )
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
