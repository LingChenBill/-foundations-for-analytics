#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/11/02
# @Author: Lingchen
# @Prescription: P130.
# pandas 在所有工作表中筛选特定行.
# 参数:
# ../data/sales_2013.xlsx ../data/ch03/16/pandas_value_meet_conditions_all_sheets.xlsx
import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheet_name=None, index_col=None)

row_output = []

for worksheet_name, data in data_frame.items():
    row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])

filtered_rows = pd.concat(row_output, axis=0, ignore_index=True)

writer = pd.ExcelWriter(output_file)
filtered_rows.to_excel(writer, sheet_name='sale_amount_gt2000', index=False)
writer.save()
