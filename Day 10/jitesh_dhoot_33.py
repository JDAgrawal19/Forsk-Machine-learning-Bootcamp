# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:09:40 2018

@author: JITESH
"""

from pymongo import MongoClient
from datetime import datetime
#import json

client = MongoClient('localhost', 27017)
mydb = client.db_University

def add_client(student_name, student_age, student_rollno, student_branch):
    unique_client = mydb.forsk_clients.find_one({"Student RollNo":student_rollno}, {"_id":0})
    if unique_client:
        return "Client already exists"
    else:
        mydb.forsk_clients.insert(
                {
                "Student Name" : student_name,
                "Student Age" : student_age,
                "Student RollNo" : student_rollno,
                "Student Branch" : student_branch,
                "Date-Time" : datetime.now()
                })
        return "Client added successfully"

def view_client(student_rollno):
    user = mydb.forsk_clients.find_one({"Student RollNo":student_rollno}, {"_id":0})
    if user:
        student = user["Student Name"]
        age = user["Student Age"]
        rollno = user["Student RollNo"]
        branch = user["Student Branch"]
        time = user["Date-Time"]
        return {"Student Name":student,"Student Age":age,"Student RollNo":rollno,"Student Branch":branch}
    else:
        return "Sorry, No such user exists"


for i in range(0,int(input())):
    student_name = raw_input("Enter Student Name: ")
    student_age = raw_input("Enter Student Age: ")
    student_rollno = raw_input("Enter Student RollNo: ")
    student_branch = raw_input("Enter Student Branch: ")
    print add_client(student_name,student_age,student_rollno,student_branch)

user = raw_input("Enter Student RollNo to find: ")
user_data = view_client(user)

print user_data