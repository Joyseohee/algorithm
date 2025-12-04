class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b/a)
        }

        stack = []
        total = 0
        for x in tokens:
            if x not in operands:
                stack.append(x)
            else:
                i1 = int(stack.pop())
                i2 = int(stack.pop())
                total = operands[x](i1, i2)
                stack.append(total)

        return int(stack[0])