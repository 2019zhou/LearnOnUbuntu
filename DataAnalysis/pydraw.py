import matplotlib.pyplot as plt
plt.plot([3, 4, 7, 6, 2, 8, 9])
plt.show()
plt.savefig('sss.jpg')

# 有关定义基本上是和matlab完全相同的
# subplot 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 300)
fig, (ax0, ax1) = plt.subplots(2,1)
ax0.plot(x, np.sin(x), color = 'r')
ax0.set_title('subplot1')
plt.subplots_adjust(hspace = 0.5) # 垂直方向的距离
ax1.plot(x, np.cos(x), color = 'g')
ax1.set_title('subplot2')

axes([left, bottom, width, height]) #参数范围是（0，1）

# pandas 绘图
#loc基于数据的标签选择
#loc 后面是包括的， iloc后面半段是不包括的

Seaborn

数据探索，数据预处理
数据探索 检查数据错误，了解数据分布特征和内在规律
数据预处理 Data cleaning Data integeration Data transformation Data reduction

import pandas as pd

isnull 看下有没有缺失值
dropna 有空值就删除
fillna 对空值进行填充
quotesdf_nan.fillna(method = 'ffill') 上一个非缺失值填充
quotesdf_nan.fillna(method = 'bfill') 下一个非缺失值填充
import pandas as pd
from scipy.interpolate import lagrange # 导入拉格朗日插值函数
 
# 利用拉格朗日插值法填充缺失值
df = pd.read_excel("nan.xlsx")
for i in df.columns:
    for j in range(len(df)):
        if (df[i].isnull())[j]: # 如果为空则进行插值
            k = 3  # 设置取前后数的个数为3，默认为5
            y = df[i][list(range(j-k, j)) + list(range(j+1, j+1+k))] # 取数
            y = y[y.notnull()]  # 去掉取出数中的空值
            df[i][j] = lagrange(y.index, list(y))(j)
 print(df)

异常值检测
quotesdf_nam.describe()
3σ原则
quotesdf_nan[abs(quotesdf_nan - quotesdf_nan.mean()) > 3*quotesdf_nan.std()]
分箱法 binning

数据变换 规范化，连续属性离散化， 特征二值化
boston = datasets.load_boston()
boston.feature_names
boston.shape
import pandas as pd
df = pd.DataFrame(boston.data[:, 4:7])
df.columns = boston.feature_names[4:7]
最小-最大规范化
from sklearn import preprocessing
preprocessing.minmax_scale(df)

(df - df.mean())/df.std()  
preprocessing.scale(df)
小数定标规范化
dp/10**np.ceil(np.log10(df.abs().max()))

连续属性离散化
分箱法binning : 等宽法，等频法
pd.cut(df.AGE, 5, labels = range(5)) 
pd.qcut(df.AGE, 5, labels = range(5)) 等频法

特征二值化 binarization
threshold
binarizer()
labelEncoder()
from sklearn.preprocessing import Binarizer
X = boston.target.reshape(-1, 1)
Binarizer(threshold = 20.0).fit_transform(X)

数据规约 data reduction
属性规约：向前选择，向后删除，决策树，PCA
数值规约：有参方法（回归法，对数线性模型） 无参法（直方图，聚类，抽样）
PCA 
from sklearn.decomposition import PCA
X = preprocessing.scale(boston.data)
pca = PCA(n_components='mle') # 自动选择保留的主成分个数
pca.fit(X)
pca.explained_varinance_ratio_
# 各自的方差百分比，方差贡献率

数值规约
import numpy as np
data = np.random.randint(1,10,50)
import matplotlib.pyplot as plt
plt.hist(data)
bins = np.linspace(data.min(), data.max(), 3, endpoint = True)
plt.hist(data, bins = bins, rwidth = 0.95, edgecolor = 'k')

随机抽样：不放回 
replace = True 放回
iris_df.sample(frac = 0.3,replace = True)#n = 10

kaggle官网获取数据集
kaggle可以跟着做一些项目
