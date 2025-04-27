class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {')':'(',  '}':'{',  ']': '['}
        # for i in s:
        #     if i in '({[':
        #         stack.append(i)
        #     else:
        #         if len(stack) == 0:
        #             return False
        #         top = stack.pop()
        #         if top != matching[i]:
        #             return False
        # if len(stack) == 0:
        #     return True

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or stack.pop() != matching[char]:
                    return False

        return len(stack) == 0