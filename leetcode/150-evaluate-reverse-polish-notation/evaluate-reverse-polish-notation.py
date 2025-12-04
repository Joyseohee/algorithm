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
        new_tokens = []

        while len(tokens) > 0:
            if tokens[-1] in cal_set:
                new_tokens.append(tokens.pop())
            else:
                if new_tokens and new_tokens[-1] not in cal_set:
                    number1 = int(tokens.pop())
                    number2 = int(new_tokens.pop())
                    calc = new_tokens.pop()

                    cal_result = calculator(number1, number2, calc)
                    
                    tokens.append(cal_result)

                else:
                    new_tokens.append(tokens.pop())

            # print(f"tokens={tokens}, new_tokens={new_tokens}")


        return int(new_tokens[0])