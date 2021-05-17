import os
from pyecharts.charts import Sankey
import pyecharts.options as opts
import openpyxl
from openpyxl.workbook.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

# 使用桑基图，直观描述一个人的年度歌单下不同类目的歌曲的数量构成


# 配置信息

# 资源文件夹
resourcesPath = "./resources"
# 歌单数据文件
songListBookName = "song.xlsx"
# 歌单工作表名
songListSheetName = "年度歌单"
# 打开歌单数据表
songListSheet = openpyxl.load_workbook(
    filename=os.path.join(resourcesPath, songListBookName)
)[songListSheetName]  # type: Worksheet


# 按照格式生成桑基图的节点数据字典
def sankey_node(node_name: str) -> dict:
    """
    绘制桑基图节点的固定格式{"name": node_name}

    :param node_name: 节点名称

    :return: 绘制桑基图固定节点格式{"name": node_name}
    """
    return {"name": node_name}


# 按照格式生成桑基图的信息流数据字典
def sankey_link(source_name: str, target_name: str, val: float) -> dict:
    """

    绘制桑基图节点的固定格式{"source": src_name, "target": target_name, "value": val}

    :param source_name: 信息流源节点的名称

    :param target_name: 信息流目标节点的名称

    :param val: 信息流权重（多少数据在这个信息流上）

    :return: {"source": src_name, "target": target_name, "value": val}
    """
    return {"source": source_name, "target": target_name, "value": val}


# 准备原始数据：先把表格内容都读进来
orgData = [row_item for row_item in songListSheet.iter_rows(min_row=2, values_only=True)]
# print(orgData)
# 准备绘图用数据：节点列表和信息流列表
nodes = []
links = []


# 扫描各行，添加节点原始数据
for songItem in orgData:
    nodes.extend(list(songItem[:-1]))
# 节点去重
nodes = list(set(nodes))
# 修饰每个节点数据，改造成符合sankey绘图格式的字典格式
for songIndex, songTypeItem in enumerate(nodes):
    nodes[songIndex] = sankey_node(node_name=songTypeItem)


# 根据原始数据生成信息流，添加至列表
for songType in orgData:
    # 把取值拎出来
    val = songType[-1]
    # 一共有多少个分级类目
    levelCount = len(songType[0:-1])
    # 考虑多个分级的通用情况
    for level in range(levelCount-1):
        # 当前分级和下一分级之间存在一个信息流
        links.append(
            sankey_link(
                source_name=songType[level],
                target_name=songType[level + 1],
                val=val)
        )

# print(nodes)
# print(links)


# 绘制桑基图的需求
# 1. 主题为dark
# 2. 背景色为#253441
# 3. 标题为“年度歌单”
# 4. 隐藏图例
# 5. 美化图片：信息流的透明度为30%，弯曲度50%，颜色与源节点统一一致（有一个特殊值，查官方文档说了）
# 6. 数据标签字体10，放节点右侧，颜色为白色#FFFFFF
# 7. 保存图片
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "songList_sankey.html"
# 执行绘图
sankey = (
    Sankey(
        init_opts=opts.InitOpts(
            theme="dark",
            bg_color="#253441"
        )
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="年度歌单"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .add(
        series_name="",
        nodes=nodes,
        links=links,
        linestyle_opt=opts.LineStyleOpts(
            opacity=0.3,
            curve=0.5,
            color="source"
        ),
        label_opts=opts.LabelOpts(
            font_size=10,
            position="right",
            color="#FFFFFF"
        )
    )
)
# 执行保存
sankey.render(path=os.path.join(resultPath, resultFileName))
