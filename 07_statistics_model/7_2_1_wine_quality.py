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
# plt.show()

print('检验红葡萄酒和白葡萄酒的平均质量是否有所不同：')
print(wine.groupby(['type'])[['quality']].agg(['std']))
# 红葡萄酒和白葡萄酒评分的标准差是否相同，所有在t检验中使用合并方差
tstat, pvalue, df = sm.stats.ttest_ind(red_wine, white_wine)
print('tstat: %.3f pvalue: %.4f' % (tstat, pvalue))

print('计算所有变量的相关矩阵：')
print(wine.corr())

print('从红葡萄酒和白葡萄酒的数据中取出一个小样本来进行绘图：')


def take_sample(data_frame, replace=False, n=200):
    """
    从红葡萄酒和白葡萄酒的数据中取出一个小样本来进行绘图
    :param data_frame:
    :param replace:
    :param n:
    :return:
    """
    return data_frame.loc[np.random.choice(data_frame.index, replace=replace, size=n)]


reds_sample = take_sample(wine.loc[wine['type'] == 'red', :])
whites_sample = take_sample(wine.loc[wine['type'] == 'white', :])

# 将抽样所得的两个数据框连接成一个数据框
wine_sample = pd.concat([reds_sample, whites_sample])

# 在wine数据框中创建一个新列in_sample，并使用where函数与isin函数对这个新列进行填充
# 填充的值根据此行的索引值是否在抽样数据的索引值中分别设为1和0
wine['in_sample'] = np.where(wine.index.isin(wine_sample.index), 1., 0.)

# 使用crosstab函数来确认in_sample列中包含400个1和6097个0
print(pd.crosstab(wine.in_sample, wine.type, margins=True))

print('查看成对变量之间的关系：')
sns.set_style("dark")

# 使用sns.pairplot来创建一个统计图矩阵
g = sns.pairplot(wine_sample, kind='reg', plot_kws={"ci": False, "x_jitter": 0.25, "y_jitter": 0.25},
                 hue='type', diag_kind='hist', diag_kws={"bins": 10, "alpha": 1.0},
                 palette=dict(red="red", white="yellow"),
                 markers=["o", "s"], vars=['quality', 'alcohol', 'residual_sugar'])
# plt.show()
print(g)

plt.suptitle('Histograms and Scatter Plots of Quality, Alcohol, and Residual Sugar',
             fontsize=14, horizontalalignment='center', verticalalignment='top', x=0.5, y=0.999)
# plt.show()

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density ' \
             '+ fixed_acidity + free_sulfur_dioxide + pH + residual_sugar ' \
             '+ sulphates + total_sulfur_dioxide + volatile_acidity'

lm = ols(my_formula, data=wine).fit()
print(lm.summary())

print("\nQuantities you can extract from the result:\n%s" % dir(lm))
print("\nCoefficients:\n%s" % lm.params)
print("\nCoefficient Std Errors:\n%s" % lm.bse)
print("\nAdj. R-squared:\n%.2f" % lm.rsquared_adj)
print("\nF-statistic: %.1f  P-value: %.2f" % (lm.fvalue, lm.f_pvalue))
print("\nNumber of obs: %d  Number of fitted values: %s" % (lm.nobs, len(lm.fittedvalues)))


print('创建一个名为dependent_variable的序列来保存质量数据：')
dependent_variable = wine['quality']

# 创建一个名为independent_variables的数据框
# 保存初始的葡萄酒数据集中除'quality', 'type', 'in_sample'之外的所有变量
independent_variables = wine[wine.columns.difference(['quality', 'type', 'in_sample'])]

independent_variable_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()

wine_standardized = pd.concat([dependent_variable, independent_variable_standardized], axis=1)

lm_standardized = ols(my_formula, data=wine_standardized).fit()
print(lm_standardized.summary())

# 使用葡萄酒数据集中的前10个观测创建10个新的观测
# 新观测中只包含模型中使用的自变量
# new_observations = wine.ix[wine.index.isin(range(10)), independent_variables.columns]
new_observations = wine.loc[wine.index.isin(range(10)), independent_variables.columns]

# 基于新观测中的葡萄酒特性预测质量评分
y_predicted = lm.predict(new_observations)

print('将预测值保留两位小数并打印到屏幕上: ')
y_predicted_rounded = [round(score, 2) for score in y_predicted]
print(y_predicted_rounded)
