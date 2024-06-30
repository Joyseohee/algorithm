class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in map.values():
                stack.append(char)
            elif char in map.keys():
                if stack and map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return not stack
