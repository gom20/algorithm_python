N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A) # 오름차순
B = sorted(B, reverse=True) # 내림차순
print(A)
print(B)

# 최대 K번 바꿔치기
cnt = 0
for i in range(N):
    if cnt == K:
        break
    elif A[i] < B[i]:
        A[i] = B[i]
        cnt += 1
    else:
        break

print(sum(A))
