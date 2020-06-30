
# Brute Force. 0(n@2).. In nested for loop get the max profit buy iterating one by one

'''
def buyandSell(lst):
    maxprofit=0

    for i in range(len(lst)):
        for j in range (i+1,len(lst)):
            maxprofit=max(maxprofit,lst[j]-lst[i])
    return maxprofit



lst=[7,1,5,3,6,4]

print(buyandSell(lst))

'''

###
import sys
def buyandSell(lst):
    maxprofit=0
    mincost=sys.maxsize

    for i in range(len(lst)):
        mincost=min(mincost,lst[i])
        maxprofit=max(maxprofit,lst[i]-mincost)
    return maxprofit



lst=[7,1,5,3,6,4]

print(buyandSell(lst))

