class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> ListNode
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: LisNode):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def _insert_at_tail(self, node: ListNode):
        prev, next = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # maintain cache
            # first, remove the node in the linked list
            node = self.cache[key]
            self._remove(node)
            # second, insert it to the tail of the linked list
            self._insert_at_tail(node)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = ListNode(key, value)
        self.cache[key] = node
        self._insert_at_tail(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            # remove lru node from linked list    
            self._remove(lru)
            # delete from cache
            del self.cache[lru.key]

        
