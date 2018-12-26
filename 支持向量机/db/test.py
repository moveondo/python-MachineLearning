import numpy as np

a1 = np.array([[1, 2], [3, 4]])
b1 = np.mat([[1, 2], [3, 4]])

a2 = np.array(([1, 2], [3, 4]))
b2 = np.mat(([1, 2], [3, 4]))

a3 = np.array(((1, 2), (3, 4)))
b3 = np.mat(((1, 2), (3, 4)))

b4 = np.mat('1 2; 3 4')

#print("\n", a1, "\n,,,,", b1, "\n,,,,", a2, "\n", b2, "\n", a3, "\n", b3, "\n", b4)



arr = np.arange(9).reshape((3,3))#生成一个3行3列的数组
# print(arr)
#
# print(arr.T)


arr1 = np.arange(24).reshape(2,3,4)#生成一个2*3*4的数组
print (arr1)
print (arr1.shape)
print(arr1.transpose((1,0,2)))

