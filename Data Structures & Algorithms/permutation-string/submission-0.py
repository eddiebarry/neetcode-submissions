class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = defaultdict(int)
        freq_map2 = defaultdict(int)

        for x in s1:
            freq_map[x]+=1



        i,j = 0,0

        while j < len(s2):
            freq_map2[s2[j]]+=1
            j+=1

            if j-i == len(s1) and all([freq_map[x] == freq_map2[x]for x in freq_map]):
                return True

            if j-i+1 > len(s1):
                freq_map2[s2[i]]-=1
                i+=1
                
            
        
        return False
        