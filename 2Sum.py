'''
def twosum(nums,target):

# Brute Force

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
    return False
lst = [2, 7, 9, 11]
print(twosum(lst, 19))
'''

###Better Solution###

## On each index save the target-val and index in a hashmap. and no on each next iteration verify its in Hashmap, this is the solution
##Else add it in the map

def twosum(nums,target):

    hashmap={}

    for i,num in enumerate(nums):
        if num not in hashmap:
            hashmap[target-num]=i
        else:
            return hashmap[num],i
lst = [2, 7, 9, 11]
print(twosum(lst, 16))


