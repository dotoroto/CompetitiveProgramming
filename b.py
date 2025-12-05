t = int(input())

for tt in range (t):
    n = int(input())
    aaa = input().split()
    red = [int(a) for a in aaa]
    aaa = input().split()
    blue = [int(a) for a in aaa]

    highest = 0
    lowest = 0

    for i in range (n):
        possible_vals = [highest - red[i], lowest - red[i], blue[i] - highest, blue[i] - lowest]
        highest = max(possible_vals)
        lowest = min(possible_vals)

    print(highest)
