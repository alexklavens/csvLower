##lowercase all fields in csv file

import csv
def csvLower(__readFromCSV, __writeToCSV = ""):
    """__readFromCSV takes "<filename>.csv"
       __writeToCSV optionally takes a write file.
       Defaults to filename created based on __readFromCSV name

       RETURNS __writeToCSV filename"""


    #Formats default __writeToCSV filename
    #i.e. "infile.csv" --> "infile_csvLower.csv"
    if __writeToCSV == "":
        __writeToCSV = __readFromCSV[:-4] + "_csvLower" + __readFromCSV[-4:]


    with open(__readFromCSV, newline='',encoding = "utf-8") as in_file:
        with open(__writeToCSV, 'w', newline='',encoding="utf-8") as out_file:
            reader = csv.reader(in_file, delimiter=',', quotechar='|')
            csvWrite = csv.writer(out_file, delimiter=',', quotechar='|')

            for row in reader:
                newRow = []
                for item in row:
                    newRow.append(item.lower())

                csvWrite.writerow(newRow)

    return __writeToCSV
