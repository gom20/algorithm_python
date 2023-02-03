s = input()
num = 0
arr = []
for i in range(len(s)):
    if not s[i].isalpha():
       num += int(s[i])
    else:
       arr.append(s[i])

arr.sort()
ss = ''
ss = ss.join(arr)
if num != 0:
    ss += str(num)
print(ss)
