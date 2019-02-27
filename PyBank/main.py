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
    #for i in range(1,len(rows)):
    print(max_month)
    print(min_month)
