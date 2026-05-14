class ListNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # {key: node}

        # head for LRU, tail for MRU
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: ListNode):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _insert_at_tail(self, node: ListNode):
        p, n = self.tail.prev, self.tail
        p.next = node
        node.prev = p
        node.next = n
        n.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # update MRU
            self._remove(self.cache[key])
            self._insert_at_tail(self.cache[key])
            return self.cache[key].value
            
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self._insert_at_tail(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove the LRU Node from the Linked List and delete it from hashmap
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
        
