n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split())) # +,-,*,/


max_result = -1e9
min_result = 1e9

def dfs(nums, opers, total, k, s):
    global n, max_result, min_result
    if k == n:
        # print(s, total)
        max_result = max(total, max_result)
        min_result = min(total, min_result)

    for i in range(len(opers)):
        temp = ''
        temp_total = total
        if opers[i] > 0:
            if i == 0:
                temp = s + '+' + str(nums[k])
                temp_total += nums[k]
            if i == 1:
                temp = s + '-' + str(nums[k])
                temp_total -= nums[k]
            if i == 2:
                temp = s + '*' + str(nums[k])
                temp_total *= nums[k]
            if i == 3:
                temp = s + '/' + str(nums[k])
                if temp_total < 0:
                    temp_total = abs(temp_total)
                    temp_total = int(temp_total//nums[k])
                    temp_total *= -1
                else:
                    temp_total = int(temp_total // nums[k])
            opers[i] -= 1
            # print(opers)
            dfs(nums, opers, temp_total, k+1, temp)
            opers[i] += 1

dfs(nums, opers, nums[0], 1, str(nums[0]))

print(max_result)
print(min_result)