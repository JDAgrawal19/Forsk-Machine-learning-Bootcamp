# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:41:20 2018

@author: JITESH
"""

import numpy as np 
import matplotlib.pyplot as plt

incomes=np.random.normal(150.0,20.0,1000)

plt.hist(incomes,100)
plt.show()

print incomes.std()

print incomes.var()