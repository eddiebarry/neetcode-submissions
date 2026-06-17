import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [(x*x + y*y, (x,y)) for x,y in points]
        print(pts)
        
        random.shuffle(pts)


        def q_sel(pts, k):
            lo, md, hi = [], [], []
            d, pt = pts[0]

            for d_cd, cd in pts:
                if d_cd  < d:
                    lo.append((d_cd,cd))
                elif d_cd > d:
                    hi.append((d_cd,cd))
                else:
                    md.append((d_cd,cd))
            
            if k <= len(lo):
                return q_sel(lo,k)
            elif k <= len(lo)+len(md):
                return lo + md[:k-len(lo)]
            else:
                return lo + md + q_sel(hi, k-len(lo)-len(md))
        
        return [pt for _, pt in q_sel(pts, k)]
