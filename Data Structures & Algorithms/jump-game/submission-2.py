class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        n = len(nums)

        for idx, x in enumerate(nums):
            if idx > curr:
                return False
            elif idx == n-1:
                return True

            curr = max(curr, idx+x)

        

            
            


            