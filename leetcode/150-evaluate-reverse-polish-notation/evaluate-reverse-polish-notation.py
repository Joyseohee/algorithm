class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 스택
        stack = []

        # 연산자 정의 : set
        operator = set(["+", "-", "*", "/"])        

        # 연산 계산기
        def calculator(calc, a, b):
            if calc == "+":
                return a + b
            if calc == "-":
                return a - b
            if calc == "*":
                return a * b
            if calc == "/":
                return int(a / b)

        # tokens 순회 숫자 stack에 넣기, 연산자가 등장하면 숫자를 꺼내서 연산 -> stack
        for c in tokens:
            if c not in operator:
                stack.append(int(c))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                calc = c
                total = calculator(c, num2, num1)
                stack.append(total)

        # stack 1개의 숫자
        return stack[0]
        
        