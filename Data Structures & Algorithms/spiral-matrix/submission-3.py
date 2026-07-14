class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1

        ans = []
        while left <= right and top <= bottom:
            
            # go right
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            # go down
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1


            if top <= bottom:                
                # go left
                for i in range(right, left-1,-1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            if left <= right:
                # go up
                for i in range(bottom, top-1,-1):
                    ans.append(matrix[i][left])
                left+=1

        return ans