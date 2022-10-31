#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/31
# @Author: Lingchen
# @Prescription: P119.
# 首先，来看一下如何使用基础 Python 筛选出特定的行.
# 在这个示例中，你想筛选出 Sale Amount 大于 $1400.00 的行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/05/output_conditions.xls
import sys
from datetime import date

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 定义的 sale_amount_column_index 中的值来定位 Sale Amount 列.
sale_amount_column_index = 3

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')

    # 创建了一个空列表 data. 将用输入文件中要写入输出文件中的那些行来填充这个列表.
    data = []

    # 提取出标题行中的值. 想保留标题行，而且检验这一行是否满足筛选条件没有意义，所以标题行直接追加到 data 中.
    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        # 为输入文件中的每一行都创建空列表 row_list，
        # 但是只使用值填充某些空列表(就是Sale Amount 这列的值大于 1400.0 的那些行的空列表).
        row_list = []

        # 创建了一个变量 sale_amount，用来保存行中的销售额.
        sale_amount = worksheet.cell_value(row_index, sale_amount_column_index)

        if sale_amount > 1400.0:
            for column_index in range(worksheet.ncols):
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)

                # 检验行中的每个值是否是日期类型. 如果是日期类型，那么就将这个值格式化成日期数据.
                if cell_type == 3:
                    date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                    date_cell = date(*date_cell[0:3]).strftime('%m%d%Y')

                    row_list.append(date_cell)
                else:
                    row_list.append(cell_value)

        # 将要保留的行追加到一个新列表 data 中的原因是，这样可以得到新的连续的行索引值.
        if row_list:
            data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
