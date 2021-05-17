import os
from pyecharts.charts import Sankey
import pyecharts.options as opts
from pyecharts.globals import ThemeType

# 桑基图直观表达宠物店商品的购买路径

# 准备绘制桑基图需要的数据（节点、数据流），省略从文件中取出数据的过程
# 创建节点列表

nodes = [
    {"name": "狗粮"},
    {"name": "玩具"},
    {"name": "1-小规格狗粮"},
    {"name": "1-大规格狗粮"},
    {"name": "1-磨牙棒"},
    {"name": "2-未购买"},
    {"name": "2-小规格狗粮"},
    {"name": "2-大规格狗粮"},
    {"name": "2-磨牙棒"},
]
# 创建信息流列表
links = [
    {"source": "狗粮", "target": "1-小规格狗粮", "value": 613},
    {"source": "狗粮", "target": "1-大规格狗粮", "value": 1018},
    {"source": "玩具", "target": "1-磨牙棒", "value": 197},
    {"source": "1-小规格狗粮", "target": "2-未购买", "value": 654},
    {"source": "1-小规格狗粮", "target": "2-磨牙棒", "value": 21},
    {"source": "1-小规格狗粮", "target": "2-小规格狗粮", "value": 231},
    {"source": "1-小规格狗粮", "target": "2-大规格狗粮", "value": 112},
    {"source": "1-大规格狗粮", "target": "2-未购买", "value": 375},
    {"source": "1-大规格狗粮", "target": "2-磨牙棒", "value": 23},
    {"source": "1-大规格狗粮", "target": "2-小规格狗粮", "value": 18},
    {"source": "1-大规格狗粮", "target": "2-大规格狗粮", "value": 197},
    {"source": "1-磨牙棒", "target": "2-未购买", "value": 157},
    {"source": "1-磨牙棒", "target": "2-磨牙棒", "value": 3},
    {"source": "1-磨牙棒", "target": "2-小规格狗粮", "value": 24},
    {"source": "1-磨牙棒", "target": "2-大规格狗粮", "value": 13},
]

# 绘制桑基图的需求
# 1. 主题设为essos风格
# 2. 标题为“购买路径”
# 3. 图例隐藏
# 4. 信息流设为垂直方向（参考下官方文档里的参数设置）
# 5. 标签在节点上方，颜色为黑色
# 6. 美化图片：信息流透明度为0.3，弯曲度为0.5，颜色与目标节点颜色一致
# 7. 保存图片
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "pet_sales_sankey.html"
# 执行绘图
sankey = (
    Sankey(init_opts=opts.InitOpts(theme=ThemeType.ESSOS))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="购买路径"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        orient="vertical",
        linestyle_opt=opts.LineStyleOpts(
            opacity=0.3,
            curve=0.5,
            color="target"
        ),
        label_opts=opts.LabelOpts(
            position="top",
            color="#000000"
        )
    )
)
# 执行保存
sankey.render(path=os.path.join(resultPath, resultFileName))
