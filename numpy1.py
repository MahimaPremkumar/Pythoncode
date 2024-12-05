# pip virutal Environment
# virutalenv venv
# cd venv
# scripts\activate
# pip install numpy
# cd..

# import numpy as np
# a=[1,2,3,4,5]
# a=np.array([1,2,3,4,5])
# print(a)
# print(type(a))

# import numpy as np
# print(np.__version__)

# import numpy as np
# a = np.array((1,2,3,4,5))
# print(a)

# import numpy as np
# a=np.array(2)
# a1=np.array([1,2,3,4,5])
# a2=np.array([[1,2,3],[4,5,6]])
# a3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,1,2]]])
# print(a3.ndim)

# import numpy as np
# num=np.array([1,2,3,4],ndmin=3)
# print(num)
# print(num.ndim)

# import numpy as np
# num=np.array([[1,2,3,4,5]])
# num[0]=10
# print(num)

# import numpy as np
# num=np.array([[1,2,3],[7,8,9]])
# print(num[1,2])

# import numpy as np
# num=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,9,8]]])
# print(num[0, 1, 1])

# import numpy as np
# num=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,11,12]]])
# print(num[1,1,-3])

# import numpy as np
# num=np.array([14,15,16,17,18,19,20])
# print(num[::-2])

# import numpy as np
# sal=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(sal[0,1:4])
# print(sal[1,1:4])

# import numpy as np
# mal=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(mal[0:2, 2])

# import numpy as np
# pal=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(pal[0:2,1:4])

# import numpy as np
# fal=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(fal[0,1:4])
# print(fal[1,0:3])

# import numpy as ny
# jal=ny.array([[1,2,3,4,5],[6,7,8,9,0]])
# print(jal[1,-4:-1])

# import numpy as ny
# str=ny.array([1,2,3,4], dtype='S')
# print(str)
# print(str.dtype)

# import numpy as ny
# intr=ny.array([1,2,3,4])
# integer=intr.astype('f')
# print(intr)
# print(integer)
# print(integer.dtype)

# import numpy as np
# call=np.array([1,0,9])
# phone=call.astype(bool)
# print(phone)

# import numpy as np
# arr=np.array([[[1,2,3,4,5],[3,6,7,8,9]],[[11,12,13,14,15],[16,17,18,19,20]]])

# print(arr.shape)
# x=arr.view()
# y=arr.copy()

# print(arr)
# print(x.base)
# print(y.base)

# import numpy as np
# dim=np.array([1,2,3,4,5],ndmin=4)

# print(dim)
# print(dim.shape)

# import numpy as np
# arr=np.array([1,2,3,4,5,6,7,8,9,0,8,9])
# reshaped=arr.reshape(2,3,-1)
# print(reshaped)

# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# for x in arr:
#     for y in x:
#         print(y)

# import numpy as np
# op=np.array([1,2,3,4,5])
# for x in np.nditer(op):
#     print(x)

# import numpy as np
# sam=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# for a in sam:
#     for x in a:
#         for y in x:
#                 print(y)
# import numpy as np
# sam=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# for i in np.nditer(sam):
#      print(i)

# import numpy as np
# man = np.array([1, 2, 3])
# for i in np.nditer(man, flags=['buffered'], op_dtypes=['S']):
#     print(i)

# import numpy as np
# dam=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# for i in dam[::,: :2]:
#     print(i)

# import numpy as np
# arr=np.array([[1,2,3,4,5],[6,7,8,9,0]])
# for idx,x in np.ndenumerate(arr):
#     print(idx,x)

# import numpy as np
# arr1=np.array([1,2,3,4,5])
# arr2=np.array([6,7,8,9,0])
# arr=np.hstack((arr1,arr2))
# arrr=np.vstack((arr1,arr2))
# arre= np.dstack((arr1,arr2))
# print(arr)
# print(arrr)
# print(arre)

# import numpy as np
# arr1=np.array([[1,2,3,4],[7,4,5,6]])
# arr2=np.array([[1,2,3,0],[7,6,7,8]])
# arry=np.concatenate ((arr1,arr2), axis=1)
# s=np.stack((arr1,arr2),axis=2)
# print(arry)
# print(s) 

# import numpy as np
# n=np.array([1,2,3,4,5])
# s=np.array_split(n,3)
# arr1= n.max()
# print(arr1)

# from numpy import random
# ran_dom=random.randint(100, size=(2,2))
# print(ran_dom)

# from numpy import random
# ran_dom=random.rand(2,2)
# print(ran_dom)

# from numpy import random
# ran_dom=random.choice([1,2,3,4,5],size=(2,2))
# print(ran_dom)

# from numpy import random
# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(random.permutation(arr)

# import numpy as np
# arr= np.array([9,25,49])
# arr1=np.sqrt(arr)
# print(arr1)

# import numpy as np
# arr=np.array([45,55,60])
# arr1=np.lcm.reduce(arr)
# print(arr1)

# import numpy as np
# arr_5 = np.array([[1, 2], [3, 4]])
# arr_6 = np.array([[2, 4], [6, 9]])
# np.dot(arr_5,arr_6)
# print(arr_5,arr_6)


# arr_5 = np.array([[1, 2], [3, 4]])
# arr_6 = np.array([[2, 4], [6, 9]])
# print("arr_5\n", arr_5)
# print("arr_6\n", arr_6)
# num=np.dot(arr_5, arr_6)
# print(num)



