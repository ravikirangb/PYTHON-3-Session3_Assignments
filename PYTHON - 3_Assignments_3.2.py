# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 19:34:25 2018

@author: 1000091

Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists
['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xx', 'yy', 'zz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]]
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
"""

list1 = [char for char in 'ACADGILD']
list2 = [x*n for x in 'xyz' for n in [1,2,3,4]]
list3 = [x*n for n in [1,2,3,4] for x in 'xyz']
list4 = [[n1 + n2] for n1 in [0,1,2] for n2 in [2,3,4]]
list5 =  [[n, n + 1, n + 2, n + 3] for n in [2,3,4,5]]
list6 =  [(y, x) for x in [1,2,3] for y in [1,2,3]]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)