# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:29:47 2018

@author: JITESH
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:09:40 2018

@author: JITESH
"""


import requests
url="https://api.mlab.com/api/1/databases/mlab/collections/mlab?apiKey=Po5yjIu98YNw4Q7hVKor3O8LtJeNpo9j"

url2="https://api.mlab.com/api/1/databases/mlab/collections/mlab/?apiKey=Po5yjIu98YNw4Q7hVKor3O8LtJeNpo9j"
#import json


def add_client(student_name, student_age, student_rollno, student_branch):
    
    data={
                "Student Name" : student_name,
                "Student Age" : student_age,
                "Student RollNo" : student_rollno,
                "Student Branch" : student_branch,
        
        }
    send=requests.post(url,json=data)
    print send.text

    

for i in range(0,int(input())):
    student_name = raw_input("Enter Student Name: ")
    student_age = raw_input("Enter Student Age: ")
    student_rollno = raw_input("Enter Student RollNo: ")
    student_branch = raw_input("Enter Student Branch: ")
    
    
add_client(student_name,student_age,student_rollno,student_branch)


def view_client(student_rollno):
    q={
       "Student RollNo" : student_rollno
       }
    receive=requests.get(url2,q)
    print receive.text
    


view_client("234")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    