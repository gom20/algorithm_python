n, m = map(int, input().split())

edges = []

total_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    total_cost += z

edges.sort()


parent = [0] * n
for i in range(n):
    parent[i] = i


def find_parent(target):
    global parent
    if parent[target] != target:
        parent[target] = find_parent(find_parent(parent[target]))
    return parent[target]

def union(a, b):
    global parent
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

real_cost = 0
for edge in edges:
    cost, x, y = edge
    if find_parent(x) != find_parent(y):
        union(x, y)
        real_cost += cost

print(total_cost-real_cost)
