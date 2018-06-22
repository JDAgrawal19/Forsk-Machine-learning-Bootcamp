# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:20:00 2018

@author: JITESH
"""
import numpy as np

x=raw_input().split()

x=[int(i) for i in x]

y=np.array(x)
z=y.reshape(3,3)

print z
