# 探究泰坦尼克号不同等级船舱的乘客年龄分布情况
import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from pyecharts.charts import Boxplot
import pyecharts.options as opts

# 资源文件目录
resourcesPath = "./resources"
# 泰坦尼克号遇难者名单
titanicBookName = "titanic.xlsx"
# 乘客名单工作表
passengerSheetName = "passenger"
# 打开文件、选表
passengerSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, titanicBookName)
)[passengerSheetName]  # type: Worksheet

# 选择[船舱等级, 年龄]两列的数据，提取这两列的原始数据
orgData = [
    [row_item[1], row_item[4]]
    for row_item in passengerSheet.iter_rows(min_row=2, values_only=True)
]


# 处理绘图用的数据
plotData = {
    "一等舱": [],
    "二等舱": [],
    "三等舱": []
}
# 扫描原始数据
for pClass, age in orgData:
    if pClass == 1:
        plotData["一等舱"].append(age)
    elif pClass == 2:
        plotData["二等舱"].append(age)
    elif pClass == 3:
        plotData["三等舱"].append(age)


# 绘制船舱等级与年龄关系的箱线图，需求：
# 1. 主题为light
# 2. 标题为“舱位与年龄的分布”
# 3. y轴起点是上述y轴所有数据的最小值
boxplot = (
    Boxplot(init_opts=opts.InitOpts(theme="light"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="舱位与年龄的分布"),
        yaxis_opts=opts.AxisOpts(min_="dataMin")
    )
    .add_xaxis(xaxis_data=list(plotData.keys()))
)
# 获取箱线图y轴[min, Q2, mid, Q1, max]序列
yData = boxplot.prepare_data(items=[plot_value for plot_value in plotData.values()])
print(yData)
boxplot.add_yaxis(
    series_name="",
    y_axis=yData
)

# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "titanic_boxplot.html"
# 执行保存
boxplot.render(path=os.path.join(resultPath, resultFileName))
