class Solution(object):
    def countStudents(self, students, sandwiches):
        zero_count = students.count(0)
        one_count = students.count(1)

        for s in sandwiches:
            if s == 0:
                if zero_count == 0:
                    break
                zero_count -= 1
            else:
                if one_count == 0:
                    break
                one_count -= 1

        return(zero_count + one_count)
