# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root == None:
            return 0
        
        # ans = []
        queue = [root]
        count = 0

        while queue:
            n = len(queue)
            # level = []
            count += 1
            for _ in range(n):
                node = queue.pop(0)
                # ans.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # ans.append(level)
        return count