import sys

n = int(input())
check_set = set()
for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        check_set.add(name)
    else:
        if name in check_set:
            check_set.remove(name)

check_set = sorted(check_set, reverse = True)

print('\n'.join(check_set))