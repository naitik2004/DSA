class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a = -1
        count = 1
        for i in range(1, len(num)):
            if num[i-1] == num[i]:
                count += 1
                if count == 3:
                    a = max(a, int(num[i]))
                    count = 1
            else:
                count = 1
                    
        if a != -1:
            return (f"{str(a) * 3}")
            
        else:
            return ("")