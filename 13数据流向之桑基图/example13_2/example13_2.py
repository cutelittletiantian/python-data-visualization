import os
from pyecharts.charts import Sankey
import pyecharts.options as opts

# 使用桑基图直观表达创意馆产品不同类型产品的数量

# 准备原始数据（节点、信息流），暂时略去从表中读取出数据的过程
# 节点列表
nodes = [
    {"name": "遥控"},
    {"name": "非遥控"},
    {"name": "机器人"},
    {"name": "猛击赛车"},
    {"name": "莱肯赛车"}
]
# 信息流列表
links = [
    {"source": "遥控", "target": "机器人", "value": 15},
    {"source": "遥控", "target": "猛击赛车", "value": 23},
    {"source": "遥控", "target": "莱肯赛车", "value": 36},
    {"source": "非遥控", "target": "机器人", "value": 48},
    {"source": "非遥控", "target": "猛击赛车", "value": 21},
    {"source": "非遥控", "target": "莱肯赛车", "value": 11}
]

# 绘制桑基图要求
# 1. 数据系列名称为空
# 2. 添加数据标签放在节点右边；
# 3. 全图标题"馆内产品分类"；
# 4. 保存图片
# 5. 图片很丑，后面再操心怎么优化
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "product_category_sankey.html"
# 执行绘图
sankey = (
    Sankey()
    .set_global_opts(title_opts=opts.TitleOpts(title="馆内产品分类"))
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        label_opts=opts.LabelOpts(position="right")
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
