import os
from pyecharts.charts import Line, Bar
import pyecharts.options as opts

"""原始数据：日本男女收入情况调查

很巧，这次原始数据就是柱状图所需的x轴和y轴数据。

字段：年龄段 | 男性收入 | 女性收入
"""
# 定义存储年龄区间，男性收入、女性收入和平均收入数据列表
# x轴（公共）
ageList = ['<20', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '>=70']
# y轴（两组数据）
male_salaryList = [145, 262, 367, 434, 498, 570, 623, 641, 616, 457, 379, 374]
female_salaryList = [106, 231, 295, 296, 292, 284, 286, 276, 261, 214, 205, 215]

# 准备折线图的数据（男女平均值）
average_salaryList = [(male_salary + female_salary) / 2
                      for male_index, male_salary in enumerate(male_salaryList)
                      for female_index, female_salary in enumerate(female_salaryList)
                      if male_index == female_index]
# 二元变量条件筛选有没有用笛卡尔积组合？可以输出验证一下。使用if做下标限制就不会出现笛卡尔积提取数据问题了
# print(average_salaryList)


"""绘制柱线叠加图

1. 将年龄段作为x轴；
2. 将日本男性和女性收入数据作为y轴绘制柱状图；图例分别为“男性收入”“女性收入”
3. 将男女收入的平均值，作为y轴绘制折线图；y轴这里可以共享同一个坐标系
4. 将折线图叠加在柱状图上；叠加后注意折线图在更高图层，防止被柱子遮挡！！！
5. 将整个图表的标题设置为：日本男女收入情况调查；
6. 将图表保存
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "salary_bar_line.html"

bar_line = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="日本男女收入情况调查"))
    .add_xaxis(xaxis_data=ageList)
    .add_yaxis(series_name="男性收入", y_axis=male_salaryList)
    .add_yaxis(series_name="女性收入", y_axis=female_salaryList)
    .overlap(chart=(
        Line()
        .add_xaxis(xaxis_data=ageList)
        .add_yaxis(series_name="平均收入", y_axis=average_salaryList, z_level=1)  # 提升图层
    ))
    .render(path=os.path.join(resultPath, resultFileName))
)