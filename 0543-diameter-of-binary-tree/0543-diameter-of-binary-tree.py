# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        a = [0]
        def dfs(root):
            if not root:
                return 0

            lhs = dfs(root.left)
            rhs = dfs(root.right)

            a[0] = max(a[0], lhs + rhs)

            return 1 + max(lhs,rhs)
        dfs(root)
        return a[0]