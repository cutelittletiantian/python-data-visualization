import os
from pyecharts.charts import Pie, Funnel, Page
from pyecharts import options as opts


def rose():
    """
    通过玫瑰图展示每个季度的销量占比，绘图需求：

    1.主题为dark，标题为“销售占比”

    2.隐藏图例

    3.玫瑰图圆心角半径相同，仅通过半径区分数据大小

    4.绘图所用数据对已给出，这里省略从文件读入数据的过程:
    [("数据线", 3884), ("手机膜", 7298), ("手机壳", 5763),("指环支架", 1326),("充电宝", 1889)]

    :return: 绘制好的玫瑰图
    """
    return (
        Pie(init_opts=opts.InitOpts(theme="dark"))
        .set_global_opts(
            title_opts=opts.TitleOpts("销售占比"),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .add(
            series_name="",
            data_pair=[("数据线", 3884), ("手机膜", 7298), ("手机壳", 5763),("指环支架", 1326),("充电宝", 1889)],
            rosetype="area"
        )
    )


def lou():
    """
    通过漏斗图展示店铺订单的转化效率，绘制需求：

    1.主题为dark

    2.标题为“订单转化效率”，隐藏图例

    3.绘图所用数据对已给出，这里省略从文件读入数据的过程:
    [("访问", 100), ("搜索", 78.12), ("点击", 35.74), ("加购", 17.17), ("订单", 2.62)]

    :return: 绘制好的漏斗图
    """
    # 使用Funnel()函数创建实例赋值给funnel
    # 使用InitOpts()，传入参数theme="dark"，赋值给init_opts
    return (
        Funnel(init_opts=opts.InitOpts(theme="dark"))
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(title="订单转化效率")
        )
        .add(
            series_name="",
            data_pair=[("访问", 100), ("搜索", 78.12), ("点击", 35.74), ("加购", 17.17), ("订单", 2.62)],
        )
    )


# 绘制页面组合图，绘制需求：简单布局
# 保存路径
resultPath = "./result"
if not os.path.exists(path=resultPath):
    os.mkdir(path=resultPath)
# 保存文件名
resultFileName = "sales_rose_funnel_page.html"
page = (
    Page(layout=Page.SimplePageLayout)
    .add(
        rose(),
        lou()
    )
    .render(path=os.path.join(resultPath, resultFileName))
)
