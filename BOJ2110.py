import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

def get_possible_count(array, distance):
    count = 1
    prev = array[0]
    for i in range(1, len(array)):
        if array[i] - prev >= distance:
            prev = array[i]
            count += 1
    return count

def binary_search(start, end, array):
    global c
    result = 0
    while start <= end:
        mid = (start+end)//2
        if get_possible_count(array, mid) >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    return result

print(binary_search(1, arr[n-1]-arr[0], arr))
