#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P123.
# 行中的值匹配于特定模式.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/09/output_re_match_pattern.xls
import re
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')

# 使用 re 模块的 compile 函数创建了一个正则表达式 pattern.
# r 表示单引号之间的模式是一个原始字符串.
# 元字符 ?P<my_pattern> 捕获了名为 <my_pattern> 的组中匹配了的子字符串，以便在需要时将它们打印到屏幕上或写入文件.
# 我们要搜索的实际模式是 '^J.*'.
# 插入符号（^）是一个特殊符号，表示“在字符串开头搜索模式”.
# 所以，字符串需要以大写字母 J 开头. 句点 . 可以匹配任何字符，除了换行符.
# 所以除换行符之外的任何字符都可以跟在 J 后面.
# 最后，* 表示重复前面的字符 0 次或更多次.
# .* 组合在一起用来表示除换行符之外的任意字符可以在 J 后面出现任意次.
pattern = re.compile(r'(?P<my_pattern>^J.*)')

customer_name_column_index = 1

with open_workbook(input_file) as workbook:
    worksheet = workbook.sheet_by_name('january_2013')
    data = []

    header = worksheet.row_values(0)
    data.append(header)

    for row_index in range(1, worksheet.nrows):
        row_list = []

        # 使用 re 模块中的 search 函数在 Customer Name 列中搜索模式，并检测是否能找到一个匹配.
        # 如果找到了一个匹配，就将这一行中的每个值添加到 row_list 中.
        if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
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
