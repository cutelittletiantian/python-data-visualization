import os
from pyecharts.charts import Line
import pyecharts.options as opts

"""读取数据（读表过程略去，这里聚焦加载文件数据过后的情景）

原始数据是这样的二维表，或者每个姓名作为一个单独的Worksheet（工作表）

        |  1月   |  2月   |  3月   |  ...  |  11月  |  12月
huanhuan|
shushu  |           (中间放主播的带货成交额数据)
binbin  |
"""
# 三位主播的带货成交额数据存入下列列表中
huanhuan = [2.3, 2.3, 1.3, 1.2, 2.4, 3.6, 3.5, 3.4, 2.2, 5.5, 10.1, 9.2]
shushu = [5.2, 4.9, 4.6, 4.7, 4.4, 5.6, 5.5, 5.5, 4.1, 6.5, 5.0, 5.2]
binbin = [3.2, 3.3, 5.6, 5.4, 3.6, 4.2, 4.5, 2.5, 8.1, 8.6, 8.8, 6.3]
# 将12各月份并赋值给变量month
month = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

"""制图

1、横坐标为月份，纵坐标是各主播带货的月成交额情况
2、曲线是平滑的
3、多曲线
4、huanhuan的折线，标记（symbol）设为"circle"。
shushu的折线，标记设为"rect"。
binbin的折线，标记设为"triangle"。
5、标记的大小均为10
6、保存
"""
line = (Line()
        .add_xaxis(xaxis_data=month)
        .add_yaxis(series_name="huanhuan", y_axis=huanhuan,
                   symbol="circle", symbol_size=10,
                   is_smooth=True)
        .add_yaxis(series_name="shushu", y_axis=shushu,
                   symbol="rect", symbol_size=10,
                   is_smooth=True)
        .add_yaxis(series_name="binbin", y_axis=binbin,
                   symbol="triangle", symbol_size=10,
                   is_smooth=True)
        )
# 存储目录
resultPath = "./result"
# 文件名
resultFileName = "live_deal.html"
# 执行保存
line.render(path=os.path.join(resultPath, resultFileName))
