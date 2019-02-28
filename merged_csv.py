# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 13:12:26 2019

@author: NICA1
"""
import pandas as pd
'''
#a = pd.read_csv("D:\\Savitri\\data\\application\\application-resources\\Results\\results5Feb.csv", encoding='ISO-8859-1',error_bad_lines=False)
b = pd.concat("D:\\Savitri\\data\\application\\application-resources\\Results\\results5Feb.csv")
#a = a.dropna(axis=1)
#merged = b.merge(a, on='Filename')
merge = pd.merge(a,b)
print(merge.head(10))
#a.to_csv("D:\\Savitri\\data\\application\\application-resources\\Results\\output3.csv", 'w+')
b.to_csv("D:\\Savitri\\data\\application\\application-resources\\Results\\output1.csv")
#merged.to_csv("D:\\Savitri\\data\\outpu3.csv", index=False)'''


fout=open('D:\\Savitri\\data\\application\\application-resources\\Results\\out.csv','a', encoding='ISO-8859-1')
# first file:
for line in open('D:\\Savitri\\data\\application\\application-resources\\Results\\results4.csv', encoding='ISO-8859-1'):
    fout.write(line)
# now the rest:    
for num in range(5,7):
    f = open('D:\\Savitri\\data\\application\\application-resources\\Results\\results'+str(num)+'.csv', encoding='ISO-8859-1')
    #f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()