class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.lnd = ListNode(-1)

    def add(self, key: int) -> None:
        lnd = self.lnd
        if lnd.key == None:
            lnd.key = key
        elif self.contains(key):
            return
        else:
            while lnd.next:
                lnd = lnd.next
            lnd.next = ListNode(key)

    def remove(self, key: int) -> None:
        lnd = self.lnd
        if lnd.key == key:
            self.lnd = lnd.next
        while lnd:
            if lnd.next and lnd.next.key == key:
                lnd.next = lnd.next.next
            lnd = lnd.next


    def contains(self, key: int) -> bool:
        lnd = self.lnd
        while lnd:
            if lnd.key == key:
                return True
            lnd = lnd.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)