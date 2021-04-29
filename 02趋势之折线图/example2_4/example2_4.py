import os
from pyecharts.charts import Line, Tab
import pyecharts.options as opts

"""数据来源（可能来自一个多sheet的excel表格，这里简化读表过程）"""
# 具体的气候数据存入下列列表中
# 最高平局气温数据
weather_dict = {
    # 平均最高气温
    "Average_highest": [8.1, 8.4, 11.3, 14.2, 17.9, 21.2, 23.5, 23.2, 20.2, 15.5, 11.1, 8.3],
    # 日均气温数据
    "Daily_mean": [5.2, 5.3, 7.6, 9.9, 13.3, 16.5, 18.7, 18.5, 15.7, 12.0, 8.0, 5.5],
    # 平均最低气温
    "Average_lowest": [2.3, 2.1, 3.9, 5.5, 8.7, 11.7, 13.9, 13.7, 11.4, 8.4, 4.9, 2.7],
    # 平均降水量
    "Average_precipitation": [55.2, 40.9, 41.6, 43.7, 49.4, 45.1, 44.5, 49.5, 49.1, 68.5, 59.0, 55.2],
    # 平均紫外线强度
    "Average_ultraviolet_index": [1, 1, 2, 4, 5, 6, 6, 5, 4, 2, 1, 0],
    # 平均日照时间
    "Mean_monthly_sunshine_hours": [61.5, 77.9, 114.6, 168.7, 198.5, 204.3, 212.0, 204.7, 149.3, 116.5, 72.6, 52.0]
}
# 气候数据的指标名称存入列表weather_key_list中（每个Tab维度的名称）
weather_key_list = list(weather_dict.keys())
# 将气候数据存入列表weather_value_list中（每个Tab维度下的y轴数据）
weather_value_list = list(weather_dict.values())
# 将12各月份并赋值给变量month（x轴信息）
month = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]


def create_line(x_axis_data, y_axis_data, legend_name) -> Line:
    """绘制曲线

    1、x轴是月份
    2、y轴是不同的气候数据系列的取值
    3、y轴图例是数据系列名，其中的下划线要全部换成空格
    4、每个系列的y轴取值的最大值和最小值要格外强调标注出来
    （markpoint_opts，这个标定有点套娃，我是看pyecharts官方文档干出来的）
    5、符合上述方法的图形要批量创建，用函数封装

    @:param x_axis_data x轴信息
    @:param y_axis_data y轴数据
    @:param legend_name y轴数据对应的图例

    @:return 创建好的曲线图Line对象
    """
    line = (Line()
            .add_xaxis(xaxis_data=x_axis_data)
            .add_yaxis(series_name=legend_name, y_axis=y_axis_data,
                       markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"),
                                       opts.MarkPointItem(type_="min")])
                       )
            )
    return line


"""建立看板，可切换不同的折线图进行观察，因为后面要添加多张折线图
"""
tab = Tab()
# 逐个创建新的曲线并添加至tab看板下
for weather_key, weather_value in weather_dict.items():
    # 把weather_key中的下划线换成空格呈现在最终的折线图中
    weather_key_modified = weather_key.replace("_", " ")
    tab.add(
        chart=create_line(x_axis_data=month, y_axis_data=weather_value, legend_name=weather_key_modified),
        tab_name=weather_key_modified
    )

# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "weather_tab.html"
# 执行多折线图看板的保存
tab.render(path=os.path.join(resultPath, resultFileName))
