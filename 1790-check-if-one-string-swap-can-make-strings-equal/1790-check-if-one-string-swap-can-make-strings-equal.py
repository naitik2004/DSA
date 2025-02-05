class Solution(object):
    def areAlmostEqual(self, s1, s2):
        a1 = sorted(s1)
        a2 = sorted(s2)

        if a1 != a2:
            return False
        elif len(s1) == len(s2):
            count = 0
            for i in range(len(a1)):
                if s1[i] != s2[i]:
                    count += 1
            if count == 0 or count == 2:
                return True
            else:
                return False
        else:
            return False

    






        # if s1 == s2:
        #     return True
        # not_match = 0
        # count = 0
        # if len(s1) == len(s2):
        #     for i in range(len(s1)):
        #         if s1[i] not in s2:
        #             not_match += 1
        # if not_match == 2 or not_match == 0:
        #     for i in range(len(s1)):
        #         if s1[i] != s2[i]:
        #             count += 1
        # if count == 2:
        #     return True
        # return False