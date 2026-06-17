class ListNode():
    def __init__(self, val):
        self.val = val
        self.front = None
        self.back = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.k = 0
        self.max_k = k
        self.head = None
        self.tail = None


    def enQueue(self, value: int) -> bool:
        if self.k == self.max_k:
            return False

        if self.k == 0:
            self.head = self.tail = ListNode(value)            
        else:
            self.tail.back = ListNode(value)
            self.tail = self.tail.back
        
        self.k += 1
        return True
        

    def deQueue(self) -> bool:
        if self.k == 0:
            return False
        
        if self.k == 1:
            self.head = self.tail = None
        else:
            temp = self.head

            self.head = self.head.back
            self.head.front = None
            temp.front = None
            temp.back = None
        
        self.k -=1
        return True
        

    def Front(self) -> int:
        if self.k > 0:
            return self.head.val
        else:
            return -1
        

    def Rear(self) -> int:
        if self.k > 0:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        return self.k == 0
        

    def isFull(self) -> bool:
        return self.k == self.max_k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()