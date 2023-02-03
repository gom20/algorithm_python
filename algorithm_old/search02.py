import sys

# 5
# 8 3 7 9 2
# 3
# 5 7 9


N = int(input())
input_data = sys.stdin.readline().rstrip()
array = input_data.split()
array.sort()

M = int(input())
input_data = sys.stdin.readline().rstrip()
targetArray = input_data.split()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None


for target in targetArray:
    if binary_search(array, target, 0, len(array)-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')