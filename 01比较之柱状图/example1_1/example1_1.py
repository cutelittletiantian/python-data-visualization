# 导入os库，方便后续路径的处理
import os
# 导入options 模块并简写为opts
import pyecharts.options as opts
# 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar

"""Step 0: 预备工作——必要的参数配置

提前指定好生成可视化图形的 数据来源路径 和 图形最终的保存路径
"""
# resourcesPath这次暂时没有
# 目标存储的路径（相对路径的默认工作区起点为.../examplex_x这个文件夹）
resultPath = "./result"


"""Step 1: 准备数据——网红博主的数据表

字段名：频道名称 | 粉丝数（单位：万） | 点赞数（单位：万）
note:
网红博主的数据可能是从网上爬取下来，经过清洗后存放在了excel表格或者csv表格中，最后才读进列表的
不过这里，前面的读取和清洗工作就暂时省略了，数据假如就是已经读进来且清洗了，因为我们关键是看数据可视化的思路
"""
channel_infos = [
    ("一起画笔记", 12.5, 18.2),
    ("我是课代表", 23.1, 15.2),
    ("菠萝冰和夏天", 38.5, 222.7),
    ("Jeannie花", 15.8, 71.5),
    ("Esther天", 14.1, 8.6),
    ("爱草莓的小挺", 11.4, 70.5),
    ("栀缘", 18.2, 107.7),
    ("钢琴上的音乐", 16.5, 128.3),
    ("Mu123", 22.6, 109),
    ("师008号", 32, 31.7)
]


"""Step 2: 将上述表格中的数据分列提取出来
"""
# 将10位博主的频道名称存入变量名为'name'的列表中
# name = ["一起画笔记", "我是课代表", "菠萝冰和夏天", "Jeannie花", "Esther天",
#         "爱草莓的小挺", "栀缘", "钢琴上的音乐", "Mu123", "师008号"]
name = [channel_info[0] for channel_info in channel_infos]
# 按照博主姓名的顺序，依次将博主的粉丝数量存入变量名为'fans'的列表中
# fans = [12.5, 23.1, 38.5, 15.8, 14.1, 11.4, 18.2, 16.5, 22.6, 32]
fans = [channel_info[1] for channel_info in channel_infos]
# 按照博主姓名的顺序，依次将博主的点赞收藏量存入变量名为‘likes’的列表中
# likes = [18.2, 15.2, 222.7, 71.5, 8.6, 70.5, 107.7, 128.3, 109, 31.7]
likes = [channel_info[2] for channel_info in channel_infos]


"""Step 3: 计算点赞收藏量与粉丝量的比值（赞粉比）

赞粉比数值具有较大的参考价值，它可以在一定程度上避免这样的博主：
1、低活跃度或低质量博主
2、买僵尸粉博主
3、从其它知名平台刚入驻，老粉多但新平台尚未充分运营的博主
"""
# 定义一个空列表ratioList，存储点赞收藏量与粉丝量的比值
ratioList = []
# 统计点赞收藏量列表长度，并赋值给length
length = len(channel_infos)
# 将点赞收藏量列表中的值除以对应粉丝量列表中的值，并使用round()函数取近似值并保留2位小数,存储到ratioList列表中
for i in range(length):
    ratio = round(likes[i] / fans[i], 2)
    ratioList.append(ratio)


"""Step 4: 使用上述数据，绘制柱状图并保存

指定x轴数据列表 -> 指定y轴数据列表及其图例 -> 指定保存路径和文件名（.html格式）执行保存
注意：
x轴和y轴的数据长度应该一致，从而一一对应生成图像
添加y轴的同时，一定要指定该数据的图例（series_name），否则运行会不予通过
"""
# 创建一个柱状图Bar对象并赋值给变量bar
bar = Bar()
# 给柱状图添加x轴数据，数据内容是博主姓名列表：name
bar.add_xaxis(xaxis_data=name)
# 给柱状图添加y轴数据，数据内容是赞粉比列表：ratioList，指定该数据的图例为”赞粉比“
bar.add_yaxis(y_axis=ratioList, series_name="赞粉比")
# 绘制出这条柱状图，并保存到路径"./result/fans_likes.html"
resultFileName = "fans_likes.html"
bar.render(path=os.path.join(resultPath, resultFileName))
