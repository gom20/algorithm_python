n, m = map(int, input().split())
parent = [0]*(n+1)
for i in range(n+1):
    parent[i] = i

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    o, a, b, = map(int, input().split())
    if o == 0 and (find_parent(parent, a) != find_parent(parent, b)):
        union(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
