class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        pr = [x for x in range(n)]



        for x,y in edges:            
            i,j = x-1, y-1
            
            

            # check if already connected            
            while pr[i] != i:
                i = pr[i]
            while pr[j] != j:
                j = pr[j]

            if i == j:
                return [x, y]
            
            # connect
            pr[j] = pr[i]

            stk = []
            while pr[j]!=j:
                stk.append(j)
                j = pr[j]
            
            while stk:
                idx = stk.pop()
                pr[idx]=j
        



