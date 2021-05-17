import os
from pyecharts.charts import Sankey
import pyecharts.options as opts

# 在example13_2基础上再进一步，使用桑基图直观表达创意馆产品不同分类的产品销售情况

# 准备原始数据（节点、信息流），省略从表格中读进数据的步骤
# 数据节点列表
nodes = [
    {"name": "机器人"},
    {"name": "猛击赛车"},
    {"name": "莱肯赛车"},
    {"name": "遥控机器人"},
    {"name": "遥控猛击赛车"},
    {"name": "遥控莱肯赛车"},
    {"name": "非遥控机器人"},
    {"name": "非遥控猛击赛车"},
    {"name": "非遥控莱肯赛车"},
    {"name": "未购买"},
    {"name": "购买"}
]
# 信息流列表
links = [
    {"source": "机器人", "target": "遥控机器人", "value": 12},
    {"source": "机器人", "target": "非遥控机器人", "value": 32},
    {"source": "猛击赛车", "target": "遥控猛击赛车", "value": 23},
    {"source": "猛击赛车", "target": "非遥控猛击赛车", "value": 11},
    {"source": "莱肯赛车", "target": "遥控莱肯赛车", "value": 45},
    {"source": "莱肯赛车", "target": "非遥控莱肯赛车", "value": 12},
    {"source": "遥控机器人", "target": "未购买", "value": 12},
    {"source": "遥控猛击赛车", "target": "购买", "value": 23},
    {"source": "遥控莱肯赛车", "target": "未购买", "value": 45},
    {"source": "非遥控机器人", "target": "购买", "value": 32},
    {"source": "非遥控猛击赛车", "target": "未购买", "value": 11},
    {"source": "非遥控莱肯赛车", "target": "购买", "value": 12}
]

# 绘制桑基图需求
# 1. 数据系列名称设置为空
# 2. 数据标签放在节点右边
# 3. 图表标题为“馆内产品售卖”
# 4. 保存
# 5. 图可能会很丑，美化的事情后面再操心
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "product_sales_sankey.html"
sankey = (
    Sankey()
    .set_global_opts(title_opts=opts.TitleOpts(title="馆内产品售卖"))
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        label_opts=opts.LabelOpts(position="right"),
        linestyle_opt=opts.LineStyleOpts(color="#FFF0F5")
    )
)
# 执行保存
sankey.render(path=os.path.join(resultPath, resultFileName))
