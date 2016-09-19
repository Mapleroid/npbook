from numpy import *

# create an array
a = array([2,3,4])

# print properties
print a             # [2 3 4]
print a.ndim        # 1
print a.shape       # (3L,)
print a.size        # 3
print a.dtype       # int32
print a.itemsize    # 4

b = array([[1.5,2.,3.],[4.,5.,6.]])
print b             # [[1.5 2. 3.] [4. 5. 6.] ]
print b.ndim        # 2
print b.shape       # (2L,3L)
print b.size        # 6
print b.dtype       # float64
print b.itemsize    # 8


# create 0s array
c = zeros((3,4))
print c

d = zeros((3,4),dtype=int32)
print d


# create 1s array
e = ones((3,4),dtype=int32)
print e

# create empty array
f = empty((3,4))
print f


# create range array
# (min,max,step)
g = arange(10,30,5)
print g


# reshape
h = arange(24).reshape(2,3,4)
print h
