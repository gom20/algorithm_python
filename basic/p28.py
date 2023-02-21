#노드 N개, 간선 M
#마을을 두개로 나눔
#크루스컬로 만들고, 가장 비용이 큰 간선 삭제

n, m = map(int, input().split())

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(x, y):
    px = find_parent(x)
    py = find_parent(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

total_cost = 0
max_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        total_cost += cost
        max_cost = max(max_cost, cost)
        union(a, b)

print(total_cost - max_cost)