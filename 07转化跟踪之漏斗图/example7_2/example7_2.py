import os
from pyecharts.charts import Funnel
import pyecharts.options as opts

"""准备原始数据：某网上商城从用户进入到下订单，用户行为在各个购买阶段的剩余人数

漏斗图不需要x轴和y轴，但需要二维的列表，分别是某一个环节的名字，以及当前这个环节中的相对变化率数值
[[环节名, 相比上一环节人数变化率], [环节名, 相比上一环节人数变化率], [环节名, 相比上一环节人数变化率], ...]

所以显然，下面的原始数据是需要组装的
"""
# 存储标签的列表label
user_behavior = ["浏览商品", "加入购物车", "生成订单", "支付订单", "完成交易"]
# 对应存储数量的列表num（非最终数值）
num = [100, 40, 30, 20, 17]

"""显示的最终数值生成

1、数据项：各环节占上一个环节的相对人数变化率（百分数值，不要百分号）
最开始的环节当然是100%
这里保留一位小数
2、标签项：假如按照 标签名+变化率 这种方式进行组合
3、组装数据各项和标签各项成为二维列表
"""
# 计算各个环节人数相对变化率
pass_rate = [100]
# 从第2个元素开始，所以下标始于1
for index in range(1, len(num)):
    relative_percentage = (num[index] / num[index - 1]) * 100
    # 保留一位小数
    relative_percentage = round(relative_percentage, 1)
    pass_rate.append(relative_percentage)

# 标签项的组装，这种写法想象一下数据库的SQL语言，结合类比一下？
label_rate = [f"{label_item}{rate_item}%"
              for label_index, label_item in enumerate(user_behavior)
              for rate_index, rate_item in enumerate(pass_rate)
              if label_index == rate_index]

# 组装二维列表作为显示数据（第一维是上一个）
data_pair = [[label_rate[label_rate_index], num[num_index]]
             for label_rate_index, _ in enumerate(label_rate)
             for num_index, _ in enumerate(num)
             if label_rate_index == num_index]
print(data_pair)

"""绘制漏斗图

图的标题设置为“用户行为转化率”
每个环节（每个漏斗条）中间距离设置为10
数据系名称（series_name）这里不设置
隐藏图例
保存图片
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "user_conversion_rate_funnel.html"
# 执行绘图
funnel = (
    Funnel()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="用户行为转化率"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .add(
        series_name="",
        data_pair=data_pair,
        gap=10
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
