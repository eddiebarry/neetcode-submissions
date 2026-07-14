class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        dp = {}
        n,m = len(s), len(t)


        def calc_sub(i,j):
            k = (i,j)
            if k in dp:
                return dp[k]

            if j == m:
                dp[k] = 1
                return 1

            if not( i < n and j < m ):
                dp[k] = 0
                return 0


            ans = 0
            if s[i] == t[j]:
                ans += calc_sub(i+1,j+1)
            ans += calc_sub(i+1,j)

            dp[k] = ans
            return ans
        
        return calc_sub(0,0)
        # print(dp)

        # return calc_sub(0,0)
        
