#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P125.
# 列索引值.
# 从工作表中选取特定列的一种方法是使用要保留的列的索引值.
# 当你想保留的列的索引值非常容易识别，或者在处理多个输入文件过程中，
# 各个输入文件中列的位置是一致（也就是不会发生改变）的时候，这种方法非常有效.
# 想保留 Customer Name 和 Purchase Date 这两列. 要使用基础 Python 选取这两列.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/11/output_columns_by_index.xls
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

my_columns = [1, 4]

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []

    for row_index in range(worksheet.nrows):
        row_list = []

        # 在 my_columns 中的两个列索引值之间迭代.
        # 在每次循环中，提取出列中单元格的值和类型，判断单元格中的值是否是日期类型，
        # 并对单元格进行相应处理，然后将值追加到 row_list 中.
        for column_index in my_columns:
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
