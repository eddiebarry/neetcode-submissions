class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = defaultdict(lambda: 0)

        for x in s:
            cnt[x]+=1

        hp = [ (-cnt[x], x) for x in cnt]
        heapq.heapify(hp)

        ans = ''

        while len(hp) >= 2:
            mx, mx_c = heapq.heappop(hp)
            mn, mn_c = heapq.heappop(hp)

            mx, mn = -mx, -mn

            ans += (mx_c+mn_c)

            if mx > 1:
                heapq.heappush(hp, (-(mx-1), mx_c) )
            if mn > 1:
                heapq.heappush(hp, (-(mn-1), mn_c) )

        if hp:
            if -hp[0][0]==1:
                ans += hp[0][1]
            else:
                return ""
        
        return ans
            


