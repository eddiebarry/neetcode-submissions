# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        max_len = defaultdict(tuple)
        # ans = 0
        max_len['ans']=(0,0)
        # print(sum(max_len['ans']) )

        def rec(node):
            l,r = 0,0
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)

            if not node.left and not node.right:
                l,r = 0,0
                max_len[node] = (l,r)
            else:
                if node.left:
                    l1,r1 = max_len[node.left]
                else:
                    l1,r1 = -1,-1
                if node.right:
                    l2,r2 = max_len[node.right]
                else:
                    l2,r2 = -1,-1

                l, r = max(l1,r1) + 1, max(l2,r2) +1
                max_len[node] = (l,r)

            if sum(max_len['ans']) < l+r:
                max_len['ans'] = (l,r)
            
        
        rec(root)
        return sum(max_len['ans'])
        # print(max_len.values())
        # return max([l+r for _, l,r in max_len.values()])

