# class Solution(object):
#     def searchBST(self, root, val):
#         a = [None]
#         def dfs(root):
#             if root == None:
#                 return 
            
#             dfs(root.left)
#             if root.val == val:
#                 a[0] = root
#             dfs(root.right)
#         dfs(root)
#         return a[0]

class Solution(object):
    def searchBST(self, root, val):
        a = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if node.val == val:
                a.append(node)
            dfs(node.right)
        dfs(root)
        return a[0] if a else None


# class Solution(object):
#     def searchBST(self, root, val):
#         if not root:
#             return None  
        
#         if root.val == val:
#             return root  
        
#         if val < root.val:
#             return self.searchBST(root.left, val)
#         else:
#             return self.searchBST(root.right, val)
