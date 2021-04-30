from pyecharts.charts import Bar, Line
import pyecharts.options as opts
import os


"""原始数据

字段：错误类型 | 近一周出现次数
"""
causes_statistics = {
    "名字拼写错误": 27,
    "地址错误": 16,
    "电话号码错误": 12,
    "邮箱错误": 9,
    "验证码错误": 3
}


"""提取坐标轴数据

x轴：错误类型（柱线公共）
柱状图y轴：x轴对应直接数据，自左向右由大到小。图例“原因”
折线图y轴：当前字段及其前柱子面积占比之和。图例“原因占比(%)”
"""
# 预备：将原始数据键值对按值自大到小排序
causes_statistics_sorted = sorted(causes_statistics.items(),
                                  key=lambda cause: cause[1], reverse=True)
# 输出一下证明它是列表
# print(causes_statistics_sorted)
# 提取公共x轴
x_data = [xData for xData, _ in causes_statistics_sorted]
# 提取柱状图y轴
y_data_bar = [yDataBar for _, yDataBar in causes_statistics_sorted]

# y轴数据总和
yTotal = sum(y_data_bar)
# 提取折线图y轴（不能直接用y_data_bar赋值柱状图存的原y轴数据，避免浅复制）
y_data_line = list(y_data_bar)
# 计算前所有字段面积占比（百分值去%符号），保留两位小数
for index, y_data in enumerate(y_data_line[1:], start=1):
    y_data_line[index] = y_data + y_data_line[index - 1]
y_data_line = [round(y_data*100/yTotal, 2) for y_data in y_data_line]


"""绘制帕累托图

1. 将未激活原因作为x轴；
2. 将未激活数量作为y轴，绘制柱状图；
3. 将柱状图的图例设置为原因，将柱状图的透明度（opacity，用法查pyecharts官方文档）设置为0.5，以防止遮挡折线图部分；
4. 将整个图表的标题设置为：信用卡未激活的原因；
5. 另起y轴，将累计频率作为y轴，绘制折线图，将折线图的图例设置为"原因占比(%)"；
6. 将折线图叠加在柱状图上。
7. 将文件保存
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "credit_company_pareto.html"
# 执行绘图
pareto = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="信用卡未激活的原因"))
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(series_name="原因", y_axis=y_data_bar, yaxis_index=0,
               itemstyle_opts=opts.ItemStyleOpts(opacity=0.5))
    .extend_axis(yaxis=opts.AxisOpts())  # 添加新的空y轴，index为1
    .overlap(chart=(
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(series_name="原因占比(%)", y_axis=y_data_line,
                   yaxis_index=1)
    ))
    .render(path=os.path.join(resultPath, resultFileName))
)