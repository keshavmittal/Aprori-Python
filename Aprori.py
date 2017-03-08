# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 11:58:33 2017

@author: Keshav
"""

from __future__ import print_function
import argparse
from itertools import chain, combinations
import sys

log = open("output.txt","w")
sys.stdout = log


""""Function to read and split data from the text file."""
def get_Data(filen):
    file_iter = open(filen, 'rU')
    for line in file_iter:
        record = frozenset(line.split())
        yield record
        
"""Function to get the Transaction List and Item Set from the data read from file"""       
def getItemsetTransactionList(data):
    Itemset = set() 
    TransactionList = list()
    for record in data:
        Transaction = frozenset(record)
        """Getting list of transactions by iterating row and appending"""
        TransactionList.append(Transaction)        
        for item in Transaction:
            """Getting Itemset by iterating rows and adding item to set"""
            Itemset.add(frozenset([item]))     
    return Itemset,TransactionList

"""Function to return Itemset with support value that has minimum support value given in argument of functuon"""
def ItemsetwithMinSupport(tlist,itemset,MinSupport):
   len_tlist = len(tlist)
   """Calculate support of the itemset(with 1 item)"""   
   cal_sup = [
        (item, float(sum(1 for row in tlist if item.issubset(row)))/len_tlist) 
        for item in itemset
    ]
   """To return the itemset with corresponding support""" 
   return dict([(item, support) for item, support in cal_sup if support >= MinSupport])
   
"""Function to join the items in set , creating a large set"""
def joinSet(Itemset,length):
    return set([i.union(j) for i in Itemset for j in Itemset if len(i.union(j)) == length])


"""Funtion to return combinations"""
def subSets(itemset):
    return chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)])

"""Function the return frequent itemsets keeping track of minimum support"""
def frequent_Itemset(TransactionList, c_itemset, minSupport):
    final_itemset = dict()

    length = 1
    while True:
        if length > 1:
            c_itemset = joinSet(local_itemset, length)
        local_itemset = ItemsetwithMinSupport(TransactionList, c_itemset, minSupport)
        if not local_itemset:
            break
        final_itemset.update(local_itemset)
        length += 1

    return final_itemset 

"""The main function to generate the rules"""
def Apriori(data, minSupport, minConfidence):
    """Get Itemset and Transaction List from the function"""
    Itemset, TransactionList = getItemsetTransactionList(data)
    """Get the frequent itemset depending upon the minimum support"""
    final_itemset = frequent_Itemset(TransactionList, Itemset, minSupport)
#To get the association rules
    getRules = list()
    for item, support in final_itemset.items():
        if len(item) > 1:
            for x in subSets(item):
                y = item.difference(x)
                if y:
                    x = frozenset(x) 
                    xy = x | y # Update the xy
                    confidence = float(final_itemset[xy]) / final_itemset[x]
                    if confidence >= minConfidence:
                        getRules.append((x, y, confidence))    
    return getRules, final_itemset

"""Function to print the rules and items"""
def get_output(getRules, final_itemset):
    countRules= 0
    countItemset = 0
    print ('-------Itemset------')
    for item, support in sorted(final_itemset.items(), key=lambda (item, support): support):
        countItemset += 1
        """support rounded upto 3 decimal digit"""
        print ('[Items {}] {} : {}'.format(countItemset,tuple(item), round(support, 3)))
    print ('Total Itemsets:' , countItemset)
    
    print ('------Rules-------')
    for x, y, confidence in sorted(getRules, key=lambda (x, y, confidence): confidence):
        countRules += 1
        """confidence rounded upto 3 decimal digit"""
        print ('[Rules{}] {} --> {} : Confidence= {}'.format(countRules, tuple(x), tuple(y), round(confidence, 3)))
    print ('Total Rules discovered:' , countRules)

    
"""Functions to add options to run in Command Line"""
#Reference - https://docs.python.org/3.3/library/argparse.html
def options():
    parser = argparse.ArgumentParser(description='Apriori Algorithm Implementation')
    parser.add_argument('-f','--inputfile', dest='filen',
                   help='Data File',
                   required=True)
    parser.add_argument('-s','--support', dest='minSupport',
                   help='Minimum Support',
                   required=True,
                   type = float)
    parser.add_argument('-c','--confidence', dest='minConfidence',
                   help='Minimum Confidence',
                   required=True,
                   type = float)
    return parser.parse_args()

#main method
def main():
    Arguments = options()

    data = get_Data(Arguments.filen)
    getRules, Itemset = Apriori(data, Arguments.minSupport, Arguments.minConfidence)
    get_output(getRules, Itemset)
    

if __name__ == '__main__':
    main()







    
    
