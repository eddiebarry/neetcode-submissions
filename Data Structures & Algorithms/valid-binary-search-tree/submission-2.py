# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l,r = -1001, 1001

        def dfs(node, l,r):            
            if l < node.val < r:
                left, right = True, True
                if node.left:
                    left = dfs(node.left, l, node.val)
                if node.right:
                    right = dfs(node.right, node.val, r)
                
                return left and right
            else:
                return False

        return dfs(root, l, r)