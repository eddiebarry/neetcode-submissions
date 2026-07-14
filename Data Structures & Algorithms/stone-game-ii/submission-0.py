class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        idx_m_cache = {}



        def calc_max(i, m):
            k = (i,m)

            if i >= n:
                return (0,0)
            
            if k in idx_m_cache:
                return idx_m_cache[k]

            lim = min(n, i + 2 * m)

            curr = 0
            ans = (-1, -1)
            # print(i, lim)
            for j in range(i, lim):
                # print(j)
                # print('******')
                curr += piles[j]
                X = j - i + 1
                new_m = max(m, X)

                b, a = calc_max(j + 1, new_m)
                a += curr
                
                if a > ans[0]:
                    ans = (a, b)
            
            idx_m_cache[k] = ans
            return idx_m_cache[k]

        return calc_max(0, 1)[0]
