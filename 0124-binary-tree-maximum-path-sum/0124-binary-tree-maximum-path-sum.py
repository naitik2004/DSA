# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.a = float('-inf')
        def dfs(root):
            if not root:
                return 0

            lhs = max(0, dfs(root.left))   
            rhs = max(0, dfs(root.right))  
            self.a = max(self.a, lhs + rhs + root.val)

            return root.val + max(lhs, rhs)

        dfs(root)
        return self.a


