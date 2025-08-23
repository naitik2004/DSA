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
#     def pre(self,root, ans,level):
#         if not root:
#             return 
#         if len(ans) <= level:
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
        if root is None:
            return []
        
        ans = []
        queue = [root]

        while queue:
            level = []
            n = len(queue)

            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)
        return ans
        