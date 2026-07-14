class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l,r = 0, len(piles)-1
        
        state_cache = {}



        def calc_max_value(i,j):
            if i > j:
                return 0,0

            k = (i,j)
            if k in state_cache:
                return state_cache[k]

            

            # we can pick left            
            bob_left_total, alice_left = calc_max_value(i+1,j)            
            alice_left_total = piles[i] + alice_left
            


            # we can pick right
            bob_right_total, alice_right = calc_max_value(i,j-1)            
            alice_right_total = piles[j] + alice_right

            if alice_left_total > alice_right_total:
                state_cache[k] = alice_left_total, bob_left_total
            else:
                state_cache[k] = alice_right_total, bob_right_total

            return state_cache[k]
        
        a, b = calc_max_value(l,r)
        # print(a,b)

        return a > b