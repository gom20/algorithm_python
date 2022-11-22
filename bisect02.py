n = int(input())

arr = list(map(int, input().split()))

def binary_search(start, end, array):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] < mid:
            start = mid + 1
        elif arr[mid] > mid:
            end = mid - 1
        else:
            return mid
    return None

rs = binary_search(0, len(arr)-1, arr)
if rs == None:
    print(-1)
else :
    print(rs)

