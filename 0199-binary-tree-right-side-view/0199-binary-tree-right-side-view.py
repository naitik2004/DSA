# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return []
        
        ans = []
        max_lvl = -1
        stack = [(root,0)]
        while stack:
            node, lvl = stack.pop()

            if lvl > max_lvl:
                ans.append(node.val)
                max_lvl = lvl
            
            if node.left:
                stack.append((node.left, lvl + 1))
            if node.right:
                stack.append((node.right, lvl + 1))
        return ans