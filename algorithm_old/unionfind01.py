# 크루스칼 알고리즘

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    else:
        return i
    return parent[i]

v, e = map(int, input().split())

parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(key=lambda item: item[0])

result = 0
for edge in edges:
    print(edge)
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union(parent, a, b)


print(result)



