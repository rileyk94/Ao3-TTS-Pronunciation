import os
path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/original"
fic_list = os.listdir(path)

file_num = 1
for fic in fic_list:
    print(f"{file_num}. {fic}")
    file_num +=1

# file_selected = false
# while file_selected == false:
    