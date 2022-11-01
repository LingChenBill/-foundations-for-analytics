#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P121.
# 行中的值属于某个集合.
# 要使用基础 Python 筛选出购买日期属于一个特定集合（例如：日期 01/24/2013 和 01/31/2013 的集合）的行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/07/output_in_set.xls
import sys
from datetime import date

from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 创建了一个列表 important_dates，包含了要使用的日期.
important_dates = ['01/24/2013', '01/31/2013']
purchase_date_column_index = 4

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []

    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        # 创建了一个变量 purchase_datetime，它等于 Purchase Date 列中格式化后的值，
        # 并用它来匹配 important_dates 中格式化的日期。
        purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index,
                                                                 purchase_date_column_index), workbook.datemode)
        purchase_datetime = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')

        row_list = []

        # 检验行中的日期是否是 important_dates 中的一个日期
        # 如果是，那么就处理这一行，并将其写入输出文件.
        if purchase_datetime in important_dates:
            for column_index in range(worksheet.ncols):
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
