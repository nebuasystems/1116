import numpy as np

l1 = [1, 2, 3, 4, 5, 'asd']
arr1 = np.array(l1)

print(arr1, arr1.ndim, arr1.dtype)

arr2 = np.array([10, 20, 30, 40, 50])
print(arr2, arr2.ndim, arr2.shape, arr2.dtype)

arr3 = np.array([10, 20, 3.14, 40, 50])
print(arr3, arr3.ndim, arr3.shape, arr3.dtype)