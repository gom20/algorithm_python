n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 8 5
# 1 5 4 3 2 4 5 2

arr.sort()
# 1 2 2 3 4 4 5 5

count = [0]*(m+1)
for weight in arr:
    count[weight] += 1

rs = 0
index = 0
for i in range(n):
    if i < index:
        continue
    weight = arr[i]
    if i == 0:
        index = count[weight]
    else:
        index += count[weight]

    print(count[weight], len(arr)-index)
    rs += count[weight] * (len(arr)-index)

print(rs)