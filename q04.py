n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(n):
    if i == 0:
        prev_cnt = 1
        prev = arr[i]
    else:
        if prev == arr[i]:
            prev_cnt += 1
        else:
            result += prev_cnt * (n-i)
            prev = arr[i]
            prev_cnt = 1

print(result)