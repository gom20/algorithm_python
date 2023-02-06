import sys

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
reqs = list(map(int, input().split()))

arr.sort()


def binary_search(start, end, target):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for req in reqs:
    if binary_search(0, n-1, req):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')









