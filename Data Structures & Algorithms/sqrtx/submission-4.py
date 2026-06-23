class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x

        ans = -1
        while l <= r:
            md = (l+r) >> 1

            if md * md <= x:
                ans = md
                l = md+1
            else:
                r = md -1
        
        return ans