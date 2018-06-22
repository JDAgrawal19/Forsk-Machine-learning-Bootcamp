# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:41:05 2018

@author: JITESH
"""

x=raw_input().split(',')
count =0
flag=0
for item in x:
    if int(item) is 13:
        flag=1
    elif flag==1:
        flag=0
    else:
        count+=int(item)
        
print count        