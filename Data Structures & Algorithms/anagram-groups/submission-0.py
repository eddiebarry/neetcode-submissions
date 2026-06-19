class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        all_anagrams = defaultdict(list)
        for wrd in strs:
            mp = defaultdict(int)
            for ch in wrd:
                mp[ch]+=1

            key = ""
            for i in range(ord('z')-ord('a')+1):
                new_ch = chr(i + ord('a'))
                key += new_ch + str(mp[new_ch])

            all_anagrams[key].append(wrd)
        
        return [all_anagrams[key] for key in all_anagrams]