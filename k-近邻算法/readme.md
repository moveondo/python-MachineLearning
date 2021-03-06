## k 近邻算法

KNN 通俗理解

>给定一个训练数据集，对新的输入实例，在训练数据集中找到与该实例最邻近的 k 个实例，这 k 个实例的多数属于某个类，就把该输入实例分为这个类。

### KNN 概述

k-近邻（kNN, k-NearestNeighbor）算法是一种基本分类与回归方法.

一句话总结：近朱者赤近墨者黑！

k 近邻算法的输入为实例的特征向量，对应于特征空间的点；输出为实例的类别，可以取多类。k 近邻算法假设给定一个训练数据集，其中的实例类别已定。分类时，对新的实例，根据其 k 个最近邻的训练实例的类别，通过多数表决等方式进行预测。因此，k近邻算法不具有显式的学习过程。

k 近邻算法实际上利用训练数据集对特征向量空间进行划分，并作为其分类的“模型”。 k值的选择、距离度量以及分类决策规则是k近邻算法的三个基本要素。


### KNN 原理

 * 假设有一个带有标签的样本数据集（训练样本集），其中包含每条数据与所属分类的对应关系。
 * 输入没有标签的新数据后，将新数据的每个特征与样本集中数据对应的特征进行比较。
   * 计算新数据与样本数据集中每条数据的距离。
   * 对求得的所有距离进行排序（从小到大，越小表示越相似）。
   * 取前 k （k 一般小于等于 20 ）个样本数据对应的分类标签。
 * 求 k 个数据中出现次数最多的分类标签作为新数据的分类。
 
KNN 开发流程

```
收集数据：任何方法
准备数据：距离计算所需要的数值，最好是结构化的数据格式
分析数据：任何方法
训练算法：此步骤不适用于 k-近邻算法
测试算法：计算错误率
使用算法：输入样本数据和结构化的输出结果，然后运行 k-近邻算法判断输入数据分类属于哪个分类，最后对计算出的分类执行后续处理

```


KNN 算法特点

```

优点：精度高、对异常值不敏感、无数据输入假定
缺点：计算复杂度高、空间复杂度高
适用数据范围：数值型和标称型

```

kNN 算法伪代码：

```
对于每一个在数据集中的数据点：
    计算目标的数据点（需要分类的数据点）与该数据点的距离
    将距离排序：从小到大
    选取前K个最短距离
    选取这K个中最多的分类类别
    返回该类别来作为目标数据点的预测值
    
```    

#### 归一化定义： 

归一化就是要把需要处理的数据经过处理后（通过某种算法）限制在需要的一定范围内。

 首先归一化是为了后面数据处理的方便，
 
 其次是保正程序运行时收敛加快。 
 
 方法有如下：

 * 线性函数转换，表达式如下：　　

   y=(x-MinValue)/(MaxValue-MinValue)　　

   说明：x、y分别为转换前、后的值，MaxValue、MinValue分别为样本的最大值和最小值。　　

 * 对数函数转换，表达式如下：　　

   y=log10(x)　　

    说明：以10为底的对数函数转换。

  * 反余切函数转换，表达式如下：

     y=arctan(x)*2/PI　




在统计学中，归一化的具体作用是归纳统一样本的统计分布性。归一化在0-1之间是统计的概率分布，归一化在-1--+1之间是统计的坐标分布。


### KNN 小结

KNN 是什么？定义： 监督学习？ 非监督学习？

KNN 是一个简单的无显示学习过程，非泛化学习的监督学习模型。在分类和回归中均有应用。

### 基本原理

简单来说： 通过距离度量来计算查询点（query point）与每个训练数据点的距离，然后选出与查询点（query point）相近的K个最邻点（K nearest neighbors），使用分类决策来选出对应的标签来作为该查询点的标签。

 ### KNN 三要素
 
 >K的取值

对查询点标签影响显著（效果拔群）。k值小的时候 近似误差小，估计误差大。 k值大 近似误差大，估计误差小。

如果选择较小的 k 值，就相当于用较小的邻域中的训练实例进行预测，“学习”的近似误差（approximation error）会减小，只有与输入实例较近的（相似的）训练实例才会对预测结果起作用。但缺点是“学习”的估计误差（estimation error）会增大，预测结果会对近邻的实例点非常敏感。如果邻近的实例点恰巧是噪声，预测就会出错。换句话说，k 值的减小就意味着整体模型变得复杂，容易发生过拟合。

如果选择较大的 k 值，就相当于用较大的邻域中的训练实例进行预测。其优点是可以减少学习的估计误差。但缺点是学习的近似误差会增大。这时与输入实例较远的（不相似的）训练实例也会对预测起作用，使预测发生错误。 k 值的增大就意味着整体的模型变得简单。

太大太小都不太好，可以用交叉验证（cross validation）来选取适合的k值。

近似误差和估计误差，请看这里：https://www.zhihu.com/question/60793482

>距离度量 Metric/Distance Measure

距离度量 通常为 欧式距离（Euclidean distance），还可以是 Minkowski 距离 或者 曼哈顿距离。也可以是 地理空间中的一些距离公式。（更多细节可以参看 sklearn 中 valid_metric 部分）

>分类决策 （decision rule）

分类决策 在 分类问题中 通常为通过少数服从多数 来选取票数最多的标签，在回归问题中通常为 K个最邻点的标签的平均值。

#### 算法：（sklearn 上有三种）

Brute Force 暴力计算/线性扫描

KD Tree 使用二叉树根据数据维度来平分参数空间。

Ball Tree 使用一系列的超球体来平分训练数据集。

树结构的算法都有建树和查询两个过程。Brute Force 没有建树的过程。

 *  算法特点：

优点： High Accuracy， No Assumption on data， not sensitive to outliers

缺点：时间和空间复杂度 高

适用范围： continuous values and nominal values

 * 相似同源产物：

radius neighbors 根据制定的半径来找寻邻点

 * 影响算法因素：

N 数据集样本数量(number of samples)， D 数据维度 (number of features)

总消耗：

Brute Force: O[DN^2]

此处考虑的是最蠢的方法：把所有训练的点之间的距离都算一遍。当然有更快的实现方式, 比如 O(ND + kN) 和 O(NDK) , 最快的是 O[DN] 。感兴趣的可以阅读这个链接： k-NN computational complexity

KD Tree: O[DN log(N)]

Ball Tree: O[DN log(N)] 跟 KD Tree 处于相同的数量级，虽然建树时间会比 KD Tree 久一点，但是在高结构的数据，甚至是高纬度的数据中，查询速度有很大的提升。

 * 查询所需消耗:

Brute Force: O[DN]

KD Tree: 当维度比较小的时候， 比如 D<20, O[Dlog(N)] 。相反，将会趋向于 O[DN]

Ball Tree: O[Dlog(N)]

当数据集比较小的时候，比如 N<30的时候，Brute Force 更有优势。

 * Intrinsic Dimensionality(本征维数) 和 Sparsity（稀疏度）

数据的 intrinsic dimensionality 是指数据所在的流形的维数 d < D , 在参数空间可以是线性或非线性的。稀疏度指的是数据填充参数空间的程度(这与“稀疏”矩阵中使用的概念不同, 数据矩阵可能没有零项, 但是从这个意义上来讲,它的结构 仍然是 "稀疏" 的)。

Brute Force 的查询时间不受影响。

对于 KD Tree 和 Ball Tree的查询时间, 较小本征维数且更稀疏的数据集的查询时间更快。KD Tree 的改善由于通过坐标轴来平分参数空间的自身特性 没有Ball Tree 显著。

 * k的取值 (k 个邻点)

Brute Force 的查询时间基本不受影响。

但是对于 KD Tree 和 Ball Tree , k越大，查询时间越慢。

k 在N的占比较大的时候，使用 Brute Force 比较好。

 * Number of Query Points （查询点数量， 即测试数据的数量）

查询点较少的时候用Brute Force。查询点较多的时候可以使用树结构算法。

 * 关于 sklearn 中模型的一些额外干货：

如果KD Tree，Ball Tree 和Brute Force 应用场景傻傻分不清楚，可以直接使用 含有algorithm='auto'的模组。 algorithm='auto' 自动为您选择最优算法。 有 regressor 和 classifier 可以来选择。

metric/distance measure 可以选择。 另外距离 可以通过weight 来加权。

 * leaf size 对KD Tree 和 Ball Tree 的影响

建树时间：leaf size 比较大的时候，建树时间也就快点。

查询时间： leaf size 太大太小都不太好。如果leaf size 趋向于 N（训练数据的样本数量），算法其实就是 brute force了。如果leaf size 太小了，趋向于1，那查询的时候 遍历树的时间就会大大增加。leaf size 建议的数值是 30，也就是默认值。

内存： leaf size 变大，存树结构的内存变小。

 * Nearest Centroid Classifier

分类决策是哪个标签的质心与测试点最近，就选哪个标签。

该模型假设在所有维度中方差相同。 是一个很好的base line。

 * 进阶版： Nearest Shrunken Centroid

可以通过shrink_threshold来设置。

作用： 可以移除某些影响分类的特征，例如移除噪音特征的影响
