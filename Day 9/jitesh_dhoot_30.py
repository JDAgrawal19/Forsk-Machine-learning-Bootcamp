# -*- coding: utf-8 -*-
"""
Created on Tue May 22 12:48:55 2018

@author: JITESH
"""

import urllib2

rank="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

page=urllib2.urlopen(rank)

from bs4 import BeautifulSoup

soup=BeautifulSoup(page)

all_tables=soup.find_all('table')

right_table=soup.find('table',class_='table')    

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==5:
        A.append(cells[0].find(text=True))
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find(text=True))
        E.append(cells[4].find(text=True))