import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prev_rank = [[] for _ in range(n+1)]
    data = list(map(int, input().split()))
    for i in range(1, n+1):
        prev_rank[i] = data[i-1]

    team = [[] for _ in range(n+1)]
    in_degree = [0]*(n+1)
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            team[prev_rank[i]].append(prev_rank[j])
            in_degree[prev_rank[j]] += 1

    m = int(input())

    isContinue = True
    for _ in range(m):
        a, b = map(int, input().split())
        if b in team[a] or not a in team[b]:
            print('IMPOSSIBLE')
            isContinue = False
            break

        team[a].append(b)
        team[b].remove(a)
        in_degree[a] -= 1
        in_degree[b] += 1

    if not isContinue:
        continue

    # topology
    q = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            q.append(i)

    cnt = 0
    rank = ''
    unknown = False

    while q:
        if len(q) > 1:
            unknown = True
            break
        now = q.popleft()
        cnt += 1
        rank += str(now) + ' '
        for next in team[now]:
            in_degree[next] -= 1
            if in_degree[next] == 0:
                q.append(next)

    if unknown:
        print('?')
    elif cnt != n:
        print('IMPOSSIBLE')
    else:
        print(rank)