# N개의 강의
import copy
from collections import deque

n = int(input())
time = [0]*n
in_degree= [0]*n
graph = [[] for _ in range(n)]

for i in range(n):
    arr  = list(map(int, input().split()))
    time[i] = arr[0]
    for j in range(1, len(arr)):
        if arr[j] != -1:
            graph[arr[j]-1].append(i)
            in_degree[i] +=1

result = copy.deepcopy(time)
q = deque()
for i in range(n):
    if in_degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for adj in graph[now]:
        result[adj] = max(result[adj], result[now] + time[adj])
        in_degree[adj] -= 1
        if in_degree[adj] == 0:
            q.append(adj)

print(result)