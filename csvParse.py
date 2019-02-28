# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 10:00:09 2019

@author: NICA1
"""
'''
import csv
import sys
#csv.field_size_limit(sys.maxsize)

maxInt = sys.maxsize
decrement = True

while decrement:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    decrement = False
    try:
        csv.field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True
with open('D:\\Savitri\\data\\application\\application-resources\\Results\\results_big.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in spamreader:
        if count<=1066055:
            print(count)
            print('___________')
            print(', '.join(row))
            print('*************')
        count+=1
'''        
        
import sys
#fil=sys.argv[1]
csvfilename = open('D:\\Savitri\\data\\application\\application-resources\\Results\\results_big23Feb.csv', 'r').readlines()
file = 1
for j in range(len(csvfilename)):
    if j % 100000 == 0:
        
        open('D:\\Savitri\\data\\Results\\result'+ str(file) + '.csv', 'w+').writelines(csvfilename[j:j+100000])
    file += 1