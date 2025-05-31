class Solution(object):
    def capitalizeTitle(self, title):
        result = []
        title = title.lower()
        title = title.split()
        for i in title:
            if len(i) > 2:
                result.append(i.capitalize())
            else:
                result.append(i)
        return(' '.join(result))