n, m = map(int, input().split())
graph = []

parent = [0]*n
for i in range(n):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

total_cost = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))
    total_cost += cost

graph.sort(key= lambda x: (x[0]))

real_cost = 0
for i in range(m):
    cost, a, b = graph[i]
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        real_cost += cost

print(total_cost - real_cost)