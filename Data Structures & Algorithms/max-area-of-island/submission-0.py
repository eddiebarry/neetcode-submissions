class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr = -1

        n,m = len(grid), len(grid[0])

        for x in range(n):
            for y in range(m):
                val = grid[x][y]

                if val <= 0:
                    continue

                grid[x][y] = curr
                stk = [(x,y)]

                for a,b in stk:
                    for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                        new_x, new_y = a+i, b+j

                        if 0 <= new_x < n and 0 <= new_y < m:
                            if grid[new_x][new_y] > 0:
                                grid[new_x][new_y] = curr
                                stk.append((new_x,new_y))

                curr -=1
        
        if curr == -1:
            return 0

        freq_map = defaultdict(int)
        
        for x in range(n):
            for y in range(m):
                val = grid[x][y]
                if val < 0:
                    freq_map[val]+=1
        
        # print(grid)

        return max([freq_map[x] for x in freq_map])

                    
