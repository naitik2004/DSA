class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')' : '(', ']' : '[', '}' : '{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or stack.pop() != matching[i]:
                    return False
            
        return len(stack) == 0
