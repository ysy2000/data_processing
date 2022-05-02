# -*- coding: utf-8 -*-
import os
import json
import csv
import pandas as pd
import re

df_val = pd.read_csv("data_list_val.csv")
df_train = pd.read_csv("data_list_train.csv")

# data = list()
# f = open("labels_for_chars.csv",'r',encoding='utf-8-sig')
# rea = csv.reader(f)
# for row in rea:
#     data.append(row[1])
# f.close

# print(data)

# for char in data[1100:]:
#     print(char)
#     df_train = df_train[~df_train['text'].str.contains(re.escape(char))]
#     df_val = df_val[~df_val['text'].str.contains(char, na=False, case=False)]

df_train = df_train[~df_train['text'].str.contains(re.escape('…'))]
df_val = df_val[~df_val['text'].str.contains(re.escape('…'))]

df_val.to_csv("data_list_val.csv", mode='w',index=False)
df_train.to_csv("data_list_train.csv", mode='w',index=False)
