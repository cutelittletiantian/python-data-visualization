import os
from pyecharts.charts import Funnel
import pyecharts.options as opts

"""准备原始数据：某网上商城从用户进入到下订单，中间各个操作过程中平均剩余用户的人数

漏斗图不需要x轴和y轴，但需要二维的列表，分别是某一个环节的名字，以及当前这个环节中的相对变化率数值
[[环节名（变化率）, 环节直接人数], [环节名（变化率）, 环节直接人数], ...]

* 环节名这里稍微加点东西：环节名里面要体现出各个环节相比上一环节的人数变化率

所以显然，下面的原始数据是需要组装的
"""
# 存储标签的列表label
label = ["展现", "点击", "访问", "咨询", "订单"]
# 对应存储数量的列表num（非最终数值）
num = [1000, 880, 264, 52.8, 5.28]

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
              for label_index, label_item in enumerate(label)
              for rate_index, rate_item in enumerate(pass_rate)
              if label_index == rate_index]

# 组装二维列表作为显示数据
data_pair = [[label_rate_item, num_item]
             for label_rate_index, label_rate_item in enumerate(label_rate)
             for num_index, num_item in enumerate(num)
             if label_rate_index == num_index]
# print(data_pair)

"""绘制漏斗图

每个环节（每个漏斗条）中间距离设置为10
数据系名称（series_name）设置为“网店商品浏览阶段人数变化示意”
隐藏图例
保存图片
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "sales_section_funnel.html"
# 执行绘图
funnel = (
    Funnel()
    .set_global_opts(legend_opts=opts.LegendOpts(is_show=False))
    .add(
        series_name="网店商品浏览阶段人数变化示意",
        data_pair=data_pair,
        gap=10
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
