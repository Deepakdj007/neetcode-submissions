
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert_at_head(self, node):
        next_node = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = next_node
        next_node.prev = node

    def move_to_head(self, node):
        self.remove(node)
        self.insert_at_head(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.move_to_head(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.move_to_head(node)
            return

        node = Node(key, value)

        self.cache[key] = node  

        self.insert_at_head(node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev

            self.remove(lru_node)

            del self.cache[lru_node.key]
