#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P122.
# pandas 行中的值属于某个集合.
# 想筛选出购买日期为 01/24/2013 或 01/31/2013 的行.
# pandas 提供了 isin 函数，你可以使用它来检验一个特定值是否在一个列表中.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/08/pandas_in_set.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=False)

# 筛选日期列表.
important_dates = ['01/24/2013', '01/31/2013']

data_frame_value_in_set = data_frame[data_frame['Purchase Date'].isin(important_dates)]

write = pd.ExcelWriter(output_file)
data_frame_value_in_set.to_excel(write, sheet_name='jan_13_output', index=False)
write.save()
