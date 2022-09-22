'''
TLOTFP1 Henry Bach, Donald Bi, Yat Long Chan
SoftDev
K<nn> -- <Title/Topic/Summary... (Aim for concision, brevity, CLARITY. Write to your future self...)>
2022-09-22
time spent: <elapsed time in hours, rounded to nearest tenth>
DISCO:
QCC:
OPS SUMMARY: Randomly choose one of the keys from the given dictionary, then grab the associated list and randomly choose a devo from the elements in the list. 
'''
import random as rand

krewes = {2:["a","b","c"],7:["d","f","g"]}
def chooseDevo(dict):
    pds = [2,7]
    key = rand.choice(pds)
    #print(key)
    devoList = krewes[key]
    #print(devoList)
    return rand.choice(devoList)

print(chooseDevo(krewes))