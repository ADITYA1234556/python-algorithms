class Solution(object):
    def isValid(self, s):
        stack = [] #creating an empty stack list to store opening brackets
        for c in s:
            #looping through the user input
            if c in '([{':
                stack.append(c)
                #if the users input is ]() the loop will add s[1] = ( into the stack
            else: #it must be a closing bracket because it is not in ({[
                if not stack:
                    return False
                elif (c == ')' and stack[-1] != '('):
                    return False
                elif (c == ']' and stack[-1] != '['):
                    return False
                elif (c == '}' and stack[-1] != '{'):
                    return False
                # elif not stack:
                #     return False
                else:
                    stack.pop() #pop the matching opening bracket from stack, pop will remove and return the last element in the list so it will be either [ or { or (
        return not stack #if the stack is empty, returns True. If the opening and closing bracket matches the pop function will make the stack empty so statement will be verified, if the stack still has elements will be False
#in our scenario => ]()
#loop 1, stack = []]
#loop 2, stack = [(]
#loop 3, stack = []] because '(' will be popped with ')'
#movinf elif not stack to line 1 first if statement because first we will want to make sure that the stack is not empty before checking for brackets

solution = Solution()
output = solution.isValid('()')
if output == False:
    print('The parenthesis is not closed properly')
else:
    print('The parenthesis is close properly')
