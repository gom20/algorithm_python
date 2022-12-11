import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
result = 0
for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0