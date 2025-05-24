import os
path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/original"
fic_list = os.listdir(path)

file_num = 1
for fic in fic_list:
    print(f"{file_num}. {fic}")
    file_num +=1

file_selected = False
while file_selected == False:
    choose = int(input("Please select the file number of the file you wish to be converted: "))
    if choose > 0 and choose <= len(fic_list):
        file = fic_list[choose-1]
        file_selected = True
    else:
        print("please try again")
print(file)
