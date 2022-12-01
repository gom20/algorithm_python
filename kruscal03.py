n, m = map(int, input().split())

parents = [0]*(n+1)
for i in range(n+1):
    parents[i] = i

def find_parent(x):
    global parents
    parent = parents[x]
    if not parents[x] == x:
        parent = find_parent(parents[x])
    return parent

def union(a, b):
    global parents
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            if find_parent(i+1) != find_parent(j+1):
                union(i+1, j+1)

plans = list(map(int, input().split()))
plans.insert(0, 0)
bPossible = True
now = find_parent(plans[1])
for i in range(1, m+1):
    if now != find_parent(plans[i]):
        bPossible = False
        break

if bPossible:
    print('YES')
else:
    print('NO')
