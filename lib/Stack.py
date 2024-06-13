class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        
        return False


    def search(self, target):
        if target in self.items:
            return len(self.items) - 1 - self.items.index(target)
        else:
            return -1
