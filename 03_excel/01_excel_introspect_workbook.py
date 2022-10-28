#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/28
# @Author: Lingchen
# @Prescription: P111.
# 内省 Excel 工作簿.
import sys
from xlrd import open_workbook

# input_file_path = '../data/sales_2013.xlsx'
input_file = sys.argv[1]

# 使用 open_workbook 函数打开一个 Excel 输入文件，并赋给一个名为 workbook 的对象.
# workbook 对象中包含了工作簿中所有可用的信息，所以可以使用这个对象从工作簿中得到单独的工作表.
workbook = open_workbook(input_file)
# 打印出工作簿中工作表的数量.
print('Number of worksheets: ', workbook.nsheets)

# 在工作簿中的所有工作表之间迭代.
# workbook 对象的 sheets 方法可以识别出工作簿中所有的工作表.
for worksheet in workbook.sheets():
    # 打印出每个工作表的名称和每个工作表中行与列的数量.
    print('Worksheet name: ', worksheet.name, '\t Rows: ', worksheet.nrows, '\t Columns: ', worksheet.ncols)
