class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        count  = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i] <= baskets[j]:
                    count += 1
                    baskets[j] = 0
                    break
        return (len(baskets) - count)
