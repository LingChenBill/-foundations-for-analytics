#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/10/31
# @Author: Lingchen
# @Prescription: P118.
# pandas 也有一组读取 Excel 文件的函数.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/04/output_sales_2013.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name='january_2013')

write = pd.ExcelWriter(output_file)

data_frame.to_excel(write, sheet_name='jan_13_output', index=False)
write.save()
