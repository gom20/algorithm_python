n, k = map(int, input().split())

count = 0
while True:
    if n%k > 0:
        n -= 1
    else:
        n //= k
    count += 1
    if n == 1:
        break

print(count)
