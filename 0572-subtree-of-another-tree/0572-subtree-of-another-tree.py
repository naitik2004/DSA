# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return False
        if subRoot == None:
            return True

        def checkSub(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return (p.val == q.val) and checkSub(p.left, q.left) and checkSub(p.right, q.right)

        return checkSub(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)