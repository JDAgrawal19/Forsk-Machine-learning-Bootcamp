# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:04:00 2018

@author: JITESH
"""

str1=raw_input()

d={}
for ch in str1:
    if ch in d:
        d[ch]+=1
        #print d[ch]
    else:
        d[ch]=1
        #print d[ch]


print d