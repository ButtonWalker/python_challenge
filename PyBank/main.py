import os
import  csv

# Go to the CSV location and open file
csvPath = os.path.join('budget_data.csv')

with open(csvPath,newline='') as csvFile:
    # Read the tab delimited file on ,
    csvReader = csv.reader(csvFile, delimiter=',')

    # Set Values for Month and Profit/Loss(Revenue)
    monthCount = 0
    revSum = 0

    # Get number of total Rows in dataset d
    rows=[d for d in csvReader]

    #Get Data in the dataset
    revDiffernce = int(rows[1][1])

    # Set the Max and Min Values
    max_month = rows[1]
    min_month = rows[1]

    # parse through data set using for loop
    for m in range(1,len(rows)):
    #for m in csvReader: this did not work! line above works

        monthCount = monthCount + 1
        row = rows[m]
        revSum = int(row[1]) + revSum

        if m > 1:
            revDiffernce = revDiffernce + int(row[1]) - int(rows[m-1][1])

        # Max Revenue
        if int(max_month[1]) < int(row[1]):
            max_month = row
        # Min Revenue
        if int(min_month[1]) > int(row[1]):
            min_month = row

aveRev = int(revSum / monthCount)
aveChange = int(revDiffernce / monthCount)

print(monthCount)
print(revSum)
print(aveChange)
print(aveRev)

