## 基于概率论的分类方法：朴素贝叶斯

### 朴素贝叶斯 概述

贝叶斯分类是一类分类算法的总称，这类算法均以贝叶斯定理为基础，故统称为贝叶斯分类。
最后，通过实例来讨论贝叶斯分类的中最简单的一种: 朴素贝叶斯分类

### 为什么说naive Bayesian分类法是 naïve的？

朴素贝叶斯分类假定一个属性值对给定类的影响独立于其它属性的值。该假定称作类条件独立。做此假定是为了简化所需计算，并在此意义下称为“朴素的”。

贝叶斯分类假设特征之间相互独立。所谓 独立(independence)指的是统计意义上的独立，即一个特征或者单词出现的可能性与它和其他单词相邻没有关系，比如说，“我们”中的“我”和“们”出现的概率与这两个字相邻没有任何关系。
这个假设正是朴素贝叶斯分类器中 朴素(naive) 一词的含义。朴素贝叶斯分类器中的另一个假设是，每个特征同等重要。

Note: 朴素贝叶斯分类器通常有两种实现方式: 一种基于伯努利模型实现，一种基于多项式模型实现。这里采用前一种实现方式。该实现方式中并不考虑词在文档中出现的次数，只考虑出不出现，因此在这个意义上相当于假设词是等权重的。


### 贝叶斯决策理论的核心思想

  选择具有最高概率的决策
  
### 条件概率


条件概率是指事件A在另外一个事件B已经发生条件下的发生概率。

条件概率表示为：P（A|B），读作“在B的条件下A的概率”。

计算公式：P(A|B)=P(AB)/P(B);

### 朴素贝叶斯场景
 
 机器学习的一个重要应用就是文档的自动分类。

在文档分类中，整个文档（如一封电子邮件）是实例，而电子邮件中的某些元素则构成特征。我们可以观察文档中出现的词，并把每个词作为一个特征，而每个词的出现或者不出现作为该特征的值，这样得到的特征数目就会跟词汇表中的词的数目一样多。

朴素贝叶斯是上面介绍的贝叶斯分类器的一个扩展，是用于文档分类的常用算法。下面我们会进行一些朴素贝叶斯分类的实践项目。

### 朴素贝叶斯 原理

```

提取所有文档中的词条并进行去重
获取文档的所有类别
计算每个类别中的文档数目
对每篇训练文档: 
    对每个类别: 
        如果词条出现在文档中-->增加该词条的计数值（for循环或者矩阵相加）
        增加所有词条的计数值（此类别下词条总数）
对每个类别: 
    对每个词条: 
        将该词条的数目除以总词条数目得到的条件概率（P(词条|类别)）
返回该文档属于每个类别的条件概率（P(类别|文档的所有词条)）


```

### 朴素贝叶斯 开发流程

```
收集数据: 可以使用任何方法。
准备数据: 需要数值型或者布尔型数据。
分析数据: 有大量特征时，绘制特征作用不大，此时使用直方图效果更好。
训练算法: 计算不同的独立特征的条件概率。
测试算法: 计算错误率。
使用算法: 一个常见的朴素贝叶斯应用是文档分类。可以在任意的分类场景中使用朴素贝叶斯分类器，不一定非要是文本。

```

### 朴素贝叶斯 算法特点

```

优点: 在数据较少的情况下仍然有效，可以处理多类别问题。
缺点: 对于输入数据的准备方式较为敏感。
适用数据类型: 标称型数据。

```

### 两道考试题

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E8%B4%9D%E5%8F%B6%E6%96%AF/image/native.jpg)


![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/%E8%B4%9D%E5%8F%B6%E6%96%AF/image/native2.jpg)





















