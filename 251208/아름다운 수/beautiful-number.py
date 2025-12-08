n = int(input())

count = 0
numbers = []

def find_beauty():
    i = 0
    while i < n:
        if i + numbers[i] >= n + 1:
            return False

        for j in range(i, i + numbers[i]):
            if numbers[j] != numbers[i]:
                return False

        i += numbers[i]

    return True


def find_numbers(curr_digit):
    global count
    if curr_digit == n:
        if find_beauty():
            count += 1
        return

    for i in range(1, 5):
        numbers.append(i)
        find_numbers(curr_digit + 1)
        numbers.pop()

find_numbers(0)

print(count)
        

