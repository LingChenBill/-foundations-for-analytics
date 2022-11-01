#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P128.
# pandas 在工作表中选取一组列的方法是使用列标题.
# 要使用 pandas 基于列标题选取特定列，
# 1. 是在数据框名称后面的方括号中将列名以字符串方式列出.
# 2. 是使用 loc 函数.
# 如果使用 loc 函数，那么需要在列标题列表前面加上一个冒号和一个逗号，表示你想为这些特定的列保留所有行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/14/pandas_columns_by_name.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# 如果使用 loc 函数，那么需要在列标题列表前面加上一个冒号和一个逗号，表示你想为这些特定的列保留所有行.
data_frame_column_by_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]

write = pd.ExcelWriter(output_file)
data_frame_column_by_name.to_excel(write, sheet_name='jan_13_output', index=False)
write.close()
