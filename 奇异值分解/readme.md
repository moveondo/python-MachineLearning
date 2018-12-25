
### SVD详解

SVD(singular value decomposition)，翻译成中文就是奇异值分解。SVD的用处有很多，比如：LSA（隐性语义分析）、推荐系统、特征压缩（或称数据降维）。SVD可以理解为：将一个比较复杂的矩阵用更小更简单的3个子矩阵的相乘来表示，这3个小矩阵描述了大矩阵重要的特性。


![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/1.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/2.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/3.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/4.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/5.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/6.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/7.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/8.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/9.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/10.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/11.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/12.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/13.png)

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E5%A5%87%E5%BC%82%E5%80%BC%E5%88%86%E8%A7%A3/image/1.png)




### SVD应用于推荐系统

数据集中行代表用户user，列代表物品item，其中的值代表用户对物品的打分。基于SVD的优势在于：用户的评分数据是稀疏矩阵，可以用SVD将原始数据映射到低维空间中，然后计算物品item之间的相似度，可以节省计算资源。

整体思路：先找到用户没有评分的物品，然后再经过SVD“压缩”后的低维空间中，计算未评分物品与其他物品的相似性，得到一个预测打分，再对这些物品的评分从高到低进行排序，返回前N个物品推荐给用户。

 

具体代码如下，主要分为5部分：

第1部分：加载测试数据集；

第2部分：定义三种计算相似度的方法；

第3部分：通过计算奇异值平方和的百分比来确定将数据降到多少维才合适，返回需要降到的维度；

第4部分：在已经降维的数据中，基于SVD对用户未打分的物品进行评分预测，返回未打分物品的预测评分值；

第5部分：产生前N个评分值高的物品，返回物品编号以及预测评分值。

 

优势在于：用户的评分数据是稀疏矩阵，可以用SVD将数据映射到低维空间，然后计算低维空间中的item之间的相似度，对用户未评分的item进行评分预测，最后将预测评分高的item推荐给用户。
