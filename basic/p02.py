

n, m = map(int, input().split())
answer = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    answer = max(min(arr), answer)

print(answer)
    