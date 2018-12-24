f =  open('5.txt', 'r')

print(f)

<.io.TextIOWrapper name='****'    mode='r'  encoding='cpp36'>

这其实不错错误，但是没有得到我们想要的结果，查找了一些，发现是文件的编码导致的



f =  open('5.txt', 'r', encoding='UTF-8')

print(f.read())



del(dataIndex[randIndex])

修改为：

把del那句改成del(list(dataIndex)[randIndex])