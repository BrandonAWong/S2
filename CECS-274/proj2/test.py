import numpy as np
e = np.zeros(3)
print(e)
e[1] = 1
print(e)
print((type(e[1])))
print(list(filter(lambda e: type(), e)))