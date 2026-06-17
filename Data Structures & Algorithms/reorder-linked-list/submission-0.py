# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []


        send = ListNode(next=head)

        while send.next:
            nodes.append(send.next)
            send = send.next

        n = len(nodes)
        first_list = nodes[:(n+1)//2]
        second_list = nodes[(n+1)//2:][::-1]
        # print([x.val for x in first_list])
        # print([x.val for x in second_list])

        i,j = 0,0

        ans = temp = ListNode()
        while i < len(first_list) or j < len(second_list):
            if i < len(first_list):
                temp.next = first_list[i]
                i+=1
                temp = temp.next
                temp.next = None
            if j < len(second_list):
                temp.next = second_list[j]
                j+=1
                temp = temp.next
                temp.next = None

        # temp = head
        # while temp:
        #     print(temp.val)
        #     temp = temp.next
