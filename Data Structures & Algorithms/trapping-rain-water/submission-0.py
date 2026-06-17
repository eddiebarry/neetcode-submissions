class Solution:
    def trap(self, height: List[int]) -> int:
        
        stk = [(0,-1)]

        ans = 0
        for i, ht1 in enumerate(height):
            
            if ht1 < stk[-1][0]:
                stk.append((ht1,i))
            else:
                print(ht1, stk, ans)
                while stk and ht1 > stk[-1][0]:
                    ht2,j = stk[-1]                    
                    ans += (min(stk[0][0],ht1) - ht2) * (i-j)                    
                    i = j
                    stk.pop()
                print(ans, 'after process')
                stk.append((ht1,i))
        return ans




        