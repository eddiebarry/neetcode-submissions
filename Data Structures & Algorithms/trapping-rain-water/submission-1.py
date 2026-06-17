class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1


        ans = 0
        max_l, max_r = height[0], height[-1]

        while l != r:
            if max_l <= max_r:
                ans += max_l - height[l]
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += max_r - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        
        return ans

                





        