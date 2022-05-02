import pandas as pd
import csv
"""
this code is for make csv file.
output of this code is index-char-frequency.
근데 지금 원래 파일 text에 해당하는 것만 하고 싶긴 함.
"""

def sort_target(x):
        return x[1]

def tocken_freq(sentence_list, file_names):
    char_count = {}

    for k, sentence in enumerate(sentence_list):
        #print(sentence)
        try:
            for char in sentence:
                try:
                    char_count[char] += 1
                except:
                    char_count[char] = 1
        except:
            # 안되는 애들 모아두기
            with open("/home/ysy/2022Old_Man_2nd/data/out.txt", "a") as f:
                f.write(file_names[k]+'\n')

    char_count = dict(sorted(char_count.items(), key=sort_target, reverse=True))

    return char_count


if __name__ == '__main__':

    labels = []
    file_names = []
    Data_list1 = pd.read_csv("/home/ysy/2022Old_Man_2nd/data/data_list_val.csv")
    Data_list2 = pd.read_csv("/home/ysy/2022Old_Man_2nd/data/data_list_train.csv")

    Data_lists = [Data_list1,Data_list2]
    for Data_list in Data_lists:
        #print(Data_list)
        for i in range(len(Data_list)):
            labels.append(Data_list.iloc[i].text)
            file_names.append(Data_list.iloc[i].file_name)

        # print(Data_list[Data_list['text'].isnull()])

    # for i, s in enumerate(labels): 
    #     print(i, ": ", len(s))

    # for i, s in enumerate(labels): 
    #     if s == null:
    #         print(file_names[i])

    #print(len(train_labels))
    csvPATH = "/home/ysy/2022Old_Man_2nd/data/labels_for_chars.csv"        
    # script 와 file csv에 쓰기
    with open(csvPATH, 'a', newline='') as f:
        wr = csv.writer(f)
        char_freq = tocken_freq(labels,file_names)
        for i, char in enumerate(list(char_freq.keys())):
            wr.writerow([i, char, char_freq[char]]) 