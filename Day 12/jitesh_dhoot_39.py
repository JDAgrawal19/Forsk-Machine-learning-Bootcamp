# -*- coding: utf-8 -*-
"""
Created on Fri May 25 11:47:12 2018

@author: JITESH
"""

import numpy as np

x=np.random.randint(5,15,40)

d={}
for i in x:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


z=max(d.values())
for i in d:
    if d[i] is z:
        print i


a=np.bincount(x)

print np.argmax(a)

from collections import Counter

b=Counter(x)

print b.most_common(1)

