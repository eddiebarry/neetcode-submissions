class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()        
        # find peak
        lo, hi = 1, n-2

        while lo!=hi:
            md = (lo+hi)>>1
            a,b,c = mountainArr.get(md-1),mountainArr.get(md),mountainArr.get(md+1)

            if a < b < c:
                lo = md+1
            elif a > b > c:
                hi = md-1
            else:
                lo = hi = md
        
        md = lo
        print(md)
        # do bin search on 2 halves
        def bn(lo,hi, tg):
            while lo<=hi:
                md = (lo+hi)>>1
                cd = mountainArr.get(md)

                if cd < tg:
                    lo = md+1
                elif cd > tg:
                    hi = md-1
                else:
                    return md

            return -1

        def bn_r(lo,hi, tg):
            while lo<=hi:
                md = (lo+hi)>>1
                cd = mountainArr.get(md)

                if cd > tg:
                    lo = md+1
                elif cd < tg:
                    hi = md-1
                else:
                    return md

            return -1

        idx = bn(0,md, target)
        if idx == -1:
            idx = bn_r(md,n-1, target)
        
        return idx


    