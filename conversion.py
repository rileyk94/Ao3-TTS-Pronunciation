import os
import pandas as pd
original_fic_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/original"
fandom_excel_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fandom_xlsx"
fandom_csv_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fandom_csvs"
fandom_output_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fic"
fic_list = os.listdir(original_fic_path)
fandom_excel_list = os.listdir(fandom_excel_path)
fandom_csv_list = os.listdir(fandom_excel_path)
fandom_list = []

#function to convert excel to csv
def excel_to_csv(filename: str):
    input_path = os.path.join(fandom_excel_path, f"{filename}.xlsx")
    output_path = os.path.join(fandom_csv_path, f"{filename}.csv")
    read_file = pd.read_excel(input_path, engine="openpyxl")
    read_file.to_csv(output_path, index = False)


#create a list of all conversion files
for file in fandom_excel_list:
    file = file.split('.')
    fandom_list.append(file[0])

#check to see if there is a csv file for all excel files
for file in fandom_list:
    expected_csv = f"{file}.csv"
    if expected_csv not in fandom_csv_list:
        excel_to_csv(file)

file_num = 1
for fic in fic_list:
    print(f"{file_num}. {fic}")
    file_num +=1

file_selected = False
file = ""
while file_selected == False:
    choose = int(input("Please select the file number of the file you wish to be converted: "))
    if choose > 0 and choose <= len(fic_list):
        file = fic_list[choose-1]
        file_selected = True
    else:
        print("please try again")
print(file)

