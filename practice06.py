# Sort

# 선택 정렬
# 가장 작은 것을 선택해서 앞으로 갖고 온다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#         array[i], array[min_index] = array[min_index], array[i]
# print(array)

# 삽입정렬
# 앞에 이미 정렬되어있다고 가정

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break
# print(array)

# 퀵정렬
# 피벗이 사용됨
# 첫번쨰 원소 기준으로, 왼쪽에서부터 피봇보다 큰것 오른쪽은 피봇보다 작은거 찾아나가다가
# 엇갈리는 지점의 작은 수와 피봇의 위치 변경


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))