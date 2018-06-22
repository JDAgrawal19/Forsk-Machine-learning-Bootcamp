# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:14:34 2018

@author: JITESH
"""

        
        
from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = raw_input().rpartition(' ')
    d[item] = d.get(item,0) + int(quantity)


for item, quantity in d.items():
    print item, quantity