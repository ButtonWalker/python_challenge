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
        revSum = float(row[1]) + revSum

        if m > 1:
            revDiffernce = revDiffernce + float(row[1]) - float(rows[m-1][1])

        # Max Revenue
        if int(max_month[1]) < float(row[1]):
            max_month = row
        # Min Revenue
        if int(min_month[1]) > float(row[1]):
            min_month = row

# Revenue Average and Change Average calculations
aveRev = float(revSum / monthCount)
aveChange = float(revDiffernce / monthCount)

# Convert Values from List to string
monthMin = ' '.join(min_month)
monthMax = ' '.join(max_month)

myAnalysis = (' Financial Analysis \n',
'--------------------\n',
f'Total Months: {monthCount}\n',
# formated to have 2 digits trailing
f'Total Revenue: ${revSum:.2f}\n',
f'Average Change: ${aveRev:.2f}\n',
# change format to ensure List read correctly
'Greatest Increase:' + ' ' + monthMax + '\n',
'Greatest Decrease:' + ' ' + monthMin)

# Terminal output
myOutput = ' '.join(myAnalysis)
print( str(myOutput))

# Open the analysis file
finaFile = open('Financial_Analysis.txt','w')

# Write to the file
finaFile.writelines(myAnalysis)

finaFile.close()

