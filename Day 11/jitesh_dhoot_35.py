# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df=pd.read_csv("training_titanic.csv")


print (df["Survived"].value_counts())

print (df["Survived"].value_counts(normalize=True))


#df_sub=df.groupby(["Sex"])


df_m=df[df['Sex']=='male']


df_f=df[df['Sex']=='female']


print (df_m["Survived"].value_counts())

print (df_m["Survived"].value_counts(normalize=True))


print (df_f["Survived"].value_counts())

print (df_f["Survived"].value_counts(normalize=True))
