# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, x in enumerate(lists):
            if x:
                heapq.heappush(min_heap,  (x.val, i, x))
        
        temp = ans = ListNode()

        while min_heap:            
            v, _, h = heapq.heappop(min_heap)
            temp.next, temp = h, h

            if h.next:
                heapq.heappush(min_heap, (h.next.val, _,  h.next))
        
        return ans.next
        

