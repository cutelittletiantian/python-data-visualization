import os
# 使用from...import从pyecharts.charts中导入Bar模块
from pyecharts.charts import Bar
# 使用from...import从pyecharts中导入options模块并简写为opts
from pyecharts import options as opts

# 目标存储的路径
resultPath = "./result"

"""数据来源（简化到已经清洗完毕并读取至列表的情形）"""
# 将公司的名字存入变量名为"name"的列表中
name = ["ibm", "microsoft", "pwc", "citi", "amazon", "apple", "ey", "walmart", "siemens", "google"]
# 按照公司名字的顺序，依次将公司的人数存入变量名为"employee"的列表中
employee = [274047, 116196, 111372, 101482, 93247, 90095, 158363, 120753, 87381, 75109]

"""绘图"""
# 创建Bar对象，并赋值给bar
bar = Bar()
# 设置图表的标题为“公司人数对比”
bar.set_global_opts(title_opts=opts.TitleOpts(title="公司人数对比"))
# 传入参数xaxis_data=name使用add_xaxis()设置x轴为公司名称
bar.add_xaxis(xaxis_data=name)
# 传入参数y_axis=employee，使用add_yaxis()设置y轴图例为“公司人数”
bar.add_yaxis(y_axis=employee, series_name="公司人数")
# 使用render()绘制柱状图保存
resultFileName = "company_size.html"
bar.render(path=os.path.join(resultPath, resultFileName))
