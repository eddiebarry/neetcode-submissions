from bisect import bisect_left

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        cp_pft = []
        for w_t,p_t in zip(capital, profits):
            cp_pft.append( (w_t, p_t) )
        
        cp_pft = sorted(cp_pft)
        # print(cp_pft)


        curr_idx = 0
        w_c = w
        mx_hp = []

        while k:
            # print(w_c)
            while curr_idx < len(cp_pft) and cp_pft[curr_idx][0] <= w_c:
                c, p = cp_pft[curr_idx]
                heapq.heappush(mx_hp, -p)
                # print(mx_hp, 'is mx')
                curr_idx+=1

            if mx_hp:
                p = -heapq.heappop(mx_hp)
                w_c +=p
            k-=1

        return w_c
            


            
            


            
