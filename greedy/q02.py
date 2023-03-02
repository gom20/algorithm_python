num = input();

n = int(num[0])
for i in range(1, len(num)):
    next = int(num[i])
    if n == 0 or next == 0 :
        n += next
    elif n == 1 or next == 1:
        n += next
    else:
        n *= next

print(n)

