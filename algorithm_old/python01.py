INF = 1e9
print(INF)
print(round(123.456, 3))
print(5**3)

# List
a = list()
print(a)
a = []
print(a)

n = 10
a = [0]*10
print(a)

a = [1, 2, 3, 4, 5]
print(a[-1])

print(a[1:4])

array = [i for i in range(20) if i%2==1]
print(array)

n = 3
m = 4
array = [[0]*m for _ in range(n)]
print(array)

#Dictionary
data = dict()
data['A'] = 'a'
data['B'] = 'b'
print(data)

if 'A' in data:
    print('yes')

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

#Set
data = set([1, 1, 2, 3, 4,55])
print(data)
#중복 제거

data = {1, 2, 2, 2, 2, 3}
print(data)
a = {1, 2, 3}
b = {2, 3, 4}
print(a|b)
print(a&b)
print(a-b)

a.add(4)
a.update([6, 4, 3])
print(a)
a.remove(4)
print(a)

score = 40
result = "Success" if score >= 80 else "Fail"

print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result= [i for i in a if i not in remove_set]
print(result)
