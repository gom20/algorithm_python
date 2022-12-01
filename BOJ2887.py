import sys
input = sys.stdin.readline

n = int(input())
arr = [[0]*3 for _ in range(n)]

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

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = data[j]

arr_x = []
arr_y = []
arr_z = []

for i in range(n):
    for j in range(3):
        if j == 0:
            arr_x.append((arr[i][j], i))
        if j == 1:
            arr_y.append((arr[i][j], i))
        if j == 2:
            arr_z.append((arr[i][j], i))

arr_x.sort()
arr_y.sort()
arr_z.sort()

edges = []
for i in range(1, n):
    edges.append((abs(arr_x[i][0] - arr_x[i - 1][0]), arr_x[i][1], arr_x[i-1][1]))
    edges.append((abs(arr_y[i][0] - arr_y[i - 1][0]), arr_y[i][1], arr_y[i-1][1]))
    edges.append((abs(arr_z[i][0] - arr_z[i - 1][0]), arr_z[i][1], arr_z[i-1][1]))

edges.sort()

minimum_cost = 0
for edge in edges:
    cost, a, b, = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        minimum_cost += cost

print(minimum_cost)
