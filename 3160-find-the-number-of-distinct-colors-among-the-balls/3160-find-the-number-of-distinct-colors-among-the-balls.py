class Solution(object):
    def queryResults(self, limit, queries):
        n = len(queries)
        result = []
        color_count = {}
        ball_count = {}
        for i in range(n):
            ball, color = queries[i]
            if ball in ball_count:
                prev_color = ball_count[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            ball_count[ball] = color
            color_count[color] = color_count.get(color, 0) + 1
            result.append(len(color_count))
        return(result)