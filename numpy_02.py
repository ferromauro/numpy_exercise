import numpy as np
a = np.array([2,3,7,3,8,1,2,2,2,0],float)
np.mean(a)
# 3.0
np.median(a)
# 2.0
from scipy import stats
m_a = stats.mode(a)
print m_a[0]
# [ 2.]
np.var(a)
# 5.7999999999999998
np.std(a)
# 2.4083189157584592
b = np.unique(a)
print b
# [ 0.  1.  2.  3.  7.  8.]
np.mean(b)
# 3.5
np.median(b)
# 2.5
m_b = stats.mode(b)
print m_b[0]
# [ 0.]
np.var(b)
# 8.9166666666666661
np.std(b)
# 2.9860788111948193
