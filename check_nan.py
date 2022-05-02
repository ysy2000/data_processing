import pandas as pd
import csv
"""
this code is for checking existness both .wav file and text from .joson file.
if ther is no text for existed .wav file, remove it.
"""
if __name__ == '__main__':

    labels = []
    Data_list1 = pd.read_csv("/home/ysy/2022Old_Man_2nd/data/data_list_val.csv")
    Data_list2 = pd.read_csv("/home/ysy/2022Old_Man_2nd/data/data_list_train.csv")

    Data_lists = [Data_list1,Data_list2]
    for Data_list in Data_lists:
        #print(Data_list)
        for i in range(len(Data_list)):
            labels.append(Data_list.iloc[i].text)

        print(Data_list[Data_list['text'].isnull()])