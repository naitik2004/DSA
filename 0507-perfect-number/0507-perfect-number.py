class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        ans = 1
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                ans += i
                if i * i  != num:
                    ans += num // i
        return ans == num


# class Solution(object):
#     def checkPerfectNumber(self, num):
#         if num <= 1:
#             return False
#         ans = 1
#         for i in range(2, int(num**0.5) + 1):
#             if num % i == 0:
#                 ans += i
#                 if i * i != num:  
#                     ans += num // i
        
#         return ans == num