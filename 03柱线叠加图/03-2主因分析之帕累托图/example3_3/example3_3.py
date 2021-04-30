from pyecharts.charts import Bar, Line
import pyecharts.options as opts
import os

"""原始数据

字段：菜品名 | 年营业额（单位：元）
"""
dish_profit = {"番茄鸡蛋": 9900, "避风塘茄夹": 6660, "广东菜心": 5210, "红烧肉": 8880, "土豆烧排骨": 2300,
               "木耳炒肉": 1600, "虾仁蒸蛋": 4280, "胡萝卜牛腩": 3460, "水果沙拉": 1800, "狮子头": 3200}

"""准备公共x轴和柱状图、折线图分别的y轴
"""
# 键值对按值排序
dish_profit_sorted = sorted(dish_profit.items(), key=lambda x: x[1], reverse=True)

# 公共x轴数据
xaxisData = [data for (data, _) in dish_profit_sorted]
# 柱状图y轴数据
yaxisBar = [data for (_, data) in dish_profit_sorted]

# 计算折线图y轴所需数据（用yaxisBar初始化）
yaxisLine = [data for data in yaxisBar]
# y轴项目总和
sumYData = sum(yaxisBar)
# 求出折线图y轴下的值（百分数，无百分号形式，保留两位小数）
for index, y_data in enumerate(yaxisLine[1:], start=1):
    yaxisLine[index] = y_data + yaxisLine[index - 1]
yaxisLine = [round(y_data / sumYData * 100, 2) for y_data in yaxisLine]
# print(yaxisLine)


"""执行绘图

1. 将菜品名字作为x轴；
2. 菜品盈利额作为y轴，绘制柱状图，图例设置为”盈利额“；
3. 计算各个菜品的盈利占总盈利额的比例，作为y轴绘制折线图，图例设置为"盈利占比(%)"；
4. x轴的标签旋转45度，防遮挡；
5. 整个表的标题设置为“各菜品盈利额”；
6. 将折线图叠加（overlap）在柱状图上。
7. 将图表保存
8. y轴取值均只保留2位小数
9. 折线图y轴在柱状图y轴图层之上，防止柱子遮挡折线
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "restaurant_pareto.html"

bar = (
    Bar()
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
                     title_opts=opts.TitleOpts(title="各菜品盈利额"))
    .add_xaxis(xaxis_data=xaxisData)
    .add_yaxis(series_name="盈利额", y_axis=yaxisBar)
    .extend_axis(yaxis=opts.AxisOpts())  # 新y轴：index为1
    .overlap(
        chart=(
            Line()
            .add_xaxis(xaxis_data=xaxisData)
            .add_yaxis(series_name="盈利占比(%)", y_axis=yaxisLine, yaxis_index=1, z_level=1)
        )
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
