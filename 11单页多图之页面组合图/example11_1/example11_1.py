import os
from pyecharts import options as opts
from pyecharts.charts import Bar, Page


def mi() -> Bar:
    """
    绘制小米手机的点赞、转发、评论数据的柱状图，绘图需求：

    1.设置图表主题为macarons

    2.设置x轴，为点赞数、转发数、评论数；

    3.设置y轴，传入数据，这里为了方便演示页面组合图，openpyxl读取数据环节先跳过，
    所需数据已直接给出：

    * 数据系列为mi10_young的三项数据为[405020, 159455, 160529]

    * 数据系列为mi10_pro的三项数据为[131234, 11431, 36922]

    * 数据系列为redmi_k30_pro的三项数据为[110892, 7518, 29415]

    4.标题为“2020小米新品手机微博数据”，副标题为“各型号获赞、评论、转发数”；

    5.图例右端位置在相对画布作图区右25%处位置。

    6.y轴取值的最大值要和另一张图统一（取值500000），
    确保和另一张柱状图直观比对时不出现可视化陷阱错误

    :return: 绘制完成的小米数据柱状图
    """
    return (
        Bar(init_opts=opts.InitOpts(theme="macarons"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020小米新品手机微博数据", subtitle="各型号获赞、评论、转发数"),
            legend_opts=opts.LegendOpts(pos_right="25%"),
            yaxis_opts=opts.AxisOpts(max_=500000)
        )
        .add_xaxis(xaxis_data=["点赞数", "转发数", "评论数"])
        .add_yaxis(series_name="mi10_young", y_axis=[405020, 159455, 160529])
        .add_yaxis(series_name="mi10_pro", y_axis=[131234, 11431, 36922])
        .add_yaxis(series_name="redmi_k30_pro", y_axis=[110892, 7518, 29415])
    )


def huawei() -> Bar:
    """
    绘制华为手机的点赞、转发、评论数据的柱状图，绘图需求：

    1.设置图表主题为macarons

    2.设置x轴，为点赞数、转发数、评论数；

    3.设置y轴，传入数据，这里为了方便演示页面组合图，openpyxl读取数据环节先跳过，
    所需数据已直接给出：

    * 数据系列为honor_x10的三项数据为[315750, 123680, 143533]

    * 数据系列为honor_30s的三项数据为[101736, 9841, 28089]

    * 数据系列为huawei_nova7的三项数据为[156793, 12412, 35721]

    4.标题为“同价位华为为手机微博数据”，副标题为“各型号获赞、评论、转发数”；

    5.图例右端位置在相对画布作图区右25%处位置。

    6.y轴取值的最大值要和另一张图统一（取值500000），
    确保和另一张柱状图直观比对时不出现可视化陷阱错误

    :return: 绘制完成的华为数据柱状图
    """
    return (
        Bar(init_opts=opts.InitOpts(theme="macarons"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="同价位华为为手机微博数据", subtitle="各型号获赞、评论、转发数"),
            legend_opts=opts.LegendOpts(pos_right="25%"),
            yaxis_opts=opts.AxisOpts(max_=500000)
        )
        .add_xaxis(xaxis_data=["点赞数", "转发数", "评论数"])
        .add_yaxis(series_name="honor_x10", y_axis=[315750, 123680, 143533])
        .add_yaxis(series_name="honor_30s", y_axis=[101736, 9841, 28089])
        .add_yaxis(series_name="huawei_nova7", y_axis=[156793, 12412, 35721])
    )


# 绘制页面组合图需求：布局形式为简单布局，就这一个，没了，此外就记得保存
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFilePath = "weiboPhoneCompete_bar_page.html"
page = (
    Page(layout=Page.SimplePageLayout)
    .add(
        mi(),
        huawei()
    )
    .render(path=os.path.join(resultPath, resultFilePath))
)
