import os
from pyecharts.charts import Pie
import pyecharts.options as opts

"""原数据：某连锁店开通会员的人群所在地区分布

键值对：地区名 | 人数（单位；人）
"""
data = {
    '北京': 78, '上海': 77, '黑龙江': 60, '吉林': 75, '辽宁': 91, '贵州': 93, '新疆': 82, '西藏': 61, '青海': 62,
    '四川': 40, '云南': 58, '陕西': 24, '重庆': 77, '内蒙古': 53, '广西': 46, '海南': 92, '澳门': 55, '湖南': 72,
    '江西': 65, '福建': 57, '安徽': 36, '浙江': 77, '江苏': 48, '宁夏': 32, '山西': 70, '河北': 86, '天津': 94
}
# 附带配色方案（生成图案顺时针依次显示的颜色）
color_series = ['#FAE927', '#E9E416', '#C9DA36', '#9ECB3C', '#6DBC49',
                '#37B44E', '#3DBA78', '#14ADCF', '#209AC9', '#1E91CA',
                '#2C6BA0', '#2B55A1', '#2D3D8E', '#44388E', '#6A368B',
                '#7D3990', '#A63F98', '#C31C88', '#D52178', '#D5225B',
                '#D02C2A', '#D44C2D', '#F57A34', '#FA8F2F', '#D99D21',
                '#CF7B25', '#CF7B25', '#CF7B25']
# 预处理：将原数据按照从大到小取值的顺序排序，生成用于绘图的标签-数值元组
data_sorted = sorted(data.items(), key=lambda data_item: data_item[1], reverse=True)


"""绘图南丁格尔玫瑰图

数据的系列名称（series_name）统一为“会员地区分布”
按照给定的配色方案给每块饼配色
绘制为南丁格尔环状玫瑰图
设置玫瑰图类型（rosetype）圆心角相同，数据差异仅通过半径给出
环的内半径（radius）为画布尺寸（长宽较小者）的30%，环的最大外半径（radius）（数值最大的饼的外径）为画布的100%
每块饼的标签（label）显示在饼的内部，字号为8，标签显示格式为"{数据项名}:{直接数值}人"
图例（legend）不显示
整张图标题设为“会员地区分布”
保存图表
"""
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 文件名
resultFileName = "vip_rose_pie.html"
# 执行绘图
rose_pie = (
    Pie()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="会员地区分布"),
        legend_opts=opts.LegendOpts(is_show=False)
    )
    .set_colors(colors=color_series)
    .add(
        series_name="会员地区分布",
        data_pair=data_sorted,
        rosetype="area",
        radius=("30%", "100%"),
        label_opts=opts.LabelOpts(
            position="inside",
            font_size=8,
            formatter="{b}:{c}人"
        )
    )
    .render(path=os.path.join(resultPath, resultFileName))
)