# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:16:16 2018

@author: JITESH
"""

x=input()
y=list(x)
max(y)
#Largest(), , , , 
def Add(a,b):
    return a+b

def Multiply(a,b)  :
    return a*b

def Largest():
    return max(y)

def Smallest():
    return min(y)

def Sorting():
    return sorted(y)

def Remove_Duplicates():
    return list(set(y))
    

def Print():
    print "Sum=",reduce(Add,y)
    print "Multiply=",reduce(Multiply,y)
    print "Largest=",Largest()
    print "Smallest=",Smallest()
    print "Sorted=",Sorting()
    print "Without Duplicates=",Remove_Duplicates()
    
    

Print()

    



