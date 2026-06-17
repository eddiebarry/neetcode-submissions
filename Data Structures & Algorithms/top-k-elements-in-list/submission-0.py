import random

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_m = defaultdict(int)

        for x in nums:
            f_m[x]+=1

        vals = [(-f_m[x],x) for x in f_m ]
        
        random.shuffle(vals)

        def q_sel(vals, k):
            p_freq, p_val = vals[0]
            lo = []
            md = []
            hi = []

            for freq, val in vals:
                if freq < p_freq:
                    lo.append((freq, val))
                elif freq > p_freq:
                    hi.append((freq, val))
                else:
                    md.append((freq, val))
            

            if k <= len(lo):
                return q_sel(lo, k)
            elif k <= len(lo)+len(md):
                return lo + md[:k-len(lo)]
            else:
                return lo + md + q_sel(hi, k - len(lo)-len(md))
        
        return [v for _,v in q_sel(vals,k)]

