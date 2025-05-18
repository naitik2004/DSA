class Solution(object):
    def isPalidrome(self, s): 
        s2 = s[::-1]
        return (s == s2)


        
    
    def getAllParts(self, s, partitions, ans):
        if len(s) == 0:
            ans.append(partitions[:])
            return

        for i in range(len(s)):
            part = s[:i+1]
            if self.isPalidrome(part):
                partitions.append(part)
                self.getAllParts(s[i+1:], partitions, ans)
                partitions.pop()


    def partition(self, s):
        self.partitions = []
        self.ans = []
        self.getAllParts(s, self.partitions, self.ans)
        return self.ans