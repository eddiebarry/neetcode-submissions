class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = prices[0]

        ans = 0

        for x in prices:
            if x > prev:
                ans += x-prev
            prev = x
        
        return ans