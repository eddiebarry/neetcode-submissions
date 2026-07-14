class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])

        def flip():
            for i in range(n):
                for j in range(i, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            

        def mirror():
            for j in range(n//2):
                for i in range(n):
                    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

        flip()
        # print(matrix)
        mirror()
        # print(matrix)

        return