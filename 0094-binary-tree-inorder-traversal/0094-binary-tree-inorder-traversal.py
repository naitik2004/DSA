# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # a = []
        # def inOrder(root):
        #     if root is None:
        #         return 
        #     inOrder(root.left)
        #     a.append(root.val)
        #     inOrder(root.right)
        # inOrder(root)
        # return a
        
        if root == None:
            return []

        ans = []
        stack = []
        curr = root

        while stack or curr:
            # go left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # now select one by one first the left then its rigth
            # visit the Node
            curr = stack.pop()
            ans.append(curr.val)
            # go to teh right child
            curr = curr.right
        return ans

