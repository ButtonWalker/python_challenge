import os
import csv

# get csv location
csvPath = os.path.join('election_data.csv')
with open(csvPath, newline='') as csvFile:

    # Read the tab delimited file on ,
    csvReader = csv.reader(csvFile, delimiter=',')

    # Set Values for canidates name, Vote Count, Poll results
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

    # Cast values from data set parse to canidates and votNum list
    for key, value in pollRes.items():
        canNames.append(key)
        voteNum.append(value)

    # calculate precentage values for canidates
    for v in voteNum:
        votePer.append(round(v/voteTal*100,1))

    # grab the canidates who have recieved votes create a list of them
    canWVotes = canNames[0]
    if len(canNames) > 1:
        for cv in range(1, len(canNames)):
            canWVotes = canWVotes + "," + canNames[cv]
    
    print(canWVotes)
    print(canNames, voteNum)


    