class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1) # dummy for head
        self.tail = ListNode(-1) # dummy for tail
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        #        0   1   2
        # head - 1 - 2 - 3 - tail
        # get(1) -> 2

        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr != self.tail:
            return curr.val
        return -1
        

    def addAtHead(self, val: int) -> None:
        # head - 1 - 2
        # head - 3 - 1 - 2
        prev = self.head
        next = self.head.next
        node = ListNode(val)
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtTail(self, val: int) -> None:
        # 1 - 2 - tail
        # 1 - 2 - 3 - tail
        prev = self.tail.prev
        next = self.tail
        node = ListNode(val)
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def addAtIndex(self, index: int, val: int) -> None:
        #        0   1
        # head - 1 - 3 - tail
        # addAtIndex(1, 2)
        #        0   1   2 
        # head - 1 - 2 - 3 - tail
        
        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        prev = curr.prev
        next = curr
        node = ListNode(val)

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def deleteAtIndex(self, index: int) -> None:
        #        0   1   2
        # head - 1 - 2 - 3 - tail
        # deleteAtIndex(1)
        #        0   1 
        # head - 1 - 3 - tail

        curr = self.head.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0 and curr != self.tail:
            prev = curr.prev
            next = curr.next
            prev.next = next
            next.prev = prev
        
# head - tail
# head - 1 - tail
# head - 1 - 3 - tail
# head - 1 - 2 - 3 - tail
# head - 1 - 3 - tail


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)