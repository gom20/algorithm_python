

# 00시 00분 00초 ~ N시 59분 59초까지 3이 포함된 시각 count

h = int(input())

count = 0
for i in range(h+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(i) + str(m) + str(s):
                count +=1

print(count)