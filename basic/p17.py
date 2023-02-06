n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort();

def get_length(array, mid):
    length = 0
    for i in range(n-1, 0, -1):
        if array[i] > mid:
            length += array[i] - mid
        else:
            break
    return length

def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        total_length = get_length(array, mid)
        if total_length == target:
            return mid
        elif total_length < target:
            end = mid -1
        else:
            start = mid + 1
            result = start
    return result

print(binary_search(arr, 0, arr[n-1], m))
