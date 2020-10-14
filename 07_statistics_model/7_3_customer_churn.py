#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/14
# @Author: Lingchen
# @Prescription:
#   分析客户流失数据集
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# 完全显示数据
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

print('读入客户流失数据集：')
churn = pd.read_csv('../data/churn.csv', sep=',', header=0)

# 处理标题行，' ' -> '_', 删除单引号，去掉?号，小写
churn.columns = [heading.lower() for heading in
                 churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]

# 创建一个新列，用1或者0来填充新列
churn['churn01'] = np.where(churn['churn'] == 'True.', 1., 0.)
print(churn.head())
print(churn.keys())

print('为分组数据计算描述性统计量，总数，均值，标准差： ')
print(churn.groupby(['churn'])[['day_charge', 'eve_charge', 'night_charge', 'intl_charge',
                                'account_length', 'custserv_calls']].agg(['count', 'mean', 'std']))

print('为不同的变量计算不同类型的多个统计量，计算均值、标准差、总数、最小值、最大值：')
print(churn.groupby(['churn']).agg({
    'day_charge': ['mean', 'std'],
    'eve_charge': ['mean', 'std'],
    'night_charge': ['mean', 'std'],
    'intl_charge': ['mean', 'std'],
    'account_length': ['count', 'min', 'max'],
    'custserv_calls': ['count', 'min', 'max']}))

print('创建一个total_charges: ')
print('将其分为5组，并为每一组计算统计量：')
churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] +\
                         churn['night_charge'] + churn['night_charge'] + churn['intl_charge']
print('使用cut函数按照等宽分箱法将total_charges分成5组：')
factor_cut = pd.cut(churn.total_charges, 5, precision=2)


def get_stats(group):
    """
    为每个分组返回一个统计量字典：最小值，最大值，总数，均值和标准差
    :param group:
    :return:
    """
    return {
        'min': group.min(),
        'max': group.max(),
        'count': group.count(),
        'mean': group.mean(),
        'std': group.std()
    }


print('按照5个分组将客户服务通话次数也分成同样的5组：')
grouped = churn.custserv_calls.groupby(factor_cut)
print(grouped.apply(get_stats).unstack())

print('使用qcut函数通过等深分箱法（按照分位数进行划分）将account_length分成了4组：')
factor_qcut = pd.qcut(churn.account_length, [0., 0.25, 0.5, 0.75, 1.])
grouped = churn.custserv_calls.groupby(factor_qcut)
print(grouped.apply(get_stats).unstack())

print('为intl_plan和vmail_plan创建二值（虚拟）指标变量：')
print('并将它们与新数据框中的churn列连接起来：')
intl_dummies = pd.get_dummies(churn['intl_plan'], prefix='intl_plan')
vmail_dummies = pd.get_dummies(churn['vmail_plan'], prefix='vmail_plan')
churn_with_dummies = churn[['churn']].join([intl_dummies, vmail_dummies])
print(churn_with_dummies)

print('将total_charges按照分位数分组，为每个分位数分组创建一个二值指标变量：')
print('并将它们加入到churn数据框中：')
qcut_names = ['1st_quartile', '2nd_quartile', '3rd_quartile', '4th_quartile']
total_charges_quartiles = pd.qcut(churn.total_charges, 4, labels=qcut_names)
dummies = pd.get_dummies(total_charges_quartiles, prefix='total_charges')
churn_with_dummies = churn.join(dummies)
print(churn_with_dummies.head())

print('创建透视表：')
print('在对total_charges表按照流失情况和客户服务通话次数进行透视转换之后，计算每组的均值：')
print('表示每个流失情况和客户服务通话次数组合的平均总费用：')
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))

print('表示对结果重新格式化，使用流失情况作为行，客户服务通话次数作为列：')
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))

print('客户服务通话次数作为行，流失情况作为列，演示了指定要计算的统计量，处理缺失值和是否显示边际值：')
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'],
                        aggfunc='mean', fill_value='NaN', margins=True))

