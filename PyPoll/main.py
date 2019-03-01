import os
import csv

# get csv location
csvPath = os.path.join('election_data.csv')
with open(csvPath, newline='') as csvFile:

    # Read the tab delimited file on ,
    csvReader = csv.reader(csvFile, delimiter=',')

    # Set Values for Canidates name, Vote Count, Poll results
    pollRes = {}
    voteTal = 0
    canNames = []
    voteNum = []
    votePer = []


    # parse through dataset find names and count using name in Index 2

    for row in csvReader:
        voteTal += 1
        if row[2] in pollRes.keys():
            pollRes[row[2]] = pollRes[row[2]] + 1
        else:
            pollRes[row[2]] = 1

    # Cast values from data set parse to canNames and votNum list
    for key, value in pollRes.items():
        canNames.append(key)
        voteNum.append(value)

    # calculate precentage values for canidates
    for v in voteNum:
        votePer.append(round(v/voteTal*100,1))

    print(votePer)


    