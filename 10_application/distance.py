from numpy import *

A = array(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15]
        ]
    )

y = array([5, 6, 7, 8, 9])

B = tile(y, (A.shape[0], 1))

C = (A - B)**2

D = C.sum(axis=1)

E = D**0.5

def distances(y, X):
    return (((tile(y, (X.shape[0], 1)) - X)**2).sum(axis=1))**0.5

F = distances(y, A)

print A
print B
print C
print D
print E
print F