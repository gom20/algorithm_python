n, m = map(int, input().split())

parent = [0] * (n+1)
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

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        if find_parent(a) != find_parent(b):
            union(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')

