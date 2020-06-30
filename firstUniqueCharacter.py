# Create a dict to store the wordcount then iterate over the string and return the first value with count 1.

def firstCharacter(s):


    wordcount={}

    for i in s:
        if i not in wordcount:
            wordcount[i]=1
        else:
            wordcount[i]+=1

    for i in range(len(s)):
        if wordcount[s[i]]==1:
            return i

print(firstCharacter("mm nn x qq rr"))

##Using built in functions of Python##
'''
s="mm nn x qq rr"
for i in s:
    if s.count(i)==1:
        print( s.index(i))
'''