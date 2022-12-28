import pandas as pd

df_train = pd.DataFrame()
df_val = pd.DataFrame()
df_test = pd.DataFrame()

df_all= pd.read_csv("data_list_all_chat.csv",encoding='utf-8') 

df_train = df_all.sample(n = 80000, replace=False)
df_val = df_all.sample(n = 10000, replace=False)
df_test = df_all.sample(n = 10000, replace=False)

df_train.to_csv("data_list_train_chat.csv", mode='w',index=False)
df_val.to_csv("data_list_val_chat.csv", mode='w',index=False)
df_test.to_csv("data_list_test_chat.csv", mode='w',index=False)
