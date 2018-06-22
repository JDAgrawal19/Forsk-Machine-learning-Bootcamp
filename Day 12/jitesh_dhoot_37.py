# -*- coding: utf-8 -*-
"""
Created on Fri May 25 10:17:49 2018

@author: JITESH
"""

import numpy as np
import matplotlib.pyplot as plt


incomes=np.random.normal(100.0,20.0,10000)

print incomes

plt.hist(incomes,50)
plt.show()


mean=np.mean(incomes)
print mean

median=np.median(incomes)
print median


#add outlier


incomes=np.append(incomes,[100000])

mean1=np.mean(incomes)
print mean1

median1=np.median(incomes)
print median1 