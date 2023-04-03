# 1, 1, 2, 2, 2, 2, 3
n, x = map(int, input().split())
arr = list(map(int, input().split()))




def binary_search(start, end, target):
    global arr

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < target:
            end = mid-1
        elif arr[mid] > target:
            start = mid+1
        else:
            return mid

    return -1


index =  binary_search(0, n-1, x)
if index == -1:
    print(-1)
else:
    answer = 1

    lIdx = index - 1
    rIdx = index + 1
    while True:
        if lIdx >= 0 and arr[lIdx] == x:
            answer += 1
            lIdx =-1
        else:
            break

    while True:
        if rIdx < n and arr[rIdx] == x:
            answer += 1
            rIdx += 1
        else:
            break

    print(answer)