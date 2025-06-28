class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows >= 1:
            res.append([1])
        for i in range(1,numRows):
            ls = [1]
            temp = res[i - 1]
            for j in range(1,i):
                ls.append(temp[j - 1] + temp[j])
            ls.append(1)
            res.append(ls)
        return res

