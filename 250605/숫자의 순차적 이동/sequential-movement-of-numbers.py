n, m = map(int, input().split())

numbers = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def find_and_move(num):
    dxs, dys = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]
    for x in range(n):
        for y in range(n):
            if numbers[x][y] == num:
                mx, my = -1, -1
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy

                    if in_range(nx, ny) and (numbers[nx][ny] > numbers[mx][my] or mx == -1):
                        mx, my = nx, ny
                #print(f"x={x}, y={y}, {numbers[x][y]}, mx={mx}, my={my}, {numbers[mx][my]}")
                numbers[mx][my], numbers[x][y] = numbers[x][y], numbers[mx][my]
                return

for _ in range(m):
    for i in range(1, n * n + 1):
        find_and_move(i)
        #print(numbers)


for row in numbers:
    for num in row:
        print(num, end = " ")
    print()
