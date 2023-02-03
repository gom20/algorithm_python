while True:
    values = list(map(int,input().split()))
    if values[0] == 0:
        break

    values.sort()
    if values[0]**2 + values[1]**2 == values[2]**2:
        print("right")
    else:
        print("wrong")


