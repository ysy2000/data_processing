import pandas as pd
import numpy as np
import os

df_all = pd.DataFrame()

df_train= pd.read_csv("data_list_train_s.csv",encoding='utf-8') 
df_val= pd.read_csv("data_list_val_s.csv",encoding='utf-8') 
df_all = pd.concat([df_train, df_val])

df_all.to_csv("data_list_all_s.csv", mode='w',index=False)
