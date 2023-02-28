# 1 2 2 2 3


n = int(input())
arr = list(map(int, input().split()))

arr.sort()

group_count = 0
count = 0
for i in arr:
    count += 1
    if i >= count:
        count = 0
        group_count += 1

print(group_count)
