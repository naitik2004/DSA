# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(root):
            if root is None:
                return 0
            
            lhs = check(root.left)
            rhs = check(root.right)

            if  (lhs == -1) or (rhs == -1) or (abs(lhs-rhs) > 1):
                return -1

            return (max(lhs, rhs) + 1)
            
        return check(root) != -1