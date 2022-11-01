#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P126.
# pandas 列索引值.
# 使用 pandas 选取特定列.
# 1. 设置数据框，在方括号中列出要保留的列的索引值或名称（字符串）.
# 2. 设置数据框和 iloc 函数.
# iloc 函数非常有用，因为它可以使你同时选择特定的行与特定的列.
# 所以，如果使用 iloc 函数来选择列，那么就需要在列索引值前面加上一个冒号和一个逗号，表示你想为这些特定的列保留所有的行.
# 否则，iloc 函数也会使用这些索引值去筛选行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/12/pandas_columns_by_index.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_column_by_index = data_frame.iloc[:, [1, 4]]

write = pd.ExcelWriter(output_file)
data_frame_column_by_index.to_excel(write, sheet_name='jan_13_output', index=False)
write.close()
