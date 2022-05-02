import pandas as pd
"""
비복원 추출
"""
df_val = pd.read_csv("data_list_val.csv")
df_train = pd.read_csv("data_list_train.csv")

df_train = df_train.sample(n=80000)
df_val = df_val.sample(n=10000)

df_val.to_csv("data_list_val_ex.csv", mode='w',index=False)
df_train.to_csv("data_list_train_ex.csv", mode='w',index=False)