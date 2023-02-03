import itertools

n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

chickens = []
homes = []
answer = 1e9

for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(1, n+1):
        arr[i][j] = data[j-1]
        if arr[i][j] == 2:
            chickens.append((i, j))
        if arr[i][j] == 1:
            homes.append((i, j))


select_list = list(itertools.combinations(chickens, m))

for selected in select_list:
    total_dist = 0
    for home in homes:
        dist = 1e9
        hx, hy = home
        for sel in selected:
            sx, sy = sel
            dist = min(dist, abs(hx - sx) + abs(hy - sy))
        total_dist += dist
    answer = min(answer, total_dist)
print(answer)