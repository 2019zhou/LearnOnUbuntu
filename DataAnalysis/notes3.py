数据探索

检查数据错误
缺失值
异常值
不一致的数据

iris_df.target.astype(float)  #把int类型转化为float类型

基本数据特征分析方法
分布分析 定量 定性
统计量分析 
集中趋势分析Central tendency analysis 均值， 中位数
离中趋势分析Dispersion tendency analysis 标准差，四分位距
相关分析
Scatter 散点图
两个变量独立且符合正态分布：使用Pearson相关系数 r> 0.5 相关， r>0.8 非常相关， r = 1完全线性相关
不服从，使用Spearman ,kendal相关系数
plt.hist(iris_df.iloc[:,0], 30, color = 'c')
正态分布的检验
import scipy
scipy.stats.normaltest(iris_df.iloc[:,0], axis = 0)
函数返回卡方分布统计和关联的p值
p > 0.05 基本满足正态分布

iris_df.target.value_counts() 看一下被分成了几类
iris_df.target.value_counts().plot(kind = 'pie')

iris_df.iloc[:, 0].mean()
iris_df.iloc[:, 0].median()
iris_df.iloc[:, 0].std()
iris_df.iloc[:, 0].quantile()
iris_df.iloc[:, 0].quantile([0.25, 0.75])
# 求四分位距
iris_df.iloc[:, 0].quantile([0.75]).loc[0.75] - iris_df.iloc[:, 0].quantile([0.25]).loc[0.25]
iris_df.iloc[:, 0].describe()
iris_df.iloc[:, 0].describe().loc['75%']-iris_df.iloc[:, 0].describe().loc['25%']

iris_df.iloc[:, [0, 1, 4]].corr()
iris_df['target'].corr(iris_df.iloc[:, 0])
import seaborn as sns
# 绘制热力图， 故意输错可以看出还有哪些可以使用
sns.heatmap(iris_df.iloc[:, [0, 1, 4]].corr(), annot = True, fmt = '.1f', cmap = 'rainbow')


import requests
import re
import json
import pandas as pd
from datetime import date
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)  
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])     # m = ['[{...},{...},...]']
        quotes = quotes[::-1]
    return  [item for item in quotes if 'type' not in item]
 
def f(x):
    return date.strftime(x, '%Y-%m-%d')
     
quotes = retrieve_quotes_historical('AXP')
quotesdf_ori = pd.DataFrame(quotes)
lst = []
lst = list(map(f, list(map(date.fromtimestamp, quotesdf_ori.date))))
quotesdf_ori.index = lst
quotesdf_m = quotesdf_ori.drop(['adjclose'], axis = 1)
quotesdf = quotesdf_m.drop(['date'], axis = 1)
print(quotesdf)

import pandas as pd
# 求最近一次成交价中的均值
djidf.price.mean()
djidf['price'].mean()
# 最近一次成交价大于等于300的公司名
djidf[djidf.price >= 300].name
# 美国运通公司近一年股票涨和跌分别的天数
len(quotesdf[quotesdf.close > quotesdf.open])
# 美国运通公司近一年相邻两天收盘价的涨跌情况
status = np.sign(np.diff(quotesdf.close))
len(status[status == 1])
len(status[status == -1])

# 关于有没有相关的函数实现
# 1. 有信心，一般python都有相关库实现了
# 2. 多看一些官方文档的例子

# 按最近一次成交价对道指成分股股票进行排序。根据排序结果列出前三甲公司名
tempdf = djidf.sort_values(by = 'price', ascending = False)
tempdf[:3].name

month = [item[5:7] for item in quotesdf.index]
quotesdf.groupby(month)
quotesdf.groupby(month).open.count()
for k, data in quotesdf.groupby(month):
    print(k)
    print(data)

Grouping: splitting, applying, combining

# 统计近一年美国运通公司每个月的股票开盘天数
month = [item[5:7] for item in quotesdf.index]
quotesdf.groupby(month).apply(len)

合并
Append 追加行
# 把美国运通公司
p.append(q)
Concat连接
join (和数据库中的概念一致)
pd.merge(djidf.drop(['price'], axis = 1), AKdf, on = 'code')

import numpy as np
from sklearn.cluster import KMeans
list1 =
list2 = 
list3 = 
list4 = 
list5 = 
list6 = 
X = np.array([list1, list2, list3, list4, list5, list6])
kmeans = KMeans(n_cluster = 2).fit(X)
pred = kmeans.predict(X)
print(pred)

# -*- coding: utf-8 -*-
"""
MovieLens data processing
"""
 
import pandas as pd
import numpy as np
 
# Download url: https://files.grouplens.org/datasets/movielens/ml-100k.zip
 
unames = ['user id', 'age', 'gender', 'occupation', 'zip code']
users = pd.read_csv('ml-100k/u.user', sep = '|', names = unames)
rnames = ['user id', 'item id', 'rating', 'timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep = '\t', names = rnames)
users_df = users.loc[:, ['user id', 'gender']]
ratings_df = ratings.loc[:, ['user id', 'rating']]
rating_df = pd.merge(users_df, ratings_df)
 
# Way 1 - groupby()
result = rating_df.groupby('gender').rating.apply(pd.Series.std)
print(result)
# Way 1 - pivot_table()
result = pd.pivot_table(rating_df, index = ['gender'], values = 'rating', aggfunc = pd.Series.std)
print(result)
 
# Way 2 - groupby()
df_temp = rating_df.groupby(['user id', 'gender']).apply(np.mean)
result = df_temp.groupby('gender').rating.apply(pd.Series.std)
print(result)
# Way 2 - pivot_table()
gender_table = pd.pivot_table(rating_df, index = ['gender', 'user id'], values = 'rating')
Female_df = gender_table.query("gender == ['F']")
Male_df = gender_table.query("gender == ['M']")
Female_std = pd.Series.std(Female_df)
Male_std = pd.Series.std(Male_df)


# -*- coding: utf-8 -*-
"""
winequality-red data mining
"""
# url: https://archive.ics.uci.edu/ml/datasets/Wine+Quality
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import warnings
warnings.filterwarnings('ignore') 
 
try:
    wine = pd.read_csv('winequality-red.csv', sep = ';') 
except:
    print("Cannot find the file!")
 
 
print(wine.info())
print(wine.describe())
wine = wine.drop_duplicates()
 
wine['quality'].value_counts().plot(kind = 'pie', autopct = '%.2f')
plt.show()
 
print(wine.corr().quality)
 
plt.subplot(121)
sns.barplot(x = 'quality', y = 'volatile acidity', data = wine)
plt.subplot(122)
sns.barplot(x = 'quality', y = 'alcohol', data = wine)
plt.show()
 
from sklearn.preprocessing import LabelEncoder
bins = (2, 4, 6, 8)
group_names  = ['low', 'medium', 'high']
wine['quality_lb'] = pd.cut(wine['quality'], bins = bins, labels = group_names)
 
lb_quality = LabelEncoder()    
wine['label'] = lb_quality.fit_transform(wine['quality_lb']) 
 
print(wine.label.value_counts())
 
wine_copy = wine.copy()
wine.drop(['quality', 'quality_lb'], axis = 1, inplace = True) 
X = wine.iloc[:,:-1]
y = wine.label
 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
 
from sklearn.preprocessing import scale     
X_train = scale(X_train)
X_test = scale(X_test)
 
from sklearn.metrics import confusion_matrix
 
rfc = RandomForestClassifier(n_estimators = 200)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test, y_pred))
 
param_rfc = {
            "n_estimators": [10,20,30,40,50,60,70,80,90,100,150,200],
            "criterion": ["gini", "entropy"]
            }
grid_rfc = GridSearchCV(rfc, param_rfc, iid = False, cv = 5)
grid_rfc.fit(X_train, y_train)
best_param_rfc = grid_rfc.best_params_
print(best_param_rfc)
rfc = RandomForestClassifier(n_estimators = best_param_rfc['n_estimators'], criterion = best_param_rfc['criterion'], random_state=0)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print('Gender', '\nF\t%.6f' % Female_std, '\nM\t%.6f' % Male_std)
