# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):  
        ans = []  
        self.pre(root, ans, 0)  
        return ans  

    def pre(self, root, ans, depth):  
        if not root:  
            return  
        if len(ans) <= depth:  
            ans.append([])  
        # Check if depth is even or odd to determine order  
        if depth % 2 == 0:  
            ans[depth].append(root.val)  # Left to right on even levels  
        else:  
            ans[depth].insert(0, root.val)  # Right to left on odd levels  
        self.pre(root.left, ans, depth + 1)  
        self.pre(root.right, ans, depth + 1)  