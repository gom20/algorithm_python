n, m = map(int, input().split())
items = list(map(int, input().split()))
items.sort()

def binary_search(array, target, start, end):
    rs = None
    while start <= end:
        mid = (start+end)//2
        total_length = get_total_length(array, mid)
        print(mid, total_length)
        if total_length >= target:
            if total_length == target:
                return mid
            start = mid + 1
            rs = mid
        elif total_length < target:
            end = mid - 1
    return rs

def get_total_length(array, h):
    total_length = 0
    for i in range(len(array)-1, -1, -1):
        if array[i] <= h:
            break
        total_length += (array[i] - h)
    return total_length

print(binary_search(items, m, 0, max(items)))
