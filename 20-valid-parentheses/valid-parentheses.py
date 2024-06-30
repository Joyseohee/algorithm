class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in map:
                if stack and map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                

        return not stack
