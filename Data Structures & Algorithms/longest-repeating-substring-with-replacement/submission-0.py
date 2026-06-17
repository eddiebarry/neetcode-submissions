class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num_ch = ord('z') - ord('a') + 1
        
        idx_map=[[0]*num_ch]


        for j, x in enumerate(s):
            curr = [0]*num_ch
            for i, y in enumerate(idx_map[-1]):
                curr[i]+=y

            curr[ord(x)-ord('A')]+=1
            idx_map.append(curr)
        

        def calc(i,j):
            v = [ idx_map[j+1][idx] - idx_map[i][idx] for idx in range(num_ch)]
            return sum(v) - max(v)

        ans=0

        i,j = 0,0
        curr_k = 0
        while i <= j and j < len(s):
            while j < len(s):                
                curr_k = calc(i,j)
                if curr_k <= k:
                    ans = max(ans, j-i+1)
                    j+=1
                else:
                    break
                
            i+=1
        
        return ans
            

