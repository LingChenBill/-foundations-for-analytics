#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P127.
# 在工作表中选取一组列的方法是使用列标题.
# 当你想保留的列的标题非常容易识别，或者在处理多个输入文件过程中，
# 各个输入文件中列的位置会发生改变，但标题不变的时候，这种方法非常有效.
# 要使用基础 Python 选取 Customer ID 和 Purchase Date 列.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/13/output_columns_by_name.xls
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = ['Customer ID', 'Purchase Date']

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = [my_columns]

    header_list = worksheet.row_values(0)
    header_index_list = []

    for header_index in range(len(header_list)):
        if header_list[header_index] in my_columns:
            header_index_list.append(header_index)

    for row_index in range(1, worksheet.nrows):
        row_list = []

        for column_index in header_index_list:
            cell_value = worksheet.cell_value(row_index, column_index)
            cell_type = worksheet.cell_type(row_index, column_index)

            if cell_type == 3:
                date_cell = xldate_as_tuple(cell_value, workbook.datemode)
                date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
                row_list.append(date_cell)
            else:
                row_list.append(cell_value)

        if row_list:
            data.append(row_list)

    for list_index, output_list in enumerate(data):
        for element_index, element in enumerate(output_list):
            output_worksheet.write(list_index, element_index, element)

output_workbook.save(output_file)
