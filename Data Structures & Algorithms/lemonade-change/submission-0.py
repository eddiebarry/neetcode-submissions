class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_5, num_10, num_20 = 0,0,0

        for x in bills:
            if x == 5:
                num_5+=1
                
            elif x == 10:
                if num_5 == 0:
                    return False
                num_5-=1
                num_10+=1
            
            else:
                if num_10 >= 1 and num_5 >=1:
                    num_10-=1
                    num_5-=1
                elif num_5 >= 3:
                    num_5 -=3
                else:
                    return False
        
        return True