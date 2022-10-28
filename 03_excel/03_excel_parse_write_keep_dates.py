#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/28
# @Author: Lingchen
# @Prescription: P116.
# 格式化日期数据.
import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

# ../data/sales_2013.xlsx ../data/ch03/03/sales_2013_date_output.xls
input_file = sys.argv[1]
output_file = sys.argv[2]

# 实例化一个 xlwt Workbook 对象，以使我们可以将结果写入用于输出的 Excel 文件.
# 使用 xlwt 的 add_sheet 函数为输出工作簿添加一个工作表 jan_2013_output.
output_workbook = Workbook(encoding='utf-8')
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    # 使用这个 workbook 对象的 sheet_by_name 函数引用名称为 january_2013 的工作表.
    worksheet = workbook.sheet_by_name('january_2013')

    for row_index in range(worksheet.nrows):
        row_list_output = []
        for col_index in range(worksheet.ncols):
            # 检验每个单元格是否含有日期数据.
            if worksheet.cell_type(row_index, col_index) == 3:
                # 函数 xldate_as_tuple 可以将 Excel 中代表日期、时间或日期时间的数值转换为元组.
                # 只要将数值转换成了元组，就可以提取出具体时间元素（例如：年、月、日）并将时间元素格式化成不同的时间格式
                # (例如：1/1/2010 或 January 1, 2010).
                date_cell = xldate_as_tuple(worksheet.cell_value(row_index, col_index), workbook.datemode)

                # 使用元组索引来引用元组 date_cell 中的前 3 个元素（也就是年、月、日）并将它们作为参数传给 date 函数，
                # 这个函数可以将这些值转换成一个 date 对象.
                # strftime 函数将 date 对象转换为一个具有特定格式的字符串.
                # 格式 '%m/%d/%Y' 表示像 2014 年 3 月 15 日这样的日期应该显示为 03/15/2014.
                print('date cell old: ', date_cell)
                date_cell = date(*date_cell[0:3]).strftime('%m%d%Y')
                print('date cell: ', date_cell)
                row_list_output.append(date_cell)
                output_worksheet.write(row_index, col_index, date_cell)
            else:
                non_date_cell = worksheet.cell_value(row_index, col_index)
                row_list_output.append(non_date_cell)
                output_worksheet.write(row_index, col_index, non_date_cell)

output_workbook.save(output_file)

# Purchase Date 列（也就是第 E 列）中的日期显示为数值，不是日期.
# Excel 将日期和时间保存为浮点数，这个浮点数代表从 1900 年 1 月 0 日开始经过的日期数，加上一个 24 小时的小数部分.
