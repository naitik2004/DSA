# class Solution(object):
#     def topKFrequent(self, nums, k):
#         dic = {}
#         nums.sort()
#         for i in nums:
#             key = i
#             if key in dic:
#                 dic[key] += 1
#             else:
#                 dic[key] = 1
#         a = []
#         b = 0

#         for i in dic.keys():
#             if b < k:
#                 a.append(i)
#             b += 1
#         return(a)





class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Make a dictionary to count each number
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Step 2: Turn the dictionary into a list of [number, count]
        items = []
        for key in freq:
            items.append([key, freq[key]])

        # Step 3: Sort the list from high to low count
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[j][1] > items[i][1]:
                    # swap items
                    temp = items[i]
                    items[i] = items[j]
                    items[j] = temp

        # Step 4: Take the first k numbers
        result = []
        for i in range(k):
            result.append(items[i][0])

        return result



