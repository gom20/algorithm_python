# 시각
# count = 0
# n = int(input())
# for i in range(n+1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)


# 상하좌우
# n = int(input())
# dxy = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
#
# data = list(input().split())
# x, y = 1, 1
# for direction in data:
#     dir = dxy.get(direction)
#     nx = x + dir[0]
#     ny = y + dir[1]
#     if nx <= 0 or ny <= 0 or nx > n or ny > n:
#         continue
#     x = nx
#     y = ny
#
# print(x, y)


# 1이 될 때까찌
# n, k = map(int, input().split())
#
# cnt = 0
# while n > 1:
#     if n%k == 0:
#         n = n/k
#         cnt += 1
#     else:
#         if n//k > 1:
#             target = n - (n//k)*k
#             n = n-target
#             cnt += target
#         else:
#             n = n-1
#             cnt += 1
#
# print(int(cnt))


# 숫자카드게임
# result = 0
# n, m = map(int, input().split())
# for i in range(n):
#     data = list(map(int, input().split()))
#     data.sort()
#     result = max(result, data[0])
#
# print(result)

# 큰 수의 법칙
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))
#
# data.sort(reverse=True)
#
# cnt = m//(k+1)
# remained_cnt = m%(k+1)
# set_value = data[0]*k + data[1]
#
# print(remained_cnt*data[0] + set_value*cnt)



