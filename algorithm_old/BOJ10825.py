n = int(input())
a = []
for _ in range(n):
    data = list(input().split())
    a.append((data[0], int(data[1]), int(data[2]), int(data[3])))

result = sorted(a, key = lambda x: (-x[1], x[2], -x[3], x[0]))
for r in result:
    print(r[0])