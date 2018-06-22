# -*- coding: utf-8 -*-
"""
Created on Mon May 28 10:27:35 2018

@author: JITESH
"""

import urllib2

share="https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"

page=urllib2.urlopen(share)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page)

type(soup)

all_tables=soup.find_all('table')
type(all_tables)

right_table=soup.find('table',class_="wikitable")

type(right_table)
A=[]
B=[]
C=[]


for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==7:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[4].find(text=True))

        
        
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State']=B
df['National Share']=C


import matplotlib.pyplot as plt

pie_c=plt.subplot()

labels=df['State'][0:6]
sizes=df['National Share'][0:6]
explode=[0.1,0,0,0,0,0]

pie_c.pie(sizes,labels=labels,autopct='%1.2f%%',explode=explode)


































