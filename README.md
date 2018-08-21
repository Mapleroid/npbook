# npbook
Samples to learn Numpy




## 10. 应用


### distance

有 x = (x0, x1, x2, ..., xn),

y = (y0, y1, y2, ..., yn).

令 distance = sqrt((x0-y0)**2 + (x1-y1)**2 + ... + (xn-yn)**2).

有 A = [ [x00, x01, ..., x0n],

        [x10, x11, ..., x1n],

        ...,

        [xm0, xm1, ..., xmn] ],
   
   y = [ y0, y1, ..., yn],

   求y与A中各元素的距离.

解：

令 B = [ [y0, y1, ..., yn],

        [y0, y1, ..., yn],

        ...

        [y0,y1, ..., yn] ],  (第m行)

   C = (A-B)**2

   D = [ sum(C00, C01, C02, ..., C0n),

        sum(C10, C11, C12, ..., C1n),

        ...,

        sum(Cm0, Cm1, Cm2, ..., Cmn)].

        (求和使用.sum(axis=1))

   E = D**0.5


示例：

A = [ [1 2 3 4 5],

    [6 7 8 9 10],

    [11 12 13 14 15] ]

y = [5 6 7 8 9]

distances = (((tile(y, (X.shape[0], 1)) - X)**2).sum(axis=1))**0.5


参考：
http://blog.csdn.net/sunny2038/article/details/9002531
