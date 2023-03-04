s = input()

arr = []
num = 0
for i in range(len(s)):
    if  48 <= ord(s[i]) <= 57:
        num += int(s[i])
    else:
        arr.append(s[i])

arr.sort()
result =''
for i in range(len(arr) ):
    result += arr[i]

result += str(num)

print(result)