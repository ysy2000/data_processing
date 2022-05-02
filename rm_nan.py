import pandas as pd
import csv
import re
def annotation_remover(string):
    # 정규식을 이용하여 텍스트의 괄호와 괄호안 문자 제거
    regex = "\(.*\)|\s-\s."

    text = string
    text = re.sub(regex, '', text)
    out = " ".join(text.split())
    return out



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    df_val = pd.read_csv("data_list_val.csv")
    df_val.dropna(subset=['text'], inplace=True)
    df_train = pd.read_csv("data_list_train.csv")
    df_train.dropna(subset=['text'], inplace=True)

    # 저장
    df_val.to_csv("data_list_val.csv", mode='w',index=False)
    df_train.to_csv("data_list_train.csv", mode='w',index=False)