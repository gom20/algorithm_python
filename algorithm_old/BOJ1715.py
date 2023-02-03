import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while len(q) >= 2:
    prev = heapq.heappop(q)
    cur = heapq.heappop(q)
    # print(prev, cur)
    result += prev + cur
    new = prev + cur
    heapq.heappush(q, new)

print(result)