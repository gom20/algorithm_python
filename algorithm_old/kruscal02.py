g = int(input())
p = int(input())

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

parent = [0]*(g+1)
for i in range(g+1):
    parent[i] = i

for i in range(1, p+1):
    possible = int(input())
    if i == 1:
        prev = possible
        if g == 1:
            print(i)
            break
    else:
        docking = False
        for j in range(possible, 0, -1):
            if find_parent(parent, prev) != find_parent(parent, j):
                union(parent, prev, j)
                docking = True
                break
        if not docking:
            print(i-1)
            break
