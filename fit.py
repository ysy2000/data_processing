# -*- coding: utf-8 -*-
import os
import json
import csv
import pandas as pd
import numpy as np
import re

df_all = pd.read_csv("data_list_all_chat.csv")

old_char = list()
gen_char = list()

f_old = open("labels_for_chars.csv",'r',encoding='utf-8-sig')
rea = csv.reader(f_old)
for row in rea:
    old_char.append(row[1])
f_old.close

f_gen = open("labels_for_chars_general.csv",'r',encoding='utf-8-sig')
rea = csv.reader(f_gen)
for row in rea:
    gen_char.append(row[1])
f_gen.close

# unfit_char = np.delete(old_char, gen_char)

for ch in gen_char:
    if ch in old_char:
        old_char.remove(ch)
    else:
        print(ch)

for char in old_char:
    # print(char)
    df_all = df_all[~df_all['text'].str.contains(re.escape(char),na=False, case=False)]
    df_all = df_all[~df_all['text'].str.contains(char, na=False, case=False)]

# df_all = df_all[~df_all['text'].str.contains(re.escape('…'))]

df_all.to_csv("data_list_all_fit.csv", mode='w',index=False)
