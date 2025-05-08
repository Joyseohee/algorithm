n,m,k=map(int,input().split())
k=k-1
grid=[list(map(int,input().split())) for _ in range(n)]

min_row = n

for j in range(k,k+m):
    for i in range(n):
        if grid[i][j] == 1:
            min_row=min(i-1, min_row)
            break

for j in range(k,k+m):
    grid[min_row][j] = 1

for row in grid:
    for num in row:
        print(num, end=" ")
    print()


