# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        if not head:
            return None

        ans = prev = ListNode(next=head)
        temp1 = temp2 = head
	
        while temp2:	
            # count out k
            needed = k
            while needed and temp2:
                temp2 = temp2.next
                needed -= 1
	
            if needed == 0:
                #  we have k elems
                
                # we do a reverse of k elems for temp1
                curr , neigh = temp1, temp1.next
                for _ in range(k-1):
                    curr, neigh, curr.next = neigh, neigh.next, curr
		
                temp1.next = temp2
                prev.next = curr
                prev = temp1
                temp1 = temp2
            else:
                break

        return ans.next
		
