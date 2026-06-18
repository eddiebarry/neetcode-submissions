class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mc = min(coins)
        DP = {}

        coins = set(coins)
        if amount == 0:
            return 0

        def dp(amt):
            if amt in DP:
                return DP[amt]
            
            if amt < mc:
                DP[amt]=-1
            
            elif amt in coins:
                DP[amt]=1
            
            else:
                ans = -1
                for x in coins:
                    t = dp(amt-x)
                    if t != -1:
                        if ans == -1:
                            ans = t
                        ans = min(ans, t)
                if ans != -1:
                    DP[amt] = 1 + ans
                else:
                    DP[amt] =  ans

            return DP[amt]
        
        return dp(amount)

                
            
