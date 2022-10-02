'''
I Am So Tired Bro, Donald Bi, David Deng
SoftDev
K06 -- read csv file of occupations and their percentages and choose an occupation weighted on the percentages
2022-09-28
time spent: 1hr
DISCO: 
- when doing splicing for lists, list[x,y], the y index is inclusive
QCC: none
OPS SUMMARY: First, we split 
HOW THIS SCRIPT WORKS: We first read the csv file and store the cumulative percentages as keys and the occupations as values in a dictionary.
Then we generate a random number from 0 to the sum of all percentages. We check one by one the keys and if the random number is less than the cumulative percentage
of that key, we return the occupation.
'''
import random as rand

def read_file():
    #opens and splits file by newlines
    f = open('occupations.csv')
    data = f.read().split('\n')[1:-2] #[1:-2] gets rid of unecessary first and last line
    
    percentages = {} #the dictionary being returned
    total = 0 #holds the cumulative percentage
    for d in data:
        info = d.split(',') #splits each line by comma to get occupation and percentage
        total += float(info[-1])*10 #some occupations have commas in name, info[-1] gets percentage
        occupation_name = ''
        
        occupation_word_list = info[:-1] #list of occupation name's words without percentage
        index = len(occupation_word_list)-1
        for word in occupation_word_list: #combines occupations with multiple commas back together
            occupation_name += word
            if index != 0: #does not add comma for final word
                occupation_name += ','
            index -= 1
        percentages[total/10] = occupation_name #total gets summed after *10 since it's float then /10 here
    return percentages

#initializes dict
occupation_percentages = read_file()

def select_occupation():
    keys = list(occupation_percentages)
    rand_num = int(rand.random()*keys[-1]*10)/10 #selects random num between 0 and total cumulative percentage 
    for key in keys:
        if rand_num < key:
            return occupation_percentages[key]
    return

print(select_occupation())

def test():
    test_dict = {}
    #chooses 100000 random occupations and puts counts in dictionary
    for i in range(100000):
        test_result = select_occupation()
        if test_result in test_dict:
            test_dict[test_result] += 1
        else:
            test_dict[test_result] = 1
    keys = list(test_dict)
    #turns counts into percentages like csv values
    for key in keys:
        test_dict[key] /= 1000
    return test_dict

print(test())
