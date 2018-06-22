# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:50:17 2018

@author: JITESH
"""

x=input()
y=list(x)

def target():
    a=y[2]/5
    b=y[2]%5
    if(a<=y[1] and b<=y[0]):
        return True
    else:
        return False

print target()    