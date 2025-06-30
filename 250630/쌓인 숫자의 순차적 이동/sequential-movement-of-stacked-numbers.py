from collections import deque

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
numbers = list(map(int, input().split()))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# grid를 stack으로
for row in range(n):
    for col in range(n):
        st = deque()
        st.append(grid[row][col])
        grid[row][col] = st

for number in numbers:
    flag = False
    for i in range(n):
        for j in range(n):
            # 만약 찾는 숫자가 grid[i][j]의 리스트 안에 있다면,
            if number in grid[i][j] and not flag:
                flag = True
                idx = grid[i][j].index(number)
                # 큐에 있는 데이터
                tmp_stack = deque()
                times = len(grid[i][j]) - idx

                for _ in range(times):
                    if len(grid[i][j]) == 0:
                        break
                    tmp_stack.append(grid[i][j].pop())
                
                # 가장 큰 수가 있는 위치를 찾아
                dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1],[0, 1, 1, 1, 0, -1, -1, -1]
                mx, my = i, j
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    if in_range(nx, ny) and len(grid[nx][ny])!=0:
                        if (mx == i and my == j) or  max(grid[nx][ny]) > max(grid[mx][my]):
                            mx, my = nx, ny
        
                    


                # 그위에 올린다
                while tmp_stack :
                    grid[mx][my].append(tmp_stack.pop())
            
                # print(grid)

# numbers를 순회하며 이동
for row in grid:
    for nums in row:
        if len(nums) == 0:
            print("None", end="")

        while nums:
            print(nums.pop(), end=" ")
        
        print()
