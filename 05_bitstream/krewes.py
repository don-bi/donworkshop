'''
Donald Bi, David Deng
SoftDev
K05 -- sumamry
2022-09-28
time spent: 
DISCO: 

QCC: none
OPS SUMMARY: 
'''
import random as rand

def createDict():
    f = open('krewes.txt')
    devo_list = f.read().split("@@@")
    devo_dict = {}
    for devo in devo_list:
        data = devo.split("$$$")
    print(devolist)

createDict()

#chooses num devos and returns them as a dictionary
def chooseNDevos(d,num):
    newD = {}
    for i in range(num):
        (period, devo) = chooseDevo(krewes)
        if period not in newD:
            newD[period] = [devo]
        else:
            newD[period].append(devo)
    return newD

#returns a list of a random devo and their period
def chooseDevo(d):
    pds = list(d)
    key = rand.choice(pds)
    devoList = d[key]
    return [key, rand.choice(devoList)]

#prints out period and devo
def printDevo(d):
    (period, devo) = chooseDevo(krewes)
    print((str)(period) + ": " + devo)
