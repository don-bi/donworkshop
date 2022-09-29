'''
Donald Bi, David Deng
SoftDev
K05 -- read in file get data wow    
2022-09-28
time spent: 0.5hr
DISCO: 
-f String are OP!!!
-open() to open the file and then .read() to read the file
QCC: none
OPS SUMMARY: We will create a function to read the krewes.txt file and split each devo into their own <key, dictionary> pair 
Using this dictionary, we will create a function to get the name of a random devo and use that name to get their information.
'''
import random as rand

def create_dict():
    f = open('krewes.txt') #opens krewes.txt
    devo_list = f.read().split("@@@") #creates list of devos
    devo_dict = {} #final return variable
    for devo in devo_list:
        data = devo.split("$$$")#creates a list of each devo's data
        devo_dict[data[1]] = {"period":data[0],"ducky":data[2]} #name as key assigned to dictionary of devo data
    #print(devo_dict)
    return devo_dict

#creates initial dictionary of devo data
devos = create_dict()

#returns the name of a random devo
def choose_devo():
    key_list = list(devos)
    key = rand.choice(key_list)
    return key

#returns a string of a devo's name, period, and ducky
def get_devo_data(devo):
    period = devos[devo]["period"]
    ducky = devos[devo]["ducky"]
    return f"{devo} [period: {period}, ducky: {ducky}]"

rand_devo = choose_devo()
print(rand_devo)
print(get_devo_data(rand_devo))