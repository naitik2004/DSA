class Solution(object):
    def canBeTypedWords(self, text, brokenLetters): 
        words = text.split()
        count = 0
        for word in words:
            can_type = True
            for char in word:
                if char in brokenLetters:
                    can_type = False
                    break
            if can_type:
                count += 1
        return count