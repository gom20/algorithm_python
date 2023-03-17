from collections import deque;

t = int(input())

prev = [(0, -1), (-1, -1), (1, -1)]

for _ in range(t):
    n, m = map(int, input().split())
    graph = [[0]*(m+1) for _ in range(n+1)]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    arr = list(map(int, input().split()))
    q = deque()
    for i in arr:
        q.append(i)

    for i in range(1, n+1):
        for j in range(1, m+1):
            graph[i][j] = q.popleft()

    # 1열 dp 정보 채우기
    for i in range(1, n+1):
        dp[i][1] = graph[i][1];

    # 2열 부터 이전 dp정보 이용하여 최대값 갱신
    for j in range(2, m+1):
        for i in range(1, n+1):
            for p in prev:
                pi = i + p[0]
                pj = j + p[1]
                if pi < 1 or pj < 1 or pi > n or pj > m:
                    continue
                dp[i][j] = max(graph[i][j] + dp[pi][pj], dp[i][j])

    answer = 0
    for i in range(n+1):
        answer = max(dp[i][m], answer)

    print(answer)
