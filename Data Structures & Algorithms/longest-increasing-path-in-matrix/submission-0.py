class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        min_dist = {}

        def dfs(k):
            if k in min_dist:
                return min_dist[k]

            i,j = k

            ans = 1
            for a,b in [(0,1),(1,0),(-1,0),(0,-1)]:
                new_i, new_j = a + i, b + j

                if 0 <= new_i < m and 0 <= new_j < n and matrix[new_i][new_j] > matrix[i][j]:
                    ans = max(ans, 1 + dfs( (new_i, new_j) ) )

            min_dist[k] = ans
            return ans

        for i in range(m):
            for j in range(n):
                k = (i,j)
                if k not in min_dist:
                    min_dist[k] = dfs(k)
        
        return max([min_dist[x] for x in min_dist])


