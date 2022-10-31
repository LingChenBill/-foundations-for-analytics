#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/31
# @Author: Lingchen
# @Prescription: P121.
# 要使用 pandas 筛选出满足特定条件的行.
# 使用 pandas 筛选出符合某个条件的行，指定你想判断的列的名称，
# 并在数据框名称后面的方括号中设定具体的判断条件.
# 如果你需要设定多个条件，那么可以将这些条件放在圆括号中，根据需要的逻辑顺序用 "&" 或 "|" 连接起来.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/06/pandas_output_conditions.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

data_frame_value_meets_condition = data_frame[data_frame['Sale Amount'].astype('float') > 1400.0]

write = pd.ExcelWriter(output_file)
data_frame_value_meets_condition.to_excel(write, sheet_name='jan_13_output', index=False)

write.save()
