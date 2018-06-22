# -*- coding: utf-8 -*-
"""
Created on Mon May 21 12:42:48 2018

@author: JITESH
"""

x=raw_input().split()


flag0=1

for i in x:
    if int(i) <0:
        flag0=0


flag1=1        
for i in x:
    if i==i[::-1]:
        flag1=0

        
if flag0 is 1 and flag1 is 0:
    print True
else:
    print False
        
        