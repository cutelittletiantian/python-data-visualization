import os
from pyecharts import options as opts
from pyecharts.charts import Radar

# 准备用于绘制雷达图的数据，省略从文件中读取的部分
# 六个数据维度的数据是[传球, 射门, 体力, 防守, 速度, 盘带]
# C·罗纳尔多的数据，并赋值给cl
cl = [[83, 92, 87, 49, 89, 86]]
# 梅西的数据，并赋值给mx
mx = [[88, 95, 66, 43, 86, 96]]
# 苏亚雷斯的数据
sy = [[80, 92, 87, 58, 78, 81]]
# 莱万多夫斯基的数据
lw = [[79, 92, 84, 53, 81, 87]]
# 列兹曼的数据
gl = [[84, 87, 70, 54, 86, 89]]

# 雷达图绘图需求
# 1. 设置雷达的坐标系
# 2. 雷达图的背景色为#dcdcdc
# 3. 雷达图的宽、高分别为1000px和600px
# 4. 雷达图的标题为"球员表现"
# 5. 数据标签全部隐藏
# 6. 雷达图围起来的区域要体现出颜色，透明度设置为1
# 7. 取值：
# 第一个球员的数据为：图例系列名称"C·罗纳尔多"，数据值cl，颜色为#6495ed，并将数据标签隐藏
# 第二个球员的数据为：图例系列名称"梅西"，数据值mx，颜色为#ff8c00，并将数据标签隐藏
# 第三个球员的数据为：图例系列名称"苏亚雷斯"，数据值sy，颜色为#00ff00，并将数据标签隐藏
# 第四个球员的数据为：图例系列名称"莱万多夫斯基"，数据值lw，颜色为#a0522d，并将数据标签隐藏
# 第五个球员的数据为：图例系列名称"格列兹曼"，数据值gl，颜色为#da70d6，并将数据标签隐藏
# 8. 保存图片
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "player_radar.html"

# 设置雷达图的坐标系
c_schema = [
    # 设置坐标轴名称"传球"和最大值100
    opts.RadarIndicatorItem(name="传球", max_=100),
    # 设置坐标轴名称"射门"和最大值100
    opts.RadarIndicatorItem(name="射门", max_=100),
    # 设置坐标轴名称"体力"和最大值100
    opts.RadarIndicatorItem(name="体力", max_=100),
    # 设置坐标轴名称"防守"和最大值100
    opts.RadarIndicatorItem(name="防守", max_=100),
    # 设置坐标轴名称"速度"和最大值100
    opts.RadarIndicatorItem(name="速度", max_=100),
    # 设置坐标轴名称"盘带"和最大值100
    opts.RadarIndicatorItem(name="盘带", max_=100)
]

# 执行绘图
radar = (
    Radar(
        init_opts=opts.InitOpts(
            bg_color="#dcdcdc",
            width="1000px",
            height="600px"
        )
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="球员表现"))
    .add_schema(
        schema=c_schema,
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True,
            areastyle_opts=opts.AreaStyleOpts(opacity=1)
        )
    )
    .add(
        series_name="C·罗纳尔多",
        data=cl,
        color="#6495ed",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        series_name="梅西",
        data=mx,
        color="#ff8c00",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        series_name="苏亚雷斯",
        data=sy,
        color="#00ff00",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        series_name="莱万多夫斯基",
        data=lw,
        color="#a0522d",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .add(
        series_name="格列兹曼",
        data=gl,
        color="#da70d6",
        label_opts=opts.LabelOpts(is_show=False)
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
