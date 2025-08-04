class Solution(object):
    def totalFruit(self, fruits):
        basket = {}
        left = 0
        max_fruits = 0
        for right in range(len(fruits)):
            if fruits[right] in basket:
                basket[fruits[right]] += 1
            else:
                basket[fruits[right]] = 1
            
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits


