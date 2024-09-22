from langdetect import detect
import csv

def onlyEnglishText(filename):

    #initialises list of english rows
    englishtext = []

    with open(filename, "r+", encoding="utf8") as file:
        for row in csv.reader(file):
            try:
                #if the row is in English, it is appended as a string to englishtext
                if detect(",".join(row))=="en":
                    englishtext.append(row)
            except:
                pass

    with open(filename, "w+", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        for row in englishtext:
            #rows in original overwritten; newline in first element overwitten
            #row casted to list
            writer.writerow([(",".join(row)).replace("\n","")])

onlyEnglishText("extractedtext.csv")

        
    
        