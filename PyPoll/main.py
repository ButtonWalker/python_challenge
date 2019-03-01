import os
import csv

# get csv location
csvPath = os.path.join('election_data.csv')
with open(csvPath, newline='') as csvFile:

    # Read the tab delimited file on ,
    csvReader = csv.reader(csvFile, delimiter=',')

    # Set Values for Canidates name and Vote Count
    pollRes = {}
    voteTal = 0
    canNames = []
    voteNum = []

    # pares through dataset find names and count using name in Index 2

    for row in csvReader:
        voteTal += 1
        if row[2] in pollRes.keys():
            pollRes[row[2]] = pollRes[row[2]] + 1
        else:
            pollRes[row[2]] = 1

    print(pollRes)