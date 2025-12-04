class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        def calculator(a: int, b: int, calc: str) -> int:
            if calc == '+':
                return a + b
            if calc == '-':
                return a - b
            if calc == '*':
                return a * b
            if calc == '/':
                return int(a / b)

        cal_set = set(['+', '-', '*', '/'])

        for i in range(len(tokens)):
            tokens[i] = int(tokens[i]) if tokens[i] not in cal_set else tokens[i]

        new_tokens = []

        while len(tokens) > 0:
            if tokens[-1] in cal_set:
                new_tokens.append(tokens.pop())
            else:
                if new_tokens and new_tokens[-1] not in cal_set:
                    number1 = tokens.pop()
                    number2 = new_tokens.pop()
                    calc = new_tokens.pop()

                    cal_result = calculator(number1, number2, calc)
                    
                    tokens.append(cal_result)

                else:
                    new_tokens.append(tokens.pop())

        return new_tokens[0]