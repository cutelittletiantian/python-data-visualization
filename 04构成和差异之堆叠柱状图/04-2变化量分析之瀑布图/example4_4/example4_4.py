import os
from pyecharts.charts import Bar
import pyecharts.options as opts

"""原数据：个体商户12个月的资金流动情况

利用瀑布图表达出每个月的盈亏变化
"""
x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
# 当月资金流动情况（+盈利，-亏损）
alter_data = [4000, 3450, 2850, -1800, -1500, 9000, 1300, 1000, 2100, -1000, -4200, -1510]
# 年初总资金
beginTotal = 5000
# 年末剩余总资金
endTotal = 18690

"""准备瀑布图数据

增加年初值和年末余值单独表示，用一组单独的柱子表示（体现不同的颜色）
中间1~12月份的数据全部用“变化量”表示（+盈-亏），变化取值悬浮于半空中，体现总值的大致走向
体现“柱子漂浮”的现象，需要柱子下方有“打底”的白色柱子垫着
打底柱子上方，放当月盈利值或者亏损值（需要创建盈利柱子和亏损柱子数据分开讨论，这样最终画出来，不同颜色的柱子区分能区分盈利和亏损）
打底柱子当月取值：当月总额-盈利值（如果是盈利）或者当月总额（如果是亏损）
所以打底柱子想求出来，先要把各个月当月总额求出来
"""
# 扩展x轴，增加年初值和年末余值两项
x_data.insert(0, "年初值")
x_data.append("年末余值")

# 增加的两项对应值单独创建一组y轴，区分颜色
total_data = ["-"] * len(x_data)
total_data[0] = beginTotal
total_data[-1] = endTotal

# 盈利提取数据y轴对应项（注意两端缺项）  ["-"] * 14
y_profit_extracted_data = ["-"] * len(x_data)
# 亏损提取数据y轴对应项（注意两端缺项）  ["-"] * 14
y_loss_extracted_data = ["-"] * len(x_data)
# 放盈利/亏损提取数据两种情景的柱子，下标从1开始（跳过头部的缺项）
for extracted_index, alter_item in enumerate(alter_data, start=1):
    if alter_item > 0:
        y_profit_extracted_data[extracted_index] = alter_item
    elif alter_item < 0:
        # 负数取相反数
        y_loss_extracted_data[extracted_index] = -alter_item
    # else，即alter_item == 0：保持缺项

# 打底柱子取值的计算（两端缺项） ["-"] * 14
base_data = ["-"] * len(x_data)
# 辅助计算使用：存放当月变化后的总收入（月末） ["-"] * 12
temp_total_data = ["-"] * len(alter_data)
temp_total_data[0] = beginTotal + alter_data[0]
for index, alter_item in enumerate(alter_data[1:], start=1):
    temp_total_data[index] = temp_total_data[index - 1] + alter_item
# 计算base_data
for index, alter_item in enumerate(alter_data):
    if alter_item > 0:
        base_data[index + 1] = temp_total_data[index] - alter_item
    elif alter_item < 0:
        base_data[index + 1] = temp_total_data[index]
    else:  # alter_item == 0
        base_data[index] = "-"
print(base_data)

"""绘制瀑布图

- 图例统一设置为空，堆叠stack统一为"waterfall_plot"
- 打底柱子颜色设置为白色；
- 其它x轴和y轴按照顺序进行叠加即可，盈利和亏损的悬浮柱子要设置图例，分别为“盈利”“亏损”
- 设置图片标题为"全年每月收入与支出"；注意避免横坐标丢失。
- 将瀑布图保存
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "in_out_waterfall_stacked_bar.html"

waterfall_stacked_bar = (
    Bar()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="下半年每月收入与支出"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45))
    )
    .add_xaxis(
        xaxis_data=x_data,
    )
    .add_yaxis(
        series_name="",
        y_axis=base_data,
        color="white",
        stack="waterfall_plot",
        # 隐藏起来打底的柱子
        label_opts=opts.LabelOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=False)
    )
    .add_yaxis(
        series_name="",
        y_axis=total_data,
        stack="waterfall_plot"
    )
    .add_yaxis(
        series_name="盈利",
        y_axis=y_profit_extracted_data,
        stack="waterfall_plot"
    )
    .add_yaxis(
        series_name="亏损",
        y_axis=y_loss_extracted_data,
        stack="waterfall_plot"
    )
    .render(path=os.path.join(resultPath, resultFileName))
)