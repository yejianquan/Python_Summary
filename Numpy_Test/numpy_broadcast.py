import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
arr2 = np.array([0,1,2])
print(arr1+arr2)#每一行都加上了[0,1,2]
'''
[[ 1  3  5]
 [ 4  6  8]
 [ 7  9 11]
 [10 12 14]]
'''