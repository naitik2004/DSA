class Solution(object):
    def defangIPaddr(self, address):
        ans = []
        for i in address:
            if i == '.':
                ans.append('[.]')
            else:
                ans.append(i)     
        result = ''.join(ans)   
        return(result)