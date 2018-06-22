# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:16:04 2018

@author: JITESH
"""

url="https://api.worldweatheronline.com/premium/v1/past-weather.ashx"
import requests
import json
req=[]
for i in range(1,13):
    params={}
    params["q"]="sonipat,India"
    params["date"]="2015-"+str(i)+"-01"
    params["enddate"]="2015-"+str(i)+"-28"
    params["key"]="333b32d3a8af46b0a8653833182006"
    params["format"]="json"
    req.append(requests.get(url,params))


#print req.json()
import pandas as pd
#import pandas as pd
#from pandas.io.json import json_normalize
#df = pd.DataFrame.from_dict(json_normalize(req.json()), orient='columns')
hour_df=pd.DataFrame()
date_list=[]
MaxTempC_list=[]
MinTempC_list=[]


import json
    

for l in range(1,13):
        
    f = open("myFile_sonipat"+str(l)+".json", "w")  # SAVING DATA TO FILE
    json.dump(req[l-1].json(), f)
    f.close()
    
    
    json_file=open("myFile_sonipat"+str(l)+".json")
    json1_str = json_file.read()
    json1_data=json.loads(json1_str)
    
    
    for j in range(28):
        for i in range(8):
            af=pd.io.json.json_normalize(json1_data["data"]["weather"][j]["hourly"][i])
            hour_df=hour_df.append(af,ignore_index=True)
        
    for j in range(28):
        for i in range(8):
            date_list.append(json1_data["data"]["weather"][j]["date"])
    
    for j in range(28):
        for i in range(8):
            MaxTempC_list.append(json1_data["data"]["weather"][j]["maxtempC"])
    
    for j in range(28):
        for i in range(8):
            MinTempC_list.append(json1_data["data"]["weather"][j]["mintempC"])
        





date_df=pd.DataFrame({'Date':date_list})
MaxTempC_df=pd.DataFrame({'MAX_TEMP_C':MaxTempC_list})
MinTempC_df=pd.DataFrame({'MIN_TEMP_C':MinTempC_list})



data=pd.concat([hour_df,date_df,MaxTempC_df,MinTempC_df], axis=1)


















