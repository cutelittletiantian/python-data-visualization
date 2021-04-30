import os
from pyecharts.charts import Line, Bar
import pyecharts.options as opts


"""数据来源：可能是年级数学校验组统计考试扣分情况的表格中提取出来的字典

字段：知识点名称 | 平均扣分值 ，以字典存储
"""
knowledge = {
    "圆锥曲线": 7.5,
    "直线与圆": 5.0,
    "立体几何": 10.1,
    "空间向量": 3.2,
    "数列": 14.5,
    "解三角": 1.9,
    "导数": 28.5,
    "函数模型": 3.3,
    "二项式定理": 3.0,
    "线性规划": 4.0,
    "平面向量": 3.5,
    "复数": 1.3,
    "集合": 1.9
}


"""坐标数据准备1：

准备帕累托图的柱状图【数据】部分：
1、横坐标：知识点名称
2、纵坐标：平均扣分的取值
3、帕累托图下的约束：纵坐标由左至右必须从大到小排列
"""
# 取出knowledge中的键值对，以值为依据将键值对进行排序（从大到小）后，将键值对以元组的形式存在knowledge_sorted中
knowledge_sorted = sorted(knowledge.items(), key=lambda knowledge_item: knowledge_item[1], reverse=True)

# 取出x轴数据
xaxis_data = [kn_item[0] for kn_item in knowledge_sorted]
# 取出柱状图的y轴数据
yaxis_data = [kn_item[1] for kn_item in knowledge_sorted]


"""坐标数据准备2：

准备帕累托图的折线图【数据】部分：
1、横坐标：知识点名称
2、纵坐标：知识点出现的累计占比（当前知识点及其左边知识点柱状图的面积和占柱状图总面积比）
3、帕累托图下的约束：纵坐标取值必须是百分数（不含%号）
"""
# 定义一个累计频率的空列表percentlist，用yaxis_data的元素初始化
y_line_percentList = [data for data in yaxis_data]
# 计算折线图的y轴数据总和
total_y_data = sum(yaxis_data)
# 添加相应的频率
for index, y_data in enumerate(y_line_percentList[1:], start=1):
    # 当前元素 = 当前元素 + 前一个元素
    # 与前一个不断累加
    y_line_percentList[index] = y_data + y_line_percentList[index - 1]
# 化作百分数形式（保留两位小数）
y_line_percentList = [round(data * 100 / total_y_data, 2) for data in y_line_percentList]
# 解开注释可以控制台验证取值正确性：
# print(percentList)
# print(yaxis_data)


"""帕累托图的柱状图部分绘制

1、x轴是知识点名称xaxis_data，适当倾斜以防止横坐标之间相互遮挡显示不全
2、y轴是平均失分的直接数值yaxis_data，图例“扣分”
3、柱状图标题设置为“数学模块最薄弱的失分点”
4、另起空y轴（extend_axis向yaxis依赖注入），用于后续累加的折线图纵轴取值
"""
bar = (
    Bar()
    .set_global_opts(title_opts=opts.TitleOpts(title="数学模块最薄弱的失分点"),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45))
                     )
    .add_xaxis(xaxis_data=xaxis_data)
    .add_yaxis(series_name="扣分", y_axis=yaxis_data)
    .extend_axis(yaxis=opts.AxisOpts())
)


"""帕累托图的折线图部分绘制

1、x轴是知识点名称xaxis_data
2、y轴是知识点出现的累计占比（当前知识点及其左边知识点柱状图的面积和占柱状图总面积比，percentList），图例“扣分占比”
3、x轴确保和帕累托图的柱状图部分一致
4、y轴用帕累托图的柱状图部分之前创建的空y轴（后创建的y轴，yaxis_index为1）
5、线容易被柱子挡住，确保折线图放在比柱状图更高图层的位置（z_level大）
"""
line = (
    Line()
    .add_xaxis(xaxis_data=xaxis_data)
    .add_yaxis(series_name="扣分占比", y_axis=y_line_percentList,
               yaxis_index=1,
               z_level=1)
)


"""万事俱备，合成帕累托图

往柱状图上叠加（overlap）折线图
"""
pareto = bar.overlap(line)

# 保存帕累托图
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
resultFileName = "math_analysis_pareto.html"

pareto.render(path=os.path.join(resultPath, resultFileName))
