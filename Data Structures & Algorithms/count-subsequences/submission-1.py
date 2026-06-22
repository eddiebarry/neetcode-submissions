class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}


        def count(i,j):
            key = (i,j)
            if key in dp:
                return dp[key]

            # print(key)
            
            ans = -1

            if j == len(t):
                ans = 1
            elif i < len(s) and j < len(t):
                ways = 0
                if s[i] == t[j]:
                    if count(i+1,j+1) != -1:
                        ways += count(i+1,j+1)
                
                if count(i+1,j) != -1:
                    ways += count(i+1,j)

                if ways:
                    ans = ways

            dp[key]=ans
            return ans
        
        
        # count(0,0)

        # print(dp)
        return count(0,0) if count(0,0) != -1 else 0



