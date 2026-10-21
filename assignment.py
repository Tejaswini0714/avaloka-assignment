# Problem 1: LRU Cache

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.add_to_front(node)
            return

        node = Node(key, value)
        self.cache[key] = node
        self.add_to_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev

            self.remove(lru)
            del self.cache[lru.key]


# Example
cache = LRUCache(2)

cache.put(1, "A")
cache.put(2, "B")

print(cache.get(1))      # A

cache.put(3, "C")       # Removes key 2

print(cache.get(2))     # -1
print(cache.get(3))     # C


# Problem 2: Event Scheduler

def can_attend_all(events):
    if not events:
        return True

    events = sorted(events)

    for i in range(1, len(events)):
        previous_end = events[i - 1][1]
        current_start = events[i][0]

        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    starts = sorted([event[0] for event in events])
    ends = sorted([event[1] for event in events])

    start_pointer = 0
    end_pointer = 0

    rooms_in_use = 0
    max_rooms = 0

    while start_pointer < len(events):

        if starts[start_pointer] < ends[end_pointer]:
            rooms_in_use += 1
            max_rooms = max(max_rooms, rooms_in_use)
            start_pointer += 1

        else:
            rooms_in_use -= 1
            end_pointer += 1

    return max_rooms
