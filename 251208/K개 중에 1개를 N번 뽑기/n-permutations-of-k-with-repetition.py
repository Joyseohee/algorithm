k, n = map(int, input().split())

answer = []

def print_answer():
    for num in answer:
        print(num, end=" ")
    print()

def combination(curr_def):
    if curr_def == n:
        print_answer()
        return

    for i in range(1, k + 1):
        answer.append(i)
        combination(curr_def + 1)
        answer.pop()

    return

combination(0)