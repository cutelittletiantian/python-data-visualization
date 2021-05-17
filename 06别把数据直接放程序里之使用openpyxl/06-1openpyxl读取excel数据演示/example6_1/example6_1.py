import os
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

"""读取数据"""
# 资源文件统一所在路径
resourcesPath = "./resources"
# 数据文件名
salesPath = "table.xlsx"
# 读文件（工作簿）
salesBook = openpyxl.load_workbook(filename=os.path.join(resourcesPath, salesPath))  # type: Workbook
# 选择工作表
fruitSalesSheet = salesBook["水果销量"]  # type: Worksheet
# 跳过表头，逐行读取数据
for rowContent in fruitSalesSheet.iter_rows(min_row=2, values_only=True):
    # 以列表形式输出
    print(list(rowContent))
