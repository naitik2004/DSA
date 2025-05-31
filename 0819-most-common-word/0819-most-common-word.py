class Solution(object):
    def mostCommonWord(self, paragraph, banned):

        for ch in [".", ",", "!", "?", ";", "'", ":"]:
            paragraph = paragraph.replace(ch, " ")
        
        paragraph = paragraph.lower()
        paragraph = paragraph.split()

        a = {}
        for i in paragraph:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        for word in banned:
            if word in a:
                del a[word]

        sorted_items = sorted(a.items(), key=lambda item: item[1])
        return sorted_items[-1][0]
