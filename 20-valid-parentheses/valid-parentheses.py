class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        matching_bracket = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching_bracket.values():
                stack.push(char)
            elif char in matching_bracket.keys():
                if stack.is_empty() or stack.pop() != matching_bracket[char]:
                    return False

        return stack.is_empty()
