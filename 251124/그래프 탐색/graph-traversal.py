n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
# Please write your code here.

for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

def dfs(vertex):
    for node in graph[vertex]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node)

dfs(1)
total = sum(visited)
print(total - 1 if total > 1 else 0)