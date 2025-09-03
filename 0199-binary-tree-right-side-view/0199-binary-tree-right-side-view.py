# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        result = []
        def dfs(root,lvl):
            if root == None:
                return 

            if lvl == len(result):
                result.append(root.val)

            dfs(root.right, lvl + 1)
            dfs(root.left, lvl + 1)
        dfs(root,0)
        return result