# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        main_root = root

        if root == None:
            return TreeNode(val)

        while root:
            if val < root.val:
                if root.left == None:
                    root.left = TreeNode(val)
                    return main_root
                root = root.left
            
            if val > root.val:
                if root.right == None:
                    root.right = TreeNode(val)
                    return main_root
                root = root.right
