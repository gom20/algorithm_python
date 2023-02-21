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
    X = find_parent(x)
    Y = find_parent(y)

    if X < Y:
        parent[Y] = X
    else:
        parent[X] = Y


total_cost = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        total_cost += cost
        union(a, b)

print(total_cost)