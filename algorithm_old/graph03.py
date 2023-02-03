n, m = map(int, input().split())

orders = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    orders[a][b] = 1
    orders[b][a] = -1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if orders[i][j] == 1 or (orders[i][k] == 1 and orders[k][j] == 1):
                orders[i][j] = 1
            else:
                if orders[i][j] == -1 or (orders[i][k] == -1 and orders[k][j] == -1):
                    orders[i][j] = -1

able_order_count = 0
for i in range(1, n+1):
    unknown_count = 0
    for j in range(1, n+1):
        if orders[i][j] == 0:
            unknown_count += 1
    if unknown_count == 1:
        able_order_count += 1

print(able_order_count)