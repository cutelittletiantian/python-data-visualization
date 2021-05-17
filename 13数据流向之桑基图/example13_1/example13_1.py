import os
from pyecharts.charts import Sankey
import pyecharts.options as opts

# 用桑基图表达月度开支的钱的各种去向

# 准备桑基图的原始数据（节点、信息流），跳过从excel中读取数据的过程
# 节点列表：格式[{"name": 标签名1}, {“name”: 标签名2}, ...]
nodes = [
    {"name": "围巾"},
    {"name": "长辈"},
    {"name": "网络费"},
    {"name": "服装"},
    {"name": "公交"},
    {"name": "同学"},
    {"name": "袜子"},
    {"name": "总费用"},
    {"name": "衣服"},
    {"name": "红包"},
    {"name": "交通"},
    {"name": "聚餐"},
    {"name": "滴滴"},
    {"name": "餐饮"},
    {"name": "管理费"},
    {"name": "水电"},
    {"name": "共享单车"},
    {"name": "外卖"},
    {"name": "房租"},
    {"name": "住宿"},
    {"name": "饮料"},
    {"name": "鞋子"},
    {"name": "地铁"}
]
# 信息流列表：格式
# [{"source": 标签名1, "target": 标签名1, "value": 取值1},
# {"source": 标签名2, "target": 标签名2, "value": 取值2},
# ......]
links = [
    {"source": "总费用", "target": "住宿", "value": 2580},
    {"source": "总费用", "target": "餐饮", "value": 1300},
    {"source": "总费用", "target": "交通", "value": 500},
    {"source": "总费用", "target": "服装", "value": 900},
    {"source": "总费用", "target": "红包","value": 1300},
    {"source": "住宿", "target": "房租", "value": 2000},
    {"source": "住宿", "target": "水电", "value": 400},
    {"source": "住宿", "target": "管理费", "value": 100},
    {"source": "住宿", "target": "网络费", "value": 80},
    {"source": "餐饮", "target": "外卖", "value": 800},
    {"source": "餐饮", "target": "聚餐", "value": 300},
    {"source": "餐饮", "target": "饮料", "value": 200},
    {"source": "交通", "target": "滴滴", "value": 220},
    {"source": "交通", "target": "地铁", "value": 150},
    {"source": "交通", "target": "公交", "value": 80},
    {"source": "交通", "target": "共享单车", "value": 50},
    {"source": "服装", "target": "衣服", "value": 400},
    {"source": "服装", "target": "鞋子", "value": 300},
    {"source": "服装", "target": "围巾", "value": 150},
    {"source": "服装", "target": "袜子", "value": 50},
    {"source": "红包", "target": "同学", "value": 800},
    {"source": "红包", "target": "长辈", "value": 500}
]

# 桑基图绘图的需求：
# 1. 根据开支明细，按照节点和信息流列表结构，直接创建数据的节点和信息流列表；
# 2. 绘制桑基图，系列名称为"月度开支"
# 3. 数据标签统一放在节点右边
# 4. 保存图片
# 5. 这个图绘制出来肯定特别丑，所以后面还会改进
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "purchase_sankey.html"
# 执行绘图
sankey = (
    Sankey()
    .add(
        series_name="月度开支",
        nodes=nodes,
        links=links,
        label_opts=opts.LabelOpts(position="right")
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
