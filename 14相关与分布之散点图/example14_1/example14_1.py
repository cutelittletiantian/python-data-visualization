import os
import openpyxl
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Scatter
import pyecharts.options as opts

# 用散点图描述电竞游戏职业玩家WJ.TS的100局游戏中，经济占比对输出占比影响的相关性

# 基础参数
# 资源文件所在目录
resourcesPath = "./resources"
# 职业玩家的游戏数据文件
gameBookName = "wj.xlsx"
# 工作表名称
gameSheetName = "选手数据"

# 取出输出和经济数据，因为原表结构不是很好，代码不是很讲究复用性
wb = openpyxl.load_workbook(filename=os.path.join(resourcesPath, gameBookName))  # type: Workbook
sheet = wb[gameSheetName]  # type: Worksheet
# 100局游戏的输出数据，作为x轴
attack_list = []
# 100局游戏的经济数据，作为y轴
income_list = []
for attackCell, incomeCell in zip(sheet["K"], sheet["M"]):
    attack_list.append(attackCell.value)
    income_list.append(incomeCell.value)

# 截取出WJ.TS的输出数据
attack_list = attack_list[1:101]
# 截取出WJ.TS的经济数据
income_list = income_list[1:101]
# print(attack_list)
# print(income_list)

# 散点图绘制需求
# 1. x轴的数据不是用作零散的数据项，而是作为取值，注意设定x轴类型（查文档）
# 2. 散点数据的标签要隐藏
# 3. x轴名为"经济占比"，y轴名为"伤害占比"
# 4. 标题"输出占比与经济占比之间的关系"
# 5. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "attack_income_scatter.html"
# 执行绘图
scatter = (
    Scatter()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="输出占比与经济占比之间的关系"),
        xaxis_opts=opts.AxisOpts(name="经济占比", type_="value"),
        yaxis_opts=opts.AxisOpts(name="伤害占比")
    )
    .add_xaxis(xaxis_data=income_list)
    .add_yaxis(
        series_name="伤害-经济相关性",
        y_axis=attack_list,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
