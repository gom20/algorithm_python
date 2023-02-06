n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

mok = m/(k+1)
nmg = m%(k+1)
print(int((arr[0]*k + arr[1])*mok + arr[0]*nmg))
