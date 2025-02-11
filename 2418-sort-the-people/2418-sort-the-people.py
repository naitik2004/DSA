class Solution(object):
    def sortPeople(self, names, heights):
        b = sorted(heights)
        final  = b[::-1]
        # print(final)

        l = []
        p = 0
        for i in range(len(heights)):
            if final[i] in heights:
                p = heights.index(final[i])
                l.append(names[p])
        return(l)
