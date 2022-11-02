#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/02
# @Author: Lingchen
# @Prescription: P129.
# 在所有工作表中筛选特定行.
# 要使用基础 Python 在所有工作表中筛选出销售额大于 $2000.00 的所有行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/15/output_value_meet_conditions_all_sheets.xls
import sys
from datetime import date

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('filtered_rows_all_sheets')

# 变量 sales_column_index，保存 Sale Amount 列的索引值.
sales_column_index = 3
# 变量 threshold 来保存你所关心的销售额.
# 要将 Sale Amount 列中的每个值与这个阈值进行比较，来确定哪一行要被写入到输出文件中.
threshold = 2000.0

first_worksheet = True

with open_workbook(input_file) as workbook:
    data = []

    # for 循环，用来在工作簿中的所有工作表之间迭代.
    for worksheet in workbook.sheets():
        # 添加标题.
        if first_worksheet:
            header_row = worksheet.row_values(0)
            data.append(header_row)
            first_worksheet = False

        # 处理每个工作表中的数据行.
        # 因为 range 函数不是从 0 开始，而是从 1 开始，所以你应该知道代码处理的是数据行，不是标题行.
        for row_index in range(1, worksheet.nrows):
            row_list = []

            sale_amount = worksheet.cell_value(row_index, sales_column_index)

            if sale_amount > threshold:
                for column_index in range(worksheet.ncols):
                    cell_value = worksheet.cell_value(row_index, column_index)
                    cell_type = worksheet.cell_type(row_index, column_index)

                    # 日期行日期数据转换.
                    if cell_type == 3:
                        date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                        date_cell = date(*date_cell[0:3]).strftime('%m%d%Y')

                        row_list.append(date_cell)
                    else:
                        row_list.append(cell_value)

            if row_list:
                data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
