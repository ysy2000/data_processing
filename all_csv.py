# -*- coding: utf-8 -*-
import os
import json
import csv
# import pandas as pd

"""
this python code is for make data_list.csv.
output of this code is pair of file directory and groundtruth text infoamation.
you need to data preporcessing after running this code.
If you get error below, call by python3 instead of python.

Traceback (most recent call last):
  File "all_csv.py", line 15, in <module>
    dir_f = open('data_list_val.csv','w',newline='')
TypeError: 'newline' is an invalid keyword argument for this function
"""

# data = pd.read_csv("./data.csv")

# f = open('data.csv','w',newline='')
dir_f = open('data_list_train.csv','w',newline='')

# wr = csv.writer(f)
dir_wr = csv.writer(dir_f)

dir_path = "/disk3/general_data/Training"

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.wav' in file:
            file_path = os.path.join(root, file)
            print(type(file_path))
            # json_file = file[:-3] + 'json'
            # json_file_path = os.path.join(root, json_file) # wav 2 json
            # with open(json_file_path,'r') as json_f:
            #     json_data = json.load(json_f)
            #     target = json_data['발화정보']['stt']
            #     target = target.replace('"','')
            #     target = target.replace('\r','')
            #     target = target.replace('\n','')
            # dir_wr.writerow([file_path, target])

# f.close()
dir_f.close()