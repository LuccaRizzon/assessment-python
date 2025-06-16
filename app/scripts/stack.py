class Stack:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items += [item]

    def pop(self):
        if self.is_empty():
            return None
        top = self.items[-1]
        self.items = self.items[:-1]
        return top

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        count = 0
        for _ in self.items:
            count += 1
        return count
