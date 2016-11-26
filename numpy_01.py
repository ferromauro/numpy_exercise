import numpy as np
a = np.ones((4,4), dtype = int)
b = np.identity(4, dtype = int)
c = a+b
print c
# [[2 1 1 1]
#  [1 2 1 1]
#  [1 1 2 1]
#  [1 1 1 2]]
d =  np.transpose(c)
e = d*c
f = c**2
print e==f
# array([[ True,  True,  True,  True],
#       [ True,  True,  True,  True],
#       [ True,  True,  True,  True],
#       [ True,  True,  True,  True]], dtype=bool)


