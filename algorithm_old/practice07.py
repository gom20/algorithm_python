# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# arr.sort(reverse=True)
# print(arr)

# n = int(input())
# arr = []
# for _ in range(n):
#     data = input().split()
#     arr.append((data[0], int(data[1])))
#
# arr.sort(key = lambda x : x[1])
#
# for x in arr:
#     print(x[0], end = ' ')

# n, k = map(int, input().split())
# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))
#
# arr1.sort()
# arr2.sort(reverse=True)
# cnt = 0
# for i in range(n):
#     if arr1[i] < arr2[i]:
#         arr1[i], arr2[i] = arr2[i], arr1[i]
#         cnt += 1
#     if cnt == k:
#         break
#
# print(sum(arr1))

