# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:05:24 2018

@author: JITESH
"""

import re

l=[]
regex=re.compile(r'[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[a-zA-Z]{2,4}$')
for i in range(0,int(input())):
    x=raw_input()
    response=regex.match(x)
    if response:
        l.append(x)


print l.sort()
    
    