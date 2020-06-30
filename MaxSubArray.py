
###Quadratic Approach###
'''
import sys
def MaxSubarray(lst):

    length=len(lst)
    maxSum=-sys.maxsize-1

    for i in range(length):
        winsum=0
        for j in range(i,length):
            winsum+=lst[j]
            maxSum=max(winsum,maxSum)
    return maxSum
x = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
print(MaxSubarray(x))

'''
### DP approach## Linear approach

#SubProblem:

# On each index either that value adds to previous sum or itself is the max value so current Max would be i or i+previus sum.

def MaxSubarray(lst):
    maxcurrent=maxglobal=lst[0]

    for i in lst[1:len(lst)]:
        maxcurrent=max(maxcurrent+i,i)
        maxglobal=max(maxcurrent,maxglobal)
    return maxglobal

x = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
print(MaxSubarray(x))



