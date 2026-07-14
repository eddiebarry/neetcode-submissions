class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        cache = {}
        n,m = len(word1), len(word2)

        def calc_min(i,j):
            k = (i,j)
            if k in cache:
                return cache[k]
            

            if j == m:
                return n-i
            if i == n:
                return m-j
            
            ans = m + n
            
            # if same char
            if word1[i] == word2[j]:                
                ans = min(ans, calc_min(i+1, j+1))
            else:
                # if we replace
                ans = min(ans, 1 + calc_min(i+1, j+1))


            # if we insert and hence skip a letter
            ans = min(ans, 1 + calc_min(i, j+1))

            # if we delete a letter 
            ans = min(ans, 1+ calc_min(i+1, j))

            cache[k] = ans
            return ans
        
        return calc_min(0,0)
