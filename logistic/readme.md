### logistic 回归

Logistic 回归 或者叫逻辑回归 虽然名字有回归，但是它是用来做分类的。其主要思想是: 根据现有数据对分类边界线(Decision Boundary)建立回归公式，以此进行分类。



#### logistic 回归和线性回归的区别

logistic 回归和线性回归的区别是：线性回归是根据样本X各个维度的Xi的线性叠加（线性叠加的权重系数wi就是模型的参数）来得到预测值的Y，然后最小化所有的样本预测值Y与真实值y'的误差来求得模型参数。我们看到这里的模型的值Y是样本X各个维度的Xi的线性叠加，是线性的。

Y=WX (假设W>0),Y的大小是随着X各个维度的叠加和的大小线性增加的，如图（x为了方便取1维）：

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/1.jpg)


然后再来看看我们这里的logistic 回归模型，模型公式是：[main]，这里假设W>0,Y与X各维度叠加和（这里都是线性叠加W）的图形关系，如图（x为了方便取1维）：

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/2.jpg)



我们看到Y的值大小不是随X叠加和的大小线性的变化了，而是一种平滑的变化，这种变化在x的叠加和为0附近的时候变化的很快，而在很大很大或很小很小的时候，X叠加和再大或再小，Y值的变化几乎就已经很小了。当X各维度叠加和取无穷大的时候，Y趋近于1，当X各维度叠加和取无穷小的时候，Y趋近于0.


这种变量与因变量的变化形式就叫做logistic变化。（注意不是说X各个维度和为无穷大的时候，Y值就趋近1，这是在基于W>0的基础上，（如果W<0,n那么Y趋近于0）而W是根据样本训练出来，可能是大于0，也可能是小0，还可能W1>0，W2<0…所以这个w值是样本自动训练出来的，也因此不是说你只要x1，x2，x3…各个维度都很大，那么Y值就趋近于1，这是错误的。凭直觉想一下也不对，因为你连样本都还没训练，你的模型就有一个特点：X很大的时候Y就很大。这种强假设肯定是不对的。因为可能样本的特点是X很大的时候Y就很小。）


所以我们看到，在logistic回归中，X各维度叠加和（或X各维度）与Y不是线性关系，而是logistic关系。而在线性回归中，X各维度叠加和就是Y，也就是Y与X就是线性的了。

X各维度叠加和Y的关系不只是这一种，还可能是其他的比如：

![Image text](https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/3.jpg)


为什么变量与因变量要选用logistic关系呢，因为这里（1）我们需要Y代表的是概率即Y∈（0,1）。（2）我们需要X各维度叠加和在0附近变化幅度比较大，并且是非线性的变化。而在很大或很小的时候，几乎不变化，这是基于概率的一种认识与需要。感性的一个例子，想想你学习努力的程度与从60分提高到80分和80提高到100分并不是线性的。（3）这个关系的公式要在之后形成的cost function是凸函数。

所以就选择了logistic。


前面已经说了，我们使用logistic回归是用于二分类问题（y只有两个值A,B，也可以写成1和0，这都没关系），回归模型得到的结果不是预测样本X对应的y值（注意下，在logistic回归这里我们小写y表示某个样本Xi的类别，而大写Y或Y(Xi)表示logistic回归模型对某个样本Xi预测为1的概率。其实这里最好把Y用其他字母表示，以免混淆，但是已经这里写了，以后注意。），而是y=1的概率或y=0的概率。
我们假设y=1的概率公式是： <img width="150" src="https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/main1.jpg"/>，
那么y=0的概率就是 <img width="150" src="https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/main2.jpg"/>
。
（注意我们也可以y=0的概率公式为前面那一个，这里是任意的。这里不同的结果只是最终的W参数不同罢了。因为我们最终的W是训练出来的，不管怎么样，模型都会表现出样本的特点来。只是我们习惯了把Y(X)当成y=1的logistic模型映射的概率）


还要注意这里我们不是对一个Xi都要分别预测出来y=1的概率和y=0的概率。而是对于一个Xi，如果它的yi=1，那么我们就用 <img width="150" src="https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/main1.jpg"/>，
这个公式映射所对应的概率，如果对于一个Xi，如果它的yi=0，那么我们就用 <img width="150" src="https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/main2.jpg"/>，这个公式映射所对应的概率。都是根据yi的值映射出来一个概率。

因为我们的Y是概率，我们不能利用最小误差等，我们这里用的是极大化所有样本的对数似然函数： <img width="400" src="https://github.com/moveondo/python-MachineLearning/blob/master/logistic/image/main4.jpg"/>，。


yi表示的是Xi真实所属的类别（1或0）。L（W）就是cost function。这里的目标函数值和W有关系，也就是X各维度线性叠加的那些权重有关系。