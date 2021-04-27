import os
import pyecharts.options as opts
from pyecharts.charts import Bar

"""指定存储目录
"""
resultPath = "./result"

"""原始数据表（省略获取、清晰、从文件读取等逻辑）

字段：姓名 | 身高（单位：米） | 体重（单位：千克）
"""
student_infos = [
    ('yoyo', 1.55, 45),
    ('coco', 1.6, 50),
    ('jojo', 1.58, 48),
    ('momo', 1.68, 55),
    ('bobo', 1.65, 49)
]

"""提取表格各列数据，准备包括后续充当x轴的name等字段
"""
# 将5位同学的姓名存入变量名为'name'的列表中
name = [student_info[0] for student_info in student_infos]
# 按照同学姓名的顺序，依次将同学的身高存入变量名为'height'的列表中
height = [student_info[1] for student_info in student_infos]
# 按照同学姓名的顺序，依次将同学的体重存入变量名为‘weight’的列表中
weight = [student_info[2] for student_info in student_infos]

"""计算BMI，准备x轴字段对应y轴数据
"""
bmiList = []
for one_name, one_height, one_weight in student_infos:
    # 保留整数
    bmiList.append(
        # round(one_weight/(one_height**2), 0)
        round(one_weight / (one_height ** 2))
    )

"""作图

标题：BMI数据统计
x轴：学生姓名
y轴：bmi值计算结果，图例无
存储位置：./result/bmi.html
"""
resultFileName = "bmi.html"
bar = (Bar().set_global_opts(title_opts=opts.TitleOpts(title="BMI数据统计"))
       .add_xaxis(xaxis_data=name)
       .add_yaxis(y_axis=bmiList, series_name="")
       .render(path=os.path.join(resultPath, resultFileName))
       )