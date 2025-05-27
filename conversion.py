import os
import pandas as pd
import csv
import re

#create file paths
original_fic_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/original"
fandom_excel_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fandom_xlsx"
fandom_csv_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fandom_csvs"
fandom_output_path = "C:/Users/rkyz9/coding/repos/Ao3-TTS-Pronunciation/fics"

#create lists of file names
fic_list = os.listdir(original_fic_path)
fandom_excel_list = os.listdir(fandom_excel_path)
fandom_csv_list = os.listdir(fandom_csv_path)
file_name_list = []
fandom_list = ["Naruto", "Harry Potter", "Star Wars", "Buffy the Vampire Slayer",
    "Fire Emblem: Three Houses", "Custom"]
#function to convert excel to csv
def excel_to_csv(filename: str):
    input_path = f"{fandom_excel_path}/{filename}.xlsx"
    output_path = f"{fandom_csv_path}/{filename}.csv"
    read_file = pd.read_excel(input_path, engine="openpyxl")
    read_file.to_csv(output_path, index = False)


#create a list of all conversion files
for file in fandom_excel_list:
    file = file.split('.')
    file_name_list.append(file[0])

#check to see if there is a csv file for all excel files
for file in file_name_list:
    expected_csv = f"{file}.csv"
    if expected_csv not in fandom_csv_list:
        excel_to_csv(file)
        fandom_csv_list.append(f"{file}.csv")

#select fic to convert
file_num = 1
for fic in fic_list:
    print(f"{file_num}. {fic}")
    file_num +=1

file_selected = False
fic = ""
while file_selected == False:
    choose = int(input("Please select the file number of the file you wish to be converted: "))
    if choose > 0 and choose <= len(fic_list):
        fic = fic_list[choose-1]
        print(fic+"\n")
        file_selected = True
    else:
        print("please try again")

#select fandom to use for conversions
fandoms_selected = False
for fandom in fandom_list:
    print(fandom)
fandoms = []
while fandoms_selected == False:
    correct_input = False
    user_choice = input(
        "Please type the name of the fandom you want to use. Type done when finished \n")
    if user_choice.lower() == "done":
        print(fandoms)
        fandoms_selected = True
        break
    for i in fandom_list:
        name = i.lower()
        if user_choice.lower() == name:
            correct_input = True
            fandoms.append(user_choice)
    if correct_input == False:
        print("Error: incorrect input. Please try again.")

#fandom file lists;
Naruto = []
Harry_Potter = []
BtVS = []
Star_Wars = []
Three_Houses = []
Custom = []

for file in fandom_csv_list:
    check = file.lower()
    if "naruto" in check:
        Naruto.append(file)
    if "harry" in check:
        Harry_Potter.append(file)
    if "buffy" in check:
        BtVS.append(file)
    if "star_wars" in check:
        Star_Wars.append(file)
    if "three_houses" in check:
        Three_Houses.append(file)
    if "custom" in check:
        Custom.append(file)

#function to convert csv file to dictionary
def csv_to_dict(file_name: str, converter: dict):
    with open(f"{fandom_csv_path}/{file_name}", "r", encoding="utf-8") as my_file:
        raw_data = my_file.read()
    data = raw_data.split("\n")
    for line in data:
        change = line.split(",")
        if len(change) > 1:
            converter[change[0]] = change[1]
    return converter

conversions = {}

for fandom in fandoms:
    if fandom.lower() == "naruto":
        for file in Naruto:
            csv_to_dict(file, conversions)
    elif fandom.lower() == "harry potter":
        for file in Harry_Potter:
            csv_to_dict(file, conversions)
    elif fandom.lower() == "star wars":
        for file in Star_Wars:
            csv_to_dict(file, conversions)
    elif fandom.lower() == "buffy the vampire slayer":
        for file in BtVS:
            csv_to_dict(file, conversions)
    elif fandom.lower() == "fire emblem: three houses":
        for file in Three_Houses:
            csv_to_dict(file, conversions)
    elif fandom.lower() == "custom":
        for file in Custom:
            csv_to_dict(file, conversions)


with open (f"{original_fic_path}/{fic}", "r",encoding="utf-8") as my_file:
    original_text = my_file.read()

new_text = original_text

for original, replacement in conversions.items():
    pattern = r"\b" + re.escape(original) + r'\b'
    new_text = re.sub(pattern,replacement, new_text, flags=re.IGNORECASE)


with open(f"{fandom_output_path}/new_{fic}", "w",encoding="utf-8") as new:
    new.write(new_text)

