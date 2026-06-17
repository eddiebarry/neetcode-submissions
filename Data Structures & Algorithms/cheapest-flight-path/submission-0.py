from functools import lru_cache

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        nb = defaultdict(dict)

        for edge in flights:
            sr, dest, p = edge[0], edge[1], edge[2]
            nb[sr][dest]=p

        
        @lru_cache(maxsize=None)
        def dfs(curr, k):            
            if curr == dst:
                return 0
            
            if k == 0:
                return 1e9
            
            ans = 1e9
            for p in nb[curr]:
                # print(p, 'is neigh of', curr)
                ans = min(ans, nb[curr][p] + dfs(p, k-1))

            return ans
        
        return -1 if dfs(src,k+1) == 1e9 else dfs(src,k+1)