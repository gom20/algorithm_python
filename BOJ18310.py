n = int(input())
data = list(map(int, input().split()))

data.sort()

if n == 1:
    print(data[0])
elif n % 2 == 0:
    print(data[int(n//2-1)])
else:
    print(data[int(n//2)])
