class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]  # A list to store the paranthesis
        valid=('(','{','[') # Open paranthesis are always added in the stack

        # Iterate over the string and if its open paranthesis add it if not, check stack is not empty and last element
        # of the stack is respective open paranthesis
        for a in s:
            if a in valid:
                stack.append(a)
            elif a == ')' and len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            elif a == '}' and len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            elif a == ']' and len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else: # If there is some false input, will return False right away
                return False

        if len(stack) == 0:
            return True
        else:
            return False



s=Solution()
print(s.isValid('()'))








