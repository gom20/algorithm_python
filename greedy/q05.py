# 1 3 2 3 2
# 1 2 2 3 3

n, m = map(int, input().split())
cnt = [0]*(m+1)

arr = list(map(int, input().split()))
for i in arr:
    cnt[i] += 1

already_calc_cnt = 0
result = 0
for i in range(1, m+1):
    result += cnt[i] * (n - (cnt[i] + already_calc_cnt))
    already_calc_cnt += cnt[i]

print(result)
