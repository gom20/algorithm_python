print(ord('A'))
print(ord('1'))
print(ord('9'))

alphabet = []
number = 0
S = input()

for s in S:
    if ord(s) < ord('A'):
        number += int(s)
    else:
        alphabet.append(s)

alphabet.sort()
rs = ''
for s in alphabet:
    rs += s

print(rs + str(number))