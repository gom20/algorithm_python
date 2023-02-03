# 모험가 N명
# 공포도 X인 모험가는 반드시 X명 이상의 그룹에 참여
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

rs = 0
std = 0
cur = 0
for i in range(len(arr)):
    if std == 0:
        std = arr[i]
        cur = 1

    else:
        std = arr[i]
        cur += 1
        if std == cur:
            rs += 1
            cur = 0
            std = 0

print(rs)