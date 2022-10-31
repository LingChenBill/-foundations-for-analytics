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