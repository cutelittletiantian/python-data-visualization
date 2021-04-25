import openpyxl
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

wb = openpyxl.load_workbook("./resources/travel_routes.xlsx", data_only=True)
sheet = wb["travel_route"]
routeList = []

for row in range(2, sheet.max_row + 1):
    routeInfo = sheet[row]
    data = (routeInfo[0].value, routeInfo[1].value)
    routeList.append(data)

line_color_js = """
new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#42AECC'
                }, {
                    offset: 1,
                    color: '#F5602C'
                }], false)
"""

geo = Geo(
    init_opts=opts.InitOpts(
        theme="dark",
        bg_color="#475262")
)

geo.add_schema(maptype="china",
               itemstyle_opts=opts.ItemStyleOpts(
                   color="#2D3948", border_color="#58667A"),
               emphasis_itemstyle_opts=opts.ItemStyleOpts(color="#2a333d"))

geo.add(
    "",
    routeList,
    type_="lines",
    symbol="circle",
    symbol_size=10,
    effect_opts=opts.EffectOpts(
        symbol="circle", symbol_size=4, trail_length=0),
    linestyle_opts=opts.LineStyleOpts(
        width=2, opacity=0.5, curve=0.1, color=JsCode(line_color_js)),
    label_opts=opts.LabelOpts(is_show=False)
)

geo.render(path="./result/result_ex0_2_geo.html")
