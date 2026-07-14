class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])

        a,b = 0, m-1
        c,d = 0, n-1

        curr = 0
        ans = []
        while (a <= b or c <= d )and len(ans) < m*n:
            if curr % 4 == 0:
                # we're going right
                for i in range(c,d+1):
                    ans.append(matrix[a][i])
                a+=1

            if curr % 4 == 1:
                # we're going down
                for i in range(a,b+1):
                    ans.append(matrix[i][d])
                d-=1

            if curr % 4 == 2:
                # we're going left
                for i in range(d,c-1,-1):
                    ans.append(matrix[b][i])
                b-=1
            
            if curr % 4 == 3:
                # we're going left
                for i in range(b,a-1,-1):
                    ans.append(matrix[i][c])
                c+=1

            curr+=1
        
        return ans