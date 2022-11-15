# 4 6
# 19 15 10 17

# 떡 4개, 자른 떡의 길이가 적어도 6이상 이어야 함

def binary_search(array, target, start, end):
    result = 0
    while start <= end:
        mid = (start+end)//2
        totalLength = getTotalLength(array, mid)
        print(mid, totalLength)
        if totalLength == target:
            return mid
        elif totalLength >= target:
            result = mid
            start = mid+1
        else:
            end = mid-1

    return result

def getTotalLength(array, h):
    result = 0
    for item in array:
        if item > h:
            result += item-h
    return result

n, m = map(int, input().split())
array = list(map(int, input().split()))

print(binary_search(array, m, 0, max(array)))
