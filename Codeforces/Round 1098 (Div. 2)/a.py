#1 2 2 1 2 2 2 1 2 1 1


q = int(input())
for _ in range (q):
    n = int(input())
    count = 0
    c0, c1, c2 = 0, 0, 0
    inp = input().split()
    for x in inp:
        if int(x) == 0:
            c0 += 1
        elif int(x) == 1:
            c1 += 1
        else:
            c2 += 1
    count += min(c1, c2)
    count += (c1 - count) // 3 + (c2 - count) // 3
    print(count + c0)
#[0], [1, 1, 1], [1, 2], [2, 1] [2, 2, 2]
