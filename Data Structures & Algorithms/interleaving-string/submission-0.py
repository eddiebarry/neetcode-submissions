class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        i, idx1, idx2 = 0,0,0

        if len(s3) != len(s2) + len(s1):
            return False

        dp = {}

        def check(key):
            i, idx1, idx2 = key
            if key in dp:
                return dp[key]

            ans = False
            if i == len(s3):
                ans = True
            
            if idx1 < len(s1) and s1[idx1] == s3[i]:
                ans |= check(
                    (i+1, idx1+1, idx2)
                )
            if idx2 < len(s2) and s2[idx2] == s3[i]:
                ans |= check(
                    (i+1, idx1, idx2+1)
                )

            dp[key] = ans
            return ans
        
        return check((0,0,0))