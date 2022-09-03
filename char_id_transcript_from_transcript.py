import pandas as pd
import csv
"""
input = original
output = transcript기반으로 변경된 char_id_transcript가 든 transcript file
"""

# index, char, freq 순으로 표시된 txt 파일 
def load_label_index(label_path):
    char2index = {'<pad>': 0, '<unk>': 1, '<sos>': 2, '<eos>': 3}

    with open(label_path, 'r', encoding="utf-8") as f:
        for no, line in enumerate(f):
            if line[0:2] == 'id': 
                continue

            index, char, freq = line.strip().split(',')
            char = char.strip()
            if len(char) == 0:
                char = ' '

            char2index[char] = int(index) +4

    return char2index

def change_to_index(transcript, char2index):
    char_id_transcript = []
    for char in transcript:
        char_id_transcript.append(char2index[char])
    return str(char_id_transcript)[1:-1].replace(',','')

if __name__ == '__main__':
    # audio_path, transcript,char_id_transcript
    file_names = []
    labels = []
    Data_list1 = pd.read_csv("/home/ysy/Conformer_baseline_NSML/KAIC120_t1-free-final-original.csv")
    char2index = load_label_index('/home/ysy/Conformer_baseline_NSML/labels_2_chars.csv') 

    for i in range(len(Data_list1)):
        file_names.append(Data_list1.iloc[i].audio_path)
        labels.append(Data_list1.iloc[i].transcript)

    csvPATH = "/home/ysy/Conformer_baseline_NSML/KAIC120_t1-free-final-original_new.csv"
     
    # script 와 file csv에 쓰기
    with open(csvPATH, 'a', newline='') as f:
        wr = csv.writer(f)
        for i, name in enumerate(file_names):
            wr.writerow([name,labels[i],change_to_index(labels[i],char2index)]) 