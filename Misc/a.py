t = int(input())

for tt in range (t):
    aaa = input().split()
    n = int(aaa[0])
    k = int(aaa[1])
    s = input()

    sleep = [0] * n
    for i in range (len(s)):
        if s[i] == '1':
            for j in range(i, min(i+k+1, n)):
                sleep[j]=1
    print(sleep.count(0))

