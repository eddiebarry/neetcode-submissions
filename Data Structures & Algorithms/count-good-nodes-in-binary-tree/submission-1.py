# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        q = []
        if root:
            q.append(
                (root,-101)
            )

        for node, mx in q:
            if node.val >= mx:
                ans +=1
            
            mx = max(node.val, mx)
            if node.left:
                q.append((node.left, mx))
            if node.right:
                q.append((node.right, mx))
        
        return ans