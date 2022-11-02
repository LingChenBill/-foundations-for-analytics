#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/02
# @Author: Lingchen
# @Prescription: P131.
# 在所有工作表中选取特定列.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/17/output_column_by_name_all_sheets.xls
import sys
from datetime import date

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('selected_columns_all_worksheets')

# 创建了一个列表变量 my_columns，包含了我们要保留的两列的名称.
my_columns = ['Customer Name', 'Sale Amount']

first_worksheet = True

with open_workbook(input_file) as workbook:
    # 将 my_columns 放入 data，作为 data 中的第一个列表，因为它是要写入输出文件的列的列标题.
    data = [my_columns]
    # 用来保存 Customer Name 和 Sale Amount 列的索引值.
    index_of_cols_to_keep = []

    for worksheet in workbook.sheets():
        # 如果是第一个工作表，我们就识别出 Customer Name 和 Sale Amount 列的索引值，
        # 并将其追加到列表 index_of_cols_to_keep 中.
        # 然后，将 first_worksheet 的值设为 False.
        if first_worksheet:
            header = worksheet.row_values(0)
            for column_index in range(len(header)):
                if header[column_index] in my_columns:
                    index_of_cols_to_keep.append(column_index)

            first_worksheet = False

        for row_index in range(1, worksheet.nrows):
            row_list = []
            # 只处理索引值在 index_of_cols_to_keep 中的那些列.
            # 如果这些列中有日期型数据，就将其格式化.
            # 在组合好一行要写入输出文件的数据之后，将这个数据列表追加到 data 中.
            for column_index in index_of_cols_to_keep:
                cell_value = worksheet.cell_value(row_index, column_index)
                cell_type = worksheet.cell_type(row_index, column_index)

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
