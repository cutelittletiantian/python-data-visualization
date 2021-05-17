import os
from pyecharts.charts import Scatter
import pyecharts.options as opts
import openpyxl
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# 资源目录
resourcesPath = "./resources"
# 日均销量对比工作表名
dailySalesBookName = "日均销量对比.xlsx"
# 选中工作表
wb = openpyxl.load_workbook(filename=os.path.join(resourcesPath, dailySalesBookName))  # type: Workbook
sheet = wb["销量对比"]  # type: Worksheet

# 取出阿珍和竞品商的销售数据（因为本身这个表结构不是特别好，所以读的话就按照下面毫无复用性的烂代码读吧）
# 取出需要对比的商品名称（作为x轴）
name_list = []
for cell in sheet["B"][1:7]:
    name_list.append(cell.value)

# 将商品销量这一列数据全部提取出
sales_list = []
for cell in sheet["C"]:
    sales_list.append(cell.value)
# 阿珍的数据sales_azhen（y轴数据1）
sales_azhen = sales_list[1:7]
# 竞品的数据sales_competitor（y轴数据2）
sales_competitor = sales_list[7:13]

# 绘制散点图需求
# 1. 标题“日均销量对比”
# 2. 阿珍的数据用点表示，竞品数据用菱形表示（查官方文档找参数）
# 3. 添加视觉映设，最大映射取350，最小映射取20，数据大小通过视觉映射的大小体现（查文档找参数）
# 4. 图例系列名分别为“阿珍”和“竞品”
# 5. 设置x轴名称为“商品”，y轴名称为“销量”
# 6. 保存文件
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "product_competitor_scatter.html"
# 执行绘图
scatter = (
    Scatter()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="日均销量对比"),
        visualmap_opts=opts.VisualMapOpts(
            max_=350,
            min_=20,
            type_="size"
        ),
        xaxis_opts=opts.AxisOpts(name="商品"),
        yaxis_opts=opts.AxisOpts(name="销量")
    )
    .add_xaxis(xaxis_data=name_list)
    .add_yaxis(
        series_name="阿珍",
        y_axis=sales_azhen
    )
    .add_yaxis(
        series_name="竞品",
        y_axis=sales_competitor,
        symbol="diamond"
    )
)
# 执行保存
scatter.render(path=os.path.join(resultPath, resultFileName))
