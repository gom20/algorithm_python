import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
team = [0]*(n+1)

for i in range(n+1):
    team[i] = i

def unionTeam(team, a, b):
    a = findTeam(team, a)
    b = findTeam(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b


def findTeam(team, a):
    if team[a] == a:
        return a
    team[a] = findTeam(team, team[a])
    return team[a]

for _ in range(m):
    oper, a, b = map(int, input().rstrip().split())

    if oper == 0:
        unionTeam(team, a, b)
    if oper == 1:
        if findTeam(team, a) == findTeam(team, b):
            print('YES')
        else:
            print('NO')






