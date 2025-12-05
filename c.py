t = int(input())

for tt in range (t):
    aaa = input().split()
    n = int(aaa[0])
    k = int(aaa[1])
    a = list({int(x) for x in input().split()})

    a2 = list(a.copy())
    a2.sort()
    b=[]
    removed = set()

    still_working = True

    for i in range(len(a2)):
        if a2[i] in removed:
            continue
        divisor = a2[i]
        b.append(divisor)
        for j in range(1, k // divisor + 1):
            found = False
            for x in range(i, len(a2)):
                if a2[x] == divisor*j:
                    found = True
                    removed.add(divisor * j)
                    break
            if not found:
                still_working = False
        if not still_working:
            break

    if not still_working:
        print(-1)
    else:
        print(len(b))
        for x in b:
            print(x, end=" ")
        print(" ")
