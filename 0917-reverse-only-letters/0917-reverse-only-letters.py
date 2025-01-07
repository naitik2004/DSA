class Solution(object):
    def reverseOnlyLetters(self, s):
        # letters = [i for i in s if i.isalpha()]
        # result = []

        # for i in s:  
        #     if i.isalpha():  
        #         result.append(letters.pop())
        #     else:  
        #         result.append(i) 

        # return ''.join(result)  

        s = list(s)
        left , right = 0, len(s)-1
        while left < right:
            if not s[left].isalpha():
                left += 1 
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)