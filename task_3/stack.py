from collections import deque

class Stack:
    def __init__(self, *args):
        self._container = deque(args)

    def push(self, value):
        if not self.empty() and value > self.peek():
            raise Exception(f"Stack error {value} {self.peek()}")  
        self._container.append(value)

    def pop(self):
        return self._container.pop()

    def peek(self):
        if not self.empty():
            return self._container[-1]
        return None

    def empty(self):
        return len(self._container) == 0
    
    def __len__(self):
        return len(self._container)

    def __repr__(self):
        return repr(list(self._container))
