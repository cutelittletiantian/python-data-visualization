import os
from pyecharts.charts import Geo
import pyecharts.options as opts
from pyecharts.globals import GeoType
import openpyxl
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# 使用地理坐标图，表达某产品在全国范围的用户分布

# 资源文件夹
resourcesPath = "./resources"
# 用户分布文件
userBookName = "用户分布.xlsx"
# 用户分布工作表
userSheetName = "用户数量"

# 打开文件并选表
userSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, userBookName))[userSheetName]  # type: Worksheet
# 取出数据对
num_list = [row_item for row_item in userSheet.iter_rows(min_row=2, values_only=True)]
print(num_list)

# 绘制地理坐标图需求
# 1. 添加但隐藏视觉映射，最大映射1000，过渡颜色设置为['#33bbff','#0015ff','#2600e5','#8a2ee5','#cc2996']
# 2. 全图背景颜色为#475262
# 3. 坐标系设置：中国地图，地图底色为#2d3948，描边为#2efef7；鼠标选中高亮情况下，颜色为#2a333d
# 4. 设置散点样式表达单一地点的用户分布情况，设置热力图表达单一地点及附近地区的用户分布情况，均隐藏数据标签，图例系列名不用填
# 5. 图的标题：会员分布
# 6. 保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "user_geo.html"
# 执行地理坐标图绘制
geo = (
    Geo(init_opts=opts.InitOpts(bg_color="#475262"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="会员分布"),
        visualmap_opts=opts.VisualMapOpts(
            is_show=False,
            max_=1000,
            range_color=["#33bbff", "#0015ff", "#2600e5", "#8a2ee5", "#cc2996"]
        )
    )
    .add_schema(
        maptype="china",
        itemstyle_opts=opts.ItemStyleOpts(color="#2d3948", border_color="#2efef7"),
        emphasis_itemstyle_opts=opts.ItemStyleOpts(color="#2a333d")
    )
    .add(
        # 单区域散点表达
        series_name="",
        data_pair=num_list,
        type_=GeoType.SCATTER,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        # 区域热力图表达
        series_name="",
        data_pair=num_list,
        type_=GeoType.HEATMAP,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
