import os
from pyecharts.charts import Pie, Bar, HeatMap, Bar, Map, Radar, Graph, Page
from pyecharts.globals import ThemeType
import pyecharts.options as opts

# 综合利用可视化大屏，展示广州餐饮业有关数据

# 配置数据：保存文件的路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)

# 原数据读取需要专门的模块负责，这里读取过程全部省略，直接上整理好的数据

# ————————————————————————————————————————————
# 饼状图数据对dataPie
dataPairPie = [("天河区", 164), ("越秀区", 69), ("海珠区", 68), ("荔湾区", 27),
               ("番禺区", 23), ("白云区", 20), ("黄埔区", 1)]


def pie(data_pair) -> Pie:
    """绘制【当地各大行政区美食商铺商圈个数占比情况】的饼状图部分需求：

    2.1 设置主题"purple-passion"；

    2.2 图例系列名称设置为空，每一块饼的标签格式为"数据项: 数值"；

    2.3 全局配置项的标题配置项传入标题"行政区美食占比"；

    2.4 return返回c；

    :param data_pair: 用于绘制图像的数据对

    :return: 绘制好的饼状图对象
    """
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(opts.TitleOpts(title="行政区美食占比"))
        .add(
            series_name="",
            data_pair=data_pair,
            label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    )
    return c


# ————————————————————————————————————————————
# 玫瑰图数据dataPairRosePie
dataPairRosePie = [("四星商户", 175), ("准五星商户", 156), ("五星商户", 34), ("准四星商户", 7)]


def pie_circle(data_pair) -> Pie:
    """绘制【当地不同星级的美食商圈个数占比情况】的环状南丁格尔玫瑰图的需求

    4.1 设置主题为"purple-passion"；

    4.2 图例系列名称设置为空，环状内径圆相对半径为40%，最大玫瑰花瓣相对外径为55%；

    4.3 大小通过半径体现，花瓣圆心角都相同

    4.4 标题为"星级占比"；

    4.5 return返回c；

    :param data_pair: 用于绘制环状南丁格尔

    :return: 绘制好的南丁格尔玫瑰图对象
    """
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(title_opts=opts.TitleOpts(title="星级占比"))
        .add(
            series_name="",
            data_pair=data_pair,
            rosetype="area",
            radius=["40%", "55%"]
        )
    )
    return c


# ————————————————————————————————————————————
# 柱状图数据x1,y1
x1Bar = ["珠江新城", "天河城/体育中心", "北京路", "江南西", "天河北", "机场路",
         "江南大道", "高德置地/花城汇", "石牌/龙口", "兴盛路/跑马场"]
y1Bar = [60, 42, 34, 23, 22, 10, 10, 10, 10, 10]


def bar(x_data, y_data) -> Bar:
    """绘制【比较当地不同地区的美食商圈分布个数情况】的柱状图的需求

    3.1 设置主题"purple-passion"；

    3.2 图例系列名称为空；

    3.3 标题设为"商圈分布"；

    3.4 防止x轴字遮挡：x轴坐标轴标签顺时针转15度；

    3.5 return返回c

    :param x_data: 当地不同地区的名称

    :param y_data: 对应美食商圈的数量

    :return: 绘制好的柱状图对象
    """
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="商圈分布"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15))
        )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data
        )
    )
    return c


# ————————————————————————————————————————————
# 热力图x轴,y轴标签数据
xHeatMap = ["评论数", "人均价格", "口味评分", "环境评分", "服务评分"]
yHeatMap = ["评论数", "人均价格", "口味评分", "环境评分", "服务评分"]
# 热力图数据value
valueHeatMap = [[0, 0, 1.00], [0, 1, 0.04], [0, 2, -0.07], [0, 3, -0.05], [0, 4, -0.28],
                [1, 0, 0.04], [1, 1, 1.00], [1, 2, 0.13], [1, 3, 0.40], [1, 4, 0.33],
                [2, 0, -0.07], [2, 1, 0.13], [2, 2, 1.00], [2, 3, 0.25], [2, 4, 0.52],
                [3, 0, -0.05], [3, 1, 0.40], [3, 2, 0.25], [3, 3, 1.00], [3, 4, 0.68],
                [4, 0, -0.28], [4, 1, 0.33], [4, 2, 0.52], [4, 3, 0.68], [4, 4, 1.00]]


def heat_corr(x_data, y_data, val_list):
    """绘制【描述"评论数", "人均价格", "口味评分", "环境评分", "服务评分"这些指标之间相关程度】的热力图

    6.1 设置主题"purple-passion"；

    6.2 图例系列名为空，数值标签位居色块中央；

    6.3 标题"价格口碑等相关性"

    6.4 隐藏视觉映射配置项传入参数，但仍指定最小和最大映射值min_=-1, max_=1；

    6.5 return返回c；

    :param x_data: "评论数", "人均价格", "口味评分", "环境评分", "服务评分"指标

    :param y_data: 也是"评论数", "人均价格", "口味评分", "环境评分", "服务评分"指标

    :param val_list: 热力矩阵各个色块的取值

    :return: 绘制好的热力图对象
    """
    c = (
        HeatMap(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="价格口碑等相关性"),
            visualmap_opts=opts.VisualMapOpts(is_show=False, min_=-1, max_=1)
        )
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            yaxis_data=y_data,
            value=val_list,
            label_opts=opts.LabelOpts(position="inside")
        )
    )
    return c


# ————————————————————————————————————————————
# 条形图数据x2BarHorizon, y2BarHorizon
x2BarReverse = ["江浙菜", "茶餐馆", "小龙虾", "海鲜", "素菜", "湘菜", "韩式料理", "创意菜", "韩国料理", "茶餐厅", "川菜",
                "东南亚菜", "咖啡厅", "烧烤", "自助餐", "面包甜点", "火锅", "日本料理", "粤菜", "西餐"]
y2BarReverse = [3, 3, 4, 4, 5, 6, 6, 7, 9, 9, 11, 11, 14, 18, 20, 21, 43, 52, 53, 61]


def bar_reverse(x_data, y_data) -> Bar:
    """
    绘制【比较当地美食不同种类商铺数量情况】的条形图（横过来的柱状图）需求

    5.1 设置主题"purple-passion"；

    5.2 图例系列名为空；

    5.3 数据标签放在柱子右边；

    5.4 标题设置为"美食种类分布"；

    5.5 return返回c；

    :param x_data: 菜肴种别的名称

    :param y_data: 相应菜肴商铺的个数

    :return: 绘制完成的条形图（横向柱状图）对象
    """
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(title_opts=opts.TitleOpts("美食种类分布"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            label_opts=opts.LabelOpts(position="right")
        )
        .reversal_axis()
    )
    return c


# ————————————————————————————————————————————
# 地图数据dataPairRadar
dataPairMap = [("天河区", 164), ("越秀区", 69), ("海珠区", 68), ("荔湾区", 27),
                 ("番禺区", 23), ("白云区", 20), ("黄埔区", 1)]


def map_chart(data_pair):
    """
    绘制【描述广州美食分布】的地图需求：

    7.1 设置主题"purple-passion"；

    7.2 图例系列名称设置为空，地图类型设置为“广州”（怎样找对应类型值可以结合官方文档提示进行查找）；

    7.3 标题设为"广州美食分布"

    7.4 配置视觉映射配置项；

    7.5 return返回c；

    :param data_pair: (地区, 该地区美食商铺个数)组成的数据对列表

    :return: 绘制好的地图对象c
    """
    c = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="广州美食分布"),
            visualmap_opts=opts.VisualMapOpts(is_show=True)
        )
        .add(
            series_name="",
            maptype="广州",
            data_pair=data_pair,
        )
    )
    return c


# ————————————————————————————————————————————
# 雷达图数据
# 各项指标分别为：["菜价菜量", "口味", "环境", "服务", "交通"]
sx = [[4.1, 4.2, 3.7, 4.5, 4.2]]   # 四星商户
zwx = [[4.5, 4.7, 4.2, 4.5, 4.8]]  # 准五星商户
wx = [[4.6, 4.9, 4.9, 5, 4.3]]     # 五星商户
zsx = [[4.3, 3.7, 4.1, 4.1, 4.6]]  # 准四星商户
# 构造雷达图坐标轴对象c_schema
# 坐标轴需要评估的对象分别为"菜价菜量", "口味", "环境", "服务", "交通"
# 评估按5分制来
c_schema = [
    {"name": "菜价菜量", "max": 5},
    {"name": "口味", "max": 5},
    {"name": "环境", "max": 5},
    {"name": "服务", "max": 5},
    {"name": "交通", "max": 5}]
# 构造各种星级商户绘制在雷达坐标上的数据及相应配置列表
# 图例名称"四星商户"，传入数据sx，颜色"#6495ed"，区域填充样式设置透明度为0.1，隐藏数据标签；
# 图例名称"准五星商户"，传入数据zwx，颜色"#696969"，区域填充样式设置透明度为0.1，隐藏数据标签；
# 图例名称"五星商户"，传入数据wx，颜色"#3cb371"，区域填充样式设置透明度为0.1，隐藏数据标签；
# 图例名称"准四星商户"，传入数据zsx，颜色"#ff8c00"，区域填充样式设置透明度为0.1，隐藏数据标签；
dataRadar = [
    dict(series_name="四星商户", data=sx, color="#6495ed",
         label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    dict(series_name="准五星商户", data=zwx, color="#696969",
         label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    dict(series_name="五星商户", data=wx, color="#3cb371",
         label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    dict(series_name="准四星商户", data=zsx, color="#ff8c00",
         label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    # Radar().add(series_name="四星商户", data=sx, color="#6495ed",
    #             label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    # Radar().add(series_name="准五星商户", data=zwx, color="#696969",
    #             label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    # Radar().add(series_name="五星商户", data=wx, color="#3cb371",
    #             label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
    # Radar().add(series_name="准四星商户", data=zsx, color="#ff8c00",
    #             label_opts=opts.LabelOpts(is_show=False), areastyle_opts=opts.AreaStyleOpts(opacity=0.1))
]


def radar(schema, radar_data: list[dict]) -> Radar:
    """
    绘制【不同星级商户在"菜价菜量", "口味", "环境", "服务", "交通"方面综合评估】的雷达图需求

    8.1 设置主题"purple-passion"；

    8.2 标题”星级商铺评分“

    8.3 返回c

    :param schema: 雷达图的坐标系配置项

    :param radar_data: 雷达图的数据系列配置项

    :return: 绘制的雷达图对象
    """
    c = (
        Radar(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(
            title_opts=opts.TitleOpts("星级商铺评分"),
            legend_opts=opts.LegendOpts(orient="horizontal", align="left")
        )
        .add_schema(schema=schema)
    )
    # 添加各种配置数据
    for data_item in radar_data:
        c.add(
            series_name=data_item["series_name"],
            data=data_item["data"],
            color=data_item["color"],
            label_opts=data_item["label_opts"],
            areastyle_opts=data_item["areastyle_opts"]
        )
    return c


# ————————————————————————————————————————————
# 关系图存储类别的列表categoryGraph
categoryGraph = [{"name": "四星推荐"}, {"name": "准五星推荐"}, {"name": "五星推荐"}, {"name": "准四星推荐"}]
# 关系图带权节点数据nodeListGraph（id是自定义关键字）
nodeListGraph = [{"id": "四星商户", "name": "四星商户", "category": 0, "symbolSize": 30},
                 {"id": "准五星商户", "name": "准五星商户", "category": 1, "symbolSize": 30},
                 {"id": "五星商户", "name": "五星商户", "category": 2, "symbolSize": 30},
                 {"id": "准四星商户", "name": "准四星商户", "category": 3, "symbolSize": 30},
                 {"id": "Mr Pilot飞行先生", "name": "Mr Pilot飞行先生", "category": 0, "symbolSize": 10},
                 {"id": "香草烤土豆", "name": "香草烤土豆", "category": 0, "symbolSize": 10},
                 {"id": "香伯爵自助餐厅", "name": "香伯爵自助餐厅", "category": 0, "symbolSize": 10},
                 {"id": "三文鱼刺身", "name": "三文鱼刺身", "category": 0, "symbolSize": 10},
                 {"id": "佬麻雀", "name": "佬麻雀", "category": 0, "symbolSize": 10},
                 {"id": "金沙红米肠", "name": "金沙红米肠", "category": 0, "symbolSize": 10},
                 {"id": "高卡一番日本料理", "name": "高卡一番日本料理", "category": 1, "symbolSize": 10},
                 {"id": "芝士牛舌", "name": "芝士牛舌", "category": 1, "symbolSize": 10},
                 {"id": "Cocina科奇娜·南美创意料理", "name": "Cocina科奇娜·南美创意料理", "category": 1, "symbolSize": 10},
                 {"id": "牛肉寿司", "name": "牛肉寿司", "category": 1, "symbolSize": 10},
                 {"id": "Ebony", "name": "Ebony", "category": 1, "symbolSize": 10},
                 {"id": "烟三文鱼沙拉", "name": "烟三文鱼沙拉", "category": 1, "symbolSize": 10},
                 {"id": "神隐酒场", "name": "神隐酒场", "category": 2, "symbolSize": 10},
                 {"id": "玫瑰露酒煮海螺", "name": "玫瑰露酒煮海螺", "category": 2, "symbolSize": 10},
                 {"id": "渔意如意", "name": "渔意如意", "category": 2, "symbolSize": 10},
                 {"id": "一鱼五食", "name": "一鱼五食", "category": 2, "symbolSize": 10},
                 {"id": "四海一家", "name": "四海一家", "category": 2, "symbolSize": 10},
                 {"id": "碳烧生蚝", "name": "碳烧生蚝", "category": 2, "symbolSize": 10},
                 {"id": "RIBS乐排馆", "name": "RIBS乐排馆", "category": 3, "symbolSize": 10},
                 {"id": "和牛牛腩", "name": "和牛牛腩", "category": 3, "symbolSize": 10},
                 {"id": "98农庄", "name": "98农庄", "category": 3, "symbolSize": 10},
                 {"id": "炭烧牛蛙紫苏味平锅", "name": "炭烧牛蛙紫苏味平锅", "category": 3, "symbolSize": 10},
                 {"id": "悦榕庄", "name": "悦榕庄", "category": 3, "symbolSize": 10},
                 {"id": "佛跳墙", "name": "佛跳墙", "category": 3, "symbolSize": 10}]
# 关系图边数据linkListGraph
linkListGraph = [{"source": "四星商户", "target": "Mr Pilot飞行先生"},
                 {"source": "四星商户", "target": "香伯爵自助餐厅"},
                 {"source": "四星商户", "target": "佬麻雀"},
                 {"source": "准五星商户", "target": "高卡一番日本料理"},
                 {"source": "准五星商户", "target": "Cocina科奇娜·南美创意料理"},
                 {"source": "准五星商户", "target": "Ebony"},
                 {"source": "五星商户", "target": "神隐酒场"},
                 {"source": "五星商户", "target": "渔意如意"},
                 {"source": "五星商户", "target": "四海一家"},
                 {"source": "准四星商户", "target": "RIBS乐排馆"},
                 {"source": "准四星商户", "target": "98农庄"},
                 {"source": "准四星商户", "target": "悦榕庄"},
                 {"source": "Mr Pilot飞行先生", "target": "香草烤土豆"},
                 {"source": "香伯爵自助餐厅", "target": "三文鱼刺身"},
                 {"source": "佬麻雀", "target": "金沙红米肠"},
                 {"source": "高卡一番日本料理", "target": "芝士牛舌"},
                 {"source": "Cocina科奇娜·南美创意料理", "target": "牛肉寿司"},
                 {"source": "Ebony", "target": "烟三文鱼沙拉"},
                 {"source": "神隐酒场", "target": "玫瑰露酒煮海螺"},
                 {"source": "渔意如意", "target": "一鱼五食"},
                 {"source": "四海一家", "target": "碳烧生蚝"},
                 {"source": "RIBS乐排馆", "target": "和牛牛腩"},
                 {"source": "98农庄", "target": "炭烧牛蛙紫苏味平锅"},
                 {"source": "悦榕庄", "target": "佛跳墙"}]


def graph_chart(node_list=None, link_list=None, category_list=None) -> Graph:
    """绘制【星级商铺及相应菜品推荐】的关系图需求

    9.1 设置主题"purple-passion"；

    9.2 图例系列名称设置为空，整体布局呈现圆形，标签可依照节点和线的分布旋转调整，
        边的颜色和起点节点颜色相同，弯曲度为0.3；

    9.3 图例垂直方向摆放，举例图片左侧和顶部的相对举例分别为3%和20%，设置标题为"星级推荐"；

    9.4 return返回c；

    :param node_list: 星级信息以及商铺信息的分类、带权节点

    :param link_list: 节点之间的连线情况

    :param category_list: 星级分类种别

    :return: 绘制好的关系图对象
    """
    c = (
        Graph(init_opts=opts.InitOpts(theme=ThemeType.PURPLE_PASSION))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="星级推荐"),
            legend_opts=opts.LegendOpts(
                orient="vertical",
                pos_left="3%",
                pos_top="20%"
            )
        )
        .add(
            series_name="",
            nodes=node_list,
            links=link_list,
            categories=category_list,
            layout="circular",
            is_rotate_label=True,
            linestyle_opts=opts.LineStyleOpts(
                color="source",
                curve=0.3
            )
        )
    )
    return c


# ————————————————————————————————————————————
# 绘制页面组合图：
# 10.1 页面上组合图表可拖动
# 10.2 将pie(), bar(), pie_circle(), bar_reverse(), heat_corr(), map_chart(), radar(), graph_chart()依次添加到函数中；
# 10.3 保存图片

# 测试文件夹
testPath = "./result/test"
if not os.path.exists(path=testPath):
    os.mkdir(path=testPath)
# 测试文件名
testFileName = "pagetest.html"

# 布局配置文件夹
configPath = "./result/config"
if not os.path.exists(path=configPath):
    os.mkdir(path=configPath)
# 布局配置文件名
configFileName = "page_screen_config.json"

# 最终生成好的可视化大屏文件名
resultFileName = "GuangZhou.html"
# 执行组图
page = (
    Page(layout=Page.DraggablePageLayout)
    .add(
        pie(data_pair=dataPairPie),
        bar(x_data=x1Bar, y_data=y1Bar),
        pie_circle(data_pair=dataPairRosePie),
        bar_reverse(x_data=x2BarReverse, y_data=y2BarReverse),
        heat_corr(x_data=xHeatMap, y_data=yHeatMap, val_list=valueHeatMap),
        map_chart(data_pair=dataPairMap),
        radar(schema=c_schema, radar_data=dataRadar),
        graph_chart(node_list=nodeListGraph, link_list=linkListGraph, category_list=categoryGraph)
    )
)

# 【查阅文档】明白可视化大屏组装的过程
# 第一次渲染的时候，先执行如下代码，注释掉最后的代码，即
# 只执行下面的代码：
# page.render(path=os.path.join(testPath, testFileName))
# 注释掉最后下面的这段代码：
# page.save_resize_html(
#     source=os.path.join(testPath, testFileName),
#     cfg_file=os.path.join(configPath, configFileName),
#     dest=os.path.join(resultPath, resultFileName)
# )
# 然后在第一次生成的html文件中，拖动及调整图片大小后，点击save config，保存生成的json文件

# 最后注释掉上面的第一次渲染的代码，即
# 注释掉：
# page.render(path=os.path.join(testPath, testFileName))
# 执行下面的代码，重新布局配置和渲染，即可得到最终的可视化大屏
page.save_resize_html(
    source=os.path.join(testPath, testFileName),
    cfg_file=os.path.join(configPath, configFileName),
    dest=os.path.join(resultPath, resultFileName)
)
