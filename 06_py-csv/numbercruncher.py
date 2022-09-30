'''
Donald Bi, David Deng
SoftDev
K06 -- 
2022-09-28
time spent: hr
DISCO: 

QCC: none
OPS SUMMARY: First, we split 
HOW THIS SCRIPT WORKS: We first read the csv file and store the cumulative percentages as keys and the occupations as values in a dictionary.
Then we generate a random number from 0 to the sum of all percentages. We check one by one the keys and if the random number is less than the cumulative percentage
of that key, we return the occupation.
'''
import random as rand

def read_file():
    f = open('occupations.csv')
    data = f.read().split('\n')[1:-2]
    #print(data)
    percentages = {}
    total = 0
    for d in data:
        info = d.split(',')
        total += float(info[-1])*10
        occupation_name = ''
        for word in info[:-1]:
            occupation_name += word
        percentages[total/10] = occupation_name
    return percentages

occupation_percentages = read_file()

def select_occupation():
    keys = list(occupation_percentages)
    rand_num = int(rand.random()*keys[-1]*10)/10
    for key in keys:
        if rand_num < key:
            return occupation_percentages[key]
    return None

print(select_occupation())   
