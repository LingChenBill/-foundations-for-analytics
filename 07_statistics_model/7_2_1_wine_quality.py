#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   分析葡萄酒质量数据集
#   计算出每列的总体描述性统计量、质量列中的唯一值以及和这个唯一值对应的观测数量
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols, glm

# 将数据集读入到Pandas数据框中
wine = pd.read_csv('../data/winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')
print(wine.head())

print('显示所有变量的描述性统计量：')
print(wine.describe())

print('找出唯一值：')
print(sorted(wine.quality.unique()))

print('计算值的频率：')
print(wine.quality.value_counts())

print('按照葡萄酒类型显示质量的描述性统计量：')
# unstack函数将结果重新排列，这样红，白葡萄酒的统计量就会显示在并排的两列中
print(wine.groupby('type')[['quality']].describe().unstack('type'))

print('按照葡萄酒类型显示质量的特定分位数值：')
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print('按照葡萄酒类型查看质量分布：')
red_wine = wine.loc[wine['type'] == 'red', 'quality']
white_wine = wine.loc[wine['type'] == 'white', 'quality']
sns.set_style("dark")
print(sns.displot(red_wine,
                  kind='hist', kde=False, color='red', label='Red wine'))
print(sns.displot(white_wine,
                  kind='hist', kde=False, color='yellow', label='White wine'))
sns.utils.axlabel("Quality Score", "Density")
plt.title("Distribution of Quality by Wine Type")
plt.legend()
plt.show()

print('检验红葡萄酒和白葡萄酒的平均质量是否有所不同：')
print(wine.groupby(['type'])[['quality']].agg(['std']))
# 红葡萄酒和白葡萄酒评分的标准差是否相同，所有在t检验中使用合并方差
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))

