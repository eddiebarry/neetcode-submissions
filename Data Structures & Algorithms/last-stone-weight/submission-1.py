class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []

        for x in stones:
            heapq.heappush(hp, -x)

        while len(hp) > 1:
            h,l = -heapq.heappop(hp), -heapq.heappop(hp)

            if h == l:
                continue
            else:
                heapq.heappush(hp, l-h)
       
        return -hp[0]  if hp else 0