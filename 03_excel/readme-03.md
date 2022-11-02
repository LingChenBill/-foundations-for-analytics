### Excel文件.

```text
安装依赖包.
pip install xlrd==1.2.0
pip install xlwt==1.2.0

排错命令:
pip show xlrd
pip uninstall xlrd
pip install xlrd==1.2.0
```

```text
01_excel_introspect_workbook.py:
内省 Excel 工作簿.
```

```text
02_excel_parse_write.py:
读写Excel文件.
```

```text
03_excel_parse_write_keep_dates.py:
格式化日期数据.
```

```text
04_pandas_read_write_excel.py:
pandas 也有一组读取 Excel 文件的函数.
```

```text
05_excel_value_meets_condition.py:
首先，来看一下如何使用基础 Python 筛选出特定的行.
在这个示例中，你想筛选出 Sale Amount 大于 $1400.00 的行.
```

```text
06_pandas_value_meets_condition.py:
要使用 pandas 筛选出满足特定条件的行.
```

```text
07_excel_value_in_set.py:
行中的值属于某个集合.
```

```text
08_pandas_value_in_set.py:
pandas 行中的值属于某个集合.
```

```text
09_excel_value_match_pattern.py:
行中的值匹配于特定模式.
```

```text
10_pandas_value_match_pattern.py:
pandas 行中的值匹配于特定模式.
```

```text
11_excel_columns_by_index.py:
列索引值.
```

```text
12_pandas_columns_by_index.py:
pandas 列索引值.
```

```text
13_excel_columns_by_name.py:
在工作表中选取一组列的方法是使用列标题.
```

```text
14_pandas_columns_by_name.py:
pandas 在工作表中选取一组列的方法是使用列标题.
```

```text
15_excel_value_meet_conditions_all_sheets.py:
在所有工作表中筛选特定行.
```

```text
16_pandas_value_meet_conditions_all_sheets.py:
pandas 在所有工作表中筛选特定行.
```

```text
17_excel_column_by_name_all_sheets.py:
在所有工作表中选取特定列.
```

```text
18_pandas_column_by_name_all_sheets.py:
pandas 在所有工作表中选取特定列.
```