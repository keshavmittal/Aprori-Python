# Aprori-Python
Implementation of Aprori Algorithm in Python

Usage: python final_Aprori.py -f filename -s minSupport -c minConfidence
Exmple:python final_Aprori.py -f data1 -s 0.2 -c 0.6

Functions Created: Everything is commented.
Summary of functions used:

get_Data(filen)
"get the data from file and split it according to space"

getItemsetTransactionList(data)
"get the Itemlist and Transaction list from the data read from get_Data function"

ItemsetwithMinSupport(tlist,itemset,MinSupport)
"return the itemset with minimum support based on arguments given by user"

joinSet(Itemset,length)
"use union to joing the itemset with itself to return n-element itemset"

subSets(itemset)
"return subset"

frequent_Itemset(TransactionList, c_itemset, minSupport)
"This functions call for ItemsetwithMinSupport function to get frequent itemset that fulfils minmum support requirement"

Apriori(data, minSupport, minConfidence)
"the main function called to that returns rules and itemset based on data file, minimum support and minimum confidence"

get_output(getRules, final_itemset)
"Print the output of rules and itemset and calculate total number of itemset and rules derived"

options()
"function to add arguments so user can choose the data file , minimum support and minimum confidence to be given"

Note: "sys.stdout is used to print the result into output file.

Sample data files added.
 
