class Solution(object):
    def findWords(self, words):
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")

        a = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word <= s1 or  lower_word <= s2 or  lower_word <= s3:
                a.append(word)
        return(a)

