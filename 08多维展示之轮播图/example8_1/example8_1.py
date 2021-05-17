import os
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Bar, Timeline
import pyecharts.options as opts
import openpyxl

# 工作簿统一所在路径
resourcesPath = "./resources"
# 工作簿名
gdpBookName = "历年前十大经济体.xlsx"
# 工作表名
gdpSheetName = "GDP"
gdpSheet = openpyxl.load_workbook(filename=os.path.join(resourcesPath, gdpBookName))[gdpSheetName]  # type: Worksheet


def get_data(row_num):
    """
    传入行数，返回用于绘制柱状图所必备的数据信息，将已经打开的工作表作为全局信息
    :param row_num:工作表的行数
    :return:三元组(年份，国家名列表，对应的GDP数值（单位：亿元）)
    """

    # 忠诚地读出当前行和下一行的原始数据，形如：
    # [(1970, '美国', '苏联', '日本', '西德', '法国', '英国', '意大利', '中国', '加拿大', '印度'),
    #  (None, 1024.9, 433.412, 209.071, 208.869, 146.985, 124.883, 109.258, 91.506, 86.304, 61.332)]
    org_data = [data_item for data_item in gdpSheet.iter_rows(min_row=row_num, max_row=row_num+1, values_only=True)]

    # 提取年份
    year_ = org_data[0][0]
    # 提取国家列表
    country_list = org_data[0][1:]
    # 提取对应的GDP取值
    gdp_list = org_data[1][1:]

    return year_, country_list, gdp_list


# 绘制轮播柱状图
timeline = Timeline()

# 扫描偶数行号，因为每一个偶数行号对应着一组新的数据，原表格一共有21行，暂时未找到合适的方法判断行数，所以直接用绝对数值
for rowNum in range(2, 21, 2):
    # 获取当前行绘图所需的(年份，x轴，y轴)所需数据
    year, x_data, y_data = get_data(row_num=rowNum)

    # 绘制单个柱状图
    # 1. 图例隐藏
    # 2. 图表的标题设置为："xxxx年前十大经济体GDP排名"；
    # 3. 逐个添加柱状图到轮播图，轮播图的每个时间节点设置：xxxx年；
    # 4. 将图表保存
    timeline.add(
        time_point=f"{year}年",
        chart=(
            Bar()
            .set_global_opts(
                title_opts=opts.TitleOpts(title=f"{year}年前十大经济体GDP排名"),
                legend_opts=opts.LegendOpts(is_show=False)
            )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
                series_name="",
                y_axis=y_data
            )
        )
    )

# 保存轮播图路径
resultPath = "./result"
if not os.path.exists(resultPath):
    os.mkdir(path=resultPath)
# 文件名
resultFileName = "GDP_bar_timeline.html"
# 执行保存
timeline.render(path=os.path.join(resultPath, resultFileName))
