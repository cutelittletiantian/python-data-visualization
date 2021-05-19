import os
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook
from pyecharts.charts import Radar
import pyecharts.options as opts

# 用雷达图绘制看上去比较高大上的手机品牌多项指标综合评测

# 配置项
# 资源文件目录
resourcesPath = "./resources"
# 手机测评文件名
phoneTestBookName = "test.xlsx"
# 手机测评工作表名
phoneTestSheetName = "测评数据"

# 打开文件并选表
phoneTestSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, phoneTestBookName))[phoneTestSheetName]  # type: Worksheet
# 取出原始数据
# 数据项一共有：["外观", "性能", "拍照", "系统", "屏幕"]，表头无需读取
orgData = [list(row_item) for row_item in phoneTestSheet.iter_rows(min_row=2, values_only=True)]
# print(orgData)
# 清洗取值为None的列
for row_item in orgData:
    while None in row_item:
        row_item.remove(None)

# 绘制雷达图需求
# 1. 设置主题为"chalk"；
# 2. 标题设置为"Amy专业手机评测"；
# 3. 将图例列表布局设置为纵向，图例与最左侧容器的相对距离设置为10%，与底部的相对距离设置为50%
# 4. 雷达图为圆形
# 5. 雷达图坐标围起来的一圈（分隔区域配置项）透明度为1
# 6. 坐标轴各个部分的名称为['外观', '性能', '拍照', '系统', '屏幕']，满分均为10分
# 7. 对于各种手机的取值设置：均隐藏数据标签，围起来的区域填充透明度为0.1
# 图例系列名“华为”，颜色#800080
# 图例系列名“OPPO”，颜色#6495ed
# 图例系列名“苹果”，颜色#696969
# 图例系列名“小米“，颜色#3cb371
# 图例系列名“三星”，颜色#ff8c00
# 8. 保存图片
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "phone_display_radar.html"

# 准备坐标轴
c_schema = [
    opts.RadarIndicatorItem(name="外观", max_=10),
    opts.RadarIndicatorItem(name="性能", max_=10),
    opts.RadarIndicatorItem(name="拍照", max_=10),
    opts.RadarIndicatorItem(name="系统", max_=10),
    opts.RadarIndicatorItem(name="屏幕", max_=10)
]
# 执行绘图
radar = (
    Radar(init_opts=opts.InitOpts(theme="chalk"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Amy专业手机评测"),
        legend_opts=opts.LegendOpts(
            orient="vertical",
            pos_left="10%",
            pos_bottom="50%"
        )
    )
    .add_schema(
        schema=c_schema,
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        shape="circle"
    )
    .add(
        data=[orgData[0][1:6]],
        series_name=orgData[0][0],
        color="#800080",
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .add(
        data=[orgData[1][1:6]],
        series_name=orgData[1][0],
        color="#6495ed",
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .add(
        data=[orgData[2][1:6]],
        series_name=orgData[2][0],
        color="#696969",
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .add(
        data=[orgData[3][1:6]],
        series_name=orgData[3][0],
        color="#3cb371",
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .add(
        data=[orgData[4][1:6]],
        series_name=orgData[4][0],
        color="#ff8c00",
        label_opts=opts.LabelOpts(is_show=False),
        areastyle_opts=opts.AreaStyleOpts(opacity=0.1)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
