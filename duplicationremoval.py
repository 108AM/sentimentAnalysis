import csv

def removingDuplicates(filename):
    
    #list to contain all rows
    originaltext = []

    with open(filename, "r+", encoding="utf8") as file:
        for row in csv.reader(file):
            #appends string
            originaltext.append(",".join(row))

    #leaves only unique values in list
    originaltext = list(dict.fromkeys(originaltext))

    with open(filename, "w+", encoding="utf8", newline="") as file:
        writer = csv.writer(file)
        for row in originaltext:
            #writes rows to file, overwritting original rows
            writer.writerow([row])

removingDuplicates("extractedtext.csv")