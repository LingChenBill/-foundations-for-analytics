#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/02
# @Author: Lingchen
# @Prescription: P132.
# pandas 在所有工作表中选取特定列.
# 使用 pandas 中的 read_excel 函数将所有工作表读入一个字典.
# 然后，使用 loc 函数在每个工作表中选取特定的列，创建一个筛选过的数据框列表，
# 并将这些数据框连接在一起，形成一个最终数据框.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/18/pandas_column_by_name_all_sheets.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=False)
print('data_frame: ', data_frame)

column_output = []

for worksheet_name, data in data_frame.items():
    column_output.append(data.loc[:, ['Customer Name', 'Sale Amount']])

selected_columns = pd.concat(column_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
selected_columns.to_excel(writer, sheet_name='selected_columns_all_worksheets', index=False)
writer.save()
