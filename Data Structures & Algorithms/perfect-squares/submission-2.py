class Solution:
    def numSquares(self, n: int) -> int:
        dp = {
            1: 1,
            0: 0
        }

        for tg in range(n):
            r_tg = tg+1

            i = 1
            ans = n
            while i*i <= r_tg:
                ans = min(ans, 1+dp[r_tg-i*i])
                i+=1
            
            dp[r_tg]=ans
        
        return dp[n]

        