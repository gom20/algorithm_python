from collections import deque
n = int(input())
in_degree = [0]*(n+1)
time = [0]*(n+1)
result = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    data = list(map(int, input().split()))
    for j in range(len(data)-1):
        if j == 0:
            time[i] = data[j]
        elif data[j] == -1:
            continue
        else:
            graph[data[j]].append(i)
            in_degree[i] += 1

def topology_sort(graph, time, in_degree):
    global n
    que = deque()
    for i in range(1, n+1):
       if in_degree[i] == 0:
           result[i] = time[i]
           que.append((i, time[i]))

    while que:
        node, acc_time = que.popleft()
        for adj in graph[node]:
            in_degree[adj] -= 1
            result[adj] = max(result[adj], acc_time + time[adj])
            if in_degree[adj] == 0:
                que.append((adj, result[adj]))

topology_sort(graph, time, in_degree)

print(result)