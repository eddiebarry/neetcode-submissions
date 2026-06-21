class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for i, x in enumerate(order):
            pos[x]=i

        def cmp(a):
            return [pos[i] for i in a]        


        return words == sorted(words, key=cmp)