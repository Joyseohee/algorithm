import sys

input = sys.stdin.readline

n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

best_values = [[0] * n for _ in range(n)]

ans = 0

def find_max_value(arr, limit):
    max_val = 0
    length = len(arr)
   
    def dfs(idx, curr_w, curr_v):
        nonlocal max_val

        if curr_w > limit:
            return
        
        max_val = max(max_val, curr_v)

        if idx == length:
            return

        # 현재 idx 요소 포함
        dfs(idx + 1, curr_w + arr[idx], curr_v + (arr[idx] ** 2))

        # 현재 idx 요소 불포함
        dfs(idx + 1, curr_w, curr_v)

    dfs(0, 0, 0)
    return max_val


for i in range(n):
    for j in range(n - m + 1):
        sub_seg = grid[i][j:j + m]
        best_values[i][j] = find_max_value(sub_seg, c)
        

for r1 in range(n):
    for c1 in range(n - m + 1):

        for r2 in range(n):
            for c2 in range(n - m + 1):

                if r1 == r2:
                    if not (c1 + m <= c2 or c2 + m <= c1):
                        continue

                ans = max(ans, best_values[r1][c1] + best_values[r2][c2])

print(ans)