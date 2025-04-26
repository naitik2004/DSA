# # Definition for a binary tree node.
# # class TreeNode(object):
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution(object):
#     def levelOrder(self, root):
#         ans = []
#         self.pre(root,ans,0)
#         return ans
#     def pre(root, ans,level):
#         if root == None:
#             return 
#         if (len(ans) = level):
#             ans.append([])
#         ans[leve].append(root.val)
#         self.pre(root.left,ans,level+1)
#         self.pre(root.right,ans,level+1)

        
# Definition for a binary tree node.  
# class TreeNode(object):  
#     def __init__(self, val=0, left=None, right=None):  
#         self.val = val  
#         self.left = left  
#         self.right = right  
class Solution(object):  
    def levelOrder(self, root):  
        ans = []  
        self.pre(root,ans,0)  
        return ans  
    def pre(self, root, ans, depth):  
        if not root:  
            return  
        if len(ans) <= depth:  
            ans.append([])  
        ans[depth].append(root.val)  
        self.pre(root.left, ans, depth+1)  
        self.pre(root.right, ans, depth+1)  
        