### set

python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.

sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。



下面来点简单的小例子说明把。

>>> x = set('spam')
>>> y = set(['h','a','m'])
>>> x, y
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))

再来些小应用。

>>> x & y # 交集
set(['a', 'm'])

>>> x | y # 并集
set(['a', 'p', 's', 'h', 'm'])

>>> x - y # 差集
set(['p', 's'])


### Python [0] * n

list * int 意思是将数组重复 int 次并依次连接形成一个新数组

### 为什么要用numpy

Python中提供了list容器，可以当作数组使用。但列表中的元素可以是任何对象，因此列表中保存的是对象的指针，这样一来，为了保存一个简单的列表[1,2,3]。就需要三个指针和三个整数对象。对于数值运算来说，这种结构显然不够高效。
Python虽然也提供了array模块，但其只支持一维数组，不支持多维数组，也没有各种运算函数。因而不适合数值运算。
NumPy的出现弥补了这些不足。


```
## 常规创建方法
a = np.array([2,3,4])
b = np.array([2.0,3.0,4.0])
c = np.array([[1.0,2.0],[3.0,4.0]])
d = np.array([[1,2],[3,4]],dtype=complex) # 指定数据类型
print a, a.dtype
print b, b.dtype
print c, c.dtype
print d, d.dtype


[2 3 4] int32
[ 2.  3.  4.] float64
[[ 1.  2.]
 [ 3.  4.]] float64
[[ 1.+0.j  2.+0.j]
 [ 3.+0.j  4.+0.j]] complex128


```
