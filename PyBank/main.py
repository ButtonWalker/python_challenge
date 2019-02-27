import os
import  csv

# Go to the CSV location and open file
csvPath = os.path.join('budget_data.csv')
with open(csvPath,newline='') as csvFile:
# Read the tab delimited file on ,
    csvReader = csv.reader(csvFile, delimiter=',')
    print(csvReader)