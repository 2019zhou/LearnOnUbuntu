# 统计词频
poem_EN = 'Life can be good, Life can be sad, life is mostly cheerful, but sometimes sad'

poem_list = poem_EN.split()
p_dict = {}
for item in poem_list:
    if item[-1] in ',.\'"':
        item = item[:-1]
    p_dict[item] = p_dict.get(item, 0) + 1

# 根据数据排序输出

def func(stu_list):
    d = {}
    for item in stu_list:
        r = item.split('_')
        a, b = r[0], r[1].strip()  # strip函数处理尾部的换行符
        if a not in d:
            d[a] = [b]
        else:
            d[a] += [b]
    sorted(d.item(), key = lambda d: d[0])) # 基于key排序
    return list

if __name__ == '__main__':
    try:
        with open('file.txt') as f:
            stu_list = f.readlines()
    except FileNOtFoundError:
        print('the file does not exist')
    else:
        result = func(stu_list)
        for item in result:
            print(item[0], '->', item[1])

# 生成符合要求的学号
import random

def func(data):
    cls_no = random.choice(list(data.keys()))
    stu_no = random.randint(1, data[cls_no])
    return "{}{:02}".format(cls_no, stu_no)

if __name__ == '__main__':
    data = {"A001":32, "A002":47, "B001":39, "B002":42}
    result = set() # 创建集合，因为可能有重复
    while len(result) < 10:
        result.add(func(data)) # 在未满的前提下，不断加入集合
    print(result)

import numpy as np
X = np.ones((10, 10))
X = [1:-1, 1:-1] = 0 # 边界全部设为1，内部设为0
X = np.full((10, 10), pi) # 扩展性比较好
X = np.array([1,2,3],[4,5,6], dtype = np.float)
np.full_like(X, 4)
np.identity(10)
np.eye(8, k = -2)
np.random.normal(0, 5, 100) # 正太分布 期望，标准差， 采样100个
np.random.uniform(-5,5,100) # 均匀分布 边界值， 采样100个
A = np.random.rand(3,5)
mask = np.random.choice(np.arange(A.shape[0]), 2, replace = True) # 随机选择两行
A[mask]
X = np.arange(1, 101)
X <=50 #返回的结果是一个bool数组
X[X <= 50]
X[(X> 50) & (X%2 == 0)]
X[X%2==0] = -1 # 修改的是原始数组
where:  x if condition else y 
np.where(X %2 == 0, -1, X) # 不修改原始数组
scores = np.array([98, 76, 87],[76, 88, 91])
scores_mean = scores.mean(axis = 1) # 求均值
help(scores.mean) 
scores_mean = scoress.mean(axis = 1, keepdims = True)
scores - scores_mean #就可以相减了
