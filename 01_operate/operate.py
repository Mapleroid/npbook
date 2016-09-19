import numpy as np

'''
    mathmatic operations

    operate on every item.
'''
# '-' operation
a = np.array([20,30,40,50])
b = np.arange(4)
c = a-b
print c


# '**' operation
d = b**2
print d


# sin
e = np.sin(a)
print e


# <
f = a<35
print f


# * vs dot
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])

C = A*B
D = np.dot(A,B)
print C
print D


# random array
g = np.random.random((2,3))
print g


# functions of ndarray instances
print g.sum()
print g.min()
print g.max()


# axis
h = np.arange(12).reshape(3,4)  #[ [0 1 2 3] 
                                #  [4 5 6 7]
                                #  [8 9 10 11] ]
print h.sum(axis=0) # [12 15 18 21]
print h.sum(axis=1) # [6 22 38]
