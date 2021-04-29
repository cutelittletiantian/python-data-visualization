import pyecharts.options as opts
from pyecharts.charts import Line
import os

"""准备数据"""
# 将周一至周日并赋值给变量data
data = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# 将不同营销渠道的点击量数据存入下列列表中
# 邮件营销点击量
email = [120, 132, 101, 134, 90, 230, 210]
# 视频推广点击量
video = [150, 232, 201, 154, 190, 330, 410]

"""执行绘图

1、折线图的标题为“营销渠道点击对比”
2、x轴是data
3、y轴数据有两项：一个是email，图例设为“邮件营销”；另一个是video，图例设为“视频推广”
4、y轴设定后的曲线都是光滑的
5、y轴下方要有阴影，设置透明度为50%（areastyle_opts，这个用法可以查看pyecharts官方文档）
"""
line = (Line()
        .set_global_opts(title_opts=opts.TitleOpts(title="营销渠道点击对比"))
        .add_xaxis(xaxis_data=data)
        .add_yaxis(series_name="邮件营销", y_axis=email,
                   is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        .add_yaxis(series_name="视频推广", y_axis=video,
                   is_smooth=True,
                   areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        )

# 保存路径
resultPath = "./result"
if not os.path.exists(resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "marketing_clicking_area.html"
# 执行保存
line.render(path=os.path.join(resultPath, resultFileName))
