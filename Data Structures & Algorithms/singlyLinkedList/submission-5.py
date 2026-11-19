class Node:
    def __init__(self, val: int = None, nextNode: "Node" = None):
        self.val = val
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.nextNode
        count = 0
        while current:
            if count == index:
                return current.val
            count += 1
            current = current.nextNode

        return -1

    def insertHead(self, val: int) -> None:
        current = self.head.nextNode
        self.head.nextNode = Node(val, current)

        if self.tail == self.head:
            self.tail = self.head.nextNode


    def insertTail(self, val: int) -> None:
        self.tail.nextNode = Node(val)
        self.tail = self.tail.nextNode

    def remove(self, index: int) -> bool:
        current = self.head.nextNode
        count = 0
        prevNode = self.head

        while current:
            if count == index:
                prevNode.nextNode = current.nextNode
                if self.tail == current:
                    self.tail = prevNode

                return True

            count += 1
            prevNode = current
            current = current.nextNode

        return False

    def getValues(self) -> List[int]:
        vals = []
        current = self.head.nextNode
        while current:
            vals.append(current.val)
            current = current.nextNode
        return vals