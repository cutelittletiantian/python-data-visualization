import os
import openpyxl
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.workbook.workbook import Workbook
import pyecharts.options as opts
from pyecharts.charts import Geo, Line, Bar, Page
from pyecharts.globals import ThemeType, GeoType
from pyecharts.commons.utils import JsCode

# 多图展示某越野爱好这在四川一些地区的越野游戏路线图

# 资源文件目录
resourcesPath = "./resources"
# 越野路线表文件
hikingBookName = "hiking1.xlsx"
# 越野路线（起点在成都的部分）工作表名
hikingSheetName = "hiking2020"

# 打开文件，选表
hikingBook = openpyxl.load_workbook(os.path.join(resourcesPath, hikingBookName))  # type: Workbook
# 使用中括号读取工作表"hiking2020"，并赋值给sheet
hikingSheet = hikingBook["hiking2020"]  # type: Worksheet

# 取出表中原始数据
# 列含义：[项目编号，马拉松项目名，起跑时间，公里数（相对起点），终点，起点，项目日期]
orgData = [list(rowItem) for rowItem in hikingSheet.iter_rows(values_only=True)]
# print(orgData)

# 取出带权节点数据：格式[(终点，公里数（相对起点）), ...]
distanceList = [(rowItem[4], rowItem[3]) for rowItem in orgData]
# print(distanceList)
# 取出路线边数据：格式[(起点-也就是成都啦，终点), ...]
routeList = [(rowItem[5], rowItem[4]) for rowItem in orgData]
# print(routeList)

# ——————————————————————————
# 绘制马拉松路线轨迹图（地理坐标图）的需求
# 1. 地理坐标类型为"四川"；
# 2. 地图坐标底色设置为"#2d3948"，描边颜色设置为"#58667a"；
# 3. 高亮状态下颜色设置为"#2a333d"；
# 4. 边数据对的图例系列名为空，设置为流向型，隐藏数据标签，设置渐变色，透明度0.1，宽度为1，弯曲度为0.1，隐藏数据标签
# 定义渐变色（需要使用的js脚本已给，具体含义可见pyecharts文档）
# 5. 带权节点以散点方式呈现，颜色为白色，图例系列名为空，数据标签格式为节点名称
# 6. 主题为"white"
# 7. 标题“2020越野足迹”
# 渐变色js脚本
line_color_js = """
new echarts.graphic.LinearGradient(
    0, 0, 0, 1,
    [{offset: 0, color: '#4682B4'}, {offset: 1, color: '#00BFFF'}])
"""
# 执行绘图
geo = (
    Geo(init_opts=opts.InitOpts(theme=ThemeType.WHITE))
    .set_global_opts(opts.TitleOpts(title="2020越野足迹"))
    .add_schema(
        maptype="四川",
        itemstyle_opts=opts.ItemStyleOpts(color="#2d3948", border_color="#58667a"),
        emphasis_itemstyle_opts=opts.ItemStyleOpts(color="#2a333d")
    )
    # 库内没有的地点经纬度信息（经纬度可以查到）要另行添加，否则会出错
    .add_coordinate(name="九顶山", longitude=103.8533363098652, latitude=31.543769959316908)
    .add_coordinate(name="四姑娘山", longitude=102.90171147915451, latitude=31.11110962351124)
    .add_coordinate(name="鹧鸪山", longitude=102.67091357156394, latitude=31.905444331066434)
    .add(
        series_name="",
        data_pair=routeList,
        type_=GeoType.LINES,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(
            opacity=0.1,
            width=1,
            curve=0.1,
            color=JsCode(line_color_js)
        )
    )
    .add(
        series_name="",
        data_pair=distanceList,
        type_=GeoType.SCATTER,
        color="white",
        label_opts=opts.LabelOpts(formatter="{b}")
    )
)

# ——————————————————————————
# 绘制爬升情况柱状图需求：
# 1. 粉笔主题
# 2. 图例系列名称空着
# 3. 数值标签放在柱子内部中线右侧
# 4. 柱子设置渐变色
# 5. 设置标题：2020越野比赛累计爬升情况；副标题：数据截止日期：2020年12月
# 6. 隐藏图例
# 7. 躺着摆放柱子

# 爬升地点的名称
race = ["九顶山", "云间花径", "孟屯河谷", "山地马拉松", "UTMB", "HAKKA"]
# 爬升高度对应数据
climb = [2464, 1206, 2215, 1022, 3300, 2243]

# 执行绘图
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="2020越野比赛累计爬升情况",
            subtitle="数据截止日期：2020年12月"
        ),
        legend_opts=opts.LegendOpts(is_show=True)
    )
    .add_xaxis(xaxis_data=race)
    .add_yaxis(
        series_name="",
        y_axis=climb
    )
    .set_series_opts(
        itemstyle_opts=opts.ItemStyleOpts(
            color=JsCode(
                """new echarts.graphic.LinearGradient(
                    1, 0, 0, 0,
                    [
                        {offset: 0, color: 'rgb(0,139,139)'},
                        {offset: 1, color: 'rgb(32,178,170)'}
                    ])"""
            )
        ),
        label_opts=opts.LabelOpts(
            is_show=True,
            position='insideRight',
            font_style='italic'
        )
    )
    .reversal_axis()
)

# ——————————————————————————
# 绘制距离与配速折线图需求：
# 1. 第一组y轴数据
# 图例系列名为"平均配速"，设置颜色为渐变色（已给定）
# 2. 第二组y轴数据
# 图例系列名为"距离"，设置颜色为渐变色（已给定）
# 3. 标签字体为斜体，宽度为15
# 4. 设置折线图标题为"2020越野比赛距离与配速情况"，副标题"数据截止日期：2020年12月"，将x坐标轴标签旋转20度，并显示图例
# 5. 粉笔主题

# 马拉松赛项目名
race = ["九顶山越野挑战赛", "四姑娘山云间花径", "梦之热土孟屯河谷", "川西红叶山地马拉松", "功夫熊猫UTMB", "HAKKA"]
# 公里数数据（一组y轴）
distance = [35, 30, 33, 35, 50, 50]
# 配速数据（另一y轴）
rapid = [15.17, 19.7, 15.27, 10.14, 12.32, 7.48]

# 执行绘图
line = (
    Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="2020越野比赛距离与配速情况",
            subtitle="数据截止日期：2020年12月"
        ),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=20)),
        legend_opts=opts.LegendOpts(is_show=True)
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(
            is_show=True,
            font_style='italic'
        ),
        itemstyle_opts=opts.ItemStyleOpts(border_width=15)
    )
    .add_xaxis(xaxis_data=race)
    .add_yaxis(
        series_name="平均配速",
        y_axis=rapid,
        color=JsCode(
            """new echarts.graphic.LinearGradient(
                1, 0, 0, 0,
                [{offset: 0,color: 'rgb(127,255,0)'},
                {offset: 1,color: 'rgb(0,255,255)'}])"""
        )
    )
    .add_yaxis(
        series_name="距离",
        y_axis=distance,
        color=JsCode(
            """new echarts.graphic.LinearGradient(
                1, 0, 0, 0,
                [{offset: 0,color: 'rgb(70,130,180)'},
                {offset: 1,color: 'rgb(0,255,255)'}])"""
        )
    )
)


# 将前面的地理坐标图、柱状图和折线图全部添加到一页中，需求：
# 1. 设置为可拖拽子图的布局
# 2. 保存页面组合图
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "hikingfan_multigraph_page.html"
# 执行作图
page = (
    Page(layout=Page.DraggablePageLayout)
    .add(geo, bar1, line)
    .render(path=os.path.join(resultPath, resultFileName))
)
