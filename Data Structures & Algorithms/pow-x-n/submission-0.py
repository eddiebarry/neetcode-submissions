class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            x = 1/x
            n = -n

        curr = x
        while n:
            if n & 1:
                ans *= curr
            n = n >> 1
            curr *= curr
        
        return ans