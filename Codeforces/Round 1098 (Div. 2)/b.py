'''
3 1 2 2
0: 1 2 -
1: caught

2

'''
q = int(input())
for _ in range (q):
    inp = input().split()
    if int(inp[0]) <= 3:
        print(1)
        continue
    direct = abs(int(inp[1]) - int(inp[2]))
    roundabout = int(inp[0]) - direct
    print(int(inp[3]) + min(direct, roundabout))
