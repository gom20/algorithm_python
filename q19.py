import sys
input = sys.stdin.readline;
sys.setrecursionlimit(10**6)

n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))

maxResult = -1e9
minResult = 1e9

def dfs(num, nIdx, oIdx, nums, opers):
    global maxResult, minResult, n
    if nIdx > 0:
        if oIdx == 0:
            num += nums[nIdx]
        elif oIdx == 1:
            num -= nums[nIdx]
        elif oIdx == 2:
            num *= nums[nIdx]
        elif oIdx == 3:
            if num < 0:
                num = (abs(num)//nums[nIdx])*-1
            else:
                num = num//nums[nIdx]

    if nIdx == n-1:
        maxResult = max(maxResult, num)
        minResult = min(minResult, num)
        return
    for j in range(len(opers)):
        if opers[j] == 0:
            continue
        opers[j] = opers[j]-1
        dfs(num, nIdx+1, j, nums, opers)
        opers[j] = opers[j]+1

dfs(nums[0], 0, 0, nums, opers)
print(maxResult)
print(minResult)