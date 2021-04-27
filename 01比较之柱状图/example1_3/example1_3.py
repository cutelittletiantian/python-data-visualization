# 导入os库，方便后续路径的处理
import os
# 导入options 模块并简写为opts
import pyecharts.options as opts
# 从pyecharts.charts中 导入 Bar模块
from pyecharts.charts import Bar

"""Step 0: 预备工作——必要的参数配置
"""
# 目标存储的路径
resultPath = "./result"


"""Step 1: 准备数据——网红博主的数据表
字段名：频道名称 | 粉丝数（单位：万） | 点赞数（单位：万）
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


"""Step 3: 使用上述数据，绘制柱状图并保存

注意：
1、这一次记得设置全局配置，设置标题并调整x轴显示不完全的问题
2、这次绘制的是多y轴柱状图（y轴有点赞量和粉丝数2项合到一张图）
3、本案例中采用pyecharts官方文档中常用的一句话到底的写法
"""
# # 创建一个柱状图Bar对象并赋值给变量bar
# bar = Bar()
# # 给柱状图添加x轴数据，数据内容是博主姓名列表：name
# bar.add_xaxis(xaxis_data=name)
# # 给柱状图添加y轴数据，y轴数据有粉丝数和点赞量两个
# bar.add_yaxis(y_axis=fans, series_name="粉丝数")
# bar.add_yaxis(y_axis=likes, series_name="点赞数")
# # 优化：横坐标文字比较长时候，部分文字被遮挡不进行显示，所以让横坐标文字稍微倾斜45度一点，同时添加一个标题
# bar.set_global_opts(
#     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
#     title_opts=opts.TitleOpts(title="博主粉丝数和点赞数")
# )
"""下述代码与上述注释代码等价"""
bar = (Bar()
       .set_global_opts(title_opts=opts.TitleOpts(title="博主粉丝数和点赞数"),
                        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))
       .add_xaxis(xaxis_data=name)
       .add_yaxis(y_axis=fans, series_name="粉丝数")
       .add_yaxis(y_axis=likes, series_name="点赞数")
       )

# 绘制出这条柱状图，并保存到路径"./result/fans_likes.html"
resultFileName = "fans_likes_2.html"
bar.render(path=os.path.join(resultPath, resultFileName))
