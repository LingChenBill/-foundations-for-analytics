#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/01
# @Author: Lingchen
# @Prescription: P124.
# pandas 行中的值匹配于特定模式.
# 筛选出客户姓名以大写字母 J 开头的那些行.
# pandas 提供了若干字符串和正则表达式函数，包括 startswith、endswith、match 和 search 等，
# 你可以使用这些函数在文本中识别子字符串和模式.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/10/pandas_re_match_pattern.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013', index_col=None)

# 识别以 J 开头的文本.
data_frame_value_match_pattern = data_frame[data_frame['Customer Name'].str.startswith('J')]

write = pd.ExcelWriter(output_file)
data_frame_value_match_pattern.to_excel(write, sheet_name='jan_13_output', index=False)
write.close()
