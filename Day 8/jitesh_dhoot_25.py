# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:49:20 2018

@author: JITESH
"""

from collections import namedtuple


"""pt=[]
for i in range(0,5):
    x=raw_input().split(',')
        
    Point=namedtuple('Point','name,age,score')
    
    pt.append(Point(name=x[0],age=x[1],score=x[2]))

   
pt=pt.sort()


def sort1(pt):
    for i in range (1,5):
        if(pt[i].name is pt[i-1].name):
            if(pt[i].age<pt[i-1].age):
                pt[i],pt[i-1]=pt[i-1],pt[i]
        elif(pt[i].name is pt[i-1].name and pt[i].age is pt[i-1].age):
            if(pt[i].score<pt[i-1].score):
                pt[i],pt[i-1]=pt[i-1],pt[i]


sort1(pt)

print pt"""


list1=[]
while True:
    inp=raw_input()
    if not inp:
        break
    tup1=inp.split(',')
    list1.append((tup1[0],int(tup1[1]),int(tup1[2])))

list1.sort()

print list1

"""def sort1(pt):
    for i in range (1,5):
        name,age,score=pt[i]
        name0,age0,score0=pt[i-1]
        if(name is name0):
            if(age<age0):
                pt[i],pt[i-1]=pt[i-1],pt[i]
        elif(name is name0 and age is age0):
            if(score<score0):
                pt[i],pt[i-1]=pt[i-1],pt[i]
    


sort1(list1)


print list1
"""    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    