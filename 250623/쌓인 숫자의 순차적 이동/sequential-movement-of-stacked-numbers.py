from collections import deque

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
numbers = list(map(int, input().split()))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# grid를 리스트로
for number in range(numbers)
    for row in range(n):
        for col in range(n):
            if number == grid[i][j]:
                dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1],[0, 1, 1, 1, 0, -1, -1, -1]
                mx, my = -1, -1
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny):
                        if mx == -1:
                            mx, my = nx, ny


                q = deque()
                # grid[i][j] = deque


# numbers를 순회하며 이동


for row in grid:
    for nums in grid:
        if len(nums) == 0:
            print("None")

        for num in nums:
            print(num, end=" ")
        print()
