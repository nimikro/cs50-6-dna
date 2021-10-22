import csv
import sys
import re

if len(sys.argv) != 3:
    sys.exit("Usage: python dna.py file.csv file.txt")

STR = []
names_counts = []

#open csv to read data into memory
with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for line in reader:
        names_counts.append(line)


STR = names_counts[0]
names_counts.remove(names_counts[0])
#STR now has all the STRs we need to search the dna sequence (first item is 'name', no need to remove so that index matches the counts in names_counts)
#names_counts has as the first item the name of the person and for the rest of the items the counts for each of the STR

#open txt to read dna sequence
with open(sys.argv[2]) as file:
    dna = file.readline().strip()

matches = {}

#for every STR in dna
for i in range(1, len(STR), 1):
    counter = 0
    max_count = 0
    for j in range(len(dna)):
        if dna[j:(j + len(STR[i]))] == STR[i]:
            k = 0
            while dna[(j + k):(j + k + len(STR[i]))] == STR[i]:
                counter += 1
                k += len(STR[i])
            # If new maximum of repeats, update max_count
            if counter > max_count:
                max_count = counter
            counter = 0
            matches[STR[i]] = max_count

most_matches = {}

#for every STR in matches, find STR index in STR and compare the value in matches to the value in names_counts
for k,v in matches.items():
    for i in range(1, len(STR), 1):
        #find index of STR
        if(k == STR[i]):
            #check to see if the count of that str in dna is the same as in the database, for every name
            #and add each name that matches to a new dictionary, that has the matching names and
            #the number of matches for every STR
            #example: for 1st STR Cedric and Serius match, but for 2nd STR Serius matches -> Cedric would be 1 and Serius would be 2 in dict
            for j in range(0, len(names_counts), 1):
                if (int)(names_counts[j][i]) == v:
                    if names_counts[j][0] in most_matches:
                        most_matches[names_counts[j][0]] += 1
                    else:
                        most_matches[names_counts[j][0]] = 1

if most_matches[max(most_matches, key=most_matches.get)] == len(STR) - 1:
    print(max(most_matches, key=most_matches.get))
else:
    print("No match")




