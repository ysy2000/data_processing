import csv
import re

# ## csv파일 확인
# f=open('data_list_train.csv', 'r', encoding='utf-8')
# rdr = csv.reader(f)
# for line in rdr:
#     print(line)
# f.close()


def annotation_remover(string):
    # 정규식을 이용하여 텍스트의 괄호와 괄호안 문자 제거
    regex = "\(.*\)|\s-\s.?."

    text = string
    text = re.sub(regex, '', text)
    out = " ".join(text.split())
    return out

if __name__ == "__main__":

    file_name = "data_list_val"
    f1 = open(file_name + ".csv","r", encoding='UTF8')
    f2 = open(file_name + "_rm_ver.csv","w", encoding='UTF8')

    while 1:
        line = f1.readline()
        if len(line) == 0:
            break
        fixed_line = annotation_remover(line)
        f2.write(fixed_line+"\n")

    f1.closed
    f2.closed
    