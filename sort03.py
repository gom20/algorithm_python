N = int(input())

array = []

def setting(data):
    return data[1]

for _ in range(N):
    name, score = input().split()
    score = int(score)
    array.append((name, score))

result = sorted(array, key=lambda item: item[1])

for i in result:
    print(i[0], end=' ')

