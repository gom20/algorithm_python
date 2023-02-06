n = int(input())

count = 0
for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(s) + str(m) + str(h):
                count += 1

print(count)