import os
from pyecharts.charts import Sankey
import pyecharts.options as opts

# 使用三维桑基图（性别-熬夜原因-人数）直观描述当代青年人熬夜的原因分布情况

# 准备原始数据（节点、信息流），从表中取数据的过程略去
# 节点
nodes = [
    {"name": "男"},
    {"name": "女"},
    {"name": "打游戏"},
    {"name": "加班"},
    {"name": "看剧"}
]
# 信息流
links = [
    {"source": "男", "target": "打游戏", "value": 79},
    {"source": "男", "target": "加班", "value": 13},
    {"source": "男", "target": "看剧", "value": 24},
    {"source": "女", "target": "打游戏", "value": 16},
    {"source": "女", "target": "加班", "value": 5},
    {"source": "女", "target": "看剧", "value": 63}
]

# 绘制桑基图需求
# 1. 主题为light
# 2. 标题为“当代青年熬夜原因”
# 3. 隐藏图例
# 4. 美化图片：信息流透明度为20%，弯曲度50%，颜色取目标节点的颜色（这种特殊值怎么取，查官方文档）
# 5. 标签放在节点右侧，颜色设置为黑色
# 6. 保存图片
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "stayup_reason_sankey.html"
# 执行绘图
sankey = (
    Sankey(init_opts=opts.InitOpts(theme="light"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="当代青年熬夜原因"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(
            opacity=0.2,
            curve=0.5,
            color="target"  # 取目标节点的颜色
        ),
        label_opts=opts.LabelOpts(
            color="rgb(0, 0, 0)",  # 或者写成#000000
            position="right"
        )
    )
)
# 执行保存
sankey.render(path=os.path.join(resultPath, resultFileName))
