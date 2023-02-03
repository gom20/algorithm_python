n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

arr.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 'yes'
        elif arr[mid] > target:
            end = mid-1
        elif arr[mid] < target:
            start = mid+1

    return 'no'

for target in targets:
    print(binary_search(arr, target, 0, n-1), end=' ')