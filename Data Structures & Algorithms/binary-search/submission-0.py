class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums)-1


        while lo <= hi:
            md = (lo+hi)//2

            cd = nums[md]

            if cd < target:
                lo = md + 1

            elif cd > target:
                hi = md - 1

            else:
                return md

        return -1
            