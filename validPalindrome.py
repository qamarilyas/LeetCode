'''

# remove the space and convert to lower cases only, only isalnum in the string

def ispal(s):


    s= "".join(a for a in s if a.isalnum()).replace(" ","").lower()

    if s==s[::-1]: # Now compare the revese and normal
        print("Yes")
    else:
        print("No")



ispal("A man, a plan, a canal: Panama")

'''

# Better approach would be using two pointer one from start and one from end. and keep them moving until they cross and compare
# character by charctr
def ispal(s):
    i=0
    j=len(s)-1

    while i<j: # Iterate pointers from both ends until they cross each other
        while i<j and not s[i].isalnum(): # keep moving the i pointer until we get alnum
            i+=1
        while i<j and not s[j].isalnum(): # Keep moving the j pointer until we get alnum
            j-=1

        if s[i].lower()!=s[j].lower(): # Compare if characters mismatch
            return False
        i+=1
        j-=1
    return True # Return True if found no error

    

print(ispal("A man, a plan, a canal: Panama"))

