#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/28
# @Author: Lingchen
# @Prescription: P115.
# 读写 Excel 文件.
import sys
from xlrd import open_workbook
from xlwt import Workbook

# ../data/sales_2013.xlsx ../data/ch03/02/sales_2013_output.xls
input_file = sys.argv[1]
output_file = sys.argv[2]

# 实例化一个 xlwt Workbook 对象，以使我们可以将结果写入用于输出的 Excel 文件.
# 使用 xlwt 的 add_sheet 函数为输出工作簿添加一个工作表 jan_2013_output.
output_workbook = Workbook(encoding='utf-8')
output_worksheet = output_workbook.add_sheet('jan_2013_output')

with open_workbook(input_file) as workbook:
    # 使用这个 workbook 对象的 sheet_by_name 函数引用名称为 january_2013 的工作表.
    worksheet = workbook.sheet_by_name('january_2013')

    # 创建了行与列索引值上的 for 循环语句，使用 range 函数和 worksheet 对象的 nrows 属性和 ncols 属性，
    # 在工作表的每行和每列之间迭代.
    for row_index in range(worksheet.nrows):
        for col_index in range(worksheet.ncols):
            # 使用 xlwt 的 write 函数和行与列的索引将每个单元格的值写入输出文件的工作表.
            output_worksheet.write(row_index, col_index, worksheet.cell_value(row_index, col_index))

output_workbook.save(output_file)

# Purchase Date 列（也就是第 E 列）中的日期显示为数值，不是日期.
# Excel 将日期和时间保存为浮点数，这个浮点数代表从 1900 年 1 月 0 日开始经过的日期数，加上一个 24 小时的小数部分.
