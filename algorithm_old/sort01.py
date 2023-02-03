array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택정렬
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
       if array[min_index] > array[j]:
           min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)

# 삽입정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)


# 퀵정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -=1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 계수정렬
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1

sort = []
for i in range(len(count)):
    for j in range(count[i]):
        sort.append(i)

print(sort)