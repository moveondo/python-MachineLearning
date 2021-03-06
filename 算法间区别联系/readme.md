
### KNN VS K-means

K近邻法（knn）是一种基本的分类与回归方法。

k-means是一种简单而有效的聚类方法。

虽然两者用途不同、解决的问题不同，但是在算法上有很多相似性，于是将二者放在一起，这样能够更好地对比二者的异同。

二者的相同点:

- k的选择类似

- 思路类似：根据最近的样本来判断某个样本的属性

二者的不同点：

应用场景不同：前者是分类或者回归问题，后者是聚类问题;

算法复杂度： 前者O（n^2）,后者O（kmn）;（k是聚类类别数，m是聚类次数）

稳定性：前者稳定，后者不稳定。

 ![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E7%AE%97%E6%B3%95%E9%97%B4%E5%8C%BA%E5%88%AB%E8%81%94%E7%B3%BB/image/knnkmean.jpg)


### Apriori VS FP-growth


频繁项集：是经常出现在一块儿的物品的集合
关联规则：按时两种物品之间可能存在很强的关系。

支持度是针对项集来说的，因此可以定义一个最小支持度，而只保留满足最小值尺度的项集。

可信度或者是置信度是针对关联规则来定义的，我们的规则对其中多少的记录都适用

Apriori算法是发现频繁项集的一种方法，Apriori算法的两个输入参数分别是最小支持度和数据集，该算法首先会生成所有单个元素的项集列表。接着扫描数据集来查看哪些项集满足最小支持度要求，那些不满足最小支持度的集合会被去掉，然后，对剩下来的集合进行组合以生成包含两个元素的项集;
接下来，再重新扫描交易记录，去掉不满足最小支持度的项集。该过程重复进行直到所有项集都被去掉。

经典的关联规则挖掘算法包括Apriori算法和FP-growth算法。
apriori算法多次扫描交易数据库，每次利用候选频繁集产生频繁集；

而FP-growth则利用树形结构，无需产生候选频繁集而是直接得到频繁集，大大减少扫描交易数据库的次数，从而提高了算法的效率。
但是apriori的算法扩展性较好，可以用于并行计算等领域。

使用Apriori算法进行关联分析。FP-growth算法来高效发现频繁项集。



### LR和SVM的联系与区别？

@朝阳在望，联系： 
1、LR和SVM都可以处理分类问题，且一般都用于处理线性二分类问题（在改进的情况下可以处理多分类问题） 

2、两个方法都可以增加不同的正则化项，如L1、L2等等。所以在很多实验中，两种算法的结果是很接近的。 

区别： 

1、LR是参数模型，SVM是非参数模型。 

2、从目标函数来看，区别在于逻辑回归采用的是Logistical Loss，SVM采用的是hinge loss.这两个损失函数的目的都是增加对分类影响较大的数据点的权重，减少与分类关系较小的数据点的权重。 

3、SVM的处理方法是只考虑Support Vectors，也就是和分类最相关的少数点，去学习分类器。而逻辑回归通过非线性映射，大大减小了离分类平面较远的点的权重，相对提升了与分类最相关的数据点的权重。 

4、逻辑回归相对来说模型更简单，好理解，特别是大规模线性分类时比较方便。而SVM的理解和优化相对来说复杂一些，SVM转化为对偶问题后,分类只需要计算与少数几个支持向量的距离,这个在进行复杂核函数计算时优势很明显,能够大大简化模型和计算。 

5、Logic 能做的 SVM能做，但可能在准确率上有问题，SVM能做的Logic有的做不了。




### LR与线性回归的区别与联系？

个人感觉逻辑回归和线性回归首先都是广义的线性回归， 

其次经典线性模型的优化目标函数是最小二乘，而逻辑回归则是似然函数， 

另外线性回归在整个实数域范围内进行预测，敏感度一致，而分类范围，需要在[0,1]。逻辑回归就是一种减小预测范围，将预测值限定为[0,1]间的一种回归模型，因而对于这类问题来说，逻辑回归的鲁棒性比线性回归的要好。 

@乖乖癞皮狗：逻辑回归的模型本质上是一个线性回归模型，逻辑回归都是以线性回归为理论支持的。但线性回归模型无法做到sigmoid的非线性形式，sigmoid可以轻松处理0/1分类问题。




### Q:在k-means或kNN，我们是用欧氏距离来计算最近的邻居之间的距离。为什么不用曼哈顿距离？

曼哈顿距离只计算水平或垂直距离，有维度的限制。

另一方面，欧氏距离可用于任何空间的距离计算问题。因为，数据点可以存在于任何空间，欧氏距离是更可行的选择。例如：想象一下国际象棋棋盘，象或车所做的移动是由曼哈顿距离计算的，因为它们是在各自的水平和垂直方向做的运动。




1.训练决策树时的参数是什么？

* 1.criterion gini(基尼系数) or entropy(信息熵)  

* 2.splitter best or random 前者是在所有特征中找最好的切分点 后者是在部分特征中（数据量大的时候）

* 3.max_features None（所有），log2，sqrt，N 特征小于50的时候一般使用所有的

* 4.max_depth 数据少或者特征少的时候可以不管这个值，如果模型样本量多，特征也多的情况下，可以尝试限制下

* 5.min_samples_split 如果某节点的样本数少于min_samples_split，则不会继续再尝试选择最优特征来进行划分如果样本量不大，不需要管这个值。如果样本量数量级非常大，则推荐增大这个值。

* 6.min_samples_leaf 这个值限制了叶子节点最少的样本数，如果某叶子节点样本数目小于min_samples_leaf，则会和兄弟节点一起被剪枝，如果样本量不大，不需要管这个值，大些如10W可是尝试下5

* 7.min_weight_fraction_leaf 这个值限制了叶子节点所有样本权重和的最小值，如果小于这个值，则会和兄弟节点一起被剪枝默认是0，就是不考虑权重问题。一般来说，如果我们有较多样本有缺失值，或者分类树样本的分布类别偏差很大，就会引入样本权重，这时我们就要注意这个值了。

* 8.max_leaf_nodes 通过限制最大叶子节点数，可以防止过拟合，默认是"None”，即不限制最大的叶子节点数。如果加了限制，算法会建立在最大叶子节点数内最优的决策树。如果特征不多，可以不考虑这个值，但是如果特征分成多的话，可以加以限制具体的值可以通过交叉验证得到。

* 9.class_weight 指定样本各类别的的权重，主要是为了防止训练集某些类别的样本过多导致训练的决策树过于偏向这些类别。这里可以自己指定各个样本的权重如果使用“balanced”，则算法会自己计算权重，样本量少的类别所对应的样本权重会高。

* 10.min_impurity_split 这个值限制了决策树的增长，如果某节点的不纯度(基尼系数，信息增益，均方差，绝对差)小于这个阈值则该节点不再生成子节点。即为叶子节点 。

 

2.在决策树的节点处分割的标准是什么？



3.基尼系数的公式是什么？

G=A/(A+B）

赫希曼根据洛伦茨曲线提出的判断分配平等程度的指标。设实际收入分配曲线和收入分配绝对平等曲线之间的面积为A，实际收入分配曲线右下方的面积为B。并以A除以（A+B）的商表示不平等程度。这个数值被称为基尼系数或称洛伦茨系数。如果A为零，基尼系数为零，表示收入分配完全平等；如果B为零则系数为1，收入分配绝对不平等。
收入分配越是趋向平等，洛伦茨曲线的弧度越小，基尼系数也越小，反之，收入分配越是趋向不平等，洛伦茨曲线的弧度越大，那么基尼系数也越大。另外，可以参看帕累托指数(是指对收入分布不均衡的程度的度量）。



4.熵的公式是什么？

计算公式

H(x) = E[I(xi)] = E[ log(2,1/p(xi)) ] = -∑p(xi)log(2,p(xi)) (i=1,2,..n)

其中，x表示随机变量，与之相对应的是所有可能输出的集合，定义为符号集,随机变量的输出用x表示。P(x)表示输出概率函数。变量的不确定性越大，熵也就越大，把它搞清楚所需要的信息量也就越大.



5.决策树如何决定在哪个特征处分割？



  那么熵如何影响决策树绘制边界呢？

  这里涉及到一个新的词汇：信息增益

  信息增益定义为：父项熵-加权平均值（分割父项熵后生成的子项熵）

  决策树算法会最大程度的提高信息增益，他通过这种算法来选择进行分割的特征。如果特征有多个可获取的不同值，决策树会通过尽可能提高信息增益的办法决定在何处分割





6.你如何用数学计算收集来的信息？你确定吗？

7.随机森林的优点有哪些？

8.介绍一下boosting算法。

9.gradient boosting如何工作？

10.关于AdaBoost算法，你了解多少？它如何工作？

11.SVM中用到了哪些核？SVM中的优化技术有哪些？

12.SVM如何学习超平面？用数学方法详细解释一下。

13.介绍一下无监督学习，算法有哪些？

14.在K-Means聚类算法中，如何定义K？

法1：(轮廓系数)在实际应用中，由于Kmean一般作为数据预处理，或者用于辅助分聚类贴标签。所以k一般不会设置很大。可以通过枚举，令k从2到一个固定值如10，在每个k值上重复运行数次kmeans(避免局部最优解)，并计算当前k的平均轮廓系数，最后选取轮廓系数最大的值对应的k作为最终的集群数目


15.告诉我至少3中定义K的方法。


8. 什么是数据标准化，为什么要进行数据标准化？

我认为这个问题需要重视。数据标准化是预处理步骤，将数据标准化到一个特定的范围能够在反向传播中保证更好的收敛。
一般来说，是将该值将去平均值后再除以标准差。如果不进行数据标准化，有些特征（值很大）将会对损失函数影响更大（就算这个特别大的特征只是改变了1%，但是他对损失函数的影响还是很大，并会使得其他值比较小的特征变得不重要了）。
因此数据标准化可以使得每个特征的重要性更加均衡。


9. 解释什么是降维，在哪里会用到降维，它的好处是什么？

降维是指通过保留一些比较重要的特征，去除一些冗余的特征，减少数据特征的维度。而特征的重要性取决于该特征能够表达多少数据集的信息，也取决于使用什么方法进行降维。
而使用哪种降维方法则是通过反复的试验和每种方法在该数据集上的效果。一般情况会先使用线性的降维方法再使用非线性的降维方法，通过结果去判断哪种方法比较合适。而降维的好处是：

（1）节省存储空间；

（2）加速计算速度（比如在机器学习算法中），维度越少，计算量越少，并且能够使用那些不适合于高维度的算法；

（3）去除一些冗余的特征，比如降维后使得数据不会既保存平方米和平方英里的表示地形大小的特征；

（4）将数据维度降到2维或者3维使之能可视化，便于观察和挖掘信息。

（5）特征太多或者太复杂会使得模型过拟合。

10. 如何处理缺失值数据？

数据中可能会有缺失值，处理的方法有两种，一种是删除整行或者整列的数据，另一种则是使用其他值去填充这些缺失值。
在Pandas库，有两种很有用的函数用于处理缺失值：isnull()和dropna()函数能帮助我们找到数据中的缺失值并且删除它们。如果你想用其他值去填充这些缺失值，则可以是用fillna()函数。

12. 你会如何进行探索性数据分析(EDA)？

EDA的目的是去挖掘数据的一些重要信息。一般情况下会从粗到细的方式进行EDA探索。一开始我们可以去探索一些全局性的信息。观察一些不平衡的数据，计算一下各个类的方差和均值。
看一下前几行数据的信息，包含什么特征等信息。使用Pandas中的df.info()去了解哪些特征是连续的，离散的，它们的类型(int、float、string)。接下来，删除一些不需要的列，这些列就是那些在分析和预测的过程中没有什么用的。


比如：某些列的值很多都是相同的，或者这些列有很多缺失值。当然你也可以去用一些中位数等去填充这些缺失值。
然后我们可以去做一些可视化。对于一些类别特征或者值比较少的可以使用条形图。类标和样本数的条形图。找到一些最一般的特征。
对一些特征和类别的关系进行可视化去获得一些基本的信息。然后还可以可视化两个特征或三个特征之间的关系，探索特征之间的联系。


你也可以使用PCA去了解哪些特征更加重要。组合特征去探索他们的关系，比如当A=0，B=0的类别是什么，A=1，B=0呢？比较特征的不同值，比如性别特征有男女两个取值，我们可以看下男和女两种取值的样本类标会不会不一样。


另外，除了条形图、散点图等基本的画图方式外，也可以使用PDF\CDF或者覆盖图等。观察一些统计数据比如数据分布、p值等。这些分析后，最后就可以开始建模了。


一开始可以使用一些比较简单的模型比如贝叶斯模型和逻辑斯谛回归模型。如果你发现你的数据是高度非线性的，你可以使用多项式回归、决策树或者SVM等。特征选择则可以基于这些特征在EDA过程中分析的重要性。如果你的数据量很大的话也可以使用神经网络。然后观察ROC曲线、查全率和查准率。


14. 在图像处理中为什么要使用卷积神经网络而不是全连接网络？

这个问题是我在面试一些视觉公司的时候遇到的。答案可以分为两个方面：首先，卷积过程是考虑到图像的局部特征，能够更加准确的抽取空间特征。
如果使用全连接的话，我们可能会考虑到很多不相关的信息。其次，CNN有平移不变性，因为权值共享，图像平移了，卷积核还是可以识别出来，但是全连接则做不到

15. 是什么使得CNN具有平移不变性？

正如上面解释，每个卷积核都是一个特征探测器。所以就像我们在侦查一样东西的时候，不管物体在图像的哪个位置都能识别该物体。
因为在卷积过程，我们使用卷积核在整张图片上进行滑动卷积，所以CNN具有平移不变性。

19. 为什么卷积核一般都是3*3而不是更大？

这个问题在VGGNet模型中很好的解释了。主要有这2点原因：第一，相对于用较大的卷积核，使用多个较小的卷积核可以获得相同的感受野和能获得更多的特征信息，同时使用小的卷积核参数更少，计算量更小。
第二：你可以使用更多的激活函数，有更多的非线性，使得在你的CNN模型中的判决函数有更有判决性。


1、L1范式和L2方式的区别

（1）L1范式是对应参数向量绝对值之和

（2）L1范式具有稀疏性

（3）L1范式可以用来作为特征选择，并且可解释性较强（这里的原理是在实际Loss function中都需要求最小值，根据L1的定义可知L1最小值只有0，故可以通过这种方式来进行特征选择）

（4）L2范式是对应参数向量的平方和，再求平方根

（5）L2范式是为了防止机器学习的过拟合，提升模型的泛化能力

2、优化算法及其优缺点

在回答面试官的问题的时候，往往将问题往大的方面去回答，这样不会陷于小的技术上死磕，最后很容易把自己嗑死了。

（1）随即梯度下降

优点：可以一定程度上解决局部最优解的问题

缺点：收敛速度较慢

（2）批量梯度下降

优点：容易陷入局部最优解

缺点：收敛速度较快

（3）mini_batch梯度下降

综合随即梯度下降和批量梯度下降的优缺点，提取的一个中和的方法。

（4）牛顿法

牛顿法在迭代的时候，需要计算Hessian矩阵，当维度较高的时候，计算Hessian矩阵比较困难。

（5）拟牛顿法

拟牛顿法是为了改进牛顿法在迭代过程中，计算Hessian矩阵而提取的算法，它采用的方式是通过逼近Hessian的方式来进行求解。

（6）共轭梯度

（7）启发式的优化算法

启发式的优化算法有遗传算法，粒子群算法等。这类算法的主要思想就是设定一个目标函数，每次迭代根据相应的策略优化种群。直到满足什么样的条件为止。

3、RF与GBDT之间的区别

（1）相同点

* 都是由多棵树组成
* 最终的结果都是由多棵树一起决定

（2）不同点

* 组成随机森林的树可以分类树也可以是回归树，而GBDT只由回归树组成
* 组成随机森林的树可以并行生成，而GBDT是串行生成
* 随机森林的结果是多数表决表决的，而GBDT则是多棵树累加之和
* 随机森林对异常值不敏感，而GBDT对异常值比较敏感
* 随机森林是通过减少模型的方差来提高性能，而GBDT是减少模型的偏差来提高性能的
* 随机森林不需要进行数据预处理，即特征归一化。而GBDT则需要进行特征归一化

（3）RF：

优点：

* 易于理解，易于可视化
* 不需要太多的数据预处理，即数据归一化
* 不易过拟合
* 易于并行化

　　缺点：　　

* 不适合小样本数据，只适合大样本数据
* 大多数情况下，RF的精度低于GBDT
* 适合决策边界的是矩阵，不适合对角线型

（4）GBDT

优点：

* 精度高

　　缺点：

* 参数较多，容易过拟合
* 不易并行化

5、SVM与树模型之间的区别

（1）SVM

* SVM是通过核函数将样本映射到高纬空间，再通过线性的SVM方式求解分界面进行分类。
* 对缺失值比较敏感
* 可以解决高纬度的问题
* 可以避免局部极小值的问题
* 可以解决小样本机器学习的问题　　

（2）树模型

* 可以解决大样本的问题
* 易于理解和解释
* 会陷入局部最优解
* 易过拟合

6、梯度消失和梯度膨胀

（1）梯度消失：

* 根据链式法则，如果每一层神经元对上一层的输出的偏导乘上权重结果都小于1的话，那么即使这个结果是0.99，在经过足够多层传播之后，误差对输入层的偏导会趋于0
* 可以采用ReLU激活函数有效的解决梯度消失的情况

（2）梯度膨胀

* 根据链式法则，如果每一层神经元对上一层的输出的偏导乘上权重结果都大于1的话，在经过足够多层传播之后，误差对输入层的偏导会趋于无穷大
* 可以通过激活函数来解决



一、算法理论

Q1: 什么是偏倚（bias）、方差（variable）均衡？

偏倚指的是模型预测值与真实值的差异，是由使用的学习算法的某些错误或过于简单的假设造成的误差。它会导致模型欠拟合，很难有高的预测准确率。 
方差指的是不同训练数据训练的模型的预测值之间的差异，它是由于使用的算法模型过于复杂，导致对训练数据的变化十分敏感，这样会导致模型过拟合，使得模型带入了过多的噪音。 
任何算法的学习误差都可以分解成偏倚、方差和噪音导致的固定误差。模型越复杂，会降低偏倚增加方差。为了降低整体的误差，我们需要对偏倚方差均衡，使得模型中不会由高偏倚或高方差。

Q2：监督学习和非监督学习有什么不同？

监督学习需要具有标签（label）的训练数据，比如做分类，你需要先对训练数据做标记，然后才能训练模型将数据分成你说需要的标记类。 
而非监督学习则不需要。

Q3: KNN和k-means聚类由什么不同？

k-Nearest Neighbors 是一种监督学习算法，而k-means 是非监督的。这两种算法看起来很相似，都需要计算样本之间的距离。knn算法需要事先已有标注好的数据，当你需要对未标注的数据进行分类时，统计它附近最近的k个样本，将其划分为样本数最多的类别中。k-means聚类只需要一些未分类的数据点和阀值，算法会逐渐将样本点进行分成族类。

Q4：解释一下ROC曲线的原理 


ROC曲线是真正率和假正率在不同的阀值下之间的图形表示关系。通常用作权衡模型的敏感度与模型对一个错误分类报警的概率。
 
真正率表示：表示正的样本被预测为正占所有正样本的比例。 

假正率表示：表示负的样本被预测为正占所有负样本的比例。 

（0，0）点表示所有样本都被预测为负，此时阀值很大。 
（1，1）点表示所有样本都被预测为正，此时阀值很小。

Q5：定义一下prediction准确率、recall召回率

召回率就是Q4中的真正率。 

准确率指的是：正样本被预测为正所占所有预测为正样本数的比例
```
-	预测正	预测负
真实正	TP	FN
真实负	FP	TN
recall：TPTP+FN precision: TPTP+FP
```

Q6: 什么是贝叶斯定理，它是如何使用在机器学习中的？

贝叶斯定理会根据一件事发生的先验知识告诉你它后验概率。数学上，它表示为：一个条件样本发生的真正率占真正率和假正率之和的比例，即： P(A|B)=P(B|A)P(A)P(B)

举个例子： 已知某疾病的患病概率为5%，现用某检验方法进行诊断，若患有该病，则有90%的几率检验结果呈阳性。但即使正常人使用该检验方法，也有10%的几率误诊而呈阳性。某人检验结果为阳性，求此人患病的概率。 
P(患病|阳性)=P(阳性|患病)∗P(患病)P(阳性)=90%∗5%90%∗5%+10%∗95%=32%

贝叶斯定理使一些机器学习算法如：朴素贝叶斯等的理论基础。

Q7：为什么我们要称“朴素“贝叶斯？

因为我们在用到它的时候，有一个很强的假设，现实数据中几乎不会出现的：我们假设特征之间是相互独立，也就是我们计算条件概率时可以简化成它的组件的条件概率乘积。

Q8：L1、L2正则之间有什么不同？

L2正则 对应的是加入2范数，使得对权重进行衰减，从而达到惩罚损失函数的目的，防止模型过拟合。保留显著减小损失函数方向上的权重，而对于那些对函数值影响不大的权重使其衰减接近于0。相当于加入一个gaussian prior。 

L1正则 对应得失加入1范数，同样可以防止过拟合。它会产生更稀疏的解，即会使得部分权重变为0，达到特征选择的效果。相当于加入了一个laplacean prior。

Q9：你最喜欢的算法是什么？把它解释一下。

这里我比较想说的是SVM，因为它的数学理论让我觉得很有意思，而且应用广泛，效果不错。先从线性可分讲起，然后是最大间隔原理。什么是支持向量？如何进行常数估计。转化成优化问题，对偶问题，kkt条件，拉格朗日方法求最值等。然后是非线性可分情况，软间隔，进行坐标变化。引入核函数。常见的：多项式核函数、指数核函数、高斯核函数。

Q10：第一类误差和第二类误差有什么区别？

第一类误差指的是假正率，第二类指的是假负率。简单来说，第一类误差意味着假设为真的情况下，作出了拒绝原假设的一种错误推断。第二类误差意味着假设为假的情况下，做出了接受原假设的一种错误判断。 
举个例子：第一类误差，你告诉一个男的他怀孕了。第二类误差，你告诉一个已经怀孕的女子，她没怀孕。

Q11：什么是傅立叶变换？

傅立叶变换指：一个满足某些条件的函数可以表示成三角函数或他们的积分形式的线性组合。

Q12：概率和似然有什么区别？

概率和似然都是指可能性，但在统计学中，概率和似然有截然不同的用法。概率描述了已知参数时的随机变量的输出结果；似然则用来描述已知随机变量输出结果时，未知参数的可能取值。例如，对于“一枚正反对称的硬币上抛十次”这种事件，我们可以问硬币落地时十次都是正面向上的“概率”是多少；而对于“一枚硬币上抛十次，我们则可以问，这枚硬币正反面对称的“似然”程度是多少。 
概率(密度)表达给定θ下样本随机向量X=x的可能性，而似然表达了给定样本X=x下参数θ1(相对于另外的参数θ2)为真实值的可能性。我们总是对随机变量的取值谈概率，而在非贝叶斯统计的角度下，参数是一个实数而非随机变量，所以我们一般不谈一个参数的概率，而说似然。

Q13：什么是深度学习，它与机器学习算法之间有什么联系？

深度学习是机器学习的一个子领域，它关心的是参照神经学科的理论构建神经网络，使用反向传播对大量未标注或半结构化的数据进行建模。从这个角度看，深度学习可以看成一种非监督学习算法，通过使用神经网络学习数据的表示。

Q14：生成模型与判别模型有什么区别？

* 生成模型会学习数据的分布；判别模型学习的是不同类型数据之间的区别，不学习数据内部特点。在分类问题上，判别模型会优于生成模型。 
* 判别模型求解的思路是：条件分布——>模型参数后验概率最大——->（似然函数\cdot 参数先验）最大——->最大似然 
* 生成模型的求解思路是：联合分布——->求解类别先验概率和类别条件概率 
* 常见的生成方法有混合高斯模型、朴素贝叶斯法和隐形马尔科夫模型等，常见的判别方法有SVM、LR等

Q15：交叉检验如何用在时间序列数据上？

与标准的k-folds 交叉检验不同，数据不是随机分布的，而是具有时序性的。如果模式出现在后期，模型仍然需要选择先前时间的数据，尽管前期对模式无影响。我们可以如下这么做：

``` 
fold1：training[1], test[2] 
fold2：training[1 2], test[3] 
fold3：training[1 2 3], test[4] 
fold4：training[1 2 3 4], test[5] 
fold5：training[1 2 3 4 5], test[6]
``` 

Q16：如何对决策树进行剪枝？

剪枝是决策树发生过拟合后，为了降低模型复杂度，提高模型准确率的一种做法。可以分为自上而下和自下而上两种。常见的方法有：误差降低剪枝（REP）和代价复杂度剪枝（CCP）。 
REP简单的来说就是对树的每一个结点进行剪枝，如果剪掉某个结点不会降低模型准确率，那么将其剪掉。这种启发式的做法实际上就是为了最大化准确率。

Q17：模型的精度和模型的性能哪个对你更重要？

许多机器学习的模型会有高的精度，但是预测能力也就是泛化能力较低，如何去理解它们呢？ 

精度只是模型性能的一部分，有可能是会产生误导的那个。对于具有倾斜的数据集，比如要从大量的金融数据中识别出少量的诈骗数据，一个精度高的模型可能会告诉你没有诈骗，然而这样的模型预测是没有意义的。所以，不要总是把精度当作模型最重要的事。

Q18：什么是F1数，怎么使用它？

F1数是衡量模型性能的一个指标。它是模型精准率和召回率的加权平均，1表示最好，0表示最差。在分类问题中有时精准率和召回率不会同时都高，那么我们可以使用F1数。

Q19：如何处理一个不平衡的数据集？

不平衡的数据集：比如二分类问题中，一类数据有90%，而另一类只有10%。我们可以轻易的得到90%准确率的模型，但是它对第二类的预测值为0。那么我们需要对这样的数据进行处理：

* 收集更多的数据，使其达到平衡
* 使用重复采样
* 使用不同的算法
* 重要的是：你注意到了数据的不平衡导致的问题，以及如何去解决它们。

Q20：什么时候你应该使用分类而不是回归？

分类会产生离散的数值，使得数据严格的分为不同类。回归会得到连续的值，使你更好的区分独立点之间的区别。当你需要知道你的数据明确的属于那些类时你可以用分类。

Q21：举个例子，说明使用集成学习会很有用。

* 集成学习通过组合一些基学习算法来优化得到更好的预测性能，通常可以防止模型的过拟合使模型更具有鲁棒性。 
* 你可以列举一些集成学习的例子，如bagging、boosting、stacking等，并且了解他们是如何增加模型预测能力的。

Q22：你如何确保你的模型没有过拟合？

过度拟合的训练数据以及数据携带的噪音，对于测试数据会带来不确定的推测。有如下三种方法避免过拟合：

* 保持模型尽可能地简单：通过考量较少的变量和参数来减少方差，达到数据中消除部分噪音的效果。
* 使用交叉检验的手段如：k-folds cross-validation。
* 使用正则化的技术如：LASSO方法来惩罚模型中可能导致过拟合的参数。

Q23：如何评估你的机器学习模型的有效性？

首先你需要将数据分成训练集和测试集,或者使用给交叉验证方法分割。然后你需要选择度量模型表现的metrics，如F1数、准确率、混淆矩阵等。更重要的是，根据实际情况你需要理解模型度量的轻微差别，以便于选择正确的度量标准。

Q24：如何评估一个LR model？

Q23的一个子问题。首先你需要知道LR的目标是什么？（分类或预测）然后通过举一些例子来说明。

Q25：什么是核技巧，有什么用处？

核技巧使用核函数，确保在高维空间不需要明确计算点的坐标，而是计算数据的特征空间中的内积。这使其具有一个很有用的属性：更容易的计算高维空间中点的坐标。许多算法都可以表示称这样的内积形式，使用核技巧可以保证低维数据在高维空间中运用算法进行计算。




参考链接： http://www.aboutyun.com/thread-23847-1-1.html

https://blog.csdn.net/wyisfish/article/details/79167271


